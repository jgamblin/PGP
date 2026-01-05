# RAG Patterns — Retrieval-Augmented Generation

> **Purpose**: Production-ready RAG system design and implementation  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: Vector databases, chunking, retrieval, evaluation  
> **Last Updated**: 2026-01

---

## Mission

Help build **effective, scalable RAG systems** that provide accurate, relevant responses. Focus on chunking strategies, embedding selection, retrieval optimization, and answer generation.

---

## Guard Clauses

**If no RAG context provided:**
```
NO_RAG_CONTEXT

Please provide context:
- Document types (PDFs, code, docs, etc.)
- Total corpus size
- Query patterns
- Accuracy requirements
- Or describe your RAG use case
```

**If RAG system is well-designed:**
```
RAG_SYSTEM_APPROVED

✅ RAG system review complete — production ready.

Checks performed:
- Chunking: ✓ (appropriate size, overlap, metadata)
- Embeddings: ✓ (model suitable for domain)
- Retrieval: ✓ (relevance, diversity, speed)
- Generation: ✓ (grounded, accurate, cited)

RAG system follows best practices.
```

---

## Quick Context Checklist

```
☐ Document corpus description
☐ Average document length
☐ Query types expected
☐ Latency requirements
☐ Accuracy requirements
☐ Update frequency
☐ Multi-tenancy needs
☐ Budget constraints
```

---

## Copy-Paste Prompts

### Prompt: Design RAG System
```text
Design a RAG system for:

Corpus: {{CORPUS_DESCRIPTION}}
Size: {{DOCUMENT_COUNT}} documents, {{TOTAL_SIZE}}
Update frequency: {{UPDATE_FREQ}}
Query volume: {{QUERIES_PER_DAY}}
Latency target: {{LATENCY_MS}}ms

Requirements:
- Chunking strategy
- Embedding model selection
- Vector database choice
- Retrieval strategy
- Reranking approach
- Answer generation

Generate:
1. Architecture diagram
2. Component selection with justification
3. Implementation plan
4. Cost estimation
5. Evaluation strategy
```

### Prompt: Optimize Retrieval
```text
Optimize retrieval for this RAG system:

Current performance:
- Recall@10: {{RECALL}}
- MRR: {{MRR}}
- Latency: {{LATENCY}}ms
- User satisfaction: {{SATISFACTION}}

Current setup:
{{CURRENT_CONFIG}}

Issues:
{{ISSUES}}

Recommend:
1. Chunking improvements
2. Embedding alternatives
3. Retrieval strategy changes
4. Reranking options
5. Hybrid search configuration
```

### Prompt: Review RAG Code
```text
Review this RAG implementation:

{{CODE}}

Check for:
1. **Chunking**
   - Size appropriate for content
   - Overlap strategy
   - Metadata preservation
   - Boundary handling

2. **Retrieval**
   - Query preprocessing
   - Similarity search config
   - Filtering effectiveness
   - Result diversity

3. **Generation**
   - Context formatting
   - Source attribution
   - Hallucination prevention
   - Answer quality

4. **Performance**
   - Embedding caching
   - Batch processing
   - Index optimization

Rate each: 🟢 Good | 🟡 Needs attention | 🔴 Critical issue
```

### Prompt: Evaluate RAG Quality
```text
Create an evaluation framework for this RAG system:

Domain: {{DOMAIN}}
Query types: {{QUERY_TYPES}}
Success criteria: {{CRITERIA}}

Generate:
1. Test dataset design
2. Evaluation metrics
3. Automated testing pipeline
4. Human evaluation rubric
5. Continuous monitoring plan
```

---

## RAG Architecture

### Complete Pipeline
```python
# rag_pipeline.py
from __future__ import annotations

import asyncio
import hashlib
from dataclasses import dataclass, field
from typing import Any

import numpy as np
from openai import AsyncOpenAI


@dataclass
class Document:
    """A document in the corpus."""
    id: str
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)
    embedding: list[float] | None = None


@dataclass
class Chunk:
    """A chunk of a document."""
    id: str
    document_id: str
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)
    embedding: list[float] | None = None
    
    @property
    def hash(self) -> str:
        return hashlib.sha256(self.content.encode()).hexdigest()[:16]


@dataclass
class RetrievalResult:
    """A retrieved chunk with score."""
    chunk: Chunk
    score: float
    rerank_score: float | None = None


@dataclass
class RAGResponse:
    """Response from RAG system."""
    answer: str
    sources: list[RetrievalResult]
    confidence: float
    tokens_used: int


class Chunker:
    """Split documents into chunks."""
    
    def __init__(
        self,
        chunk_size: int = 512,
        chunk_overlap: int = 50,
        separators: list[str] | None = None,
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separators = separators or ["\n\n", "\n", ". ", " "]
    
    def chunk(self, document: Document) -> list[Chunk]:
        """Split document into overlapping chunks."""
        text = document.content
        chunks = []
        
        # Try to split on semantic boundaries
        segments = self._split_on_separators(text)
        
        current_chunk = ""
        chunk_idx = 0
        
        for segment in segments:
            if len(current_chunk) + len(segment) <= self.chunk_size:
                current_chunk += segment
            else:
                if current_chunk:
                    chunks.append(self._create_chunk(
                        document, current_chunk, chunk_idx
                    ))
                    chunk_idx += 1
                    
                    # Add overlap from end of current chunk
                    overlap_start = max(0, len(current_chunk) - self.chunk_overlap)
                    current_chunk = current_chunk[overlap_start:] + segment
                else:
                    current_chunk = segment
        
        # Don't forget the last chunk
        if current_chunk:
            chunks.append(self._create_chunk(document, current_chunk, chunk_idx))
        
        return chunks
    
    def _split_on_separators(self, text: str) -> list[str]:
        """Split text on semantic separators."""
        segments = [text]
        
        for sep in self.separators:
            new_segments = []
            for segment in segments:
                parts = segment.split(sep)
                for i, part in enumerate(parts):
                    if i < len(parts) - 1:
                        new_segments.append(part + sep)
                    else:
                        new_segments.append(part)
            segments = new_segments
        
        return [s for s in segments if s.strip()]
    
    def _create_chunk(self, doc: Document, content: str, idx: int) -> Chunk:
        """Create a chunk from content."""
        return Chunk(
            id=f"{doc.id}_chunk_{idx}",
            document_id=doc.id,
            content=content.strip(),
            metadata={
                **doc.metadata,
                "chunk_index": idx,
            },
        )


class EmbeddingService:
    """Generate embeddings for text."""
    
    def __init__(
        self,
        model: str = "text-embedding-3-small",
        dimensions: int = 1536,
    ):
        self.model = model
        self.dimensions = dimensions
        self._client = AsyncOpenAI()
        self._cache: dict[str, list[float]] = {}
    
    async def embed(self, text: str) -> list[float]:
        """Embed a single text."""
        cache_key = hashlib.sha256(text.encode()).hexdigest()
        
        if cache_key in self._cache:
            return self._cache[cache_key]
        
        response = await self._client.embeddings.create(
            model=self.model,
            input=text,
            dimensions=self.dimensions,
        )
        
        embedding = response.data[0].embedding
        self._cache[cache_key] = embedding
        return embedding
    
    async def embed_batch(
        self, 
        texts: list[str], 
        batch_size: int = 100,
    ) -> list[list[float]]:
        """Embed multiple texts efficiently."""
        embeddings = []
        
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            
            response = await self._client.embeddings.create(
                model=self.model,
                input=batch,
                dimensions=self.dimensions,
            )
            
            batch_embeddings = [item.embedding for item in response.data]
            embeddings.extend(batch_embeddings)
        
        return embeddings


class VectorStore:
    """Simple in-memory vector store (replace with Pinecone/Weaviate/etc.)"""
    
    def __init__(self):
        self._chunks: dict[str, Chunk] = {}
        self._embeddings: dict[str, np.ndarray] = {}
    
    def add(self, chunks: list[Chunk]) -> None:
        """Add chunks to the store."""
        for chunk in chunks:
            if chunk.embedding is None:
                raise ValueError(f"Chunk {chunk.id} has no embedding")
            
            self._chunks[chunk.id] = chunk
            self._embeddings[chunk.id] = np.array(chunk.embedding)
    
    def search(
        self,
        query_embedding: list[float],
        k: int = 10,
        filter_metadata: dict[str, Any] | None = None,
    ) -> list[tuple[Chunk, float]]:
        """Search for similar chunks."""
        query_vec = np.array(query_embedding)
        
        results = []
        for chunk_id, embedding in self._embeddings.items():
            chunk = self._chunks[chunk_id]
            
            # Apply metadata filter
            if filter_metadata:
                if not all(
                    chunk.metadata.get(k) == v 
                    for k, v in filter_metadata.items()
                ):
                    continue
            
            # Cosine similarity
            similarity = np.dot(query_vec, embedding) / (
                np.linalg.norm(query_vec) * np.linalg.norm(embedding)
            )
            results.append((chunk, float(similarity)))
        
        # Sort by similarity
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:k]


class Reranker:
    """Rerank results using cross-encoder or LLM."""
    
    def __init__(self, model: str = "gpt-4o-mini"):
        self.model = model
        self._client = AsyncOpenAI()
    
    async def rerank(
        self,
        query: str,
        results: list[tuple[Chunk, float]],
        top_k: int = 5,
    ) -> list[RetrievalResult]:
        """Rerank results using LLM scoring."""
        if not results:
            return []
        
        # Build reranking prompt
        chunks_text = "\n\n".join([
            f"[{i}] {chunk.content[:500]}"
            for i, (chunk, _) in enumerate(results)
        ])
        
        response = await self._client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": """Score each passage's relevance to the query from 0-10.
Return only a JSON array of scores in order, like: [8, 3, 9, 2, 7]""",
                },
                {
                    "role": "user",
                    "content": f"Query: {query}\n\nPassages:\n{chunks_text}",
                },
            ],
            temperature=0,
        )
        
        try:
            import json
            scores = json.loads(response.choices[0].message.content)
        except:
            # Fallback to original scores
            scores = [score for _, score in results]
        
        # Combine with original results
        reranked = []
        for i, (chunk, original_score) in enumerate(results):
            rerank_score = scores[i] if i < len(scores) else 0
            reranked.append(RetrievalResult(
                chunk=chunk,
                score=original_score,
                rerank_score=rerank_score / 10,  # Normalize to 0-1
            ))
        
        # Sort by rerank score
        reranked.sort(key=lambda x: x.rerank_score or 0, reverse=True)
        return reranked[:top_k]


class RAGPipeline:
    """Complete RAG pipeline."""
    
    def __init__(
        self,
        chunker: Chunker | None = None,
        embedding_service: EmbeddingService | None = None,
        vector_store: VectorStore | None = None,
        reranker: Reranker | None = None,
        generation_model: str = "gpt-4o",
    ):
        self.chunker = chunker or Chunker()
        self.embedding_service = embedding_service or EmbeddingService()
        self.vector_store = vector_store or VectorStore()
        self.reranker = reranker or Reranker()
        self.generation_model = generation_model
        self._client = AsyncOpenAI()
    
    async def ingest(self, documents: list[Document]) -> int:
        """Ingest documents into the RAG system."""
        all_chunks = []
        
        for doc in documents:
            chunks = self.chunker.chunk(doc)
            all_chunks.extend(chunks)
        
        # Batch embed all chunks
        contents = [chunk.content for chunk in all_chunks]
        embeddings = await self.embedding_service.embed_batch(contents)
        
        for chunk, embedding in zip(all_chunks, embeddings):
            chunk.embedding = embedding
        
        self.vector_store.add(all_chunks)
        return len(all_chunks)
    
    async def query(
        self,
        question: str,
        k: int = 5,
        filter_metadata: dict[str, Any] | None = None,
        use_reranking: bool = True,
    ) -> RAGResponse:
        """Answer a question using RAG."""
        # Embed query
        query_embedding = await self.embedding_service.embed(question)
        
        # Retrieve candidates
        candidates = self.vector_store.search(
            query_embedding,
            k=k * 2 if use_reranking else k,
            filter_metadata=filter_metadata,
        )
        
        if not candidates:
            return RAGResponse(
                answer="I don't have enough information to answer this question.",
                sources=[],
                confidence=0.0,
                tokens_used=0,
            )
        
        # Rerank
        if use_reranking:
            results = await self.reranker.rerank(question, candidates, k)
        else:
            results = [
                RetrievalResult(chunk=chunk, score=score)
                for chunk, score in candidates[:k]
            ]
        
        # Generate answer
        context = "\n\n---\n\n".join([
            f"Source [{i+1}]: {r.chunk.content}"
            for i, r in enumerate(results)
        ])
        
        response = await self._client.chat.completions.create(
            model=self.generation_model,
            messages=[
                {
                    "role": "system",
                    "content": """Answer the question based ONLY on the provided sources.
If the sources don't contain enough information, say so.
Cite sources using [1], [2], etc.""",
                },
                {
                    "role": "user",
                    "content": f"Sources:\n{context}\n\nQuestion: {question}",
                },
            ],
            temperature=0.3,
        )
        
        answer = response.choices[0].message.content or ""
        
        # Calculate confidence based on retrieval scores
        avg_score = sum(r.score for r in results) / len(results)
        
        return RAGResponse(
            answer=answer,
            sources=results,
            confidence=avg_score,
            tokens_used=response.usage.total_tokens,
        )
```

---

## Chunking Strategies

### Semantic Chunking
```python
# semantic_chunker.py
import re
from dataclasses import dataclass


@dataclass
class SemanticChunk:
    """Chunk with semantic boundaries."""
    content: str
    chunk_type: str  # "paragraph", "section", "code", etc.
    metadata: dict


class SemanticChunker:
    """Chunk documents respecting semantic boundaries."""
    
    def __init__(
        self,
        max_chunk_size: int = 1000,
        min_chunk_size: int = 100,
    ):
        self.max_chunk_size = max_chunk_size
        self.min_chunk_size = min_chunk_size
    
    def chunk_markdown(self, content: str) -> list[SemanticChunk]:
        """Chunk markdown document by headers and sections."""
        chunks = []
        
        # Split by headers
        sections = re.split(r"(^#{1,6}\s.+$)", content, flags=re.MULTILINE)
        
        current_header = ""
        current_content = ""
        
        for i, section in enumerate(sections):
            if re.match(r"^#{1,6}\s", section):
                # This is a header
                if current_content.strip():
                    chunks.extend(self._split_large_section(
                        current_content,
                        header=current_header,
                    ))
                current_header = section.strip()
                current_content = ""
            else:
                current_content += section
        
        # Don't forget the last section
        if current_content.strip():
            chunks.extend(self._split_large_section(
                current_content,
                header=current_header,
            ))
        
        return chunks
    
    def chunk_code(self, content: str, language: str) -> list[SemanticChunk]:
        """Chunk code files by functions/classes."""
        chunks = []
        
        # Language-specific patterns
        patterns = {
            "python": r"^(class\s+\w+|def\s+\w+|async\s+def\s+\w+)",
            "javascript": r"^(function\s+\w+|class\s+\w+|const\s+\w+\s*=|export\s+)",
            "typescript": r"^(function\s+\w+|class\s+\w+|const\s+\w+\s*=|export\s+|interface\s+\w+)",
        }
        
        pattern = patterns.get(language, r"^(function|class|def)\s+")
        
        # Split on function/class boundaries
        parts = re.split(f"({pattern})", content, flags=re.MULTILINE)
        
        current_chunk = ""
        for part in parts:
            if re.match(pattern, part, re.MULTILINE):
                if current_chunk.strip():
                    chunks.append(SemanticChunk(
                        content=current_chunk.strip(),
                        chunk_type="code",
                        metadata={"language": language},
                    ))
                current_chunk = part
            else:
                current_chunk += part
        
        if current_chunk.strip():
            chunks.append(SemanticChunk(
                content=current_chunk.strip(),
                chunk_type="code",
                metadata={"language": language},
            ))
        
        return chunks
    
    def _split_large_section(
        self,
        content: str,
        header: str = "",
    ) -> list[SemanticChunk]:
        """Split sections that exceed max size."""
        if len(content) <= self.max_chunk_size:
            return [SemanticChunk(
                content=f"{header}\n{content}".strip() if header else content.strip(),
                chunk_type="section",
                metadata={"header": header},
            )]
        
        chunks = []
        paragraphs = content.split("\n\n")
        
        current_chunk = header + "\n" if header else ""
        
        for para in paragraphs:
            if len(current_chunk) + len(para) > self.max_chunk_size:
                if current_chunk.strip():
                    chunks.append(SemanticChunk(
                        content=current_chunk.strip(),
                        chunk_type="paragraph",
                        metadata={"header": header},
                    ))
                current_chunk = para + "\n\n"
            else:
                current_chunk += para + "\n\n"
        
        if current_chunk.strip():
            chunks.append(SemanticChunk(
                content=current_chunk.strip(),
                chunk_type="paragraph",
                metadata={"header": header},
            ))
        
        return chunks
```

### Parent-Child Chunking
```python
# parent_child_chunker.py
@dataclass
class ParentChildChunk:
    """Chunk with parent reference for context expansion."""
    id: str
    content: str
    parent_id: str | None
    parent_content: str | None
    children_ids: list[str]


class ParentChildChunker:
    """Create hierarchical chunks for context expansion."""
    
    def __init__(
        self,
        parent_chunk_size: int = 2000,
        child_chunk_size: int = 400,
        child_overlap: int = 50,
    ):
        self.parent_chunk_size = parent_chunk_size
        self.child_chunk_size = child_chunk_size
        self.child_overlap = child_overlap
    
    def chunk(self, document_id: str, content: str) -> list[ParentChildChunk]:
        """Create parent and child chunks."""
        chunks = []
        
        # Create parent chunks first
        parent_chunks = self._create_parents(document_id, content)
        
        # Create children for each parent
        for parent in parent_chunks:
            children = self._create_children(parent)
            parent.children_ids = [c.id for c in children]
            chunks.append(parent)
            chunks.extend(children)
        
        return chunks
    
    def _create_parents(
        self, 
        doc_id: str, 
        content: str,
    ) -> list[ParentChildChunk]:
        """Create large parent chunks."""
        parents = []
        
        for i in range(0, len(content), self.parent_chunk_size):
            chunk_content = content[i:i + self.parent_chunk_size]
            parents.append(ParentChildChunk(
                id=f"{doc_id}_parent_{len(parents)}",
                content=chunk_content,
                parent_id=None,
                parent_content=None,
                children_ids=[],
            ))
        
        return parents
    
    def _create_children(
        self,
        parent: ParentChildChunk,
    ) -> list[ParentChildChunk]:
        """Create small child chunks from parent."""
        children = []
        content = parent.content
        
        start = 0
        child_idx = 0
        
        while start < len(content):
            end = min(start + self.child_chunk_size, len(content))
            chunk_content = content[start:end]
            
            children.append(ParentChildChunk(
                id=f"{parent.id}_child_{child_idx}",
                content=chunk_content,
                parent_id=parent.id,
                parent_content=parent.content,
                children_ids=[],
            ))
            
            start = end - self.child_overlap
            child_idx += 1
        
        return children
```

---

## Retrieval Strategies

### Hybrid Search
```python
# hybrid_search.py
from dataclasses import dataclass
from typing import Any


@dataclass
class HybridResult:
    """Result from hybrid search."""
    chunk_id: str
    content: str
    vector_score: float
    keyword_score: float
    combined_score: float


class HybridRetriever:
    """Combine vector and keyword search."""
    
    def __init__(
        self,
        vector_weight: float = 0.7,
        keyword_weight: float = 0.3,
    ):
        self.vector_weight = vector_weight
        self.keyword_weight = keyword_weight
    
    def search(
        self,
        query: str,
        vector_results: list[tuple[str, str, float]],  # (id, content, score)
        keyword_results: list[tuple[str, str, float]],
        k: int = 10,
    ) -> list[HybridResult]:
        """Combine vector and keyword search results."""
        # Normalize scores
        vector_scores = self._normalize_scores(vector_results)
        keyword_scores = self._normalize_scores(keyword_results)
        
        # Combine results
        all_ids = set(r[0] for r in vector_results) | set(r[0] for r in keyword_results)
        
        combined = []
        for chunk_id in all_ids:
            v_score = vector_scores.get(chunk_id, 0)
            k_score = keyword_scores.get(chunk_id, 0)
            
            content = next(
                (r[1] for r in vector_results if r[0] == chunk_id),
                next((r[1] for r in keyword_results if r[0] == chunk_id), ""),
            )
            
            combined_score = (
                self.vector_weight * v_score +
                self.keyword_weight * k_score
            )
            
            combined.append(HybridResult(
                chunk_id=chunk_id,
                content=content,
                vector_score=v_score,
                keyword_score=k_score,
                combined_score=combined_score,
            ))
        
        # Sort by combined score
        combined.sort(key=lambda x: x.combined_score, reverse=True)
        return combined[:k]
    
    def _normalize_scores(
        self,
        results: list[tuple[str, str, float]],
    ) -> dict[str, float]:
        """Normalize scores to 0-1 range."""
        if not results:
            return {}
        
        scores = [r[2] for r in results]
        min_score = min(scores)
        max_score = max(scores)
        
        if max_score == min_score:
            return {r[0]: 1.0 for r in results}
        
        return {
            r[0]: (r[2] - min_score) / (max_score - min_score)
            for r in results
        }
```

### Query Expansion
```python
# query_expansion.py
from openai import AsyncOpenAI


class QueryExpander:
    """Expand queries for better retrieval."""
    
    def __init__(self, model: str = "gpt-4o-mini"):
        self.model = model
        self._client = AsyncOpenAI()
    
    async def expand(self, query: str, n_variations: int = 3) -> list[str]:
        """Generate query variations."""
        response = await self._client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": f"""Generate {n_variations} alternative phrasings of the query.
Each should capture the same intent but use different words.
Return one variation per line, no numbering.""",
                },
                {"role": "user", "content": query},
            ],
            temperature=0.7,
        )
        
        variations = response.choices[0].message.content.strip().split("\n")
        return [query] + [v.strip() for v in variations if v.strip()]
    
    async def decompose(self, query: str) -> list[str]:
        """Decompose complex query into sub-queries."""
        response = await self._client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": """Break down the query into simpler sub-questions.
If the query is already simple, return it as-is.
Return one sub-question per line.""",
                },
                {"role": "user", "content": query},
            ],
            temperature=0.3,
        )
        
        sub_queries = response.choices[0].message.content.strip().split("\n")
        return [q.strip() for q in sub_queries if q.strip()]
```

---

## Vector Database Configs

### Pinecone
```python
# pinecone_store.py
from pinecone import Pinecone, ServerlessSpec


def create_pinecone_index(
    index_name: str,
    dimension: int = 1536,
    metric: str = "cosine",
):
    """Create a Pinecone index."""
    pc = Pinecone()
    
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=dimension,
            metric=metric,
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1",
            ),
        )
    
    return pc.Index(index_name)


async def upsert_chunks(
    index,
    chunks: list[Chunk],
    namespace: str = "",
    batch_size: int = 100,
):
    """Upsert chunks to Pinecone."""
    vectors = []
    
    for chunk in chunks:
        vectors.append({
            "id": chunk.id,
            "values": chunk.embedding,
            "metadata": {
                "content": chunk.content[:1000],  # Pinecone metadata limit
                "document_id": chunk.document_id,
                **chunk.metadata,
            },
        })
    
    # Batch upsert
    for i in range(0, len(vectors), batch_size):
        batch = vectors[i:i + batch_size]
        index.upsert(vectors=batch, namespace=namespace)
```

### Weaviate
```python
# weaviate_store.py
import weaviate
from weaviate.classes.config import Configure, Property, DataType


def create_weaviate_collection(
    client: weaviate.Client,
    collection_name: str = "Document",
):
    """Create a Weaviate collection."""
    client.collections.create(
        name=collection_name,
        vectorizer_config=Configure.Vectorizer.text2vec_openai(
            model="text-embedding-3-small",
        ),
        properties=[
            Property(name="content", data_type=DataType.TEXT),
            Property(name="document_id", data_type=DataType.TEXT),
            Property(name="chunk_index", data_type=DataType.INT),
        ],
    )


async def search_weaviate(
    client: weaviate.Client,
    query: str,
    collection_name: str = "Document",
    limit: int = 10,
    filters: dict | None = None,
):
    """Search Weaviate collection."""
    collection = client.collections.get(collection_name)
    
    response = collection.query.near_text(
        query=query,
        limit=limit,
        filters=filters,
        return_metadata=["distance"],
    )
    
    return [
        {
            "content": obj.properties["content"],
            "score": 1 - obj.metadata.distance,  # Convert distance to similarity
            "metadata": obj.properties,
        }
        for obj in response.objects
    ]
```

### pgvector
```python
# pgvector_store.py
import asyncpg
import numpy as np


async def setup_pgvector(conn: asyncpg.Connection):
    """Set up pgvector extension and table."""
    await conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
    
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS chunks (
            id TEXT PRIMARY KEY,
            document_id TEXT NOT NULL,
            content TEXT NOT NULL,
            embedding vector(1536),
            metadata JSONB DEFAULT '{}',
            created_at TIMESTAMPTZ DEFAULT NOW()
        )
    """)
    
    await conn.execute("""
        CREATE INDEX IF NOT EXISTS chunks_embedding_idx 
        ON chunks USING ivfflat (embedding vector_cosine_ops)
        WITH (lists = 100)
    """)


async def search_pgvector(
    conn: asyncpg.Connection,
    query_embedding: list[float],
    limit: int = 10,
    filter_document_id: str | None = None,
) -> list[dict]:
    """Search pgvector for similar chunks."""
    embedding_str = f"[{','.join(map(str, query_embedding))}]"
    
    query = """
        SELECT 
            id,
            document_id,
            content,
            metadata,
            1 - (embedding <=> $1::vector) as similarity
        FROM chunks
        WHERE ($2::text IS NULL OR document_id = $2)
        ORDER BY embedding <=> $1::vector
        LIMIT $3
    """
    
    rows = await conn.fetch(query, embedding_str, filter_document_id, limit)
    
    return [
        {
            "id": row["id"],
            "document_id": row["document_id"],
            "content": row["content"],
            "metadata": row["metadata"],
            "score": row["similarity"],
        }
        for row in rows
    ]
```

---

## Evaluation Framework

```python
# rag_evaluation.py
from dataclasses import dataclass
from typing import Any
import asyncio


@dataclass
class EvalQuestion:
    """A question for RAG evaluation."""
    question: str
    ground_truth: str
    expected_sources: list[str] | None = None


@dataclass
class EvalResult:
    """Result of evaluating a single question."""
    question: str
    answer: str
    ground_truth: str
    relevance_score: float  # Is the answer relevant?
    faithfulness_score: float  # Is it grounded in sources?
    correctness_score: float  # Is it factually correct?
    retrieval_precision: float  # Did we get the right sources?


class RAGEvaluator:
    """Evaluate RAG system performance."""
    
    def __init__(self, rag_pipeline: RAGPipeline):
        self.rag = rag_pipeline
        self._client = AsyncOpenAI()
    
    async def evaluate(
        self,
        test_set: list[EvalQuestion],
    ) -> dict[str, Any]:
        """Evaluate RAG on a test set."""
        results = []
        
        for question in test_set:
            result = await self._evaluate_single(question)
            results.append(result)
        
        # Aggregate metrics
        return {
            "num_questions": len(results),
            "avg_relevance": sum(r.relevance_score for r in results) / len(results),
            "avg_faithfulness": sum(r.faithfulness_score for r in results) / len(results),
            "avg_correctness": sum(r.correctness_score for r in results) / len(results),
            "avg_retrieval_precision": sum(r.retrieval_precision for r in results) / len(results),
            "results": results,
        }
    
    async def _evaluate_single(self, question: EvalQuestion) -> EvalResult:
        """Evaluate a single question."""
        # Get RAG response
        response = await self.rag.query(question.question)
        
        # Score relevance, faithfulness, correctness using LLM
        scores = await self._llm_judge(
            question.question,
            response.answer,
            question.ground_truth,
            [r.chunk.content for r in response.sources],
        )
        
        # Calculate retrieval precision
        if question.expected_sources:
            retrieved_ids = [r.chunk.id for r in response.sources]
            precision = len(
                set(retrieved_ids) & set(question.expected_sources)
            ) / len(question.expected_sources)
        else:
            precision = response.confidence
        
        return EvalResult(
            question=question.question,
            answer=response.answer,
            ground_truth=question.ground_truth,
            relevance_score=scores["relevance"],
            faithfulness_score=scores["faithfulness"],
            correctness_score=scores["correctness"],
            retrieval_precision=precision,
        )
    
    async def _llm_judge(
        self,
        question: str,
        answer: str,
        ground_truth: str,
        sources: list[str],
    ) -> dict[str, float]:
        """Use LLM to score answer quality."""
        response = await self._client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": """Score the answer on three dimensions (0-10):
1. Relevance: Does it answer the question?
2. Faithfulness: Is it grounded in the sources?
3. Correctness: Is it factually accurate vs ground truth?

Return JSON: {"relevance": X, "faithfulness": Y, "correctness": Z}""",
                },
                {
                    "role": "user",
                    "content": f"""Question: {question}

Answer: {answer}

Ground Truth: {ground_truth}

Sources: {sources[:3]}""",
                },
            ],
            temperature=0,
        )
        
        import json
        scores = json.loads(response.choices[0].message.content)
        
        return {
            "relevance": scores["relevance"] / 10,
            "faithfulness": scores["faithfulness"] / 10,
            "correctness": scores["correctness"] / 10,
        }
```

---

## Report Template

```markdown
# RAG System Review — {{SYSTEM_NAME}}

**Date**: {{DATE}}
**Corpus**: {{CORPUS_SIZE}} documents

## Summary

| Component | Status | Notes |
|-----------|--------|-------|
| Chunking | 🟢/🟡/🔴 | {{NOTES}} |
| Embeddings | 🟢/🟡/🔴 | {{NOTES}} |
| Retrieval | 🟢/🟡/🔴 | {{NOTES}} |
| Generation | 🟢/🟡/🔴 | {{NOTES}} |

## Performance Metrics
- Retrieval Recall@10: {{RECALL}}
- Answer Relevance: {{RELEVANCE}}
- Answer Faithfulness: {{FAITHFULNESS}}
- Avg Latency: {{LATENCY}}ms

## Issues Found
{{ISSUES}}

## Recommendations
{{RECOMMENDATIONS}}

## Implementation Plan
{{PLAN}}
```

---

## Best Practices Checklist

### Chunking
- [ ] Size appropriate for content type
- [ ] Overlap to preserve context
- [ ] Semantic boundaries respected
- [ ] Metadata preserved

### Embeddings
- [ ] Model matches domain
- [ ] Dimension appropriate for accuracy/speed
- [ ] Caching implemented
- [ ] Batch processing used

### Retrieval
- [ ] Hybrid search considered
- [ ] Reranking implemented
- [ ] Query expansion for complex queries
- [ ] Filtering available

### Generation
- [ ] Sources properly cited
- [ ] Hallucination prevention
- [ ] Confidence scoring
- [ ] Graceful no-result handling

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | No chunking strategy, wrong embedding model |
| **High** | 🟠 | No reranking, missing metadata, poor retrieval |
| **Medium** | 🟡 | No caching, suboptimal chunk sizes |
| **Low** | 🟢 | Minor tuning, documentation gaps |

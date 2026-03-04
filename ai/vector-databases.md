# Vector Databases — Embedding Storage & Retrieval

> **Purpose**: Production-ready vector database patterns and optimization  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: pgvector, Pinecone, Weaviate, Chroma, Qdrant  
> **Last Updated**: 2026-03

---

## Mission

Help implement **efficient, scalable vector storage and retrieval** for AI applications. Focus on database selection, index optimization, query patterns, and production operations.

---

## Guard Clauses

**If no vector DB context provided:**
```
NO_VECTOR_DB_CONTEXT

Please provide context:
- Use case (RAG, search, recommendations, etc.)
- Data volume (vectors count, dimensions)
- Query patterns (similarity, filtered, hybrid)
- Infrastructure constraints
- Or describe your vector database needs
```

**If vector DB is well-configured:**
```
VECTOR_DB_APPROVED

✅ Vector database review complete — production ready.

Checks performed:
- Index type: ✓ (appropriate for scale/accuracy)
- Query patterns: ✓ (efficient, batched where needed)
- Metadata: ✓ (filterable, properly indexed)
- Operations: ✓ (backup, monitoring, scaling)

Vector database follows best practices.
```

---

## Quick Context Checklist

```
☐ Vector count (current and projected)
☐ Embedding dimensions
☐ Query latency requirements
☐ Accuracy requirements (recall@k)
☐ Filter/metadata needs
☐ Update frequency
☐ Infrastructure (cloud, self-hosted)
☐ Budget constraints
```

---

## Copy-Paste Prompts

### Prompt: Select Vector Database
```text
Help me choose a vector database:

Use case: {{USE_CASE}}
Vector count: {{VECTOR_COUNT}}
Dimensions: {{DIMENSIONS}}
Query volume: {{QUERIES_PER_SECOND}}
Latency target: {{LATENCY_MS}}ms
Recall target: {{RECALL_PERCENTAGE}}%

Infrastructure:
- Cloud provider: {{CLOUD_PROVIDER}}
- Self-hosted option: {{YES_NO}}
- Budget: {{BUDGET}}

Requirements:
- Metadata filtering: {{YES_NO}}
- Hybrid search: {{YES_NO}}
- Multi-tenancy: {{YES_NO}}

Compare options and recommend the best fit.
```

### Prompt: pgvector Setup & Optimization
```text
Review/design pgvector implementation:

{{CODE_OR_SCHEMA}}

Context:
- Vector count: {{COUNT}}
- Dimensions: {{DIMENSIONS}}
- PostgreSQL version: {{VERSION}}
- Query patterns: {{PATTERNS}}

Analyze:
1. **Index Selection**
   - IVFFlat vs HNSW tradeoffs
   - Parameters (lists, m, ef_construction)
   - Build time vs query performance

2. **Schema Design**
   - Vector column type
   - Metadata columns
   - Partitioning strategy

3. **Query Optimization**
   - Distance function choice
   - Probes/ef_search tuning
   - Filtered query patterns

4. **Operations**
   - Index maintenance
   - VACUUM strategy
   - Monitoring queries
```

### Prompt: Pinecone Implementation
```text
Review/design Pinecone implementation:

{{CODE}}

Context:
- Index type: {{SERVERLESS_OR_POD}}
- Vector count: {{COUNT}}
- Dimensions: {{DIMENSIONS}}
- Namespaces: {{NAMESPACE_STRATEGY}}

Analyze:
1. **Index Configuration**
   - Pod type selection
   - Replicas and shards
   - Metric (cosine, euclidean, dotproduct)

2. **Upsert Patterns**
   - Batch size optimization
   - Metadata structure
   - Namespace organization

3. **Query Patterns**
   - Top-k selection
   - Metadata filtering
   - Sparse-dense hybrid

4. **Cost Optimization**
   - Pod sizing
   - Query efficiency
   - Storage management
```

### Prompt: Weaviate Implementation
```text
Review/design Weaviate implementation:

{{CODE_OR_SCHEMA}}

Context:
- Deployment: {{CLOUD_OR_SELF_HOSTED}}
- Object count: {{COUNT}}
- Vectorizer: {{VECTORIZER_MODULE}}
- Multi-tenancy: {{YES_NO}}

Analyze:
1. **Schema Design**
   - Class definitions
   - Property types
   - Cross-references
   - Vectorizer configuration

2. **Index Configuration**
   - HNSW parameters
   - Inverted index settings
   - BM25 configuration

3. **Query Patterns**
   - GraphQL queries
   - Hybrid search (vector + BM25)
   - Filtering and aggregation

4. **Modules**
   - Vectorizer selection
   - Reranker integration
   - Generative module
```

### Prompt: Chroma Implementation
```text
Review/design Chroma implementation:

{{CODE}}

Context:
- Mode: {{EPHEMERAL_OR_PERSISTENT}}
- Collection count: {{COUNT}}
- Embedding function: {{EMBEDDING_MODEL}}

Analyze:
1. **Setup**
   - Client configuration
   - Persistence settings
   - Embedding function

2. **Collection Design**
   - Naming conventions
   - Metadata schema
   - Distance function

3. **Operations**
   - Add/update/delete patterns
   - Query optimization
   - Batch operations

4. **Integration**
   - LangChain integration
   - Custom embedding functions
   - Error handling
```

### Prompt: Qdrant Implementation
```text
Review/design Qdrant implementation:

{{CODE}}

Context:
- Deployment: {{CLOUD_OR_SELF_HOSTED}}
- Collection size: {{VECTOR_COUNT}}
- Payload complexity: {{SIMPLE_OR_COMPLEX}}

Analyze:
1. **Collection Configuration**
   - Vector parameters
   - Distance metric
   - On-disk vs in-memory

2. **Index Optimization**
   - HNSW parameters (m, ef_construct)
   - Payload indexes
   - Quantization options

3. **Query Patterns**
   - Search with filters
   - Scroll/pagination
   - Batch queries
   - Recommendation API

4. **Advanced Features**
   - Multi-vector support
   - Sparse vectors
   - Sharding configuration
```

### Prompt: Vector DB Migration
```text
Plan vector database migration:

Current: {{CURRENT_DB}}
Target: {{TARGET_DB}}
Vector count: {{COUNT}}
Downtime tolerance: {{TOLERANCE}}

Create migration plan:
1. **Data Export**
   - Export format
   - Batch size
   - Metadata handling

2. **Schema Mapping**
   - Field mappings
   - Index translation
   - Metadata conversion

3. **Migration Strategy**
   - Parallel operation period
   - Validation approach
   - Rollback plan

4. **Cutover**
   - Traffic switching
   - Verification queries
   - Monitoring setup
```

---

## Vector Database Comparison

### Quick Selection Guide

| Database | Best For | Scale | Managed | OSS |
|----------|----------|-------|---------|-----|
| **pgvector** | PostgreSQL shops, <10M vectors | Medium | ✅ | ✅ |
| **Pinecone** | Serverless, enterprise scale | Large | ✅ | ❌ |
| **Weaviate** | Hybrid search, GraphQL | Large | ✅ | ✅ |
| **Chroma** | Local dev, prototyping | Small | ❌ | ✅ |
| **Qdrant** | High performance, filtering | Large | ✅ | ✅ |
| **Milvus** | Massive scale, GPU | Very Large | ✅ | ✅ |

### Detailed Comparison

| Feature | pgvector | Pinecone | Weaviate | Chroma | Qdrant |
|---------|----------|----------|----------|--------|--------|
| **Max Vectors** | ~10M+ | Billions | Billions | Millions | Billions |
| **Index Types** | IVFFlat, HNSW | Proprietary | HNSW | HNSW | HNSW |
| **Hybrid Search** | Manual | ✅ | ✅ (BM25) | ❌ | ✅ |
| **Filtering** | SQL WHERE | Metadata | GraphQL | Metadata | Payload |
| **Multi-tenancy** | Schemas | Namespaces | Native | Collections | Collections |
| **Quantization** | ❌ | ✅ | ✅ | ❌ | ✅ |

---

## Index Type Reference

### HNSW (Hierarchical Navigable Small World)

```python
# pgvector HNSW
CREATE INDEX ON items USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

# Query-time parameter
SET hnsw.ef_search = 100;
```

**Parameters:**
| Parameter | Default | Description | Tuning |
|-----------|---------|-------------|--------|
| `m` | 16 | Connections per layer | Higher = better recall, more memory |
| `ef_construction` | 64 | Build-time search width | Higher = better index, slower build |
| `ef_search` | 40 | Query-time search width | Higher = better recall, slower query |

**When to use:** Most production workloads, good recall/speed balance

### IVFFlat (Inverted File Index)

```python
# pgvector IVFFlat
CREATE INDEX ON items USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100);

# Query-time parameter
SET ivfflat.probes = 10;
```

**Parameters:**
| Parameter | Default | Description | Tuning |
|-----------|---------|-------------|--------|
| `lists` | - | Number of clusters | √n to n/1000 |
| `probes` | 1 | Clusters to search | Higher = better recall |

**When to use:** Large datasets, can tolerate lower recall, need fast builds

---

## pgvector Patterns

### Schema Design

```sql
-- Basic vector table
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    content TEXT NOT NULL,
    embedding vector(1536),  -- OpenAI ada-002
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Optimized index for cosine similarity
CREATE INDEX documents_embedding_idx ON documents 
USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

-- Metadata index for filtered queries
CREATE INDEX documents_metadata_idx ON documents 
USING gin (metadata jsonb_path_ops);
```

### Query Patterns

```sql
-- Basic similarity search
SELECT id, content, 1 - (embedding <=> $1) AS similarity
FROM documents
ORDER BY embedding <=> $1
LIMIT 10;

-- Filtered similarity search
SELECT id, content, 1 - (embedding <=> $1) AS similarity
FROM documents
WHERE metadata->>'category' = 'technical'
  AND created_at > NOW() - INTERVAL '30 days'
ORDER BY embedding <=> $1
LIMIT 10;

-- Hybrid search with full-text
SELECT id, content,
       (0.7 * (1 - (embedding <=> $1))) + 
       (0.3 * ts_rank(to_tsvector(content), plainto_tsquery($2))) AS score
FROM documents
WHERE to_tsvector(content) @@ plainto_tsquery($2)
ORDER BY score DESC
LIMIT 10;
```

### Python Integration

```python
import asyncpg
import numpy as np
from pgvector.asyncpg import register_vector

async def setup_connection():
    conn = await asyncpg.connect(DATABASE_URL)
    await register_vector(conn)
    return conn

async def upsert_embeddings(
    conn: asyncpg.Connection,
    documents: list[dict],
    embeddings: list[list[float]]
) -> None:
    """Batch upsert documents with embeddings."""
    await conn.executemany(
        """
        INSERT INTO documents (id, content, embedding, metadata)
        VALUES ($1, $2, $3, $4)
        ON CONFLICT (id) DO UPDATE SET
            content = EXCLUDED.content,
            embedding = EXCLUDED.embedding,
            metadata = EXCLUDED.metadata,
            updated_at = NOW()
        """,
        [
            (doc["id"], doc["content"], emb, doc.get("metadata", {}))
            for doc, emb in zip(documents, embeddings)
        ]
    )

async def similarity_search(
    conn: asyncpg.Connection,
    query_embedding: list[float],
    limit: int = 10,
    filters: dict | None = None
) -> list[dict]:
    """Search for similar documents."""
    query = """
        SELECT id, content, metadata, 1 - (embedding <=> $1) AS similarity
        FROM documents
        WHERE 1=1
    """
    params = [query_embedding]
    
    if filters:
        for key, value in filters.items():
            params.append(value)
            query += f" AND metadata->>'{key}' = ${len(params)}"
    
    query += f" ORDER BY embedding <=> $1 LIMIT {limit}"
    
    rows = await conn.fetch(query, *params)
    return [dict(row) for row in rows]
```

---

## Pinecone Patterns

### Index Setup

```python
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key="your-api-key")

# Create serverless index
pc.create_index(
    name="documents",
    dimension=1536,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )
)

index = pc.Index("documents")
```

### Upsert Patterns

```python
from pinecone import Pinecone
import itertools

def chunked(iterable, size):
    """Yield chunks of specified size."""
    it = iter(iterable)
    while chunk := list(itertools.islice(it, size)):
        yield chunk

async def batch_upsert(
    index,
    vectors: list[dict],
    batch_size: int = 100,
    namespace: str = ""
) -> None:
    """Efficient batch upsert with chunking."""
    for batch in chunked(vectors, batch_size):
        index.upsert(
            vectors=[
                {
                    "id": v["id"],
                    "values": v["embedding"],
                    "metadata": v.get("metadata", {})
                }
                for v in batch
            ],
            namespace=namespace
        )

# Example usage
vectors = [
    {
        "id": f"doc_{i}",
        "embedding": embeddings[i],
        "metadata": {
            "source": "web",
            "category": "technical",
            "date": "2026-01-01"
        }
    }
    for i in range(len(documents))
]

await batch_upsert(index, vectors, namespace="production")
```

### Query Patterns

```python
def similarity_search(
    index,
    query_embedding: list[float],
    top_k: int = 10,
    namespace: str = "",
    filters: dict | None = None,
    include_metadata: bool = True
) -> list[dict]:
    """Search with optional metadata filtering."""
    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        namespace=namespace,
        filter=filters,
        include_metadata=include_metadata,
        include_values=False
    )
    
    return [
        {
            "id": match.id,
            "score": match.score,
            "metadata": match.metadata
        }
        for match in results.matches
    ]

# Filtered search example
results = similarity_search(
    index,
    query_embedding,
    filters={
        "category": {"$eq": "technical"},
        "date": {"$gte": "2025-01-01"}
    }
)

# Hybrid search with sparse vectors
results = index.query(
    vector=dense_embedding,
    sparse_vector={
        "indices": [102, 312, 512],
        "values": [0.8, 0.6, 0.4]
    },
    top_k=10
)
```

---

## Weaviate Patterns

### Schema Definition

```python
import weaviate
from weaviate.classes.config import Configure, Property, DataType

client = weaviate.connect_to_local()  # or connect_to_wcs()

# Create collection with vectorizer
client.collections.create(
    name="Document",
    vectorizer_config=Configure.Vectorizer.text2vec_openai(
        model="text-embedding-3-small"
    ),
    generative_config=Configure.Generative.openai(
        model="gpt-4o-mini"
    ),
    properties=[
        Property(name="content", data_type=DataType.TEXT),
        Property(name="category", data_type=DataType.TEXT),
        Property(name="source", data_type=DataType.TEXT),
        Property(name="created_at", data_type=DataType.DATE),
    ]
)
```

### Query Patterns

```python
from weaviate.classes.query import MetadataQuery, Filter

collection = client.collections.get("Document")

# Vector search
results = collection.query.near_text(
    query="machine learning optimization",
    limit=10,
    return_metadata=MetadataQuery(distance=True)
)

# Hybrid search (vector + BM25)
results = collection.query.hybrid(
    query="machine learning optimization",
    alpha=0.75,  # 0=BM25, 1=vector
    limit=10
)

# Filtered search
results = collection.query.near_text(
    query="machine learning",
    filters=Filter.by_property("category").equal("technical"),
    limit=10
)

# Generative search (RAG)
results = collection.generate.near_text(
    query="machine learning optimization",
    grouped_task="Summarize these documents",
    limit=5
)
```

---

## Chroma Patterns

### Setup and Collections

```python
import chromadb
from chromadb.config import Settings

# Persistent client
client = chromadb.PersistentClient(
    path="/path/to/persist",
    settings=Settings(anonymized_telemetry=False)
)

# Create collection with custom embedding function
from chromadb.utils import embedding_functions

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key="your-api-key",
    model_name="text-embedding-3-small"
)

collection = client.get_or_create_collection(
    name="documents",
    embedding_function=openai_ef,
    metadata={"hnsw:space": "cosine"}
)
```

### CRUD Operations

```python
# Add documents
collection.add(
    ids=["doc1", "doc2", "doc3"],
    documents=["First document", "Second document", "Third document"],
    metadatas=[
        {"category": "tech", "source": "web"},
        {"category": "science", "source": "paper"},
        {"category": "tech", "source": "blog"}
    ]
)

# Add with pre-computed embeddings
collection.add(
    ids=["doc4"],
    embeddings=[[0.1, 0.2, 0.3, ...]],
    metadatas=[{"category": "tech"}],
    documents=["Fourth document"]
)

# Update
collection.update(
    ids=["doc1"],
    documents=["Updated first document"],
    metadatas=[{"category": "updated"}]
)

# Delete
collection.delete(ids=["doc2"])
collection.delete(where={"category": "old"})
```

### Query Patterns

```python
# Basic query
results = collection.query(
    query_texts=["machine learning"],
    n_results=10
)

# Query with filters
results = collection.query(
    query_texts=["machine learning"],
    n_results=10,
    where={"category": "tech"},
    where_document={"$contains": "neural"}
)

# Query with embeddings
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=10,
    include=["documents", "metadatas", "distances"]
)

# Complex filters
results = collection.query(
    query_texts=["optimization techniques"],
    where={
        "$and": [
            {"category": {"$eq": "tech"}},
            {"date": {"$gte": "2025-01-01"}}
        ]
    },
    n_results=10
)
```

---

## Qdrant Patterns

### Collection Setup

```python
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance, VectorParams, 
    OptimizersConfigDiff, HnswConfigDiff
)

client = QdrantClient(url="http://localhost:6333")

# Create optimized collection
client.create_collection(
    collection_name="documents",
    vectors_config=VectorParams(
        size=1536,
        distance=Distance.COSINE,
        on_disk=True  # For large collections
    ),
    hnsw_config=HnswConfigDiff(
        m=16,
        ef_construct=100,
        full_scan_threshold=10000
    ),
    optimizers_config=OptimizersConfigDiff(
        indexing_threshold=20000
    )
)

# Create payload index for filtering
client.create_payload_index(
    collection_name="documents",
    field_name="category",
    field_schema="keyword"
)
```

### Upsert Patterns

```python
from qdrant_client.models import PointStruct, Batch

# Single upsert
client.upsert(
    collection_name="documents",
    points=[
        PointStruct(
            id=1,
            vector=embedding,
            payload={"content": "...", "category": "tech"}
        )
    ]
)

# Batch upsert (recommended)
client.upsert(
    collection_name="documents",
    points=Batch(
        ids=list(range(len(embeddings))),
        vectors=embeddings,
        payloads=[{"content": doc, "category": cat} for doc, cat in zip(docs, cats)]
    )
)
```

### Query Patterns

```python
from qdrant_client.models import Filter, FieldCondition, MatchValue, Range

# Basic search
results = client.search(
    collection_name="documents",
    query_vector=query_embedding,
    limit=10
)

# Filtered search
results = client.search(
    collection_name="documents",
    query_vector=query_embedding,
    query_filter=Filter(
        must=[
            FieldCondition(
                key="category",
                match=MatchValue(value="tech")
            ),
            FieldCondition(
                key="date",
                range=Range(gte="2025-01-01")
            )
        ]
    ),
    limit=10
)

# Search with score threshold
results = client.search(
    collection_name="documents",
    query_vector=query_embedding,
    score_threshold=0.7,
    limit=10
)

# Recommendation (find similar to positive, dissimilar to negative)
results = client.recommend(
    collection_name="documents",
    positive=[1, 2, 3],  # Point IDs
    negative=[4],
    limit=10
)
```

---

## Performance Optimization

### Index Tuning Guidelines

| Vector Count | Database | Index | Key Parameters |
|--------------|----------|-------|----------------|
| < 100K | Any | Flat/Brute | None needed |
| 100K - 1M | pgvector | HNSW | m=16, ef=64 |
| 1M - 10M | Qdrant/Pinecone | HNSW | m=32, ef=128 |
| > 10M | Pinecone/Milvus | Product Quantization | segment size |

### Query Optimization

```python
# ❌ Inefficient: Large top_k with post-filtering
results = search(query, top_k=1000)
filtered = [r for r in results if r.category == "tech"][:10]

# ✅ Efficient: Pre-filtering with metadata
results = search(query, top_k=10, filter={"category": "tech"})

# ❌ Inefficient: One-by-one queries
for query in queries:
    result = search(query)

# ✅ Efficient: Batch queries
results = batch_search(queries)
```

### Memory Management

```python
# pgvector: Control work_mem for index builds
SET maintenance_work_mem = '2GB';
CREATE INDEX ...;
RESET maintenance_work_mem;

# Qdrant: Use on-disk vectors for large collections
VectorParams(size=1536, distance=Distance.COSINE, on_disk=True)

# Pinecone: Use namespaces to partition data
index.upsert(vectors, namespace="tenant_123")
```

---

## Monitoring & Operations

### Key Metrics

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Query latency p99 | < 100ms | > 500ms |
| Recall@10 | > 95% | < 90% |
| Index build time | - | Regression |
| Storage usage | - | > 80% capacity |

### Health Checks

```python
# pgvector
SELECT pg_size_pretty(pg_total_relation_size('documents'));
SELECT * FROM pg_stat_user_indexes WHERE indexrelname LIKE '%embedding%';

# Qdrant
client.get_collection("documents").status
client.get_collection("documents").points_count

# Pinecone
index.describe_index_stats()
```

---

## Severity Guide

| Severity | Pattern | Impact |
|----------|---------|--------|
| 🔴 Critical | No index on vectors | O(n) queries |
| 🔴 Critical | Wrong distance metric | Incorrect results |
| 🟠 High | Suboptimal index params | Poor recall/latency |
| 🟠 High | No filtered index | Slow filtered queries |
| 🟡 Medium | Missing batch operations | Slow ingestion |
| 🟡 Medium | No monitoring | Silent degradation |

---

## Report Template

```markdown
## Vector Database Analysis

### Configuration
- Database: [type and version]
- Vector count: [current]
- Dimensions: [size]
- Index type: [HNSW/IVF/etc]

### Performance Assessment
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Query latency p50 | | < 50ms | |
| Query latency p99 | | < 200ms | |
| Recall@10 | | > 95% | |
| Ingestion rate | | | |

### Issues Found
1. [Severity] Issue description
   - Impact: 
   - Recommendation:

### Recommendations
1. [Priority] Recommendation
   - Rationale:
   - Implementation:
```

---

## Related Prompts

- [rag-patterns.md](rag-patterns.md) — RAG system design
- [llm-integration.md](llm-integration.md) — LLM API patterns
- [../db/postgresql-optimization.md](../db/postgresql-optimization.md) — PostgreSQL tuning

---

*Last updated: 2026-01*

# Prompt Engineering — Design, Testing & Optimization

> **Purpose**: Systematic prompt development for production systems  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Prompt design, testing, versioning, evaluation  
> **Last Updated**: 2026-03

---

## Mission

Help create **effective, reliable prompts** through systematic design, testing, and iteration. Focus on clear structure, consistent outputs, and measurable quality.

---

## Guard Clauses

**If no prompt context provided:**
```
NO_PROMPT_CONTEXT

Please provide context:
- Task the prompt should accomplish
- Input format and examples
- Expected output format
- Or share an existing prompt to review
```

**If prompt is well-designed:**
```
PROMPT_APPROVED

✅ Prompt review complete — production ready.

Checks performed:
- Clarity: ✓ (clear instructions, no ambiguity)
- Structure: ✓ (logical flow, proper formatting)
- Robustness: ✓ (handles edge cases)
- Output: ✓ (consistent format, reliable quality)

Prompt follows best practices.
```

---

## Quick Context Checklist

```
☐ Task description
☐ Input format and constraints
☐ Output format requirements
☐ Success criteria
☐ Edge cases to handle
☐ Examples (good and bad)
☐ Model target (GPT-4, Claude, etc.)
☐ Token budget
```

---

## Copy-Paste Prompts

### Prompt: Design New Prompt
```text
Design a prompt for:

Task: {{TASK_DESCRIPTION}}
Input: {{INPUT_FORMAT}}
Output: {{OUTPUT_FORMAT}}
Model: {{TARGET_MODEL}}
Token budget: {{MAX_TOKENS}}

Requirements:
- {{REQUIREMENT_1}}
- {{REQUIREMENT_2}}
- {{REQUIREMENT_3}}

Generate:
1. System prompt
2. User prompt template
3. 3 test examples
4. Edge cases to test
5. Evaluation criteria
```

### Prompt: Review Existing Prompt
```text
Review this prompt:

{{PROMPT}}

Check for:
1. **Clarity**
   - Instructions unambiguous
   - Task clearly defined
   - Constraints explicit

2. **Structure**
   - Logical organization
   - Proper formatting cues
   - Delimiter usage

3. **Robustness**
   - Edge case handling
   - Input validation
   - Failure modes

4. **Efficiency**
   - Token usage
   - Necessary vs redundant content
   - Output length control

Rate each: 🟢 Good | 🟡 Needs attention | 🔴 Critical issue
Provide improved version.
```

### Prompt: Optimize for Model
```text
Optimize this prompt for {{TARGET_MODEL}}:

Current prompt:
{{PROMPT}}

Current performance:
- Success rate: {{SUCCESS_RATE}}
- Consistency: {{CONSISTENCY}}
- Issues: {{ISSUES}}

Generate:
1. Model-specific optimizations
2. Improved prompt version
3. Expected improvement
4. Test cases to validate
```

### Prompt: Create Test Suite
```text
Create a test suite for this prompt:

{{PROMPT}}

Expected behavior: {{EXPECTED_BEHAVIOR}}

Generate:
1. 10 diverse test inputs
2. Expected outputs for each
3. Edge cases (5+)
4. Adversarial inputs (3+)
5. Evaluation rubric
6. Automated test script
```

---

## Prompt Design Patterns

### Basic Structure
```text
# Role and Context
You are a {{ROLE}} with expertise in {{DOMAIN}}.
Your task is to {{PRIMARY_TASK}}.

# Instructions
1. {{STEP_1}}
2. {{STEP_2}}
3. {{STEP_3}}

# Constraints
- {{CONSTRAINT_1}}
- {{CONSTRAINT_2}}
- NEVER {{PROHIBITION}}

# Output Format
Respond in the following format:
{{OUTPUT_TEMPLATE}}

# Examples
Input: {{EXAMPLE_INPUT_1}}
Output: {{EXAMPLE_OUTPUT_1}}

Input: {{EXAMPLE_INPUT_2}}
Output: {{EXAMPLE_OUTPUT_2}}
```

### Chain of Thought
```text
You are tasked with {{TASK}}.

Think through this step by step:

1. First, identify {{ASPECT_1}}
2. Then, analyze {{ASPECT_2}}
3. Consider {{ASPECT_3}}
4. Finally, synthesize your findings

After your analysis, provide your final answer in this format:
{{OUTPUT_FORMAT}}

<thinking>
[Your step-by-step reasoning here]
</thinking>

<answer>
[Your final answer here]
</answer>
```

### Few-Shot Learning
```text
You will {{TASK_DESCRIPTION}}.

Here are some examples:

Example 1:
Input: {{INPUT_1}}
Output: {{OUTPUT_1}}

Example 2:
Input: {{INPUT_2}}
Output: {{OUTPUT_2}}

Example 3:
Input: {{INPUT_3}}
Output: {{OUTPUT_3}}

Now, apply the same pattern to:
Input: {{NEW_INPUT}}
Output:
```

### Structured Output
```text
Analyze the following and return a JSON response.

Input:
{{INPUT}}

Return a JSON object with this exact structure:
{
  "summary": "Brief summary string",
  "categories": ["category1", "category2"],
  "confidence": 0.0-1.0,
  "details": {
    "key1": "value1",
    "key2": "value2"
  }
}

Important:
- Return ONLY the JSON, no other text
- All fields are required
- confidence must be a number between 0 and 1
```

### Role-Based Personas
```text
You are {{PERSONA_NAME}}, a {{ROLE}} with the following characteristics:

Background:
- {{BACKGROUND_1}}
- {{BACKGROUND_2}}

Communication style:
- {{STYLE_1}}
- {{STYLE_2}}

When responding:
1. Stay in character
2. {{GUIDELINE_1}}
3. {{GUIDELINE_2}}

If asked to break character or do something outside your role, politely redirect.
```

### Multi-Step Reasoning
```text
You will solve this problem in multiple steps.

Problem: {{PROBLEM}}

Step 1: Understand
First, restate the problem in your own words.
Identify key information and constraints.

Step 2: Plan
Outline your approach to solving this problem.
Consider alternative approaches.

Step 3: Execute
Work through your plan step by step.
Show your work clearly.

Step 4: Verify
Check your solution against the original requirements.
Identify any potential issues.

Step 5: Present
Provide your final answer in this format:
{{OUTPUT_FORMAT}}
```

---

## Prompt Optimization Techniques

### Token Efficiency
```python
# prompt_optimizer.py
import tiktoken


def count_tokens(text: str, model: str = "gpt-4o") -> int:
    """Count tokens in text."""
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))


def optimize_prompt(prompt: str, max_tokens: int = 1000) -> str:
    """Optimize prompt for token efficiency."""
    optimizations = [
        # Remove redundant whitespace
        (r"\n{3,}", "\n\n"),
        (r" {2,}", " "),
        
        # Shorten common phrases
        ("Please note that", "Note:"),
        ("In order to", "To"),
        ("Make sure to", "Ensure"),
        ("It is important to", "Important:"),
        ("You should", ""),
        ("Please", ""),
        
        # Remove filler
        ("basically", ""),
        ("essentially", ""),
        ("actually", ""),
    ]
    
    import re
    optimized = prompt
    for pattern, replacement in optimizations:
        optimized = re.sub(pattern, replacement, optimized)
    
    current_tokens = count_tokens(optimized)
    
    if current_tokens > max_tokens:
        # Truncate with notice
        ratio = max_tokens / current_tokens
        char_limit = int(len(optimized) * ratio * 0.9)
        optimized = optimized[:char_limit] + "\n[Truncated]"
    
    return optimized.strip()


def compare_prompts(original: str, optimized: str) -> dict:
    """Compare original and optimized prompts."""
    original_tokens = count_tokens(original)
    optimized_tokens = count_tokens(optimized)
    
    return {
        "original_tokens": original_tokens,
        "optimized_tokens": optimized_tokens,
        "tokens_saved": original_tokens - optimized_tokens,
        "reduction_percent": round(
            (1 - optimized_tokens / original_tokens) * 100, 1
        ),
    }
```

### A/B Testing Framework
```python
# prompt_ab_test.py
from dataclasses import dataclass, field
from typing import Any
import random
import asyncio
from openai import AsyncOpenAI


@dataclass
class PromptVariant:
    """A prompt variant for A/B testing."""
    name: str
    system_prompt: str
    user_template: str
    weight: float = 1.0


@dataclass
class ABTestResult:
    """Result of an A/B test."""
    variant_name: str
    input: str
    output: str
    latency_ms: float
    tokens_used: int
    score: float | None = None


class PromptABTester:
    """A/B test prompt variants."""
    
    def __init__(self, variants: list[PromptVariant]):
        self.variants = variants
        self._client = AsyncOpenAI()
        self._results: list[ABTestResult] = []
    
    def select_variant(self) -> PromptVariant:
        """Select a variant based on weights."""
        total_weight = sum(v.weight for v in self.variants)
        r = random.random() * total_weight
        
        cumulative = 0
        for variant in self.variants:
            cumulative += variant.weight
            if r <= cumulative:
                return variant
        
        return self.variants[-1]
    
    async def test(
        self,
        input_text: str,
        variant: PromptVariant | None = None,
        model: str = "gpt-4o",
    ) -> ABTestResult:
        """Run a single test."""
        if variant is None:
            variant = self.select_variant()
        
        import time
        start = time.perf_counter()
        
        response = await self._client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": variant.system_prompt},
                {"role": "user", "content": variant.user_template.format(input=input_text)},
            ],
        )
        
        latency = (time.perf_counter() - start) * 1000
        
        result = ABTestResult(
            variant_name=variant.name,
            input=input_text,
            output=response.choices[0].message.content or "",
            latency_ms=latency,
            tokens_used=response.usage.total_tokens,
        )
        
        self._results.append(result)
        return result
    
    async def run_test_suite(
        self,
        test_inputs: list[str],
        runs_per_variant: int = 10,
    ) -> dict[str, Any]:
        """Run comprehensive A/B test."""
        for variant in self.variants:
            for input_text in test_inputs:
                for _ in range(runs_per_variant):
                    await self.test(input_text, variant)
        
        return self.analyze_results()
    
    def analyze_results(self) -> dict[str, Any]:
        """Analyze A/B test results."""
        by_variant = {}
        
        for result in self._results:
            if result.variant_name not in by_variant:
                by_variant[result.variant_name] = []
            by_variant[result.variant_name].append(result)
        
        analysis = {}
        for name, results in by_variant.items():
            analysis[name] = {
                "count": len(results),
                "avg_latency_ms": sum(r.latency_ms for r in results) / len(results),
                "avg_tokens": sum(r.tokens_used for r in results) / len(results),
                "avg_score": (
                    sum(r.score for r in results if r.score is not None)
                    / len([r for r in results if r.score is not None])
                    if any(r.score is not None for r in results)
                    else None
                ),
            }
        
        return analysis
```

### Prompt Versioning
```python
# prompt_versioning.py
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
import hashlib
import json


@dataclass
class PromptVersion:
    """A versioned prompt."""
    name: str
    version: str
    system_prompt: str
    user_template: str
    created_at: datetime = field(default_factory=datetime.now)
    metadata: dict[str, Any] = field(default_factory=dict)
    
    @property
    def hash(self) -> str:
        """Content hash for comparison."""
        content = f"{self.system_prompt}|{self.user_template}"
        return hashlib.sha256(content.encode()).hexdigest()[:12]
    
    def to_dict(self) -> dict:
        """Serialize to dictionary."""
        return {
            "name": self.name,
            "version": self.version,
            "system_prompt": self.system_prompt,
            "user_template": self.user_template,
            "created_at": self.created_at.isoformat(),
            "metadata": self.metadata,
            "hash": self.hash,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "PromptVersion":
        """Deserialize from dictionary."""
        return cls(
            name=data["name"],
            version=data["version"],
            system_prompt=data["system_prompt"],
            user_template=data["user_template"],
            created_at=datetime.fromisoformat(data["created_at"]),
            metadata=data.get("metadata", {}),
        )


class PromptRegistry:
    """Manage prompt versions."""
    
    def __init__(self, storage_path: str = "prompts.json"):
        self.storage_path = storage_path
        self._prompts: dict[str, list[PromptVersion]] = {}
        self._load()
    
    def _load(self):
        """Load prompts from storage."""
        try:
            with open(self.storage_path) as f:
                data = json.load(f)
                for name, versions in data.items():
                    self._prompts[name] = [
                        PromptVersion.from_dict(v) for v in versions
                    ]
        except FileNotFoundError:
            pass
    
    def _save(self):
        """Save prompts to storage."""
        data = {
            name: [v.to_dict() for v in versions]
            for name, versions in self._prompts.items()
        }
        with open(self.storage_path, "w") as f:
            json.dump(data, f, indent=2)
    
    def register(self, prompt: PromptVersion) -> str:
        """Register a new prompt version."""
        if prompt.name not in self._prompts:
            self._prompts[prompt.name] = []
        
        # Check for duplicate content
        for existing in self._prompts[prompt.name]:
            if existing.hash == prompt.hash:
                return existing.version
        
        self._prompts[prompt.name].append(prompt)
        self._save()
        return prompt.version
    
    def get(
        self, 
        name: str, 
        version: str | None = None,
    ) -> PromptVersion | None:
        """Get a prompt by name and optional version."""
        if name not in self._prompts:
            return None
        
        versions = self._prompts[name]
        
        if version is None:
            return versions[-1]  # Latest
        
        for v in versions:
            if v.version == version:
                return v
        
        return None
    
    def list_versions(self, name: str) -> list[str]:
        """List all versions of a prompt."""
        if name not in self._prompts:
            return []
        return [v.version for v in self._prompts[name]]
    
    def diff(self, name: str, v1: str, v2: str) -> dict:
        """Compare two prompt versions."""
        p1 = self.get(name, v1)
        p2 = self.get(name, v2)
        
        if not p1 or not p2:
            raise ValueError("Version not found")
        
        return {
            "system_prompt_changed": p1.system_prompt != p2.system_prompt,
            "user_template_changed": p1.user_template != p2.user_template,
            "v1_hash": p1.hash,
            "v2_hash": p2.hash,
        }
```

---

## Evaluation Framework

```python
# prompt_evaluation.py
from dataclasses import dataclass
from typing import Callable, Any
from openai import AsyncOpenAI


@dataclass
class EvalCriterion:
    """A criterion for evaluating prompts."""
    name: str
    description: str
    scorer: Callable[[str, str, str], float]  # (input, output, expected) -> score


@dataclass 
class EvalResult:
    """Result of evaluating a prompt."""
    input: str
    output: str
    expected: str | None
    scores: dict[str, float]
    total_score: float


class PromptEvaluator:
    """Evaluate prompt quality."""
    
    def __init__(self, criteria: list[EvalCriterion] | None = None):
        self.criteria = criteria or self._default_criteria()
        self._client = AsyncOpenAI()
    
    def _default_criteria(self) -> list[EvalCriterion]:
        """Default evaluation criteria."""
        return [
            EvalCriterion(
                name="relevance",
                description="Is the output relevant to the input?",
                scorer=self._score_relevance,
            ),
            EvalCriterion(
                name="completeness",
                description="Does the output fully address the request?",
                scorer=self._score_completeness,
            ),
            EvalCriterion(
                name="format",
                description="Is the output in the expected format?",
                scorer=self._score_format,
            ),
        ]
    
    async def evaluate(
        self,
        input_text: str,
        output: str,
        expected: str | None = None,
    ) -> EvalResult:
        """Evaluate a single output."""
        scores = {}
        
        for criterion in self.criteria:
            score = await criterion.scorer(input_text, output, expected or "")
            scores[criterion.name] = score
        
        total = sum(scores.values()) / len(scores)
        
        return EvalResult(
            input=input_text,
            output=output,
            expected=expected,
            scores=scores,
            total_score=total,
        )
    
    async def _score_relevance(
        self,
        input_text: str,
        output: str,
        expected: str,
    ) -> float:
        """Score output relevance using LLM."""
        response = await self._client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Rate the relevance of the output to the input from 0-10. Return only the number.",
                },
                {
                    "role": "user",
                    "content": f"Input: {input_text}\n\nOutput: {output}",
                },
            ],
            temperature=0,
        )
        
        try:
            score = float(response.choices[0].message.content.strip())
            return score / 10
        except:
            return 0.5
    
    async def _score_completeness(
        self,
        input_text: str,
        output: str,
        expected: str,
    ) -> float:
        """Score output completeness."""
        response = await self._client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Rate how completely the output addresses the input request from 0-10. Return only the number.",
                },
                {
                    "role": "user",
                    "content": f"Input: {input_text}\n\nOutput: {output}",
                },
            ],
            temperature=0,
        )
        
        try:
            score = float(response.choices[0].message.content.strip())
            return score / 10
        except:
            return 0.5
    
    async def _score_format(
        self,
        input_text: str,
        output: str,
        expected: str,
    ) -> float:
        """Score format compliance."""
        if not expected:
            return 1.0
        
        response = await self._client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Rate how well the output matches the expected format from 0-10. Return only the number.",
                },
                {
                    "role": "user",
                    "content": f"Expected format:\n{expected}\n\nActual output:\n{output}",
                },
            ],
            temperature=0,
        )
        
        try:
            score = float(response.choices[0].message.content.strip())
            return score / 10
        except:
            return 0.5


async def run_prompt_eval(
    prompt_system: str,
    prompt_user_template: str,
    test_cases: list[dict[str, str]],  # {"input": ..., "expected": ...}
    model: str = "gpt-4o",
) -> dict[str, Any]:
    """Run full evaluation on a prompt."""
    client = AsyncOpenAI()
    evaluator = PromptEvaluator()
    
    results = []
    
    for test in test_cases:
        # Generate output
        response = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": prompt_system},
                {"role": "user", "content": prompt_user_template.format(**test)},
            ],
        )
        
        output = response.choices[0].message.content or ""
        
        # Evaluate
        eval_result = await evaluator.evaluate(
            test["input"],
            output,
            test.get("expected"),
        )
        
        results.append(eval_result)
    
    # Aggregate
    return {
        "num_tests": len(results),
        "avg_total_score": sum(r.total_score for r in results) / len(results),
        "scores_by_criterion": {
            criterion.name: sum(r.scores[criterion.name] for r in results) / len(results)
            for criterion in evaluator.criteria
        },
        "results": results,
    }
```

---

## Common Prompt Patterns

### Classification
```text
Classify the following text into exactly one category.

Categories:
- {{CATEGORY_1}}: {{DESCRIPTION_1}}
- {{CATEGORY_2}}: {{DESCRIPTION_2}}
- {{CATEGORY_3}}: {{DESCRIPTION_3}}

Text to classify:
{{INPUT}}

Return ONLY the category name, nothing else.
```

### Extraction
```text
Extract the following information from the text:

Fields to extract:
- name: The person's full name
- email: Their email address
- date: Any mentioned date (format: YYYY-MM-DD)
- amount: Any monetary amount

Text:
{{INPUT}}

Return a JSON object with the extracted fields.
Use null for fields not found in the text.
```

### Summarization
```text
Summarize the following text in {{LENGTH}} words.

Guidelines:
- Include the main point and key supporting details
- Maintain the original tone
- Do not add information not in the original
- Use clear, concise language

Text:
{{INPUT}}

Summary:
```

### Translation
```text
Translate the following from {{SOURCE_LANG}} to {{TARGET_LANG}}.

Guidelines:
- Maintain the original meaning and tone
- Use appropriate idioms in the target language
- Preserve formatting (paragraphs, lists, etc.)
- Keep proper nouns unchanged unless they have standard translations

Text:
{{INPUT}}

Translation:
```

### Code Generation
```text
Generate {{LANGUAGE}} code that accomplishes the following:

Task: {{TASK_DESCRIPTION}}

Requirements:
- {{REQ_1}}
- {{REQ_2}}
- {{REQ_3}}

Constraints:
- {{CONSTRAINT_1}}
- {{CONSTRAINT_2}}

Return ONLY the code, no explanations.
Use best practices for {{LANGUAGE}}.
Include comments for complex logic.
```

---

## Report Template

```markdown
# Prompt Review — {{PROMPT_NAME}}

**Date**: {{DATE}}
**Model Target**: {{MODEL}}

## Summary

| Aspect | Status | Notes |
|--------|--------|-------|
| Clarity | 🟢/🟡/🔴 | {{NOTES}} |
| Structure | 🟢/🟡/🔴 | {{NOTES}} |
| Robustness | 🟢/🟡/🔴 | {{NOTES}} |
| Efficiency | 🟢/🟡/🔴 | {{NOTES}} |

## Performance Metrics
- Success rate: {{SUCCESS_RATE}}
- Consistency: {{CONSISTENCY}}
- Avg tokens: {{TOKENS}}

## Issues Found
{{ISSUES}}

## Improved Version
{{IMPROVED_PROMPT}}

## Test Results
{{TEST_RESULTS}}
```

---

## Best Practices Checklist

### Structure
- [ ] Clear role/persona defined
- [ ] Task explicitly stated
- [ ] Step-by-step instructions
- [ ] Output format specified
- [ ] Examples provided

### Clarity
- [ ] No ambiguous language
- [ ] Constraints explicit
- [ ] Edge cases addressed
- [ ] Terminology consistent

### Efficiency
- [ ] No redundant text
- [ ] Token usage optimized
- [ ] Examples minimal but effective
- [ ] Instructions concise

### Robustness
- [ ] Handles edge cases
- [ ] Fails gracefully
- [ ] Input validation
- [ ] Output validation

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | Ambiguous instructions, wrong output format |
| **High** | 🟠 | Missing examples, unclear constraints |
| **Medium** | 🟡 | Suboptimal token usage, verbose instructions |
| **Low** | 🟢 | Minor wording, formatting polish |

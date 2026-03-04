# Copilot Instructions — AI & ML

> **Purpose**: Configure AI coding assistants for AI/ML development workflows  
> **Best For**: GitHub Copilot, Codex, Claude, Cursor  
> **Scope**: Assistant instruction-file generation and coding guidance for AI/ML workflows  
> **Last Updated**: 2026-03

---

## Context

You are assisting with AI/ML development tasks including LLM integrations, agent systems, RAG pipelines, and ML workflows.

## Key Principles

1. **Async-first**: Use async/await for all LLM calls
2. **Error resilient**: Always implement retries with backoff
3. **Cost-aware**: Track tokens and implement caching
4. **Security-conscious**: Defend against prompt injection
5. **Observable**: Log all LLM interactions with metrics

## Code Patterns

### LLM Client Setup
```python
# Always use retry logic
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential())
async def call_llm(messages: list[dict]) -> str:
    ...
```

### Structured Outputs
```python
# Prefer Pydantic for LLM responses
from pydantic import BaseModel

class LLMResponse(BaseModel):
    content: str
    reasoning: str | None = None
```

### Prompt Safety
```python
# Always sanitize user input
def build_prompt(system: str, user_input: str) -> list[dict]:
    # Wrap user content in delimiters
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": f"<input>{user_input}</input>"}
    ]
```

## When Generating Code

- Include token counting for cost awareness
- Add response caching where appropriate
- Use streaming for user-facing responses
- Implement graceful degradation
- Log model, tokens, latency for every call

## Related Prompts

See `ai/` folder for detailed prompts on:
- LLM integration patterns
- RAG and vector databases
- Agent development
- Prompt engineering
- ML pipelines

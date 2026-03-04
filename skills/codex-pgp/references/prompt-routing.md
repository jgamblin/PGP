# Prompt Routing Map

## Domain Routing
- AI/LLM integrations, RAG, MCP, agent behavior: `ai/`
- Database schema/query/migration/performance work: `db/`
- React/TypeScript/frontend architecture and testing: `frontend/`
- HTML/CSS fundamentals and compatibility paths: `html/`
- Infrastructure, CI/CD, cloud, IaC, observability: `infrastructure/`
- Python implementation, packaging, typing, testing, security: `python/`
- Ruby/Rails implementation, testing, performance, security: `ruby/`
- Cross-stack architecture, docs, review, cleanup, security process: `generic/`

## Intent Routing
- “Review” or “audit” requests: prefer `*/pr-review-feedback.md` or security/performance equivalents.
- “Set up project/repo” requests: prefer `*/project-repo.md`.
- “Write/refresh docs” requests: prefer `*/documentation-generation.md`.
- “Modernize/refactor” requests: prefer `*/code-refactoring.md` and domain-specific modernization files.

## Fallback Rule
If intent is ambiguous, start with `generic/agents.md`, then narrow to one domain prompt after inspecting repository structure.

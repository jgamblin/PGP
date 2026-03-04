# Prompt Routing Map

## Domain Routing
- AI/LLM and agent tasks: `ai/`
- Database tasks: `db/`
- Frontend React/TypeScript tasks: `frontend/`
- HTML/CSS compatibility or fundamentals: `html/`
- Infrastructure and CI/CD tasks: `infrastructure/`
- Python tasks: `python/`
- Ruby/Rails tasks: `ruby/`
- Cross-domain architecture/process/documentation tasks: `generic/`

## Intent Routing
- Planning and architecture: `generic/system-design-architecture-review.md`
- Documentation refresh: `generic/documentation-generation.md` plus domain docs prompt
- Security review: `generic/security-analysis.md` or domain-specific security prompt
- Refactoring and modernization: domain `code-refactoring.md` plus domain `agents.md`

## Fallback Rule
Use `generic/agents.md` when intent spans multiple domains, then branch into one primary domain prompt.

# Changelog

All notable changes to Pretty Good Prompts will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [2.0.0] - 2026-01-05

### 🎉 Major Relaunch — "2026 Edition"

Complete transformation of PGP into a comprehensive, modern prompt library for AI-assisted development. Expanded from 59 to ~90 prompts.

### Added

#### New `ai/` Folder (7 prompts)
- `ai/llm-integration.md` — LangChain, Instructor, OpenAI/Anthropic SDK patterns
- `ai/rag-patterns.md` — RAG architecture, chunking, embeddings, retrieval strategies
- `ai/prompt-engineering.md` — Meta-prompt design, chain-of-thought, few-shot patterns
- `ai/mcp-server-development.md` — Model Context Protocol servers and tools
- `ai/vector-databases.md` — pgvector, Pinecone, Weaviate, Chroma patterns
- `ai/agents.md` — AI agent architectures, tool use, memory patterns
- `ai/copilot-instructions.md` — AI guidance for AI development

#### New `frontend/` Folder (9 prompts)
- `frontend/typescript-patterns.md` — TypeScript best practices, generics, utility types
- `frontend/react-components.md` — React 18+, hooks, Server Components, patterns
- `frontend/modern-css.md` — Container queries, :has(), cascade layers, subgrid
- `frontend/tailwind-css.md` — Utility-first patterns, plugins, optimization
- `frontend/frontend-testing.md` — Vitest, Playwright, Testing Library
- `frontend/nextjs-vite-config.md` — Next.js 14+, Vite configuration, build optimization
- `frontend/state-management.md` — Zustand, Jotai, TanStack Query patterns
- `frontend/agents.md` — Agent instructions for frontend development
- `frontend/copilot-instructions.md` — AI guidance for frontend prompts
- `frontend/_common-sections.md` — Shared boilerplate for frontend prompts

#### Infrastructure Expansion (5 new prompts)
- `infrastructure/kubernetes.md` — K8s deployments, Helm, resource management
- `infrastructure/terraform-iac.md` — Multi-cloud IaC, modules, state management
- `infrastructure/serverless.md` — AWS Lambda, Vercel, Cloudflare Workers
- `infrastructure/github-actions-deployment.md` — CI/CD pipelines, deployment workflows
- `infrastructure/monitoring-observability.md` — Prometheus, Grafana, OpenTelemetry
- `infrastructure/agents.md` — Agent instructions for infrastructure tasks
- `infrastructure/_common-sections.md` — Shared boilerplate for infrastructure prompts

#### Ruby Modernization (5 new prompts)
- `ruby/hotwire-turbo.md` — Turbo Frames, Streams, morphing, broadcasting
- `ruby/stimulus-controllers.md` — Stimulus patterns, targets, values, outlets
- `ruby/viewcomponent.md` — Component-based views, previews, testing
- `ruby/background-jobs.md` — Sidekiq, Solid Queue, Active Job patterns
- `ruby/security-analysis.md` — Ruby/Rails security audit, OWASP patterns
- `ruby/_common-sections.md` — Shared boilerplate for Ruby prompts

#### Database Expansion (4 new prompts)
- `db/nosql-mongodb.md` — MongoDB patterns, aggregation, schema design
- `db/redis-patterns.md` — Caching, pub/sub, data structures, Lua scripting
- `db/migrations-safety.md` — Safe migrations, zero-downtime deploys
- `db/agents.md` — Agent instructions for database tasks

#### Generic Additions (2 new prompts)
- `generic/api-design.md` — REST, GraphQL, OpenAPI, versioning
- `generic/observability-logging.md` — Structured logging, OpenTelemetry

### Changed

- Updated all prompts to "Last Updated: 2026-01" date format
- Standardized severity labels across all prompts (🔴 Critical, 🟠 High, 🟡 Medium, 🟢 Low)
- Added guard clauses to all prompts for handling edge cases
- Added report templates to all prompts missing them
- Updated tool references to 2026 stack (uv, Ruff, Bun, Vite, etc.)

### Documentation

- Complete rewrite of `README.md` for new structure
- Created `docs/CHANGELOG.md` (this file)
- Created `_common-sections.md` files for ruby/, frontend/, infrastructure/

---

## [1.0.0] - 2025-12-01

### Initial Release

Original 59-prompt collection covering:
- **generic/** — 11 universal prompts
- **python/** — 17 Python ecosystem prompts  
- **ruby/** — 11 Ruby/Rails prompts
- **html/** — 12 frontend/web prompts
- **db/** — 5 database prompts
- **infrastructure/** — 3 DevOps prompts

---

## Roadmap

### Planned for v2.1.0

- [ ] Python additions (fastapi-development.md, ai-ml-integration.md, data-engineering.md)
- [ ] Update html/ folder prompts for WCAG 2.2
- [ ] Add more language-specific prompts (Go, Rust)

### Under Consideration

- [ ] Mobile development prompts (React Native, Flutter)
- [ ] Game development prompts
- [ ] Embedded/IoT prompts
- [ ] Machine learning operations (MLOps) prompts

---

## Contributing

This is a personal project and PRs are not accepted. Feel free to fork and adapt for your own use. See README.md for details.

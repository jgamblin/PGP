# Pretty Good Prompts

## Personal AI Coding Assistant Prompt Library

Personal prompt collection by [@JGamblin](https://github.com/JGamblin), focused on practical engineering workflows.

## March 2026 Status

- Prompt files: **96**
- Markdown files (repo-wide): **100+**
- Native skills added: **2** (`skills/codex-pgp`, `skills/claudeai-pgp`)
- Documentation QA automation: **enabled** (`scripts/qa` + `.github/workflows/docs-quality.yml`)

## Repository Layout

| Directory | Prompt Count | Focus |
|---|---:|---|
| `ai/` | 7 | LLM integration, RAG, MCP, prompt engineering |
| `db/` | 9 | Schema design, migrations, SQL/NoSQL optimization |
| `frontend/` | 10 | TypeScript, React, testing, modern CSS |
| `generic/` | 13 | Cross-language architecture, review, docs, security |
| `html/` | 12 | Legacy-compatible web fundamentals and accessibility |
| `infrastructure/` | 10 | Terraform, Kubernetes, CI/CD, observability |
| `python/` | 18 | Python implementation, packaging, testing, security |
| `ruby/` | 17 | Ruby/Rails architecture, testing, performance |

## Compatibility Policy

The `html/` directory is preserved for backward compatibility in this release cycle.

- Prefer new guidance from `frontend/`.
- Use the migration map: [`docs/compat/html-to-frontend-map.md`](docs/compat/html-to-frontend-map.md).
- Keep legacy links stable when updating docs.

## Native Skills

### Codex Skill
- Path: [`skills/codex-pgp/SKILL.md`](skills/codex-pgp/SKILL.md)
- Use when working terminal-first and mapping tasks to the correct PGP prompt quickly.

### ClaudeAI Skill
- Path: [`skills/claudeai-pgp/SKILL.md`](skills/claudeai-pgp/SKILL.md)
- Use when producing structured, artifact-oriented plans, reviews, and documentation outputs.

## Documentation Quality Checks

Run all checks locally:

```bash
bash scripts/qa/run_docs_qa.sh
```

Checks included:

1. Metadata contract validation (`Purpose`, `Best For`, `Scope`, `Last Updated`)
2. Internal markdown link validation
3. Mojibake detection

## Prompt Standards

Standards are defined in [`docs/prompt-standards.md`](docs/prompt-standards.md).

All prompt files should follow the same metadata contract and quality expectations.

## Domain Index Files

Use each domain index (`agents.md`) as the routing entry point:

- [`ai/agents.md`](ai/agents.md)
- [`db/agents.md`](db/agents.md)
- [`frontend/agents.md`](frontend/agents.md)
- [`generic/agents.md`](generic/agents.md)
- [`html/agents.md`](html/agents.md)
- [`infrastructure/agents.md`](infrastructure/agents.md)
- [`python/agents.md`](python/agents.md)
- [`ruby/agents.md`](ruby/agents.md)

## Changelog

See [`docs/CHANGELOG.md`](docs/CHANGELOG.md) for release history and roadmap updates.

## Fork & Adapt

This is a personal project and pull requests are not accepted.

If you want to extend it:

1. Fork the repository
2. Adapt prompts to your workflows
3. Keep internal conventions consistent with `docs/prompt-standards.md`

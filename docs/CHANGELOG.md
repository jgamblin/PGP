# Changelog

All notable changes to Pretty Good Prompts are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [2.2.0] - 2026-03-04

### Added

- Native Codex skill pack: `skills/codex-pgp/`
- Native ClaudeAI skill pack: `skills/claudeai-pgp/`
- Documentation QA scripts:
  - `scripts/qa/validate_metadata.py`
  - `scripts/qa/check_internal_links.py`
  - `scripts/qa/check_mojibake.py`
  - `scripts/qa/run_docs_qa.sh`
- GitHub Actions workflow: `.github/workflows/docs-quality.yml`
- Compatibility map: `docs/compat/html-to-frontend-map.md`
- Baseline audit snapshot: `docs/audit/2026-03-baseline.md`

### Changed

- Standardized metadata contract across all prompt files:
  - `Purpose`
  - `Best For`
  - `Scope`
  - `Last Updated`
- Normalized prompt `Last Updated` values to `2026-03`.
- Fixed AI index references in `ai/agents.md`.
- Removed mojibake severity markers and replaced with canonical icons.
- Reduced repeated Python boilerplate by routing shared sections to `python/_common-sections.md`.
- Rewrote `README.md` with current inventory, QA usage, and skill integration docs.
- Rewrote `docs/prompt-standards.md` to a valid, enforceable markdown standard.

### Compatibility

- Preserved `html/` paths and added forward links to `frontend/` guidance.

---

## [2.0.1] - 2026-01-10

### Added

- `python/data-processing-performance.md` — heavy data processing optimization with benchmarking and vectorization guidance.

---

## [2.0.0] - 2026-01-05

### Added

- New `ai/` folder (7 prompts)
- New `frontend/` folder (9 prompts + `_common-sections.md`)
- Infrastructure expansion prompts (`kubernetes.md`, `terraform-iac.md`, `serverless.md`, `github-actions-deployment.md`, `monitoring-observability.md`)
- Ruby additions (`hotwire-turbo.md`, `stimulus-controllers.md`, `viewcomponent.md`, `background-jobs.md`, `security-analysis.md`, `_common-sections.md`)
- Database additions (`nosql-mongodb.md`, `redis-patterns.md`, `migrations-safety.md`, `agents.md`)
- Generic additions (`api-design.md`, `observability-logging.md`)

### Documentation

- Full README rewrite for 2026 structure
- Initial `docs/CHANGELOG.md`
- Shared common-section references for selected domains

---

## [1.0.0] - 2025-12-01

### Initial Release

Original prompt collection covering:

- `generic/`
- `python/`
- `ruby/`
- `html/`
- `db/`
- `infrastructure/`

---

## Roadmap

### Planned for v2.3.0

- Expand AI prompt coverage for evaluation workflows
- Add additional language packs (Go, Rust)
- Continue `html/` to `frontend/` compatibility migration notes

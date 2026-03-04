# Prompt Modernization Standards

## Purpose
These standards define the required structure, quality gates, and maintenance rules for all prompt files in this repository.

## Required Metadata Contract
Every prompt in `ai/`, `db/`, `frontend/`, `generic/`, `html/`, `infrastructure/`, `python/`, and `ruby/` must include this metadata block directly under the title:

```markdown
> **Purpose**: ...
> **Best For**: ...
> **Scope**: ...
> **Last Updated**: YYYY-MM
```

## Required Structural Sections
All prompt files should contain these core sections unless the file is a domain index (`agents.md`) or a shared reference (`_common-sections.md`):

1. `## Mission`
2. `## Guard Clauses`
3. `## Quick Context Checklist`
4. Task-specific content sections (prompts, examples, checklists)
5. Output/report format guidance

## Content Quality Rules

1. Prefer actionable, copy-paste-ready guidance.
2. Use severity labels consistently: `🔴 Critical`, `🟠 High`, `🟡 Medium`, `🟢 Low`.
3. Keep examples current with modern tooling.
4. Keep repetitive boilerplate in `_common-sections.md` and link to it.
5. Preserve backward compatibility when moving guidance from `html/` to `frontend/`.

## Documentation Quality Gates
The repository must pass all checks in `scripts/qa/run_docs_qa.sh`:

1. Metadata completeness and `Last Updated` format validation.
2. Internal markdown link validation.
3. Mojibake detection (replacement character check).

## Update Process

1. Update prompt content.
2. Set `Last Updated` to the current `YYYY-MM`.
3. Run `bash scripts/qa/run_docs_qa.sh`.
4. Update affected index files (`agents.md`) and compatibility docs if routing changed.
5. Add changelog entries for notable prompt additions or structural changes.

## Compatibility Policy

- Keep existing path contracts stable during migration cycles.
- Add forward links from legacy paths to modern paths.
- Do not remove legacy files until compatibility notes and replacements are in place.

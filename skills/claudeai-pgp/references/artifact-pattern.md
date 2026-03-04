# Artifact Pattern

## Required Sections
- Summary
- Findings or implementation outcomes
- Proposed changes (with file targets)
- Validation and acceptance checks
- Assumptions and defaults

## Style Rules
- Prioritize clarity over verbosity.
- Keep section ordering stable across updates.
- Use explicit severity and priority terms for findings.

## Validation Checklist
- `bash scripts/qa/run_docs_qa.sh`
- Verify internal links and metadata contract still pass.
- Ensure compatibility notes are included when touching legacy paths.

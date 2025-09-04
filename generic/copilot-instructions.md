# 🧭 Generic Prompt Set – Copilot Usage Guide

Context: This repository is a prompt library (Markdown only). This file is NOT describing this repo's build (there is none). It is meant to be copied into a *real* code repository to standardize AI-assisted reviews. If kept here, it documents how to use the generic prompts.

Use this to:
1. Guide Copilot / Chat tools when auditing arbitrary codebases.
2. Combine with stack-specific files (python/html/ruby) after copying prompts over.
3. Keep analysis cycles small: report → minimal diff → tests → verification.

If you copy this into another repo, edit any sections marked "Example" to reflect actual tooling.

---
## 🎯 Goals Copilot Should Prioritize
1. Architecture clarity (boundaries, layering, dependency direction)
2. Security hygiene (input validation, dependency risk, secrets handling)
3. Performance awareness (algorithmic complexity, I/O hotspots)
4. Test coverage expansion (critical path + regression protection)
5. Documentation scaffolding (README, ADRs, API surface)
6. Incremental, low-risk refactoring (minimal diffs)

---
## 📁 Example Target Project Structure (Edit/Remove After Copy)
```
repo/
  src/                # Primary source code
  tests/              # Automated tests (mirror structure of src/)
  docs/               # Architecture diagrams, ADRs, usage guides
  scripts/            # Tooling helpers (lint, build, maintenance)
  .github/workflows/  # CI (lint, test, security scan)
  Makefile            # (Optional) Common developer tasks
  README.md
  LICENSE
```
Optional: `infra/`, `deploy/`, `examples/`, `config/`.

---
## 🚀 Base Prompt Template (Paste into Copilot Chat)
Use this with selected code or the repository root context:
```
You are a neutral senior technical reviewer.
Scope: <file(s) / module / diff>.
Objectives (ranked): architecture boundaries, security risks, test gaps, refactor opportunities.
Constraints: minimal speculation, no business language, no full rewrites unless unsafe.
Output format:
# Technical Report
## Summary (bullets only)
## Critical Findings (ranked Critical/High/Medium/Low)
## Security
## Performance
## Architecture & Coupling
## Testing Gaps
## Suggested Minimal Patches (top 2)
## Follow-up Options
End by asking me which area to address first.
```

Follow-up examples:
- "Generate unified diff for Issue 1 only—no narration."
- "List untested branches with file:line."
- "Propose ADR titles for major architectural adjustments."

---
## 🛡️ Security Baseline Checklist (Ask Copilot To Audit)
- Hardcoded secrets
- Unsanitized external input
- Missing authentication / authorization checks
- Unpinned critical dependencies
- Insecure transport / crypto misuse

Prompt: "Security-only scan of scope. Rank findings. Provide minimal mitigation patch for top 1." 

---
## 🧪 Testing Strategy Pattern (Reusable Follow-up)
Ask:
```
List critical logic paths without direct test coverage (file:line → condition).
Generate focused tests (no broad scaffolds) for top 3 uncovered branches.
Return only test code + notes on expected behavior.
```

---
## 🏗️ Architecture Review Prompt (Optional High-Level Scan)
```
Analyze current layering & module coupling.
Identify boundary violations, global state leakage, tight coupling clusters.
Suggest a phased restructuring (3 phases max) with minimal churn.
Provide a dependency inversion example (before/after) only if needed.
```

---
## 🔄 Refactor Iteration Loop (Execution Pattern)
1. Run analysis → capture report as `code-refactoring-analysis-YYYY-MM-DD.md`
2. Approve top 1–2 items
3. Request minimal patch
4. Ask for risk + rollback list
5. Generate/add tests
6. Request final verification checklist

---
## ✅ Quality Gate (Have Copilot Produce PASS/FAIL Table)
- Lint clean?
- Tests added for changed logic?
- Public API unchanged (unless intentional)?
- No new global state introduced?
- Complexity reduced or stable?
- Security risk count not increased?

Prompt: "Produce quality gate table PASS/FAIL with one-line justification each." 

---
## 🧾 Documentation Scaffolding Prompt (If Target Repo Lacks README Quality)
```
Generate/update README sections:
- Overview
- Quick Start
- Development (install, run, test)
- Architecture Summary
- Contributing Expectations
- Security Reporting Process
```
Optional: "Suggest first 2 ADR titles + summaries." 

---
## 🧩 Diff-Only Mode (Patch Generation Constraint)
Ask Copilot explicitly:
```
Return unified diff only.
Do not modify unrelated lines.
Do not collapse blank line groups.
Add TODO markers for deferred improvements.
```

---
## 🧠 When Output Is Too Generic (Regeneration Filter)
Reply:
```
Regenerate with:
- Concrete line references
- Before/after code blocks
- Explicit severity rationale (cause → impact → fix)
- Remove vague adjectives
```

---
## 🔐 Example Follow-up Chain
```
1. High-level report
2. Security patch diff
3. Test generation
4. Architecture boundary proposal
5. Documentation sync summary
6. Final quality gate report
```

---
## 🪜 Minimal Onboarding Script Prompt (Only If Target Repo Needs Bootstrapping)
```
Generate a Makefile with targets: install, lint, test, format, coverage.
Assume generic language tooling; use placeholders where language-specific items unknown.
```

---
## ♻️ Using This File Inside The Prompt Library
If you are browsing *inside* the prompt library (this repo) you don't run commands—just copy fragments. Only adapt after moving to a code repo.

Keep iterations narrow. Prefer multiple small diffs over one sweeping rewrite.

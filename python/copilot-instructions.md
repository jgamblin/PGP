# 🧭 Python Prompt Set – Copilot Usage Guide

Context: This file lives in a *prompt library* (no Python runtime here). Copy it into an actual Python repository to guide AI-assisted improvements. After copying, replace example structures/tooling with real project details.

Primary purpose: Coordinate refactor, typing, performance, and test coverage workflows using the Python prompt files in this folder.

---
## 🎯 Priority Focus Areas (Ordered)
1. Correctness & safety (input validation, error handling, side effects)
2. Type coverage & static analysis (mypy, pyright, runtime guards where needed)
3. Performance (algorithmic complexity, DB/IO efficiency, async concurrency)
4. Test coverage (critical paths, edge cases, regression protection)
5. Architecture boundaries (domain vs infrastructure separation)
6. Observability (structured logging, metrics, tracing hooks)

---
## 📁 Example Python Project Structure (Adjust After Copy)
```
project/
  src/               # Application packages
    app/
    domain/
    infra/
    adapters/
  tests/
    unit/
    integration/
    e2e/
  scripts/
  docs/
  pyproject.toml / requirements.txt
  mypy.ini / pyproject typing config
  .github/workflows/ci.yml
  README.md
```
Optional: `alembic/`, `docker/`, `infra/`.

---
## 🛠️ Base Analysis Prompt (Drop-In)
```
You are a neutral senior Python reviewer.
Scope: <files / module / diff>.
Objectives: correctness + type safety + performance + test gaps.
Constraints: minimal speculation, no framework overreach, no full rewrites.
Output:
# Python Technical Report
## Summary
## Critical Issues (ranked)
## Type Safety & Static Analysis
## Performance / Algorithmic Concerns
## Concurrency / Async Risks (if any)
## Security & Input Validation
## Testing Gaps
## Suggested Minimal Patches (top 2)
End with next-step question.
```

Follow-ups:
- "Show mypy error elimination order (highest leverage first)."
- "Generate diff adding only return type hints to public functions in file X." 
- "List unawaited async calls or blocking sync calls inside async funcs." 

---
## 🔡 Typing Increment Plan Prompt (Progressive Adoption)
```
Phase 1: Add return + parameter types for public APIs.
Phase 2: Introduce TypedDict / Protocol for key structures.
Phase 3: Enable mypy strict flags incrementally.
List top 5 fastest type wins with file:line and target annotation.
```

---
## ⚙️ Performance / Async Audit Prompt
```
Identify:
- O(n^2) loops on large collections
- Inefficient DB/ORM patterns (N+1 queries)
- Blocking I/O in async contexts
- Over-frequent object allocations in hot paths
Return each with file:line, impact rationale, suggested fix.
```

---
## 🧪 Test Gap Analysis Prompt
```
List untested conditional branches (file:line → condition).
Rank by risk (data mutation, external I/O, security relevance).
Generate pytest tests for top 3 branches—return only code.
```

---
## 🛡️ Security Checklist (General Python)
- Unsanitized external input
- Direct SQL string formatting
- Use of eval/exec or insecure deserialization (pickle, yaml.load)
- Weak hashing / crypto misuse
- Missing auth/authorization guards
Prompt: "Security-only scan; provide top 3 issues with safer code snippet." 

---
## 🧾 Logging & Observability Prompt
```
Scan for:
- Print statements (replace with structured logging)
- Missing exception context (bare except / suppressed traceback)
- No correlation IDs at request boundaries
Return suggestions + minimal diff for top 1.
```

---
## 🔄 Refactor Iteration Loop (Execution Sequence)
1. Run high-level report
2. Approve first fix target
3. Generate minimal patch
4. Ask for regression risk list
5. Add tests
6. Add types / tighten static checks
7. Final quality gate

---
## ✅ Quality Gate (Ask Copilot)
- Tests pass (new tests fail pre-patch?)
- mypy (or pyright) clean on touched files
- Cyclomatic complexity stable or reduced
- No new global mutable state
- Logging improved (not degraded)
- Security risk count decreased or stable
Prompt: "Produce PASS/FAIL table + one-line rationale." 

---
## 🗜️ Diff Rules Prompt
```
Return unified diff only.
Do not reorder imports unless required.
Preserve formatting; no sweeping black reflow if unrelated.
Add TODO for non-critical improvements.
```

---
## 🧠 When Output Too Generic
Reply:
```
Regenerate with:
- Concrete before/after code
- Complexity classification (O notation) where relevant
- File:line references
- Explicit severity rationale (cause → impact → fix)
```

---
## 🧩 Example Multi-Phase Session
```
1. Report (types + performance + test gaps)
2. Patch: remove O(n^2) hotspot
3. Add tests for refactored area
4. Add protocol & TypedDict for key data flow
5. Introduce structured logging
6. Final gate + risk summary
```

---
## 🧪 Tooling Bootstrap Prompt (Optional if Starting Fresh)
```
Generate minimal pyproject.toml with:
- dependencies section placeholder
- black, isort, mypy, pytest tool config
Also produce mypy.ini strict-but-gradual config.
```

---
## 🔐 Final Verification Checklist
Ask Copilot:
- New code paths covered by tests?
- Any silent behavior change risk?
- Any lingering blocking calls in async context?
- Any added untyped public API?
- Are security-sensitive operations validated?

Prompt: "Generate final checklist PASS/FAIL with 1-line per item." 

---
## ♻️ Using Inside the Prompt Library
Inside this repo you only copy text; do not attempt to run anything here. After copying to a real project, replace placeholders (e.g. Python version, package manager, CI specifics).

Small diffs, measurable improvements, type + test reinforcement every step.

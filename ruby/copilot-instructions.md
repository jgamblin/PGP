# 🧭 Ruby / Rails Prompt Set – Copilot Usage Guide

Context: Prompt library only (no running Rails app here). Copy into a Rails project to coordinate performance, safety, and refactor workflows. Replace placeholders (e.g. DB, cache, Ruby version) after copying.

---
## 🎯 Priority Focus Areas (Ordered)
1. Data integrity & correctness (transactions, validations)
2. Performance (N+1 elimination, query optimization, caching strategy)
3. Object & service boundaries (thin controllers, fat models avoidance)
4. Test coverage & failure isolation (RSpec layering)
5. Security (mass assignment, injection, CSRF, authZ gaps)
6. Code quality (Rubocop alignment, cognitive reduction)

---
## 📁 Example Rails Structure (Adapt After Copy)
```
app/
  controllers/
  models/
  services/
  jobs/
  serializers/
  presenters/
  policies/
config/
db/
  migrations/
  schema.rb
spec/
  models/
  requests/
  services/
  support/
Gemfile
.rubocop.yml
README.md
```
Optional: `lib/`, `engines/`, `docs/`, `scripts/`.

---
## 🛠️ Base Analysis Prompt (Drop-In)
```
You are a neutral senior Rails reviewer.
Scope: <files / diff / component>.
Objectives: data integrity, performance, security, object boundaries, test gaps.
Output:
# Rails Technical Report
## Summary
## Critical Issues (ranked)
## Data Integrity & Transactions
## Performance (queries / memory / allocations)
## Security (auth/authz/mass assignment)
## Architecture & Boundaries
## Testing Gaps
## Suggested Minimal Patches (top 2)
End with next-step question.
```

Follow-ups:
- "List all N+1 risks with file:line and suggested preload." 
- "Show AR callbacks that can be replaced with service objects." 
- "Generate diff adding basic spec for service X covering success + failure." 

---
## 🗃️ ActiveRecord Query Audit Prompt
```
Scan for:
- N+1 includes
- SELECT * on large tables
- Unscoped queries on multi-tenant data
- Callback logic doing external I/O
Return file:line, issue, improvement suggestion (one line each).
```

---
## 🛡️ Security Checklist (Rails)
- Strong params enforcement
- Dangerous dynamic finders / string interpolation in SQL
- CSRF protections disabled / bypassed
- Missing authorization checks (Pundit/CanCan roles)
- Insecure file handling / open redirects
Prompt: "Security-only scan; rank issues; provide safe patch for top 1 only." 

---
## 🚦 Transactions & Consistency Prompt
```
Identify multi-step data updates lacking a wrapping transaction.
Highlight race condition risks (update-then-save patterns).
Suggest minimal transaction-safe refactor for top 1 case.
```

---
## 🧪 Test Gap Analysis Prompt
```
List untested service object branches (file:line → condition).
List controllers without request specs.
Generate RSpec examples for top 2 high-risk branches (only code output).
```

---
## 🧾 Logging & Observability Prompt
```
Identify absence of structured logging around external API calls.
Recommend log context fields (request_id, user_id, latency).
Return minimal diff adding instrumentation to top 1 hotspot.
```

---
## 🔄 Refactor Loop
1. High-level report
2. Pick one: N+1 fix / callback extraction / transaction safety
3. Request minimal diff
4. Ask for risk & rollback
5. Add/update specs
6. Quality gate summary

---
## ✅ Quality Gate (Ask Copilot)
- New queries -> reduced count? (qualitative if not measurable)
- No added global state
- Strong params enforced for modified controllers
- Specs added for changed logic
- RuboCop clean on touched files
Prompt: "Produce PASS/FAIL table with 1-line rationales." 

---
## 🗜️ Diff Output Rules
```
Return unified diff only.
Do not reorder unrelated requires.
Avoid stylistic rewrites unless required by RuboCop.
Add TODO for deeper refactors not included.
```

---
## 🧠 When Output is Generic
Reply:
```
Regenerate with:
- Specific AR relation modifications
- Before/after query strategies
- File:line references
- Severity rationale (data risk / perf impact / security surface)
```

---
## 🧩 Example Session
```
1. Run report
2. Fix N+1 on endpoint
3. Add RSpec request + model specs
4. Extract callback logic to service
5. Add transaction around multi-step update
6. Final verification checklist
```

---
## 🔐 Final Verification Checklist
Ask Copilot to confirm:
- No mass assignment vulnerabilities introduced
- No orphaned records from partial saves
- Query count stable or improved
- Sensitive data not logged
- Specs cover success + failure paths

Prompt: "Generate final checklist PASS/FAIL with 1-line per item." 

---
## ♻️ Using Inside the Prompt Library
In this repo: copy text only. In a real app: ensure environment (DB, caching, background jobs) is declared in README. Small incremental diffs > sweeping rewrites. Validate with specs after each step.

# 🚀 Pretty Good Prompts

## Personal AI Coding Assistant Prompt Library

Personal prompt collection by **[@JGamblin](https://github.com/JGamblin)**. Shared so others can adapt—optimized for my own workflow (analysis first, pragmatic improvements, durable documentation).

### Who This Helps

- Engineers who want structured, repeatable analysis output
- People standardizing review/report formats
- Anyone reducing technical debt with evidence-based refactors

---

## 🛠️ Recent Cleanup Snapshot

- Neutral wording + heading normalization
- Removed quantified hour/effort estimates
- Unified: "domain logic" terminology
- Normalized dashboard/analysis labels
- Eliminated earlier duplication & stray markdown fences

---

## 📂 Repository Structure & File Index

### Top-Level Files
- `LICENSE` — License terms for reuse.
- `README.md` — This documentation.

---

### 🗂️ `generic/` — Universal Prompts
| File | Purpose |
|------|---------|
| `agents.md` | Agent instructions for using generic prompts |
| `ci-cd-pipeline-analysis.md` | CI/CD pipeline analysis |
| `code-refactoring.md` | Refactoring analysis (security, performance, architecture) |
| `copilot-instructions.md` | Copilot/AI guidance for generic prompt usage |
| `do-next.md` | Next-step planning prompt |
| `documentation-generation.md` | Documentation strategy (API specs, records) |
| `pr-review-feedback.md` | Code review (security, performance) |
| `project-repo.md` | Repository setup guide |
| `system-design-architecture-review.md` | System design and architecture review |

---

### 🐍 `python/` — Python Ecosystem Prompts
| File | Purpose |
|------|---------|
| `agents.md` | Agent instructions for Python prompt usage |
| `code-refactoring.md` | Python refactoring (asyncio, Django/Flask/FastAPI) |
| `concurrency-asyncio-pattern-analysis.md` | Concurrency and asyncio pattern analysis |
| `copilot-instructions.md` | Copilot/AI guidance for Python prompt usage |
| `database-schema-orm-optimization.md` | Database schema and ORM optimization |
| `docstring-creation.md` | API documentation (Google/PEP 257) |
| `documentation-generation.md` | Python documentation (Sphinx, type hints) |
| `flake8-compliance.md` | Flake8 compliance check |
| `pr-review-feedback.md` | Python code review (ORM, security, performance) |
| `project-repo.md` | Python repository setup (Poetry, pytest) |
| `type-hinting.md` | Type safety analysis (mypy, modern typing) |
| `unit-test-generation.md` | Test strategy and coverage analysis (pytest) |

---

### 🌐 `html/` — Frontend & Web Prompts
| File | Purpose |
|------|---------|
| `accessibility-check.md` | WCAG compliance audit (accessibility) |
| `agents.md` | Agent instructions for frontend prompt usage |
| `bem-naming-convention.md` | CSS architecture analysis (BEM) |
| `code-refactoring.md` | Frontend refactoring (React/Vue/Angular, BEM, accessibility) |
| `component-design-system-review.md` | Component design system review |
| `copilot-instructions.md` | Copilot/AI guidance for frontend prompt usage |
| `documentation-generation.md` | Frontend documentation (Storybook, design systems) |
| `navigation-consistency.md` | UX navigation standardization |
| `performance-core-web-vitals-audit.md` | Core Web Vitals performance audit |
| `pr-review-feedback.md` | Frontend code review (performance, accessibility) |
| `project-repo.md` | Frontend repository setup (Webpack/Vite, ESLint) |
| `semantic-markup-refinement.md` | HTML5 semantic optimization (SEO, performance) |

---

### 💎 `ruby/` — Ruby & Rails Prompts
| File | Purpose |
|------|---------|
| `agents.md` | Agent instructions for Ruby/Rails prompt usage |
| `code-refactoring.md` | Ruby refactoring (Rails, metaprogramming, gems) |
| `copilot-instructions.md` | Copilot/AI guidance for Ruby/Rails prompt usage |
| `documentation-generation.md` | Ruby documentation (YARD, Rails API) |
| `gemfile-management.md` | Dependency security audit (Gemfile) |
| `pr-review-feedback.md` | Ruby code review (Rails, ActiveRecord) |
| `project-repo.md` | Ruby repository setup (Bundler, RSpec, Rails) |
| `rails-active-record-performance-audit.md` | ActiveRecord performance audit |
| `rspec-test-generation.md` | RSpec test strategy (coverage planning) |
| `rubocop-compliance.md` | Code quality analysis (Rubocop) |
| `service-object-domain-logic-refactoring.md` | Service object and domain logic refactoring |

---

## 📊 Report Output (What To Expect)

Each prompt produces a dated markdown file with:

- Dashboard / summary (security, performance, maintainability highlights)
- Issue list grouped by severity / category
- Concrete remediation suggestions (code snippets where relevant)
- Optional follow-up question offering next-step focus

Benefits: historical trace, shareable review artifact, incremental improvement tracking.

---

## ⚙️ Approach & Cycle

Design principles: evidence-based analysis, smallest safe change, repeat.

Loop:

1. Analyze
2. Prioritize
3. Implement
4. Test / Verify
5. Re-run (compare deltas)

---

## 🎖️ Quality Focus Areas

- Security (common vulnerability classes, unsafe patterns)
- Performance (hot paths, unnecessary allocations, query inefficiencies)
- Architecture (boundaries, cohesion, coupling)
- Testing (coverage of risk & regression vectors)
- Documentation (clarity of intent & public contracts)

---

## 📈 Why It Helps (In Practice)

Common effects: earlier issue detection, clearer priorities, reduced rework, incremental hardening of performance & security posture.

Disclaimer: Effectiveness varies by codebase maturity and follow-through.

---

## 🔀 Fork & Adapt (No Direct PRs)

I am not accepting pull requests. If you want to extend or alter these:

1. Fork the repository
2. Adjust wording / sections to match your team or tooling
3. Rename or reorganize prompts as needed
4. Remove sections you don't use to reduce noise
5. Maintain attribution if large portions are reused

Feel free to publish your own variant.

## 🔍 Quick Start (TL;DR)

1. Pick prompt
2. Provide code
3. Save report
4. Triage top items
5. Implement + verify
6. Re-run for changes

---

## ✅ Style Consistency (Optional)

- Sentence case headings
- Prefer "Analysis" / "Review" / "Report" labels
- Use "domain logic" not "business logic"
- Flat improvement task lists (no speculative effort estimates)
- Avoid unverifiable quantitative claims

---

## 📋 Instruction & Meta Files

Each folder includes:
- `agents.md`: World-class instructions for AI agents and Copilot coding agent, clarifying how to use the prompts for automated code review, technical reporting, and incremental improvements. Domain-specific guidance for each folder.
- `copilot-instructions.md`: Guidance for Copilot/AI tools on how to use the prompts in code review, refactoring, and analysis workflows. Copy into your own repo to standardize AI-assisted reviews.

See each folder for details and usage examples.

---

## 🧭 Usage

1. Pick a domain prompt (e.g. `python/code-refactoring.md`)
2. Copy prompt + relevant code into your AI assistant
3. Save generated report (e.g. `python-refactor-YYYY-MM-DD.md`)
4. Skim top issues, pick 1–2 highest impact
5. Implement & validate (tests / lint / run)
6. Re-run prompt for delta analysis

---

## 📜 License

See `LICENSE` for terms. Prompts may be reused with attribution to the original repository.

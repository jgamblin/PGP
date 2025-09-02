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

## 📂 Prompt Library

### 🌟 Universal Prompts

Analysis prompts for any codebase.

| Prompt | Purpose |
|--------|---------|
| [`ci-cd-pipeline-analysis.md`](./generic/ci-cd-pipeline-analysis.md) | **CI/CD pipeline analysis** |
| [`code-refactoring.md`](./generic/code-refactoring.md) | **Refactoring analysis** with security, performance, and architecture assessment |
| [`documentation-generation.md`](./generic/documentation-generation.md) | **Documentation strategy** with API specs and architectural records |
| [`pr-review-feedback.md`](./generic/pr-review-feedback.md) | **Code review** with security and performance analysis |
| [`project-repo.md`](./generic/project-repo.md) | **Repository setup guide** for creating well-structured project foundations |
| [`system-design-architecture-review.md`](./generic/system-design-architecture-review.md) | **System design and architecture review** |


### 🐍 Python Ecosystem

Python development prompts. All Python prompt files explicitly mention support for all common Python file types, including `.py`, `.pyw`, `.pyx`, `.pxd`, and Jupyter notebooks (`.ipynb`). Prompts are markdown lint clean and ready for use in modern workflows.

| Prompt | Purpose |
|--------|---------|
| [`code-refactoring.md`](./python/code-refactoring.md) | **Python refactoring** with asyncio, Django/Flask/FastAPI optimization |
| [`concurrency-asyncio-pattern-analysis.md`](./python/concurrency-asyncio-pattern-analysis.md) | **Concurrency and asyncio pattern analysis** |
| [`database-schema-orm-optimization.md`](./python/database-schema-orm-optimization.md) | **Database schema and ORM optimization** |
| [`docstring-creation.md`](./python/docstring-creation.md) | **API documentation** with Google/PEP 257 standards |
| [`documentation-generation.md`](./python/documentation-generation.md) | **Python documentation** with Sphinx, type hints, and framework integration |
| [`flake8-compliance.md`](./python/flake8-compliance.md) | **Flake8 compliance check** |
| [`pr-review-feedback.md`](./python/pr-review-feedback.md) | **Python code review** with Django ORM, security, and performance focus |
| [`project-repo.md`](./python/project-repo.md) | **Python repository setup** with Poetry, pytest, and development tooling |
| [`type-hinting.md`](./python/type-hinting.md) | **Type safety analysis** with mypy integration and modern typing |
| [`unit-test-generation.md`](./python/unit-test-generation.md) | **Test strategy and coverage analysis** with pytest best practices |

### 🌐 Frontend & Web

Web development prompts.

| Prompt | Purpose |
|--------|---------|
| [`accessibility-check.md`](./html/accessibility-check.md) | **WCAG compliance audit** with comprehensive accessibility analysis |
| [`bem-naming-convention.md`](./html/bem-naming-convention.md) | **CSS architecture analysis** with BEM methodology implementation |
| [`code-refactoring.md`](./html/code-refactoring.md) | **Frontend refactoring** with React/Vue/Angular, BEM CSS, accessibility |
| [`component-design-system-review.md`](./html/component-design-system-review.md) | **Component design system review** |
| [`documentation-generation.md`](./html/documentation-generation.md) | **Frontend documentation** with Storybook, component libraries, design systems |
| [`navigation-consistency.md`](./html/navigation-consistency.md) | **UX navigation standardization** across multi-page applications |
| [`performance-core-web-vitals-audit.md`](./html/performance-core-web-vitals-audit.md) | **Core Web Vitals performance audit** |
| [`pr-review-feedback.md`](./html/pr-review-feedback.md) | **Frontend code review** with Core Web Vitals, accessibility, performance |
| [`project-repo.md`](./html/project-repo.md) | **Frontend repository setup** with Webpack/Vite, ESLint, and modern tooling |
| [`semantic-markup-refinement.md`](./html/semantic-markup-refinement.md) | **HTML5 semantic optimization** with SEO and performance focus |

### 💎 Ruby Ecosystem

Ruby and Rails development prompts.

| Prompt | Purpose |
|--------|---------|
| [`code-refactoring.md`](./ruby/code-refactoring.md) | **Ruby refactoring** with Rails conventions, metaprogramming, gem patterns |
| [`documentation-generation.md`](./ruby/documentation-generation.md) | **Ruby documentation** with YARD, Rails API docs, gem documentation |
| [`gemfile-management.md`](./ruby/gemfile-management.md) | **Dependency security audit** with version management strategy |
| [`pr-review-feedback.md`](./ruby/pr-review-feedback.md) | **Ruby code review** with Rails security, ActiveRecord optimization |
| [`project-repo.md`](./ruby/project-repo.md) | **Ruby repository setup** with Bundler, RSpec, and Rails conventions |
| [`rails-active-record-performance-audit.md`](./ruby/rails-active-record-performance-audit.md) | **ActiveRecord performance audit** |
| [`rspec-test-generation.md`](./ruby/rspec-test-generation.md) | **RSpec test strategy** with comprehensive coverage planning |
| [`rubocop-compliance.md`](./ruby/rubocop-compliance.md) | **Code quality analysis** with Ruby style guide enforcement |
| [`service-object-domain-logic-refactoring.md`](./ruby/service-object-domain-logic-refactoring.md) | **Service object and domain logic refactoring** |

---

## 🧭 Usage

### Quick Start

```bash
# 1. Pick a domain prompt (e.g. python/code-refactoring.md)
# 2. Copy prompt + relevant code into AI assistant
# 3. Save generated report: name like python-refactor-YYYY-MM-DD.md
# 4. Skim top issues → pick 1–2 highest impact
# 5. Implement & validate (tests / lint / run)
# 6. Re-run prompt for delta analysis
```

### Tools Tested

Windsurf, Claude, GitHub Copilot, Cursor (others should work).

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

## 📜 License

See `LICENSE` for terms. Prompts may be reused with attribution to the original repository.

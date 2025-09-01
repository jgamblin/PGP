# 🚀 Pretty Good Prompts

## Personal AI Coding Assistant Prompt Library

Personal prompt collection by **@JGamblin** – published so others can adapt, but optimized for my workflow.

Curated, practical prompts for common code analysis, review, refactoring, and documentation tasks. Optimized for structured technical output and iterative improvement workflows.

### 🎯 Focus Areas

- **Analysis First** – Structured diagnostics before modification
- **Clean Code & Architecture** – SOLID-aligned, modular design
- **Security Awareness** – Routine review against common vulnerability classes
- **Performance Consideration** – Identify obvious bottlenecks early
- **Testing Mindset** – Encourage coverage and regression safety nets
- **Actionable Documentation** – Persistent technical records

### 🤷 Who Might Find These Useful

- Developers who prefer systematic diagnostics
- Engineers seeking structured review artifacts
- Teams standardizing technical feedback formats
- Anyone improving repository quality and maintainability

---

## 🛠️ Recent Updates (Language & Consistency Cleanup)

Neutral technical wording pass applied across all prompt files:

- Removed marketing / enterprise / executive / strategic style phrases
- Standardized headings to use "Technical Report", "Analysis", or "Review"
- Replaced occurrences of "business logic" with "domain logic" where appropriate
- Normalized dashboard labels (e.g. "Technical Dashboard", "Type Safety Performance Dashboard")
- Reframed ROI / revenue impact wording into reliability, user impact, or maintenance effort
- Unified improvement sections (e.g. renamed "Strategic Improvement Opportunities" → "Technical Improvement Opportunities")
- Cleaned duplicate/legacy sections and fixed markdown spacing & fenced code language tags
- Removed quantified effort estimates
- Standardized implementation tasks as flat to-do lists

If any legacy wording slipped through, it's easy to patch later.

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

Python development prompts.

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

## 🧭 How To Use

### Workflow

```bash
# Step 1: Select the code I want help with
# Step 2: Copy the relevant prompt
# Step 3: Paste it into my AI assistant (usually Windsurf or Claude)
# Step 4: AI generates a detailed report and saves it as a markdown file
# Step 5: Review the saved analysis file
# Step 6: Implement the changes that make sense to me
```

### Compatible AI Tools

- ✅ **Windsurf** - My main IDE, works great
- ✅ **Claude** - Good for detailed analysis
- ✅ **GitHub Copilot** - Works in VS Code
- ✅ **Cursor** - Also pretty good
- 🤔 **Others** - Haven't tried extensively but should work

---

## 📊 Output Characteristics

### Saved Analysis Reports

All prompts generate comprehensive reports saved as dated markdown files:

- `python-test-analysis-2024-01-15.md`
- `ruby-code-review-2024-01-15.md`
- `html-accessibility-analysis-2024-01-15.md`

### Structured Analysis Pattern

Each saved report contains organized feedback like:

```markdown
# Example of what I typically see
## Issues Found
- Potential security problem on line 45
- This algorithm might be slow with large datasets
- Code structure could be cleaner

## Suggestions
1. Fix the input validation
2. Consider using a more efficient algorithm
3. Maybe refactor this into smaller functions
```

### Follow-up Question Pattern

The prompts usually ask helpful questions like:
> *"Want me to help fix that security issue first?"*

Which helps me decide what to tackle next.

### Benefits of Persisted Output

- **Permanent Record**: All analysis reports are saved for future reference
- **Team Sharing**: Easy to share detailed analysis with colleagues
- **Progress Tracking**: Compare reports over time to see improvements
- **Documentation**: Reports serve as technical documentation for decisions

---

## ⚙️ Rationale

### Practical Basis

- I've been writing code for a while and made plenty of mistakes
- I try to follow industry best practices (WCAG, OWASP, SOLID, etc.)
- I update these based on what actually helps in day-to-day work
- I use modern tools and try to stay current

### Practical Focus

- I like getting specific suggestions rather than vague advice
- I want to know what to prioritize when I have limited time
- I prefer step-by-step guidance over theory
- I want to understand why something matters

### Iterative Cycle

How I typically use these:

1. **Analyze** → Figure out what needs attention
2. **Prioritize** → Decide what to tackle first
3. **Implement** → Make changes one at a time
4. **Test** → Make sure I didn't break anything

---

## 🎖️ Core Quality Axes

> **These are the things I try to focus on in my own code.**

- **🔒 Security**: I check for common vulnerabilities (OWASP Top 10, etc.)
- **⚡ Performance**: I look for obvious bottlenecks and inefficiencies
- **🏗️ Clean Architecture**: I try to follow SOLID principles when I remember
- **🧪 Testing**: I aim for good test coverage (though I don't always achieve it)
- **📚 Documentation**: I document things so future me understands the code

---

## 📈 Expected Outcomes

| What I'm Aiming For | Reality Check |
|---------------------|---------------|
| **Faster Development** | Helps me catch issues earlier |
| **Better Code Quality** | My code has gotten cleaner over time |
| **Fewer Security Issues** | I catch more problems before they hit production |
| **Better Performance** | I'm more aware of performance implications |
| **Less Technical Debt** | My code is easier to maintain now |
| **Better Testing** | I write more tests than I used to |

**Disclaimer**: Results vary by codebase size, team norms, and tooling maturity.

---

## 🔀 Fork & Adapt (No Direct PRs)

I am not accepting pull requests. If you want to extend or alter these:

1. Fork the repository
2. Adjust wording / sections to match your team or tooling
3. Rename or reorganize prompts as needed
4. Remove sections you don't use to reduce noise
5. Maintain attribution if large portions are reused

Feel free to publish your own variant.

## 📜 License

See `LICENSE` for terms. Prompts may be reused with attribution to the original repository.

---

## 🔍 Quick Start (TL;DR)

1. Select domain prompt (e.g. Python refactoring)
2. Paste prompt + target code into your AI assistant
3. Receive structured analysis markdown
4. Save under dated filename
5. Triage high-impact items first
6. Implement + re-run for regression confirmation

---

## ✅ Style Consistency Checklist (Optional)

- Headings: Use sentence case except proper nouns
- Sections: Favor "Analysis", "Review", "Report" over marketing terms
- Replace "business logic" with "domain logic"
- Prefer "improvement tasks" over "action plan" / "strategic initiatives"
- Avoid unverifiable quantitative impact claims

# 🚀 Pretty Good Prompts
## JGamblin's Personal AI Coding Assistant Prompts

**⚠️ PERSONAL COLLECTION - USE AT YOUR OWN RISK**  

These are my personal prompts that I've developed to help with common coding issues. I'm sharing them in case others find them useful, but they reflect my own preferences and workflow.

### 🎯 **What I Focus On**

- **📊 Analysis-First**: I prefer getting detailed reports before making changes
- **🏗️ Clean Code**: I try to follow SOLID principles and good architecture
- **🛡️ Security**: I've learned to always think about security implications
- **⚡ Performance**: I care about making code that runs efficiently
- **🧪 Testing**: I believe in comprehensive testing (when I remember to write it)
- **📚 Documentation**: I document things so I don't forget how they work

### 🤷 **Who Might Find These Useful**

These prompts work for me, but your mileage may vary:
- Developers who like detailed code analysis
- People who want structured feedback on their code
- Teams that care about code quality and security
- Anyone who wants to improve their development process

---

## � Recent Updates (Language & Consistency Cleanup)

Neutral technical wording pass applied across all prompt files:

- Removed marketing / enterprise / executive / strategic style phrases
- Standardized headings to use "Technical Report", "Analysis", or "Review"
- Replaced occurrences of "business logic" with "domain logic" where appropriate
- Normalized dashboard labels (e.g. "Technical Dashboard", "Type Safety Performance Dashboard")
- Reframed ROI / revenue impact wording into reliability, user impact, or maintenance effort
- Unified improvement sections (e.g. renamed "Strategic Improvement Opportunities" → "Technical Improvement Opportunities")
- Cleaned duplicate/legacy sections and fixed markdown spacing & fenced code language tags

If any legacy wording slipped through, it's easy to patch later.

---

## �📂 **Prompt Library**

### 🌟 **Universal Prompts**

Analysis prompts for any codebase.

| Prompt | Purpose |
|--------|---------|
| [`ci-cd-pipeline-analysis.md`](./generic/ci-cd-pipeline-analysis.md) | **CI/CD pipeline analysis** |
| [`code-refactoring.md`](./generic/code-refactoring.md) | **Refactoring analysis** with security, performance, and architecture assessment |
| [`documentation-generation.md`](./generic/documentation-generation.md) | **Documentation strategy** with API specs and architectural records |
| [`pr-review-feedback.md`](./generic/pr-review-feedback.md) | **Code review** with security and performance analysis |
| [`project-repo.md`](./generic/project-repo.md) | **Repository setup guide** for creating well-structured project foundations |
| [`system-design-architecture-review.md`](./generic/system-design-architecture-review.md) | **System design and architecture review** |

### 🐍 **Python Ecosystem**

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

### 🌐 **Frontend & Web**

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

### 💎 **Ruby Ecosystem**

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

## 🛠️ **How I Use These**

### **My Workflow**

```bash
# Step 1: Select the code I want help with
# Step 2: Copy the relevant prompt
# Step 3: Paste it into my AI assistant (usually Windsurf or Claude)
# Step 4: AI generates a detailed report and saves it as a markdown file
# Step 5: Review the saved analysis file
# Step 6: Implement the changes that make sense to me
```

### **AI Tools I've Tested With**

- ✅ **Windsurf** - My main IDE, works great
- ✅ **Claude** - Good for detailed analysis
- ✅ **GitHub Copilot** - Works in VS Code
- ✅ **Cursor** - Also pretty good
- 🤔 **Others** - Haven't tried extensively but should work

---

## 📊 **What These Prompts Give Me**

### **📁 Saved Analysis Reports**

All prompts generate comprehensive reports saved as dated markdown files:

- `python-test-analysis-2024-01-15.md`
- `ruby-code-review-2024-01-15.md`
- `html-accessibility-analysis-2024-01-15.md`

### **📋 Structured Analysis**

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

### **🎯 Follow-up Questions**

The prompts usually ask helpful questions like:
> *"Want me to help fix that security issue first?"*

Which helps me decide what to tackle next.

### **💾 File Output Benefits**

- **Permanent Record**: All analysis reports are saved for future reference
- **Team Sharing**: Easy to share detailed analysis with colleagues
- **Progress Tracking**: Compare reports over time to see improvements
- **Documentation**: Reports serve as technical documentation for decisions

---

## ⚡ **Why I Think These Work**

### **🧠 Based on Real Experience**

- I've been writing code for a while and made plenty of mistakes
- I try to follow industry best practices (WCAG, OWASP, SOLID, etc.)
- I update these based on what actually helps in day-to-day work
- I use modern tools and try to stay current

### **🎯 Practical Focus**

- I like getting specific suggestions rather than vague advice
- I want to know what to prioritize when I have limited time
- I prefer step-by-step guidance over theory
- I want to understand why something matters

### **🔄 My Process**

How I typically use these:

1. **Analyze** → Figure out what needs attention
2. **Prioritize** → Decide what to tackle first
3. **Implement** → Make changes one at a time
4. **Test** → Make sure I didn't break anything

---

## 🎖️ **What I Care About**

> **These are the things I try to focus on in my own code.**

- **🔒 Security**: I check for common vulnerabilities (OWASP Top 10, etc.)
- **⚡ Performance**: I look for obvious bottlenecks and inefficiencies
- **🏗️ Clean Architecture**: I try to follow SOLID principles when I remember
- **🧪 Testing**: I aim for good test coverage (though I don't always achieve it)
- **📚 Documentation**: I document things so future me understands the code

---

## 📈 **What I Hope You Get Out of These**

| What I'm Aiming For | Reality Check |
|---------------------|---------------|
| **Faster Development** | Helps me catch issues earlier |
| **Better Code Quality** | My code has gotten cleaner over time |
| **Fewer Security Issues** | I catch more problems before they hit production |
| **Better Performance** | I'm more aware of performance implications |
| **Less Technical Debt** | My code is easier to maintain now |
| **Better Testing** | I write more tests than I used to |

**Disclaimer**: Your results will definitely vary. These work for my style and the kind of projects I work on, but everyone's different.

---


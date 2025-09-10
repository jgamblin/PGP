# 🚀 Pretty Good Prompts

## Personal AI Coding Assistant Prompt Library

Personal prompt collection by **[@JGamblin](https://github.com/JGamblin)**. Shared so others can adapt—optimized for personal projects and proof-of-concept development with practical, actionable guidance.

### Who This Helps

- Engineers who want structured, repeatable analysis output
- People standardizing review/report formats
- Anyone reducing technical debt with evidence-based refactors

---


## 📂 Repository Structure & File Index

### Top-Level Files
- `LICENSE` — License terms for reuse.
- `README.md` — This documentation.

**Total: 37 normalized prompts across all technology stacks**

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
| `cli-application-development.md` | Professional CLI development (Click, Rich, testing) |
| `code-refactoring.md` | Python refactoring (asyncio, Django/Flask/FastAPI, modern patterns) |
| `concurrency-asyncio-pattern-analysis.md` | Concurrency and asyncio pattern analysis |
| `copilot-instructions.md` | Copilot/AI guidance for Python prompt usage |
| `database-schema-orm-optimization.md` | Database schema and ORM optimization |
| `documentation-generation.md` | Comprehensive Python documentation (docstrings, Sphinx, API docs) |
| `logging-error-handling.md` | Logging setup, structured error handling, security events |
| `packaging-distribution.md` | Modern Python packaging (Poetry, pyproject.toml, PyPI) |
| `pr-review-feedback.md` | Python code review (ORM, security, performance) |
| `project-repo.md` | Python repository setup (Poetry, pytest) |
| `python-linting.md` | Modern code linting and formatting (Ruff, Black, Flake8) |
| `security-analysis.md` | Security vulnerability analysis and secure coding practices |
| `type-hinting.md` | Type safety analysis (mypy, modern typing) |
| `unit-test-generation.md` | Test strategy and coverage analysis (pytest) |

---

---

### 🏗️ `infrastructure/` — DevOps & Infrastructure Prompts
| File | Purpose |
|------|---------|
| `aws-ec2-deployment.md` | EC2 instance selection, containerized deployment scripts |
| `docker-containerization.md` | Container optimization, multi-stage builds, orchestration |

---

### 🌐 `html/` — Frontend & Web Prompts
| File | Purpose |
|------|---------|
| `accessibility-check.md` | WCAG compliance audit (accessibility) |
| `agents.md` | Agent instructions for frontend prompt usage |
| `bem-naming-convention.md` | CSS architecture analysis (BEM) |
| `code-refactoring.md` | Frontend refactoring (React/Vue/Angular, BEM, accessibility) |
| `component-design-system-review.md` | Component design system review and optimization |
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
| `rails-active-record-performance-audit.md` | ActiveRecord performance optimization and N+1 query detection |
| `rspec-test-generation.md` | RSpec test strategy (coverage planning) |
| `rubocop-compliance.md` | Code quality analysis (Rubocop) |
| `service-object-domain-logic-refactoring.md` | Service object and domain logic refactoring |

---


## 🔀 Fork & Adapt (No Direct PRs)

I am not accepting pull requests. If you want to extend or alter these:

1. Fork the repository
2. Adjust wording / sections to match your team or tooling
3. Rename or reorganize prompts as needed
4. Remove sections you don't use to reduce noise
5. Maintain attribution if large portions are reused

Feel free to publish your own variant.

## 🎯 Which Prompt Should I Use?

### "My code is messy and hard to understand"
**Python:** `python/code-refactoring.md` - Python Code Helper  
**Ruby:** `ruby/code-refactoring.md` - Ruby Code Helper  
**Frontend:** `html/code-refactoring.md` - Frontend Code Helper  
**Any Language:** `generic/code-refactoring.md` - Code Refactoring Helper  

### "I need to add tests to my project"
**Python:** `python/unit-test-generation.md` - Python Testing Assistant  
**Ruby:** `ruby/rspec-test-generation.md` - Ruby Testing Assistant  
**Any Language:** Use language-specific testing prompts  

### "I want feedback on my code changes"
**Python:** `python/pr-review-feedback.md` - Python Code Review Assistant  
**Ruby:** `ruby/pr-review-feedback.md` - Ruby Code Review Assistant  
**Frontend:** `html/pr-review-feedback.md` - Frontend Code Review Assistant  
**Any Language:** `generic/pr-review-feedback.md` - Code Review Helper  

### "My project needs better documentation"
**Python:** `python/documentation-generation.md` - Python Documentation Assistant  
**Ruby:** `ruby/documentation-generation.md` - Ruby Documentation Assistant  
**Frontend:** `html/documentation-generation.md` - Frontend Documentation Assistant  
**Any Language:** `generic/documentation-generation.md` - Documentation Helper  

### "I need to set up a new project"
**Any Language:** `generic/project-repo.md` - Project Setup Helper  
- Repository structure and organization
- README templates and essential files
- Development tools and CI/CD setup

### "My website is slow or has accessibility issues"
**Frontend:** `html/performance-core-web-vitals-audit.md` - Web Performance Helper  
**Frontend:** `html/accessibility-check.md` - Web Accessibility Helper  
**Frontend:** `html/semantic-markup-refinement.md` - HTML Semantic Helper  

### "I need help with specific technologies"
**Python Types:** `python/type-hinting.md` - Python Type Hints Assistant  
**Python Docs:** `python/documentation-generation.md` - Python Documentation Assistant  
**Python Database:** `python/database-schema-orm-optimization.md` - Database & ORM Assistant  
**Python CLI:** `python/cli-application-development.md` - Python CLI Assistant  
**Python Packaging:** `python/packaging-distribution.md` - Python Packaging Assistant  
**Python Logging:** `python/logging-error-handling.md` - Python Logging Assistant  
**Python Security:** `python/security-analysis.md` - Python Security Assistant  
**Python Linting:** `python/python-linting.md` - Python Code Style Assistant  
**Ruby Style:** `ruby/rubocop-compliance.md` - Ruby Style Guide Helper  
**Ruby Gems:** `ruby/gemfile-management.md` - Ruby Dependencies Helper  
**Ruby Services:** `ruby/service-object-domain-logic-refactoring.md` - Ruby Service Objects Helper  
**CSS Organization:** `html/bem-naming-convention.md` - CSS Organization Helper  
**Navigation:** `html/navigation-consistency.md` - Navigation Helper

### "I need help with infrastructure and DevOps"
**Docker:** `infrastructure/docker-containerization.md` - Docker Container Assistant  
**AWS EC2:** `infrastructure/aws-ec2-deployment.md` - AWS EC2 Deployment Assistant  

### "I need help with development workflow"
**CI/CD:** `generic/ci-cd-pipeline-analysis.md` - CI/CD Pipeline Helper  
**Architecture:** `generic/system-design-architecture-review.md` - Architecture Review Helper  
**AI Tools:** `generic/copilot-instructions.md` - AI Assistant Instructions Helper  
**Project Planning:** `generic/do-next.md` - Project Next Steps Helper  
**General Help:** `generic/agents.md` - Generic Development Helper

---

## ⚡ Quick Commands by Technology

Copy and paste these into your AI assistant:

### Python Projects
```
# Code cleanup
Use the Python Code Helper prompt to review this code and suggest improvements:
[paste your Python code]

# Add tests
Use the Python Testing Assistant prompt to create pytest tests for this function:
[paste your function]

# Add type hints
Use the Python Type Hints Assistant prompt to add type annotations:
[paste your code]

# Database optimization
Use the Database & ORM Assistant prompt to optimize these models:
[paste your Django/SQLAlchemy models]

# Function documentation
Use the Python Documentation Assistant prompt to write docstrings:
[paste your functions]

# Code linting and formatting
Use the Python Code Style Assistant prompt to improve code style:
[paste your Python code]

# CLI application
Use the Python CLI Assistant prompt to build command-line tools:
[describe your CLI needs or paste existing code]

# Package for distribution
Use the Python Packaging Assistant prompt to package your project:
[describe your project structure]

# Add logging and error handling
Use the Python Logging Assistant prompt to improve error handling:
[paste your code]

# Security analysis
Use the Python Security Assistant prompt to find vulnerabilities:
[paste your code or describe security concerns]
```

### Infrastructure & DevOps Projects
```
# Containerize application
Use the Docker Container Assistant prompt to create optimized containers:
[describe your application stack or paste existing Dockerfile]

# Deploy to AWS EC2
Use the AWS EC2 Deployment Assistant prompt to deploy containerized apps:
[describe your application requirements and expected traffic]
```

### Ruby/Rails Projects
```
# Code cleanup
Use the Ruby Code Helper prompt to improve this Ruby code:
[paste your Ruby code]

# Add RSpec tests
Use the Ruby Testing Assistant prompt to create RSpec tests:
[paste your Ruby class or method]

# Check Ruby style
Use the Ruby Style Guide Helper prompt to review code style:
[paste your Ruby code]

# Extract service objects
Use the Ruby Service Objects Helper prompt to refactor this controller:
[paste your Rails controller]

# Manage dependencies
Use the Ruby Dependencies Helper prompt to review my Gemfile:
[paste your Gemfile]
```

### Frontend Projects
```
# Improve HTML/CSS/JS
Use the Frontend Code Helper prompt to improve this code:
[paste your frontend code]

# Check accessibility
Use the Web Accessibility Helper prompt to review this component:
[paste your HTML/React component]

# Optimize performance
Use the Web Performance Helper prompt to speed up this page:
[describe your performance issues or paste code]

# Organize CSS
Use the CSS Organization Helper prompt to improve this stylesheet:
[paste your CSS]

# Improve HTML semantics
Use the HTML Semantic Helper prompt to review this markup:
[paste your HTML]
```

### Any Project Type
```
# Project setup
Use the Project Setup Helper prompt to organize my repository:
[describe your project type and needs]

# Code review
Use the Code Review Helper prompt to review these changes:
[paste your git diff or changed code]

# Documentation
Use the Documentation Helper prompt to create docs for this project:
[describe your project or paste code]

# CI/CD setup
Use the CI/CD Pipeline Helper prompt to set up automation:
[describe your project and deployment needs]

# Architecture review
Use the Architecture Review Helper prompt to evaluate this design:
[describe your system or paste architecture diagrams]
```

---

## 🔄 Common Workflows by Technology

### Python Web App (Django/Flask)
1. **Setup:** `generic/project-repo.md` → **Code:** `python/code-refactoring.md` → **Linting:** `python/python-linting.md` → **Tests:** `python/unit-test-generation.md` → **Database:** `python/database-schema-orm-optimization.md` → **Security:** `python/security-analysis.md` → **Logging:** `python/logging-error-handling.md` → **Containerize:** `infrastructure/docker-containerization.md` → **Deploy:** `infrastructure/aws-ec2-deployment.md` → **Review:** `python/pr-review-feedback.md`

### Ruby on Rails App
1. **Setup:** `generic/project-repo.md` → **Code:** `ruby/code-refactoring.md` → **Services:** `ruby/service-object-domain-logic-refactoring.md` → **Tests:** `ruby/rspec-test-generation.md` → **Style:** `ruby/rubocop-compliance.md`

### Frontend React/Vue App
1. **Setup:** `generic/project-repo.md` → **Code:** `html/code-refactoring.md` → **Performance:** `html/performance-core-web-vitals-audit.md` → **Accessibility:** `html/accessibility-check.md` → **CSS:** `html/bem-naming-convention.md`

### Any Project - Quick Cleanup
1. **Review:** `generic/pr-review-feedback.md` → **Refactor:** Language-specific `code-refactoring.md` → **Document:** `generic/documentation-generation.md`

### Infrastructure Project - Simple Stack
1. **Containers:** `infrastructure/docker-containerization.md` → **Deploy:** `infrastructure/aws-ec2-deployment.md`

### Any Project - Production Ready
1. **Architecture:** `generic/system-design-architecture-review.md` → **Code Quality:** Language-specific prompts → **CI/CD:** `generic/ci-cd-pipeline-analysis.md` → **Final Review:** `generic/pr-review-feedback.md`

---

## 🚀 Personal Project Quick Start Guide

### Python Projects
1. **Start with**: `python/code-refactoring.md` - Clean up your Python code with modern patterns
2. **Code quality**: `python/python-linting.md` - Format and lint with Ruff and Black
3. **Add testing**: `python/unit-test-generation.md` - Cover key functionality with pytest
4. **Add types**: `python/type-hinting.md` - Catch bugs with type hints
5. **Document**: `python/documentation-generation.md` - Create comprehensive documentation
6. **Security**: `python/security-analysis.md` - Find and fix security vulnerabilities
7. **Package**: `python/packaging-distribution.md` - Prepare for distribution with Poetry
8. **CLI tools**: `python/cli-application-development.md` - Build professional command-line interfaces
9. **Logging**: `python/logging-error-handling.md` - Add robust logging and error handling

### Ruby/Rails Projects
1. **Start with**: `ruby/code-refactoring.md` - Improve Ruby code quality
2. **Add testing**: `ruby/rspec-test-generation.md` - Write comprehensive RSpec tests
3. **Check style**: `ruby/rubocop-compliance.md` - Follow Ruby style guidelines
4. **Manage gems**: `ruby/gemfile-management.md` - Keep dependencies secure

### HTML/CSS/Frontend Projects
1. **Start with**: `html/code-refactoring.md` - Improve frontend code structure
2. **Check accessibility**: `html/accessibility-check.md` - Make sites accessible
3. **Containerize**: `infrastructure/docker-containerization.md` - Package for deployment
4. **Deploy**: `infrastructure/aws-ec2-deployment.md` - Deploy to AWS EC2

### Infrastructure & DevOps Projects
1. **Containerize**: `infrastructure/docker-containerization.md` - Create optimized containers
2. **Deploy**: `infrastructure/aws-ec2-deployment.md` - Deploy to AWS EC2 with automation scripts
3. **Optimize performance**: `html/performance-core-web-vitals-audit.md` - Speed up loading
4. **Improve CSS**: `html/bem-naming-convention.md` - Better CSS organization

### Any Project Type (Generic)
1. **Project setup**: `generic/project-repo.md` - Organize your repository
2. **Code review**: `generic/pr-review-feedback.md` - Get feedback on changes
3. **Documentation**: `generic/documentation-generation.md` - Write clear docs
4. **CI/CD**: `generic/ci-cd-pipeline-analysis.md` - Automate testing and deployment

---

## 🧭 How to Use These Prompts

1. Pick a domain prompt (e.g. `python/code-refactoring.md`)
2. Copy prompt + relevant code into your AI assistant
3. Save generated report (e.g. `python-refactor-YYYY-MM-DD.md`)
4. Skim top issues, pick 1–2 highest impact
5. Implement & validate (tests / lint / run)
6. Re-run prompt for delta analysis

---

## 📋 Instruction & Meta Files

Each folder includes:
- `agents.md`: Instructions for AI agents and Copilot coding agent, clarifying how to use the prompts for automated code review, technical reporting, and incremental improvements. Domain-specific guidance for each folder.
- `copilot-instructions.md`: Guidance for Copilot/AI tools on how to use the prompts in code review, refactoring, and analysis workflows. Copy into your own repo to standardize AI-assisted reviews.

See each folder for details and usage examples.

---

## 🛠️ Recent Cleanup Snapshot

- Normalized all prompts across Python, Ruby, HTML/CSS, and Generic technology stacks
- **Python Collection Enhanced**: Added 4 new essential prompts and modernized existing ones
  - New: CLI development, packaging/distribution, logging/error handling, security analysis
  - Updated: Consolidated documentation prompts, modernized linting with Ruff/Black
  - Enhanced: Code refactoring with Python-specific patterns (dataclasses, context managers, etc.)
- **Infrastructure Collection Added**: 2 focused DevOps prompts for personal projects
  - Docker containerization with multi-stage builds and security best practices
  - AWS EC2 deployment with instance selection and automated deployment scripts
- Transformed enterprise-focused prompts into practical personal project helpers
- Consolidated PERSONAL_PROJECT_GUIDE.md and QUICK_REFERENCE.md into README.md
- Standardized role statements and removed "world-class" language
- Added comprehensive quick start guides and workflows by technology
- Unified prompt naming conventions (e.g., "Python Code Helper", "Ruby Testing Assistant")
- **Modern Python Tooling**: Updated all Python prompts to feature current best practices
  - Ruff for ultra-fast linting (10-100x faster than Flake8)
  - Poetry for modern dependency management and packaging
  - Click and Rich for professional CLI applications
  - Structured logging and comprehensive security analysis
- **Practical Infrastructure Approach**: Simple, effective deployment toolkit
  - Container-first development with Docker optimization and security
  - AWS EC2 deployment with cost-effective instance selection and automation
  - Complete deployment scripts for containerized applications
  - Focus on personal projects and proof-of-concept deployments
- Removed quantified hour/effort estimates and enterprise jargon
- Added copy-paste command examples for immediate use

---

## 📜 License

See `LICENSE` for terms. Prompts may be reused with attribution to the original repository.

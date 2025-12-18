# Ruby/Rails Prompts — Index

> **Purpose**: Index of all Ruby/Rails assistant prompts  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: Ruby 3.x, Rails 7+, RSpec, RuboCop  
> **Last Updated**: 2025-12

---

## Available Prompts

| Prompt | Purpose | Use When |
|--------|---------|----------|
| [code-refactoring.md](code-refactoring.md) | Ruby code improvements | Cleaning up methods, using idioms |
| [copilot-instructions.md](copilot-instructions.md) | AI assistant config | Setting up Copilot for Ruby/Rails |
| [documentation-generation.md](documentation-generation.md) | YARD docs, READMEs | Documenting classes and APIs |
| [gemfile-management.md](gemfile-management.md) | Dependency management | Organizing Gemfile, security |
| [pr-review-feedback.md](pr-review-feedback.md) | Pull request review | Reviewing Ruby code changes |
| [project-repo.md](project-repo.md) | Project structure | Setting up new Ruby/Rails projects |
| [rails-active-record-performance-audit.md](rails-active-record-performance-audit.md) | Database performance | N+1 queries, indexes, caching |
| [rspec-test-generation.md](rspec-test-generation.md) | RSpec tests | Writing model, controller, feature specs |
| [rubocop-compliance.md](rubocop-compliance.md) | Code style | RuboCop setup and fixes |
| [service-object-domain-logic-refactoring.md](service-object-domain-logic-refactoring.md) | Architecture | Extracting service objects |

---

## Quick Start Prompts

### Prompt: Review My Ruby Code
```text
Review this Ruby code for improvements:

{{CODE}}

Check for:
1. Ruby idioms and style
2. Method complexity
3. Error handling
4. Performance issues
5. Test suggestions
```

### Prompt: Set Up Rails Project
```text
Help me set up a new Rails project:

Project: {{PROJECT_NAME}}
Ruby: 3.3
Rails: 7.1
Database: {{DATABASE}}
Features: {{FEATURES}}

Include:
- Gemfile essentials
- RuboCop config
- RSpec setup
- CI configuration
```

### Prompt: Fix N+1 Queries
```text
Analyze this Rails code for N+1 query problems:

{{CODE}}

For each issue:
1. Show the problematic code
2. Explain the query pattern
3. Provide eager loading fix
4. Show resulting queries
```

---

## Severity Guide

| Level | Icon | Action | Examples |
|-------|------|--------|----------|
| **Critical** | 🔴 | Fix immediately | Security holes, data loss, crashes |
| **High** | 🟠 | Fix before merge | N+1 queries, broken validations |
| **Medium** | 🟡 | Should fix | Style issues, missing tests |
| **Low** | 🟢 | Consider | Minor optimizations |

---

## Workflow Recommendations

### New Rails Feature
1. **Plan**: Use [service-object-domain-logic-refactoring.md](service-object-domain-logic-refactoring.md) for architecture
2. **Build**: Follow Rails conventions
3. **Test**: Use [rspec-test-generation.md](rspec-test-generation.md) for specs
4. **Review**: Use [pr-review-feedback.md](pr-review-feedback.md) before merge

### Performance Investigation
1. **Audit**: Use [rails-active-record-performance-audit.md](rails-active-record-performance-audit.md)
2. **Fix**: Address N+1 queries and missing indexes
3. **Verify**: Check query counts in test logs

### Code Quality Sprint
1. **Style**: Use [rubocop-compliance.md](rubocop-compliance.md) for RuboCop setup
2. **Refactor**: Use [code-refactoring.md](code-refactoring.md) for improvements
3. **Document**: Use [documentation-generation.md](documentation-generation.md) for YARD docs

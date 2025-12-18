# Ruby/Rails Copilot Instructions — AI Configuration

> **Purpose**: Configure AI assistants for Ruby/Rails development  
> **Best For**: GitHub Copilot, VS Code settings  
> **Scope**: Ruby 3.x, Rails 7+, RSpec  
> **Last Updated**: 2025-12

---

## Mission

Configure AI assistants to generate **idiomatic Ruby code** following Rails conventions, modern patterns, and project standards.

---

## Guard Clauses

**If no project context:**
```
NO_PROJECT_CONTEXT

To configure AI for your Ruby project, I need:
- Ruby version
- Rails version (if applicable)
- Key gems (RSpec, RuboCop config)
- Coding conventions

Or share your Gemfile and .rubocop.yml.
```

---

## Quick Context Checklist

```
☐ Ruby version
☐ Rails version (if Rails project)
☐ Testing framework (RSpec, Minitest)
☐ Style guide (RuboCop rules)
☐ Project-specific patterns
```

---

## Copy-Paste Prompts

### Prompt: Generate Copilot Instructions
```text
Generate .github/copilot-instructions.md for my Ruby/Rails project:

Ruby: {{RUBY_VERSION}}
Rails: {{RAILS_VERSION}}
Testing: {{TEST_FRAMEWORK}}
Style: {{STYLE_PREFERENCES}}

Include rules for:
- Ruby idioms
- Rails conventions
- Testing patterns
- Security practices
```

### Prompt: Add Project Context
```text
Based on my Gemfile and .rubocop.yml:

Gemfile:
{{GEMFILE}}

.rubocop.yml:
{{RUBOCOP_CONFIG}}

Generate AI instructions that match my project's conventions.
```

---

## Copilot Instructions Template

### .github/copilot-instructions.md

```markdown
# Ruby/Rails AI Assistant Guidelines

## Project Overview
- Ruby 3.3, Rails 7.1
- PostgreSQL database
- RSpec for testing
- RuboCop + Standard for style

## Code Style

### Ruby Conventions
- Use Ruby 3.x syntax (endless methods, pattern matching when clearer)
- Prefer keyword arguments for methods with 3+ parameters
- Use guard clauses instead of nested conditionals
- Prefer `&:method` syntax for simple blocks
- Use frozen string literals (`# frozen_string_literal: true`)

### Rails Conventions
- Follow RESTful resource patterns
- Keep controllers thin (max 5 public methods)
- Use strong parameters in controllers
- Prefer scopes over class methods for queries
- Use concerns for shared model behavior

### Naming
- snake_case for methods, variables, files
- CamelCase for classes and modules
- SCREAMING_SNAKE_CASE for constants
- Descriptive names over abbreviations
- `?` suffix for boolean methods
- `!` suffix for dangerous/mutating methods

## Testing

### RSpec Style
- Use `describe`/`context`/`it` structure
- One expectation per test when practical
- Use `let` for lazy-loaded test data
- Use `let!` when data must exist before test
- Prefer factories (FactoryBot) over fixtures
- Use `subject` for the object under test

### Test Organization
```ruby
describe ClassName do
  describe '#instance_method' do
    context 'when condition' do
      it 'does expected behavior' do
      end
    end
  end
end
```

## Security

### Always
- Use `params.require().permit()` for mass assignment
- Escape user input in views (automatic in ERB)
- Use `find_by` not `find_by_sql` with user input
- Store secrets in credentials, not code

### Never
- Never use `eval` with user input
- Never disable CSRF protection
- Never expose sensitive data in logs
- Never commit secrets to git

## Database

### ActiveRecord
- Use migrations for schema changes
- Add indexes for foreign keys and frequently queried columns
- Use `includes` to prevent N+1 queries
- Use scopes for reusable query logic
- Prefer `find_each` for batch processing

### Query Style
```ruby
# Good
User.active.where(role: :admin).includes(:profile)

# Avoid
User.where("active = ? AND role = ?", true, 'admin')
```

## Common Patterns

### Service Objects
- One public method: `call`
- Return result objects, not booleans
- Keep under 100 lines

### Form Objects
- Inherit from `ActiveModel::Model`
- Encapsulate complex form logic
- Handle validations for non-model forms

### Background Jobs
- Keep jobs small and idempotent
- Use `perform_later` for async work
- Handle failures gracefully

## DO NOT

- Generate code with SQL injection vulnerabilities
- Skip validation in models
- Use `update_all` without understanding side effects
- Generate `binding.pry` in production code
- Create N+1 query patterns
```

---

## VS Code Settings

### settings.json (Ruby/Rails)
```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "Shopify.ruby-lsp",
  "[ruby]": {
    "editor.tabSize": 2,
    "editor.insertSpaces": true,
    "editor.rulers": [80, 120]
  },
  "rubyLsp.formatter": "rubocop",
  "github.copilot.enable": {
    "*": true
  }
}
```

---

## Framework-Specific Settings

### Rails API Project
```markdown
## Additional Rules

### Controllers
- Use `ActionController::API` as base
- Return JSON responses only
- Use serializers (Blueprinter, Alba) for response formatting
- Version APIs in routes: `/api/v1/`

### Authentication
- Use token-based auth (JWT or API keys)
- Implement rate limiting
- Log all authentication failures
```

### Gem/Library Project
```markdown
## Additional Rules

### Public API
- Document all public methods with YARD
- Keep public API minimal
- Version following SemVer
- Include CHANGELOG.md

### Compatibility
- Support Ruby 3.0+
- Minimize dependencies
- Test against multiple Ruby versions
```

---

## Report Format

### Generated Config: `copilot-instructions-[YYYY-MM-DD].md`

```markdown
# AI Configuration Summary

## Project Detection
- Ruby: [version]
- Rails: [version]
- Testing: [framework]
- Style: [rubocop config]

## Generated Instructions
[Full copilot-instructions.md content]

## Custom Rules Added
- [Project-specific rule 1]
- [Project-specific rule 2]
```

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | Security misconfigurations |
| **High** | 🟠 | Wrong framework version assumptions |
| **Medium** | 🟡 | Missing project conventions |
| **Low** | 🟢 | Style preference variations |

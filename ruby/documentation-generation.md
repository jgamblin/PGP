# Ruby Documentation Generation — YARD & README

> **Purpose**: Generate documentation for Ruby classes, methods, and projects  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: YARD docs, README files, API documentation  
> **Last Updated**: 2025-12

---

## Mission

Create **clear, maintainable documentation** for Ruby code. Generate YARD docs, README files, and API references that help developers understand and use your code.

---

## Guard Clauses

**If no code provided:**
```
NO_CODE_PROVIDED

Please share the Ruby code to document:
- Class or module
- Method signatures
- Or describe what you need documented

I'll generate appropriate YARD docs.
```

**If already well-documented:**
```
DOCS_LOOK_GOOD

✅ **Well-Documented Code**

Documentation coverage is good:
- All public methods documented ✓
- Parameters described ✓
- Return values specified ✓
- Examples included ✓

Minor suggestions (optional):
[list any improvements]
```

---

## Quick Context Checklist

```
☐ Ruby code to document
☐ Documentation type (YARD, README, API)
☐ Audience (internal team, open source, API consumers)
☐ Existing documentation (if any)
☐ Project context
```

---

## Copy-Paste Prompts

### Prompt: Generate YARD Documentation
```text
Generate YARD documentation for this Ruby code:

{{CODE}}

Include:
- Class/module description
- Method descriptions
- @param tags with types
- @return tags with types
- @example blocks
- @raise tags if applicable
```

### Prompt: Create README
```text
Create a README.md for this Ruby project:

Project: {{PROJECT_NAME}}
Purpose: {{PURPOSE}}
Key features: {{FEATURES}}

Include:
- Installation instructions
- Quick start example
- Configuration options
- API overview
- Contributing guidelines
```

### Prompt: Document API Endpoints
```text
Document these Rails controller actions:

{{CONTROLLER_CODE}}

For each endpoint:
- HTTP method and path
- Parameters (required/optional)
- Response format
- Example request/response
- Error responses
```

### Prompt: Generate Changelog Entry
```text
Generate a CHANGELOG entry for these changes:

{{CHANGES}}

Format: Keep a Changelog style
Include: Added, Changed, Fixed, Removed sections
```

---

## YARD Documentation Reference

### Class Documentation
```ruby
# Handles user authentication and session management.
#
# This class provides methods for authenticating users via various
# strategies (password, OAuth, API key) and managing their sessions.
#
# @example Basic authentication
#   authenticator = Authenticator.new(strategy: :password)
#   result = authenticator.authenticate(email: 'user@example.com', password: 'secret')
#   if result.success?
#     session[:user_id] = result.user.id
#   end
#
# @author Your Name
# @since 1.0.0
class Authenticator
end
```

### Method Documentation
```ruby
# Authenticates a user with the given credentials.
#
# Attempts to authenticate using the configured strategy. Returns a result
# object indicating success or failure with appropriate error messages.
#
# @param email [String] the user's email address
# @param password [String] the user's password
# @param remember [Boolean] whether to create a persistent session (default: false)
#
# @return [AuthResult] result object with success status and user/errors
#
# @raise [InvalidCredentialsError] if email format is invalid
# @raise [RateLimitError] if too many failed attempts
#
# @example Successful authentication
#   result = authenticate(email: 'user@example.com', password: 'secret')
#   result.success? # => true
#   result.user     # => #<User id: 1, email: "user@example.com">
#
# @example Failed authentication
#   result = authenticate(email: 'user@example.com', password: 'wrong')
#   result.success? # => false
#   result.errors   # => ["Invalid password"]
#
# @see #logout
# @see AuthResult
def authenticate(email:, password:, remember: false)
end
```

### Common YARD Tags

| Tag | Purpose | Example |
|-----|---------|---------|
| `@param` | Document parameter | `@param name [String] the user's name` |
| `@return` | Document return value | `@return [User] the created user` |
| `@raise` | Document exceptions | `@raise [NotFoundError] if user missing` |
| `@example` | Show usage example | `@example` + code block |
| `@see` | Reference related docs | `@see #other_method` |
| `@since` | Version introduced | `@since 2.0.0` |
| `@deprecated` | Mark as deprecated | `@deprecated Use {#new_method} instead` |
| `@note` | Important information | `@note This method is not thread-safe` |
| `@todo` | Future work | `@todo Add caching support` |
| `@api` | Visibility level | `@api private` |
| `@yield` | Document blocks | `@yield [item] each item in collection` |
| `@yieldparam` | Block parameter | `@yieldparam item [User] the current user` |
| `@yieldreturn` | Block return | `@yieldreturn [Boolean] whether to continue` |

### Type Syntax
```ruby
# Simple types
@param name [String]
@param age [Integer]
@param active [Boolean]

# Multiple types
@param id [String, Integer] ID as string or integer

# Arrays
@param names [Array<String>] list of names
@param users [Array<User>] list of user objects

# Hashes
@param options [Hash{Symbol => String}] option key-value pairs
@param data [Hash{String => Object}] arbitrary data

# Nilable
@param email [String, nil] optional email

# Duck types
@param io [#read, #write] IO-like object
```

---

## README Template

```markdown
# Project Name

Brief description of what this project does and why it exists.

## Installation

Add to your Gemfile:

```ruby
gem 'project_name'
```

Then run:

```bash
bundle install
```

## Quick Start

```ruby
require 'project_name'

client = ProjectName::Client.new(api_key: ENV['API_KEY'])
result = client.do_something(param: 'value')
```

## Configuration

```ruby
ProjectName.configure do |config|
  config.api_key = ENV['API_KEY']
  config.timeout = 30
  config.logger = Rails.logger
end
```

### Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `api_key` | String | required | Your API key |
| `timeout` | Integer | 30 | Request timeout in seconds |
| `logger` | Logger | nil | Logger instance |

## Usage

### Basic Usage

```ruby
# Example code here
```

### Advanced Usage

```ruby
# More complex example
```

## API Reference

See [API Documentation](docs/api.md) for full reference.

## Development

```bash
# Install dependencies
bundle install

# Run tests
bundle exec rspec

# Run linter
bundle exec rubocop
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Create a Pull Request

## License

MIT License - see [LICENSE](LICENSE) file.
```

---

## Report Format

### Documentation Review: `docs-review-[YYYY-MM-DD].md`

```markdown
# Documentation Review

## Summary
- **Files Reviewed**: [Count]
- **Coverage**: [Percentage]
- **Missing Docs**: [Count]

## Coverage by Type

| Type | Documented | Missing | Coverage |
|------|------------|---------|----------|
| Classes | X | Y | Z% |
| Methods | X | Y | Z% |
| Constants | X | Y | Z% |

## Missing Documentation

### Critical (Public API)
- `ClassName#method_name` - no documentation
- `ModuleName::CONSTANT` - no description

### Should Document
- `InternalClass#helper` - complex logic undocumented

## Recommendations
1. [First priority]
2. [Second priority]
```

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | Public API undocumented, wrong parameter docs |
| **High** | 🟠 | Missing return types, no examples |
| **Medium** | 🟡 | Missing @raise tags, incomplete descriptions |
| **Low** | 🟢 | Style improvements, additional examples |

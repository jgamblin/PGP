# Gemfile Management — Dependencies & Security

> **Purpose**: Organize Gemfile, manage updates, and ensure security  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: Bundler, gem dependencies, security auditing  
> **Last Updated**: 2025-12

---

## Mission

Maintain **organized, secure, and up-to-date** Ruby dependencies. Prevent security vulnerabilities, manage version conflicts, and keep Gemfiles clean.

---

## Guard Clauses

**If no Gemfile provided:**
```
NO_GEMFILE_PROVIDED

Please share your Gemfile to review:
- Paste the Gemfile content
- Or describe your project type (Rails, Sinatra, gem)

I'll analyze dependencies and suggest improvements.
```

**If Gemfile looks good:**
```
GEMFILE_LOOKS_GOOD

✅ **Well-Organized Gemfile**

Your dependencies are in good shape:
- Properly grouped ✓
- Versions specified appropriately ✓
- No known vulnerabilities ✓
- No unnecessary gems ✓

Minor suggestions (optional):
[list any refinements]
```

---

## Quick Context Checklist

```
☐ Gemfile content
☐ Gemfile.lock (for security audit)
☐ Ruby version
☐ Project type (Rails, API, gem, CLI)
☐ Known issues or conflicts
```

---

## Copy-Paste Prompts

### Prompt: Audit Gemfile
```text
Audit this Gemfile for issues:

{{GEMFILE}}

Check for:
1. Security vulnerabilities
2. Outdated gems
3. Unnecessary dependencies
4. Missing version constraints
5. Organization issues

Provide prioritized recommendations.
```

### Prompt: Organize Gemfile
```text
Reorganize this Gemfile following best practices:

{{GEMFILE}}

Apply:
- Logical grouping (core, development, test, production)
- Consistent formatting
- Appropriate version constraints
- Comments for non-obvious gems
```

### Prompt: Check for Vulnerabilities
```text
Check these dependencies for security vulnerabilities:

Gemfile.lock:
{{GEMFILE_LOCK}}

For each vulnerability:
1. Gem name and version
2. CVE or advisory ID
3. Severity level
4. Upgrade path
```

### Prompt: Upgrade Strategy
```text
Create an upgrade plan for this Gemfile:

{{GEMFILE}}

Current issues:
{{ISSUES}}

Provide:
- Safe upgrade order
- Breaking changes to watch for
- Test recommendations
- Rollback plan
```

---

## Gemfile Best Practices

### Organized Structure
```ruby
# frozen_string_literal: true

source 'https://rubygems.org'

ruby '3.3.0'

# ============================================
# Core
# ============================================
gem 'rails', '~> 7.1.0'
gem 'pg', '~> 1.5'
gem 'puma', '~> 6.4'

# ============================================
# API & Serialization
# ============================================
gem 'blueprinter', '~> 0.30'
gem 'oj', '~> 3.16'  # Fast JSON

# ============================================
# Background Jobs
# ============================================
gem 'sidekiq', '~> 7.2'
gem 'redis', '~> 5.0'

# ============================================
# Authentication & Authorization
# ============================================
gem 'devise', '~> 4.9'
gem 'pundit', '~> 2.3'

# ============================================
# Development & Test
# ============================================
group :development, :test do
  gem 'rspec-rails', '~> 6.1'
  gem 'factory_bot_rails', '~> 6.4'
  gem 'faker', '~> 3.2'
  gem 'debug', '~> 1.9'
end

group :development do
  gem 'rubocop', '~> 1.59', require: false
  gem 'rubocop-rails', '~> 2.23', require: false
  gem 'rubocop-rspec', '~> 2.25', require: false
  gem 'brakeman', '~> 6.1', require: false
  gem 'bundler-audit', '~> 0.9', require: false
end

group :test do
  gem 'simplecov', '~> 0.22', require: false
  gem 'webmock', '~> 3.19'
  gem 'vcr', '~> 6.2'
end
```

### Version Constraint Guidelines

| Constraint | Meaning | Use When |
|------------|---------|----------|
| `'~> 3.0'` | >= 3.0, < 4.0 | Major version lock |
| `'~> 3.1.0'` | >= 3.1.0, < 3.2.0 | Minor version lock |
| `'>= 3.0'` | Any version >= 3.0 | Minimum version needed |
| `'= 3.1.2'` | Exactly 3.1.2 | Pinning (avoid if possible) |
| No version | Latest available | Development only |

### Recommended Constraints by Gem Type

| Gem Type | Constraint | Reason |
|----------|------------|--------|
| **Rails** | `~> 7.1.0` | Minor version stability |
| **Database** | `~> 1.5` | Major version lock |
| **Dev tools** | `~> 6.1` | More flexibility OK |
| **Security** | `>= 6.0` | Get latest patches |

---

## Security Auditing

### Essential Commands
```bash
# Check for vulnerable gems
bundle audit check --update

# Check for outdated gems
bundle outdated

# Check for insecure gem sources
bundle doctor

# Update advisory database
bundle audit update
```

### Automated Security Gems
```ruby
group :development do
  # Security scanner for Ruby on Rails
  gem 'brakeman', require: false
  
  # Checks for vulnerable gem versions
  gem 'bundler-audit', require: false
  
  # Alternative: ruby_audit
  gem 'ruby_audit', require: false
end
```

### CI Security Check
```yaml
# .github/workflows/security.yml
name: Security Audit
on: [push, pull_request]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: ruby/setup-ruby@v1
        with:
          bundler-cache: true
      - run: bundle exec bundler-audit check --update
      - run: bundle exec brakeman -q
```

---

## Common Issues & Fixes

### Dependency Conflicts
```ruby
# Problem: Version conflict between gems
# Solution: Check which gem requires which version

bundle viz  # Visualize dependencies
bundle info GEM_NAME  # See gem details

# Or in Gemfile, use compatible versions:
gem 'activesupport', '~> 7.0'  # Lock to compatible version
```

### Slow Bundle Install
```bash
# Use parallel installation
bundle config set jobs 4

# Skip groups you don't need
bundle config set without 'production staging'

# Cache gems locally
bundle config set path 'vendor/bundle'
```

### Reducing Dependencies
```ruby
# Before: Heavy gem for simple task
gem 'activesupport'  # Just for .present?

# After: Use Ruby stdlib or smaller gem
# Or require only what you need:
gem 'activesupport', require: 'active_support/core_ext/object/blank'
```

---

## Essential Gems by Category

### Rails Essentials
| Gem | Purpose |
|-----|---------|
| `pg` / `mysql2` / `sqlite3` | Database adapter |
| `puma` | Application server |
| `redis` | Caching, sessions, jobs |
| `sidekiq` | Background jobs |

### API Development
| Gem | Purpose |
|-----|---------|
| `blueprinter` / `alba` | JSON serialization |
| `oj` | Fast JSON parsing |
| `rack-cors` | CORS handling |
| `api-pagination` | Pagination headers |

### Testing
| Gem | Purpose |
|-----|---------|
| `rspec-rails` | Testing framework |
| `factory_bot_rails` | Test factories |
| `faker` | Fake data generation |
| `webmock` | HTTP request stubbing |
| `vcr` | Record HTTP interactions |
| `simplecov` | Code coverage |

### Code Quality
| Gem | Purpose |
|-----|---------|
| `rubocop` | Linting |
| `rubocop-rails` | Rails-specific rules |
| `rubocop-rspec` | RSpec-specific rules |
| `brakeman` | Security scanner |

---

## Report Format

### Gemfile Audit: `gemfile-audit-[YYYY-MM-DD].md`

```markdown
# Gemfile Audit

## Summary
- **Total Gems**: [Count]
- **Outdated**: [Count]
- **Vulnerabilities**: [Count]
- **Risk Level**: [Critical/High/Medium/Low]

## Vulnerabilities

| Gem | Version | CVE | Severity | Fix |
|-----|---------|-----|----------|-----|

## Outdated Gems

| Gem | Current | Latest | Update Risk |
|-----|---------|--------|-------------|

## Recommendations

### Critical (Do Now)
1. [Security fix]

### High Priority
1. [Important update]

### Consider
1. [Nice to have]

## Upgrade Order
1. [First gem to update]
2. [Second gem to update]
```

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | Known CVE, RCE vulnerability |
| **High** | 🟠 | Security advisory, major version behind |
| **Medium** | 🟡 | Multiple minor versions behind |
| **Low** | 🟢 | Organization issues, minor updates |

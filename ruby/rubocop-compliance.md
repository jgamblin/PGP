# RuboCop Compliance — Ruby Code Style

> **Purpose**: Set up and fix RuboCop linting issues  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: RuboCop configuration, style fixes, custom rules  
> **Last Updated**: 2025-12

---

## Mission

Establish **consistent code style** across Ruby projects using RuboCop. Configure rules, fix violations, and maintain clean, readable code.

---

## Guard Clauses

**If no code/config provided:**
```
NO_CODE_PROVIDED

Please share:
- Ruby code with RuboCop violations
- Or current .rubocop.yml for review
- Or describe your project type for config generation

I'll help fix issues or generate configuration.
```

**If code is compliant:**
```
CODE_COMPLIANT

✅ **RuboCop Compliant**

Code passes all enabled rules:
- Style cops: Passing ✓
- Layout cops: Passing ✓
- Lint cops: Passing ✓
- Metrics cops: Passing ✓

No violations detected.
```

---

## Quick Context Checklist

```
☐ Ruby code to fix (or violations list)
☐ Current .rubocop.yml (if exists)
☐ Project type (Rails, gem, CLI)
☐ Ruby version
☐ Style preferences (Standard Ruby, custom)
```

---

## Copy-Paste Prompts

### Prompt: Fix RuboCop Violations
```text
Fix these RuboCop violations:

{{VIOLATIONS}}

Code:
{{CODE}}

For each violation:
1. Show the fix
2. Explain why RuboCop flags it
3. Note if autocorrectable
```

### Prompt: Generate RuboCop Config
```text
Generate .rubocop.yml for my project:

Type: {{PROJECT_TYPE}}
Ruby: {{RUBY_VERSION}}
Framework: {{FRAMEWORK}}
Team preferences:
- Max line length: {{LINE_LENGTH}}
- Method length: {{METHOD_LENGTH}}
- Block length: {{BLOCK_LENGTH}}

Include appropriate cops and exclusions.
```

### Prompt: Review Config
```text
Review this RuboCop configuration:

{{RUBOCOP_YML}}

Check for:
1. Missing important cops
2. Overly strict rules
3. Overly lenient rules
4. Project-appropriate exclusions
5. Performance cops

Suggest improvements.
```

### Prompt: Migrate RuboCop Version
```text
Help migrate RuboCop config from {{OLD_VERSION}} to {{NEW_VERSION}}:

Current config:
{{RUBOCOP_YML}}

Identify:
1. Deprecated cops
2. Renamed cops
3. New recommended cops
4. Changed defaults
```

---

## RuboCop Configuration

### Basic .rubocop.yml
```yaml
require:
  - rubocop-rails
  - rubocop-rspec

AllCops:
  TargetRubyVersion: 3.3
  NewCops: enable
  SuggestExtensions: false
  Exclude:
    - 'db/schema.rb'
    - 'db/migrate/*'
    - 'bin/*'
    - 'vendor/**/*'
    - 'node_modules/**/*'
    - 'tmp/**/*'

# ============================================
# Style
# ============================================
Style/Documentation:
  Enabled: false

Style/FrozenStringLiteralComment:
  Enabled: true
  EnforcedStyle: always

Style/StringLiterals:
  EnforcedStyle: single_quotes

Style/TrailingCommaInArrayLiteral:
  EnforcedStyleForMultiline: comma

Style/TrailingCommaInHashLiteral:
  EnforcedStyleForMultiline: comma

Style/HashSyntax:
  EnforcedShorthandSyntax: either

# ============================================
# Layout
# ============================================
Layout/LineLength:
  Max: 120
  AllowedPatterns:
    - '^\s*#'  # Comments

Layout/MultilineMethodCallIndentation:
  EnforcedStyle: indented

Layout/FirstArrayElementIndentation:
  EnforcedStyle: consistent

Layout/FirstHashElementIndentation:
  EnforcedStyle: consistent

# ============================================
# Metrics
# ============================================
Metrics/MethodLength:
  Max: 15
  CountAsOne:
    - array
    - hash
    - heredoc

Metrics/ClassLength:
  Max: 150

Metrics/BlockLength:
  Exclude:
    - 'spec/**/*'
    - 'config/routes.rb'
    - '*.gemspec'

Metrics/AbcSize:
  Max: 20

# ============================================
# Rails
# ============================================
Rails/FilePath:
  EnforcedStyle: arguments

Rails/HttpStatus:
  EnforcedStyle: symbolic

# ============================================
# RSpec
# ============================================
RSpec/ExampleLength:
  Max: 20

RSpec/MultipleExpectations:
  Max: 5

RSpec/NestedGroups:
  Max: 4
```

### Minimal Config (Inheriting Standard)
```yaml
inherit_gem:
  standard: config/base.yml

AllCops:
  TargetRubyVersion: 3.3
  NewCops: enable

# Override specific rules
Layout/LineLength:
  Max: 120
```

---

## Common Violations & Fixes

### Style/FrozenStringLiteralComment
```ruby
# ❌ Missing frozen string literal
class User
end

# ✅ Fixed
# frozen_string_literal: true

class User
end
```

### Style/StringLiterals
```ruby
# ❌ Double quotes without interpolation
name = "John"

# ✅ Single quotes
name = 'John'

# ✅ Double quotes with interpolation (correct)
greeting = "Hello, #{name}"
```

### Style/GuardClause
```ruby
# ❌ Nested conditional
def process(user)
  if user.present?
    do_something
  end
end

# ✅ Guard clause
def process(user)
  return unless user.present?

  do_something
end
```

### Style/SymbolProc
```ruby
# ❌ Explicit block
users.map { |u| u.name }

# ✅ Symbol to proc
users.map(&:name)
```

### Layout/LineLength
```ruby
# ❌ Too long
def create_user(first_name:, last_name:, email:, phone:, address:, city:, state:, zip:)
end

# ✅ Multi-line
def create_user(
  first_name:,
  last_name:,
  email:,
  phone:,
  address:,
  city:,
  state:,
  zip:
)
end
```

### Metrics/MethodLength
```ruby
# ❌ Method too long (>15 lines)
def process_order(order)
  # ... 20 lines of code
end

# ✅ Extract methods
def process_order(order)
  validate_order(order)
  calculate_totals(order)
  apply_discounts(order)
  finalize_order(order)
end

private

def validate_order(order)
  # ...
end
```

---

## Useful Commands

```bash
# Run RuboCop
bundle exec rubocop

# Auto-correct safe violations
bundle exec rubocop -a

# Auto-correct all violations (including unsafe)
bundle exec rubocop -A

# Check specific file
bundle exec rubocop app/models/user.rb

# Check specific cop
bundle exec rubocop --only Style/FrozenStringLiteralComment

# Generate TODO file for existing violations
bundle exec rubocop --auto-gen-config

# Show all cops
bundle exec rubocop --show-cops

# Check config for errors
bundle exec rubocop --validate-config
```

---

## Cop Categories

| Category | Purpose | Examples |
|----------|---------|----------|
| **Style** | Code style conventions | StringLiterals, HashSyntax |
| **Layout** | Formatting and whitespace | LineLength, Indentation |
| **Lint** | Potential errors | UnusedVariables, Debugger |
| **Metrics** | Complexity limits | MethodLength, AbcSize |
| **Naming** | Naming conventions | MethodName, VariableName |
| **Security** | Security issues | Eval, YAMLLoad |
| **Rails** | Rails-specific | HttpStatus, FilePath |
| **RSpec** | RSpec-specific | ExampleLength, NestedGroups |

---

## Report Format

### Compliance Report: `rubocop-report-[YYYY-MM-DD].md`

```markdown
# RuboCop Compliance Report

## Summary
- **Files Scanned**: [Count]
- **Violations Found**: [Count]
- **Auto-correctable**: [Count]
- **Compliance Rate**: [Percentage]

## Violations by Category

| Category | Count | Auto-fix |
|----------|-------|----------|
| Style | X | Y |
| Layout | X | Y |
| Metrics | X | Y |
| Lint | X | Y |

## Top Violations

| Cop | Count | Severity |
|-----|-------|----------|

## Recommended Actions
1. Run `rubocop -a` to fix [X] violations
2. Manually fix [Y] violations
3. Consider disabling [cop] if intentional

## Files with Most Violations
1. [file.rb] - X violations
2. [file.rb] - X violations
```

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | Security cops, Lint/Debugger |
| **High** | �� | Style violations affecting readability |
| **Medium** | 🟡 | Metrics violations, minor style issues |
| **Low** | 🟢 | Layout preferences, optional conventions |

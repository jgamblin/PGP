# Ruby Code Refactoring — Idiomatic Improvements

> **Purpose**: Improve Ruby code using idiomatic patterns and best practices  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: Ruby 3.x, Rails 7+, Pure Ruby  
> **Last Updated**: 2025-12

---

## Mission

Transform Ruby code into **clean, idiomatic, maintainable** implementations. Focus on readability, Ruby conventions, and practical improvements.

---

## Guard Clauses

**If no code provided:**
```
NO_CODE_PROVIDED

Please share Ruby code to review:
- Paste the code directly
- Or provide the file path

I'll suggest idiomatic improvements.
```

**If code looks good:**
```
CODE_LOOKS_GOOD

✅ **Clean Ruby Code**

This code follows Ruby best practices:
- Idiomatic patterns ✓
- Clear naming ✓
- Reasonable complexity ✓
- Good structure ✓

Minor suggestions (optional):
[list any refinements]
```

---

## Quick Context Checklist

```
☐ Ruby code to review
☐ Ruby version (default: 3.x)
☐ Framework context (Rails, Sinatra, pure Ruby)
☐ Purpose of the code
☐ Known pain points
```

---

## Copy-Paste Prompts

### Prompt: Full Refactoring Review
```text
Review this Ruby code for refactoring opportunities:

{{CODE}}

Check:
1. Ruby idioms (blocks, enumerable, guard clauses)
2. Method length and complexity
3. Naming clarity
4. Error handling patterns
5. Performance considerations

For each issue, show before/after code.
```

### Prompt: Make It Idiomatic
```text
Rewrite this code using idiomatic Ruby:

{{CODE}}

Apply:
- Guard clauses instead of nested ifs
- Enumerable methods instead of loops
- Symbols where appropriate
- Ruby 3.x features if beneficial
```

### Prompt: Simplify Method
```text
This method is too complex. Simplify it:

{{CODE}}

Goals:
- Single responsibility
- Under 10 lines if possible
- Clear intent
- Easy to test
```

### Prompt: Extract Class/Module
```text
This code has grown too large. Help me extract:

{{CODE}}

Suggest:
1. What to extract (class, module, concern)
2. How to name it
3. The interface/API
4. How to wire it together
```

---

## Ruby Idioms Reference

### Guard Clauses
```ruby
# ❌ Nested conditionals
def process(user)
  if user
    if user.active?
      if user.admin?
        do_admin_stuff
      end
    end
  end
end

# ✅ Guard clauses
def process(user)
  return unless user
  return unless user.active?
  return unless user.admin?
  
  do_admin_stuff
end
```

### Enumerable Methods
```ruby
# ❌ Manual iteration
result = []
items.each do |item|
  if item.valid?
    result << item.name.upcase
  end
end

# ✅ Enumerable chain
result = items
  .select(&:valid?)
  .map { |item| item.name.upcase }

# ✅ Even better with Symbol#to_proc
result = items.select(&:valid?).map(&:name).map(&:upcase)
```

### Safe Navigation
```ruby
# ❌ Nil checks
if user && user.profile && user.profile.avatar
  user.profile.avatar.url
end

# ✅ Safe navigation operator
user&.profile&.avatar&.url
```

### Hash Transformations
```ruby
# ❌ Building hash manually
result = {}
items.each do |item|
  result[item.id] = item.name
end

# ✅ to_h with block (Ruby 2.6+)
result = items.to_h { |item| [item.id, item.name] }

# ✅ Or index_by for Rails
result = items.index_by(&:id)
```

### Pattern Matching (Ruby 3.x)
```ruby
# ❌ Complex conditionals
def handle_response(response)
  if response[:status] == 'success'
    process_data(response[:data])
  elsif response[:status] == 'error'
    handle_error(response[:message])
  end
end

# ✅ Pattern matching
def handle_response(response)
  case response
  in { status: 'success', data: }
    process_data(data)
  in { status: 'error', message: }
    handle_error(message)
  end
end
```

### Keyword Arguments
```ruby
# ❌ Positional arguments (unclear)
def create_user(name, email, true, false, 'admin')

# ✅ Keyword arguments (clear)
def create_user(name:, email:, active: true, verified: false, role: 'user')

create_user(name: 'Alice', email: 'a@b.com', role: 'admin')
```

---

## Code Smells to Fix

| Smell | Sign | Fix |
|-------|------|-----|
| **Long Method** | >15 lines | Extract methods |
| **Long Parameter List** | >3 params | Use keyword args or object |
| **Nested Conditionals** | >2 levels deep | Guard clauses |
| **Feature Envy** | Calls other object's methods constantly | Move method to that class |
| **Data Clump** | Same params passed together | Extract value object |
| **Primitive Obsession** | Strings/ints for concepts | Create domain class |
| **God Class** | Too many responsibilities | Extract classes |

---

## Method Complexity Guidelines

| Metric | Good | Needs Work |
|--------|------|------------|
| **Lines** | ≤10 | >15 |
| **Parameters** | ≤3 | >4 |
| **Conditionals** | ≤2 branches | >3 branches |
| **Nesting** | ≤2 levels | >3 levels |
| **Dependencies** | ≤3 objects | >5 objects |

---

## Report Format

### Refactoring Review: `refactoring-[YYYY-MM-DD].md`

```markdown
# Ruby Refactoring Review

## Summary
- **Files Reviewed**: [Count]
- **Issues Found**: [Count]
- **Severity**: [Critical/High/Medium/Low]

## Issues

### �� Critical
| Location | Issue | Fix |
|----------|-------|-----|

### 🟠 High
| Location | Issue | Fix |
|----------|-------|-----|

### 🟡 Medium
| Location | Issue | Fix |
|----------|-------|-----|

## Before/After Examples
[Include code transformations]

## Recommended Priority
1. [First thing to fix]
2. [Second thing to fix]
```

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | Security issues, broken logic, data corruption |
| **High** | 🟠 | Performance problems, complex methods, poor error handling |
| **Medium** | 🟡 | Non-idiomatic code, naming issues, missing extractions |
| **Low** | 🟢 | Style preferences, minor optimizations |

# Code Refactoring — Quality Improvement

> **Purpose**: Improve code quality, readability, and maintainability  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Languages**: Any  
> **Last Updated**: 2025-12

---

## Mission

Help identify and implement **code improvements** that make code easier to read, test, and maintain. Focus on practical refactoring with clear benefits.

---

## Guard Clauses

**If no code provided:**
```
NO_CODE_PROVIDED

Please provide code to refactor:
- Source file(s)
- Specific functions or classes
- Or describe what you want to improve
```

**If code looks good:**
```
NO_REFACTORING_NEEDED

✅ Code analysis complete — no major issues found.

Checks performed:
- Readability: clear and well-structured ✓
- Complexity: within reasonable limits ✓
- Duplication: minimal repetition ✓
- Error handling: appropriate ✓

Code is well-written. Consider adding tests if missing.
```

---

## Quick Context Checklist

```
☐ Code to refactor
☐ Language and framework
☐ Current pain points
☐ Constraints (performance, compatibility)
```

---

## Copy-Paste Refactoring Prompts

### Prompt: General Code Review
```text
Review this code for refactoring opportunities:

{{CODE}}

Language: {{LANGUAGE}}

Identify:
1. Code smells (duplication, long functions, deep nesting)
2. Naming issues
3. Complexity hotspots
4. Missing error handling
5. Performance issues

Prioritize by impact. Show before/after for top 3 issues.
```

### Prompt: Extract Functions
```text
This function is too long. Extract smaller, focused functions:

{{CODE}}

Goals:
- Each function does one thing
- Functions under 20-30 lines
- Clear, descriptive names
- Proper parameter passing

Show the refactored code with all extracted functions.
```

### Prompt: Reduce Complexity
```text
Reduce complexity in this code:

{{CODE}}

Apply:
- Early returns (guard clauses)
- Dictionary/map dispatch instead of if/elif chains
- Extract conditional logic to functions
- Simplify nested structures

Target: No function over cyclomatic complexity 10.
```

### Prompt: Improve Naming
```text
Improve naming in this code:

{{CODE}}

Check:
- Variable names describe their purpose
- Function names describe what they do
- Class names describe what they represent
- No abbreviations unless universally understood

Show renamed version with original names as comments.
```

### Prompt: Add Error Handling
```text
Add proper error handling to this code:

{{CODE}}

Add:
- Input validation
- Specific exception/error types
- Meaningful error messages
- Graceful degradation
- Logging where appropriate

Show the improved code with error handling.
```

### Prompt: Remove Duplication
```text
Find and eliminate duplication in this code:

{{CODE}}

Identify:
- Repeated code blocks
- Similar functions that can be merged
- Copy-paste patterns
- Opportunities for abstraction

Extract common code to reusable functions/classes.
```

---

## Refactoring Patterns

### 1. **Common Code Smells**

| Smell | Description | Fix |
|-------|-------------|-----|
| **Long Function** | Function > 30 lines | Extract smaller functions |
| **Deep Nesting** | > 3 levels of indentation | Guard clauses, extract |
| **Duplicate Code** | Same logic repeated | Extract to function |
| **Magic Numbers** | Hardcoded values | Named constants |
| **God Class** | Class does too much | Split responsibilities |
| **Long Parameter List** | > 4 parameters | Object/config parameter |

### 2. **Refactoring Techniques**

#### Extract Function
```
BEFORE:
function processOrder(order) {
  // validate
  if (!order.items) return;
  if (!order.customer) return;
  // calculate total
  let total = 0;
  for (let item of order.items) {
    total += item.price * item.quantity;
  }
  // apply discount
  if (order.discount) {
    total = total * (1 - order.discount);
  }
  return total;
}

AFTER:
function processOrder(order) {
  if (!isValidOrder(order)) return;
  return calculateTotal(order);
}

function isValidOrder(order) {
  return order.items && order.customer;
}

function calculateTotal(order) {
  const subtotal = sumItems(order.items);
  return applyDiscount(subtotal, order.discount);
}
```

#### Guard Clauses
```
BEFORE:
function getDiscount(customer) {
  if (customer) {
    if (customer.isPremium) {
      if (customer.yearsActive > 5) {
        return 0.20;
      } else {
        return 0.10;
      }
    }
  }
  return 0;
}

AFTER:
function getDiscount(customer) {
  if (!customer) return 0;
  if (!customer.isPremium) return 0;
  if (customer.yearsActive > 5) return 0.20;
  return 0.10;
}
```

#### Replace Conditionals with Polymorphism/Map
```
BEFORE:
function getSound(animal) {
  if (animal === 'dog') return 'bark';
  if (animal === 'cat') return 'meow';
  if (animal === 'cow') return 'moo';
  return 'unknown';
}

AFTER:
const sounds = {
  dog: 'bark',
  cat: 'meow',
  cow: 'moo',
};

function getSound(animal) {
  return sounds[animal] ?? 'unknown';
}
```

---

## Report Format

### Refactoring Report: `refactoring-[YYYY-MM-DD].md`

```markdown
# Code Refactoring Analysis

## Summary
- **Files Analyzed**: [Count]
- **Issues Found**: [Count by severity]
- **Estimated Effort**: [Hours]

## Findings

### 🔴 Critical
| Issue | Location | Impact | Fix |
|-------|----------|--------|-----|

### 🟠 High
| Issue | Location | Impact | Fix |
|-------|----------|--------|-----|

### 🟡 Medium
| Issue | Location | Impact | Fix |
|-------|----------|--------|-----|

## Recommended Order
1. [First priority with rationale]
2. [Second priority]
3. [Third priority]

## Refactored Code
[Include before/after for major changes]
```

---

## Severity Levels

| Level | Icon | Criteria |
|-------|------|----------|
| **Critical** | 🔴 | Bugs, security issues, data corruption risk |
| **High** | 🟠 | Major complexity, hard to maintain, error-prone |
| **Medium** | 🟡 | Code smells, duplication, poor naming |
| **Low** | 🟢 | Style issues, minor improvements |

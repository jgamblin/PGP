# HTML/CSS Code Refactoring — Frontend Cleanup

> **Purpose**: Improve frontend code quality and maintainability  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Stack**: HTML, CSS, JavaScript  
> **Last Updated**: 2025-12

---

## Mission

Help improve **HTML, CSS, and frontend JavaScript** to make it more readable, maintainable, and performant. Focus on practical improvements that make code easier to work with.

---

## Guard Clauses

**If no code provided:**
```
NO_CODE_PROVIDED

Please provide frontend code to refactor:
- HTML markup
- CSS/SCSS stylesheets
- JavaScript (if applicable)

Include context about what the code does.
```

**If code is already clean:**
```
CODE_LOOKS_GOOD

✅ **No Major Refactoring Needed**

Quick assessment:
- HTML structure: Clean ✓
- CSS organization: Well organized ✓
- Performance: Optimized ✓
- Accessibility: Good ✓

Minor suggestions (if any):
[LIST OPTIONAL IMPROVEMENTS]
```

---

## Quick Context Checklist

```
☐ HTML/CSS/JS code to refactor
☐ What the component/page does
☐ Known issues or pain points
☐ Browser support requirements
```

---

## Copy-Paste Refactoring Prompts

### Prompt: Full Frontend Review
```text
Review and refactor this frontend code:

{{CODE}}

Analyze:
1. HTML: Semantic structure, accessibility
2. CSS: Organization, specificity, duplication
3. JS: Performance, readability
4. Performance: Loading, rendering

Provide refactored code with explanations.
```

### Prompt: Clean Up HTML
```text
Refactor this HTML for better structure:

{{HTML}}

Improve:
1. Use semantic elements
2. Fix accessibility issues
3. Remove unnecessary wrappers
4. Improve class naming
5. Add missing attributes

Show before/after comparison.
```

### Prompt: Organize CSS
```text
Refactor this CSS for maintainability:

{{CSS}}

Focus on:
1. Remove duplication
2. Reduce specificity
3. Organize by component
4. Convert to BEM naming
5. Add CSS custom properties

Group related styles together.
```

### Prompt: Fix Specific Issue
```text
Help fix this frontend issue:

Code: {{CODE}}
Problem: {{DESCRIBE_ISSUE}}

Provide:
1. Root cause
2. Fixed code
3. Explanation
4. Prevention tips
```

### Prompt: Modernize Legacy Code
```text
Modernize this legacy frontend code:

{{CODE}}

Update to use:
- Modern HTML5 elements
- CSS Grid/Flexbox (instead of floats)
- CSS custom properties
- Modern JS (if applicable)

Maintain backwards compatibility with: {{BROWSERS}}
```

### Prompt: Performance Optimization
```text
Optimize this frontend code for performance:

{{CODE}}

Check:
1. Render-blocking resources
2. Image optimization opportunities
3. CSS efficiency
4. JavaScript loading
5. DOM complexity

Suggest specific improvements with expected impact.
```

---

## HTML Code Smells

| Smell | Problem | Fix |
|-------|---------|-----|
| **Div soup** | Too many meaningless divs | Use semantic elements |
| **Inline styles** | Hard to maintain | Move to CSS classes |
| **Missing alt** | Accessibility fail | Add descriptive alt |
| **Generic classes** | `.box`, `.container` everywhere | Use descriptive BEM names |
| **Deprecated tags** | `<center>`, `<font>` | Use CSS instead |
| **ID for styling** | High specificity | Use classes |

### HTML Refactoring Examples

```html
<!-- ❌ Before: Div soup -->
<div class="header">
  <div class="logo">Logo</div>
  <div class="nav">
    <div class="nav-item"><a href="/">Home</a></div>
    <div class="nav-item"><a href="/about">About</a></div>
  </div>
</div>

<!-- ✅ After: Semantic HTML -->
<header class="site-header">
  <a href="/" class="site-header__logo">Logo</a>
  <nav class="site-header__nav">
    <ul class="nav__list">
      <li><a href="/" class="nav__link">Home</a></li>
      <li><a href="/about" class="nav__link">About</a></li>
    </ul>
  </nav>
</header>
```

---

## CSS Code Smells

| Smell | Problem | Fix |
|-------|---------|-----|
| **!important** | Specificity nightmare | Fix cascade properly |
| **Deep nesting** | Hard to override | Flatten selectors |
| **Magic numbers** | `margin: 37px` | Use variables/scale |
| **Repeated values** | Same color 20 times | CSS custom properties |
| **Overly specific** | `div.container ul li a` | Use classes |
| **Unused CSS** | Bloated stylesheets | Audit and remove |

### CSS Refactoring Examples

```css
/* ❌ Before: Overly specific, magic numbers */
div.container > ul.nav > li > a.active {
  color: #3498db;
  padding: 13px 27px;
  margin-left: 8px !important;
}

/* ✅ After: Clean, maintainable */
:root {
  --color-primary: #3498db;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
}

.nav__link--active {
  color: var(--color-primary);
  padding: var(--spacing-md) var(--spacing-lg);
  margin-left: var(--spacing-sm);
}
```

---

## Refactoring Checklist

### HTML
- [ ] Uses semantic elements (`<header>`, `<main>`, `<nav>`, etc.)
- [ ] Proper heading hierarchy (h1 → h2 → h3)
- [ ] Images have alt attributes
- [ ] Forms have associated labels
- [ ] No inline styles
- [ ] No unnecessary wrapper divs

### CSS
- [ ] No `!important` (or justified use only)
- [ ] BEM or consistent naming convention
- [ ] CSS custom properties for repeated values
- [ ] Mobile-first media queries
- [ ] No ID selectors for styling
- [ ] Reasonable specificity (max 2-3 levels)

### Performance
- [ ] Critical CSS inlined
- [ ] Non-critical CSS deferred
- [ ] Images optimized and lazy-loaded
- [ ] Minimal DOM depth
- [ ] No render-blocking resources

---

## Modern CSS Patterns

### Replace Floats with Flexbox
```css
/* ❌ Old: Float layout */
.container::after { content: ""; clear: both; display: table; }
.sidebar { float: left; width: 25%; }
.main { float: left; width: 75%; }

/* ✅ Modern: Flexbox */
.container {
  display: flex;
  gap: 1rem;
}
.sidebar { flex: 0 0 25%; }
.main { flex: 1; }
```

### Replace Fixed Widths with Grid
```css
/* ❌ Old: Fixed card grid */
.card { width: 300px; float: left; margin: 10px; }

/* ✅ Modern: CSS Grid */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1rem;
}
```

### Replace Repeated Colors with Custom Properties
```css
/* ❌ Old: Repeated colors */
.btn-primary { background: #0066cc; }
.link { color: #0066cc; }
.heading { border-bottom: 2px solid #0066cc; }

/* ✅ Modern: CSS custom properties */
:root {
  --color-primary: #0066cc;
}
.btn-primary { background: var(--color-primary); }
.link { color: var(--color-primary); }
.heading { border-bottom: 2px solid var(--color-primary); }
```

---

## Report Format

### Refactoring Report: `refactor-[YYYY-MM-DD].md`

```markdown
# Frontend Refactoring Report

## Summary
- **Files Reviewed**: [Count]
- **Issues Found**: [Count by severity]
- **Lines Changed**: [Before → After]

## Findings

### 🔴 Critical
| Issue | File | Line | Fix |
|-------|------|------|-----|

### �� High
| Issue | File | Line | Fix |
|-------|------|------|-----|

### 🟡 Medium
| Issue | File | Line | Fix |
|-------|------|------|-----|

### 🟢 Low
| Issue | File | Line | Fix |
|-------|------|------|-----|

## Changes Made
[List of refactoring changes with before/after]

## Performance Impact
- CSS size: [Before] → [After]
- DOM nodes: [Before] → [After]
- Lighthouse score: [Before] → [After]
```

---

## Severity Guide

| Level | Icon | Impact | Examples |
|-------|------|--------|----------|
| **Critical** | 🔴 | Breaks functionality | Invalid HTML, broken layout |
| **High** | 🟠 | Major maintainability | Deep nesting, !important abuse |
| **Medium** | 🟡 | Code quality | Inconsistent naming, duplication |
| **Low** | 🟢 | Enhancement | Could be more semantic |

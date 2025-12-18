# Component Design System — Reusable UI Patterns

> **Purpose**: Create and review reusable UI components  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Stack**: HTML, CSS, JavaScript, Design Systems  
> **Last Updated**: 2025-12

---

## Mission

Help create and review **reusable HTML/CSS components** that are consistent, accessible, and maintainable. Build a cohesive design system from individual components.

---

## Guard Clauses

**If no component spec provided:**
```
COMPONENT_SPEC_REQUIRED

Please describe the component:
- What it does
- Expected variants/states
- Content requirements
- Interaction behavior

Or provide existing code to review.
```

**If component is already well-designed:**
```
COMPONENT_APPROVED

✅ **Well-Designed Component**

Quality checks passed:
- Reusable structure ✓
- Consistent with design system ✓
- Accessible ✓
- Responsive ✓
- Well-documented ✓

Ready for use.
```

---

## Quick Context Checklist

```
☐ Component purpose/requirements
☐ Design mockup or reference
☐ Existing design system (if any)
☐ Framework context (vanilla, React, Vue)
☐ Accessibility requirements
```

---

## Copy-Paste Component Prompts

### Prompt: Create New Component
```text
Create a [COMPONENT_NAME] component:

Requirements:
- {{REQUIREMENTS}}

Variants needed:
- {{VARIANT_1}}
- {{VARIANT_2}}

Provide:
1. HTML structure
2. CSS (BEM naming)
3. Accessibility features
4. Usage examples
5. Documentation
```

### Prompt: Review Component
```text
Review this component:

{{CODE}}

Evaluate:
1. Reusability (can it be used in different contexts?)
2. Consistency (follows design system?)
3. Accessibility (keyboard, screen reader?)
4. Responsiveness (works on all sizes?)
5. Maintainability (easy to modify?)

Suggest improvements.
```

### Prompt: Component Variants
```text
Create variants for this component:

Base component:
{{CODE}}

Variants needed:
- Size: small, medium, large
- Color: primary, secondary, danger
- State: default, hover, active, disabled

Use CSS modifiers (BEM --modifier pattern).
```

### Prompt: Design System Audit
```text
Audit these components for design system consistency:

{{COMPONENT_LIST}}

Check:
1. Naming conventions consistent?
2. Spacing scale followed?
3. Color palette adhered to?
4. Typography consistent?
5. Common patterns reused?

Identify inconsistencies and suggest fixes.
```

### Prompt: Document Component
```text
Create documentation for this component:

{{CODE}}

Include:
1. Component overview
2. When to use / when not to use
3. Props/variants table
4. Code examples
5. Accessibility notes
6. Related components
```

---

## Component Structure Template

### HTML Structure
```html
<!-- Component: [Name] -->
<div class="component component--variant">
  <div class="component__header">
    <!-- Header content -->
  </div>
  <div class="component__body">
    <!-- Main content -->
  </div>
  <div class="component__footer">
    <!-- Footer content -->
  </div>
</div>
```

### CSS Structure
```css
/* ==========================================================================
   Component: [Name]
   ========================================================================== */

/**
 * Base component styles
 */
.component {
  /* Layout */
  display: flex;
  flex-direction: column;
  
  /* Spacing */
  padding: var(--spacing-md);
  gap: var(--spacing-sm);
  
  /* Appearance */
  background: var(--color-surface);
  border-radius: var(--radius-md);
}

/* Elements
   ========================================================================== */

.component__header {
  /* Header styles */
}

.component__body {
  /* Body styles */
}

.component__footer {
  /* Footer styles */
}

/* Modifiers
   ========================================================================== */

.component--small {
  padding: var(--spacing-sm);
}

.component--large {
  padding: var(--spacing-lg);
}

/* States
   ========================================================================== */

.component:hover {
  /* Hover state */
}

.component:focus-within {
  /* Focus state */
}

.component--disabled {
  opacity: 0.5;
  pointer-events: none;
}
```

---

## Common Components Library

### Button
```html
<button class="btn btn--primary btn--medium">
  <span class="btn__icon">→</span>
  <span class="btn__label">Button Text</span>
</button>
```

| Modifier | Purpose |
|----------|---------|
| `--primary` | Main action |
| `--secondary` | Secondary action |
| `--ghost` | Subtle action |
| `--danger` | Destructive action |
| `--small/medium/large` | Size variants |
| `--disabled` | Inactive state |
| `--loading` | Loading state |

### Card
```html
<article class="card card--interactive">
  <img class="card__image" src="..." alt="...">
  <div class="card__content">
    <h3 class="card__title">Title</h3>
    <p class="card__description">Description</p>
  </div>
  <div class="card__actions">
    <button class="btn btn--primary">Action</button>
  </div>
</article>
```

| Modifier | Purpose |
|----------|---------|
| `--interactive` | Clickable card |
| `--horizontal` | Side-by-side layout |
| `--featured` | Highlighted card |
| `--compact` | Less padding |

### Form Field
```html
<div class="form-field form-field--error">
  <label class="form-field__label" for="email">
    Email
    <span class="form-field__required">*</span>
  </label>
  <input class="form-field__input" type="email" id="email">
  <span class="form-field__error">Please enter a valid email</span>
  <span class="form-field__hint">We'll never share your email</span>
</div>
```

| Modifier | Purpose |
|----------|---------|
| `--error` | Validation error |
| `--success` | Validation success |
| `--disabled` | Disabled field |
| `--required` | Required indicator |

### Modal
```html
<div class="modal" role="dialog" aria-modal="true" aria-labelledby="modal-title">
  <div class="modal__overlay"></div>
  <div class="modal__container">
    <header class="modal__header">
      <h2 class="modal__title" id="modal-title">Modal Title</h2>
      <button class="modal__close" aria-label="Close modal">×</button>
    </header>
    <div class="modal__body">
      <!-- Content -->
    </div>
    <footer class="modal__footer">
      <button class="btn btn--secondary">Cancel</button>
      <button class="btn btn--primary">Confirm</button>
    </footer>
  </div>
</div>
```

---

## Design Tokens

### Spacing Scale
```css
:root {
  --spacing-xs: 0.25rem;   /* 4px */
  --spacing-sm: 0.5rem;    /* 8px */
  --spacing-md: 1rem;      /* 16px */
  --spacing-lg: 1.5rem;    /* 24px */
  --spacing-xl: 2rem;      /* 32px */
  --spacing-2xl: 3rem;     /* 48px */
}
```

### Color Palette
```css
:root {
  /* Brand */
  --color-primary: #0066cc;
  --color-secondary: #6c757d;
  
  /* Semantic */
  --color-success: #28a745;
  --color-warning: #ffc107;
  --color-danger: #dc3545;
  --color-info: #17a2b8;
  
  /* Neutral */
  --color-background: #ffffff;
  --color-surface: #f8f9fa;
  --color-text: #212529;
  --color-text-muted: #6c757d;
  --color-border: #dee2e6;
}
```

### Typography Scale
```css
:root {
  --font-size-xs: 0.75rem;    /* 12px */
  --font-size-sm: 0.875rem;   /* 14px */
  --font-size-md: 1rem;       /* 16px */
  --font-size-lg: 1.25rem;    /* 20px */
  --font-size-xl: 1.5rem;     /* 24px */
  --font-size-2xl: 2rem;      /* 32px */
  
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-bold: 700;
  
  --line-height-tight: 1.25;
  --line-height-normal: 1.5;
  --line-height-loose: 1.75;
}
```

---

## Component Checklist

### Structure
- [ ] Single responsibility (does one thing well)
- [ ] Self-contained (no external dependencies)
- [ ] Composable (can be combined with others)
- [ ] BEM naming convention

### Accessibility
- [ ] Keyboard navigable
- [ ] Focus indicators visible
- [ ] ARIA attributes where needed
- [ ] Color contrast compliant
- [ ] Screen reader friendly

### Responsiveness
- [ ] Works on mobile (320px+)
- [ ] Works on tablet (768px+)
- [ ] Works on desktop (1024px+)
- [ ] Content adapts gracefully

### Documentation
- [ ] Purpose described
- [ ] Variants documented
- [ ] Usage examples provided
- [ ] Accessibility notes included

---

## Report Format

### Component Review: `component-review-[YYYY-MM-DD].md`

```markdown
# Component Review

## Component: [Name]

## Quality Assessment
| Criteria | Score | Notes |
|----------|-------|-------|
| Reusability | ⭐⭐⭐⭐☆ | |
| Consistency | ⭐⭐⭐⭐⭐ | |
| Accessibility | ⭐⭐⭐☆☆ | |
| Responsiveness | ⭐⭐⭐⭐☆ | |
| Documentation | ⭐⭐☆☆☆ | |

## Findings

### Issues
| Issue | Severity | Fix |
|-------|----------|-----|

### Suggestions
| Suggestion | Impact |
|------------|--------|

## Recommended Changes
1. [Change 1]
2. [Change 2]
```

---

## Severity Guide

| Level | Icon | Impact | Examples |
|-------|------|--------|----------|
| **Critical** | 🔴 | Unusable | Component broken, inaccessible |
| **High** | 🟠 | Major issue | Not reusable, inconsistent |
| **Medium** | 🟡 | Should fix | Missing variants, poor docs |
| **Low** | 🟢 | Enhancement | Could be more polished |

# BEM Naming Convention — CSS Architecture

> **Purpose**: Organize CSS using Block Element Modifier methodology  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: CSS, SCSS, Component Styling  
> **Last Updated**: 2025-12

---

## Mission

Help organize **CSS code using BEM methodology** to make stylesheets more predictable, maintainable, and scalable. Eliminate specificity wars and naming conflicts.

---

## Guard Clauses

**If no CSS provided:**
```
NO_CSS_PROVIDED

Please provide CSS to refactor:
- Paste your current CSS/SCSS
- Or describe the components you're styling
- Include HTML structure if helpful

I'll help convert to BEM naming.
```

**If already using BEM:**
```
BEM_COMPLIANT

✅ **Already Using BEM**

Your CSS follows BEM conventions:
- Blocks are clearly defined ✓
- Elements use __ separator ✓
- Modifiers use -- separator ✓
- No deep nesting ✓

Minor suggestions (if any):
[LIST ANY REFINEMENTS]
```

---

## Quick Context Checklist

```
☐ Current CSS/SCSS to refactor
☐ Component HTML structure
☐ Framework in use (vanilla, React, Vue)
☐ Existing naming conventions
```

---

## Copy-Paste BEM Prompts

### Prompt: Convert to BEM
```text
Convert this CSS to BEM methodology:

{{CSS}}

Rules:
- Block: standalone component (.card, .nav)
- Element: part of block (.card__title)
- Modifier: variation (.card--featured)

Show before/after with explanation.
```

### Prompt: Name This Component
```text
Suggest BEM class names for this component:

{{HTML}}

Provide:
1. Block name
2. Element names
3. Common modifier names
4. Complete CSS structure
```

### Prompt: Review BEM Usage
```text
Review this CSS for BEM compliance:

{{CSS}}

Check:
1. Block naming (clear, descriptive)
2. Element naming (double underscore)
3. Modifier naming (double hyphen)
4. Nesting depth (max 1 level)
5. No element of element (.block__el__el)

Suggest improvements.
```

### Prompt: Component Library
```text
Create BEM structure for these components:

Components needed:
- {{COMPONENT_1}}
- {{COMPONENT_2}}
- {{COMPONENT_3}}

For each provide:
1. Block and element names
2. Common modifiers
3. CSS skeleton
4. HTML example
```

### Prompt: Migrate Legacy CSS
```text
Migrate this legacy CSS to BEM:

{{OLD_CSS}}

Current issues:
- [DESCRIBE PROBLEMS]

Create a migration plan:
1. Identify blocks
2. Map old classes to new
3. Provide new CSS
4. Note breaking changes
```

---

## BEM Fundamentals

### The Pattern
```
.block {}
.block__element {}
.block--modifier {}
.block__element--modifier {}
```

### Naming Rules

| Type | Pattern | Example |
|------|---------|---------|
| **Block** | `.noun` | `.card`, `.nav`, `.hero` |
| **Element** | `.block__noun` | `.card__title`, `.nav__link` |
| **Modifier** | `.block--adjective` | `.card--featured`, `.btn--large` |
| **Element + Modifier** | `.block__element--modifier` | `.card__title--highlighted` |

### What NOT to Do
```css
/* ❌ Never nest elements */
.card__header__title {}

/* ❌ Never chain blocks */
.card.featured {}

/* ❌ Never use IDs for styling */
#card-title {}

/* ❌ Never nest beyond 1 level in SCSS */
.card {
  .card__title {
    .card__title-icon {}  /* Too deep! */
  }
}
```

---

## BEM Examples

### Card Component
```html
<article class="card card--featured">
  <img class="card__image" src="..." alt="...">
  <div class="card__content">
    <h3 class="card__title">Title</h3>
    <p class="card__description">Description</p>
    <a class="card__link" href="#">Read more</a>
  </div>
</article>
```

```css
/* Block */
.card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

/* Elements */
.card__image {
  width: 100%;
  border-radius: 8px 8px 0 0;
}

.card__content {
  padding: 1rem;
}

.card__title {
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
}

.card__description {
  color: #666;
}

.card__link {
  color: #0066cc;
}

/* Modifier */
.card--featured {
  border: 2px solid gold;
}
```

### Navigation Component
```html
<nav class="nav nav--dark">
  <a class="nav__logo" href="/">Logo</a>
  <ul class="nav__list">
    <li class="nav__item">
      <a class="nav__link nav__link--active" href="/">Home</a>
    </li>
    <li class="nav__item">
      <a class="nav__link" href="/about">About</a>
    </li>
  </ul>
  <button class="nav__toggle">Menu</button>
</nav>
```

```css
.nav {
  display: flex;
  align-items: center;
  padding: 1rem;
}

.nav--dark {
  background: #1a1a1a;
  color: white;
}

.nav__logo {
  font-weight: bold;
}

.nav__list {
  display: flex;
  gap: 1rem;
  list-style: none;
}

.nav__link {
  color: inherit;
  text-decoration: none;
}

.nav__link--active {
  border-bottom: 2px solid currentColor;
}

.nav__toggle {
  display: none;
}

@media (max-width: 768px) {
  .nav__toggle {
    display: block;
  }
}
```

### Button Component
```html
<button class="btn btn--primary btn--large">
  <span class="btn__icon">→</span>
  <span class="btn__text">Submit</span>
</button>
```

```css
.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

/* Size modifiers */
.btn--small { padding: 0.25rem 0.5rem; font-size: 0.875rem; }
.btn--large { padding: 0.75rem 1.5rem; font-size: 1.125rem; }

/* Color modifiers */
.btn--primary { background: #0066cc; color: white; }
.btn--secondary { background: #666; color: white; }
.btn--outline { background: transparent; border: 1px solid currentColor; }

/* State modifiers */
.btn--disabled { opacity: 0.5; cursor: not-allowed; }
.btn--loading { pointer-events: none; }

/* Elements */
.btn__icon { font-size: 1.2em; }
.btn__text { /* default styling */ }
```

---

## SCSS with BEM

```scss
// Use & for clean BEM in SCSS
.card {
  background: white;
  border-radius: 8px;

  // Elements (one level only)
  &__image {
    width: 100%;
  }

  &__title {
    font-size: 1.25rem;
  }

  &__description {
    color: #666;
  }

  // Modifiers
  &--featured {
    border: 2px solid gold;
  }

  &--compact {
    padding: 0.5rem;
  }
}
```

---

## Common Component Names

| Component | Block Name | Common Elements |
|-----------|------------|-----------------|
| **Card** | `.card` | `__image`, `__title`, `__body`, `__footer`, `__link` |
| **Navigation** | `.nav` | `__logo`, `__list`, `__item`, `__link`, `__toggle` |
| **Button** | `.btn` | `__icon`, `__text`, `__badge` |
| **Form** | `.form` | `__group`, `__label`, `__input`, `__error`, `__help` |
| **Modal** | `.modal` | `__overlay`, `__content`, `__header`, `__body`, `__footer`, `__close` |
| **Hero** | `.hero` | `__background`, `__content`, `__title`, `__subtitle`, `__cta` |
| **Header** | `.header` | `__logo`, `__nav`, `__search`, `__actions` |
| **Footer** | `.footer` | `__nav`, `__links`, `__social`, `__copyright` |

---

## Report Format

### BEM Refactor: `bem-refactor-[YYYY-MM-DD].md`

```markdown
# BEM Refactoring Report

## Components Refactored
| Component | Old Classes | New BEM Classes |
|-----------|-------------|-----------------|

## Changes Made
### [Component Name]
**Before:**
\`\`\`css
[old CSS]
\`\`\`

**After:**
\`\`\`css
[new BEM CSS]
\`\`\`

## Migration Notes
- [Breaking changes]
- [HTML updates needed]

## Benefits
- Eliminated specificity issues
- Reduced CSS size by X%
- Improved maintainability
```

---

## Severity Guide

| Level | Icon | Issue | Example |
|-------|------|-------|---------|
| **Critical** | 🔴 | Breaks component | Conflicting class names |
| **High** | 🟠 | Hard to maintain | Deep nesting, unclear names |
| **Medium** | 🟡 | Inconsistent | Mixed naming conventions |
| **Low** | 🟢 | Minor improvement | Could be more semantic |

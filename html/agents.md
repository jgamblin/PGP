# HTML/CSS Prompts — Index

> **Purpose**: Quick reference for all HTML/CSS prompts  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Stack**: HTML, CSS, JavaScript, Accessibility  
> **Last Updated**: 2025-12

---

## Available Prompts

| Prompt | Purpose | Use When |
|--------|---------|----------|
| [accessibility-check.md](accessibility-check.md) | WCAG compliance & a11y | Making sites accessible |
| [semantic-markup-refinement.md](semantic-markup-refinement.md) | Proper HTML elements | Improving structure |
| [performance-core-web-vitals-audit.md](performance-core-web-vitals-audit.md) | Core Web Vitals | Site is slow |
| [bem-naming-convention.md](bem-naming-convention.md) | CSS organization | Messy stylesheets |
| [navigation-consistency.md](navigation-consistency.md) | Nav patterns | Building menus |
| [component-design-system-review.md](component-design-system-review.md) | Reusable components | Creating UI library |
| [code-refactoring.md](code-refactoring.md) | Clean up code | Technical debt |
| [pr-review-feedback.md](pr-review-feedback.md) | Review changes | Before merging |
| [documentation-generation.md](documentation-generation.md) | Write docs | New projects |
| [project-repo.md](project-repo.md) | Project setup | Starting fresh |
| [copilot-instructions.md](copilot-instructions.md) | AI configuration | Copilot setup |

---

## Quick Start Prompts

### Fix Accessibility Issues
```text
Review this HTML for accessibility:

{{CODE}}

Check WCAG 2.1 AA compliance:
1. Missing alt text
2. Form labels
3. Color contrast
4. Keyboard navigation
5. ARIA usage

Prioritize fixes by impact.
```

### Improve Performance
```text
Audit this page for Core Web Vitals:

{{HTML}}

Focus on:
- LCP (Largest Contentful Paint) < 2.5s
- FID (First Input Delay) < 100ms
- CLS (Cumulative Layout Shift) < 0.1

Suggest specific fixes.
```

### Clean Up CSS
```text
Refactor this CSS using BEM methodology:

{{CSS}}

Convert to:
- Block__Element--Modifier naming
- Remove deeply nested selectors
- Consolidate duplicate styles
- Organize by component
```

### Review HTML Structure
```text
Review this HTML for semantic markup:

{{HTML}}

Check:
1. Proper use of semantic elements
2. Heading hierarchy (h1-h6)
3. Landmark regions
4. List structure
5. Form organization

Show before/after examples.
```

---

## Severity Guide

| Level | Icon | Meaning | Examples |
|-------|------|---------|----------|
| **Critical** | 🔴 | Breaks functionality | Missing form labels, broken navigation |
| **High** | 🟠 | Major UX/a11y issue | No alt text, poor contrast |
| **Medium** | 🟡 | Should fix | Non-semantic HTML, unoptimized images |
| **Low** | 🟢 | Nice to have | CSS organization, minor improvements |

---

## Common Workflows

### New Project Setup
1. Start with [project-repo.md](project-repo.md) for structure
2. Use [copilot-instructions.md](copilot-instructions.md) for AI config
3. Apply [bem-naming-convention.md](bem-naming-convention.md) for CSS

### Code Review
1. Run [accessibility-check.md](accessibility-check.md) first
2. Check [performance-core-web-vitals-audit.md](performance-core-web-vitals-audit.md)
3. Use [pr-review-feedback.md](pr-review-feedback.md) for final review

### Refactoring
1. Start with [semantic-markup-refinement.md](semantic-markup-refinement.md)
2. Apply [code-refactoring.md](code-refactoring.md)
3. Organize with [component-design-system-review.md](component-design-system-review.md)

---

## HTML/CSS Best Practices

### Accessibility First
- All images have descriptive `alt` text
- Forms have associated `<label>` elements
- Color contrast meets WCAG AA (4.5:1 for text)
- All functionality works via keyboard

### Semantic HTML
- Use `<header>`, `<nav>`, `<main>`, `<footer>`
- Proper heading hierarchy (one `<h1>` per page)
- Lists for related items (`<ul>`, `<ol>`)
- `<button>` for actions, `<a>` for navigation

### Performance
- Optimize and lazy-load images
- Minimize CSS/JS bundles
- Use modern image formats (WebP, AVIF)
- Set explicit `width`/`height` on images

### CSS Organization
- BEM naming: `.block__element--modifier`
- Mobile-first responsive design
- CSS custom properties for theming
- Avoid deep nesting (max 3 levels)

# Modern CSS — Container Queries, :has(), Cascade Layers & Subgrid

> **Purpose**: Production-ready modern CSS patterns and best practices  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: CSS 2024-2026 features, progressive enhancement  
> **Last Updated**: 2026-01

---

## Mission

Help write **modern, maintainable CSS** using the latest features with proper fallbacks. Focus on container queries, `:has()`, cascade layers, subgrid, and other production-ready CSS features.

---

## Guard Clauses

**If no CSS context provided:**
```
NO_CSS_CONTEXT

Please provide context:
- Browser support requirements
- Framework/preprocessor in use
- Component or layout to implement
- Or describe your CSS challenge
```

**If CSS is well-structured:**
```
CSS_APPROVED

✅ CSS review complete — production ready.

Checks performed:
- Modern features: ✓ (with appropriate fallbacks)
- Cascade layers: ✓ (organized specificity)
- Container queries: ✓ (component-based responsive)
- Performance: ✓ (no layout thrashing)

CSS follows modern best practices.
```

---

## Quick Context Checklist

```
☐ Browser support targets
☐ Build tooling (PostCSS, Lightning CSS)
☐ Framework (vanilla, React, Vue, etc.)
☐ Design system constraints
☐ Accessibility requirements
☐ Performance requirements
☐ Dark mode support needed
☐ RTL support needed
```

---

## Copy-Paste Prompts

### Prompt: Review Modern CSS
```text
Review this CSS for modern best practices:

{{CSS_CODE}}

Browser targets: {{BROWSER_TARGETS}}

Check for:
1. **Modern Features**
   - Container queries usage
   - :has() selector opportunities
   - Cascade layers organization
   - Subgrid implementation

2. **Fallbacks**
   - @supports queries
   - Progressive enhancement
   - Graceful degradation

3. **Performance**
   - Selector efficiency
   - Layout thrashing prevention
   - Animation performance

4. **Maintainability**
   - Custom properties usage
   - Logical properties
   - Nesting structure
```

### Prompt: Implement Container Queries
```text
Convert this media query layout to container queries:

{{CSS_CODE}}

Component context: {{COMPONENT_DESCRIPTION}}

Requirements:
- Container query implementation
- Fallback for older browsers
- Responsive breakpoints
- Nested container support if needed
```

### Prompt: Add Cascade Layers
```text
Organize this CSS with cascade layers:

{{CSS_CODE}}

Layer requirements:
- Reset/normalize layer
- Base/theme layer
- Components layer
- Utilities layer
- Overrides layer

Include @layer order declaration and proper organization.
```

### Prompt: Implement Subgrid Layout
```text
Create a subgrid layout for:

{{LAYOUT_DESCRIPTION}}

Requirements:
- Parent grid definition
- Subgrid children
- Fallback for non-supporting browsers
- Alignment consistency
```

### Prompt: Modernize Legacy CSS
```text
Modernize this CSS to 2026 standards:

{{CSS_CODE}}

Target browsers: {{BROWSER_TARGETS}}

Modernize:
1. Replace @media with @container where appropriate
2. Add cascade layers
3. Use :has() for parent selection
4. Convert to logical properties
5. Use CSS nesting
6. Add custom properties for theming
7. Include necessary fallbacks
```

---

## Container Queries

### Basic Setup

```css
/* Define containment on parent */
.card-container {
  container-type: inline-size;
  container-name: card;
}

/* Query the container */
@container card (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 200px 1fr;
    gap: 1rem;
  }
}

@container card (min-width: 600px) {
  .card {
    grid-template-columns: 250px 1fr 150px;
  }
}
```

### Container Query Units

```css
/* Container query units */
.card-title {
  /* cqw = 1% of container width */
  font-size: clamp(1rem, 4cqw, 2rem);
  
  /* cqh = 1% of container height */
  /* cqi = 1% of container inline size */
  /* cqb = 1% of container block size */
  /* cqmin = smaller of cqi/cqb */
  /* cqmax = larger of cqi/cqb */
}
```

### Style Queries (Container Style Queries)

```css
/* Define custom property on container */
.card-container {
  container-type: inline-size;
  --theme: light;
}

.card-container.dark {
  --theme: dark;
}

/* Query the style */
@container style(--theme: dark) {
  .card {
    background: #1a1a1a;
    color: #ffffff;
  }
}
```

### Container Queries with Fallback

```css
/* Fallback for browsers without container query support */
.card {
  display: block;
}

/* Modern browsers */
@supports (container-type: inline-size) {
  .card-container {
    container-type: inline-size;
  }
  
  @container (min-width: 400px) {
    .card {
      display: grid;
      grid-template-columns: 200px 1fr;
    }
  }
}
```

---

## The :has() Selector

### Parent Selection

```css
/* Style parent based on child */
.card:has(img) {
  display: grid;
  grid-template-rows: auto 1fr;
}

.card:has(.badge) {
  padding-top: 2rem;
}

/* Form validation styling */
.form-group:has(input:invalid) {
  border-color: red;
}

.form-group:has(input:valid) {
  border-color: green;
}

/* Has required field indicator */
label:has(+ input:required)::after {
  content: " *";
  color: red;
}
```

### Sibling Selection

```css
/* Style based on sibling state */
.menu-toggle:checked ~ .menu {
  display: block;
}

/* Style elements that have a following sibling */
h2:has(+ p) {
  margin-bottom: 0.5rem;
}

/* Style based on sibling with class */
.grid:has(.featured) .grid-item:not(.featured) {
  opacity: 0.7;
}
```

### Conditional Layouts

```css
/* Change layout based on content */
.gallery:has(> :nth-child(4)) {
  grid-template-columns: repeat(2, 1fr);
}

.gallery:has(> :nth-child(7)) {
  grid-template-columns: repeat(3, 1fr);
}

/* Empty state styling */
.list:not(:has(li)) {
  display: none;
}

.list:not(:has(li)) + .empty-state {
  display: block;
}
```

### :has() with Fallback

```css
/* Fallback approach */
.card {
  padding: 1rem;
}

/* Enhancement with :has() */
@supports selector(:has(*)) {
  .card:has(img) {
    padding: 0;
  }
  
  .card:has(img) .card-content {
    padding: 1rem;
  }
}
```

---

## Cascade Layers

### Layer Organization

```css
/* Declare layer order first */
@layer reset, base, components, utilities, overrides;

/* Reset layer */
@layer reset {
  *,
  *::before,
  *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
}

/* Base/theme layer */
@layer base {
  :root {
    --color-primary: #3b82f6;
    --color-text: #1f2937;
    --spacing-unit: 0.25rem;
  }
  
  body {
    font-family: system-ui, sans-serif;
    color: var(--color-text);
  }
}

/* Components layer */
@layer components {
  .btn {
    padding: 0.5rem 1rem;
    border-radius: 0.375rem;
    font-weight: 500;
  }
  
  .card {
    background: white;
    border-radius: 0.5rem;
    box-shadow: 0 1px 3px rgb(0 0 0 / 0.1);
  }
}

/* Utilities layer */
@layer utilities {
  .sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    clip: rect(0, 0, 0, 0);
  }
  
  .flex {
    display: flex;
  }
  
  .grid {
    display: grid;
  }
}

/* Overrides layer - highest specificity in layers */
@layer overrides {
  .btn-primary {
    background: var(--color-primary);
    color: white;
  }
}
```

### Nested Layers

```css
@layer framework {
  @layer base, components;
  
  @layer base {
    /* Framework base styles */
  }
  
  @layer components {
    /* Framework components */
  }
}

@layer app {
  @layer base, components;
  
  @layer base {
    /* App base styles */
  }
  
  @layer components {
    /* App components */
  }
}
```

### Importing into Layers

```css
/* Import external stylesheet into a layer */
@import url("reset.css") layer(reset);
@import url("framework.css") layer(framework);

/* Layer order still respected */
@layer reset, framework, app;
```

---

## Subgrid

### Basic Subgrid

```css
/* Parent grid */
.page-layout {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  grid-template-rows: auto 1fr auto;
  gap: 1rem;
}

/* Child inherits parent tracks */
.main-content {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: subgrid;
  gap: 1rem;
}
```

### Card Grid with Subgrid

```css
/* Cards align across rows */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.card {
  display: grid;
  grid-template-rows: auto 1fr auto;
  /* Each card has consistent internal alignment */
}

/* With subgrid for cross-card alignment */
.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, auto 1fr auto);
  gap: 1.5rem;
}

.card {
  display: grid;
  grid-template-rows: subgrid;
  grid-row: span 3;
}
```

### Subgrid with Fallback

```css
/* Fallback */
.grid-parent {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.grid-child {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

/* Enhancement */
@supports (grid-template-columns: subgrid) {
  .grid-child {
    grid-column: 1 / -1;
    grid-template-columns: subgrid;
  }
}
```

---

## CSS Nesting

### Native CSS Nesting

```css
/* Native CSS nesting (supported in modern browsers) */
.card {
  background: white;
  border-radius: 0.5rem;
  
  & .card-header {
    padding: 1rem;
    border-bottom: 1px solid #eee;
  }
  
  & .card-body {
    padding: 1rem;
  }
  
  /* State variations */
  &:hover {
    box-shadow: 0 4px 6px rgb(0 0 0 / 0.1);
  }
  
  &.is-featured {
    border: 2px solid var(--color-primary);
  }
  
  /* Media query nesting */
  @media (min-width: 768px) {
    display: grid;
    grid-template-columns: 200px 1fr;
  }
}
```

### Nesting with :has() and Container Queries

```css
.product-card {
  container-type: inline-size;
  
  & .product-image {
    aspect-ratio: 16 / 9;
  }
  
  & .product-info {
    padding: 1rem;
  }
  
  /* Container query inside nesting */
  @container (min-width: 400px) {
    display: grid;
    grid-template-columns: 150px 1fr;
    
    & .product-image {
      aspect-ratio: 1;
    }
  }
  
  /* :has() inside nesting */
  &:has(.sale-badge) {
    border: 2px solid red;
    
    & .original-price {
      text-decoration: line-through;
    }
  }
}
```

---

## Logical Properties

### Direction-Agnostic Layout

```css
/* Physical properties (avoid) */
.card {
  margin-left: 1rem;
  padding-top: 1rem;
  border-right: 1px solid;
  text-align: left;
}

/* Logical properties (preferred) */
.card {
  margin-inline-start: 1rem;
  padding-block-start: 1rem;
  border-inline-end: 1px solid;
  text-align: start;
}
```

### Logical Property Reference

| Physical | Logical |
|----------|---------|
| `margin-left` | `margin-inline-start` |
| `margin-right` | `margin-inline-end` |
| `margin-top` | `margin-block-start` |
| `margin-bottom` | `margin-block-end` |
| `padding-left` | `padding-inline-start` |
| `width` | `inline-size` |
| `height` | `block-size` |
| `top` | `inset-block-start` |
| `left` | `inset-inline-start` |

### Shorthand Logical Properties

```css
.element {
  /* Block (top/bottom) and inline (left/right) */
  margin-block: 1rem 2rem;    /* block-start block-end */
  margin-inline: auto;        /* inline-start inline-end */
  padding-block: 1rem;        /* both block directions */
  
  /* Inset shorthand */
  inset: 0;                   /* all sides */
  inset-block: 1rem;          /* top/bottom */
  inset-inline: 2rem;         /* left/right */
  
  /* Size */
  inline-size: 100%;          /* width */
  block-size: auto;           /* height */
  max-inline-size: 80ch;      /* max-width */
}
```

---

## Color Functions

### Modern Color Syntax

```css
:root {
  /* Modern RGB (no commas, optional alpha) */
  --color-primary: rgb(59 130 246);
  --color-primary-50: rgb(59 130 246 / 0.5);
  
  /* HSL */
  --color-accent: hsl(220 90% 56%);
  --color-accent-light: hsl(220 90% 56% / 0.2);
  
  /* OKLCH - perceptually uniform */
  --color-brand: oklch(65% 0.19 250);
  --color-brand-light: oklch(85% 0.1 250);
  --color-brand-dark: oklch(45% 0.19 250);
  
  /* color-mix() */
  --color-mixed: color-mix(in srgb, var(--color-primary) 70%, white);
}
```

### Relative Color Syntax

```css
:root {
  --base-color: #3b82f6;
  
  /* Create variations from base */
  --lighter: hsl(from var(--base-color) h s calc(l + 20%));
  --darker: hsl(from var(--base-color) h s calc(l - 20%));
  --muted: hsl(from var(--base-color) h calc(s - 30%) l);
  
  /* OKLCH relative colors */
  --oklch-lighter: oklch(from var(--base-color) calc(l + 0.2) c h);
}
```

---

## View Transitions

### Basic Page Transitions

```css
/* Opt-in to view transitions */
@view-transition {
  navigation: auto;
}

/* Default transition */
::view-transition-old(root),
::view-transition-new(root) {
  animation-duration: 0.3s;
}

/* Custom transition */
::view-transition-old(root) {
  animation: fade-out 0.3s ease-out;
}

::view-transition-new(root) {
  animation: fade-in 0.3s ease-in;
}

@keyframes fade-out {
  to { opacity: 0; }
}

@keyframes fade-in {
  from { opacity: 0; }
}
```

### Named View Transitions

```css
/* Mark element for individual transition */
.hero-image {
  view-transition-name: hero;
}

/* Style the hero transition */
::view-transition-old(hero),
::view-transition-new(hero) {
  animation-duration: 0.5s;
}

::view-transition-group(hero) {
  animation-timing-function: ease-in-out;
}
```

---

## Scroll-Driven Animations

### Scroll Progress Animation

```css
/* Animation tied to scroll progress */
@keyframes reveal {
  from {
    opacity: 0;
    transform: translateY(50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-on-scroll {
  animation: reveal linear;
  animation-timeline: view();
  animation-range: entry 0% cover 40%;
}
```

### Scroll-Linked Header

```css
@keyframes shrink-header {
  from {
    padding-block: 2rem;
    background: transparent;
  }
  to {
    padding-block: 0.5rem;
    background: white;
    box-shadow: 0 2px 10px rgb(0 0 0 / 0.1);
  }
}

.header {
  position: sticky;
  top: 0;
  animation: shrink-header linear;
  animation-timeline: scroll();
  animation-range: 0 200px;
}
```

---

## Performance Patterns

### Content-Visibility

```css
/* Defer rendering of off-screen content */
.card {
  content-visibility: auto;
  contain-intrinsic-size: auto 300px;
}

/* Skip rendering entirely when hidden */
.hidden-section {
  content-visibility: hidden;
}
```

### Containment

```css
/* Full containment for isolated components */
.widget {
  contain: strict; /* layout, paint, size */
}

/* Layout and paint containment */
.card {
  contain: layout paint;
}

/* Content containment (common for scrollable areas) */
.scrollable-list {
  contain: content;
}
```

### Will-Change (Use Sparingly)

```css
/* Only when animation is imminent */
.card:hover {
  will-change: transform;
}

.card:active {
  transform: scale(0.98);
}

/* Remove after animation */
.card {
  will-change: auto;
}
```

---

## Severity Guide

| Severity | Issue | Impact |
|----------|-------|--------|
| 🔴 Critical | No fallback for critical features | Broken in older browsers |
| 🔴 Critical | Layout thrashing animations | Poor performance |
| 🟠 High | Missing container queries | Non-responsive components |
| 🟠 High | Unorganized specificity | Maintenance nightmare |
| 🟡 Medium | No logical properties | RTL support issues |
| 🟡 Medium | Overuse of !important | Cascade problems |
| 🟢 Low | Missing CSS nesting | Verbosity only |

---

## Browser Support Reference (2026)

| Feature | Chrome | Firefox | Safari | Edge |
|---------|--------|---------|--------|------|
| Container Queries | 105+ | 110+ | 16+ | 105+ |
| :has() | 105+ | 121+ | 15.4+ | 105+ |
| Cascade Layers | 99+ | 97+ | 15.4+ | 99+ |
| Subgrid | 117+ | 71+ | 16+ | 117+ |
| CSS Nesting | 120+ | 117+ | 17.2+ | 120+ |
| View Transitions | 111+ | ❌ | 18+ | 111+ |
| Scroll Animations | 115+ | ❌ | ❌ | 115+ |

---

## Report Template

```markdown
## Modern CSS Review

### Browser Targets
- Minimum: [browsers]
- Progressive enhancement: [yes/no]

### Modern Features Usage
| Feature | Used | Fallback | Status |
|---------|------|----------|--------|
| Container Queries | | | |
| :has() | | | |
| Cascade Layers | | | |
| Subgrid | | | |
| Logical Properties | | | |

### Issues Found
1. [Severity] Issue description
   - Impact: 
   - Recommendation:

### Modernization Opportunities
1. [Feature] Current approach → Modern approach
```

---

## Related Prompts

- [typescript-patterns.md](typescript-patterns.md) — TypeScript for CSS-in-JS
- [react-components.md](react-components.md) — React component styling
- [frontend-testing.md](frontend-testing.md) — Visual regression testing
- [accessibility-check.md](../html/accessibility-check.md) — Accessible styling

---

*Last updated: 2026-01*

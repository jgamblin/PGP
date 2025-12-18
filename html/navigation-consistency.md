# Navigation Consistency — User-Friendly Menus

> **Purpose**: Create consistent, accessible navigation patterns  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: Navigation, Menus, Headers, Sidebars  
> **Last Updated**: 2025-12

---

## Mission

Help create **consistent, user-friendly navigation** that is accessible, works across devices, and helps users find what they need quickly.

---

## Guard Clauses

**If no navigation code provided:**
```
NO_NAV_PROVIDED

Please provide navigation to review:
- Current HTML markup
- Site structure/pages
- Design requirements

I'll help improve your navigation.
```

**If navigation is already good:**
```
NAVIGATION_APPROVED

✅ **Navigation Looks Good**

Quality checks passed:
- Clear structure ✓
- Keyboard accessible ✓
- Mobile-friendly ✓
- Consistent placement ✓
- Descriptive labels ✓

Minor suggestions (if any):
[LIST ENHANCEMENTS]
```

---

## Quick Context Checklist

```
☐ Current navigation HTML
☐ Site structure (pages/sections)
☐ Mobile requirements
☐ Accessibility requirements
☐ Design constraints
```

---

## Copy-Paste Navigation Prompts

### Prompt: Review Navigation
```text
Review this navigation for usability and accessibility:

{{HTML}}

Check:
1. Semantic HTML structure
2. Keyboard navigation
3. Screen reader support
4. Mobile responsiveness
5. Clear labeling
6. Consistent patterns

Suggest improvements with code examples.
```

### Prompt: Create Navigation
```text
Create navigation for this site structure:

Pages:
- {{PAGE_1}}
- {{PAGE_2}}
- {{PAGE_3}}

Requirements:
- {{REQUIREMENTS}}

Provide:
1. HTML structure
2. CSS (BEM)
3. Mobile menu behavior
4. Accessibility features
```

### Prompt: Fix Mobile Menu
```text
Make this navigation mobile-friendly:

{{HTML}}

Requirements:
- Hamburger menu on mobile
- Smooth transitions
- Touch-friendly targets (44px min)
- Works without JavaScript (progressive enhancement)

Provide HTML, CSS, and minimal JS.
```

### Prompt: Add Mega Menu
```text
Convert this navigation to a mega menu:

{{HTML}}

Sections needed:
- {{SECTION_1}}
- {{SECTION_2}}

Include:
1. Accessible markup
2. Keyboard navigation
3. Hover and click support
4. Mobile fallback
```

### Prompt: Breadcrumb Navigation
```text
Create breadcrumb navigation for:

Site: {{SITE_NAME}}
Current path: {{PATH}}

Include:
1. Semantic markup with schema.org
2. Accessible structure
3. Responsive design
4. Clear separators
```

---

## Navigation Patterns

### Primary Navigation
```html
<header class="header">
  <a href="/" class="header__logo">
    <img src="logo.svg" alt="Site Name">
  </a>
  
  <nav class="nav" aria-label="Main navigation">
    <ul class="nav__list">
      <li class="nav__item">
        <a href="/" class="nav__link nav__link--active" aria-current="page">Home</a>
      </li>
      <li class="nav__item">
        <a href="/about" class="nav__link">About</a>
      </li>
      <li class="nav__item">
        <a href="/services" class="nav__link">Services</a>
      </li>
      <li class="nav__item">
        <a href="/contact" class="nav__link">Contact</a>
      </li>
    </ul>
  </nav>
  
  <button class="nav__toggle" aria-expanded="false" aria-controls="nav-menu">
    <span class="sr-only">Menu</span>
    <span class="nav__toggle-icon"></span>
  </button>
</header>
```

### Mobile Menu CSS
```css
.nav__list {
  display: flex;
  gap: 1rem;
  list-style: none;
}

.nav__link {
  display: block;
  padding: 0.5rem 1rem;
  color: inherit;
  text-decoration: none;
}

.nav__link:hover,
.nav__link:focus {
  text-decoration: underline;
}

.nav__link--active {
  font-weight: bold;
}

.nav__toggle {
  display: none;
}

/* Mobile styles */
@media (max-width: 768px) {
  .nav__list {
    position: fixed;
    top: 60px;
    left: 0;
    right: 0;
    flex-direction: column;
    background: white;
    padding: 1rem;
    transform: translateY(-100%);
    transition: transform 0.3s ease;
  }
  
  .nav__list[data-open="true"] {
    transform: translateY(0);
  }
  
  .nav__toggle {
    display: block;
  }
}
```

### Dropdown Menu
```html
<li class="nav__item nav__item--dropdown">
  <button class="nav__link nav__link--dropdown" 
          aria-expanded="false" 
          aria-haspopup="true">
    Services
    <span class="nav__arrow" aria-hidden="true">▼</span>
  </button>
  <ul class="nav__dropdown" role="menu">
    <li role="none">
      <a href="/web-design" class="nav__dropdown-link" role="menuitem">Web Design</a>
    </li>
    <li role="none">
      <a href="/development" class="nav__dropdown-link" role="menuitem">Development</a>
    </li>
    <li role="none">
      <a href="/consulting" class="nav__dropdown-link" role="menuitem">Consulting</a>
    </li>
  </ul>
</li>
```

### Breadcrumbs
```html
<nav aria-label="Breadcrumb" class="breadcrumb">
  <ol class="breadcrumb__list" itemscope itemtype="https://schema.org/BreadcrumbList">
    <li class="breadcrumb__item" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <a href="/" class="breadcrumb__link" itemprop="item">
        <span itemprop="name">Home</span>
      </a>
      <meta itemprop="position" content="1">
    </li>
    <li class="breadcrumb__item" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <a href="/products" class="breadcrumb__link" itemprop="item">
        <span itemprop="name">Products</span>
      </a>
      <meta itemprop="position" content="2">
    </li>
    <li class="breadcrumb__item" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <span itemprop="name" aria-current="page">Widget Pro</span>
      <meta itemprop="position" content="3">
    </li>
  </ol>
</nav>
```

### Skip Link
```html
<!-- First element in body -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<style>
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  padding: 8px 16px;
  background: #000;
  color: #fff;
  z-index: 100;
  transition: top 0.2s;
}

.skip-link:focus {
  top: 0;
}
</style>
```

---

## Accessibility Checklist

### Keyboard Navigation
- [ ] All links/buttons focusable with Tab
- [ ] Logical tab order
- [ ] Visible focus indicators
- [ ] Enter/Space activates items
- [ ] Escape closes dropdowns
- [ ] Arrow keys navigate within menus

### Screen Readers
- [ ] `<nav>` element with `aria-label`
- [ ] Current page marked with `aria-current="page"`
- [ ] Expandable menus use `aria-expanded`
- [ ] Dropdowns use `aria-haspopup`
- [ ] Skip link provided

### Visual
- [ ] Sufficient color contrast
- [ ] Active state clearly visible
- [ ] Hover/focus states distinct
- [ ] Touch targets 44px minimum

---

## Common Navigation Issues

| Issue | Problem | Fix |
|-------|---------|-----|
| No keyboard support | Can't navigate without mouse | Add proper tabindex, use buttons |
| Missing aria-current | Screen readers don't know current page | Add `aria-current="page"` |
| Dropdown hover only | Doesn't work on touch | Add click/tap support |
| Small touch targets | Hard to tap on mobile | Minimum 44x44px |
| No skip link | Must tab through all nav items | Add skip link at top |
| No focus indicators | Can't see keyboard position | Style `:focus` state |

---

## Mobile Navigation Best Practices

### Hamburger Menu
```html
<button class="nav__toggle" 
        aria-expanded="false" 
        aria-controls="main-nav"
        aria-label="Toggle navigation">
  <span class="hamburger">
    <span class="hamburger__line"></span>
    <span class="hamburger__line"></span>
    <span class="hamburger__line"></span>
  </span>
</button>
```

### Touch-Friendly Spacing
```css
/* Minimum touch target size */
.nav__link {
  display: block;
  padding: 12px 16px;
  min-height: 44px;
  min-width: 44px;
}

/* Adequate spacing between items */
.nav__item + .nav__item {
  margin-top: 4px;
}
```

### Progressive Enhancement
```css
/* Works without JS */
.nav__list {
  display: block;
}

/* Enhanced with JS */
.js .nav__list {
  display: none;
}

.js .nav__list[data-open="true"] {
  display: block;
}
```

---

## Report Format

### Navigation Review: `nav-review-[YYYY-MM-DD].md`

```markdown
# Navigation Review

## Summary
- **Pages/Links**: [Count]
- **Depth**: [Levels]
- **Mobile Support**: [Yes/No/Partial]
- **Accessibility**: [Score/10]

## Findings

### 🔴 Critical (Blocks Access)
| Issue | Location | Fix |
|-------|----------|-----|

### 🟠 High (Major UX Issue)
| Issue | Location | Fix |
|-------|----------|-----|

### 🟡 Medium (Should Improve)
| Issue | Location | Fix |
|-------|----------|-----|

### 🟢 Low (Enhancement)
| Issue | Location | Fix |
|-------|----------|-----|

## Recommendations
1. [Priority 1]
2. [Priority 2]

## Testing Performed
- [ ] Keyboard only navigation
- [ ] Screen reader testing
- [ ] Mobile device testing
- [ ] Various viewport sizes
```

---

## Severity Guide

| Level | Icon | Impact | Examples |
|-------|------|--------|----------|
| **Critical** | 🔴 | Can't navigate | Keyboard trap, broken links |
| **High** | 🟠 | Major difficulty | No mobile menu, missing labels |
| **Medium** | 🟡 | Usability issue | Poor focus indicators, small targets |
| **Low** | 🟢 | Enhancement | Could be more intuitive |

# Semantic Markup Refinement — HTML Structure Audit

> **Purpose**: Improve HTML document structure and semantics  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: HTML5 Semantic Elements, Document Outline, Accessibility  
> **Last Updated**: 2026-03

---

> **Legacy Path Notice**: `html/` is maintained for backward compatibility. For stack-first guidance, also use [frontend/agents.md](../frontend/agents.md). 
> **Migration Map**: [docs/compat/html-to-frontend-map.md](../docs/compat/html-to-frontend-map.md)

## Mission

Transform **div soup into meaningful HTML** structure. Improve document outline, accessibility, and SEO through proper semantic element usage.

---

## Guard Clauses

**If no HTML provided:**
```
NO_HTML_PROVIDED

Please share HTML to review:
- Full page document
- Component markup
- Or describe the content structure

I'll suggest semantic improvements.
```

**If HTML is already semantic:**
```
SEMANTICS_GOOD

✅ **Well-Structured HTML**

Your markup uses semantic elements correctly:
- Document structure: Proper ✓
- Heading hierarchy: Correct ✓
- Sectioning elements: Appropriate ✓
- Landmarks: Present ✓

Minor suggestions (optional):
[list any refinements]
```

---

## Quick Context Checklist

```
☐ HTML markup to review
☐ Page purpose (article, product, form, etc.)
☐ Content hierarchy description
☐ Target audience (if relevant)
☐ Accessibility requirements
```

---

## Copy-Paste Prompts

### Prompt: Full Semantic Audit
```text
Review this HTML for semantic structure:

{{HTML_CODE}}

Check:
1. Document structure (header, main, footer)
2. Heading hierarchy (h1-h6)
3. Sectioning elements (article, section, nav, aside)
4. Lists usage (ul, ol, dl)
5. Interactive elements (button vs a)

Provide refactored HTML with semantic elements.
```

### Prompt: Convert Div Soup
```text
Convert this div-based markup to semantic HTML5:

{{DIV_SOUP}}

Requirements:
- Use proper sectioning elements
- Add landmark roles where needed
- Maintain heading hierarchy
- Keep classes for styling

Show before/after comparison.
```

### Prompt: Document Outline Check
```text
Analyze the document outline of this HTML:

{{HTML_CODE}}

Generate:
1. Current outline structure
2. Heading hierarchy issues
3. Sectioning problems
4. Fixed outline structure
5. Corrected HTML
```

### Prompt: Component Semantics
```text
What semantic element should wrap this content?

Content type: {{CONTENT_DESCRIPTION}}
Current markup: {{CURRENT_HTML}}

Suggest:
1. Appropriate wrapper element
2. Child element structure
3. ARIA roles if needed
4. Complete semantic markup
```

### Prompt: Landing Page Structure
```text
Create semantic HTML structure for a landing page with:

{{PAGE_SECTIONS}}

Include:
- Proper document outline
- Landmark regions
- Skip navigation
- Schema.org basics
- All semantic elements
```

---

## Semantic Elements Reference

### Document Structure

| Element | Purpose | Contains |
|---------|---------|----------|
| `<header>` | Introductory content | Logo, nav, search |
| `<nav>` | Navigation links | ul/ol of links |
| `<main>` | Main content (one per page) | Primary content |
| `<article>` | Self-contained content | Blog post, product, comment |
| `<section>` | Thematic grouping | Related content with heading |
| `<aside>` | Tangentially related | Sidebar, callout, related |
| `<footer>` | Footer information | Copyright, links, contact |

### Content Sectioning

| Element | Use For | Not For |
|---------|---------|---------|
| `<article>` | Independent, reusable content | Generic grouping |
| `<section>` | Thematic group with heading | Styling wrapper |
| `<nav>` | Major navigation | Single links |
| `<aside>` | Supplementary content | Primary content |

### Text Semantics

| Element | Purpose | Example |
|---------|---------|---------|
| `<strong>` | Important text | Warnings, key points |
| `<em>` | Stressed emphasis | Tone change |
| `<mark>` | Highlighted/relevant | Search results |
| `<time>` | Date/time | `<time datetime="2025-12-17">` |
| `<code>` | Code fragment | Inline code |
| `<abbr>` | Abbreviation | `<abbr title="HyperText">HTML</abbr>` |
| `<cite>` | Creative work title | Book, article names |
| `<q>` | Inline quotation | Short quotes |
| `<blockquote>` | Block quotation | Long quotes |
| `<address>` | Contact information | Author contact |

### Lists

| Element | Use For | Structure |
|---------|---------|-----------|
| `<ul>` | Unordered items | Navigation, features |
| `<ol>` | Ordered/sequential | Steps, rankings |
| `<dl>` | Key-value pairs | Glossary, metadata |

---

## Common Patterns

### Page Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page Title</title>
</head>
<body>
  <a href="#main" class="skip-link">Skip to main content</a>
  
  <header>
    <nav aria-label="Primary">
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
      </ul>
    </nav>
  </header>
  
  <main id="main">
    <h1>Page Title</h1>
    <!-- Main content -->
  </main>
  
  <footer>
    <p>&copy; 2025 Company Name</p>
  </footer>
</body>
</html>
```

### Blog Article
```html
<article>
  <header>
    <h2><a href="/post/slug">Article Title</a></h2>
    <p>
      By <address class="author"><a href="/author/name">Author Name</a></address>
      on <time datetime="2025-12-17">December 17, 2025</time>
    </p>
  </header>
  
  <p>Article introduction...</p>
  
  <section>
    <h3>Section Heading</h3>
    <p>Section content...</p>
  </section>
  
  <footer>
    <p>Tags: 
      <a href="/tag/html" rel="tag">HTML</a>,
      <a href="/tag/css" rel="tag">CSS</a>
    </p>
  </footer>
</article>
```

### Product Card
```html
<article class="product-card">
  <a href="/product/123">
    <img src="product.jpg" alt="Product Name - Blue, Size M" width="300" height="300">
  </a>
  <header>
    <h3><a href="/product/123">Product Name</a></h3>
  </header>
  <p class="price">
    <data value="29.99">$29.99</data>
  </p>
  <p class="description">Short product description.</p>
  <button type="button">Add to Cart</button>
</article>
```

### Navigation
```html
<!-- Primary Navigation -->
<nav aria-label="Primary">
  <ul>
    <li><a href="/" aria-current="page">Home</a></li>
    <li><a href="/products">Products</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>

<!-- Breadcrumb -->
<nav aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/products">Products</a></li>
    <li><a href="/products/widgets" aria-current="page">Widgets</a></li>
  </ol>
</nav>
```

### Definition List
```html
<dl class="product-specs">
  <dt>Material</dt>
  <dd>100% Cotton</dd>
  
  <dt>Dimensions</dt>
  <dd>10" x 12" x 4"</dd>
  
  <dt>Weight</dt>
  <dd>2.5 lbs</dd>
</dl>
```

### Figure with Caption
```html
<figure>
  <img src="chart.png" alt="Bar chart showing sales growth from 2020-2025">
  <figcaption>
    <strong>Figure 1:</strong> Annual sales growth showing 150% increase over 5 years.
  </figcaption>
</figure>
```

---

## Anti-Patterns to Fix

### ❌ Div Soup → ✅ Semantic

```html
<!-- ❌ Before -->
<div class="header">
  <div class="nav">
    <div class="nav-item"><a href="/">Home</a></div>
  </div>
</div>
<div class="content">
  <div class="post">
    <div class="title">Post Title</div>
  </div>
</div>
<div class="footer">Copyright 2025</div>

<!-- ✅ After -->
<header>
  <nav aria-label="Primary">
    <ul>
      <li><a href="/">Home</a></li>
    </ul>
  </nav>
</header>
<main>
  <article>
    <h1>Post Title</h1>
  </article>
</main>
<footer>
  <p>&copy; 2025</p>
</footer>
```

### ❌ Broken Heading Hierarchy → ✅ Fixed

```html
<!-- ❌ Before -->
<h1>Site Name</h1>
<h3>Welcome</h3>
<h5>Features</h5>
<h2>About</h2>

<!-- ✅ After -->
<header>
  <p class="site-name">Site Name</p>
</header>
<main>
  <h1>Welcome</h1>
  <section>
    <h2>Features</h2>
  </section>
  <section>
    <h2>About</h2>
  </section>
</main>
```

### ❌ Button vs Link

```html
<!-- ❌ Wrong: Link styled as button for action -->
<a href="#" class="btn" onclick="submitForm()">Submit</a>

<!-- ✅ Correct: Button for actions -->
<button type="submit" class="btn">Submit</button>

<!-- ❌ Wrong: Button for navigation -->
<button onclick="location.href='/about'">About Us</button>

<!-- ✅ Correct: Link for navigation -->
<a href="/about" class="btn">About Us</a>
```

### ❌ Missing List Semantics

```html
<!-- ❌ Before -->
<div class="features">
  <div class="feature">Fast</div>
  <div class="feature">Secure</div>
  <div class="feature">Reliable</div>
</div>

<!-- ✅ After -->
<ul class="features">
  <li>Fast</li>
  <li>Secure</li>
  <li>Reliable</li>
</ul>
```

---

## Report Format

### Semantic Audit: `semantic-audit-[YYYY-MM-DD].md`

```markdown
# Semantic Markup Audit

## Summary
- **Elements Reviewed**: [Count]
- **Issues Found**: [Count]
- **Semantic Score**: [X/10]

## Document Outline
```
Current:
├── h1: [Text]
├── h3: [Text] ⚠️ Skipped h2
└── h2: [Text]

Recommended:
├── h1: [Text]
├── h2: [Text]
└── h2: [Text]
```

## Issues

### Critical
| Location | Issue | Fix |
|----------|-------|-----|

### Improvements
| Location | Current | Suggested |
|----------|---------|-----------|

## Refactored HTML
[Include corrected markup]
```

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | No h1, broken outline, no main element |
| **High** | 🟠 | Heading hierarchy skips, missing nav |
| **Medium** | 🟡 | Div instead of section, missing article |
| **Low** | 🟢 | Could use figure, time, or address |

---

## Validation Tools

| Tool | Purpose | URL |
|------|---------|-----|
| W3C Validator | HTML validation | validator.w3.org |
| HeadingsMap | Check outline | Browser extension |
| WAVE | Accessibility + structure | wave.webaim.org |
| Lighthouse | SEO + accessibility | Chrome DevTools |
| HTML5 Outliner | Document outline | gsnedders.html5.org |

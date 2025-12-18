# Performance & Core Web Vitals — Speed Optimization

> **Purpose**: Optimize website speed and user experience  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Metrics**: LCP, FID/INP, CLS  
> **Last Updated**: 2025-12

---

## Mission

Help improve **website performance and Core Web Vitals** to make pages load faster, respond quicker, and provide a stable visual experience.

---

## Guard Clauses

**If no code/URL provided:**
```
NO_CONTENT_PROVIDED

Please provide content to audit:
- HTML/CSS code
- Page URL
- Lighthouse report
- Specific performance concerns

I'll analyze and suggest optimizations.
```

**If performance is already good:**
```
PERFORMANCE_GOOD

✅ **Core Web Vitals Pass**

- LCP: < 2.5s ✓
- FID/INP: < 100ms ✓
- CLS: < 0.1 ✓

Your page meets Google's performance thresholds.

Optional optimizations:
[LIST ANY MINOR IMPROVEMENTS]
```

---

## Quick Context Checklist

```
☐ Page URL or HTML/CSS code
☐ Current performance metrics
☐ Largest content element
☐ Known slow areas
☐ Hosting/CDN setup
```

---

## Copy-Paste Performance Prompts

### Prompt: Full Performance Audit
```text
Audit this page for Core Web Vitals:

{{URL_OR_CODE}}

Analyze:
1. LCP (Largest Contentful Paint) - target < 2.5s
2. INP (Interaction to Next Paint) - target < 200ms
3. CLS (Cumulative Layout Shift) - target < 0.1

For each issue:
- Current impact
- Specific fix
- Expected improvement

Prioritize by impact.
```

### Prompt: Fix Slow Loading
```text
This page loads slowly. Help optimize:

{{CODE}}

Current LCP: {{TIME}}

Check:
1. Large unoptimized images
2. Render-blocking resources
3. Slow server response
4. Unoptimized fonts
5. Large JavaScript bundles

Provide specific fixes with code.
```

### Prompt: Fix Layout Shift
```text
This page has layout shift issues (CLS):

{{CODE}}

Identify:
1. Images without dimensions
2. Dynamic content insertion
3. Web fonts causing FOIT/FOUT
4. Ads or embeds
5. Late-loading content

Show how to reserve space for each element.
```

### Prompt: Optimize Images
```text
Optimize images for this page:

{{CODE}}

For each image provide:
1. Recommended format (WebP, AVIF)
2. Responsive srcset
3. Lazy loading setup
4. Width/height attributes
5. Placeholder strategy
```

### Prompt: Critical CSS
```text
Extract critical CSS for above-the-fold content:

{{HTML}}
{{CSS}}

Provide:
1. Inline critical CSS
2. Defer remaining CSS
3. Loading strategy
```

---

## Core Web Vitals Reference

### LCP (Largest Contentful Paint)
**Target: < 2.5s**

| Rating | Time | Status |
|--------|------|--------|
| Good | ≤ 2.5s | ✅ |
| Needs Improvement | 2.5s - 4s | 🟡 |
| Poor | > 4s | 🔴 |

**Common LCP Elements:**
- Hero images
- Large text blocks
- Video poster images
- Background images

### INP (Interaction to Next Paint)
**Target: < 200ms**

| Rating | Time | Status |
|--------|------|--------|
| Good | ≤ 200ms | ✅ |
| Needs Improvement | 200ms - 500ms | 🟡 |
| Poor | > 500ms | 🔴 |

**Common INP Issues:**
- Long JavaScript tasks
- Heavy event handlers
- Layout thrashing
- Main thread blocking

### CLS (Cumulative Layout Shift)
**Target: < 0.1**

| Rating | Score | Status |
|--------|-------|--------|
| Good | ≤ 0.1 | ✅ |
| Needs Improvement | 0.1 - 0.25 | 🟡 |
| Poor | > 0.25 | 🔴 |

**Common CLS Causes:**
- Images without dimensions
- Ads, embeds, iframes
- Dynamically injected content
- Web fonts causing FOIT/FOUT

---

## Performance Fixes

### Images

```html
<!-- ❌ Bad: No dimensions, not lazy loaded -->
<img src="hero.jpg">

<!-- ✅ Good: Dimensions, lazy loading, modern format -->
<img 
  src="hero.webp"
  alt="Hero image description"
  width="1200"
  height="600"
  loading="lazy"
  decoding="async"
>

<!-- ✅ Better: Responsive with srcset -->
<img 
  src="hero-800.webp"
  srcset="
    hero-400.webp 400w,
    hero-800.webp 800w,
    hero-1200.webp 1200w
  "
  sizes="(max-width: 600px) 400px, (max-width: 1000px) 800px, 1200px"
  alt="Hero image description"
  width="1200"
  height="600"
  loading="lazy"
>
```

### Critical CSS

```html
<head>
  <!-- Inline critical CSS -->
  <style>
    /* Above-the-fold styles only */
    body { margin: 0; font-family: system-ui; }
    .header { height: 60px; background: #fff; }
    .hero { min-height: 400px; background: #f0f0f0; }
  </style>
  
  <!-- Defer non-critical CSS -->
  <link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="styles.css"></noscript>
</head>
```

### Font Loading

```html
<!-- Preload critical fonts -->
<link rel="preload" href="/fonts/main.woff2" as="font" type="font/woff2" crossorigin>

<style>
/* Use font-display: swap to prevent FOIT */
@font-face {
  font-family: 'Main Font';
  src: url('/fonts/main.woff2') format('woff2');
  font-display: swap;
}

/* Optional: size-adjust to reduce CLS */
@font-face {
  font-family: 'Main Font';
  src: url('/fonts/main.woff2') format('woff2');
  font-display: swap;
  size-adjust: 100.5%;
  ascent-override: 95%;
}
</style>
```

### Prevent Layout Shift

```css
/* Reserve space for images */
.image-container {
  aspect-ratio: 16 / 9;
  background: #f0f0f0;
}

/* Reserve space for ads */
.ad-slot {
  min-height: 250px;
  background: #f5f5f5;
}

/* Reserve space for embeds */
.video-embed {
  aspect-ratio: 16 / 9;
  background: #000;
}
```

### Resource Hints

```html
<head>
  <!-- Preconnect to required origins -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://cdn.example.com" crossorigin>
  
  <!-- DNS prefetch for third parties -->
  <link rel="dns-prefetch" href="https://analytics.example.com">
  
  <!-- Preload critical resources -->
  <link rel="preload" href="/critical.css" as="style">
  <link rel="preload" href="/hero.webp" as="image">
  
  <!-- Prefetch next page -->
  <link rel="prefetch" href="/next-page.html">
</head>
```

---

## Performance Checklist

### Images
- [ ] All images have width and height
- [ ] Using modern formats (WebP, AVIF)
- [ ] Responsive images with srcset
- [ ] Lazy loading below the fold
- [ ] Optimized file sizes

### CSS
- [ ] Critical CSS inlined
- [ ] Non-critical CSS deferred
- [ ] No unused CSS
- [ ] No render-blocking stylesheets

### JavaScript
- [ ] Deferred or async loading
- [ ] No long tasks (> 50ms)
- [ ] Code splitting implemented
- [ ] Tree shaking enabled

### Fonts
- [ ] font-display: swap used
- [ ] Fonts preloaded
- [ ] Subset fonts if possible
- [ ] Fallback fonts specified

### Layout Stability
- [ ] Reserved space for dynamic content
- [ ] No content injection above fold
- [ ] Ads have reserved space
- [ ] Transform animations (not layout)

---

## Testing Tools

| Tool | Purpose | URL |
|------|---------|-----|
| **PageSpeed Insights** | Core Web Vitals | pagespeed.web.dev |
| **Lighthouse** | Comprehensive audit | DevTools > Lighthouse |
| **WebPageTest** | Detailed waterfall | webpagetest.org |
| **Chrome UX Report** | Real user data | crux.run |
| **web.dev/measure** | Quick check | web.dev/measure |

---

## Report Format

### Performance Audit: `perf-audit-[YYYY-MM-DD].md`

```markdown
# Performance Audit

## Core Web Vitals
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| LCP | [time] | < 2.5s | 🔴/🟡/✅ |
| INP | [time] | < 200ms | 🔴/🟡/✅ |
| CLS | [score] | < 0.1 | 🔴/🟡/✅ |

## Key Findings

### 🔴 Critical (Major Impact)
| Issue | Impact | Fix |
|-------|--------|-----|

### 🟠 High (Significant Impact)
| Issue | Impact | Fix |
|-------|--------|-----|

### 🟡 Medium (Moderate Impact)
| Issue | Impact | Fix |
|-------|--------|-----|

### 🟢 Low (Minor Impact)
| Issue | Impact | Fix |
|-------|--------|-----|

## Optimization Plan
1. [Highest impact fix first]
2. [Second priority]
3. [Third priority]

## Expected Improvements
- LCP: [current] → [expected]
- CLS: [current] → [expected]
- Page weight: [current] → [expected]
```

---

## Severity Guide

| Level | Icon | Impact | Examples |
|-------|------|--------|----------|
| **Critical** | 🔴 | Fails Core Web Vitals | LCP > 4s, CLS > 0.25 |
| **High** | 🟠 | Needs improvement | Large unoptimized images |
| **Medium** | 🟡 | Noticeable delay | Missing preconnects |
| **Low** | 🟢 | Minor optimization | Could use newer format |

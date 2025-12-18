# Accessibility Check — WCAG Compliance Audit

> **Purpose**: Ensure websites are accessible to all users  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Standard**: WCAG 2.1 AA  
> **Last Updated**: 2025-12

---

## Mission

Help make **websites accessible to all users** including those using screen readers, keyboards, and other assistive technologies. Focus on WCAG 2.1 AA compliance.

---

## Guard Clauses

**If no HTML provided:**
```
NO_HTML_PROVIDED

Please provide HTML to review:
- Paste the HTML code
- Or share the file path
- Or provide the URL to audit

Include any associated CSS if relevant.
```

**If already accessible:**
```
ACCESSIBILITY_PASS

✅ **WCAG 2.1 AA Compliant**

Checks performed:
- Images have alt text ✓
- Forms have labels ✓
- Color contrast meets 4.5:1 ✓
- Keyboard navigation works ✓
- Heading hierarchy correct ✓
- ARIA used appropriately ✓

No accessibility issues found.
```

---

## Quick Context Checklist

```
☐ HTML markup to review
☐ Associated CSS (for contrast checks)
☐ Target WCAG level (A, AA, AAA)
☐ Specific concerns or user reports
```

---

## Copy-Paste Accessibility Prompts

### Prompt: Full Accessibility Audit
```text
Perform a WCAG 2.1 AA accessibility audit:

{{HTML}}

Check:
1. 🔴 Critical: Keyboard traps, missing form labels
2. 🟠 High: Missing alt text, poor contrast
3. 🟡 Medium: Heading hierarchy, landmark regions
4. 🟢 Low: ARIA improvements, focus indicators

For each issue provide:
- WCAG criterion violated
- Impact on users
- Code fix

Prioritize by user impact.
```

### Prompt: Screen Reader Review
```text
Review this HTML for screen reader compatibility:

{{HTML}}

Check:
1. Logical reading order
2. Meaningful link text (no "click here")
3. Form labels and instructions
4. Image alt text quality
5. ARIA live regions for dynamic content
6. Skip navigation links

Simulate what a screen reader would announce.
```

### Prompt: Keyboard Navigation Audit
```text
Audit keyboard accessibility:

{{HTML}}

Verify:
1. All interactive elements focusable (Tab)
2. Logical tab order
3. Visible focus indicators
4. No keyboard traps
5. Escape closes modals
6. Arrow keys for widgets

List any keyboard-only users would struggle with.
```

### Prompt: Color Contrast Check
```text
Check color contrast compliance:

{{CSS}}

Requirements (WCAG AA):
- Normal text: 4.5:1 minimum
- Large text (18pt+): 3:1 minimum
- UI components: 3:1 minimum

For each failing color pair:
- Current ratio
- Required ratio
- Suggested fix (adjusted color)
```

### Prompt: Fix Specific Issue
```text
Fix this accessibility issue:

Issue: {{DESCRIBE_ISSUE}}
Code: {{CODE}}

Provide:
1. What's wrong
2. WCAG criterion
3. Fixed code
4. Why this matters to users
```

---

## WCAG 2.1 Quick Reference

### Perceivable (Can users perceive it?)

| Criterion | Requirement | How to Check |
|-----------|-------------|--------------|
| **1.1.1** | Alt text for images | Every `<img>` has `alt` |
| **1.3.1** | Info via structure | Use semantic HTML |
| **1.4.3** | Contrast (AA) | 4.5:1 for text |
| **1.4.4** | Resize text | Works at 200% zoom |
| **1.4.11** | Non-text contrast | 3:1 for UI elements |

### Operable (Can users operate it?)

| Criterion | Requirement | How to Check |
|-----------|-------------|--------------|
| **2.1.1** | Keyboard access | Tab through everything |
| **2.1.2** | No keyboard trap | Can Tab away from all elements |
| **2.4.1** | Skip links | Bypass repetitive content |
| **2.4.3** | Focus order | Logical tab sequence |
| **2.4.4** | Link purpose | Meaningful link text |
| **2.4.6** | Headings/labels | Descriptive headings |

### Understandable (Can users understand it?)

| Criterion | Requirement | How to Check |
|-----------|-------------|--------------|
| **3.1.1** | Page language | `<html lang="en">` |
| **3.2.1** | On focus | No unexpected changes |
| **3.3.1** | Error identification | Clear error messages |
| **3.3.2** | Labels/instructions | Forms have labels |

### Robust (Does it work with assistive tech?)

| Criterion | Requirement | How to Check |
|-----------|-------------|--------------|
| **4.1.1** | Valid HTML | No duplicate IDs |
| **4.1.2** | Name, role, value | ARIA used correctly |

---

## Common Issues & Fixes

### Missing Alt Text
```html
<!-- ❌ Bad -->
<img src="hero.jpg">

<!-- ✅ Good -->
<img src="hero.jpg" alt="Team celebrating product launch">

<!-- ✅ Decorative (empty alt) -->
<img src="decorative-line.svg" alt="">
```

### Missing Form Labels
```html
<!-- ❌ Bad -->
<input type="email" placeholder="Email">

<!-- ✅ Good -->
<label for="email">Email address</label>
<input type="email" id="email">

<!-- ✅ Also good (visually hidden label) -->
<label for="search" class="sr-only">Search</label>
<input type="search" id="search" placeholder="Search...">
```

### Poor Color Contrast
```css
/* ❌ Bad: 2.5:1 ratio */
.light-text {
  color: #999;
  background: #fff;
}

/* ✅ Good: 4.6:1 ratio */
.accessible-text {
  color: #666;
  background: #fff;
}
```

### Missing Focus Indicators
```css
/* ❌ Bad: Removes focus indicator */
button:focus {
  outline: none;
}

/* ✅ Good: Custom focus indicator */
button:focus {
  outline: 2px solid #005fcc;
  outline-offset: 2px;
}

/* ✅ Also good: Focus-visible for keyboard only */
button:focus-visible {
  outline: 2px solid #005fcc;
  outline-offset: 2px;
}
```

### Missing Skip Link
```html
<!-- ✅ Add at top of page -->
<a href="#main-content" class="skip-link">
  Skip to main content
</a>

<!-- Style to show on focus -->
<style>
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  padding: 8px;
  background: #000;
  color: #fff;
  z-index: 100;
}
.skip-link:focus {
  top: 0;
}
</style>
```

---

## Testing Tools

| Tool | Purpose | URL |
|------|---------|-----|
| **axe DevTools** | Browser extension | devtools.deque.com |
| **WAVE** | Visual feedback | wave.webaim.org |
| **Lighthouse** | Built into Chrome | DevTools > Lighthouse |
| **Color Contrast Checker** | Contrast ratios | webaim.org/resources/contrastchecker |
| **NVDA** | Free screen reader | nvaccess.org |
| **VoiceOver** | Mac screen reader | Built into macOS |

---

## Report Format

### Accessibility Audit: `a11y-audit-[YYYY-MM-DD].md`

```markdown
# Accessibility Audit

## Summary
- **Pages Reviewed**: [Count]
- **WCAG Level**: AA
- **Issues Found**: [Critical: X, High: X, Medium: X, Low: X]

## Findings

### 🔴 Critical (Blocks Access)
| Issue | Location | WCAG | Fix |
|-------|----------|------|-----|

### 🟠 High (Significant Barrier)
| Issue | Location | WCAG | Fix |
|-------|----------|------|-----|

### 🟡 Medium (Usability Impact)
| Issue | Location | WCAG | Fix |
|-------|----------|------|-----|

### 🟢 Low (Enhancement)
| Issue | Location | WCAG | Fix |
|-------|----------|------|-----|

## Recommendations
1. [Priority fix 1]
2. [Priority fix 2]

## Testing Performed
- [ ] Keyboard navigation
- [ ] Screen reader (NVDA/VoiceOver)
- [ ] Color contrast
- [ ] Zoom to 200%
- [ ] axe DevTools scan
```

---

## Severity Guide

| Level | Icon | Impact | Examples |
|-------|------|--------|----------|
| **Critical** | 🔴 | Blocks access completely | Keyboard trap, no form labels |
| **High** | 🟠 | Significant barrier | Missing alt text, no focus indicator |
| **Medium** | 🟡 | Causes difficulty | Poor heading structure, low contrast |
| **Low** | 🟢 | Minor inconvenience | Missing skip link, verbose alt |

---

## Quick Wins Checklist

- [ ] Add `lang` attribute to `<html>`
- [ ] All images have `alt` attributes
- [ ] All form inputs have `<label>` elements
- [ ] Color contrast meets 4.5:1
- [ ] Focus indicators visible
- [ ] Heading levels don't skip (h1 → h2 → h3)
- [ ] Links have meaningful text
- [ ] Skip link to main content
- [ ] No `tabindex` greater than 0

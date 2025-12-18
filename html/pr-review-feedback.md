# HTML/CSS PR Review — Code Change Feedback

> **Purpose**: Review frontend code changes in pull requests  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: HTML, CSS, JavaScript changes  
> **Last Updated**: 2025-12

---

## Mission

Provide **practical code review feedback** for HTML, CSS, and frontend changes. Catch bugs, accessibility issues, and ensure good user experience before merge.

---

## Guard Clauses

**If no diff provided:**
```
NO_DIFF_PROVIDED

Please provide the PR changes to review:
- Run: git diff main...HEAD
- Or paste the changed code
- Include file paths for context
```

**If changes look good:**
```
LGTM

✅ **Approved to Merge**

Frontend review complete:
- Accessibility: No issues ✓
- Semantic HTML: Correct ✓
- CSS quality: Clean ✓
- Performance: No concerns ✓
- Mobile: Responsive ✓

Ship it! 🚀
```

---

## Quick Context Checklist

```
☐ PR diff (git diff main...HEAD)
☐ Changed files list
☐ PR description/intent
☐ Screenshots (if visual changes)
```

---

## Copy-Paste Review Prompts

### Prompt: Full Frontend Review
```text
Review this frontend PR:

{{DIFF}}

Check:
1. 🔴 Accessibility issues (missing alt, labels, contrast)
2. 🟠 Semantic HTML problems
3. 🟡 CSS quality (BEM, specificity, organization)
4. 🟢 Performance (images, loading)
5. Mobile responsiveness

For each issue:
- Location (file:line)
- Severity
- Fix suggestion

Use GitHub suggestion blocks.
```

### Prompt: Accessibility Review
```text
Review accessibility in this PR:

{{DIFF}}

Check:
1. Images have alt text
2. Forms have labels
3. Keyboard navigation works
4. Color contrast sufficient
5. ARIA used correctly

Flag all violations with WCAG criterion.
```

### Prompt: CSS Review
```text
Review CSS changes in this PR:

{{DIFF}}

Check:
1. BEM naming followed
2. No !important abuse
3. Specificity reasonable
4. No duplicate styles
5. Responsive patterns correct

Suggest improvements for maintainability.
```

### Prompt: Quick Review
```text
Quick review this frontend PR:

{{DIFF}}

Only flag:
- Broken functionality
- Accessibility violations
- Performance issues
- Mobile breakage

Skip minor style issues. Be concise.
```

### Prompt: Generate PR Description
```text
Generate a PR description for these frontend changes:

{{DIFF}}

Include:
1. What changed (visual and code)
2. Why (user impact)
3. Testing done
4. Screenshots needed
5. Accessibility considerations
```

---

## Review Checklist

### HTML Changes
- [ ] Semantic elements used correctly
- [ ] Heading hierarchy maintained
- [ ] Images have alt text
- [ ] Forms have labels
- [ ] Links have meaningful text
- [ ] No accessibility regressions

### CSS Changes
- [ ] BEM naming convention followed
- [ ] No !important (or justified)
- [ ] Specificity reasonable
- [ ] Mobile styles included
- [ ] No hardcoded values (use variables)
- [ ] No duplicate styles

### JavaScript Changes (if any)
- [ ] No errors in console
- [ ] Keyboard events handled
- [ ] Focus management correct
- [ ] No performance issues
- [ ] Progressive enhancement

### Visual Changes
- [ ] Matches design spec
- [ ] Works on mobile
- [ ] Works in all browsers
- [ ] Animations smooth
- [ ] Loading states present

---

## Common Issues to Catch

### Accessibility
```html
<!-- ❌ Missing alt -->
<img src="hero.jpg">

<!-- ✅ Fixed -->
<img src="hero.jpg" alt="Product showcase">

<!-- ❌ Missing label -->
<input type="email" placeholder="Email">

<!-- ✅ Fixed -->
<label for="email">Email</label>
<input type="email" id="email">
```

### Semantic HTML
```html
<!-- ❌ Div soup -->
<div class="header">
  <div class="nav">...</div>
</div>

<!-- ✅ Semantic -->
<header>
  <nav>...</nav>
</header>
```

### CSS Organization
```css
/* ❌ Bad specificity */
div.container > ul.nav > li.active > a {}

/* ✅ BEM class */
.nav__link--active {}

/* ❌ Magic numbers */
.card { margin: 13px 27px; }

/* ✅ Variables */
.card { margin: var(--spacing-sm) var(--spacing-lg); }
```

### Performance
```html
<!-- ❌ Missing dimensions -->
<img src="photo.jpg">

<!-- ✅ With dimensions -->
<img src="photo.jpg" width="800" height="600" loading="lazy">
```

---

## Feedback Format

### GitHub Suggestion Block
````markdown
**🟠 High: Missing form label**

This input needs a label for accessibility:

```suggestion
<label for="search">Search</label>
<input type="search" id="search" placeholder="Search...">
```

This helps screen reader users understand the input purpose.
````

### Inline Comment Format
```markdown
**🔴 Critical: Missing alt text**

File: `src/components/hero.html`, line 15

Images must have alt text for accessibility (WCAG 1.1.1).

Suggested fix:
- Add descriptive alt: `alt="Team collaborating in modern office"`
- Or mark as decorative: `alt=""`
```

---

## Report Format

### PR Review: `pr-review-[branch]-[YYYY-MM-DD].md`

```markdown
# PR Review: [Branch Name]

## Summary
- **Files Changed**: [Count]
- **Lines Changed**: +[added] / -[removed]
- **Verdict**: Approved / Request Changes / Needs Discussion

## Accessibility
| Issue | File | Line | Fix |
|-------|------|------|-----|

## HTML Quality
| Issue | File | Line | Fix |
|-------|------|------|-----|

## CSS Quality
| Issue | File | Line | Fix |
|-------|------|------|-----|

## Performance
| Issue | File | Line | Fix |
|-------|------|------|-----|

## What's Good
- [Positive observation 1]
- [Positive observation 2]

## Questions
- [Clarification needed]
```

---

## Severity Guide

| Level | Icon | Action | Examples |
|-------|------|--------|----------|
| **Critical** | 🔴 | Block merge | Missing labels, broken layout |
| **High** | 🟠 | Should fix | Missing alt text, poor contrast |
| **Medium** | 🟡 | Consider | BEM naming, CSS organization |
| **Low** | 🟢 | Optional | Minor improvements |

---

## Review Tips

1. **Check accessibility first**: It's easy to miss and hard to fix later
2. **Test on mobile**: Many issues only appear on small screens
3. **Look at the design**: Does the code match intent?
4. **Consider performance**: Large images, blocking resources?
5. **Be constructive**: Suggest fixes, not just problems
6. **Acknowledge good work**: Positive feedback matters

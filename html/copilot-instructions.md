# HTML/CSS Copilot Instructions — AI Configuration

> **Purpose**: Configure AI assistants for HTML/CSS development  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Frontend web development  
> **Last Updated**: 2026-03

---

> **Legacy Path Notice**: `html/` is maintained for backward compatibility. For stack-first guidance, also use [frontend/agents.md](../frontend/agents.md). 
> **Migration Map**: [docs/compat/html-to-frontend-map.md](../docs/compat/html-to-frontend-map.md)

## Mission

Configure AI assistants to provide **consistent, high-quality help** with HTML/CSS development. Focus on accessibility, semantic markup, performance, and maintainable code.

---

## Quick Context Checklist

```
☐ Project type (static site, SPA, CMS)
☐ CSS methodology (BEM, Tailwind, CSS Modules)
☐ Framework (vanilla, React, Vue, Svelte)
☐ Browser support requirements
☐ Accessibility requirements (WCAG level)
```

---

## Copy-Paste Configuration Prompts

### Prompt: Set Up Frontend Assistant
```text
Configure yourself as an HTML/CSS assistant for this project:

Project: {{PROJECT_TYPE}}
CSS Approach: {{BEM / TAILWIND / CSS_MODULES}}
Framework: {{VANILLA / REACT / VUE}}
Browsers: {{MODERN / IE11+ / SPECIFIC}}

Priorities:
1. Accessibility (WCAG 2.1 AA)
2. Semantic HTML
3. Performance
4. Maintainability

When I share code, automatically check for these issues.
```

### Prompt: Code Review Mode
```text
Act as a frontend code reviewer. For any HTML/CSS I share:

1. Check accessibility (alt text, labels, contrast, keyboard)
2. Verify semantic HTML usage
3. Review CSS organization and specificity
4. Identify performance issues
5. Suggest improvements

Use this format:
- 🔴 Critical: [Must fix]
- 🟠 High: [Should fix]
- 🟡 Medium: [Consider]
- 🟢 Low: [Nice to have]
```

### Prompt: Learning Mode
```text
I'm learning HTML/CSS. When you help me:

1. Explain why, not just what
2. Show both wrong and right approaches
3. Link to relevant documentation
4. Suggest related topics to explore
5. Keep examples simple and focused

Start with fundamentals, add complexity gradually.
```

### Prompt: Component Builder Mode
```text
Act as a frontend component architect. When building components:

1. Use semantic HTML first
2. Apply BEM naming convention
3. Make accessible by default
4. Design mobile-first
5. Include all common variants
6. Document usage

Template:
- HTML structure
- CSS (with custom properties)
- Accessibility features
- Usage examples
```

### Prompt: Quick Fix Mode
```text
I need quick fixes, not explanations. When I share code:

1. Identify the issue immediately
2. Provide the corrected code
3. One-line explanation only
4. No alternatives unless asked

Format: Problem → Fix → Done
```

---

## Project-Level Instructions

### For .github/copilot-instructions.md

```markdown
# HTML/CSS Project Instructions

## Tech Stack
- HTML5 semantic markup
- CSS3 with custom properties
- BEM naming convention
- Mobile-first responsive design

## Coding Standards

### HTML
- Use semantic elements: header, nav, main, section, article, footer
- Every img must have alt attribute
- Every form input must have associated label
- Use button for actions, a for navigation
- One h1 per page, logical heading hierarchy

### CSS
- BEM naming: .block__element--modifier
- CSS custom properties for colors, spacing, typography
- Mobile-first media queries
- No !important except utilities
- Max selector specificity: 3 levels

### Accessibility
- WCAG 2.1 AA compliance required
- All interactive elements keyboard accessible
- Color contrast minimum 4.5:1 for text
- Focus indicators must be visible
- No keyboard traps

### Performance
- Images must have width/height attributes
- Lazy load images below the fold
- Critical CSS inlined
- No render-blocking resources

## File Structure
\`\`\`
src/
├── index.html
├── css/
│   ├── main.css
│   ├── components/
│   └── utilities/
├── js/
└── images/
\`\`\`

## Response Format
When reviewing code, use severity levels:
- 🔴 Critical: Blocks functionality or accessibility
- 🟠 High: Should be fixed before merge
- 🟡 Medium: Improve when possible
- 🟢 Low: Nice to have
```

---

## Context-Specific Behaviors

### When Creating HTML
```
✅ DO:
- Start with semantic structure
- Add accessibility attributes
- Use descriptive class names
- Include required attributes (alt, for, type)

❌ DON'T:
- Use div when semantic element exists
- Skip alt text on images
- Use inline styles
- Create deeply nested structures
```

### When Writing CSS
```
✅ DO:
- Use BEM naming convention
- Define custom properties for repeated values
- Write mobile-first media queries
- Group related properties

❌ DON'T:
- Use ID selectors for styling
- Use !important (except utilities)
- Nest more than 3 levels
- Use magic numbers
```

### When Reviewing Code
```
✅ DO:
- Check accessibility first
- Verify semantic HTML usage
- Look for performance issues
- Suggest specific fixes

❌ DON'T:
- Approve without checking a11y
- Ignore browser compatibility
- Skip mobile responsiveness check
- Overlook missing attributes
```

---

## Framework-Specific Settings

### React/JSX
```markdown
## React HTML/CSS Guidelines
- Use className instead of class
- Use htmlFor instead of for
- Prefer CSS Modules or styled-components
- Extract components at 50+ lines
- Use Fragment to avoid wrapper divs
```

### Vue
```markdown
## Vue HTML/CSS Guidelines
- Use scoped styles by default
- Prefer class binding for dynamic styles
- Use BEM within components
- Leverage CSS custom properties for theming
```

### Tailwind CSS
```markdown
## Tailwind Guidelines
- Extract components for repeated patterns
- Use @apply sparingly
- Extend theme for project colors
- Group related utilities with comments
- Use arbitrary values sparingly
```

---

## Response Templates

### For Code Review
```markdown
## HTML/CSS Review

### Summary
- Files: [count]
- Issues: [🔴 X] [🟠 X] [🟡 X] [🟢 X]

### Critical Issues
[List or "None found"]

### Recommendations
1. [Top priority]
2. [Second priority]
3. [Third priority]

### What's Good
- [Positive observation]
```

### For Component Creation
```markdown
## Component: [Name]

### HTML
\`\`\`html
[semantic structure]
\`\`\`

### CSS
\`\`\`css
[BEM styles with custom properties]
\`\`\`

### Accessibility
- [Feature 1]
- [Feature 2]

### Usage
\`\`\`html
[example]
\`\`\`
```

---

## Severity Guide

| Level | Icon | When to Use |
|-------|------|-------------|
| **Critical** | 🔴 | Accessibility failure, broken functionality |
| **High** | 🟠 | Major UX issue, should fix before deploy |
| **Medium** | 🟡 | Code quality, maintainability concern |
| **Low** | 🟢 | Enhancement, nice to have |

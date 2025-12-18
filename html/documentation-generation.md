# HTML/CSS Documentation — Frontend Docs Generator

> **Purpose**: Create clear documentation for frontend projects  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: HTML, CSS, Components, Style Guides  
> **Last Updated**: 2025-12

---

## Mission

Help create **clear, useful documentation** for HTML, CSS, and frontend projects. Make it easy for anyone to understand and use your code.

---

## Guard Clauses

**If no code provided:**
```
NO_CODE_PROVIDED

Please provide code to document:
- Component HTML/CSS
- Style guide sections
- Project structure

I'll generate appropriate documentation.
```

**If already well-documented:**
```
DOCUMENTATION_COMPLETE

✅ **Documentation Looks Good**

Existing docs cover:
- Purpose and usage ✓
- Code examples ✓
- Variants/options ✓
- Accessibility notes ✓

Suggestions for improvement (if any):
[LIST ENHANCEMENTS]
```

---

## Quick Context Checklist

```
☐ Code/components to document
☐ Target audience (devs, designers, both)
☐ Existing documentation style
☐ Level of detail needed
```

---

## Copy-Paste Documentation Prompts

### Prompt: Generate README
```text
Generate a README for this frontend project:

Project: {{NAME}}
Purpose: {{DESCRIPTION}}
Stack: HTML, CSS, {{OTHER}}

Include:
1. Project overview
2. Quick start / installation
3. File structure
4. Usage examples
5. Browser support
6. Contributing guidelines
```

### Prompt: Document Component
```text
Document this component:

{{CODE}}

Include:
1. Component name and purpose
2. When to use / when not to use
3. HTML structure explanation
4. CSS classes table
5. Variants and modifiers
6. Accessibility features
7. Usage examples
```

### Prompt: Create Style Guide
```text
Create a style guide section for:

{{TOPIC}} (colors / typography / spacing / components)

Include:
1. Design tokens/values
2. Usage guidelines
3. Do's and don'ts
4. Code examples
5. Visual examples (described)
```

### Prompt: Document CSS Utilities
```text
Document these CSS utility classes:

{{CSS}}

For each utility:
1. Class name
2. What it does
3. When to use
4. Example usage

Format as a reference table.
```

### Prompt: Migration Guide
```text
Create a migration guide for:

Old approach: {{OLD}}
New approach: {{NEW}}

Include:
1. What's changing
2. Step-by-step migration
3. Before/after examples
4. Common issues and solutions
5. Breaking changes
```

---

## README Template

```markdown
# Project Name

Brief description of what this project does.

## Quick Start

\`\`\`bash
# Clone and open
git clone https://github.com/user/project.git
cd project

# Open in browser (or use local server)
open index.html
\`\`\`

## Project Structure

\`\`\`
project/
├── index.html          # Main HTML file
├── css/
│   ├── main.css        # Main styles
│   ├── components/     # Component styles
│   └── utilities/      # Utility classes
├── js/
│   └── main.js         # JavaScript
└── images/             # Image assets
\`\`\`

## Components

| Component | File | Description |
|-----------|------|-------------|
| Card | css/components/card.css | Content cards |
| Button | css/components/button.css | Action buttons |
| Nav | css/components/nav.css | Navigation |

## Browser Support

- Chrome (last 2 versions)
- Firefox (last 2 versions)
- Safari (last 2 versions)
- Edge (last 2 versions)

## Development

### Prerequisites
- Modern web browser
- Local server (optional): \`npx serve\`

### CSS Naming
We use BEM naming convention:
- Block: \`.component\`
- Element: \`.component__element\`
- Modifier: \`.component--modifier\`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT
```

---

## Component Documentation Template

```markdown
# Component Name

Brief description of what this component does.

## When to Use

✅ **Use this component when:**
- [Use case 1]
- [Use case 2]

❌ **Don't use this component when:**
- [Anti-pattern 1]
- [Anti-pattern 2]

## Structure

\`\`\`html
<div class="component">
  <div class="component__header">Header</div>
  <div class="component__body">Body</div>
  <div class="component__footer">Footer</div>
</div>
\`\`\`

## CSS Classes

| Class | Description |
|-------|-------------|
| \`.component\` | Base component styles |
| \`.component__header\` | Header section |
| \`.component__body\` | Main content area |
| \`.component__footer\` | Footer section |

## Modifiers

| Modifier | Description | Example |
|----------|-------------|---------|
| \`--small\` | Compact size | \`.component--small\` |
| \`--large\` | Expanded size | \`.component--large\` |
| \`--primary\` | Primary color | \`.component--primary\` |

## Examples

### Basic Usage
\`\`\`html
<div class="component">
  <div class="component__body">Basic content</div>
</div>
\`\`\`

### With Modifier
\`\`\`html
<div class="component component--primary">
  <div class="component__body">Primary variant</div>
</div>
\`\`\`

## Accessibility

- Uses semantic HTML elements
- Keyboard navigable
- Screen reader friendly
- Color contrast compliant

## Related Components

- [Related Component 1](link)
- [Related Component 2](link)
```

---

## Style Guide Section Templates

### Colors
```markdown
## Colors

### Brand Colors
| Name | Variable | Value | Usage |
|------|----------|-------|-------|
| Primary | \`--color-primary\` | #0066cc | Main actions, links |
| Secondary | \`--color-secondary\` | #6c757d | Secondary actions |

### Semantic Colors
| Name | Variable | Value | Usage |
|------|----------|-------|-------|
| Success | \`--color-success\` | #28a745 | Success states |
| Warning | \`--color-warning\` | #ffc107 | Warning states |
| Danger | \`--color-danger\` | #dc3545 | Error states |

### Usage Guidelines
- Use primary color for main CTAs
- Use semantic colors consistently for their purpose
- Ensure 4.5:1 contrast ratio for text
```

### Typography
```markdown
## Typography

### Font Families
| Name | Variable | Value |
|------|----------|-------|
| Body | \`--font-body\` | system-ui, sans-serif |
| Heading | \`--font-heading\` | system-ui, sans-serif |
| Mono | \`--font-mono\` | monospace |

### Font Sizes
| Name | Variable | Size | Usage |
|------|----------|------|-------|
| XS | \`--font-size-xs\` | 0.75rem | Captions |
| SM | \`--font-size-sm\` | 0.875rem | Small text |
| MD | \`--font-size-md\` | 1rem | Body text |
| LG | \`--font-size-lg\` | 1.25rem | Lead text |
| XL | \`--font-size-xl\` | 1.5rem | H3 |
| 2XL | \`--font-size-2xl\` | 2rem | H2 |
| 3XL | \`--font-size-3xl\` | 2.5rem | H1 |
```

### Spacing
```markdown
## Spacing

### Spacing Scale
| Name | Variable | Value | Pixels |
|------|----------|-------|--------|
| XS | \`--spacing-xs\` | 0.25rem | 4px |
| SM | \`--spacing-sm\` | 0.5rem | 8px |
| MD | \`--spacing-md\` | 1rem | 16px |
| LG | \`--spacing-lg\` | 1.5rem | 24px |
| XL | \`--spacing-xl\` | 2rem | 32px |
| 2XL | \`--spacing-2xl\` | 3rem | 48px |

### Usage
- Use spacing scale consistently
- Prefer \`gap\` for flexbox/grid spacing
- Use margin for component separation
- Use padding for internal spacing
```

---

## Inline Documentation

### HTML Comments
```html
<!-- 
  Component: Card
  Purpose: Display content in a contained card format
  Variants: --featured, --compact
  
  Usage:
  <article class="card card--featured">
    <div class="card__content">...</div>
  </article>
-->
```

### CSS Comments
```css
/* ==========================================================================
   Component: Card
   
   A versatile card component for displaying content.
   
   Markup:
   <article class="card">
     <img class="card__image" src="..." alt="...">
     <div class="card__content">...</div>
   </article>
   
   Modifiers:
   .card--featured - Highlighted card with border
   .card--compact - Reduced padding
   ========================================================================== */
```

---

## Report Format

### Documentation Review: `docs-review-[YYYY-MM-DD].md`

```markdown
# Documentation Review

## Summary
- **Files Reviewed**: [Count]
- **Coverage**: [Percentage]
- **Quality**: [Good/Needs Work/Poor]

## Findings

### Missing Documentation
| Item | Type | Priority |
|------|------|----------|

### Incomplete Documentation
| Item | Missing | Priority |
|------|---------|----------|

### Outdated Documentation
| Item | Issue | Priority |
|------|-------|----------|

## Recommendations
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]
```

---

## Severity Guide

| Level | Icon | When to Use |
|-------|------|-------------|
| **Critical** | 🔴 | Missing docs for public API |
| **High** | 🟠 | Incomplete component docs |
| **Medium** | 🟡 | Missing examples |
| **Low** | 🟢 | Could be clearer |

# BEM Naming Convention

You are a CSS architecture specialist with expertise in BEM (Block-Element-Modifier) methodology and scalable CSS design systems. Transform the following HTML to follow strict BEM naming conventions for maintainable, modular stylesheets.

**BEM Methodology Standards:**
1. **Block**: Independent, reusable component (`.card`, `.button`, `.navigation`)
2. **Element**: Part of a block that has no meaning outside of it (`.card__title`, `.button__icon`)
3. **Modifier**: Variation of a block or element (`.button--large`, `.card--featured`)
4. **Naming Rules**: Use double underscores `__` for elements, double hyphens `--` for modifiers
5. **Independence**: Each block should be independent and reusable
6. **Flat Structure**: Avoid deep nesting in class names

**BEM Transformation Process:**
- **Identify blocks**: Independent UI components
- **Define elements**: Child components within blocks  
- **Create modifiers**: Variations and states
- **Establish relationships**: Proper parent-child associations
- **Ensure consistency**: Follow naming patterns throughout
- **Document patterns**: Explain the BEM structure created

**Report Format:**
Generate a comprehensive BEM methodology analysis and implementation report:

```markdown
# BEM Naming Convention Analysis Report

## 📋 BEM Assessment Summary
- **Files Analyzed**: [Number of HTML/template files]
- **Current Naming Convention**: [BEM/Custom/Mixed/None]
- **CSS Classes Found**: [Total count]
- **BEM Compliance Score**: [Percentage]
- **Refactoring Complexity**: [Low/Medium/High]
- **Estimated Effort**: [Hours/days]

## 🔍 Current CSS Architecture Analysis

### Existing Class Structure
- **Non-BEM Classes**: [Count and examples]
- **Partial BEM Implementation**: [Classes that partially follow BEM]
- **Component Boundaries**: [Identified UI components]
- **Naming Inconsistencies**: [Mixed patterns found]

### Component Analysis
1. **Card Component**
   - **Current Classes**: `.featured-card`, `.card-title`, `.card-content`
   - **Issues**: Mixed naming conventions, unclear hierarchy
   - **Component Boundary**: Clear card container with header, body, footer
   - **Complexity**: Medium (nested elements with variations)

2. **Button Component**
   - **Current Classes**: `.btn`, `.btn-primary`, `.small-btn`
   - **Issues**: Inconsistent modifier patterns
   - **Component Boundary**: Button with icon and text elements
   - **Variations**: Size, color, state modifiers needed

## 📝 Proposed BEM Structure

### Block-Element-Modifier Mapping

#### Card Component Transformation
```html
<!-- Before (non-BEM) -->
<div class="featured-card large">
  <div class="card-header">
    <h2 class="card-title">Title</h2>
    <span class="subtitle muted">Subtitle</span>
  </div>
  <div class="card-content">Content</div>
</div>

<!-- After (BEM-compliant) -->
<div class="card card--featured card--large">
  <header class="card__header">
    <h2 class="card__title">Title</h2>
    <span class="card__subtitle card__subtitle--muted">Subtitle</span>
  </header>
  <div class="card__body">Content</div>
</div>
```

#### Button Component Transformation
```html
<!-- Before (non-BEM) -->
<button class="btn btn-primary small">
  <span class="btn-text">Click me</span>
  <i class="icon icon-arrow">→</i>
</button>

<!-- After (BEM-compliant) -->
<button class="button button--primary button--small">
  <span class="button__text">Click me</span>
  <span class="button__icon button__icon--right">→</span>
</button>
```

## 🎯 CSS Architecture Benefits

### Improved Organization
- **Flat Specificity**: No CSS specificity wars
- **Component Isolation**: Each block is independent
- **Scalable Structure**: Easy to add new components
- **Team Collaboration**: Clear naming conventions

### SCSS Structure Recommendation
```scss
// Component-based organization
.card {
  // Block styles
  
  &__header {
    // Element styles
  }
  
  &__title {
    // Element styles
  }
  
  &--featured {
    // Modifier styles
  }
}
```

## 📋 Implementation Action Plan

### Phase 1: Component Identification (High Priority)
1. [ ] **Map existing components** to BEM blocks
2. [ ] **Identify reusable elements** within each block
3. [ ] **Catalog modifiers** for each component
4. [ ] **Document component boundaries** and relationships

### Phase 2: Class Transformation (Medium Priority)
1. [ ] **Update HTML classes** following BEM conventions
2. [ ] **Refactor CSS selectors** to match new class names
3. [ ] **Test visual consistency** after class changes
4. [ ] **Update JavaScript selectors** if applicable

### Phase 3: Documentation & Standards (Low Priority)
1. [ ] **Create BEM style guide** for the project
2. [ ] **Document component library** with examples
3. [ ] **Set up linting rules** for BEM compliance
4. [ ] **Train team members** on BEM methodology

## 🛠️ Technical Considerations

### CSS Refactoring Impact
- **Selector Changes**: [List all selectors requiring updates]
- **Specificity Changes**: [Impact on CSS cascade]
- **File Organization**: [Recommended SCSS structure]

### Framework Integration
- **CSS Modules**: Compatible with BEM for scoped styles
- **Styled Components**: BEM classes can coexist
- **Utility Classes**: Combine with utility-first approaches

## 📊 Migration Checklist
- [ ] **Backup current CSS** before making changes
- [ ] **Create component inventory** with current and proposed names
- [ ] **Update HTML templates** with new BEM classes
- [ ] **Refactor CSS files** to use new selectors
- [ ] **Test all components** for visual regression
- [ ] **Update documentation** with new class conventions
```

**BEM Conversion Scope:**
- **Current Selection**: Apply BEM methodology to the currently selected HTML elements
- **Current File**: Transform all CSS classes in the active HTML/template file
- **Component Focus**: Convert the HTML component containing the cursor
- **Workspace CSS**: Reference linked stylesheets for existing class usage patterns

**IDE Integration:**
- Auto-detect existing CSS/SCSS files in the workspace for class mapping
- Preserve framework-specific class bindings (React className, Vue :class)
- Analyze existing CSS architecture to maintain consistency
- Reference component structure to understand block relationships
- Use file naming conventions to infer component boundaries

**Smart BEM Application:**
- Compliance level: [Adapt to existing CSS methodology in the project]
- CSS generation: [Provide SCSS structure if .scss files are detected in workspace]
- Component hierarchy: [Auto-map based on HTML nesting and component files]
- Framework integration: [Maintain CSS-in-JS, styled-components, or CSS modules compatibility]
- Modifier patterns: [Generate variations based on existing class patterns in workspace]

**Interactive Follow-up:**
After generating the report, ask: "Would you like me to help implement the BEM transformation for the first component identified in the analysis?"

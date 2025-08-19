# Navigation Consistency Analysis

**Role**: You are a senior UX/UI developer specializing in web navigation design and user experience consistency.

**Task**: Analyze the navigation structure across multiple HTML pages in the current workspace to ensure consistency, accessibility, and optimal user experience.

**Context Analysis**: 
- Examine navigation elements across all HTML files in the workspace
- Identify navigation patterns, menus, breadcrumbs, and linking structures
- Analyze current file and related pages for navigation inconsistencies
- Consider mobile responsiveness and accessibility standards
- Evaluate user flow and information architecture

**Navigation Consistency Principles:**
1. **Structural Consistency**: Same navigation placement and hierarchy across pages
2. **Visual Consistency**: Consistent styling, colors, fonts, and spacing
3. **Functional Consistency**: Identical behavior and interaction patterns  
4. **Content Consistency**: Same menu items, labels, and organizational structure
5. **Accessibility Consistency**: Uniform keyboard navigation, ARIA labels, and screen reader support
6. **Responsive Consistency**: Navigation adapts consistently across all device sizes

**Report Format:**
Generate a comprehensive navigation consistency analysis and standardization report:

```markdown
# Navigation Consistency Analysis Report

## 📋 Navigation Overview
- **Pages Analyzed**: [Count of HTML files in workspace]
- **Navigation Types Found**: [Primary nav, secondary nav, breadcrumbs, footer nav]
- **Consistency Score**: [X% consistent across pages]
- **Framework Detected**: [Bootstrap, Tailwind, custom CSS, etc.]
- **Mobile Navigation**: [Present/Missing/Inconsistent]
- **Accessibility Compliance**: [WCAG level assessment]

## 🔍 Current Navigation Analysis

### Navigation Structure Inventory
1. **Primary Navigation**
   - **Location**: [Header, sidebar, top bar]
   - **Items**: [List of menu items found]
   - **Hierarchy**: [Flat/Multi-level/Mega menu]
   - **Consistency**: [✅ Consistent / ⚠️ Minor variations / ❌ Major inconsistencies]

2. **Secondary Navigation**
   - **Type**: [Tabs, sidebar menu, contextual links]
   - **Context**: [Section-specific/Page-specific]
   - **Placement**: [Below header, in content area, sidebar]

3. **Breadcrumb Navigation**
   - **Present On**: [X of Y pages]
   - **Format**: [Home > Category > Page / Category > Page]
   - **Schema Markup**: [Present/Missing]

### Page-by-Page Breakdown
1. **index.html**
   - **Nav Items**: [Home, About, Services, Contact]
   - **Active State**: [CSS class for current page]
   - **Mobile Menu**: [Hamburger icon, slide-out drawer]
   - **Issues**: [Missing active state on Home link]

2. **about.html**
   - **Nav Items**: [Same as index but missing Services]
   - **Active State**: [Not implemented]
   - **Mobile Menu**: [Different implementation]
   - **Issues**: [Inconsistent menu structure, broken mobile nav]

## ⚠️ Consistency Issues Identified

### Critical Inconsistencies
1. **Menu Item Variations**
   - **Issue**: Different pages show different menu items
   - **Pages Affected**: about.html, contact.html
   - **Impact**: User confusion, broken user experience
   - **Solution**: Standardize menu items across all pages
   - **Priority**: High

2. **Active State Implementation**
   - **Issue**: Current page highlighting inconsistent or missing
   - **Pages Affected**: 4 out of 6 pages
   - **Impact**: Users can't identify their current location
   - **Solution**: Implement consistent active state CSS
   - **Priority**: High

### Accessibility Issues
1. **Missing ARIA Labels**
   - **Issue**: Navigation lacks screen reader support
   - **Elements**: Mobile menu toggle, dropdown menus
   - **WCAG Impact**: Level A compliance failure
   - **Solution**: Add proper ARIA attributes

2. **Keyboard Navigation**
   - **Issue**: Dropdown menus not keyboard accessible
   - **Impact**: Users with disabilities cannot navigate
   - **Solution**: Implement focus management and keyboard controls

## 🎯 Standardization Recommendations

### Unified Navigation Structure
```html
<!-- Recommended navigation template -->
<nav class="primary-navigation" role="navigation" aria-label="Main navigation">
  <div class="nav-container">
    <a href="/" class="nav-logo" aria-label="Company homepage">
      <img src="logo.svg" alt="Company Name">
    </a>
    
    <ul class="nav-menu" id="nav-menu">
      <li class="nav-item">
        <a href="/" class="nav-link" aria-current="page">Home</a>
      </li>
      <li class="nav-item">
        <a href="/about" class="nav-link">About</a>
      </li>
      <li class="nav-item dropdown">
        <a href="/services" class="nav-link dropdown-toggle" 
           aria-expanded="false" aria-haspopup="true">
          Services
        </a>
        <ul class="dropdown-menu" role="menu">
          <li><a href="/services/web-design" role="menuitem">Web Design</a></li>
          <li><a href="/services/development" role="menuitem">Development</a></li>
        </ul>
      </li>
      <li class="nav-item">
        <a href="/contact" class="nav-link">Contact</a>
      </li>
    </ul>
    
    <button class="mobile-menu-toggle" aria-controls="nav-menu" 
            aria-expanded="false" aria-label="Toggle navigation menu">
      <span class="hamburger-line"></span>
      <span class="hamburger-line"></span>
      <span class="hamburger-line"></span>
    </button>
  </div>
</nav>
```

### CSS Standardization Guidelines
```css
/* Navigation consistency standards */
.primary-navigation {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--nav-bg-color);
  border-bottom: 1px solid var(--nav-border-color);
}

.nav-link {
  color: var(--nav-text-color);
  text-decoration: none;
  padding: 1rem;
  transition: color 0.3s ease;
}

.nav-link:hover,
.nav-link:focus {
  color: var(--nav-hover-color);
  outline: 2px solid var(--focus-color);
}

.nav-link[aria-current="page"] {
  color: var(--nav-active-color);
  font-weight: 600;
}
```

## 📋 Implementation Action Plan

### Phase 1: Structure Standardization (High Priority)
1. [ ] **Create navigation template**
   - Design unified HTML structure
   - Define consistent menu items
   - Implement across all pages
   - **Estimated Time**: 2-3 hours

2. [ ] **Implement active state logic**
   - Add JavaScript for current page detection
   - Apply consistent active state styling
   - Test across all pages
   - **Estimated Time**: 1 hour

### Phase 2: Accessibility Enhancement (High Priority)
1. [ ] **Add ARIA attributes**
   - Implement proper navigation labels
   - Add dropdown menu accessibility
   - Include keyboard navigation support
   - **Estimated Time**: 1-2 hours

2. [ ] **Test accessibility compliance**
   - Screen reader testing
   - Keyboard-only navigation testing
   - WCAG compliance validation
   - **Estimated Time**: 30 minutes

### Phase 3: Mobile Optimization (Medium Priority)
1. [ ] **Standardize mobile navigation**
   - Implement consistent hamburger menu
   - Ensure touch-friendly interactions
   - Test across device sizes
   - **Estimated Time**: 2 hours

2. [ ] **Performance optimization**
   - Minimize navigation-related CSS/JS
   - Implement lazy loading for large menus
   - Optimize for Core Web Vitals
   - **Estimated Time**: 1 hour

## 🛠️ Technical Implementation

### JavaScript for Active States
```javascript
// Auto-highlight current page in navigation
document.addEventListener('DOMContentLoaded', function() {
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.nav-link');
  
  navLinks.forEach(link => {
    if (link.getAttribute('href') === currentPath) {
      link.setAttribute('aria-current', 'page');
      link.classList.add('active');
    }
  });
});
```

### Mobile Menu Toggle
```javascript
// Accessible mobile menu implementation
const mobileToggle = document.querySelector('.mobile-menu-toggle');
const navMenu = document.querySelector('#nav-menu');

mobileToggle.addEventListener('click', function() {
  const isExpanded = this.getAttribute('aria-expanded') === 'true';
  this.setAttribute('aria-expanded', !isExpanded);
  navMenu.classList.toggle('show');
});
```

## 📊 Success Metrics

### Before Standardization
- **Consistency Score**: 45%
- **Accessibility Score**: C (65%)
- **Mobile Experience**: Poor
- **User Confusion**: High

### Target After Implementation
- **Consistency Score**: 95%+
- **Accessibility Score**: AA (90%+)
- **Mobile Experience**: Excellent
- **User Navigation**: Intuitive and seamless
```

**Navigation Analysis Scope:**
- **Current File**: Analyze navigation in the active HTML file
- **Workspace Pages**: Compare navigation across all HTML files in project
- **Template Files**: Include partials, components, and layout files
- **Style Dependencies**: Reference CSS files for navigation styling patterns

**IDE Integration:**
- Auto-detect navigation patterns from existing HTML files
- Analyze CSS classes and JavaScript for navigation functionality
- Reference framework documentation (Bootstrap, Tailwind) if detected
- Identify template engines (Handlebars, Liquid) for dynamic navigation

**Smart Navigation Analysis:**
- Multi-page detection: [Scan workspace for HTML files to compare navigation structures]
- Framework integration: [Adapt recommendations based on CSS framework in use]
- CMS compatibility: [Account for WordPress, Jekyll, or other CMS navigation patterns]
- SEO considerations: [Include navigation structure impact on search engine crawling]
- Performance impact: [Analyze navigation JavaScript and CSS for optimization opportunities]

**Interactive Follow-up:**
After generating the report, ask: "Would you like me to help implement the unified navigation template for the first page identified with inconsistencies?"

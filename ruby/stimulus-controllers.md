# Stimulus Controllers — Modern Rails JavaScript

> **Purpose**: Production-ready Stimulus controller patterns and best practices  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: Controllers, targets, values, outlets, actions  
> **Last Updated**: 2026-01

---

## Mission

Help write **minimal, maintainable JavaScript** for Rails applications using Stimulus. Focus on proper controller design, DOM connections, and Hotwire integration.

---

## Guard Clauses

**If no Stimulus context provided:**
```
NO_STIMULUS_CONTEXT

Please provide context:
- Feature/interaction to implement
- Current HTML structure
- Related Turbo integration needs
- Or describe the JavaScript behavior needed

Include any existing controller code if refactoring.
```

**If Stimulus implementation is solid:**
```
STIMULUS_APPROVED

✅ Stimulus controller review complete — production ready.

Checks performed:
- Controller design: ✓ (single responsibility)
- Targets: ✓ (properly declared and used)
- Values: ✓ (typed, with defaults)
- Actions: ✓ (correct event handling)
- Memory: ✓ (cleanup on disconnect)

Implementation follows Stimulus best practices.
```

---

## Quick Context Checklist

```
☐ Stimulus version (3.x)
☐ Feature to implement
☐ HTML structure
☐ Events to handle
☐ State requirements
☐ Turbo integration needs
☐ Third-party library integration
☐ Animation requirements
```

---

## Copy-Paste Prompts

### Prompt: Create Stimulus Controller
```text
Create a Stimulus controller for:

Feature: {{FEATURE_DESCRIPTION}}
HTML structure: {{HTML}}

Requirements:
- Events: {{EVENTS_TO_HANDLE}}
- Targets needed: {{TARGETS}}
- State to track: {{STATE}}
- Turbo integration: {{YES_NO}}

Provide:
1. Complete controller code
2. Updated HTML with data attributes
3. Any CSS needed for states
4. Usage examples
```

### Prompt: Review Stimulus Controller
```text
Review this Stimulus controller:

{{CODE}}

HTML using it:
{{HTML}}

Check for:
1. **Controller Design**
   - Single responsibility
   - Naming conventions
   - File organization

2. **Targets**
   - Properly declared
   - Null checking
   - Optional vs required

3. **Values**
   - Type declarations
   - Default values
   - Change callbacks

4. **Actions**
   - Event selection
   - Parameter usage
   - Event options

5. **Lifecycle**
   - connect/disconnect
   - Memory cleanup
   - Event listener removal
```

### Prompt: Convert jQuery to Stimulus
```text
Convert this jQuery code to Stimulus:

{{JQUERY_CODE}}

HTML context:
{{HTML}}

Requirements:
- Maintain all functionality
- Proper Stimulus patterns
- Work with Turbo Drive
```

### Prompt: Implement Stimulus + Turbo Pattern
```text
Implement this interactive feature with Stimulus + Turbo:

Feature: {{DESCRIPTION}}
Server endpoint: {{ENDPOINT}}

Requirements:
- Stimulus for UI state
- Turbo Frames/Streams for updates
- Loading states
- Error handling

Provide controller, HTML, and any server code needed.
```

---

## Controller Basics

### Controller Structure

```javascript
// app/javascript/controllers/dropdown_controller.js
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  // Declare targets
  static targets = ["menu", "button"]
  
  // Declare values with types
  static values = {
    open: { type: Boolean, default: false },
    closeOnClickOutside: { type: Boolean, default: true }
  }
  
  // Declare CSS classes
  static classes = ["active", "hidden"]
  
  // Declare outlets (connections to other controllers)
  static outlets = ["popover"]
  
  // Lifecycle: when controller connects to DOM
  connect() {
    this.boundClickOutside = this.clickOutside.bind(this)
  }
  
  // Lifecycle: when controller disconnects
  disconnect() {
    document.removeEventListener("click", this.boundClickOutside)
  }
  
  // Actions
  toggle() {
    this.openValue = !this.openValue
  }
  
  open() {
    this.openValue = true
  }
  
  close() {
    this.openValue = false
  }
  
  // Value changed callback
  openValueChanged(value, previousValue) {
    if (value) {
      this.menuTarget.classList.remove(this.hiddenClass)
      this.buttonTarget.setAttribute("aria-expanded", "true")
      document.addEventListener("click", this.boundClickOutside)
    } else {
      this.menuTarget.classList.add(this.hiddenClass)
      this.buttonTarget.setAttribute("aria-expanded", "false")
      document.removeEventListener("click", this.boundClickOutside)
    }
  }
  
  // Private methods
  clickOutside(event) {
    if (this.closeOnClickOutsideValue && !this.element.contains(event.target)) {
      this.close()
    }
  }
}
```

### HTML Data Attributes

```html
<div data-controller="dropdown"
     data-dropdown-open-value="false"
     data-dropdown-close-on-click-outside-value="true"
     data-dropdown-active-class="is-active"
     data-dropdown-hidden-class="hidden">
  
  <button data-dropdown-target="button"
          data-action="click->dropdown#toggle"
          aria-expanded="false">
    Menu
  </button>
  
  <ul data-dropdown-target="menu" class="hidden">
    <li><a href="/profile">Profile</a></li>
    <li><a href="/settings">Settings</a></li>
    <li>
      <button data-action="click->dropdown#close">
        Close
      </button>
    </li>
  </ul>
</div>
```

---

## Targets

### Target Declaration & Usage

```javascript
export default class extends Controller {
  static targets = ["input", "output", "submitButton"]
  
  // Singular target (returns first matching element or undefined)
  updateOutput() {
    if (this.hasInputTarget) {
      this.outputTarget.textContent = this.inputTarget.value
    }
  }
  
  // Plural targets (returns array, empty if none)
  clearAllInputs() {
    this.inputTargets.forEach(input => {
      input.value = ""
    })
  }
  
  // Check existence before use
  submit() {
    if (this.hasSubmitButtonTarget) {
      this.submitButtonTarget.disabled = true
    }
  }
}
```

```html
<form data-controller="form">
  <input data-form-target="input" type="text">
  <input data-form-target="input" type="email">
  
  <div data-form-target="output"></div>
  
  <button data-form-target="submitButton">Submit</button>
</form>
```

### Target Callbacks

```javascript
export default class extends Controller {
  static targets = ["item"]
  
  // Called when target is added to DOM
  itemTargetConnected(element) {
    console.log("Item added:", element)
    this.updateCount()
  }
  
  // Called when target is removed from DOM
  itemTargetDisconnected(element) {
    console.log("Item removed:", element)
    this.updateCount()
  }
  
  updateCount() {
    this.element.dataset.count = this.itemTargets.length
  }
}
```

---

## Values

### Value Types

```javascript
export default class extends Controller {
  static values = {
    // Boolean
    open: { type: Boolean, default: false },
    
    // String
    url: { type: String, default: "" },
    
    // Number
    count: { type: Number, default: 0 },
    
    // Array
    items: { type: Array, default: [] },
    
    // Object
    config: { type: Object, default: {} }
  }
  
  // Access values
  logValues() {
    console.log(this.openValue)      // boolean
    console.log(this.urlValue)       // string
    console.log(this.countValue)     // number
    console.log(this.itemsValue)     // array
    console.log(this.configValue)    // object
  }
  
  // Set values (triggers change callback)
  increment() {
    this.countValue++
  }
  
  addItem(item) {
    this.itemsValue = [...this.itemsValue, item]
  }
}
```

```html
<div data-controller="example"
     data-example-open-value="true"
     data-example-url-value="/api/data"
     data-example-count-value="5"
     data-example-items-value='["a","b","c"]'
     data-example-config-value='{"key":"value"}'>
</div>
```

### Value Changed Callbacks

```javascript
export default class extends Controller {
  static values = {
    loading: Boolean,
    page: Number,
    filters: Object
  }
  
  // Called whenever value changes
  loadingValueChanged(value, previousValue) {
    this.element.classList.toggle("is-loading", value)
    
    if (value) {
      this.disableInteraction()
    } else {
      this.enableInteraction()
    }
  }
  
  pageValueChanged(value) {
    this.loadPage(value)
  }
  
  filtersValueChanged(value, previousValue) {
    // Only fetch if actually changed
    if (JSON.stringify(value) !== JSON.stringify(previousValue)) {
      this.applyFilters()
    }
  }
}
```

---

## Actions

### Action Syntax

```html
<!-- Basic action -->
<button data-action="click->controller#method">Click</button>

<!-- Multiple actions -->
<input data-action="input->search#update focus->search#expand blur->search#collapse">

<!-- Event options -->
<form data-action="submit->form#save:prevent">

<!-- Window/document events -->
<div data-controller="sidebar"
     data-action="resize@window->sidebar#layout
                  keydown.escape@document->sidebar#close">

<!-- Keyboard shortcuts -->
<input data-action="keydown.enter->form#submit
                    keydown.escape->form#cancel">
```

### Action Parameters

```html
<!-- Pass data to actions -->
<button data-action="click->cart#add"
        data-cart-id-param="123"
        data-cart-quantity-param="2">
  Add to Cart
</button>

<button data-action="click->tabs#select"
        data-tabs-index-param="0">
  Tab 1
</button>
```

```javascript
export default class extends Controller {
  add({ params: { id, quantity } }) {
    console.log(`Adding ${quantity} of item ${id}`)
  }
  
  select({ params: { index } }) {
    this.showTab(index)
  }
}
```

### Event Object Access

```javascript
export default class extends Controller {
  handleClick(event) {
    // Access event
    event.preventDefault()
    event.stopPropagation()
    
    // Access current target (element with action)
    console.log(event.currentTarget)
    
    // Access original target
    console.log(event.target)
    
    // Access params
    const { id } = event.params
  }
  
  handleKeydown(event) {
    if (event.key === "Enter" && event.metaKey) {
      this.submit()
    }
  }
}
```

---

## Outlets

### Outlet Declaration

```javascript
// tabs_controller.js
export default class extends Controller {
  static outlets = ["tab-panel"]
  
  select(event) {
    const index = event.params.index
    
    // Access all outlet controllers
    this.tabPanelOutlets.forEach((panel, i) => {
      panel.toggle(i === index)
    })
  }
}

// tab_panel_controller.js
export default class extends Controller {
  static values = { active: Boolean }
  
  toggle(active) {
    this.activeValue = active
  }
  
  activeValueChanged(value) {
    this.element.hidden = !value
  }
}
```

```html
<div data-controller="tabs"
     data-tabs-tab-panel-outlet=".tab-panel">
  
  <nav>
    <button data-action="click->tabs#select" data-tabs-index-param="0">Tab 1</button>
    <button data-action="click->tabs#select" data-tabs-index-param="1">Tab 2</button>
  </nav>
</div>

<div class="tab-panel" data-controller="tab-panel" data-tab-panel-active-value="true">
  Content 1
</div>
<div class="tab-panel" data-controller="tab-panel">
  Content 2
</div>
```

### Outlet Callbacks

```javascript
export default class extends Controller {
  static outlets = ["item"]
  
  // Called when outlet connects
  itemOutletConnected(outlet, element) {
    console.log("Item outlet connected:", outlet)
    this.updateCount()
  }
  
  // Called when outlet disconnects
  itemOutletDisconnected(outlet, element) {
    console.log("Item outlet disconnected:", outlet)
    this.updateCount()
  }
  
  updateCount() {
    this.countValue = this.itemOutlets.length
  }
}
```

---

## CSS Classes

### Class Declaration

```javascript
export default class extends Controller {
  static classes = ["active", "loading", "error", "hidden"]
  
  activate() {
    this.element.classList.add(this.activeClass)
  }
  
  deactivate() {
    this.element.classList.remove(this.activeClass)
  }
  
  setLoading(isLoading) {
    this.element.classList.toggle(this.loadingClass, isLoading)
  }
  
  // Check if class is configured
  showError() {
    if (this.hasErrorClass) {
      this.element.classList.add(this.errorClass)
    }
  }
}
```

```html
<div data-controller="button"
     data-button-active-class="btn--active"
     data-button-loading-class="btn--loading"
     data-button-error-class="btn--error">
  <button data-action="click->button#activate">
    Click me
  </button>
</div>
```

---

## Common Patterns

### Debounced Input

```javascript
// search_controller.js
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  static targets = ["input", "results"]
  static values = { 
    url: String,
    debounce: { type: Number, default: 300 }
  }
  
  search() {
    clearTimeout(this.timeout)
    
    this.timeout = setTimeout(() => {
      this.performSearch()
    }, this.debounceValue)
  }
  
  async performSearch() {
    const query = this.inputTarget.value
    if (query.length < 2) return
    
    const response = await fetch(`${this.urlValue}?q=${encodeURIComponent(query)}`)
    this.resultsTarget.innerHTML = await response.text()
  }
  
  disconnect() {
    clearTimeout(this.timeout)
  }
}
```

```html
<div data-controller="search" data-search-url-value="/search">
  <input data-search-target="input"
         data-action="input->search#search"
         type="search">
  <div data-search-target="results"></div>
</div>
```

### Form Validation

```javascript
// form_validation_controller.js
export default class extends Controller {
  static targets = ["submit", "field"]
  
  connect() {
    this.validate()
  }
  
  validate() {
    const isValid = this.fieldTargets.every(field => field.checkValidity())
    this.submitTarget.disabled = !isValid
  }
  
  showErrors(event) {
    this.fieldTargets.forEach(field => {
      const error = field.nextElementSibling
      if (error?.classList.contains("error")) {
        error.textContent = field.validationMessage
        error.hidden = field.validity.valid
      }
    })
  }
}
```

### Clipboard

```javascript
// clipboard_controller.js
export default class extends Controller {
  static targets = ["source"]
  static values = { successDuration: { type: Number, default: 2000 } }
  
  async copy() {
    const text = this.sourceTarget.value || this.sourceTarget.textContent
    
    try {
      await navigator.clipboard.writeText(text)
      this.showSuccess()
    } catch {
      this.showError()
    }
  }
  
  showSuccess() {
    this.element.dataset.copied = "true"
    
    setTimeout(() => {
      delete this.element.dataset.copied
    }, this.successDurationValue)
  }
}
```

```html
<div data-controller="clipboard">
  <code data-clipboard-target="source">npm install stimulus</code>
  <button data-action="click->clipboard#copy">Copy</button>
</div>

<style>
  [data-copied="true"] button::after {
    content: " ✓";
  }
</style>
```

### Toggle Visibility

```javascript
// toggle_controller.js
export default class extends Controller {
  static targets = ["content"]
  static classes = ["hidden"]
  static values = { open: Boolean }
  
  toggle() {
    this.openValue = !this.openValue
  }
  
  show() {
    this.openValue = true
  }
  
  hide() {
    this.openValue = false
  }
  
  openValueChanged(value) {
    this.contentTargets.forEach(el => {
      el.classList.toggle(this.hiddenClass, !value)
    })
    
    this.element.setAttribute("aria-expanded", value)
  }
}
```

### Loading Button

```javascript
// loading_button_controller.js
export default class extends Controller {
  static values = { 
    loadingText: { type: String, default: "Loading..." }
  }
  
  connect() {
    this.originalText = this.element.textContent
  }
  
  start() {
    this.element.disabled = true
    this.element.textContent = this.loadingTextValue
  }
  
  stop() {
    this.element.disabled = false
    this.element.textContent = this.originalText
  }
}
```

```html
<button data-controller="loading-button"
        data-action="click->loading-button#start"
        data-loading-button-loading-text-value="Saving...">
  Save
</button>
```

### Auto-Submit Form

```javascript
// auto_submit_controller.js
export default class extends Controller {
  static values = { debounce: { type: Number, default: 300 } }
  
  submit() {
    clearTimeout(this.timeout)
    
    this.timeout = setTimeout(() => {
      this.element.requestSubmit()
    }, this.debounceValue)
  }
  
  submitNow() {
    clearTimeout(this.timeout)
    this.element.requestSubmit()
  }
  
  disconnect() {
    clearTimeout(this.timeout)
  }
}
```

```html
<form data-controller="auto-submit" data-turbo-frame="results">
  <select data-action="change->auto-submit#submitNow">
    <option>Option 1</option>
    <option>Option 2</option>
  </select>
  
  <input type="search" 
         data-action="input->auto-submit#submit"
         placeholder="Search...">
</form>
```

---

## Turbo Integration

### Handling Turbo Events

```javascript
// navigation_controller.js
export default class extends Controller {
  connect() {
    document.addEventListener("turbo:before-fetch-request", this.showLoading)
    document.addEventListener("turbo:before-fetch-response", this.hideLoading)
  }
  
  disconnect() {
    document.removeEventListener("turbo:before-fetch-request", this.showLoading)
    document.removeEventListener("turbo:before-fetch-response", this.hideLoading)
  }
  
  showLoading = () => {
    this.element.classList.add("is-loading")
  }
  
  hideLoading = () => {
    this.element.classList.remove("is-loading")
  }
}
```

### Frame Loading States

```javascript
// frame_controller.js
export default class extends Controller {
  static targets = ["frame", "loading"]
  
  connect() {
    this.frameTarget.addEventListener("turbo:before-fetch-request", this.start.bind(this))
    this.frameTarget.addEventListener("turbo:before-fetch-response", this.stop.bind(this))
    this.frameTarget.addEventListener("turbo:fetch-request-error", this.error.bind(this))
  }
  
  start() {
    this.loadingTarget.hidden = false
  }
  
  stop() {
    this.loadingTarget.hidden = true
  }
  
  error() {
    this.loadingTarget.hidden = true
    // Show error state
  }
}
```

### Stream Callbacks

```javascript
// notifications_controller.js
export default class extends Controller {
  static targets = ["badge", "list"]
  
  connect() {
    document.addEventListener("turbo:before-stream-render", this.beforeRender.bind(this))
  }
  
  disconnect() {
    document.removeEventListener("turbo:before-stream-render", this.beforeRender.bind(this))
  }
  
  beforeRender(event) {
    const { target } = event.detail.newStream
    
    if (target === "notifications") {
      this.incrementBadge()
      this.playSound()
    }
  }
  
  incrementBadge() {
    const current = parseInt(this.badgeTarget.textContent) || 0
    this.badgeTarget.textContent = current + 1
    this.badgeTarget.hidden = false
  }
  
  playSound() {
    // Play notification sound
  }
}
```

---

## Testing

### Stimulus Test Helpers

```javascript
// test/controllers/toggle_controller.test.js
import { Application } from "@hotwired/stimulus"
import ToggleController from "controllers/toggle_controller"

describe("ToggleController", () => {
  let application
  
  beforeEach(() => {
    document.body.innerHTML = `
      <div data-controller="toggle" data-toggle-hidden-class="hidden">
        <button data-action="click->toggle#toggle">Toggle</button>
        <div data-toggle-target="content">Content</div>
      </div>
    `
    
    application = Application.start()
    application.register("toggle", ToggleController)
  })
  
  afterEach(() => {
    application.stop()
  })
  
  test("toggles content visibility on click", async () => {
    const button = document.querySelector("button")
    const content = document.querySelector("[data-toggle-target='content']")
    
    expect(content.classList.contains("hidden")).toBe(false)
    
    button.click()
    await nextFrame()
    
    expect(content.classList.contains("hidden")).toBe(true)
  })
})

function nextFrame() {
  return new Promise(resolve => requestAnimationFrame(resolve))
}
```

---

## Severity Guide

| Severity | Issue | Impact |
|----------|-------|--------|
| 🔴 Critical | Memory leaks (no cleanup) | Performance degradation |
| 🔴 Critical | Missing null checks on targets | Runtime errors |
| 🟠 High | Not using values for state | Brittle code |
| 🟠 High | Complex inline actions | Maintainability |
| 🟡 Medium | Missing loading states | Poor UX |
| 🟡 Medium | Not using CSS classes API | Coupling to CSS |
| 🟢 Low | Non-descriptive names | Readability |

---

## Report Template

```markdown
## Stimulus Controller Review

### Controller: [name]
- File: [path]
- Purpose: [description]

### Implementation Assessment
| Feature | Used | Correct |
|---------|------|---------|
| Targets | | |
| Values | | |
| Actions | | |
| Classes | | |
| Outlets | | |
| Lifecycle | | |

### Issues Found
1. [Severity] Issue description
   - Impact:
   - Fix:

### Recommendations
1. [Priority] Recommendation
   - Benefit:
```

---

## Related Prompts

- [hotwire-turbo.md](hotwire-turbo.md) — Turbo Frames & Streams
- [viewcomponent.md](viewcomponent.md) — Component-based views
- [../frontend/typescript-patterns.md](../frontend/typescript-patterns.md) — TypeScript patterns

---

*Last updated: 2026-01*

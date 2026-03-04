# ViewComponent — Component-Based Rails Views

> **Purpose**: Production-ready ViewComponent patterns and best practices  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Components, slots, previews, testing, Hotwire integration  
> **Last Updated**: 2026-03

---

## Mission

Help build **reusable, testable view components** for Rails applications. Focus on component design, slots, previews, testing, and proper Hotwire integration.

---

## Guard Clauses

**If no ViewComponent context provided:**
```
NO_VIEWCOMPONENT_CONTEXT

Please provide context:
- Component to build or refactor
- UI pattern/design reference
- Data/props needed
- Slot requirements
- Or describe the view logic to encapsulate

Include existing partial code if converting.
```

**If ViewComponent implementation is solid:**
```
VIEWCOMPONENT_APPROVED

✅ ViewComponent review complete — production ready.

Checks performed:
- Design: ✓ (single responsibility, reusable)
- Slots: ✓ (properly typed and documented)
- Testing: ✓ (unit tests with good coverage)
- Previews: ✓ (all variants documented)
- Performance: ✓ (no N+1, proper caching)

Component follows ViewComponent best practices.
```

---

## Quick Context Checklist

```
☐ view_component gem version
☐ Component purpose
☐ Props/parameters needed
☐ Slot requirements
☐ Variants to support
☐ Preview scenarios
☐ Turbo/Stimulus needs
☐ Test coverage requirements
```

---

## Copy-Paste Prompts

### Prompt: Create ViewComponent
```text
Create a ViewComponent for:

UI element: {{DESCRIPTION}}
Design reference: {{DESIGN_OR_HTML}}

Props needed:
{{PROPS}}

Slots needed:
{{SLOTS}}

Variants: {{VARIANTS}}

Provide:
1. Component class
2. Template (ERB/HTML)
3. Preview class with all variants
4. Tests
5. Usage example
```

### Prompt: Convert Partial to Component
```text
Convert this Rails partial to a ViewComponent:

{{PARTIAL_CODE}}

Called from:
{{CALLER_CODE}}

Requirements:
- Maintain all functionality
- Add proper typing
- Add preview
- Add tests
```

### Prompt: Review ViewComponent
```text
Review this ViewComponent:

Component class:
{{CLASS_CODE}}

Template:
{{TEMPLATE_CODE}}

Check for:
1. **Design**
   - Single responsibility
   - Proper encapsulation
   - Reusability

2. **Interface**
   - Parameter typing
   - Required vs optional
   - Default values

3. **Slots**
   - Proper declarations
   - Polymorphic slots
   - Conditional rendering

4. **Testing**
   - Coverage
   - Edge cases
   - Accessibility

5. **Performance**
   - Collection rendering
   - Caching strategy
   - N+1 queries
```

### Prompt: Add Component Slots
```text
Add slots to this ViewComponent:

Current component:
{{COMPONENT_CODE}}

Slots needed:
- {{SLOT_1}}: {{DESCRIPTION}}
- {{SLOT_2}}: {{DESCRIPTION}}

Requirements:
- Polymorphic where needed
- Default content
- Conditional rendering
```

---

## Component Basics

### Simple Component

```ruby
# app/components/button_component.rb
class ButtonComponent < ViewComponent::Base
  # Parameters with types and defaults
  def initialize(
    label:,
    variant: :primary,
    size: :md,
    disabled: false,
    **html_options
  )
    @label = label
    @variant = variant
    @size = size
    @disabled = disabled
    @html_options = html_options
  end

  # Computed CSS classes
  def classes
    class_names(
      "btn",
      "btn--#{@variant}",
      "btn--#{@size}",
      "btn--disabled" => @disabled
    )
  end

  # Merged HTML attributes
  def html_attributes
    @html_options.merge(
      class: classes,
      disabled: @disabled
    )
  end
end
```

```erb
<%# app/components/button_component.html.erb %>
<button <%= tag.attributes(html_attributes) %>>
  <%= @label %>
</button>
```

```erb
<%# Usage %>
<%= render ButtonComponent.new(
  label: "Submit",
  variant: :primary,
  size: :lg,
  data: { turbo_submit: true }
) %>
```

### Component with Content Block

```ruby
# app/components/card_component.rb
class CardComponent < ViewComponent::Base
  def initialize(title: nil, variant: :default)
    @title = title
    @variant = variant
  end

  def classes
    class_names("card", "card--#{@variant}")
  end

  # Check if content block was provided
  def render?
    content.present? || @title.present?
  end
end
```

```erb
<%# app/components/card_component.html.erb %>
<div class="<%= classes %>">
  <% if @title %>
    <div class="card__header">
      <h3 class="card__title"><%= @title %></h3>
    </div>
  <% end %>
  
  <div class="card__body">
    <%= content %>
  </div>
</div>
```

```erb
<%# Usage %>
<%= render CardComponent.new(title: "Welcome") do %>
  <p>Card content goes here.</p>
<% end %>
```

---

## Slots

### Basic Slots

```ruby
# app/components/modal_component.rb
class ModalComponent < ViewComponent::Base
  # Single slot
  renders_one :header
  renders_one :footer
  
  # Slot with component type
  renders_one :close_button, ButtonComponent
  
  def initialize(open: false, size: :md)
    @open = open
    @size = size
  end
end
```

```erb
<%# app/components/modal_component.html.erb %>
<div class="modal modal--<%= @size %>" data-open="<%= @open %>">
  <div class="modal__content">
    <% if header? %>
      <div class="modal__header">
        <%= header %>
        <% if close_button? %>
          <%= close_button %>
        <% end %>
      </div>
    <% end %>
    
    <div class="modal__body">
      <%= content %>
    </div>
    
    <% if footer? %>
      <div class="modal__footer">
        <%= footer %>
      </div>
    <% end %>
  </div>
</div>
```

```erb
<%# Usage %>
<%= render ModalComponent.new(size: :lg) do |modal| %>
  <% modal.with_header do %>
    <h2>Confirm Action</h2>
  <% end %>
  
  <% modal.with_close_button(label: "×", variant: :ghost) %>
  
  <p>Are you sure you want to continue?</p>
  
  <% modal.with_footer do %>
    <%= render ButtonComponent.new(label: "Cancel", variant: :secondary) %>
    <%= render ButtonComponent.new(label: "Confirm", variant: :danger) %>
  <% end %>
<% end %>
```

### Collection Slots

```ruby
# app/components/nav_component.rb
class NavComponent < ViewComponent::Base
  # Multiple slots of same type
  renders_many :items, "ItemComponent"
  renders_many :actions, ButtonComponent
  
  def initialize(orientation: :horizontal)
    @orientation = orientation
  end

  # Nested component class
  class ItemComponent < ViewComponent::Base
    def initialize(href:, active: false)
      @href = href
      @active = active
    end

    def classes
      class_names("nav__item", "nav__item--active" => @active)
    end
  end
end
```

```erb
<%# app/components/nav_component.html.erb %>
<nav class="nav nav--<%= @orientation %>">
  <ul class="nav__list">
    <% items.each do |item| %>
      <li><%= item %></li>
    <% end %>
  </ul>
  
  <% if actions? %>
    <div class="nav__actions">
      <% actions.each do |action| %>
        <%= action %>
      <% end %>
    </div>
  <% end %>
</nav>

<%# app/components/nav_component/item_component.html.erb %>
<a href="<%= @href %>" class="<%= classes %>">
  <%= content %>
</a>
```

```erb
<%# Usage %>
<%= render NavComponent.new do |nav| %>
  <% nav.with_item(href: "/", active: current_page?("/")) do %>
    Home
  <% end %>
  
  <% nav.with_item(href: "/products") do %>
    Products
  <% end %>
  
  <% nav.with_item(href: "/about") do %>
    About
  <% end %>
  
  <% nav.with_action(label: "Sign In", variant: :secondary) %>
  <% nav.with_action(label: "Sign Up", variant: :primary) %>
<% end %>
```

### Polymorphic Slots

```ruby
# app/components/alert_component.rb
class AlertComponent < ViewComponent::Base
  # Slot that can be different types
  renders_one :icon, types: {
    success: "SuccessIconComponent",
    warning: "WarningIconComponent", 
    error: "ErrorIconComponent",
    info: -> { tag.span("ℹ️", class: "alert__icon") }
  }
  
  renders_one :action, types: {
    button: ButtonComponent,
    link: "LinkComponent"
  }
  
  def initialize(variant: :info, dismissible: false)
    @variant = variant
    @dismissible = dismissible
  end
end
```

```erb
<%# Usage with polymorphic slots %>
<%= render AlertComponent.new(variant: :success, dismissible: true) do |alert| %>
  <% alert.with_icon_success %>
  
  <p>Your changes have been saved.</p>
  
  <% alert.with_action_button(label: "Undo", variant: :ghost, size: :sm) %>
<% end %>

<%= render AlertComponent.new(variant: :error) do |alert| %>
  <% alert.with_icon_error %>
  
  <p>Something went wrong. Please try again.</p>
  
  <% alert.with_action_link(href: "/help") do %>
    Get help
  <% end %>
<% end %>
```

### Lambda Slots

```ruby
# app/components/data_table_component.rb
class DataTableComponent < ViewComponent::Base
  renders_many :columns, ->(header:, key: nil, &block) {
    ColumnComponent.new(header: header, key: key, content_block: block)
  }
  
  def initialize(data:)
    @data = data
  end

  class ColumnComponent < ViewComponent::Base
    attr_reader :header, :key, :content_block
    
    def initialize(header:, key:, content_block:)
      @header = header
      @key = key
      @content_block = content_block
    end
    
    def render_cell(row)
      if content_block
        content_block.call(row)
      elsif key
        row.public_send(key)
      end
    end
  end
end
```

```erb
<%# app/components/data_table_component.html.erb %>
<table class="data-table">
  <thead>
    <tr>
      <% columns.each do |column| %>
        <th><%= column.header %></th>
      <% end %>
    </tr>
  </thead>
  <tbody>
    <% @data.each do |row| %>
      <tr>
        <% columns.each do |column| %>
          <td><%= column.render_cell(row) %></td>
        <% end %>
      </tr>
    <% end %>
  </tbody>
</table>
```

```erb
<%# Usage %>
<%= render DataTableComponent.new(data: @users) do |table| %>
  <% table.with_column(header: "Name", key: :name) %>
  <% table.with_column(header: "Email", key: :email) %>
  <% table.with_column(header: "Status") do |user| %>
    <%= render StatusBadgeComponent.new(status: user.status) %>
  <% end %>
  <% table.with_column(header: "Actions") do |user| %>
    <%= link_to "Edit", edit_user_path(user) %>
  <% end %>
<% end %>
```

---

## Previews

### Basic Preview

```ruby
# test/components/previews/button_component_preview.rb
class ButtonComponentPreview < ViewComponent::Preview
  # @!group Variants
  
  def primary
    render ButtonComponent.new(label: "Primary Button", variant: :primary)
  end
  
  def secondary
    render ButtonComponent.new(label: "Secondary Button", variant: :secondary)
  end
  
  def danger
    render ButtonComponent.new(label: "Danger Button", variant: :danger)
  end
  
  # @!endgroup
  
  # @!group Sizes
  
  def small
    render ButtonComponent.new(label: "Small", size: :sm)
  end
  
  def medium
    render ButtonComponent.new(label: "Medium", size: :md)
  end
  
  def large
    render ButtonComponent.new(label: "Large", size: :lg)
  end
  
  # @!endgroup
  
  # @!group States
  
  def disabled
    render ButtonComponent.new(label: "Disabled", disabled: true)
  end
  
  def with_icon
    render ButtonComponent.new(label: "With Icon", icon: "arrow-right")
  end
  
  # @!endgroup
end
```

### Preview with Parameters

```ruby
# test/components/previews/alert_component_preview.rb
class AlertComponentPreview < ViewComponent::Preview
  # @param variant select { choices: [info, success, warning, error] }
  # @param dismissible toggle
  # @param message text
  def playground(variant: :info, dismissible: false, message: "This is an alert message.")
    render AlertComponent.new(variant: variant.to_sym, dismissible: dismissible) do
      message
    end
  end
  
  # Preview with real data
  def with_user_context
    user = User.first || User.new(name: "Example User")
    
    render AlertComponent.new(variant: :success) do |alert|
      alert.with_icon_success
      "Welcome back, #{user.name}!"
    end
  end
end
```

### Preview Layouts

```ruby
# test/components/previews/card_component_preview.rb
class CardComponentPreview < ViewComponent::Preview
  # Use custom layout for preview
  layout "component_preview"
  
  def default
    render CardComponent.new(title: "Card Title") do
      "Card content goes here."
    end
  end
  
  # Different layout for specific preview
  def in_grid
    render_with_template(
      template: "card_component_preview/in_grid",
      locals: { cards: 6 }
    )
  end
end
```

```erb
<%# test/components/previews/card_component_preview/in_grid.html.erb %>
<div class="grid grid-cols-3 gap-4">
  <% cards.times do |i| %>
    <%= render CardComponent.new(title: "Card #{i + 1}") do %>
      Content for card <%= i + 1 %>
    <% end %>
  <% end %>
</div>
```

---

## Testing

### Unit Testing Components

```ruby
# test/components/button_component_test.rb
require "test_helper"

class ButtonComponentTest < ViewComponent::TestCase
  def test_renders_label
    render_inline(ButtonComponent.new(label: "Click me"))
    
    assert_selector "button", text: "Click me"
  end
  
  def test_renders_variant_class
    render_inline(ButtonComponent.new(label: "Test", variant: :danger))
    
    assert_selector "button.btn--danger"
  end
  
  def test_renders_disabled_state
    render_inline(ButtonComponent.new(label: "Test", disabled: true))
    
    assert_selector "button[disabled]"
    assert_selector "button.btn--disabled"
  end
  
  def test_passes_html_attributes
    render_inline(ButtonComponent.new(
      label: "Test",
      data: { action: "click->form#submit" },
      id: "submit-btn"
    ))
    
    assert_selector "button#submit-btn[data-action='click->form#submit']"
  end
  
  def test_renders_all_sizes
    %i[sm md lg].each do |size|
      render_inline(ButtonComponent.new(label: "Test", size: size))
      
      assert_selector "button.btn--#{size}"
    end
  end
end
```

### Testing Slots

```ruby
# test/components/modal_component_test.rb
class ModalComponentTest < ViewComponent::TestCase
  def test_renders_with_header_slot
    render_inline(ModalComponent.new) do |modal|
      modal.with_header { "Modal Title" }
      "Body content"
    end
    
    assert_selector ".modal__header", text: "Modal Title"
    assert_selector ".modal__body", text: "Body content"
  end
  
  def test_renders_without_optional_slots
    render_inline(ModalComponent.new) do
      "Just body"
    end
    
    assert_no_selector ".modal__header"
    assert_no_selector ".modal__footer"
    assert_selector ".modal__body", text: "Just body"
  end
  
  def test_renders_collection_slot
    render_inline(NavComponent.new) do |nav|
      nav.with_item(href: "/home") { "Home" }
      nav.with_item(href: "/about") { "About" }
    end
    
    assert_selector ".nav__item", count: 2
    assert_selector "a[href='/home']", text: "Home"
    assert_selector "a[href='/about']", text: "About"
  end
end
```

### RSpec Testing

```ruby
# spec/components/button_component_spec.rb
require "rails_helper"

RSpec.describe ButtonComponent, type: :component do
  it "renders the label" do
    render_inline(described_class.new(label: "Submit"))
    
    expect(page).to have_button("Submit")
  end
  
  it "applies variant classes" do
    render_inline(described_class.new(label: "Test", variant: :primary))
    
    expect(page).to have_css("button.btn--primary")
  end
  
  context "when disabled" do
    it "renders disabled attribute" do
      render_inline(described_class.new(label: "Test", disabled: true))
      
      expect(page).to have_button("Test", disabled: true)
    end
  end
  
  describe "accessibility" do
    it "has accessible name" do
      render_inline(described_class.new(label: "Submit Form"))
      
      expect(page).to have_button("Submit Form")
    end
  end
end
```

---

## Hotwire Integration

### Turbo Frame Component

```ruby
# app/components/turbo_form_component.rb
class TurboFormComponent < ViewComponent::Base
  def initialize(model:, url: nil, frame: nil)
    @model = model
    @url = url
    @frame = frame || dom_id(model)
  end

  def form_options
    {
      url: @url,
      data: { turbo_frame: @frame }
    }
  end
end
```

```erb
<%# app/components/turbo_form_component.html.erb %>
<%= turbo_frame_tag @frame do %>
  <%= form_with model: @model, **form_options do |f| %>
    <%= content %>
  <% end %>
<% end %>
```

### Stimulus-Ready Component

```ruby
# app/components/dropdown_component.rb
class DropdownComponent < ViewComponent::Base
  renders_one :trigger
  renders_many :items, "ItemComponent"
  
  def initialize(align: :left)
    @align = align
  end

  def stimulus_controller
    "dropdown"
  end

  def stimulus_attributes
    {
      controller: stimulus_controller,
      "#{stimulus_controller}-open-value": false
    }
  end

  class ItemComponent < ViewComponent::Base
    def initialize(href: nil, divider: false)
      @href = href
      @divider = divider
    end
  end
end
```

```erb
<%# app/components/dropdown_component.html.erb %>
<div <%= tag.attributes(stimulus_attributes) %> class="dropdown">
  <div data-action="click->dropdown#toggle" data-dropdown-target="trigger">
    <%= trigger %>
  </div>
  
  <div data-dropdown-target="menu" class="dropdown__menu dropdown__menu--<%= @align %>" hidden>
    <% items.each do |item| %>
      <%= item %>
    <% end %>
  </div>
</div>
```

### Streaming Component Updates

```ruby
# app/components/comment_component.rb
class CommentComponent < ViewComponent::Base
  with_collection_parameter :comment
  
  def initialize(comment:)
    @comment = comment
  end

  # DOM ID for Turbo Streams targeting
  def dom_id
    helpers.dom_id(@comment)
  end

  # Used for broadcasts
  def self.broadcast_target
    "comments"
  end
end
```

```ruby
# app/models/comment.rb
class Comment < ApplicationRecord
  after_create_commit -> {
    broadcast_append_to(
      post,
      target: CommentComponent.broadcast_target,
      partial: "comments/comment",
      locals: { comment: self }
    )
  }
end
```

---

## Collection Rendering

### Efficient Collection Rendering

```ruby
# app/components/user_card_component.rb
class UserCardComponent < ViewComponent::Base
  # Enable collection rendering
  with_collection_parameter :user
  
  def initialize(user:, show_avatar: true)
    @user = user
    @show_avatar = show_avatar
  end
end
```

```erb
<%# Render entire collection efficiently %>
<%= render UserCardComponent.with_collection(@users, show_avatar: true) %>

<%# Equivalent to, but faster than: %>
<% @users.each do |user| %>
  <%= render UserCardComponent.new(user: user, show_avatar: true) %>
<% end %>
```

### Collection with Counter

```ruby
class ItemComponent < ViewComponent::Base
  with_collection_parameter :item
  
  def initialize(item:, item_counter: nil, item_iteration: nil)
    @item = item
    @counter = item_counter        # 1-based index
    @iteration = item_iteration    # Iteration object
  end

  def first?
    @iteration&.first?
  end

  def last?
    @iteration&.last?
  end

  def index
    @iteration&.index  # 0-based
  end
end
```

---

## Performance

### Caching

```ruby
# app/components/expensive_component.rb
class ExpensiveComponent < ViewComponent::Base
  def initialize(data:, cache_key: nil)
    @data = data
    @cache_key = cache_key
  end

  # Fragment caching
  def cache_key
    @cache_key || [@data, "v1"]
  end

  def cached?
    @cache_key.present?
  end
end
```

```erb
<%# With Rails fragment caching %>
<% cache cache_key do %>
  <div class="expensive">
    <%= expensive_computation %>
  </div>
<% end %>
```

### Avoiding N+1 in Components

```ruby
# ❌ Bad: N+1 in component
class CommentComponent < ViewComponent::Base
  def initialize(comment:)
    @comment = comment
  end

  def author_name
    @comment.user.name  # N+1!
  end
end

# ✅ Good: Preload in controller/parent
class CommentsController < ApplicationController
  def index
    @comments = Comment.includes(:user).recent
  end
end

# Or accept preloaded data
class CommentComponent < ViewComponent::Base
  def initialize(comment:, author: nil)
    @comment = comment
    @author = author || comment.user
  end

  def author_name
    @author.name
  end
end
```

---

## Severity Guide

| Severity | Issue | Impact |
|----------|-------|--------|
| 🔴 Critical | N+1 queries in components | Performance disaster |
| 🔴 Critical | Missing accessibility | Excludes users |
| 🟠 High | No tests | Unreliable components |
| 🟠 High | Missing previews | Poor documentation |
| 🟡 Medium | Oversized components | Hard to maintain |
| 🟡 Medium | No slot typing | Unclear API |
| 🟢 Low | Missing inline docs | Developer experience |

---

## Report Template

```markdown
## ViewComponent Review

### Component: [name]
- File: [path]
- Purpose: [description]

### Interface
| Parameter | Type | Required | Default |
|-----------|------|----------|---------|
| | | | |

### Slots
| Slot | Type | Multiple | Description |
|------|------|----------|-------------|
| | | | |

### Assessment
| Criteria | Status | Notes |
|----------|--------|-------|
| Single responsibility | | |
| Proper encapsulation | | |
| Test coverage | | |
| Preview coverage | | |
| Accessibility | | |
| Performance | | |

### Issues Found
1. [Severity] Issue
   - Impact:
   - Fix:
```

---

## Related Prompts

- [hotwire-turbo.md](hotwire-turbo.md) — Turbo integration
- [stimulus-controllers.md](stimulus-controllers.md) — Stimulus patterns
- [rspec-test-generation.md](rspec-test-generation.md) — Testing patterns

---

*Last updated: 2026-01*

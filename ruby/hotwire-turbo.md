# Hotwire & Turbo — Modern Rails Frontend

> **Purpose**: Production-ready Turbo Frames, Streams, and morphing patterns  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Turbo Drive, Frames, Streams, broadcasting, page refreshes  
> **Last Updated**: 2026-03

---

## Mission

Help build **fast, modern Rails frontends** using Hotwire/Turbo without writing custom JavaScript. Focus on Turbo Frames for partial updates, Turbo Streams for real-time, and page refresh morphing for seamless updates.

---

## Guard Clauses

**If no Turbo context provided:**
```
NO_TURBO_CONTEXT

Please provide context:
- Rails version (7.0+, 7.1+, 8.0+)
- Feature to implement
- Current view/controller code
- Or describe the interaction pattern

Include whether you need real-time updates.
```

**If Turbo implementation is solid:**
```
TURBO_APPROVED

✅ Hotwire implementation review complete — production ready.

Checks performed:
- Turbo Frames: ✓ (proper IDs, lazy loading)
- Turbo Streams: ✓ (correct actions, broadcasts)
- Drive: ✓ (form handling, navigation)
- Morphing: ✓ (page refresh patterns)

Implementation follows Hotwire best practices.
```

---

## Quick Context Checklist

```
☐ Rails version (7.x or 8.x)
☐ turbo-rails gem version
☐ Real-time requirements
☐ Feature description
☐ Current implementation (if refactoring)
☐ WebSocket setup (Action Cable)
☐ Authentication context
```

---

## Copy-Paste Prompts

### Prompt: Implement Turbo Frames
```text
Implement Turbo Frames for this feature:

Feature: {{FEATURE_DESCRIPTION}}
Current view: {{VIEW_CODE}}
Controller: {{CONTROLLER_CODE}}

Requirements:
- Lazy loading: {{YES_NO}}
- Frame targeting: {{TARGETS}}
- Loading states: {{YES_NO}}

Provide:
1. Updated view with turbo_frame_tag
2. Controller changes
3. Any partials needed
4. Loading/empty states
```

### Prompt: Implement Turbo Streams
```text
Implement real-time updates with Turbo Streams:

Feature: {{FEATURE_DESCRIPTION}}
Model: {{MODEL_CODE}}
Current view: {{VIEW_CODE}}

Requirements:
- Actions needed: {{APPEND_PREPEND_REPLACE_REMOVE}}
- Broadcast to: {{CHANNEL_SCOPE}}
- Trigger: {{MODEL_CALLBACK_OR_CONTROLLER}}

Provide:
1. Model broadcasts
2. Stream subscription in view
3. Partial for stream content
4. Controller updates if needed
```

### Prompt: Add Page Refresh Morphing
```text
Implement Turbo page refresh with morphing:

Feature: {{FEATURE_DESCRIPTION}}
Rails version: {{VERSION}}

Requirements:
- Preserve scroll: {{YES_NO}}
- Preserve form state: {{YES_NO}}
- Broadcast updates: {{YES_NO}}

Provide:
1. Turbo refresh configuration
2. Broadcast setup
3. Permanent element marking
4. Any stimulus controllers needed
```

### Prompt: Review Turbo Implementation
```text
Review this Hotwire/Turbo implementation:

{{CODE}}

Check for:
1. **Turbo Frames**
   - Unique, meaningful IDs
   - Proper nesting
   - Target attributes
   - Lazy loading optimization

2. **Turbo Streams**
   - Correct action types
   - DOM ID targeting
   - Broadcast efficiency
   - Authorization in broadcasts

3. **Turbo Drive**
   - Form submissions
   - Flash messages
   - Redirect handling
   - Data-turbo attributes

4. **Performance**
   - Minimal DOM updates
   - Efficient broadcasts
   - Proper caching
```

### Prompt: Convert to Hotwire
```text
Convert this JavaScript/AJAX feature to Hotwire:

Current implementation:
{{CURRENT_CODE}}

Feature behavior: {{DESCRIPTION}}

Convert to use:
- Turbo Frames for partial updates
- Turbo Streams for real-time
- Stimulus only where necessary

Maintain all existing functionality.
```

---

## Turbo Frames

### Basic Frame

```erb
<%# app/views/posts/show.html.erb %>
<%= turbo_frame_tag @post do %>
  <h1><%= @post.title %></h1>
  <p><%= @post.content %></p>
  
  <%= link_to "Edit", edit_post_path(@post) %>
<% end %>

<%# app/views/posts/edit.html.erb %>
<%= turbo_frame_tag @post do %>
  <%= render "form", post: @post %>
<% end %>
```

### Lazy Loading Frame

```erb
<%# Lazy load comments when scrolled into view %>
<%= turbo_frame_tag "comments", 
                    src: post_comments_path(@post),
                    loading: :lazy do %>
  <div class="animate-pulse">Loading comments...</div>
<% end %>

<%# app/views/comments/index.html.erb %>
<%= turbo_frame_tag "comments" do %>
  <%= render @comments %>
<% end %>
```

### Frame Targeting

```erb
<%# Link that updates a different frame %>
<%= link_to "View Details", 
            product_path(product),
            data: { turbo_frame: "product_details" } %>

<%# Target frame %>
<%= turbo_frame_tag "product_details" do %>
  <p>Select a product to see details</p>
<% end %>

<%# Breaking out of frames %>
<%= link_to "Full Page", 
            product_path(product),
            data: { turbo_frame: "_top" } %>
```

### Nested Frames

```erb
<%# Parent frame %>
<%= turbo_frame_tag "inbox" do %>
  <div class="email-list">
    <% @emails.each do |email| %>
      <%= turbo_frame_tag dom_id(email) do %>
        <%= render email %>
      <% end %>
    <% end %>
  </div>
  
  <%# Nested frame for preview %>
  <%= turbo_frame_tag "email_preview" do %>
    <p>Select an email to preview</p>
  <% end %>
<% end %>
```

### Frame with Loading States

```erb
<%= turbo_frame_tag "search_results",
                    data: { turbo_frame_loading_class: "opacity-50" } do %>
  <%= render @results %>
<% end %>

<style>
  turbo-frame[busy] { opacity: 0.5; }
  turbo-frame[busy]::after {
    content: "";
    /* spinner styles */
  }
</style>
```

---

## Turbo Streams

### Stream Actions

```erb
<%# Append to a list %>
<%= turbo_stream.append "messages" do %>
  <%= render @message %>
<% end %>

<%# Prepend to a list %>
<%= turbo_stream.prepend "notifications" do %>
  <%= render @notification %>
<% end %>

<%# Replace specific element %>
<%= turbo_stream.replace dom_id(@post) do %>
  <%= render @post %>
<% end %>

<%# Update contents (keep element) %>
<%= turbo_stream.update "flash" do %>
  <%= render "shared/flash" %>
<% end %>

<%# Remove element %>
<%= turbo_stream.remove dom_id(@comment) %>

<%# Multiple actions %>
<%= turbo_stream.remove dom_id(@item) %>
<%= turbo_stream.update "cart_count", html: @cart.items_count %>
<%= turbo_stream.prepend "flash" do %>
  <div class="alert alert-success">Item removed!</div>
<% end %>
```

### Controller Stream Response

```ruby
# app/controllers/comments_controller.rb
class CommentsController < ApplicationController
  def create
    @comment = @post.comments.build(comment_params)
    
    if @comment.save
      respond_to do |format|
        format.turbo_stream
        format.html { redirect_to @post }
      end
    else
      render :new, status: :unprocessable_entity
    end
  end
  
  def destroy
    @comment = Comment.find(params[:id])
    @comment.destroy
    
    respond_to do |format|
      format.turbo_stream { render turbo_stream: turbo_stream.remove(@comment) }
      format.html { redirect_to @comment.post }
    end
  end
end
```

```erb
<%# app/views/comments/create.turbo_stream.erb %>
<%= turbo_stream.append "comments" do %>
  <%= render @comment %>
<% end %>

<%= turbo_stream.update "new_comment" do %>
  <%= render "form", comment: Comment.new %>
<% end %>

<%= turbo_stream.update "comments_count", html: @post.comments.count %>
```

### Model Broadcasts

```ruby
# app/models/message.rb
class Message < ApplicationRecord
  belongs_to :room
  
  # Broadcast to room channel after create
  broadcasts_to :room
  
  # Or with custom options
  broadcasts_to :room,
                inserts_by: :prepend,
                target: "messages"
  
  # Multiple broadcasts
  after_create_commit -> { broadcast_prepend_to room }
  after_update_commit -> { broadcast_replace_to room }
  after_destroy_commit -> { broadcast_remove_to room }
end

# With custom partial/locals
class Notification < ApplicationRecord
  after_create_commit -> {
    broadcast_prepend_to(
      user,
      :notifications,
      partial: "notifications/notification",
      locals: { notification: self, unread: true }
    )
  }
end
```

### Stream Subscription

```erb
<%# Subscribe to streams in view %>
<%= turbo_stream_from @room %>
<%= turbo_stream_from current_user, :notifications %>

<%# Multiple streams %>
<%= turbo_stream_from @room %>
<%= turbo_stream_from @room, :typing_indicators %>

<div id="messages">
  <%= render @room.messages %>
</div>
```

### Conditional Broadcasts

```ruby
class Comment < ApplicationRecord
  after_create_commit :broadcast_to_subscribers
  
  private
  
  def broadcast_to_subscribers
    # Only broadcast to users who should see it
    post.subscribers.each do |user|
      broadcast_append_to(
        [user, :feed],
        target: "feed",
        partial: "comments/comment"
      )
    end
  end
end

# With authorization check
class Message < ApplicationRecord
  after_create_commit -> {
    room.users.each do |user|
      next unless user.can_view?(room)
      
      broadcast_append_to(
        [user, room],
        target: "messages"
      )
    end
  }
end
```

---

## Turbo Drive

### Form Submission

```erb
<%# Standard form - Turbo handles automatically %>
<%= form_with model: @post do |f| %>
  <%= f.text_field :title %>
  <%= f.submit %>
<% end %>

<%# Disable Turbo for specific form %>
<%= form_with model: @file, data: { turbo: false } do |f| %>
  <%= f.file_field :attachment %>
  <%= f.submit %>
<% end %>

<%# Form with stream response %>
<%= form_with model: @comment, 
              data: { turbo_stream: true } do |f| %>
  <%= f.text_area :body %>
  <%= f.submit %>
<% end %>
```

### Flash Messages

```ruby
# app/controllers/application_controller.rb
class ApplicationController < ActionController::Base
  # Flash works with Turbo automatically in Rails 7+
  add_flash_types :success, :error, :warning
end

# Controller
def create
  if @post.save
    redirect_to @post, notice: "Post created!"
  else
    flash.now[:error] = "Could not save post"
    render :new, status: :unprocessable_entity
  end
end
```

```erb
<%# app/views/layouts/application.html.erb %>
<div id="flash">
  <% flash.each do |type, message| %>
    <div class="alert alert-<%= type %>" data-controller="alert">
      <%= message %>
    </div>
  <% end %>
</div>
```

### Navigation Control

```erb
<%# Disable Turbo for link %>
<%= link_to "Download", file_path, data: { turbo: false } %>

<%# Prefetch on hover %>
<%= link_to "Article", article_path, data: { turbo_prefetch: true } %>

<%# Replace instead of advance history %>
<%= link_to "Filter", items_path(sort: :date), 
            data: { turbo_action: "replace" } %>

<%# Confirm before navigation %>
<%= link_to "Delete", post_path(@post),
            data: { turbo_method: :delete,
                    turbo_confirm: "Are you sure?" } %>
```

---

## Page Refresh & Morphing (Rails 8+)

### Basic Morphing Setup

```erb
<%# app/views/layouts/application.html.erb %>
<head>
  <%= turbo_refreshes_with method: :morph, scroll: :preserve %>
  <%= yield :head %>
</head>
```

### Broadcast Page Refresh

```ruby
# app/models/post.rb
class Post < ApplicationRecord
  # Broadcast refresh to viewers
  broadcasts_refreshes
  
  # Or manually
  after_update_commit -> {
    broadcast_refresh_to self
  }
end
```

```erb
<%# Subscribe to refreshes %>
<%= turbo_stream_from @post %>

<%# Content that will morph %>
<article id="<%= dom_id(@post) %>">
  <h1><%= @post.title %></h1>
  <div class="content"><%= @post.content %></div>
</article>
```

### Permanent Elements

```erb
<%# Elements that persist across morphs %>
<div data-turbo-permanent id="video-player">
  <video src="<%= @video.url %>" data-controller="video">
</div>

<%# Form that preserves state %>
<form data-turbo-permanent id="search-form">
  <input type="search" name="q" value="<%= params[:q] %>">
</form>
```

### Scroll Preservation

```erb
<%# Preserve scroll position %>
<%= turbo_refreshes_with method: :morph, scroll: :preserve %>

<%# Reset scroll on specific pages %>
<%= turbo_refreshes_with method: :morph, scroll: :reset %>
```

---

## Common Patterns

### Inline Editing

```erb
<%# Display mode %>
<%= turbo_frame_tag dom_id(post, :content) do %>
  <div class="post-content">
    <%= post.content %>
    <%= link_to "Edit", edit_post_path(post), 
                class: "edit-link" %>
  </div>
<% end %>

<%# Edit mode (returned by edit action) %>
<%= turbo_frame_tag dom_id(@post, :content) do %>
  <%= form_with model: @post do |f| %>
    <%= f.text_area :content %>
    <%= f.submit "Save" %>
    <%= link_to "Cancel", post_path(@post) %>
  <% end %>
<% end %>
```

### Modal Pattern

```erb
<%# Trigger %>
<%= link_to "New Post", new_post_path, 
            data: { turbo_frame: "modal" } %>

<%# Modal frame in layout %>
<%= turbo_frame_tag "modal" %>

<%# Modal content (new.html.erb) %>
<%= turbo_frame_tag "modal" do %>
  <div class="modal-backdrop" data-controller="modal">
    <div class="modal-content">
      <h2>New Post</h2>
      <%= render "form", post: @post %>
    </div>
  </div>
<% end %>
```

### Infinite Scroll

```erb
<%# app/views/posts/index.html.erb %>
<div id="posts">
  <%= render @posts %>
</div>

<% if @pagy.next %>
  <%= turbo_frame_tag "pagination",
                      src: posts_path(page: @pagy.next),
                      loading: :lazy do %>
    <div class="loading">Loading more...</div>
  <% end %>
<% end %>

<%# Subsequent pages append and include next pagination %>
<%= turbo_frame_tag "pagination" do %>
  <% @posts.each do |post| %>
    <%= turbo_stream.append "posts" do %>
      <%= render post %>
    <% end %>
  <% end %>
  
  <% if @pagy.next %>
    <%= turbo_frame_tag "pagination",
                        src: posts_path(page: @pagy.next),
                        loading: :lazy do %>
      <div class="loading">Loading more...</div>
    <% end %>
  <% end %>
<% end %>
```

### Live Search

```erb
<%# Search form with debounce %>
<%= form_with url: search_path, 
              method: :get,
              data: { 
                controller: "search",
                turbo_frame: "search_results",
                turbo_action: "replace"
              } do |f| %>
  <%= f.search_field :q, 
                     data: { 
                       search_target: "input",
                       action: "input->search#submit"
                     } %>
<% end %>

<%= turbo_frame_tag "search_results" do %>
  <%= render @results %>
<% end %>
```

### Flash Messages with Auto-dismiss

```erb
<%# Stream flash to page %>
<%= turbo_stream.prepend "flash" do %>
  <div class="alert alert-<%= type %>" 
       data-controller="alert"
       data-alert-dismiss-after-value="5000">
    <%= message %>
  </div>
<% end %>
```

---

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Frame not updating | ID mismatch | Ensure frame IDs match exactly |
| Form errors not showing | Missing status code | Return `status: :unprocessable_entity` |
| Stream not received | No subscription | Add `turbo_stream_from` |
| Full page reload | Turbo disabled | Check `data-turbo` attributes |
| Broadcast not working | Wrong channel | Verify broadcast target matches |

### Debugging

```ruby
# Enable Turbo logging
# config/environments/development.rb
config.action_cable.logger = Logger.new(STDOUT)

# Check broadcast targets
Rails.logger.debug "Broadcasting to: #{Turbo::StreamsChannel.verified_stream_name(streamable)}"

# Test broadcasts in console
Turbo::StreamsChannel.broadcast_append_to(
  "messages",
  target: "messages",
  html: "<p>Test</p>"
)
```

---

## Severity Guide

| Severity | Issue | Impact |
|----------|-------|--------|
| 🔴 Critical | Missing frame IDs | Broken functionality |
| 🔴 Critical | Unauthorized broadcasts | Security vulnerability |
| 🟠 High | No loading states | Poor UX |
| 🟠 High | Missing error handling | Silent failures |
| 🟡 Medium | Not using lazy loading | Performance |
| 🟡 Medium | Over-broadcasting | Unnecessary updates |
| 🟢 Low | Inconsistent frame naming | Maintainability |

---

## Report Template

```markdown
## Hotwire/Turbo Review

### Configuration
- Rails version: [version]
- turbo-rails version: [version]
- Action Cable: [yes/no]

### Implementation Assessment
| Feature | Implemented | Quality |
|---------|-------------|---------|
| Turbo Frames | | |
| Turbo Streams | | |
| Turbo Drive | | |
| Page Refresh | | |
| Broadcasts | | |

### Issues Found
1. [Severity] Issue description
   - Location: 
   - Impact:
   - Fix:

### Recommendations
1. [Priority] Recommendation
   - Benefit:
   - Implementation:
```

---

## Related Prompts

- [stimulus-controllers.md](stimulus-controllers.md) — Stimulus JavaScript
- [viewcomponent.md](viewcomponent.md) — Component-based views
- [rails-active-record-performance-audit.md](rails-active-record-performance-audit.md) — Query optimization

---

*Last updated: 2026-01*

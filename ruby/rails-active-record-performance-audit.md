# Rails ActiveRecord Performance — N+1 & Query Optimization

> **Purpose**: Identify and fix database performance issues in Rails  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: N+1 queries, indexes, eager loading, query optimization  
> **Last Updated**: 2026-03

---

## Mission

Find and fix **database performance problems** in Rails applications. Eliminate N+1 queries, add missing indexes, and optimize slow queries.

---

## Guard Clauses

**If no code provided:**
```
NO_CODE_PROVIDED

Please share Rails code to analyze:
- Controller actions
- Model scopes
- View templates
- Or describe the slow behavior

Include any query logs if available.
```

**If performance looks good:**
```
PERFORMANCE_LOOKS_GOOD

✅ **Well-Optimized Queries**

Database access patterns are efficient:
- No N+1 queries detected ✓
- Eager loading used appropriately ✓
- Queries use indexes ✓
- Batch processing where needed ✓

Minor suggestions (optional):
[list any refinements]
```

---

## Quick Context Checklist

```
☐ Rails code (controller, model, view)
☐ Query logs (if available)
☐ Database schema (relevant tables)
☐ Current indexes
☐ Slow endpoints or features
```

---

## Copy-Paste Prompts

### Prompt: Find N+1 Queries
```text
Analyze this Rails code for N+1 query problems:

{{CODE}}

For each N+1 found:
1. Show the problematic code
2. Explain why it's N+1
3. Show the SQL generated
4. Provide the fix with includes/preload
5. Show expected query count after fix
```

### Prompt: Audit Query Performance
```text
Audit this Rails code for performance issues:

{{CODE}}

Schema:
{{SCHEMA}}

Check:
1. N+1 queries
2. Missing indexes
3. Inefficient queries
4. Memory issues (loading too many records)
5. Opportunities for caching

Prioritize fixes by impact.
```

### Prompt: Add Missing Indexes
```text
Analyze this schema and queries for missing indexes:

Schema:
{{SCHEMA}}

Common queries:
{{QUERIES}}

Generate:
1. Migration for missing indexes
2. Explanation of why each index helps
3. Impact estimate
```

### Prompt: Optimize Slow Query
```text
This query is slow:

{{QUERY_OR_CODE}}

EXPLAIN output:
{{EXPLAIN_OUTPUT}}

Suggest:
1. Query optimization
2. Index additions
3. Restructuring options
4. Caching strategies
```

---

## N+1 Query Patterns

### The Problem
```ruby
# ❌ N+1 Query - executes 1 + N queries
# 1 query for posts
# N queries for authors (one per post)
@posts = Post.all
@posts.each do |post|
  puts post.author.name  # Triggers query each iteration
end

# SQL generated:
# SELECT * FROM posts
# SELECT * FROM users WHERE id = 1
# SELECT * FROM users WHERE id = 2
# SELECT * FROM users WHERE id = 3
# ... (N more queries)
```

### The Solutions

#### includes (eager load)
```ruby
# ✅ 2 queries total
@posts = Post.includes(:author).all

# SQL generated:
# SELECT * FROM posts
# SELECT * FROM users WHERE id IN (1, 2, 3, ...)
```

#### preload (always separate queries)
```ruby
# ✅ 2 queries total - always uses separate queries
@posts = Post.preload(:author).all

# Use when you need separate queries (e.g., complex joins)
```

#### eager_load (single JOIN query)
```ruby
# ✅ 1 query with JOIN
@posts = Post.eager_load(:author).all

# SQL generated:
# SELECT posts.*, users.* FROM posts
# LEFT OUTER JOIN users ON users.id = posts.author_id

# Use when you need to filter by association
@posts = Post.eager_load(:author).where(users: { active: true })
```

### Nested Associations
```ruby
# ❌ Multiple N+1 levels
@posts = Post.all
@posts.each do |post|
  puts post.author.profile.bio  # N+1 at each level
end

# ✅ Nested includes
@posts = Post.includes(author: :profile).all
```

### Conditional Loading
```ruby
# Load different associations based on conditions
@posts = Post.includes(:author)
@posts = @posts.includes(:comments) if params[:with_comments]
```

---

## Index Optimization

### When to Add Indexes

| Column Type | Add Index? | Example |
|-------------|------------|---------|
| Foreign keys | ✅ Always | `user_id` |
| Unique constraints | ✅ Always | `email` |
| WHERE clause columns | ✅ Usually | `status`, `active` |
| ORDER BY columns | ⚠️ Consider | `created_at` |
| JOIN columns | ✅ Always | Any joined column |

### Index Migration Examples
```ruby
class AddMissingIndexes < ActiveRecord::Migration[7.1]
  def change
    # Foreign key indexes
    add_index :posts, :user_id
    add_index :comments, :post_id
    
    # Composite index for common query pattern
    add_index :posts, [:user_id, :status]
    
    # Partial index for common filter
    add_index :posts, :published_at, where: "published = true"
    
    # Index for sorting
    add_index :posts, [:user_id, :created_at]
    
    # Unique index
    add_index :users, :email, unique: true
  end
end
```

### Check Existing Indexes
```ruby
# In Rails console
ActiveRecord::Base.connection.indexes(:posts)

# Or check schema.rb
```

---

## Query Optimization Patterns

### Batch Processing
```ruby
# ❌ Loads all records into memory
User.all.each do |user|
  user.update(processed: true)
end

# ✅ Processes in batches of 1000
User.find_each(batch_size: 1000) do |user|
  user.update(processed: true)
end

# ✅ For batch updates
User.in_batches(of: 1000) do |batch|
  batch.update_all(processed: true)
end
```

### Select Only Needed Columns
```ruby
# ❌ Loads all columns
users = User.all.map(&:name)

# ✅ Only loads name column
users = User.pluck(:name)

# ✅ For objects with limited columns
users = User.select(:id, :name, :email).all
```

### Counter Caches
```ruby
# ❌ Counts with query each time
post.comments.count  # SELECT COUNT(*) ...

# ✅ Add counter cache
# Migration
add_column :posts, :comments_count, :integer, default: 0

# Model
class Comment < ApplicationRecord
  belongs_to :post, counter_cache: true
end

# Now post.comments_count is instant (no query)
```

### Avoid N+1 in Views
```erb
<!-- ❌ N+1 in view -->
<% @posts.each do |post| %>
  <%= post.author.name %>
  <%= post.comments.count %>
<% end %>

<!-- ✅ Eager load in controller -->
# Controller
@posts = Post.includes(:author).with_comments_count

<!-- Or use counter cache -->
<%= post.comments_count %>
```

---

## Debugging Tools

### Query Logging
```ruby
# Enable query logging
ActiveRecord::Base.logger = Logger.new(STDOUT)

# See exact queries
User.includes(:posts).where(active: true).to_sql
```

### Bullet Gem (Development)
```ruby
# Gemfile
group :development do
  gem 'bullet'
end

# config/environments/development.rb
config.after_initialize do
  Bullet.enable = true
  Bullet.alert = true
  Bullet.bullet_logger = true
  Bullet.console = true
  Bullet.rails_logger = true
end
```

### EXPLAIN Queries
```ruby
# See query plan
User.where(active: true).explain

# With analyze (PostgreSQL)
User.where(active: true).explain(:analyze)
```

---

## Common Fixes Reference

| Problem | Solution |
|---------|----------|
| N+1 on belongs_to | `includes(:association)` |
| N+1 on has_many | `includes(:association)` |
| N+1 nested | `includes(assoc: :nested)` |
| Slow WHERE | Add index on column |
| Slow JOIN | Add index on foreign key |
| Slow ORDER | Add index on sort column |
| Too many records | Use `find_each` |
| Count queries | Use counter_cache |
| Loading unused columns | Use `select` or `pluck` |

---

## Report Format

### Performance Audit: `performance-audit-[YYYY-MM-DD].md`

```markdown
# Rails Performance Audit

## Summary
- **N+1 Queries Found**: [Count]
- **Missing Indexes**: [Count]
- **Other Issues**: [Count]
- **Impact**: [Critical/High/Medium/Low]

## N+1 Queries

| Location | Association | Queries | Fix |
|----------|-------------|---------|-----|

## Missing Indexes

| Table | Column | Query Pattern | Migration |
|-------|--------|---------------|-----------|

## Other Optimizations

| Issue | Location | Fix |
|-------|----------|-----|

## Recommended Priority
1. [Highest impact fix]
2. [Second priority]
3. [Third priority]

## Migration to Run
```ruby
# Generated migration for all fixes
```
```

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | N+1 with 100+ queries, full table scans |
| **High** | 🟠 | N+1 queries, missing foreign key indexes |
| **Medium** | 🟡 | Suboptimal queries, unnecessary loads |
| **Low** | 🟢 | Minor optimizations, edge cases |

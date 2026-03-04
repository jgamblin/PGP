# Database & ORM Helper

> **Purpose**: Optimize database usage and ORM patterns  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Python 3.11+ application development, tooling, and code quality  
> **Last Updated**: 2026-03
> **Python Version**: 3.11+  

---

## Mission

Help identify **practical database improvements** using SQLAlchemy 2.0, Django ORM, or Polars for analytics. Focus on N+1 problems, indexing, and query optimization.

---

## Guard Clauses

**If no code/schema provided:**
```
NO_ACTIONABLE_INPUT

Please provide database-related code to analyze:
- Models/schema definitions
- Query code
- Migration files
- Performance metrics (slow query logs)
```

**If no issues found:**
```
NO_DATABASE_ISSUES

✅ Database code looks good.
- Indexes: appropriate
- Queries: efficient
- Relationships: properly loaded
- No N+1 problems detected

Consider adding query logging to monitor production performance.
```

---

## Quick Context Checklist

```
☐ ORM framework (SQLAlchemy, Django, Peewee)
☐ Database type (PostgreSQL, MySQL, SQLite)
☐ Models/schema to review
☐ Known slow queries or performance issues
```

> 📝 **Standard Context**: See [_common-sections.md](_common-sections.md) for full input checklist and severity levels.

---

## Copy-Paste Database Prompts

### Prompt: Review ORM Models
```text
Review these ORM models for issues:

{{MODELS}}

Check for:
1. Missing indexes on frequently queried fields
2. N+1 query problems
3. Relationship loading strategies
4. Proper constraints (unique, not null, foreign keys)
5. Data type appropriateness

Provide specific fixes with code examples.
```

### Prompt: Optimize Slow Query
```text
Optimize this slow database query:

Query/Code:
{{CODE}}

Query plan (if available):
{{QUERY_PLAN}}

Database: {{DATABASE_TYPE}}

Suggest:
1. Index additions
2. Query restructuring
3. Eager/lazy loading changes
4. Caching strategies
5. Denormalization if appropriate
```

### Prompt: Design Schema
```text
Design a database schema for:

Requirements: {{REQUIREMENTS}}
Database: {{DATABASE_TYPE}}
ORM: SQLAlchemy 2.0

Generate:
1. SQLAlchemy models with type hints
2. Relationships and backrefs
3. Indexes for expected queries
4. Alembic migration script
5. Sample queries for common operations
```

### Prompt: Fix N+1 Problem
```text
Fix the N+1 query problem in this code:

{{CODE}}

Show:
1. Where the N+1 occurs
2. selectinload/joinedload solution
3. Before/after query count
4. Performance impact estimate
```

### Prompt: Create Migration
```text
Create an Alembic migration for this schema change:

Current model:
{{CURRENT}}

New model:
{{NEW}}

Generate:
1. upgrade() function
2. downgrade() function
3. Data migration if needed
4. Safety checks for production
```

---

## Practical Database Review

### 1. **Schema & Performance**

- **Indexes**: Are frequently queried fields indexed?
- **Relationships**: Proper foreign keys and relationships
- **Data Types**: Appropriate field types and sizes

### 2. **Query Efficiency**

- **N+1 Problems**: Using selectinload/joinedload properly
- **Slow Queries**: Identifying and fixing expensive operations
- **Query Patterns**: Simple, efficient database access

### 3. **Data Safety**

- **Constraints**: Basic data validation at database level
- **Migrations**: Safe database changes
- **Backups**: Data protection strategies

### 4. **Code Quality**

- **Model Organization**: Clear, understandable model structure
- **Documentation**: Key models and relationships explained
- **Maintainability**: Easy to modify and extend

## Review Guidelines

**Watch Out For:**

- Missing indexes on frequently queried fields
- N+1 query problems that slow down the app
- Unsafe migrations that could lose data
- Overly complex models that are hard to understand

## Action Items

### Fix First (High Priority)

1. [ ] **Fix N+1 Query Problems**
 - Add select_related/prefetch_related where needed
 - **Why**: Much faster page loads
 - **Time**: 2-4 hours

2. [ ] **Add Missing Indexes**
 - Index fields you search/filter on frequently
 - **Why**: Faster database queries
 - **Time**: 1-2 hours

3. [ ] **Review Migrations**
 - Make sure database changes are safe
 - **Why**: Avoid data loss or downtime
 - **Time**: 30 minutes

### Improvements (Medium Priority)

4. [ ] **Optimize Complex Queries**
 - Simplify or improve slow database operations
 - **Why**: Better performance with more data
 - **Time**: 2-4 hours

5. [ ] **Clean Up Models**
 - Make model relationships clearer
 - **Why**: Easier to understand and maintain
 - **Time**: 1-3 hours

## Database Review Report

Generate a **Practical Database Analysis** and save it as a markdown file named `database-review-[YYYY-MM-DD].md`:


## Report Format

Generate a comprehensive analysis and save as **two deliverables**:

### 1. Summary Report: `database-schema-orm-optimization-[YYYY-MM-DD].md`

```markdown
# Database Schema Orm Optimization

## Overview
- **Scope**: [What was analyzed]
- **Files Analyzed**: [Count]
- **Critical Issues**: [Count]
- **High Priority Items**: [Count]
- **Recommended Priority**: [Summary]

## Summary
[Brief overview of findings and recommended approach]

## Findings Summary
- Security: [Summary with count]
- Performance: [Summary with count]
- Code Quality: [Summary with count]
- Quality & Testing: [Summary with count]

## Prioritized Action Items
1. [Critical item with link to finding file]
2. [High priority item with link to finding file]
3. [Medium priority item with link to finding file]
...

## Success Metrics
- Security: Zero critical vulnerabilities
- Quality: Linting passes, complexity reduced
- Performance: Response times within targets
- Testing: 80%+ coverage for critical paths
```

### 2. Per-Finding Details: `database-schema-orm-optimization-[YYYY-MM-DD]/`

Create a folder with individual markdown files for each finding:
- `finding-001-security-vulnerability.md`
- `finding-002-performance-issue.md`
- `finding-003-code-quality-concern.md`

Each finding file should contain:
- **Issue description** with friendly, clear explanation
- **Location** (file:line references)
- **Current state** (the problematic code/configuration)
- **Recommended solution** (improved code/configuration with inline comments)
- **Why this helps** (benefits and rationale)
- **Implementation steps** (step-by-step guidance)
- **Testing recommendations** (how to verify the fix works)


```markdown
# Database & ORM Review

## Review Summary

- **Performance**: [How fast are your database queries?]
- **Data Safety**: [Are your migrations and constraints safe?]
- **Query Efficiency**: [Any N+1 problems or slow queries?]
- **Model Quality**: [Are your models clear and well-organized?]
- **Indexing**: [Are the right fields indexed?]

## Good Patterns Found

- **Proper Indexing**: [Fields that are well-indexed]
- **Efficient Queries**: [Good use of select_related/prefetch_related]
- **Safe Migrations**: [Well-planned database changes]
- **Clear Models**: [Easy to understand model structure]

## Role & Intent

**Communication Style**: Polite, friendly, and supportive. Every recommendation should help collaborators feel confident.

**Mission**-Critical Issues (Deployment Blockers)

### Issue 1: [Performance/Data Integrity/Security Risk]

- **Location**: `models.py:lines X-Y` (or relevant file)
- **Impact**: [Performance, data loss, or security risk]
- **Technical Severity**: [Critical - production incident risk]
- **Root Cause**: [Detailed technical analysis]
- **Blast Radius**: [Tables/queries/systems affected]
- **Remediation Strategy**: [Step-by-step fix]
- **Prevention Measures**: [Process/tooling changes]
- **Implementation Example**:
```python
# Current Implementation (Inefficient)
[current model or query]
# Improved Solution (Optimized)
[improved model or query]
# Additional Safeguards
[indexing, migration script, etc.]
```

## Technical Improvement Opportunities

### Schema & Indexing

- **Composite Indexes**: [Where to add for query speed]
- **Denormalization**: [When to use for performance]

### Query Optimization

- **N+1 Prevention**: [select_related, prefetch_related, joinedload]
- **Aggregation & Annotation**: [Optimized query patterns]

### Data Integrity & Security

- **Constraint Enforcement**: [Unique, not null, check constraints]
- **Sensitive Data**: [Encryption and access control]

## Implementation Tasks

1. Add or optimize indexes as identified
2. Refactor queries to prevent N+1 and improve aggregation
3. Ensure migration safety and rollback support
4. Update documentation and model comments

## Review Excellence Validation

**ORM Quality Checklist:**

- Indexes on all foreign keys and frequent query columns
- No N+1 queries or inefficient aggregations
- Migration scripts are safe and reversible
- Sensitive data is protected
- Documentation is clear and complete

```markdown

## Tooling & Automation

Use [_common-sections.md](_common-sections.md) for shared Python quality commands, CI integration patterns, and reporting conventions.

## Metrics & Validation

Use [_common-sections.md](_common-sections.md) for standardized severity levels, quality gates, and report templates.

## Follow-Up & Continuous Improvement

Use [_common-sections.md](_common-sections.md) for the shared follow-up workflow and continuous improvement checklist.

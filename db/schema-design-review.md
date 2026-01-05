# Schema Design Review — Database Architecture Analysis

> **Purpose**: Review and improve database schema design  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Databases**: MySQL, PostgreSQL, SQL Server, SQLite  
> **Last Updated**: 2025-12

---

## Mission

Help review and improve **database schema designs** for correctness, performance, scalability, and maintainability. Focus on identifying design issues early and recommending best practices for the target database.

---

## Guard Clauses

**If no schema provided:**
```
NO_SCHEMA_PROVIDED

Please provide schema to review:
- CREATE TABLE statements
- ER diagram or description
- Data model document
- Or describe the entities and relationships
```

**If schema is well-designed:**
```
SCHEMA_APPROVED

✅ Schema review complete — design looks solid.

Checks performed:
- Normalization: ✓ (appropriate level)
- Data types: ✓ (correctly sized)
- Relationships: ✓ (properly defined)
- Indexes: ✓ (appropriate coverage)
- Constraints: ✓ (data integrity enforced)

Schema is well-designed for stated requirements.
```

---

## Quick Context Checklist

```
☐ Schema DDL or diagram
☐ Database type and version
☐ Expected data volume
☐ Read/write ratio
☐ Query patterns
☐ Scalability requirements
☐ Compliance requirements (PII, etc.)
```

---

## Copy-Paste Review Prompts

### Prompt: Full Schema Review
```text
Review this database schema design:

{{SCHEMA}}

Database: {{DATABASE_TYPE}}
Expected scale: {{EXPECTED_ROWS}} rows
Read/write ratio: {{RATIO}}
Critical queries: {{QUERY_PATTERNS}}

Evaluate:
1. **Normalization**
   - Under-normalized (redundancy, update anomalies)
   - Over-normalized (excessive joins)
   
2. **Data Types**
   - Appropriate sizes (not too large/small)
   - Correct types for data
   - Consistency across tables
   
3. **Primary Keys**
   - Natural vs surrogate key choice
   - Composite key appropriateness
   
4. **Foreign Keys**
   - Missing relationships
   - Cascade behavior
   
5. **Indexes**
   - Coverage for common queries
   - Missing or excessive indexes
   
6. **Constraints**
   - NOT NULL where appropriate
   - CHECK constraints for validation
   - UNIQUE constraints
   
7. **Scalability**
   - Partitioning needs
   - Sharding considerations
   
8. **Naming Conventions**
   - Consistency
   - Clarity

Rate each area: 🟢 Good | 🟡 Needs attention | 🔴 Critical issue
```

### Prompt: Normalization Analysis
```text
Analyze normalization of this schema:

{{SCHEMA}}

Check for:
1. **1NF violations**
   - Repeating groups
   - Multi-valued columns
   - Non-atomic values
   
2. **2NF violations**
   - Partial dependencies
   - Columns depending on part of composite key
   
3. **3NF violations**
   - Transitive dependencies
   - Non-key columns depending on other non-key columns
   
4. **Denormalization assessment**
   - Is intentional denormalization justified?
   - What are the trade-offs?

Provide specific examples and recommended fixes.
```

### Prompt: Data Type Review
```text
Review data type choices in this schema:

{{SCHEMA}}

Database: {{DATABASE_TYPE}}

Check for:
1. **Numeric types**
   - INT vs BIGINT (do you need 2B+ rows?)
   - DECIMAL vs FLOAT for money
   - Appropriate precision/scale
   
2. **String types**
   - VARCHAR length appropriateness
   - CHAR vs VARCHAR
   - TEXT for large content
   
3. **Date/Time types**
   - DATE vs DATETIME vs TIMESTAMP
   - Timezone handling
   
4. **Special types**
   - UUID storage (native vs CHAR(36))
   - JSON/JSONB usage
   - ENUM appropriateness
   - Boolean representation
   
5. **Consistency**
   - Same data, same type across tables
   - ID columns match FK columns

Provide migration SQL for recommended changes.
```

### Prompt: Relationship Design Review
```text
Review relationships in this schema:

{{SCHEMA}}

Check for:
1. **Missing relationships**
   - Columns that should be FKs
   - Implicit relationships not enforced
   
2. **Relationship types**
   - 1:1 — should these be merged?
   - 1:N — correct direction?
   - M:N — proper junction table?
   
3. **Cascade behavior**
   - ON DELETE: CASCADE vs SET NULL vs RESTRICT
   - ON UPDATE behavior
   - Orphan data risks
   
4. **Self-referential relationships**
   - Hierarchy handling
   - Circular reference risks
   
5. **Polymorphic associations**
   - Proper implementation
   - Type safety concerns

Provide ER diagram and recommendations.
```

### Prompt: Performance-Oriented Review
```text
Review this schema for query performance:

{{SCHEMA}}

Expected queries:
{{QUERIES}}

Data volumes:
{{VOLUMES}}

Analyze:
1. **Index strategy**
   - Indexes for WHERE clauses
   - Indexes for JOINs
   - Indexes for ORDER BY
   - Covering index opportunities
   
2. **Join efficiency**
   - FK indexes present
   - Join column types match
   - Excessive joins needed?
   
3. **Query patterns**
   - Hot tables / columns
   - Aggregation needs
   - Full-text search needs
   
4. **Partitioning**
   - Time-based partitioning
   - Range partitioning
   - Archive strategy
   
5. **Denormalization candidates**
   - Frequently joined data
   - Computed columns
   - Materialized views

Provide recommended indexes and changes.
```

### Prompt: Scalability Review
```text
Review schema for scalability:

{{SCHEMA}}

Growth expectations:
- Current size: {{CURRENT}}
- 1 year: {{YEAR_1}}
- 3 years: {{YEAR_3}}
- Peak concurrent users: {{USERS}}

Evaluate:
1. **Vertical scaling limits**
   - Table size concerns
   - Index size concerns
   
2. **Horizontal scaling readiness**
   - Sharding key candidates
   - Cross-shard query needs
   - Global vs local indexes
   
3. **Partitioning strategy**
   - Partition key selection
   - Partition pruning effectiveness
   - Partition maintenance
   
4. **Hot spots**
   - Tables with high write volume
   - Auto-increment contention
   - Lock contention patterns
   
5. **Archive strategy**
   - Historical data handling
   - Soft delete vs hard delete
   - Data retention policies

Provide scaling recommendations.
```

---

## Design Patterns

### Primary Key Strategies
```sql
-- Auto-increment (simple, but hot spot for inserts)
id BIGINT AUTO_INCREMENT PRIMARY KEY

-- UUID (distributed-friendly, but larger)
id UUID DEFAULT gen_random_uuid() PRIMARY KEY  -- PostgreSQL
id CHAR(36) DEFAULT (UUID()) PRIMARY KEY       -- MySQL 8+

-- ULID/KSUID (sortable, distributed-friendly)
id CHAR(26) PRIMARY KEY  -- Store as string

-- Composite natural key (when appropriate)
PRIMARY KEY (tenant_id, order_number)
```

### Soft Delete Pattern
```sql
-- Simple soft delete
deleted_at TIMESTAMP NULL,
INDEX idx_active (deleted_at) WHERE deleted_at IS NULL  -- Partial index

-- With status
status ENUM('active', 'deleted', 'archived') DEFAULT 'active',
INDEX idx_status (status)

-- Query pattern
SELECT * FROM users WHERE deleted_at IS NULL;
```

### Audit Columns Pattern
```sql
-- Standard audit columns
created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
created_by BIGINT REFERENCES users(id),
updated_by BIGINT REFERENCES users(id)
```

### Multi-Tenancy Patterns
```sql
-- Column-based (shared tables)
tenant_id BIGINT NOT NULL,
INDEX idx_tenant (tenant_id),
-- All queries must include: WHERE tenant_id = ?

-- Schema-based (separate schemas per tenant)
CREATE SCHEMA tenant_123;
CREATE TABLE tenant_123.users (...);

-- Database-based (separate databases)
-- Managed at application/connection level
```

### Hierarchical Data Patterns
```sql
-- Adjacency List (simple, recursive queries needed)
parent_id BIGINT REFERENCES categories(id)

-- Nested Sets (fast reads, slow writes)
lft INT NOT NULL,
rgt INT NOT NULL,
INDEX idx_nested (lft, rgt)

-- Materialized Path (good balance)
path VARCHAR(255) NOT NULL,  -- e.g., '/1/5/12/'
INDEX idx_path (path)

-- Closure Table (most flexible)
CREATE TABLE category_paths (
    ancestor_id BIGINT,
    descendant_id BIGINT,
    depth INT,
    PRIMARY KEY (ancestor_id, descendant_id)
);
```

### Polymorphic Association Patterns
```sql
-- Separate FK columns (most explicit)
commentable_post_id BIGINT REFERENCES posts(id),
commentable_article_id BIGINT REFERENCES articles(id),
CHECK (
    (commentable_post_id IS NOT NULL)::int +
    (commentable_article_id IS NOT NULL)::int = 1
)

-- Type + ID (flexible but no FK enforcement)
commentable_type VARCHAR(50) NOT NULL,
commentable_id BIGINT NOT NULL,
INDEX idx_commentable (commentable_type, commentable_id)

-- Separate tables (cleanest)
CREATE TABLE post_comments (...);
CREATE TABLE article_comments (...);
```

---

## Anti-Patterns to Avoid

### ❌ Entity-Attribute-Value (EAV)
```sql
-- Avoid this pattern
CREATE TABLE attributes (
    entity_id BIGINT,
    attribute_name VARCHAR(100),
    attribute_value TEXT
);
-- Problems: No type safety, hard to query, poor performance

-- Better: JSONB for flexible schema
CREATE TABLE entities (
    id BIGINT PRIMARY KEY,
    data JSONB NOT NULL
);
```

### ❌ Storing Lists in Strings
```sql
-- Avoid
tags VARCHAR(255)  -- "tag1,tag2,tag3"

-- Better: Junction table
CREATE TABLE item_tags (
    item_id BIGINT REFERENCES items(id),
    tag_id BIGINT REFERENCES tags(id),
    PRIMARY KEY (item_id, tag_id)
);

-- Or array type (PostgreSQL)
tags TEXT[] NOT NULL DEFAULT '{}'
```

### ❌ Overloaded Columns
```sql
-- Avoid: status meaning different things
status INT  -- 1=active, 2=deleted, 3=pending, 4=special_active...

-- Better: Separate concerns
is_active BOOLEAN DEFAULT true,
is_deleted BOOLEAN DEFAULT false,
approval_status ENUM('pending', 'approved', 'rejected')
```

### ❌ Missing Foreign Keys
```sql
-- Avoid: Implicit relationships
user_id BIGINT  -- No FK, data can become orphaned

-- Better: Explicit enforcement
user_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE
```

---

## Review Checklist

### Data Integrity
- [ ] All relationships have FKs
- [ ] Appropriate cascade behavior
- [ ] NOT NULL where data is required
- [ ] CHECK constraints for valid values
- [ ] UNIQUE constraints where needed
- [ ] DEFAULT values make sense

### Performance
- [ ] Primary keys are appropriate
- [ ] Foreign keys are indexed
- [ ] Query patterns have indexes
- [ ] No excessive indexing
- [ ] Data types appropriately sized
- [ ] Partitioning considered for large tables

### Scalability
- [ ] Hot spots identified
- [ ] Sharding strategy considered
- [ ] Archive strategy planned
- [ ] Growth projections analyzed
- [ ] Concurrent access patterns reviewed

### Maintainability
- [ ] Consistent naming conventions
- [ ] Tables are documented
- [ ] Columns have descriptions
- [ ] Relationships are clear
- [ ] Migration path is feasible

---

## Report Template

```markdown
# Schema Design Review — {{SCHEMA_NAME}}

**Date**: {{DATE}}
**Database**: {{DATABASE_TYPE}} {{VERSION}}
**Reviewer**: {{REVIEWER}}

## Summary

| Category | Rating | Issues |
| --- | --- | --- |
| Normalization | 🟢/🟡/🔴 | {{COUNT}} |
| Data Types | 🟢/🟡/🔴 | {{COUNT}} |
| Relationships | 🟢/🟡/🔴 | {{COUNT}} |
| Indexes | 🟢/🟡/🔴 | {{COUNT}} |
| Constraints | 🟢/🟡/🔴 | {{COUNT}} |
| Scalability | 🟢/🟡/🔴 | {{COUNT}} |

## Critical Issues

### Issue 1: {{TITLE}}
- **Table**: {{TABLE}}
- **Problem**: {{DESCRIPTION}}
- **Impact**: {{IMPACT}}
- **Fix**: {{RECOMMENDATION}}
```sql
{{FIX_SQL}}
```

## Recommendations

### High Priority
1. {{RECOMMENDATION}}

### Medium Priority
1. {{RECOMMENDATION}}

### Low Priority / Future
1. {{RECOMMENDATION}}

## ER Diagram

```mermaid
{{DIAGRAM}}
```
```

# Database Agents — AI Development Instructions

> **Purpose**: Agent instructions for database-related development tasks  
> **Best For**: Copilot, Cursor, Windsurf, Claude Agents  
> **Scope**: Schema design, queries, migrations, optimization  
> **Last Updated**: 2026-03

---

## Overview

This file contains instructions for AI coding agents working on database-related tasks. Agents should follow these guidelines when designing schemas, writing queries, creating migrations, and optimizing database performance.

---

## Core Principles

### 1. Safety First
- **Never run destructive operations without confirmation**
- Always provide rollback plans for migrations
- Prefer soft deletes over hard deletes in production schemas
- Use transactions for multi-statement operations

### 2. Performance Awareness
- Consider query plans and index usage
- Account for table sizes when suggesting operations
- Prefer set-based operations over loops
- Be aware of N+1 query patterns

### 3. Data Integrity
- Enforce constraints at the database level
- Use appropriate data types for the domain
- Design for referential integrity
- Consider NULL handling carefully

---

## Agent Capabilities

### Schema Design Tasks

When asked to design a database schema:

```markdown
1. **Gather requirements first**
   - What entities need to be stored?
   - What are the relationships between entities?
   - What queries will be most common?
   - What is the expected data volume?

2. **Apply normalization appropriately**
   - Start with 3NF as baseline
   - Denormalize only with justification
   - Document denormalization decisions

3. **Define constraints**
   - Primary keys (prefer UUIDs or identity columns)
   - Foreign keys with appropriate ON DELETE behavior
   - NOT NULL where required
   - UNIQUE constraints for natural keys
   - CHECK constraints for domain validation

4. **Plan for indexing**
   - Primary key indexes (automatic)
   - Foreign key indexes (often forgotten)
   - Indexes for frequent WHERE clauses
   - Composite indexes for common query patterns
```

### Query Optimization Tasks

When asked to optimize queries:

```markdown
1. **Request the query plan**
   - EXPLAIN ANALYZE for PostgreSQL
   - EXPLAIN with actual timings for MySQL
   - Identify sequential scans on large tables

2. **Check index usage**
   - Are relevant indexes being used?
   - Are there missing indexes?
   - Are there redundant indexes?

3. **Analyze query patterns**
   - Look for N+1 patterns
   - Check for unnecessary columns in SELECT
   - Review JOIN order and types
   - Identify opportunities for query restructuring

4. **Consider data distribution**
   - Index selectivity
   - NULL distribution
   - Hot spots in data
```

### Migration Tasks

When asked to create migrations:

```markdown
1. **Assess risk level**
   - Table size and row count
   - Current production load
   - Lock implications
   - Backward compatibility

2. **Plan for zero-downtime** (when required)
   - Use expand-contract pattern for breaking changes
   - Create indexes concurrently
   - Add columns as nullable first
   - Plan multi-phase deployments

3. **Include rollback plan**
   - Document exact rollback steps
   - Test rollback in non-production
   - Consider data preservation needs

4. **Add validation queries**
   - Pre-migration checks
   - Post-migration verification
   - Data integrity validation
```

---

## Database-Specific Guidelines

### PostgreSQL

```markdown
**Prefer:**
- `SERIAL` or `BIGSERIAL` for auto-increment (or `IDENTITY` in PG 10+)
- `TIMESTAMPTZ` over `TIMESTAMP` for time data
- `TEXT` over `VARCHAR` when length doesn't matter
- `JSONB` over `JSON` for JSON data
- `CREATE INDEX CONCURRENTLY` for production
- `ALTER TABLE ... NOT VALID` then `VALIDATE CONSTRAINT` for FKs
- CTEs for complex queries (readable, often optimized)
- `FOR UPDATE SKIP LOCKED` for queue patterns

**Avoid:**
- `SERIAL` as primary key for distributed systems (use UUID)
- `SELECT *` in production code
- Storing arrays that need to be queried (normalize instead)
- Large transactions that hold locks
```

### MySQL

```markdown
**Prefer:**
- `BIGINT AUTO_INCREMENT` for primary keys
- `DATETIME(6)` for microsecond precision
- `utf8mb4` character set for Unicode
- `InnoDB` engine (default in modern MySQL)
- `ALGORITHM=INSTANT` or `INPLACE` for DDL
- Covering indexes for frequent queries

**Avoid:**
- `ENUM` for values that may change
- `FLOAT`/`DOUBLE` for financial data (use `DECIMAL`)
- Large `TEXT`/`BLOB` columns in frequently accessed tables
- Implicit type conversions in WHERE clauses
```

### MongoDB

```markdown
**Prefer:**
- Embedding for one-to-few relationships
- Referencing for one-to-many with independent access
- Compound indexes following ESR rule (Equality, Sort, Range)
- Schema validation for critical collections
- Appropriate shard keys for scaled deployments

**Avoid:**
- Unbounded array growth
- Documents approaching 16MB limit
- $lookup in high-frequency queries (denormalize instead)
- Monotonically increasing shard keys
```

### Redis

```markdown
**Prefer:**
- Appropriate data structures (Hash, Set, Sorted Set, etc.)
- Key namespacing with colons (e.g., `user:1001:profile`)
- TTL on all cache keys
- Pipeline for multiple operations
- Lua scripts for atomic operations

**Avoid:**
- Keys without expiration in cache scenarios
- Large values (>1MB)
- Blocking operations in main application thread
- Single large sorted set for leaderboards (partition instead)
```

---

## Code Generation Patterns

### Entity/Model Generation

When generating database models, include:

```python
# Example: Python SQLAlchemy model
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "users"
    
    # Primary key
    id = Column(Integer, primary_key=True)
    
    # Required fields with constraints
    email = Column(String(255), nullable=False, unique=True)
    name = Column(String(255), nullable=False)
    
    # Optional fields
    phone = Column(String(20), nullable=True)
    
    # Timestamps (always include these)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Soft delete
    deleted_at = Column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    orders = relationship("Order", back_populates="user")
    
    # Indexes
    __table_args__ = (
        Index("idx_users_email", "email"),
        Index("idx_users_created_at", "created_at"),
    )
```

### Query Generation

When generating queries, include:

```sql
-- Include comments explaining the query purpose
-- Get active users who have placed orders in the last 30 days

SELECT DISTINCT
    u.id,
    u.email,
    u.name,
    COUNT(o.id) AS order_count,
    SUM(o.total) AS total_spent
FROM users u
INNER JOIN orders o ON o.user_id = u.id
WHERE 
    u.deleted_at IS NULL  -- Respect soft deletes
    AND o.created_at >= NOW() - INTERVAL '30 days'
    AND o.status = 'completed'
GROUP BY u.id, u.email, u.name
HAVING COUNT(o.id) >= 1
ORDER BY total_spent DESC
LIMIT 100;

-- Index recommendation:
-- CREATE INDEX idx_orders_user_created ON orders(user_id, created_at) WHERE status = 'completed';
```

### Migration Generation

When generating migrations, include:

```sql
-- Migration: Add phone column to users
-- Author: AI Agent
-- Date: 2026-01-15
-- Risk: LOW (nullable column addition)
-- Rollback: ALTER TABLE users DROP COLUMN phone;

-- Pre-check: Verify column doesn't exist
SELECT column_name 
FROM information_schema.columns 
WHERE table_name = 'users' AND column_name = 'phone';
-- Expected: 0 rows

-- Migration
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Post-check: Verify column exists
SELECT column_name, data_type, is_nullable 
FROM information_schema.columns 
WHERE table_name = 'users' AND column_name = 'phone';
-- Expected: phone, character varying, YES
```

---

## Response Patterns

### When Designing Schemas

```markdown
## Schema Design: [Feature Name]

### Requirements Summary
- [Requirement 1]
- [Requirement 2]

### Entities
| Entity | Description | Key Fields |
|--------|-------------|------------|
| | | |

### Schema Definition
```sql
[CREATE TABLE statements]
```

### Indexes
```sql
[CREATE INDEX statements]
```

### Sample Queries
```sql
[Common queries this schema supports]
```

### Trade-offs
- [Trade-off 1 and rationale]
- [Trade-off 2 and rationale]
```

### When Reviewing Queries

```markdown
## Query Review

### Original Query
```sql
[Original query]
```

### Issues Found
1. [Issue 1 - severity]
2. [Issue 2 - severity]

### Query Plan Analysis
- Current: [Sequential scan / Index scan]
- Missing indexes: [List]
- Estimated rows vs actual: [Comparison]

### Optimized Query
```sql
[Optimized query]
```

### Recommended Indexes
```sql
[Index creation statements]
```

### Expected Improvement
- Before: [metrics]
- After: [metrics]
```

### When Creating Migrations

```markdown
## Migration Plan: [Description]

### Risk Assessment
- Risk Level: [Low/Medium/High/Critical]
- Table Size: [row count]
- Lock Type: [None/Share/Exclusive]
- Estimated Duration: [time]
- Backward Compatible: [Yes/No]

### Pre-Migration Checklist
- [ ] Backup verified
- [ ] Validation queries prepared
- [ ] Rollback tested
- [ ] Application code ready (if needed)

### Migration SQL
```sql
[Migration statements]
```

### Rollback SQL
```sql
[Rollback statements]
```

### Validation Queries
```sql
[Pre and post validation]
```
```

---

## Error Handling

When encountering database errors, provide:

```markdown
1. **Error interpretation** - What the error means
2. **Common causes** - Why this typically happens
3. **Resolution steps** - How to fix it
4. **Prevention** - How to avoid in the future
```

Example:

```markdown
### Error: deadlock detected

**Interpretation:** Two or more transactions are waiting for each other to release locks.

**Common Causes:**
- Concurrent updates to the same rows in different order
- Long-running transactions holding locks
- Missing indexes causing table-level locks

**Resolution:**
1. Retry the transaction (most applications should handle this)
2. Review transaction scope and reduce duration
3. Consider using `SELECT FOR UPDATE SKIP LOCKED` for queue patterns

**Prevention:**
- Keep transactions short
- Access tables in consistent order
- Use appropriate isolation levels
- Add proper indexes to avoid escalation to table locks
```

---

## Integration with Other Prompts

Reference these related prompts for specific tasks:

| Task | Prompt |
|------|--------|
| PostgreSQL optimization | [postgresql-optimization.md](postgresql-optimization.md) |
| MySQL optimization | [mysql-optimization.md](mysql-optimization.md) |
| MongoDB patterns | [nosql-mongodb.md](nosql-mongodb.md) |
| Redis patterns | [redis-patterns.md](redis-patterns.md) |
| Migration safety | [migrations-safety.md](migrations-safety.md) |
| Schema design | [schema-design-review.md](schema-design-review.md) |

---

## Quality Checklist

Before completing any database task, verify:

```markdown
- [ ] Schema follows naming conventions
- [ ] Appropriate data types used
- [ ] Constraints defined (PK, FK, NOT NULL, UNIQUE)
- [ ] Indexes planned for query patterns
- [ ] Timestamps included (created_at, updated_at)
- [ ] Soft delete considered (deleted_at)
- [ ] Migration is backward compatible (or documented otherwise)
- [ ] Rollback plan provided
- [ ] Validation queries included
- [ ] Performance implications considered
```

---

*Last updated: 2026-01*

## Repository Standards

- Prompt standard: [docs/prompt-standards.md](../docs/prompt-standards.md)
- QA checks: run `bash scripts/qa/run_docs_qa.sh` from repo root.
- Codex skill: [skills/codex-pgp/SKILL.md](../skills/codex-pgp/SKILL.md)
- ClaudeAI skill: [skills/claudeai-pgp/SKILL.md](../skills/claudeai-pgp/SKILL.md)

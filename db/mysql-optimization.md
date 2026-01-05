# MySQL Optimization — Performance & Query Tuning

> **Purpose**: Optimize MySQL queries, indexes, and schema design  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Databases**: MySQL, MariaDB  
> **Last Updated**: 2025-12

---

## Mission

Help identify and resolve **MySQL performance issues** through query optimization, proper indexing, schema improvements, and configuration tuning. Focus on practical improvements with measurable performance gains.

---

## Guard Clauses

**If no query or schema provided:**
```
NO_DATABASE_CONTEXT

Please provide database context to analyze:
- Slow queries or EXPLAIN output
- Table schema (SHOW CREATE TABLE)
- Current indexes
- Or describe the performance issue
```

**If query is already optimized:**
```
QUERY_OPTIMIZED

✅ Query analysis complete — no major optimizations needed.

Checks performed:
- Index usage: ✓ (using appropriate indexes)
- Join efficiency: ✓ (optimal join order)
- WHERE clause: ✓ (sargable conditions)
- SELECT fields: ✓ (no unnecessary columns)
- Subqueries: ✓ (efficient or converted to JOINs)

Query is well-optimized for current schema.
```

---

## Quick Context Checklist

```
☐ Slow query or queries
☐ EXPLAIN / EXPLAIN ANALYZE output
☐ Table schemas (SHOW CREATE TABLE)
☐ Current indexes
☐ Table sizes (approximate row counts)
☐ MySQL version
☐ Current performance metrics
```

---

## Copy-Paste Optimization Prompts

### Prompt: Query Performance Analysis
```text
Analyze this MySQL query for performance:

Query:
{{QUERY}}

EXPLAIN output:
{{EXPLAIN_OUTPUT}}

Table schema:
{{SCHEMA}}

Row counts: {{ROW_COUNTS}}

Identify:
1. Missing indexes (full table scans)
2. Inefficient joins (wrong join type, bad order)
3. Non-sargable WHERE conditions
4. Unnecessary columns in SELECT
5. Subquery vs JOIN opportunities
6. LIMIT/OFFSET pagination issues
7. Function calls preventing index use

Provide:
- Current bottleneck explanation
- Optimized query
- Recommended indexes (with CREATE INDEX statements)
- Expected improvement
```

### Prompt: Index Optimization
```text
Optimize indexes for these tables:

Schemas:
{{SCHEMAS}}

Common queries:
{{QUERIES}}

Current indexes:
{{INDEXES}}

Analyze:
1. Missing indexes for WHERE/JOIN/ORDER BY
2. Redundant indexes (covered by others)
3. Unused indexes (candidates for removal)
4. Composite index column order
5. Covering indexes opportunities
6. Index cardinality issues

Output:
| Table | Action | Index | Columns | Reason |
| --- | --- | --- | --- | --- |
| users | ADD | idx_email | (email) | WHERE clause |
| users | DROP | idx_old | (col) | Redundant |

Include CREATE INDEX and DROP INDEX statements.
```

### Prompt: Schema Design Review
```text
Review this MySQL schema design:

{{SCHEMA}}

Use case: {{USE_CASE}}
Expected scale: {{SCALE}}

Check for:
1. Normalization issues (over/under normalized)
2. Data type choices (VARCHAR vs TEXT, INT sizes)
3. Primary key design (natural vs surrogate)
4. Foreign key relationships
5. NULL vs DEFAULT handling
6. Character set and collation
7. Partitioning opportunities
8. Storage engine choice (InnoDB vs others)

Provide:
- Issues found with severity
- Recommended changes
- Migration path for changes
```

### Prompt: Slow Query Log Analysis
```text
Analyze these slow queries from the log:

{{SLOW_QUERY_LOG}}

For each query:
1. Identify why it's slow
2. Check for common anti-patterns
3. Suggest optimization
4. Estimate improvement

Prioritize by:
- Frequency (queries per hour)
- Impact (total time consumed)
- Fix complexity

Output top 10 recommendations with specific fixes.
```

### Prompt: JOIN Optimization
```text
Optimize this JOIN query:

{{QUERY}}

Table sizes:
{{TABLE_SIZES}}

Current indexes:
{{INDEXES}}

Analyze:
1. Join order (smallest result set first)
2. Join type (nested loop vs hash vs merge)
3. Index availability for join columns
4. Filtering before vs after join
5. Derived table opportunities
6. EXISTS vs IN vs JOIN choices

Provide optimized query with explanation.
```

### Prompt: Pagination Optimization
```text
Optimize pagination for this query:

{{QUERY}}

Current approach: LIMIT {{LIMIT}} OFFSET {{OFFSET}}
Total rows: {{TOTAL}}
Page size: {{PAGE_SIZE}}

Problems with current approach:
- OFFSET scans and discards rows
- Performance degrades with higher pages

Suggest alternatives:
1. Keyset/cursor pagination
2. Deferred join technique
3. Covering index approach
4. Caching strategies

Provide implementation for best approach.
```

---

## Analysis Techniques

### Reading EXPLAIN Output
```text
Key columns to check:
- type: ALL (bad) → index → range → ref → eq_ref → const (best)
- key: Which index is used (NULL = no index)
- rows: Estimated rows examined (lower is better)
- Extra: 
  - "Using filesort" = needs optimization
  - "Using temporary" = needs optimization
  - "Using index" = good (covering index)
  - "Using where" = filtering after fetch
```

### Index Selection Rules
```text
1. Columns in WHERE with = conditions first
2. Columns in WHERE with range conditions next
3. Columns in ORDER BY last
4. Consider query frequency and write impact
5. Composite indexes: most selective column first
6. Don't index low-cardinality columns alone
```

### Query Anti-Patterns
```text
❌ SELECT * (fetch only needed columns)
❌ OR conditions (consider UNION)
❌ Functions on indexed columns: WHERE YEAR(date) = 2024
❌ Leading wildcards: WHERE name LIKE '%smith'
❌ Implicit type conversion
❌ NOT IN with NULLs
❌ Large OFFSET pagination
❌ Correlated subqueries (convert to JOIN)
```

---

## Common Optimization Patterns

### Convert OR to UNION
```sql
-- Before (can't use index efficiently)
SELECT * FROM users WHERE status = 'active' OR role = 'admin';

-- After (uses indexes on both)
SELECT * FROM users WHERE status = 'active'
UNION
SELECT * FROM users WHERE role = 'admin';
```

### Keyset Pagination
```sql
-- Before (slow for large offsets)
SELECT * FROM posts ORDER BY created_at DESC LIMIT 20 OFFSET 10000;

-- After (fast regardless of page)
SELECT * FROM posts 
WHERE created_at < '2024-01-15 10:30:00'
ORDER BY created_at DESC 
LIMIT 20;
```

### Covering Index
```sql
-- Query only needs these columns
SELECT id, email, status FROM users WHERE status = 'active';

-- Covering index includes all columns
CREATE INDEX idx_status_covering ON users (status, id, email);
-- Now query is satisfied entirely from index
```

### Deferred Join
```sql
-- Before (fetches all columns then sorts/limits)
SELECT * FROM posts ORDER BY created_at DESC LIMIT 20 OFFSET 1000;

-- After (finds IDs first, then fetches)
SELECT p.* FROM posts p
INNER JOIN (
  SELECT id FROM posts ORDER BY created_at DESC LIMIT 20 OFFSET 1000
) AS tmp ON p.id = tmp.id;
```

---

## Diagnostic Commands

```sql
-- Show query execution plan
EXPLAIN SELECT ...;
EXPLAIN ANALYZE SELECT ...;  -- MySQL 8.0.18+

-- Show table structure and indexes
SHOW CREATE TABLE table_name;
SHOW INDEX FROM table_name;

-- Check index usage statistics
SELECT * FROM sys.schema_index_statistics 
WHERE table_schema = 'your_db';

-- Find unused indexes
SELECT * FROM sys.schema_unused_indexes;

-- Show running queries
SHOW PROCESSLIST;
SHOW FULL PROCESSLIST;

-- Table statistics
SHOW TABLE STATUS LIKE 'table_name';

-- InnoDB status
SHOW ENGINE INNODB STATUS;

-- Current configuration
SHOW VARIABLES LIKE 'innodb%';
SHOW VARIABLES LIKE 'query_cache%';
```

---

## Configuration Tuning

### Key Parameters
```ini
# InnoDB Buffer Pool (50-70% of RAM for dedicated server)
innodb_buffer_pool_size = 4G

# Log file size (larger = better write performance)
innodb_log_file_size = 256M

# Flush behavior (2 = good balance of safety/performance)
innodb_flush_log_at_trx_commit = 2

# Query cache (disabled by default in 8.0+)
query_cache_type = 0

# Temp tables
tmp_table_size = 64M
max_heap_table_size = 64M

# Connections
max_connections = 200

# Sort and join buffers
sort_buffer_size = 4M
join_buffer_size = 4M
```

---

## Report Template

```markdown
# MySQL Optimization Report — {{DATABASE}}

**Date**: {{DATE}}
**Analyzed**: {{QUERY_COUNT}} queries, {{TABLE_COUNT}} tables

## Executive Summary
- Critical issues: {{COUNT}}
- Estimated performance gain: {{PERCENTAGE}}
- Priority fixes: {{TOP_3}}

## Query Optimizations
| Query | Issue | Fix | Impact |
| --- | --- | --- | --- |

## Index Recommendations
| Table | Action | Index | Reason |
| --- | --- | --- | --- |

## Schema Improvements
{{SCHEMA_RECOMMENDATIONS}}

## Configuration Changes
{{CONFIG_RECOMMENDATIONS}}

## Implementation Order
1. {{FIRST_PRIORITY}}
2. {{SECOND_PRIORITY}}
3. {{THIRD_PRIORITY}}
```

---

## Best Practices

### Query Writing
- Select only needed columns
- Use appropriate JOIN types
- Filter early in the query
- Avoid functions on indexed columns
- Use prepared statements
- Consider query result caching

### Index Management
- Index foreign keys
- Review indexes quarterly
- Monitor index usage
- Remove unused indexes
- Update statistics regularly

### Monitoring
- Enable slow query log
- Set appropriate long_query_time
- Use Performance Schema
- Monitor buffer pool hit rate
- Track query patterns over time

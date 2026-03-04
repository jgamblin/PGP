# PostgreSQL Optimization — Performance & Query Tuning

> **Purpose**: Optimize PostgreSQL queries, indexes, and schema design  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Database design, query optimization, migrations, and data operations  
> **Last Updated**: 2026-03
> **Databases**: PostgreSQL  

---

## Mission

Help identify and resolve **PostgreSQL performance issues** through query optimization, proper indexing, schema improvements, and configuration tuning. Focus on practical improvements leveraging PostgreSQL's advanced features.

---

## Guard Clauses

**If no query or schema provided:**
```
NO_DATABASE_CONTEXT

Please provide database context to analyze:
- Slow queries or EXPLAIN ANALYZE output
- Table schema (\d+ table_name)
- Current indexes
- Or describe the performance issue
```

**If query is already optimized:**
```
QUERY_OPTIMIZED

✅ Query analysis complete — no major optimizations needed.

Checks performed:
- Index usage: ✓ (using appropriate indexes)
- Join strategy: ✓ (optimal plan chosen)
- WHERE clause: ✓ (sargable conditions)
- SELECT fields: ✓ (no unnecessary columns)
- Seq scans: ✓ (appropriate for data size)

Query is well-optimized for current schema.
```

---

## Quick Context Checklist

```
☐ Slow query or queries
☐ EXPLAIN (ANALYZE, BUFFERS) output
☐ Table schemas (\d+ table_name)
☐ Current indexes
☐ Table sizes (pg_relation_size)
☐ PostgreSQL version
☐ Current performance metrics
```

---

## Copy-Paste Optimization Prompts

### Prompt: Query Performance Analysis
```text
Analyze this PostgreSQL query for performance:

Query:
{{QUERY}}

EXPLAIN (ANALYZE, BUFFERS) output:
{{EXPLAIN_OUTPUT}}

Table schema:
{{SCHEMA}}

Row counts: {{ROW_COUNTS}}

Identify:
1. Sequential scans on large tables
2. Inefficient join strategies
3. Missing or unused indexes
4. Poor statistics (row estimate vs actual)
5. Excessive buffer usage
6. Sort and hash operations in memory vs disk
7. CTE materialization issues (PostgreSQL 12+)

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
1. Missing B-tree indexes for equality/range
2. GIN indexes for array/JSONB/full-text
3. GiST indexes for geometric/range types
4. BRIN indexes for naturally ordered data
5. Partial indexes for filtered queries
6. Expression indexes for computed values
7. Covering indexes (INCLUDE clause)
8. Redundant/unused indexes

Output:
| Table | Action | Index Type | Columns | Reason |
| --- | --- | --- | --- | --- |
| users | ADD | B-tree | (email) | WHERE clause |
| logs | ADD | BRIN | (created_at) | Time-series data |

Include CREATE INDEX CONCURRENTLY statements.
```

### Prompt: Schema Design Review
```text
Review this PostgreSQL schema design:

{{SCHEMA}}

Use case: {{USE_CASE}}
Expected scale: {{SCALE}}

Check for:
1. Data type choices (use appropriate sizes)
2. JSONB vs normalized tables
3. Array columns vs junction tables
4. Primary key design (UUID vs SERIAL vs IDENTITY)
5. Foreign key constraints and cascades
6. CHECK constraints for data integrity
7. Partitioning strategy (range, list, hash)
8. Table inheritance vs partitioning
9. ENUM types vs lookup tables

Provide:
- Issues found with severity
- Recommended changes with PostgreSQL-specific features
- Migration path for changes
```

### Prompt: JSONB Query Optimization
```text
Optimize queries on this JSONB column:

Table schema:
{{SCHEMA}}

JSONB structure example:
{{JSONB_EXAMPLE}}

Queries:
{{QUERIES}}

Analyze:
1. GIN index opportunities (jsonb_ops vs jsonb_path_ops)
2. Expression indexes for frequently accessed paths
3. Query operator choices (@>, ?, ?&, ?|, @?)
4. JSONB vs JSON performance
5. Extraction and casting efficiency
6. Containment vs existence checks

Provide optimized queries and appropriate indexes.
```

### Prompt: CTE and Subquery Optimization
```text
Optimize this query with CTEs/subqueries:

{{QUERY}}

PostgreSQL version: {{VERSION}}

Check for:
1. CTE materialization (pre-12 always materialized)
2. NOT MATERIALIZED hint opportunities (12+)
3. Correlated subqueries to lateral joins
4. Subquery to CTE conversion benefits
5. Recursive CTE efficiency
6. Window functions vs self-joins

Provide optimized query with explanation.
```

### Prompt: Partitioning Strategy
```text
Design partitioning strategy for this table:

{{SCHEMA}}

Data characteristics:
- Total rows: {{TOTAL_ROWS}}
- Growth rate: {{GROWTH_RATE}}
- Query patterns: {{QUERY_PATTERNS}}
- Retention policy: {{RETENTION}}

Recommend:
1. Partition type (range, list, hash)
2. Partition key selection
3. Partition granularity
4. Partition maintenance strategy
5. Index strategy for partitioned table
6. Query modifications needed

Provide DDL for partitioned table and maintenance scripts.
```

---

## PostgreSQL-Specific Features

### Advanced Index Types
```sql
-- B-tree (default, equality and range)
CREATE INDEX idx_email ON users (email);

-- GIN for JSONB containment
CREATE INDEX idx_data ON events USING GIN (data);

-- GIN with jsonb_path_ops (smaller, @> only)
CREATE INDEX idx_data ON events USING GIN (data jsonb_path_ops);

-- GiST for range types and geometric
CREATE INDEX idx_period ON reservations USING GiST (period);

-- BRIN for naturally ordered large tables
CREATE INDEX idx_created ON logs USING BRIN (created_at);

-- Partial index (only index active users)
CREATE INDEX idx_active_email ON users (email) WHERE status = 'active';

-- Expression index
CREATE INDEX idx_lower_email ON users (LOWER(email));

-- Covering index (PostgreSQL 11+)
CREATE INDEX idx_user_lookup ON users (email) INCLUDE (name, status);
```

### EXPLAIN Analysis
```text
Key things to look for:
- Seq Scan on large tables (needs index?)
- Rows vs actual rows (statistics outdated?)
- Buffers: shared hit vs read (cache effectiveness)
- Sort Method: external merge (needs more work_mem)
- Hash Batch/Buckets (memory pressure)
- actual time: first row vs total (where is time spent?)
```

### Query Optimization Patterns
```sql
-- Use ANY instead of IN for parameter lists
SELECT * FROM users WHERE id = ANY(ARRAY[1, 2, 3, 4, 5]);

-- LATERAL joins for correlated subqueries
SELECT u.*, latest_order.*
FROM users u
CROSS JOIN LATERAL (
  SELECT * FROM orders 
  WHERE user_id = u.id 
  ORDER BY created_at DESC 
  LIMIT 1
) latest_order;

-- Window functions instead of self-joins
SELECT *, 
  LAG(value) OVER (PARTITION BY user_id ORDER BY date) as prev_value
FROM metrics;

-- FILTER clause for conditional aggregates
SELECT 
  COUNT(*) as total,
  COUNT(*) FILTER (WHERE status = 'active') as active_count
FROM users;
```

---

## Diagnostic Commands

```sql
-- Detailed query plan
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) SELECT ...;

-- Table and index sizes
SELECT 
  relname,
  pg_size_pretty(pg_relation_size(oid)) as size,
  pg_size_pretty(pg_indexes_size(oid)) as index_size
FROM pg_class 
WHERE relkind = 'r'
ORDER BY pg_relation_size(oid) DESC;

-- Index usage statistics
SELECT 
  schemaname, tablename, indexname,
  idx_scan, idx_tup_read, idx_tup_fetch
FROM pg_stat_user_indexes
ORDER BY idx_scan ASC;

-- Unused indexes
SELECT indexrelname, idx_scan
FROM pg_stat_user_indexes
WHERE idx_scan = 0 AND indexrelname NOT LIKE '%_pkey';

-- Table statistics
SELECT * FROM pg_stat_user_tables;

-- Cache hit ratio
SELECT 
  sum(heap_blks_hit) / (sum(heap_blks_hit) + sum(heap_blks_read)) as ratio
FROM pg_statio_user_tables;

-- Currently running queries
SELECT pid, now() - pg_stat_activity.query_start AS duration, query
FROM pg_stat_activity
WHERE state = 'active';

-- Blocking queries
SELECT blocked.pid, blocked.query, blocking.pid, blocking.query
FROM pg_stat_activity blocked
JOIN pg_stat_activity blocking ON blocking.pid = ANY(pg_blocking_pids(blocked.pid));

-- Update statistics
ANALYZE table_name;
ANALYZE VERBOSE table_name;
```

---

## Configuration Tuning

### Key Parameters
```ini
# Shared buffers (25% of RAM)
shared_buffers = 4GB

# Effective cache size (50-75% of RAM)
effective_cache_size = 12GB

# Work memory (per operation)
work_mem = 64MB

# Maintenance work memory (for VACUUM, CREATE INDEX)
maintenance_work_mem = 512MB

# WAL settings
wal_buffers = 64MB
checkpoint_completion_target = 0.9

# Planner settings
random_page_cost = 1.1  # For SSDs
effective_io_concurrency = 200  # For SSDs

# Parallelism (adjust based on CPU cores)
max_parallel_workers_per_gather = 4
max_parallel_workers = 8
max_worker_processes = 8
```

### Per-Query Tuning
```sql
-- Temporarily increase work_mem for large sorts
SET work_mem = '256MB';
SELECT ... ORDER BY ...;
RESET work_mem;

-- Enable parallel query hints
SET max_parallel_workers_per_gather = 4;
SET parallel_tuple_cost = 0.001;
```

---

## Maintenance Tasks

```sql
-- Update statistics
ANALYZE;
ANALYZE table_name;

-- Reclaim space and update visibility map
VACUUM table_name;
VACUUM (VERBOSE, ANALYZE) table_name;

-- Full vacuum (locks table, use carefully)
VACUUM FULL table_name;

-- Reindex without blocking
REINDEX INDEX CONCURRENTLY idx_name;
REINDEX TABLE CONCURRENTLY table_name;

-- Rebuild all indexes
REINDEX DATABASE CONCURRENTLY dbname;
```

---

## Report Template

```markdown
# PostgreSQL Optimization Report — {{DATABASE}}

**Date**: {{DATE}}
**PostgreSQL Version**: {{VERSION}}
**Analyzed**: {{QUERY_COUNT}} queries, {{TABLE_COUNT}} tables

## Executive Summary
- Critical issues: {{COUNT}}
- Estimated performance gain: {{PERCENTAGE}}
- Priority fixes: {{TOP_3}}

## Query Optimizations
| Query | Issue | Fix | Impact |
| --- | --- | --- | --- |

## Index Recommendations
| Table | Type | Index | Reason |
| --- | --- | --- | --- |

## Schema Improvements
{{SCHEMA_RECOMMENDATIONS}}

## Configuration Changes
{{CONFIG_RECOMMENDATIONS}}

## Maintenance Recommendations
- [ ] ANALYZE frequency
- [ ] VACUUM schedule
- [ ] Partition maintenance

## Implementation Order
1. {{FIRST_PRIORITY}}
2. {{SECOND_PRIORITY}}
3. {{THIRD_PRIORITY}}
```

---

## Best Practices

### Query Writing
- Use EXPLAIN (ANALYZE, BUFFERS) to understand plans
- Leverage PostgreSQL-specific features (LATERAL, window functions)
- Use appropriate operators for JSONB (@>, ?, etc.)
- Consider partial indexes for filtered queries
- Use CTEs wisely (NOT MATERIALIZED when needed)

### Index Management
- Use CONCURRENTLY for production index changes
- Consider BRIN for time-series data
- Remove unused indexes (they slow writes)
- Keep statistics updated (ANALYZE)
- Use covering indexes to avoid heap fetches

### Monitoring
- Track pg_stat_statements for query patterns
- Monitor cache hit ratio
- Watch for sequential scans on large tables
- Check for lock contention
- Review autovacuum effectiveness

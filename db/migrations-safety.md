# Database Migrations — Safety & Zero-Downtime Patterns

> **Purpose**: Safe migration strategies for production databases  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Schema changes, data migrations, rollback strategies, zero-downtime deploys  
> **Last Updated**: 2026-03

---

## Mission

Help design and execute **safe database migrations** that minimize risk, support rollbacks, and enable zero-downtime deployments. Focus on strategies that work across PostgreSQL, MySQL, and other production databases.

---

## Guard Clauses

**If no migration context provided:**
```
NO_MIGRATION_CONTEXT

Please provide context:
- Database type (PostgreSQL, MySQL, etc.)
- Current schema (relevant tables)
- Desired changes
- Data volume (row counts)
- Deployment strategy
- Downtime tolerance

Include constraints and foreign keys if relevant.
```

**If migration is low risk:**
```
MIGRATION_APPROVED

✅ Migration review complete — safe to proceed.

Checks performed:
- Backward compatibility: ✓
- Lock assessment: ✓ (minimal locking)
- Rollback plan: ✓
- Data safety: ✓

Migration follows safe deployment practices.
```

---

## Quick Context Checklist

```
☐ Database type and version
☐ Tables affected
☐ Row counts for affected tables
☐ Current production load
☐ Maintenance window availability
☐ Rollback requirements
☐ Application deployment strategy
☐ Replication setup
```

---

## Copy-Paste Prompts

### Prompt: Review Migration Safety
```text
Review this database migration for safety:

Migration:
{{MIGRATION_SQL_OR_CODE}}

Context:
- Database: {{DATABASE_TYPE}} {{VERSION}}
- Table row counts: {{ROW_COUNTS}}
- Peak traffic: {{TRAFFIC_PATTERNS}}
- Deployment: {{ZERO_DOWNTIME_OR_MAINTENANCE}}

Analyze:
1. Lock duration and type
2. Backward compatibility
3. Rollback complexity
4. Data loss risk
5. Performance impact

Provide:
- Risk assessment (Low/Medium/High/Critical)
- Recommended approach
- Step-by-step execution plan
```

### Prompt: Design Zero-Downtime Migration
```text
Design a zero-downtime migration for:

Current schema:
{{CURRENT_SCHEMA}}

Desired change: {{CHANGE_DESCRIPTION}}

Constraints:
- No application downtime
- Must support rollback
- Table size: {{SIZE}}
- Current traffic: {{TRAFFIC}}

Provide:
1. Migration phases
2. Application code changes needed
3. Rollback procedure
4. Monitoring checkpoints
5. Timeline estimate
```

### Prompt: Plan Data Migration
```text
Plan a data migration:

Source: {{SOURCE_DESCRIPTION}}
Target: {{TARGET_DESCRIPTION}}
Data volume: {{VOLUME}}

Requirements:
- Data consistency: {{REQUIREMENTS}}
- Downtime budget: {{BUDGET}}
- Validation needs: {{VALIDATION}}

Provide:
1. Migration strategy (big bang vs incremental)
2. ETL steps
3. Validation queries
4. Rollback procedure
5. Estimated timeline
```

### Prompt: Create Rollback Plan
```text
Create a rollback plan for:

Migration being deployed:
{{MIGRATION}}

Current state: {{CURRENT_STATE}}
Post-migration state: {{POST_STATE}}

Requirements:
- Maximum rollback time: {{TIME}}
- Data preservation: {{REQUIREMENTS}}

Provide:
1. Pre-migration snapshots needed
2. Rollback SQL/scripts
3. Application considerations
4. Data reconciliation steps
5. Validation queries
```

---

## Zero-Downtime Patterns

### Adding a Column

```sql
-- ✅ SAFE: Adding nullable column (no lock on reads)
-- PostgreSQL
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- MySQL 8.0+ (instant DDL)
ALTER TABLE users ADD COLUMN phone VARCHAR(20), ALGORITHM=INSTANT;

-- ❌ UNSAFE: Adding column with default (full table rewrite in older versions)
-- PostgreSQL <11, MySQL <8.0
ALTER TABLE users ADD COLUMN phone VARCHAR(20) DEFAULT 'N/A';
```

### Adding NOT NULL Column (Multi-Phase)

```sql
-- Phase 1: Add nullable column
ALTER TABLE users ADD COLUMN email_verified BOOLEAN;

-- Phase 2: Backfill data (in batches)
-- Application: Start writing to new column

UPDATE users 
SET email_verified = false 
WHERE email_verified IS NULL 
  AND id BETWEEN 1 AND 10000;
-- Repeat in batches...

-- Phase 3: Add NOT NULL constraint (after all data filled)
ALTER TABLE users ALTER COLUMN email_verified SET NOT NULL;

-- Phase 4: Add default for new rows (PostgreSQL 11+, instant)
ALTER TABLE users ALTER COLUMN email_verified SET DEFAULT false;
```

### Renaming a Column (Expand-Contract)

```sql
-- Phase 1: Add new column
ALTER TABLE users ADD COLUMN full_name VARCHAR(255);

-- Phase 2: Dual-write from application
-- Application code writes to BOTH name AND full_name

-- Phase 3: Backfill existing data
UPDATE users SET full_name = name WHERE full_name IS NULL;
-- Run in batches for large tables

-- Phase 4: Application reads from new column
-- Deploy application to read from full_name

-- Phase 5: Stop writing to old column
-- Deploy application to only write to full_name

-- Phase 6: Drop old column (after verification period)
ALTER TABLE users DROP COLUMN name;
```

### Adding an Index

```sql
-- ✅ SAFE: Concurrent index creation (PostgreSQL)
CREATE INDEX CONCURRENTLY idx_users_email ON users(email);
-- Note: Takes longer, doesn't block writes

-- ✅ SAFE: Online index creation (MySQL 8.0+)
ALTER TABLE users ADD INDEX idx_email (email), ALGORITHM=INPLACE, LOCK=NONE;

-- ❌ UNSAFE: Standard index creation (blocks writes)
CREATE INDEX idx_users_email ON users(email);
```

### Removing a Column

```sql
-- Phase 1: Stop reading from column (application deploy)
-- Phase 2: Stop writing to column (application deploy)  
-- Phase 3: Wait for verification period (1-2 weeks recommended)
-- Phase 4: Drop column

-- PostgreSQL (fast, just marks as dropped)
ALTER TABLE users DROP COLUMN old_field;

-- MySQL (may rewrite table depending on version)
ALTER TABLE users DROP COLUMN old_field, ALGORITHM=INPLACE;
```

### Changing Column Type

```sql
-- ✅ SAFE: Widening type (VARCHAR(50) → VARCHAR(255))
-- Usually instant or very fast
ALTER TABLE users ALTER COLUMN name TYPE VARCHAR(255);

-- ❌ REQUIRES CAUTION: Narrowing or changing type
-- Use expand-contract pattern instead

-- Expand-Contract for type change:
-- 1. Add new column with new type
ALTER TABLE orders ADD COLUMN amount_decimal DECIMAL(10,2);

-- 2. Backfill (in batches)
UPDATE orders SET amount_decimal = amount_int::DECIMAL WHERE id BETWEEN 1 AND 10000;

-- 3. Dual-write from application
-- 4. Switch reads to new column
-- 5. Stop writes to old column
-- 6. Drop old column
```

### Adding Foreign Key

```sql
-- ✅ SAFE: Add FK without validation (fast), then validate
-- PostgreSQL
ALTER TABLE orders 
ADD CONSTRAINT fk_customer 
FOREIGN KEY (customer_id) REFERENCES customers(id) 
NOT VALID;

-- Validate separately (scans table, but doesn't lock)
ALTER TABLE orders VALIDATE CONSTRAINT fk_customer;

-- MySQL (validate existing data first manually)
-- Check for orphans before adding constraint
SELECT o.id FROM orders o 
LEFT JOIN customers c ON o.customer_id = c.id 
WHERE c.id IS NULL;

-- Then add FK
ALTER TABLE orders 
ADD CONSTRAINT fk_customer 
FOREIGN KEY (customer_id) REFERENCES customers(id);
```

---

## Batch Processing Patterns

### Safe Batch Updates

```sql
-- PostgreSQL: Batched update with progress
DO $$
DECLARE
    batch_size INT := 10000;
    affected INT;
BEGIN
    LOOP
        UPDATE users 
        SET status = 'migrated' 
        WHERE id IN (
            SELECT id FROM users 
            WHERE status = 'pending' 
            LIMIT batch_size
            FOR UPDATE SKIP LOCKED
        );
        
        GET DIAGNOSTICS affected = ROW_COUNT;
        
        IF affected = 0 THEN
            EXIT;
        END IF;
        
        RAISE NOTICE 'Updated % rows', affected;
        COMMIT;
        
        -- Optional: Small delay to reduce load
        PERFORM pg_sleep(0.1);
    END LOOP;
END $$;
```

```python
# Python: Batched migration with monitoring
def migrate_in_batches(batch_size: int = 10000):
    total_migrated = 0
    
    while True:
        with db.begin():
            result = db.execute("""
                UPDATE users 
                SET status = 'migrated' 
                WHERE id IN (
                    SELECT id FROM users 
                    WHERE status = 'pending' 
                    LIMIT :batch_size
                    FOR UPDATE SKIP LOCKED
                )
                RETURNING id
            """, {"batch_size": batch_size})
            
            affected = result.rowcount
            
            if affected == 0:
                break
            
            total_migrated += affected
            logger.info(f"Migrated {total_migrated} rows")
            
            # Check system health
            if is_database_overloaded():
                logger.warning("Database overloaded, pausing...")
                time.sleep(10)
        
        # Small delay between batches
        time.sleep(0.1)
    
    return total_migrated
```

### Ghost Table Migration (MySQL)

```bash
# Using gh-ost for large table changes
gh-ost \
  --host=db.example.com \
  --database=myapp \
  --table=users \
  --alter="ADD COLUMN phone VARCHAR(20)" \
  --execute \
  --allow-on-master \
  --chunk-size=1000 \
  --max-load=Threads_running=25 \
  --critical-load=Threads_running=50
```

### pg_repack (PostgreSQL)

```bash
# Reclaim space and remove bloat without locks
pg_repack -d myapp -t users --no-kill-backend

# With index rebuild
pg_repack -d myapp -t users --only-indexes
```

---

## Rollback Strategies

### Pre-Migration Snapshot

```sql
-- Create snapshot table before migration
CREATE TABLE users_backup_20260115 AS SELECT * FROM users;

-- Or use PostgreSQL's pg_dump for specific tables
-- pg_dump -t users -f users_backup.sql myapp

-- Rollback if needed
TRUNCATE users;
INSERT INTO users SELECT * FROM users_backup_20260115;
-- Or restore from pg_dump
```

### Reversible Migration Pattern

```python
# migrations/20260115_add_user_phone.py

def up(db):
    """Forward migration"""
    db.execute("""
        ALTER TABLE users ADD COLUMN phone VARCHAR(20);
    """)
    
    # Store rollback metadata
    db.execute("""
        INSERT INTO migration_metadata (migration_id, rollback_data)
        VALUES ('20260115_add_user_phone', '{"column": "phone", "table": "users"}')
    """)

def down(db):
    """Rollback migration"""
    db.execute("""
        ALTER TABLE users DROP COLUMN phone;
    """)
    
    db.execute("""
        DELETE FROM migration_metadata WHERE migration_id = '20260115_add_user_phone'
    """)

def verify(db) -> bool:
    """Verify migration success"""
    result = db.execute("""
        SELECT column_name FROM information_schema.columns 
        WHERE table_name = 'users' AND column_name = 'phone'
    """)
    return result.rowcount == 1
```

### Feature Flag Integration

```python
# Enable new schema behavior gradually
class UserService:
    def get_user(self, user_id: int) -> User:
        user_data = db.query("SELECT * FROM users WHERE id = %s", user_id)
        
        # Feature flag controls which column to use
        if feature_flags.is_enabled("use_new_email_column", user_id):
            email = user_data["email_v2"]
        else:
            email = user_data["email"]
        
        return User(id=user_data["id"], email=email, ...)
    
    def update_user_email(self, user_id: int, email: str):
        # Always dual-write during migration
        db.execute("""
            UPDATE users SET email = %s, email_v2 = %s WHERE id = %s
        """, email, email, user_id)
```

---

## Lock Management

### PostgreSQL Lock Analysis

```sql
-- Check for blocking locks
SELECT 
    blocked_locks.pid AS blocked_pid,
    blocked_activity.usename AS blocked_user,
    blocking_locks.pid AS blocking_pid,
    blocking_activity.usename AS blocking_user,
    blocked_activity.query AS blocked_query,
    blocking_activity.query AS blocking_query
FROM pg_catalog.pg_locks blocked_locks
JOIN pg_catalog.pg_stat_activity blocked_activity 
    ON blocked_activity.pid = blocked_locks.pid
JOIN pg_catalog.pg_locks blocking_locks 
    ON blocking_locks.locktype = blocked_locks.locktype
    AND blocking_locks.database IS NOT DISTINCT FROM blocked_locks.database
    AND blocking_locks.relation IS NOT DISTINCT FROM blocked_locks.relation
    AND blocking_locks.page IS NOT DISTINCT FROM blocked_locks.page
    AND blocking_locks.tuple IS NOT DISTINCT FROM blocked_locks.tuple
    AND blocking_locks.virtualxid IS NOT DISTINCT FROM blocked_locks.virtualxid
    AND blocking_locks.transactionid IS NOT DISTINCT FROM blocked_locks.transactionid
    AND blocking_locks.classid IS NOT DISTINCT FROM blocked_locks.classid
    AND blocking_locks.objid IS NOT DISTINCT FROM blocked_locks.objid
    AND blocking_locks.objsubid IS NOT DISTINCT FROM blocked_locks.objsubid
    AND blocking_locks.pid != blocked_locks.pid
JOIN pg_catalog.pg_stat_activity blocking_activity 
    ON blocking_activity.pid = blocking_locks.pid
WHERE NOT blocked_locks.granted;

-- Set statement timeout for migrations
SET statement_timeout = '5s';

-- Set lock timeout (fail fast if can't acquire)
SET lock_timeout = '3s';
```

### MySQL Lock Analysis

```sql
-- Check for blocking locks
SELECT 
    r.trx_id waiting_trx_id,
    r.trx_mysql_thread_id waiting_thread,
    r.trx_query waiting_query,
    b.trx_id blocking_trx_id,
    b.trx_mysql_thread_id blocking_thread,
    b.trx_query blocking_query
FROM information_schema.innodb_lock_waits w
INNER JOIN information_schema.innodb_trx b 
    ON b.trx_id = w.blocking_trx_id
INNER JOIN information_schema.innodb_trx r 
    ON r.trx_id = w.requesting_trx_id;

-- Set lock wait timeout
SET SESSION innodb_lock_wait_timeout = 3;
```

### Lock-Free DDL Checklist

| Operation | PostgreSQL | MySQL 8.0+ |
|-----------|------------|------------|
| ADD COLUMN (nullable) | ✅ Fast | ✅ INSTANT |
| ADD COLUMN (with default) | ✅ Fast (11+) | ✅ INSTANT |
| DROP COLUMN | ✅ Fast | ⚠️ INPLACE |
| ADD INDEX | ⚠️ CONCURRENTLY | ✅ INPLACE, LOCK=NONE |
| DROP INDEX | ✅ Fast | ✅ INPLACE |
| RENAME COLUMN | ✅ Fast | ✅ INSTANT |
| CHANGE TYPE (widen) | ⚠️ Depends | ⚠️ INPLACE |
| ADD FK | ⚠️ NOT VALID | ⚠️ Blocks writes |
| ADD NOT NULL | ⚠️ Scans table | ⚠️ Scans table |

---

## Validation Queries

### Pre-Migration Validation

```sql
-- Check for orphaned records before adding FK
SELECT COUNT(*) FROM orders o 
LEFT JOIN customers c ON o.customer_id = c.id 
WHERE c.id IS NULL AND o.customer_id IS NOT NULL;

-- Check for NULL values before adding NOT NULL
SELECT COUNT(*) FROM users WHERE email IS NULL;

-- Check for duplicates before adding unique constraint
SELECT email, COUNT(*) 
FROM users 
GROUP BY email 
HAVING COUNT(*) > 1;

-- Estimate migration time based on row count
SELECT 
    relname AS table_name,
    reltuples::bigint AS row_estimate,
    pg_size_pretty(pg_total_relation_size(oid)) AS total_size
FROM pg_class
WHERE relname = 'users';
```

### Post-Migration Validation

```sql
-- Verify column exists
SELECT column_name, data_type, is_nullable 
FROM information_schema.columns 
WHERE table_name = 'users' AND column_name = 'phone';

-- Verify index exists and is valid
SELECT indexname, indexdef 
FROM pg_indexes 
WHERE tablename = 'users' AND indexname = 'idx_users_email';

-- Check constraint is valid (PostgreSQL)
SELECT conname, convalidated 
FROM pg_constraint 
WHERE conname = 'fk_customer';

-- Verify data integrity
SELECT COUNT(*) FROM users WHERE status = 'migrated';

-- Compare counts before and after
SELECT 
    (SELECT COUNT(*) FROM users) AS current_count,
    (SELECT COUNT(*) FROM users_backup_20260115) AS backup_count;
```

---

## Migration Framework Examples

### Rails Active Record

```ruby
# db/migrate/20260115_add_phone_to_users.rb
class AddPhoneToUsers < ActiveRecord::Migration[7.1]
  # Disable transaction for large tables
  disable_ddl_transaction!
  
  def change
    # Safe: nullable column
    add_column :users, :phone, :string
    
    # Safe: concurrent index
    add_index :users, :phone, algorithm: :concurrently
  end
end

# Strong migrations gem for safety checks
# Gemfile: gem 'strong_migrations'
class AddEmailIndexToUsers < ActiveRecord::Migration[7.1]
  disable_ddl_transaction!
  
  def change
    add_index :users, :email, algorithm: :concurrently
  end
end
```

### Django

```python
# migrations/0002_add_phone_to_users.py
from django.db import migrations

class Migration(migrations.Migration):
    atomic = False  # Disable transaction for concurrent ops
    
    dependencies = [
        ('users', '0001_initial'),
    ]
    
    operations = [
        # Safe: Add nullable column
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        
        # Safe: Concurrent index (PostgreSQL)
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['phone'], name='users_phone_idx'),
        ),
    ]
```

### Alembic (SQLAlchemy)

```python
# alembic/versions/20260115_add_phone.py
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Safe: nullable column
    op.add_column('users', sa.Column('phone', sa.String(20), nullable=True))
    
    # Safe: concurrent index
    op.execute("""
        CREATE INDEX CONCURRENTLY idx_users_phone ON users(phone)
    """)

def downgrade():
    op.execute("DROP INDEX CONCURRENTLY IF EXISTS idx_users_phone")
    op.drop_column('users', 'phone')
```

---

## Severity Guide

| Severity | Issue | Impact |
|----------|-------|--------|
| 🔴 Critical | Full table lock on production | Service outage |
| 🔴 Critical | Data loss potential | Irrecoverable |
| 🔴 Critical | No rollback plan | Stuck if failed |
| 🟠 High | Long-running migration without batching | Performance degradation |
| 🟠 High | Breaking backward compatibility | Application errors |
| 🟡 Medium | Missing validation queries | Silent data issues |
| 🟡 Medium | No monitoring during migration | Blind execution |
| 🟢 Low | Missing documentation | Future maintenance |

---

## Report Template

```markdown
## Migration Safety Review

### Migration Details
- Migration ID: [id]
- Description: [description]
- Tables affected: [tables]
- Estimated rows: [count]

### Risk Assessment
- Overall Risk: [Low/Medium/High/Critical]
- Lock Type: [None/Share/Exclusive]
- Estimated Duration: [time]
- Backward Compatible: [Yes/No]
- Reversible: [Yes/No]

### Pre-Migration Checklist
- [ ] Backup created
- [ ] Validation queries run
- [ ] Application prepared
- [ ] Rollback tested
- [ ] Monitoring in place

### Execution Plan
1. [Step 1]
2. [Step 2]
...

### Rollback Plan
1. [Rollback step 1]
2. [Rollback step 2]
...

### Post-Migration Validation
- [ ] Schema verified
- [ ] Data integrity checked
- [ ] Application functioning
- [ ] Performance acceptable
```

---

## Related Prompts

- [schema-design-review.md](schema-design-review.md) — Schema design patterns
- [postgresql-optimization.md](postgresql-optimization.md) — PostgreSQL specifics
- [mysql-optimization.md](mysql-optimization.md) — MySQL specifics

---

*Last updated: 2026-01*

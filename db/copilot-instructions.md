# Database Development — Copilot Instructions

> **Purpose**: Configure Copilot for database development best practices  
> **Best For**: GitHub Copilot, VS Code  
> **Databases**: MySQL, PostgreSQL, SQL Server, SQLite  
> **Last Updated**: 2025-12

---

## Overview

This file provides GitHub Copilot with context about database development best practices, SQL conventions, and schema design patterns to generate higher-quality database code.

---

## SQL Style Guidelines

### Naming Conventions

```sql
-- Tables: lowercase, plural, snake_case
users, order_items, user_permissions

-- Columns: lowercase, snake_case
first_name, created_at, is_active

-- Primary keys: 'id' or 'table_id'
id, user_id, order_id

-- Foreign keys: singular_table_id
user_id, category_id, parent_id

-- Indexes: idx_table_columns
idx_users_email, idx_orders_user_id_status

-- Constraints: type_table_columns
pk_users, fk_orders_user, uq_users_email, chk_orders_total
```

### SQL Formatting

```sql
-- Keywords uppercase, identifiers lowercase
SELECT
    u.id,
    u.first_name,
    u.email,
    COUNT(o.id) AS order_count
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
WHERE u.is_active = true
    AND u.created_at > '2024-01-01'
GROUP BY u.id, u.first_name, u.email
HAVING COUNT(o.id) > 5
ORDER BY order_count DESC
LIMIT 100;

-- Table definitions: one column per line
CREATE TABLE users (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    password_hash VARCHAR(255) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT uq_users_email UNIQUE (email)
);
```

---

## Common Patterns

### Standard Table Template

```sql
-- PostgreSQL
CREATE TABLE {{table_name}} (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    -- business columns here
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- MySQL
CREATE TABLE {{table_name}} (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    -- business columns here
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

### Foreign Key Pattern

```sql
-- PostgreSQL
user_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,

-- MySQL
user_id BIGINT NOT NULL,
CONSTRAINT fk_{{table}}_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
```

### Junction Table Pattern

```sql
CREATE TABLE user_roles (
    user_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    role_id BIGINT NOT NULL REFERENCES roles(id) ON DELETE CASCADE,
    assigned_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    assigned_by BIGINT REFERENCES users(id),
    
    PRIMARY KEY (user_id, role_id)
);
```

### Soft Delete Pattern

```sql
-- Column
deleted_at TIMESTAMP NULL,

-- Index (PostgreSQL partial index)
CREATE INDEX idx_{{table}}_active ON {{table}} (id) WHERE deleted_at IS NULL;

-- Query
SELECT * FROM users WHERE deleted_at IS NULL;
```

---

## Index Best Practices

### When to Index

```sql
-- Always index:
-- 1. Foreign keys
CREATE INDEX idx_orders_user_id ON orders (user_id);

-- 2. Columns in WHERE clauses
CREATE INDEX idx_users_email ON users (email);

-- 3. Columns in ORDER BY
CREATE INDEX idx_posts_created_at ON posts (created_at DESC);

-- 4. Columns in JOIN conditions
CREATE INDEX idx_order_items_order_id ON order_items (order_id);
```

### Composite Index Order

```sql
-- Order: equality conditions first, then range, then sort
-- For: WHERE status = 'active' AND created_at > '2024-01-01' ORDER BY name
CREATE INDEX idx_users_status_created_name ON users (status, created_at, name);
```

### Covering Indexes

```sql
-- PostgreSQL: INCLUDE for covering index
CREATE INDEX idx_users_email_cover ON users (email) INCLUDE (first_name, last_name);

-- Query satisfied entirely from index
SELECT first_name, last_name FROM users WHERE email = 'test@example.com';
```

---

## Query Patterns

### Pagination

```sql
-- Keyset pagination (preferred for large datasets)
SELECT * FROM posts
WHERE created_at < :last_created_at
ORDER BY created_at DESC
LIMIT 20;

-- Offset pagination (simpler, slower for large offsets)
SELECT * FROM posts
ORDER BY created_at DESC
LIMIT 20 OFFSET 100;
```

### Upsert

```sql
-- PostgreSQL
INSERT INTO user_settings (user_id, key, value)
VALUES (:user_id, :key, :value)
ON CONFLICT (user_id, key) 
DO UPDATE SET value = EXCLUDED.value, updated_at = CURRENT_TIMESTAMP;

-- MySQL
INSERT INTO user_settings (user_id, `key`, value)
VALUES (:user_id, :key, :value)
ON DUPLICATE KEY UPDATE value = VALUES(value), updated_at = CURRENT_TIMESTAMP;
```

### Batch Operations

```sql
-- Batch insert
INSERT INTO users (email, first_name) VALUES
    ('user1@example.com', 'User 1'),
    ('user2@example.com', 'User 2'),
    ('user3@example.com', 'User 3');

-- Batch update with CASE
UPDATE products
SET price = CASE id
    WHEN 1 THEN 19.99
    WHEN 2 THEN 29.99
    WHEN 3 THEN 39.99
END
WHERE id IN (1, 2, 3);
```

### CTEs for Readability

```sql
WITH active_users AS (
    SELECT id, email
    FROM users
    WHERE is_active = true
),
recent_orders AS (
    SELECT user_id, COUNT(*) AS order_count
    FROM orders
    WHERE created_at > CURRENT_DATE - INTERVAL '30 days'
    GROUP BY user_id
)
SELECT 
    u.email,
    COALESCE(o.order_count, 0) AS recent_orders
FROM active_users u
LEFT JOIN recent_orders o ON o.user_id = u.id
ORDER BY recent_orders DESC;
```

---

## Security Practices

### Always Use Parameterized Queries

```sql
-- Never concatenate user input
-- ❌ Bad: "SELECT * FROM users WHERE email = '" + email + "'"

-- ✅ Good: Use parameters
SELECT * FROM users WHERE email = :email;
SELECT * FROM users WHERE email = $1;
SELECT * FROM users WHERE email = ?;
```

### Principle of Least Privilege

```sql
-- Create read-only user for reporting
CREATE USER report_user WITH PASSWORD 'secure_password';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO report_user;

-- Create application user with limited permissions
CREATE USER app_user WITH PASSWORD 'secure_password';
GRANT SELECT, INSERT, UPDATE, DELETE ON users, orders, order_items TO app_user;
-- Don't grant: DROP, ALTER, TRUNCATE
```

### Audit Sensitive Operations

```sql
-- Audit table
CREATE TABLE audit_log (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    table_name VARCHAR(100) NOT NULL,
    record_id BIGINT NOT NULL,
    action VARCHAR(10) NOT NULL,  -- INSERT, UPDATE, DELETE
    old_data JSONB,
    new_data JSONB,
    user_id BIGINT,
    ip_address INET,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

---

## Migration Best Practices

### Safe Migration Patterns

```sql
-- Add column (safe)
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Add NOT NULL column (safe approach)
ALTER TABLE users ADD COLUMN status VARCHAR(20) DEFAULT 'active';
-- Later, after backfill:
ALTER TABLE users ALTER COLUMN status SET NOT NULL;

-- Add index concurrently (PostgreSQL - no lock)
CREATE INDEX CONCURRENTLY idx_users_phone ON users (phone);

-- Rename column (use new column approach for zero-downtime)
ALTER TABLE users ADD COLUMN full_name VARCHAR(200);
UPDATE users SET full_name = name;
-- Deploy code to use full_name
-- Later: ALTER TABLE users DROP COLUMN name;
```

### Migration File Template

```sql
-- Migration: {{description}}
-- Created: {{date}}
-- Author: {{author}}

-- Up
BEGIN;

-- Changes here
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
CREATE INDEX CONCURRENTLY idx_users_phone ON users (phone);

COMMIT;

-- Down
BEGIN;

DROP INDEX IF EXISTS idx_users_phone;
ALTER TABLE users DROP COLUMN IF EXISTS phone;

COMMIT;
```

---

## Performance Tips

### Query Optimization

```sql
-- Use EXISTS instead of IN for subqueries
-- ❌ Slower
SELECT * FROM users WHERE id IN (SELECT user_id FROM orders);

-- ✅ Faster
SELECT * FROM users u WHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);

-- Avoid SELECT *
-- ❌ Bad
SELECT * FROM users;

-- ✅ Good
SELECT id, email, first_name FROM users;

-- Use UNION ALL when duplicates are impossible
-- ❌ UNION (removes duplicates, slower)
SELECT id FROM active_users UNION SELECT id FROM premium_users;

-- ✅ UNION ALL (keeps duplicates, faster)
SELECT id FROM active_users UNION ALL SELECT id FROM premium_users;
```

### Explain Your Queries

```sql
-- PostgreSQL
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) SELECT ...;

-- MySQL
EXPLAIN ANALYZE SELECT ...;
```

---

## Database-Specific Notes

### PostgreSQL

```sql
-- Use JSONB over JSON
data JSONB NOT NULL DEFAULT '{}';

-- Use IDENTITY over SERIAL
id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY;

-- Use TEXT over VARCHAR for variable-length strings
description TEXT;

-- Array types are available
tags TEXT[] NOT NULL DEFAULT '{}';
```

### MySQL

```sql
-- Always specify ENGINE and CHARSET
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Use BIGINT for IDs (room to grow)
id BIGINT AUTO_INCREMENT PRIMARY KEY;

-- JSON type available in 5.7+
data JSON NOT NULL;
```

---

## Copilot Hints

When generating SQL, prefer:
- Explicit column lists over SELECT *
- JOINs over subqueries where appropriate
- CTEs for complex queries
- Parameterized queries for any user input
- Proper indexes for WHERE, JOIN, ORDER BY columns
- Transaction wrappers for multi-statement operations
- Comments explaining complex logic

# MongoDB — NoSQL Patterns & Optimization

> **Purpose**: Production-ready MongoDB patterns, schema design, and optimization  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: Document design, aggregation, indexes, performance  
> **Last Updated**: 2026-01

---

## Mission

Help design and optimize **MongoDB databases** for production workloads. Focus on document modeling, aggregation pipelines, indexing strategies, and performance optimization.

---

## Guard Clauses

**If no MongoDB context provided:**
```
NO_MONGODB_CONTEXT

Please provide context:
- Collection schemas or sample documents
- Query patterns / access patterns
- Performance issues (if any)
- MongoDB version
- Or describe your use case

Include current indexes if optimizing.
```

**If MongoDB design is solid:**
```
MONGODB_APPROVED

✅ MongoDB review complete — production ready.

Checks performed:
- Schema design: ✓ (appropriate embedding/referencing)
- Indexes: ✓ (covering query patterns)
- Aggregation: ✓ (efficient pipeline stages)
- Performance: ✓ (no obvious bottlenecks)

Design follows MongoDB best practices.
```

---

## Quick Context Checklist

```
☐ MongoDB version (6.x, 7.x)
☐ Collection schemas / sample documents
☐ Query patterns (read/write ratio)
☐ Current indexes
☐ Collection sizes
☐ Sharding requirements
☐ Replica set configuration
☐ Performance requirements
```

---

## Copy-Paste Prompts

### Prompt: Design MongoDB Schema
```text
Design a MongoDB schema for:

Use case: {{USE_CASE}}
Entities: {{ENTITIES}}
Relationships: {{RELATIONSHIPS}}

Access patterns:
- Read: {{READ_PATTERNS}}
- Write: {{WRITE_PATTERNS}}

Requirements:
- Document size limit awareness
- Query performance optimization
- Data consistency needs

Provide:
1. Collection schemas with sample documents
2. Embedding vs referencing decisions
3. Index recommendations
4. Aggregation examples if needed
```

### Prompt: Optimize MongoDB Queries
```text
Optimize this MongoDB query/aggregation:

{{QUERY_OR_PIPELINE}}

Collection schema:
{{SCHEMA}}

Current indexes:
{{INDEXES}}

Performance issue: {{ISSUE}}

Analyze:
1. Index utilization
2. Pipeline stage efficiency
3. Memory usage
4. Recommendations
```

### Prompt: Review MongoDB Schema
```text
Review this MongoDB schema design:

Collections:
{{SCHEMAS}}

Access patterns:
{{PATTERNS}}

Check for:
1. **Document Design**
   - Embedding vs referencing
   - Document size
   - Array growth patterns

2. **Query Optimization**
   - Index coverage
   - Query patterns
   - Aggregation efficiency

3. **Scalability**
   - Sharding readiness
   - Write scaling
   - Read distribution
```

### Prompt: Create Aggregation Pipeline
```text
Create a MongoDB aggregation pipeline for:

Requirement: {{REQUIREMENT}}
Source collection: {{COLLECTION}}
Sample document: {{SAMPLE}}

Expected output: {{OUTPUT_FORMAT}}

Consider:
- Pipeline stage ordering
- Index utilization
- Memory limits ($allowDiskUse)
- Performance optimization
```

---

## Schema Design Patterns

### Embedding vs Referencing

```javascript
// ✅ EMBED: One-to-few, data read together
// Blog post with comments (few comments, always shown)
{
  _id: ObjectId("..."),
  title: "My Post",
  content: "...",
  author: {
    _id: ObjectId("..."),
    name: "John Doe",
    avatar: "/avatars/john.jpg"
  },
  comments: [
    { 
      _id: ObjectId("..."),
      text: "Great post!",
      author: "Jane",
      createdAt: ISODate("2026-01-01")
    }
  ]
}

// ✅ REFERENCE: One-to-many, independent access
// Order referencing products (many products, independent updates)
{
  _id: ObjectId("..."),
  orderNumber: "ORD-001",
  customerId: ObjectId("..."),  // Reference
  items: [
    { productId: ObjectId("..."), quantity: 2, price: 29.99 },
    { productId: ObjectId("..."), quantity: 1, price: 49.99 }
  ],
  total: 109.97
}

// ✅ HYBRID: Embed frequently accessed, reference for full data
// User with denormalized info
{
  _id: ObjectId("..."),
  email: "user@example.com",
  profile: {
    name: "John Doe",
    avatar: "/avatars/john.jpg"
  },
  // Reference for rarely accessed data
  settingsId: ObjectId("..."),
  billingId: ObjectId("...")
}
```

### Common Schema Patterns

#### Polymorphic Pattern

```javascript
// Different document types in one collection
// Products with varying attributes
{
  _id: ObjectId("..."),
  type: "book",
  name: "MongoDB Guide",
  price: 49.99,
  // Type-specific fields
  author: "Jane Smith",
  isbn: "978-0-123456-78-9",
  pages: 350
}

{
  _id: ObjectId("..."),
  type: "electronics",
  name: "Wireless Mouse",
  price: 29.99,
  // Type-specific fields
  brand: "TechCo",
  warranty: "2 years",
  specifications: {
    dpi: 1600,
    wireless: true
  }
}

// Index for polymorphic queries
db.products.createIndex({ type: 1, price: 1 })
```

#### Bucket Pattern

```javascript
// Time-series data bucketed by hour
{
  _id: ObjectId("..."),
  sensorId: "sensor-001",
  bucket: ISODate("2026-01-05T10:00:00Z"),
  measurements: [
    { ts: ISODate("2026-01-05T10:00:15Z"), temp: 22.5, humidity: 45 },
    { ts: ISODate("2026-01-05T10:01:30Z"), temp: 22.6, humidity: 44 },
    // ... more measurements
  ],
  count: 60,
  sum_temp: 1350,
  sum_humidity: 2700
}

// Query last hour of data efficiently
db.sensor_data.find({
  sensorId: "sensor-001",
  bucket: { $gte: ISODate("2026-01-05T09:00:00Z") }
})
```

#### Computed Pattern

```javascript
// Pre-computed aggregations for performance
{
  _id: ObjectId("..."),
  productId: ObjectId("..."),
  // Raw data
  reviews: [
    { rating: 5, text: "Excellent!" },
    { rating: 4, text: "Very good" },
    { rating: 5, text: "Love it!" }
  ],
  // Pre-computed on write
  computed: {
    averageRating: 4.67,
    totalReviews: 3,
    ratingDistribution: { 5: 2, 4: 1, 3: 0, 2: 0, 1: 0 }
  }
}

// Update with recomputation
db.products.updateOne(
  { _id: productId },
  [
    { $set: { reviews: { $concatArrays: ["$reviews", [newReview]] } } },
    { $set: {
      "computed.totalReviews": { $size: "$reviews" },
      "computed.averageRating": { $avg: "$reviews.rating" }
    }}
  ]
)
```

#### Outlier Pattern

```javascript
// Handle documents that exceed normal size
// Main document with overflow reference
{
  _id: ObjectId("..."),
  title: "Popular Post",
  content: "...",
  commentCount: 15000,
  recentComments: [/* last 100 comments */],
  hasOverflow: true,
  overflowId: ObjectId("...")  // Reference to overflow collection
}

// Overflow collection for excess data
{
  _id: ObjectId("..."),
  sourceId: ObjectId("..."),
  sourceCollection: "posts",
  comments: [/* older comments */]
}
```

---

## Indexing Strategies

### Index Types

```javascript
// Single field index
db.users.createIndex({ email: 1 })

// Compound index (field order matters!)
// Supports queries on: {status}, {status, createdAt}, {status, createdAt, priority}
db.orders.createIndex({ status: 1, createdAt: -1, priority: 1 })

// Multikey index (for arrays)
db.products.createIndex({ tags: 1 })

// Text index for full-text search
db.articles.createIndex({ title: "text", content: "text" })

// Geospatial index
db.locations.createIndex({ coordinates: "2dsphere" })

// Hashed index (for sharding)
db.users.createIndex({ email: "hashed" })

// TTL index (auto-expire documents)
db.sessions.createIndex(
  { createdAt: 1 },
  { expireAfterSeconds: 86400 }  // 24 hours
)

// Partial index (index subset of documents)
db.orders.createIndex(
  { customerId: 1 },
  { partialFilterExpression: { status: "active" } }
)

// Unique index
db.users.createIndex({ email: 1 }, { unique: true })

// Sparse index (only index documents with field)
db.users.createIndex({ nickname: 1 }, { sparse: true })
```

### Compound Index Order (ESR Rule)

```javascript
// ESR: Equality, Sort, Range
// Query: find active orders, sorted by date, price > $100

// ✅ OPTIMAL: Equality → Sort → Range
db.orders.createIndex({ status: 1, createdAt: -1, price: 1 })

// Query can use index fully
db.orders.find({ status: "active", price: { $gt: 100 } })
  .sort({ createdAt: -1 })

// ❌ SUBOPTIMAL: Range before Sort
db.orders.createIndex({ status: 1, price: 1, createdAt: -1 })
// Sort happens in memory after range scan
```

### Index Analysis

```javascript
// Check index usage
db.orders.aggregate([
  { $indexStats: {} }
])

// Explain query plan
db.orders.find({ status: "active" }).explain("executionStats")

// Look for:
// - "stage": "IXSCAN" (good) vs "COLLSCAN" (bad)
// - "totalDocsExamined" close to "nReturned"
// - "executionTimeMillis" reasonable

// Find unused indexes
db.orders.aggregate([
  { $indexStats: {} },
  { $match: { "accesses.ops": 0 } }
])
```

---

## Aggregation Pipelines

### Pipeline Optimization

```javascript
// ✅ OPTIMIZED: Filter early, project only needed fields
db.orders.aggregate([
  // 1. Match first (uses index)
  { $match: { 
    status: "completed",
    createdAt: { $gte: ISODate("2026-01-01") }
  }},
  
  // 2. Project early (reduce document size)
  { $project: {
    customerId: 1,
    total: 1,
    createdAt: 1
  }},
  
  // 3. Group
  { $group: {
    _id: "$customerId",
    totalSpent: { $sum: "$total" },
    orderCount: { $sum: 1 }
  }},
  
  // 4. Sort
  { $sort: { totalSpent: -1 } },
  
  // 5. Limit
  { $limit: 100 }
])

// ❌ INEFFICIENT: Group before match, unnecessary fields
db.orders.aggregate([
  { $group: { /* processes ALL documents */ } },
  { $match: { /* filter after grouping */ } }
])
```

### Common Aggregation Patterns

#### Lookup with Unwind

```javascript
// Join orders with customers
db.orders.aggregate([
  { $match: { status: "completed" } },
  
  // Lookup (LEFT JOIN)
  { $lookup: {
    from: "customers",
    localField: "customerId",
    foreignField: "_id",
    as: "customer"
  }},
  
  // Unwind (convert array to object)
  { $unwind: {
    path: "$customer",
    preserveNullAndEmptyArrays: true  // Keep orders without customer
  }},
  
  { $project: {
    orderNumber: 1,
    total: 1,
    customerName: "$customer.name",
    customerEmail: "$customer.email"
  }}
])
```

#### Faceted Search

```javascript
// Multiple aggregations in parallel
db.products.aggregate([
  { $match: { category: "electronics" } },
  
  { $facet: {
    // Results with pagination
    results: [
      { $sort: { price: 1 } },
      { $skip: 0 },
      { $limit: 20 }
    ],
    
    // Total count
    totalCount: [
      { $count: "count" }
    ],
    
    // Price ranges
    priceRanges: [
      { $bucket: {
        groupBy: "$price",
        boundaries: [0, 50, 100, 200, 500, Infinity],
        default: "Other",
        output: { count: { $sum: 1 } }
      }}
    ],
    
    // Brand breakdown
    brands: [
      { $group: { _id: "$brand", count: { $sum: 1 } } },
      { $sort: { count: -1 } },
      { $limit: 10 }
    ]
  }}
])
```

#### Window Functions (MongoDB 5.0+)

```javascript
// Running totals and rankings
db.sales.aggregate([
  { $match: { year: 2026 } },
  
  { $setWindowFields: {
    partitionBy: "$region",
    sortBy: { month: 1 },
    output: {
      // Running total within region
      runningTotal: {
        $sum: "$revenue",
        window: { documents: ["unbounded", "current"] }
      },
      
      // Rank within region
      rank: {
        $rank: {}
      },
      
      // Moving average (3 months)
      movingAvg: {
        $avg: "$revenue",
        window: { documents: [-1, 1] }
      }
    }
  }}
])
```

#### Graph Lookup

```javascript
// Recursive lookup (org chart, categories)
db.employees.aggregate([
  { $match: { _id: "ceo" } },
  
  { $graphLookup: {
    from: "employees",
    startWith: "$_id",
    connectFromField: "_id",
    connectToField: "managerId",
    as: "reports",
    maxDepth: 3,
    depthField: "level"
  }}
])
```

---

## Performance Optimization

### Query Optimization

```javascript
// ✅ Use projection to limit returned fields
db.users.find(
  { status: "active" },
  { name: 1, email: 1, _id: 0 }
)

// ✅ Use covered queries (all fields in index)
db.orders.createIndex({ status: 1, total: 1, createdAt: 1 })
db.orders.find(
  { status: "active" },
  { total: 1, createdAt: 1, _id: 0 }  // Covered!
)

// ✅ Avoid $where and $regex without prefix
// ❌ Bad
db.users.find({ name: { $regex: /john/i } })
// ✅ Good (prefix match uses index)
db.users.find({ name: { $regex: /^John/i } })

// ✅ Use hint() to force index
db.orders.find({ customerId: id })
  .hint({ customerId: 1, createdAt: -1 })
```

### Write Optimization

```javascript
// ✅ Bulk operations
const bulk = db.products.initializeUnorderedBulkOp()

products.forEach(p => {
  bulk.find({ sku: p.sku })
    .upsert()
    .updateOne({ $set: p })
})

await bulk.execute()

// ✅ Use $inc instead of read-modify-write
// ❌ Bad
const doc = await db.counters.findOne({ _id: "visits" })
await db.counters.updateOne(
  { _id: "visits" },
  { $set: { count: doc.count + 1 } }
)

// ✅ Good (atomic)
await db.counters.updateOne(
  { _id: "visits" },
  { $inc: { count: 1 } },
  { upsert: true }
)

// ✅ Avoid growing arrays unbounded
// ❌ Bad - array grows forever
{ $push: { comments: newComment } }

// ✅ Good - cap array size
{ $push: { 
  recentComments: { 
    $each: [newComment], 
    $slice: -100  // Keep last 100
  }
}}
```

### Memory and Disk

```javascript
// Allow disk use for large aggregations
db.largeCollection.aggregate([
  { $group: { _id: "$category", total: { $sum: "$amount" } } }
], { allowDiskUse: true })

// Use $merge for incremental aggregation
db.orders.aggregate([
  { $match: { createdAt: { $gte: lastRunTime } } },
  { $group: { 
    _id: { customer: "$customerId", month: { $month: "$createdAt" } },
    total: { $sum: "$amount" }
  }},
  { $merge: {
    into: "monthly_totals",
    on: "_id",
    whenMatched: "merge",
    whenNotMatched: "insert"
  }}
])
```

---

## Transactions

### Multi-Document Transactions

```javascript
const session = client.startSession()

try {
  session.startTransaction({
    readConcern: { level: "snapshot" },
    writeConcern: { w: "majority" }
  })
  
  // Transfer funds between accounts
  await db.accounts.updateOne(
    { _id: fromAccountId, balance: { $gte: amount } },
    { $inc: { balance: -amount } },
    { session }
  )
  
  await db.accounts.updateOne(
    { _id: toAccountId },
    { $inc: { balance: amount } },
    { session }
  )
  
  await db.transactions.insertOne({
    from: fromAccountId,
    to: toAccountId,
    amount,
    timestamp: new Date()
  }, { session })
  
  await session.commitTransaction()
} catch (error) {
  await session.abortTransaction()
  throw error
} finally {
  session.endSession()
}
```

---

## Sharding

### Shard Key Selection

```javascript
// ✅ Good shard keys
// High cardinality, even distribution, query isolation

// Hashed for even distribution (random access patterns)
sh.shardCollection("mydb.users", { email: "hashed" })

// Range for query isolation (time-series, geo)
sh.shardCollection("mydb.logs", { timestamp: 1 })

// Compound for better distribution
sh.shardCollection("mydb.orders", { customerId: 1, _id: 1 })

// ❌ Bad shard keys
// - Low cardinality (status, boolean)
// - Monotonically increasing (_id with ObjectId, timestamp alone)
// - Random values without query pattern support
```

### Zone Sharding

```javascript
// Geographic data locality
sh.addShardTag("shard0", "US")
sh.addShardTag("shard1", "EU")

sh.addTagRange(
  "mydb.users",
  { region: "US", _id: MinKey },
  { region: "US", _id: MaxKey },
  "US"
)

sh.addTagRange(
  "mydb.users",
  { region: "EU", _id: MinKey },
  { region: "EU", _id: MaxKey },
  "EU"
)
```

---

## Change Streams

```javascript
// Watch for real-time changes
const pipeline = [
  { $match: { 
    operationType: { $in: ["insert", "update"] },
    "fullDocument.status": "active"
  }}
]

const changeStream = db.orders.watch(pipeline, {
  fullDocument: "updateLookup"
})

changeStream.on("change", (change) => {
  console.log("Change detected:", change.operationType)
  console.log("Document:", change.fullDocument)
  
  // Process change...
})

// Resume from token after restart
const resumeToken = change._id
const resumedStream = db.orders.watch(pipeline, {
  resumeAfter: resumeToken
})
```

---

## Severity Guide

| Severity | Issue | Impact |
|----------|-------|--------|
| 🔴 Critical | Missing indexes on query fields | Slow queries, high CPU |
| 🔴 Critical | Unbounded array growth | Document size limit exceeded |
| 🔴 Critical | Collection scan on large collection | Performance degradation |
| 🟠 High | Wrong embedding/referencing choice | Data duplication or slow joins |
| 🟠 High | Index not supporting sort | In-memory sort |
| 🟡 Medium | Over-indexing | Slow writes, memory waste |
| 🟡 Medium | Missing partial indexes | Unnecessary index size |
| 🟢 Low | Schema validation missing | Data quality |

---

## Report Template

```markdown
## MongoDB Review

### Environment
- MongoDB version: [version]
- Deployment: [standalone/replica set/sharded]
- Collection count: [count]
- Total data size: [size]

### Schema Assessment
| Collection | Documents | Avg Size | Design Quality |
|------------|-----------|----------|----------------|
| | | | |

### Index Analysis
| Collection | Index | Size | Usage | Status |
|------------|-------|------|-------|--------|
| | | | | |

### Issues Found
1. [Severity] Issue description
   - Collection: 
   - Impact:
   - Recommendation:

### Recommendations
1. [Priority] Recommendation
   - Benefit:
   - Implementation:
```

---

## Related Prompts

- [schema-design-review.md](schema-design-review.md) — General schema design
- [postgresql-optimization.md](postgresql-optimization.md) — PostgreSQL patterns
- [redis-patterns.md](redis-patterns.md) — Caching layer

---

*Last updated: 2026-01*

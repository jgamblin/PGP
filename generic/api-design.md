# API Design — REST, GraphQL, and Best Practices

> **Purpose**: Production-ready API design patterns and review  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: REST, GraphQL, OpenAPI, versioning, error handling  
> **Last Updated**: 2026-03

---

## Mission

Help design and review **APIs** that are consistent, well-documented, secure, and maintainable. Focus on RESTful design, GraphQL patterns, OpenAPI specifications, versioning strategies, and error handling.

---

## Guard Clauses

**If no API context provided:**
```
NO_API_CONTEXT

Please provide context:
- API type (REST, GraphQL, gRPC)
- Current endpoints or schema
- Use case/domain
- Client types (web, mobile, third-party)
- Authentication requirements

Include request/response examples if reviewing.
```

**If API design is solid:**
```
API_APPROVED

✅ API review complete — production ready.

Checks performed:
- Naming conventions: ✓
- HTTP methods/status codes: ✓
- Error handling: ✓
- Security: ✓
- Documentation: ✓

Design follows API best practices.
```

---

## Quick Context Checklist

```
☐ API style (REST/GraphQL/gRPC)
☐ Domain/resource model
☐ Client types
☐ Authentication method
☐ Rate limiting requirements
☐ Versioning strategy
☐ Documentation format
☐ Backward compatibility needs
```

---

## Copy-Paste Prompts

### Prompt: Design REST API
```text
Design a REST API for:

Domain: {{DOMAIN}}
Resources: {{RESOURCES}}
Operations needed: {{OPERATIONS}}

Clients: {{CLIENT_TYPES}}
Authentication: {{AUTH_METHOD}}

Provide:
1. Resource URIs and methods
2. Request/response formats
3. Error responses
4. Pagination strategy
5. OpenAPI specification snippet
```

### Prompt: Review API Design
```text
Review this API design:

{{API_SPECIFICATION_OR_ENDPOINTS}}

Check for:
1. **Naming & Conventions**
   - URI structure
   - HTTP methods usage
   - Naming consistency

2. **Responses**
   - Status codes
   - Error formats
   - Pagination

3. **Security**
   - Authentication
   - Authorization
   - Input validation

4. **Documentation**
   - Completeness
   - Examples
   - Versioning
```

### Prompt: Design GraphQL Schema
```text
Design a GraphQL schema for:

Domain: {{DOMAIN}}
Entities: {{ENTITIES}}
Operations: {{QUERIES_AND_MUTATIONS}}

Requirements:
- Pagination style: {{CURSOR_OR_OFFSET}}
- Real-time needs: {{SUBSCRIPTIONS}}
- Performance: {{N+1_HANDLING}}

Provide:
1. Type definitions
2. Query/Mutation definitions
3. Input types
4. Error handling approach
5. DataLoader patterns for N+1
```

### Prompt: Create OpenAPI Specification
```text
Create an OpenAPI 3.1 specification for:

API: {{API_NAME}}
Base URL: {{BASE_URL}}
Endpoints:
{{ENDPOINT_LIST}}

Include:
1. Path definitions with parameters
2. Request/response schemas
3. Security definitions
4. Error responses
5. Examples for each endpoint
```

---

## REST API Design

### Resource Naming

```yaml
# ✅ GOOD: Nouns, plural, lowercase, hyphens
GET    /users                    # List users
GET    /users/{id}               # Get user
POST   /users                    # Create user
PUT    /users/{id}               # Replace user
PATCH  /users/{id}               # Update user
DELETE /users/{id}               # Delete user

GET    /users/{id}/orders        # User's orders
GET    /order-items              # Multi-word resource

# ❌ BAD: Verbs, actions in URL, inconsistent
GET    /getUsers
GET    /user/{id}                # Singular
POST   /users/create
GET    /users/{id}/getOrders
GET    /orderItems               # camelCase
```

### HTTP Methods

| Method | Purpose | Idempotent | Safe | Request Body |
|--------|---------|------------|------|--------------|
| GET | Retrieve resource(s) | ✅ | ✅ | No |
| POST | Create resource | ❌ | ❌ | Yes |
| PUT | Replace resource | ✅ | ❌ | Yes |
| PATCH | Partial update | ❌* | ❌ | Yes |
| DELETE | Remove resource | ✅ | ❌ | Rarely |

*PATCH can be idempotent if using JSON Patch or similar

### Status Codes

```yaml
# Success
200 OK              # GET, PUT, PATCH success with body
201 Created         # POST success, include Location header
204 No Content      # DELETE success, PUT/PATCH without body

# Redirection
301 Moved Permanently   # Resource permanently moved
304 Not Modified        # Conditional GET, use cached version

# Client Errors
400 Bad Request         # Invalid request syntax/payload
401 Unauthorized        # Authentication required
403 Forbidden           # Authenticated but not authorized
404 Not Found           # Resource doesn't exist
405 Method Not Allowed  # HTTP method not supported
409 Conflict            # State conflict (duplicate, version)
422 Unprocessable Entity # Valid syntax but semantic errors
429 Too Many Requests   # Rate limited

# Server Errors
500 Internal Server Error   # Unexpected server error
502 Bad Gateway             # Upstream server error
503 Service Unavailable     # Temporarily unavailable
504 Gateway Timeout         # Upstream timeout
```

### Request/Response Format

```json
// POST /users
// Request
{
  "email": "user@example.com",
  "name": "John Doe",
  "role": "member"
}

// Response 201 Created
// Headers: Location: /users/123
{
  "id": 123,
  "email": "user@example.com",
  "name": "John Doe",
  "role": "member",
  "createdAt": "2026-01-15T10:30:00Z",
  "updatedAt": "2026-01-15T10:30:00Z"
}

// GET /users?page=1&limit=20&sort=-createdAt
// Response 200 OK
{
  "data": [
    { "id": 123, "email": "user@example.com", ... }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "totalPages": 8
  },
  "links": {
    "self": "/users?page=1&limit=20",
    "next": "/users?page=2&limit=20",
    "last": "/users?page=8&limit=20"
  }
}
```

### Error Response Format

```json
// Standard error format (RFC 7807 Problem Details)
{
  "type": "https://api.example.com/errors/validation",
  "title": "Validation Error",
  "status": 422,
  "detail": "The request body contains invalid fields",
  "instance": "/users",
  "errors": [
    {
      "field": "email",
      "code": "invalid_format",
      "message": "Email must be a valid email address"
    },
    {
      "field": "name",
      "code": "required",
      "message": "Name is required"
    }
  ],
  "traceId": "abc123def456"
}

// Simplified format (common alternative)
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "The request body contains invalid fields",
    "details": [
      { "field": "email", "message": "Invalid email format" }
    ]
  }
}
```

---

## Pagination Patterns

### Offset Pagination

```yaml
# Simple, but has issues with large offsets
GET /users?page=5&limit=20
GET /users?offset=80&limit=20

# Response
{
  "data": [...],
  "pagination": {
    "page": 5,
    "limit": 20,
    "total": 500,
    "totalPages": 25
  }
}

# ⚠️ Issues:
# - Slow for large offsets (OFFSET 10000 LIMIT 20)
# - Inconsistent if data changes between requests
```

### Cursor Pagination

```yaml
# Better for large datasets and real-time data
GET /users?limit=20
GET /users?limit=20&cursor=eyJpZCI6MTIzfQ==

# Response
{
  "data": [...],
  "pagination": {
    "limit": 20,
    "hasMore": true,
    "nextCursor": "eyJpZCI6MTQzfQ==",
    "prevCursor": "eyJpZCI6MTIzfQ=="
  }
}

# Cursor is typically base64-encoded: {"id": 143, "createdAt": "..."}
# ✅ Benefits:
# - Consistent performance regardless of position
# - Stable results even with data changes
```

### Keyset Pagination

```yaml
# Similar to cursor but with explicit fields
GET /users?limit=20&after_id=143&after_created_at=2026-01-15

# SQL: WHERE (created_at, id) > ('2026-01-15', 143)
#      ORDER BY created_at DESC, id DESC
#      LIMIT 20
```

---

## Filtering, Sorting, and Field Selection

### Filtering

```yaml
# Simple filters
GET /users?status=active&role=admin

# Operators
GET /users?created_at[gte]=2026-01-01&created_at[lt]=2026-02-01
GET /orders?total[gt]=100&status[in]=pending,processing

# Search
GET /users?q=john
GET /products?search=wireless+headphones

# Complex filters (JSON or custom syntax)
GET /users?filter={"status":"active","role":{"$in":["admin","moderator"]}}
```

### Sorting

```yaml
# Single field
GET /users?sort=created_at        # Ascending
GET /users?sort=-created_at       # Descending (prefix -)

# Multiple fields
GET /users?sort=-created_at,name  # Primary: created_at DESC, Secondary: name ASC

# Alternative syntax
GET /users?sort_by=created_at&order=desc
```

### Field Selection (Sparse Fieldsets)

```yaml
# Include only specified fields
GET /users?fields=id,name,email
GET /users/123?fields=id,name,profile.avatar

# Exclude fields
GET /users?exclude=password_hash,internal_notes

# Expand related resources
GET /users/123?include=orders,profile
GET /orders/456?expand=customer,items.product
```

---

## Versioning Strategies

### URI Versioning

```yaml
# Most explicit, easy to understand
GET /v1/users
GET /v2/users

# ✅ Pros: Clear, cacheable, easy routing
# ❌ Cons: URL pollution, harder to sunset
```

### Header Versioning

```yaml
# Version in custom header
GET /users
Accept-Version: v1
X-API-Version: 2

# ✅ Pros: Clean URLs
# ❌ Cons: Less discoverable, harder to test in browser
```

### Content Negotiation

```yaml
# Version in Accept header
GET /users
Accept: application/vnd.example.v1+json

# ✅ Pros: RESTful, standard approach
# ❌ Cons: Complex, verbose
```

### Query Parameter

```yaml
# Version as query param
GET /users?version=1

# ✅ Pros: Easy to switch, visible
# ❌ Cons: Pollutes query string, caching issues
```

### Recommended: URI with Deprecation Headers

```yaml
# Use URI versioning with deprecation signals
GET /v1/users
# Response headers for deprecation
Deprecation: true
Sunset: Sat, 01 Jun 2026 00:00:00 GMT
Link: </v2/users>; rel="successor-version"
```

---

## GraphQL Design

### Schema Design

```graphql
# Types
type User {
  id: ID!
  email: String!
  name: String!
  role: Role!
  profile: Profile
  orders(first: Int, after: String): OrderConnection!
  createdAt: DateTime!
  updatedAt: DateTime!
}

enum Role {
  ADMIN
  MODERATOR
  MEMBER
}

type Profile {
  bio: String
  avatar: String
  website: String
}

# Pagination (Relay Connection spec)
type OrderConnection {
  edges: [OrderEdge!]!
  pageInfo: PageInfo!
  totalCount: Int!
}

type OrderEdge {
  node: Order!
  cursor: String!
}

type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}

# Queries
type Query {
  user(id: ID!): User
  users(
    first: Int
    after: String
    filter: UserFilter
    orderBy: UserOrderBy
  ): UserConnection!
  me: User
}

input UserFilter {
  status: UserStatus
  role: Role
  search: String
}

input UserOrderBy {
  field: UserOrderField!
  direction: OrderDirection!
}

enum UserOrderField {
  CREATED_AT
  NAME
  EMAIL
}

enum OrderDirection {
  ASC
  DESC
}

# Mutations
type Mutation {
  createUser(input: CreateUserInput!): CreateUserPayload!
  updateUser(id: ID!, input: UpdateUserInput!): UpdateUserPayload!
  deleteUser(id: ID!): DeleteUserPayload!
}

input CreateUserInput {
  email: String!
  name: String!
  role: Role
}

type CreateUserPayload {
  user: User
  errors: [UserError!]
}

type UserError {
  field: String
  code: String!
  message: String!
}
```

### N+1 Prevention with DataLoader

```javascript
// DataLoader batches and caches database requests
const userLoader = new DataLoader(async (userIds) => {
  const users = await db.query(
    'SELECT * FROM users WHERE id = ANY($1)',
    [userIds]
  );
  // Return in same order as requested IDs
  const userMap = new Map(users.map(u => [u.id, u]));
  return userIds.map(id => userMap.get(id) || null);
});

// Resolver
const resolvers = {
  Order: {
    user: (order, args, context) => {
      return context.loaders.user.load(order.userId);
    }
  }
};
```

### Error Handling

```graphql
# Union type for errors
union CreateUserResult = User | ValidationError | AuthorizationError

type ValidationError {
  message: String!
  field: String!
}

type AuthorizationError {
  message: String!
  requiredPermission: String!
}

type Mutation {
  createUser(input: CreateUserInput!): CreateUserResult!
}
```

```json
// Response with errors
{
  "data": {
    "createUser": null
  },
  "errors": [
    {
      "message": "Validation failed",
      "locations": [{ "line": 2, "column": 3 }],
      "path": ["createUser"],
      "extensions": {
        "code": "VALIDATION_ERROR",
        "field": "email",
        "details": "Email already exists"
      }
    }
  ]
}
```

---

## OpenAPI Specification

### Complete Example

```yaml
openapi: 3.1.0
info:
  title: User Management API
  version: 1.0.0
  description: API for managing users
  contact:
    name: API Support
    email: api@example.com

servers:
  - url: https://api.example.com/v1
    description: Production
  - url: https://staging-api.example.com/v1
    description: Staging

security:
  - bearerAuth: []

paths:
  /users:
    get:
      summary: List users
      operationId: listUsers
      tags: [Users]
      parameters:
        - name: page
          in: query
          schema:
            type: integer
            default: 1
            minimum: 1
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
            minimum: 1
            maximum: 100
        - name: status
          in: query
          schema:
            $ref: '#/components/schemas/UserStatus'
        - name: sort
          in: query
          schema:
            type: string
            enum: [created_at, -created_at, name, -name]
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserListResponse'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '429':
          $ref: '#/components/responses/TooManyRequests'
    
    post:
      summary: Create user
      operationId: createUser
      tags: [Users]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
            example:
              email: user@example.com
              name: John Doe
              role: member
      responses:
        '201':
          description: User created
          headers:
            Location:
              schema:
                type: string
              description: URL of created user
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '400':
          $ref: '#/components/responses/BadRequest'
        '422':
          $ref: '#/components/responses/ValidationError'

  /users/{id}:
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
    
    get:
      summary: Get user by ID
      operationId: getUser
      tags: [Users]
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          $ref: '#/components/responses/NotFound'
    
    patch:
      summary: Update user
      operationId: updateUser
      tags: [Users]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateUserRequest'
      responses:
        '200':
          description: User updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          $ref: '#/components/responses/NotFound'
        '422':
          $ref: '#/components/responses/ValidationError'
    
    delete:
      summary: Delete user
      operationId: deleteUser
      tags: [Users]
      responses:
        '204':
          description: User deleted
        '404':
          $ref: '#/components/responses/NotFound'

components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
  
  schemas:
    User:
      type: object
      required: [id, email, name, role, createdAt, updatedAt]
      properties:
        id:
          type: integer
          readOnly: true
        email:
          type: string
          format: email
        name:
          type: string
          minLength: 1
          maxLength: 255
        role:
          $ref: '#/components/schemas/UserRole'
        createdAt:
          type: string
          format: date-time
          readOnly: true
        updatedAt:
          type: string
          format: date-time
          readOnly: true
    
    UserRole:
      type: string
      enum: [admin, moderator, member]
    
    UserStatus:
      type: string
      enum: [active, inactive, suspended]
    
    CreateUserRequest:
      type: object
      required: [email, name]
      properties:
        email:
          type: string
          format: email
        name:
          type: string
          minLength: 1
          maxLength: 255
        role:
          $ref: '#/components/schemas/UserRole'
          default: member
    
    UpdateUserRequest:
      type: object
      properties:
        email:
          type: string
          format: email
        name:
          type: string
          minLength: 1
          maxLength: 255
        role:
          $ref: '#/components/schemas/UserRole'
    
    UserListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/User'
        pagination:
          $ref: '#/components/schemas/Pagination'
    
    Pagination:
      type: object
      properties:
        page:
          type: integer
        limit:
          type: integer
        total:
          type: integer
        totalPages:
          type: integer
    
    Error:
      type: object
      required: [type, title, status]
      properties:
        type:
          type: string
          format: uri
        title:
          type: string
        status:
          type: integer
        detail:
          type: string
        instance:
          type: string
        traceId:
          type: string
    
    ValidationError:
      allOf:
        - $ref: '#/components/schemas/Error'
        - type: object
          properties:
            errors:
              type: array
              items:
                type: object
                properties:
                  field:
                    type: string
                  code:
                    type: string
                  message:
                    type: string
  
  responses:
    BadRequest:
      description: Bad request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
    
    Unauthorized:
      description: Unauthorized
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
    
    NotFound:
      description: Resource not found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
    
    ValidationError:
      description: Validation error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ValidationError'
    
    TooManyRequests:
      description: Rate limit exceeded
      headers:
        Retry-After:
          schema:
            type: integer
          description: Seconds until rate limit resets
        X-RateLimit-Limit:
          schema:
            type: integer
        X-RateLimit-Remaining:
          schema:
            type: integer
        X-RateLimit-Reset:
          schema:
            type: integer
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
```

---

## Security Best Practices

### Authentication Headers

```yaml
# Bearer token (JWT)
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...

# API Key
X-API-Key: sk_live_abc123def456
# Or in query (less secure, avoid if possible)
GET /users?api_key=sk_live_abc123def456
```

### Rate Limiting Headers

```yaml
# Response headers
X-RateLimit-Limit: 100        # Requests allowed per window
X-RateLimit-Remaining: 95     # Requests remaining
X-RateLimit-Reset: 1704470400 # Unix timestamp when limit resets
Retry-After: 60               # Seconds to wait (when limited)
```

### Security Headers

```yaml
# Required response headers
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Content-Security-Policy: default-src 'none'

# CORS headers (when needed)
Access-Control-Allow-Origin: https://app.example.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Authorization, Content-Type
Access-Control-Max-Age: 86400
```

### Input Validation

```yaml
# Always validate:
- Data types (string, number, boolean)
- Required fields
- String lengths (min, max)
- Number ranges
- Email formats
- URL formats
- Enum values
- Array sizes
- Nested object depth

# Sanitize:
- Strip HTML/scripts from text inputs
- Normalize Unicode
- Trim whitespace
- Validate file uploads (type, size)
```

---

## Severity Guide

| Severity | Issue | Impact |
|----------|-------|--------|
| 🔴 Critical | Missing authentication | Security breach |
| 🔴 Critical | SQL injection possibility | Data exposure |
| 🔴 Critical | No input validation | System compromise |
| 🟠 High | Inconsistent error formats | Poor DX |
| 🟠 High | No rate limiting | DoS vulnerability |
| 🟠 High | Missing versioning | Breaking changes |
| 🟡 Medium | Inconsistent naming | Confusion |
| 🟡 Medium | Missing pagination | Performance |
| 🟢 Low | Missing examples in docs | Onboarding |

---

## Report Template

```markdown
## API Review

### Overview
- API Type: [REST/GraphQL/gRPC]
- Version: [version]
- Base URL: [url]
- Endpoints reviewed: [count]

### Design Assessment
| Category | Status | Notes |
|----------|--------|-------|
| Naming conventions | | |
| HTTP methods | | |
| Status codes | | |
| Error handling | | |
| Pagination | | |
| Versioning | | |
| Documentation | | |

### Issues Found
1. [Severity] Issue description
   - Endpoint:
   - Impact:
   - Recommendation:

### Security Assessment
- [ ] Authentication implemented
- [ ] Authorization checked
- [ ] Input validation present
- [ ] Rate limiting configured
- [ ] HTTPS enforced
- [ ] Sensitive data protected

### Recommendations
1. [Priority] Recommendation
   - Benefit:
   - Implementation:
```

---

## Related Prompts

- [security-analysis.md](security-analysis.md) — Security review
- [documentation-generation.md](documentation-generation.md) — API documentation
- [observability-logging.md](observability-logging.md) — API monitoring

---

*Last updated: 2026-01*

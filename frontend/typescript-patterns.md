# TypeScript Patterns — Modern Type-Safe Development

> **Purpose**: Production-ready TypeScript patterns and best practices  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Types, generics, utilities, architecture  
> **Last Updated**: 2026-03

---

## Mission

Help write **type-safe, maintainable TypeScript code** using modern patterns. Focus on proper typing, generics, utility types, and architectural patterns that scale.

---

## Guard Clauses

**If no TypeScript context provided:**
```
NO_TYPESCRIPT_CONTEXT

Please provide context:
- Project type (React, Node, library, etc.)
- TypeScript version
- Code to review or task description
- Or describe what you want to accomplish
```

**If TypeScript is well-typed:**
```
TYPESCRIPT_APPROVED

✅ TypeScript review complete — production ready.

Checks performed:
- Type safety: ✓ (no any, proper inference)
- Generics: ✓ (reusable, constrained appropriately)
- Utilities: ✓ (using built-in types effectively)
- Patterns: ✓ (consistent, maintainable)

Code follows TypeScript best practices.
```

---

## Quick Context Checklist

```
☐ TypeScript version (5.x recommended)
☐ Strict mode enabled
☐ Project type and framework
☐ ESLint/Biome configuration
☐ Module system (ESM/CJS)
☐ Build target
☐ External dependencies
☐ Testing requirements
```

---

## Copy-Paste Prompts

### Prompt: Review TypeScript Code
```text
Review this TypeScript code:

{{CODE}}

Check for:
1. **Type Safety**
   - No `any` types without justification
   - Proper type narrowing
   - Null/undefined handling
   - Type assertions minimized

2. **Generics**
   - Appropriate use of generics
   - Proper constraints
   - Inference working correctly

3. **Patterns**
   - Discriminated unions where appropriate
   - Proper error handling types
   - Consistent naming conventions

4. **Performance**
   - Type complexity reasonable
   - No excessive conditional types

Rate each: 🟢 Good | 🟡 Needs attention | 🔴 Critical issue
```

### Prompt: Add Types to JavaScript
```text
Add TypeScript types to this JavaScript code:

{{CODE}}

Requirements:
- Strict mode compatible
- No `any` types
- Proper generics where needed
- JSDoc comments for public APIs
- Export types for consumers

Provide:
1. Typed version of the code
2. Separate type definitions if needed
3. Explanation of type decisions
```

### Prompt: Design Type System
```text
Design a type system for:

Domain: {{DOMAIN}}
Entities: {{ENTITIES}}
Operations: {{OPERATIONS}}

Generate:
1. Core type definitions
2. Utility types for common operations
3. Type guards
4. Generic patterns
5. Example usage
```

---

## Core Patterns

### Discriminated Unions
```typescript
// ✅ Good: Discriminated union for state management
type AsyncState<T, E = Error> =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; error: E };

// Type guard
function isSuccess<T>(state: AsyncState<T>): state is { status: "success"; data: T } {
  return state.status === "success";
}

// Usage with exhaustive checking
function renderState<T>(state: AsyncState<T>): string {
  switch (state.status) {
    case "idle":
      return "Ready";
    case "loading":
      return "Loading...";
    case "success":
      return `Data: ${state.data}`;
    case "error":
      return `Error: ${state.error.message}`;
    // TypeScript ensures all cases are handled
  }
}
```

### Result Type (Error Handling)
```typescript
// Result type for explicit error handling
type Result<T, E = Error> =
  | { ok: true; value: T }
  | { ok: false; error: E };

// Constructor functions
const Ok = <T>(value: T): Result<T, never> => ({ ok: true, value });
const Err = <E>(error: E): Result<never, E> => ({ ok: false, error });

// Usage
async function fetchUser(id: string): Promise<Result<User, ApiError>> {
  try {
    const response = await fetch(`/api/users/${id}`);
    if (!response.ok) {
      return Err({ code: response.status, message: "Failed to fetch user" });
    }
    const user = await response.json();
    return Ok(user);
  } catch (e) {
    return Err({ code: 500, message: "Network error" });
  }
}

// Pattern matching style
const result = await fetchUser("123");
if (result.ok) {
  console.log(result.value.name);
} else {
  console.error(result.error.message);
}
```

### Builder Pattern with Types
```typescript
// Type-safe builder pattern
interface QueryBuilder<T extends object> {
  select<K extends keyof T>(...fields: K[]): QueryBuilder<Pick<T, K>>;
  where(condition: Partial<T>): QueryBuilder<T>;
  orderBy(field: keyof T, direction?: "asc" | "desc"): QueryBuilder<T>;
  limit(n: number): QueryBuilder<T>;
  execute(): Promise<T[]>;
}

// Implementation preserves type information
class UserQueryBuilder implements QueryBuilder<User> {
  private query: QueryConfig = {};

  select<K extends keyof User>(...fields: K[]): QueryBuilder<Pick<User, K>> {
    this.query.select = fields;
    return this as unknown as QueryBuilder<Pick<User, K>>;
  }

  where(condition: Partial<User>): this {
    this.query.where = { ...this.query.where, ...condition };
    return this;
  }

  orderBy(field: keyof User, direction: "asc" | "desc" = "asc"): this {
    this.query.orderBy = { field, direction };
    return this;
  }

  limit(n: number): this {
    this.query.limit = n;
    return this;
  }

  async execute(): Promise<User[]> {
    // Execute query
    return [];
  }
}

// Usage - TypeScript tracks selected fields
const users = await new UserQueryBuilder()
  .select("id", "name")
  .where({ role: "admin" })
  .orderBy("name")
  .limit(10)
  .execute();

// users is typed as Pick<User, "id" | "name">[]
```

### Branded Types
```typescript
// Branded types for type-safe IDs
declare const brand: unique symbol;
type Brand<T, B> = T & { [brand]: B };

type UserId = Brand<string, "UserId">;
type OrderId = Brand<string, "OrderId">;
type Email = Brand<string, "Email">;

// Constructor functions with validation
function createUserId(id: string): UserId {
  if (!id.startsWith("usr_")) {
    throw new Error("Invalid user ID format");
  }
  return id as UserId;
}

function createEmail(email: string): Email {
  if (!email.includes("@")) {
    throw new Error("Invalid email format");
  }
  return email as Email;
}

// Now these are type-safe
function getUser(id: UserId): Promise<User> { /* ... */ }
function getOrder(id: OrderId): Promise<Order> { /* ... */ }

const userId = createUserId("usr_123");
const orderId = "ord_456" as OrderId;

getUser(userId);  // ✅ OK
getUser(orderId); // ❌ Type error! Can't pass OrderId to UserId
```

### Const Assertions
```typescript
// Use const assertions for literal types
const ROUTES = {
  home: "/",
  users: "/users",
  userDetail: "/users/:id",
  settings: "/settings",
} as const;

type Route = (typeof ROUTES)[keyof typeof ROUTES];
// Type: "/" | "/users" | "/users/:id" | "/settings"

// For arrays
const STATUS_CODES = [200, 201, 400, 401, 404, 500] as const;
type StatusCode = (typeof STATUS_CODES)[number];
// Type: 200 | 201 | 400 | 401 | 404 | 500

// Object with literal keys
const PERMISSIONS = {
  read: { level: 1, description: "Read access" },
  write: { level: 2, description: "Write access" },
  admin: { level: 3, description: "Admin access" },
} as const;

type Permission = keyof typeof PERMISSIONS;
// Type: "read" | "write" | "admin"
```

---

## Utility Types

### Built-in Utilities
```typescript
interface User {
  id: string;
  name: string;
  email: string;
  role: "admin" | "user";
  createdAt: Date;
  updatedAt: Date;
}

// Partial - all properties optional
type UserUpdate = Partial<User>;

// Required - all properties required
type CompleteUser = Required<User>;

// Pick - select specific properties
type UserPreview = Pick<User, "id" | "name">;

// Omit - exclude specific properties
type UserWithoutDates = Omit<User, "createdAt" | "updatedAt">;

// Record - object with specific key/value types
type UsersByRole = Record<User["role"], User[]>;

// Readonly - immutable version
type ImmutableUser = Readonly<User>;

// Extract/Exclude for union types
type AdminRole = Extract<User["role"], "admin">;  // "admin"
type NonAdminRole = Exclude<User["role"], "admin">; // "user"

// ReturnType - get function return type
declare function getUser(): Promise<User>;
type GetUserReturn = ReturnType<typeof getUser>; // Promise<User>

// Parameters - get function parameter types
declare function updateUser(id: string, data: Partial<User>): void;
type UpdateUserParams = Parameters<typeof updateUser>; // [string, Partial<User>]

// Awaited - unwrap Promise types
type ResolvedUser = Awaited<Promise<User>>; // User
```

### Custom Utility Types
```typescript
// Deep partial - recursively make all properties optional
type DeepPartial<T> = T extends object
  ? { [P in keyof T]?: DeepPartial<T[P]> }
  : T;

// Deep readonly - recursively make all properties readonly
type DeepReadonly<T> = T extends object
  ? { readonly [P in keyof T]: DeepReadonly<T[P]> }
  : T;

// Nullable - allow null
type Nullable<T> = T | null;

// NonNullableFields - make specific fields non-nullable
type NonNullableFields<T, K extends keyof T> = T & {
  [P in K]-?: NonNullable<T[P]>;
};

// RequiredFields - make specific fields required
type RequiredFields<T, K extends keyof T> = T & Required<Pick<T, K>>;

// Mutable - remove readonly
type Mutable<T> = {
  -readonly [P in keyof T]: T[P];
};

// ValueOf - get union of object values
type ValueOf<T> = T[keyof T];

// Entries type
type Entries<T> = {
  [K in keyof T]: [K, T[K]];
}[keyof T][];

// Function overloads helper
type Overloads<T> = T extends {
  (...args: infer A1): infer R1;
  (...args: infer A2): infer R2;
}
  ? [(...args: A1) => R1, (...args: A2) => R2]
  : never;
```

### Type Guards
```typescript
// Type guard functions
function isString(value: unknown): value is string {
  return typeof value === "string";
}

function isNonNullable<T>(value: T): value is NonNullable<T> {
  return value !== null && value !== undefined;
}

function hasProperty<K extends PropertyKey>(
  obj: object,
  key: K
): obj is object & Record<K, unknown> {
  return key in obj;
}

// Array type guard
function isArrayOf<T>(
  arr: unknown,
  guard: (item: unknown) => item is T
): arr is T[] {
  return Array.isArray(arr) && arr.every(guard);
}

// Usage
const values: unknown[] = ["a", "b", "c"];
if (isArrayOf(values, isString)) {
  // values is now string[]
  values.map((s) => s.toUpperCase());
}

// Discriminated union guard
interface Dog { type: "dog"; bark(): void; }
interface Cat { type: "cat"; meow(): void; }
type Animal = Dog | Cat;

function isDog(animal: Animal): animal is Dog {
  return animal.type === "dog";
}
```

---

## Advanced Patterns

### Template Literal Types
```typescript
// Event types from template literals
type EventName = "click" | "focus" | "blur";
type EventHandler = `on${Capitalize<EventName>}`;
// Type: "onClick" | "onFocus" | "onBlur"

// API routes
type ApiVersion = "v1" | "v2";
type Resource = "users" | "posts" | "comments";
type ApiEndpoint = `/${ApiVersion}/${Resource}`;
// Type: "/v1/users" | "/v1/posts" | ... | "/v2/comments"

// CSS units
type Unit = "px" | "em" | "rem" | "%";
type CSSValue = `${number}${Unit}`;
// Accepts "10px", "1.5em", "100%", etc.

// Path parameters extraction
type ExtractParams<T extends string> =
  T extends `${infer _Start}:${infer Param}/${infer Rest}`
    ? Param | ExtractParams<`/${Rest}`>
    : T extends `${infer _Start}:${infer Param}`
      ? Param
      : never;

type UserRouteParams = ExtractParams<"/users/:userId/posts/:postId">;
// Type: "userId" | "postId"
```

### Mapped Types with Modifiers
```typescript
// Add prefix to all keys
type Prefixed<T, P extends string> = {
  [K in keyof T as `${P}${Capitalize<string & K>}`]: T[K];
};

interface User {
  name: string;
  age: number;
}

type PrefixedUser = Prefixed<User, "user">;
// { userName: string; userAge: number }

// Getters and setters
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};

type Setters<T> = {
  [K in keyof T as `set${Capitalize<string & K>}`]: (value: T[K]) => void;
};

// Filter keys by value type
type FilterByType<T, U> = {
  [K in keyof T as T[K] extends U ? K : never]: T[K];
};

interface Mixed {
  id: number;
  name: string;
  age: number;
  email: string;
}

type StringFields = FilterByType<Mixed, string>;
// { name: string; email: string }
```

### Conditional Types
```typescript
// Infer return type
type UnwrapPromise<T> = T extends Promise<infer U> ? U : T;

type A = UnwrapPromise<Promise<string>>; // string
type B = UnwrapPromise<number>; // number

// Infer array element type
type ElementType<T> = T extends (infer E)[] ? E : never;

type C = ElementType<string[]>; // string

// Infer function parameters
type FirstParam<T> = T extends (first: infer F, ...args: any[]) => any
  ? F
  : never;

type D = FirstParam<(name: string, age: number) => void>; // string

// Distributive conditional types
type ToArray<T> = T extends any ? T[] : never;

type E = ToArray<string | number>; // string[] | number[]

// Non-distributive (wrapped in tuple)
type ToArrayNonDist<T> = [T] extends [any] ? T[] : never;

type F = ToArrayNonDist<string | number>; // (string | number)[]
```

---

## React TypeScript Patterns

### Component Props
```typescript
// Props with children
interface CardProps {
  title: string;
  children: React.ReactNode;
}

// Props extending HTML attributes
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary";
  isLoading?: boolean;
}

// Generic component props
interface ListProps<T> {
  items: T[];
  renderItem: (item: T, index: number) => React.ReactNode;
  keyExtractor: (item: T) => string;
}

function List<T>({ items, renderItem, keyExtractor }: ListProps<T>) {
  return (
    <ul>
      {items.map((item, index) => (
        <li key={keyExtractor(item)}>{renderItem(item, index)}</li>
      ))}
    </ul>
  );
}

// Polymorphic component
type PolymorphicProps<E extends React.ElementType> = {
  as?: E;
  children: React.ReactNode;
} & Omit<React.ComponentPropsWithoutRef<E>, "as" | "children">;

function Box<E extends React.ElementType = "div">({
  as,
  children,
  ...props
}: PolymorphicProps<E>) {
  const Component = as || "div";
  return <Component {...props}>{children}</Component>;
}

// Usage
<Box as="section" id="main">Content</Box>
<Box as="a" href="/link">Link</Box>
```

### Hooks Types
```typescript
// Custom hook with generics
function useLocalStorage<T>(
  key: string,
  initialValue: T
): [T, (value: T | ((prev: T) => T)) => void] {
  const [stored, setStored] = useState<T>(() => {
    try {
      const item = localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch {
      return initialValue;
    }
  });

  const setValue = (value: T | ((prev: T) => T)) => {
    const valueToStore = value instanceof Function ? value(stored) : value;
    setStored(valueToStore);
    localStorage.setItem(key, JSON.stringify(valueToStore));
  };

  return [stored, setValue];
}

// Reducer with discriminated unions
type CounterAction =
  | { type: "increment" }
  | { type: "decrement" }
  | { type: "set"; payload: number };

interface CounterState {
  count: number;
}

function counterReducer(state: CounterState, action: CounterAction): CounterState {
  switch (action.type) {
    case "increment":
      return { count: state.count + 1 };
    case "decrement":
      return { count: state.count - 1 };
    case "set":
      return { count: action.payload };
  }
}
```

---

## Configuration

### tsconfig.json (Strict)
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "noPropertyAccessFromIndexSignature": true,
    "exactOptionalPropertyTypes": true,
    
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "forceConsistentCasingInFileNames": true,
    
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["src"],
  "exclude": ["node_modules"]
}
```

---

## Best Practices Checklist

### Type Safety
- [ ] `strict: true` enabled
- [ ] No `any` without justification
- [ ] Proper null/undefined handling
- [ ] Type guards for narrowing

### Code Quality
- [ ] Discriminated unions for variants
- [ ] Generics where appropriate
- [ ] Utility types over manual types
- [ ] Consistent naming conventions

### Performance
- [ ] Avoid excessive type complexity
- [ ] Use `interface` for objects (faster)
- [ ] Limit conditional type depth

### Maintainability
- [ ] Export types for consumers
- [ ] Document complex types
- [ ] Keep types close to usage

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | `any` abuse, disabled strict mode, type assertions everywhere |
| **High** | 🟠 | Missing type guards, improper null handling |
| **Medium** | 🟡 | Overly complex types, missing exports |
| **Low** | 🟢 | Naming conventions, documentation |

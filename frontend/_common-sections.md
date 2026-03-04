# Common Sections Reference — Frontend

> **Purpose**: Shared boilerplate for all frontend/TypeScript prompts  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Shared reference sections for frontend prompt workflows  
> **Last Updated**: 2026-03
> **Usage**: Reference this file instead of duplicating content  

---

## Quick Context Checklist

Use this condensed checklist instead of the full "Inputs Required" section:

```
☐ Branch: `git branch --show-current`
☐ Changes: `git diff main...HEAD --name-only`
☐ Diff: `git diff main...HEAD`
☐ Framework (React, Vue, Svelte, etc.)
☐ Build tool (Vite, Next.js, etc.)
☐ TypeScript version
☐ Key dependencies
☐ Pain points or constraints
```

---

## Standard Guard Clauses

Include these at the top of analysis output to handle edge cases:

### No Input Provided
```
NO_ACTIONABLE_INPUT

Unable to proceed without source material. Please provide:
- TypeScript/JavaScript file(s) to analyze, OR
- Code pasted directly in the message, OR
- Repository URL with specific files to review

Example: "Review src/components/UserProfile.tsx for performance issues"
```

### Empty Diff / No Changes
```
NO_CHANGES_DETECTED

No code changes found between branches.

Checked:
- `git diff main...HEAD` returned empty
- No modified TS/JS/TSX/JSX files detected

Next steps:
- Verify you're on the correct branch
- Ensure changes are committed
- Try: `git status` to see uncommitted changes
```

### Analysis Complete - No Issues
```
NO_ISSUES_FOUND

✅ Analysis complete — no significant issues detected.

Summary:
- Files scanned: {{FILE_COUNT}}
- Checks performed: {{CHECK_TYPES}}
- Result: Code meets quality standards

Recommendation: Proceed with confidence.
```

### Analysis Complete - With Findings
```
ANALYSIS_COMPLETE

📋 Found {{ISSUE_COUNT}} items requiring attention.

Breakdown:
- 🔴 Critical: {{CRITICAL_COUNT}}
- 🟠 High: {{HIGH_COUNT}}
- 🟡 Medium: {{MEDIUM_COUNT}}
- 🟢 Low: {{LOW_COUNT}}

See detailed findings below.
```

---

## Severity Levels

Use consistent severity across all prompts:

| Level | Label | Criteria | Action |
|-------|-------|----------|--------|
| 🔴 | **Critical** | Security vulnerability, data exposure, app crash | Fix immediately before merge |
| 🟠 | **High** | Bugs, significant performance issues, a11y blockers | Fix before merge |
| 🟡 | **Medium** | Code quality, minor performance, maintainability | Should fix, can be follow-up |
| 🟢 | **Low** | Style, minor improvements, nice-to-haves | Optional, track for later |

---

## Standard Output Formats

### Code Issue Format

```markdown
### 🔴 [Issue Title]

**Location:** `src/components/Example.tsx:42`

**Problem:**
[Description of what's wrong]

**Current Code:**
```tsx
// Current problematic implementation
```

**Suggested Fix:**
```tsx
// Improved implementation
```

**Why This Matters:**
[Impact on security/performance/accessibility]
```

### Code Diff Format

For suggesting changes, use GitHub-compatible diff:

```diff
// src/components/Example.tsx
- const oldWay = () => { /* ... */ }
+ const newWay = () => { /* ... */ }
```

---

## Report Template

Use this structure for comprehensive reviews:

```markdown
## Frontend Code Review Report

### Summary
| Metric | Value |
|--------|-------|
| Files Reviewed | X |
| Issues Found | X |
| Critical | X |
| High | X |
| Medium | X |
| Low | X |

### Environment
- Framework: [React/Vue/Svelte]
- TypeScript: [version]
- Build Tool: [Vite/Next.js/etc]
- Key Dependencies: [relevant packages]

### Critical Issues
[List critical issues]

### High Priority Issues
[List high priority issues]

### Medium Priority Issues
[List medium priority issues]

### Low Priority Issues
[List low priority issues]

### Recommendations
1. [Priority action items]
```

---

## TypeScript Patterns

### Modern Type Patterns

```typescript
// Const assertions for literal types
const STATUSES = ['pending', 'active', 'completed'] as const;
type Status = typeof STATUSES[number];

// Discriminated unions
type Result<T> = 
  | { success: true; data: T }
  | { success: false; error: Error };

// Template literal types
type EventName = `on${Capitalize<string>}`;

// Utility types
type UserDTO = Pick<User, 'id' | 'name' | 'email'>;
type PartialUser = Partial<User>;
type RequiredUser = Required<User>;

// Satisfies operator (TS 4.9+)
const config = {
  apiUrl: 'https://api.example.com',
  timeout: 5000,
} satisfies Config;
```

### Generic Patterns

```typescript
// Generic components
interface ListProps<T> {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
  keyExtractor: (item: T) => string;
}

function List<T>({ items, renderItem, keyExtractor }: ListProps<T>) {
  return (
    <ul>
      {items.map((item) => (
        <li key={keyExtractor(item)}>{renderItem(item)}</li>
      ))}
    </ul>
  );
}

// Generic hooks
function useAsync<T>(asyncFn: () => Promise<T>) {
  const [state, setState] = useState<{
    data: T | null;
    error: Error | null;
    loading: boolean;
  }>({ data: null, error: null, loading: true });
  
  // ...
}
```

---

## React Patterns

### Component Patterns

```tsx
// Compound components
const Tabs = {
  Root: TabsRoot,
  List: TabsList,
  Trigger: TabsTrigger,
  Content: TabsContent,
};

// Render props (when needed)
interface RenderProps<T> {
  children: (props: T) => React.ReactNode;
}

// Forwarded refs
const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ label, ...props }, ref) => (
    <label>
      {label}
      <input ref={ref} {...props} />
    </label>
  )
);
```

### Hook Patterns

```tsx
// Custom hooks with proper typing
function useLocalStorage<T>(key: string, initialValue: T) {
  const [storedValue, setStoredValue] = useState<T>(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch {
      return initialValue;
    }
  });

  const setValue = useCallback((value: T | ((val: T) => T)) => {
    setStoredValue((prev) => {
      const valueToStore = value instanceof Function ? value(prev) : value;
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
      return valueToStore;
    });
  }, [key]);

  return [storedValue, setValue] as const;
}
```

---

## Common Code Smells

### Performance Issues

```tsx
// ❌ Bad - object created on every render
<Component style={{ color: 'red' }} />

// ✅ Good - stable reference
const style = { color: 'red' };
<Component style={style} />

// ❌ Bad - function created on every render
<button onClick={() => handleClick(id)}>Click</button>

// ✅ Good - memoized callback
const handleClickMemo = useCallback(() => handleClick(id), [id]);
<button onClick={handleClickMemo}>Click</button>

// ❌ Bad - expensive computation on every render
const filtered = items.filter(expensiveFilter);

// ✅ Good - memoized computation
const filtered = useMemo(() => items.filter(expensiveFilter), [items]);
```

### Type Safety Issues

```tsx
// ❌ Bad - any type
function process(data: any) { /* ... */ }

// ✅ Good - proper typing
function process(data: UserData) { /* ... */ }

// ❌ Bad - type assertion
const user = response.data as User;

// ✅ Good - runtime validation
const user = userSchema.parse(response.data);
```

### Accessibility Issues

```tsx
// ❌ Bad - click handler on div
<div onClick={handleClick}>Click me</div>

// ✅ Good - semantic button
<button onClick={handleClick}>Click me</button>

// ❌ Bad - image without alt
<img src={src} />

// ✅ Good - descriptive alt
<img src={src} alt="User profile avatar" />

// ❌ Bad - missing form labels
<input type="text" placeholder="Email" />

// ✅ Good - proper label association
<label>
  Email
  <input type="email" />
</label>
```

---

## Testing Standards

### Component Testing

```tsx
import { render, screen, userEvent } from '@testing-library/react';

describe('Button', () => {
  it('calls onClick when clicked', async () => {
    const handleClick = vi.fn();
    render(<Button onClick={handleClick}>Click me</Button>);
    
    await userEvent.click(screen.getByRole('button', { name: /click me/i }));
    
    expect(handleClick).toHaveBeenCalledTimes(1);
  });
  
  it('is disabled when loading', () => {
    render(<Button loading>Submit</Button>);
    
    expect(screen.getByRole('button')).toBeDisabled();
  });
});
```

### Hook Testing

```tsx
import { renderHook, act } from '@testing-library/react';

describe('useCounter', () => {
  it('increments count', () => {
    const { result } = renderHook(() => useCounter());
    
    act(() => {
      result.current.increment();
    });
    
    expect(result.current.count).toBe(1);
  });
});
```

---

## Performance Baselines

| Metric | Target | Concern |
|--------|--------|---------|
| LCP | < 2.5s | > 4s |
| FID/INP | < 100ms | > 300ms |
| CLS | < 0.1 | > 0.25 |
| TTI | < 3.8s | > 7.3s |
| Bundle size (main) | < 200KB | > 500KB |
| First render | < 100ms | > 300ms |
| Re-render | < 16ms | > 50ms |

---

## Recommended Dependencies

### Essential

```json
{
  "dependencies": {
    "react": "^18.x",
    "typescript": "^5.x",
    "zod": "^3.x"
  },
  "devDependencies": {
    "@testing-library/react": "^14.x",
    "@testing-library/user-event": "^14.x",
    "vitest": "^1.x",
    "eslint": "^8.x",
    "prettier": "^3.x"
  }
}
```

### State Management

| Use Case | Recommendation |
|----------|----------------|
| Local state | useState, useReducer |
| Server state | TanStack Query, SWR |
| Global UI state | Zustand, Jotai |
| Complex forms | React Hook Form + Zod |

### Modern Alternatives

| Old | Modern Alternative | Notes |
|-----|-------------------|-------|
| Redux | Zustand, Jotai | Simpler, less boilerplate |
| Axios | fetch + wrapper | Native, smaller |
| Moment.js | date-fns, Temporal | Smaller, tree-shakeable |
| Lodash | Native JS | Most methods now native |
| styled-components | Tailwind, CSS Modules | Better performance |

---

*Last updated: 2026-01*

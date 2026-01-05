# Frontend Copilot Instructions

> **Purpose**: Repository-level instructions for GitHub Copilot in frontend projects  
> **Usage**: Save as `.github/copilot-instructions.md` in your frontend repository  
> **Last Updated**: 2026-01

---

## Project Context

This is a modern frontend project using React, TypeScript, and contemporary tooling.

### Tech Stack

- **Framework**: React 18+ with TypeScript
- **Build Tool**: Vite / Next.js
- **Styling**: Tailwind CSS
- **State**: Zustand (client) + TanStack Query (server)
- **Forms**: React Hook Form + Zod
- **Testing**: Vitest + React Testing Library + Playwright

---

## Code Style Requirements

### TypeScript

```typescript
// ✅ DO: Use strict TypeScript
interface UserProps {
  id: string;
  name: string;
  email: string;
  role: "admin" | "user" | "guest";
}

// ❌ DON'T: Use `any` or loose types
interface UserProps {
  id: any;
  data: object;
}
```

### Components

```tsx
// ✅ DO: Functional components with explicit types
interface ButtonProps {
  variant?: "primary" | "secondary" | "ghost";
  size?: "sm" | "md" | "lg";
  disabled?: boolean;
  onClick?: () => void;
  children: React.ReactNode;
  className?: string;
}

export function Button({
  variant = "primary",
  size = "md",
  disabled = false,
  onClick,
  children,
  className,
}: ButtonProps) {
  return (
    <button
      type="button"
      disabled={disabled}
      onClick={onClick}
      className={cn(buttonVariants({ variant, size }), className)}
    >
      {children}
    </button>
  );
}

// ❌ DON'T: Class components or implicit any
export default function Button(props) {
  return <button {...props} />;
}
```

### Hooks

```tsx
// ✅ DO: Custom hooks with clear return types
interface UseCounterReturn {
  count: number;
  increment: () => void;
  decrement: () => void;
  reset: () => void;
}

export function useCounter(initial = 0): UseCounterReturn {
  const [count, setCount] = useState(initial);
  
  const increment = useCallback(() => setCount((c) => c + 1), []);
  const decrement = useCallback(() => setCount((c) => c - 1), []);
  const reset = useCallback(() => setCount(initial), [initial]);
  
  return { count, increment, decrement, reset };
}
```

### Styling

```tsx
// ✅ DO: Tailwind with cn() utility
import { cn } from "@/lib/utils";

<div className={cn(
  "flex items-center gap-2 p-4",
  "rounded-lg border bg-card",
  isActive && "border-primary",
  className
)} />

// ❌ DON'T: Inline styles or string concatenation
<div style={{ display: "flex", padding: 16 }} />
<div className={"flex " + (isActive ? "active" : "")} />
```

---

## Patterns to Follow

### State Management

```tsx
// Server state: TanStack Query
const { data, isLoading, error } = useQuery({
  queryKey: ["users", filters],
  queryFn: () => fetchUsers(filters),
});

// Client state: Zustand
const theme = useAppStore((s) => s.theme);
const toggleTheme = useAppStore((s) => s.toggleTheme);

// Form state: React Hook Form + Zod
const form = useForm<FormData>({
  resolver: zodResolver(schema),
});
```

### Data Fetching

```tsx
// ✅ DO: Use query key factories
export const userKeys = {
  all: ["users"] as const,
  lists: () => [...userKeys.all, "list"] as const,
  list: (filters: Filters) => [...userKeys.lists(), filters] as const,
  details: () => [...userKeys.all, "detail"] as const,
  detail: (id: string) => [...userKeys.details(), id] as const,
};

// ✅ DO: Handle loading and error states
if (isLoading) return <Skeleton />;
if (error) return <ErrorMessage error={error} />;
```

### Event Handlers

```tsx
// ✅ DO: Inline handlers for simple cases
<button onClick={() => setOpen(true)}>Open</button>

// ✅ DO: Named handlers for complex logic
const handleSubmit = async (data: FormData) => {
  try {
    await mutation.mutateAsync(data);
    toast.success("Saved successfully");
  } catch (error) {
    toast.error("Failed to save");
  }
};
```

---

## File Organization

```
src/
├── app/                    # Next.js app router (or pages/)
├── components/
│   ├── ui/                 # Primitive components (Button, Input, etc.)
│   │   ├── Button.tsx
│   │   ├── Button.test.tsx
│   │   └── index.ts
│   ├── features/           # Feature-specific components
│   │   └── auth/
│   │       ├── LoginForm.tsx
│   │       └── LoginForm.test.tsx
│   └── layouts/            # Layout components
├── hooks/                  # Custom hooks
├── lib/                    # Utilities and helpers
│   ├── api.ts
│   ├── utils.ts
│   └── constants.ts
├── stores/                 # Zustand stores
├── types/                  # Shared TypeScript types
└── test/                   # Test utilities and setup
```

---

## Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Components | PascalCase | `UserProfile.tsx` |
| Hooks | camelCase with `use` prefix | `useAuth.ts` |
| Utilities | camelCase | `formatDate.ts` |
| Types/Interfaces | PascalCase | `UserData` |
| Constants | SCREAMING_SNAKE_CASE | `API_BASE_URL` |
| CSS classes | kebab-case | `user-profile` |
| Files | Match export name | `UserProfile.tsx` |

---

## Testing Requirements

### Component Tests

```tsx
// ✅ DO: Test behavior, not implementation
describe("Button", () => {
  it("calls onClick when clicked", async () => {
    const onClick = vi.fn();
    render(<Button onClick={onClick}>Click me</Button>);
    
    await userEvent.click(screen.getByRole("button", { name: /click me/i }));
    
    expect(onClick).toHaveBeenCalledTimes(1);
  });
});

// ❌ DON'T: Test implementation details
it("updates internal state when clicked", () => {
  // Don't test useState directly
});
```

### Query Selection Priority

1. `getByRole` - Accessible queries first
2. `getByLabelText` - Form elements
3. `getByPlaceholderText` - When label is not available
4. `getByText` - Non-interactive elements
5. `getByTestId` - Last resort only

---

## Accessibility Requirements

### Required ARIA Attributes

```tsx
// Interactive elements
<button aria-label="Close dialog" aria-pressed={isPressed}>
  <XIcon />
</button>

// Loading states
<div aria-busy={isLoading} aria-live="polite">
  {isLoading ? <Spinner /> : content}
</div>

// Form errors
<input aria-invalid={!!error} aria-describedby="email-error" />
{error && <span id="email-error" role="alert">{error}</span>}
```

### Keyboard Navigation

- All interactive elements must be keyboard accessible
- Provide visible focus indicators
- Support Escape to close modals/dropdowns
- Trap focus in modals

---

## Performance Guidelines

### Memoization

```tsx
// ✅ DO: Memoize expensive computations
const sortedItems = useMemo(
  () => items.sort((a, b) => a.name.localeCompare(b.name)),
  [items]
);

// ✅ DO: Stabilize callbacks passed to children
const handleChange = useCallback((value: string) => {
  onChange(value);
}, [onChange]);

// ❌ DON'T: Over-memoize simple values
const doubled = useMemo(() => count * 2, [count]); // Unnecessary
```

### Code Splitting

```tsx
// ✅ DO: Lazy load routes and heavy components
const Dashboard = lazy(() => import("./pages/Dashboard"));

<Suspense fallback={<PageLoader />}>
  <Dashboard />
</Suspense>
```

---

## Common Mistakes to Avoid

```tsx
// ❌ Using index as key
{items.map((item, index) => <Item key={index} />)}
// ✅ Use unique identifier
{items.map((item) => <Item key={item.id} />)}

// ❌ Direct state mutation
setItems(items.push(newItem));
// ✅ Create new reference
setItems([...items, newItem]);

// ❌ Missing dependency array
useEffect(() => { fetchData(); }, []);
// ✅ Include dependencies or use query library
const { data } = useQuery({ queryKey: ["data"], queryFn: fetchData });

// ❌ Prop drilling
<A><B><C><D value={value} /></C></B></A>
// ✅ Use context or state management
const value = useStore((s) => s.value);

// ❌ Mixing server and client state
const [users, setUsers] = useState([]);
useEffect(() => { fetch("/api/users").then(setUsers); }, []);
// ✅ Use TanStack Query for server state
const { data: users } = useQuery({ queryKey: ["users"], queryFn: fetchUsers });
```

---

## When Generating Code

1. **Always** use TypeScript with strict mode
2. **Always** handle loading and error states
3. **Always** include accessibility attributes
4. **Always** use semantic HTML elements
5. **Prefer** composition over configuration
6. **Prefer** explicit over implicit behavior
7. **Avoid** `any` type - use `unknown` if type is truly unknown
8. **Avoid** inline styles - use Tailwind CSS
9. **Avoid** class components - use functional components
10. **Avoid** prop drilling - use state management

# React Component Development — Modern Patterns

> **Purpose**: Production-ready React component patterns  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: Components, hooks, state, performance  
> **Last Updated**: 2026-01

---

## Mission

Help build **well-structured, performant React components** using modern patterns. Focus on composition, hooks, TypeScript integration, and accessibility.

---

## Guard Clauses

**If no React context provided:**
```
NO_REACT_CONTEXT

Please provide context:
- Component purpose and requirements
- Props and state needed
- Parent/child relationships
- Or share existing component code
```

**If component is well-designed:**
```
COMPONENT_APPROVED

✅ React component review complete — production ready.

Checks performed:
- Structure: ✓ (proper composition, single responsibility)
- Types: ✓ (fully typed props and state)
- Performance: ✓ (memoization, no unnecessary renders)
- Accessibility: ✓ (ARIA, keyboard, semantic HTML)

Component follows React best practices.
```

---

## Quick Context Checklist

```
☐ Component purpose
☐ Props interface
☐ State requirements
☐ Side effects needed
☐ Event handlers
☐ Accessibility needs
☐ Styling approach
☐ Testing requirements
```

---

## Copy-Paste Prompts

### Prompt: Create Component
```text
Create a React component for:

Purpose: {{PURPOSE}}
Props: {{PROPS}}
State: {{STATE_NEEDS}}
Interactions: {{INTERACTIONS}}

Requirements:
- TypeScript with strict types
- Accessible (WCAG 2.1 AA)
- Performant (proper memoization)
- Testable

Generate:
1. Component implementation
2. Props interface
3. Custom hooks if needed
4. Usage examples
5. Test cases
```

### Prompt: Review Component
```text
Review this React component:

{{CODE}}

Check for:
1. **Structure**
   - Single responsibility
   - Proper composition
   - Reasonable size

2. **Types**
   - Props fully typed
   - State types correct
   - Event handlers typed

3. **Performance**
   - Unnecessary re-renders
   - Missing memoization
   - Heavy computations

4. **Accessibility**
   - Semantic HTML
   - ARIA attributes
   - Keyboard navigation
   - Focus management

Rate each: 🟢 Good | 🟡 Needs attention | 🔴 Critical issue
```

### Prompt: Optimize Component
```text
Optimize this React component for performance:

{{CODE}}

Current issues:
- {{ISSUE_1}}
- {{ISSUE_2}}

Generate:
1. Optimized version
2. Explanation of changes
3. Before/after render analysis
4. Testing approach
```

---

## Component Patterns

### Basic Component Structure
```tsx
// components/Button.tsx
import { forwardRef, type ButtonHTMLAttributes } from "react";
import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "@/lib/utils";

// Variants using CVA
const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-md font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        primary: "bg-blue-600 text-white hover:bg-blue-700",
        secondary: "bg-gray-100 text-gray-900 hover:bg-gray-200",
        destructive: "bg-red-600 text-white hover:bg-red-700",
        ghost: "hover:bg-gray-100",
        link: "text-blue-600 underline-offset-4 hover:underline",
      },
      size: {
        sm: "h-8 px-3 text-sm",
        md: "h-10 px-4",
        lg: "h-12 px-6 text-lg",
        icon: "h-10 w-10",
      },
    },
    defaultVariants: {
      variant: "primary",
      size: "md",
    },
  }
);

// Props interface
interface ButtonProps
  extends ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  isLoading?: boolean;
}

// Component with forwardRef
const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, isLoading, disabled, children, ...props }, ref) => {
    return (
      <button
        ref={ref}
        className={cn(buttonVariants({ variant, size }), className)}
        disabled={disabled || isLoading}
        {...props}
      >
        {isLoading ? (
          <>
            <svg
              className="mr-2 h-4 w-4 animate-spin"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle
                className="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                strokeWidth="4"
              />
              <path
                className="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"
              />
            </svg>
            Loading...
          </>
        ) : (
          children
        )}
      </button>
    );
  }
);

Button.displayName = "Button";

export { Button, buttonVariants };
export type { ButtonProps };
```

### Compound Components
```tsx
// components/Tabs.tsx
import {
  createContext,
  useContext,
  useState,
  useCallback,
  type ReactNode,
} from "react";

// Context
interface TabsContextValue {
  activeTab: string;
  setActiveTab: (id: string) => void;
}

const TabsContext = createContext<TabsContextValue | null>(null);

function useTabsContext() {
  const context = useContext(TabsContext);
  if (!context) {
    throw new Error("Tabs components must be used within a Tabs provider");
  }
  return context;
}

// Root component
interface TabsProps {
  defaultTab: string;
  children: ReactNode;
  onChange?: (tab: string) => void;
}

function Tabs({ defaultTab, children, onChange }: TabsProps) {
  const [activeTab, setActiveTabState] = useState(defaultTab);

  const setActiveTab = useCallback(
    (id: string) => {
      setActiveTabState(id);
      onChange?.(id);
    },
    [onChange]
  );

  return (
    <TabsContext.Provider value={{ activeTab, setActiveTab }}>
      <div className="tabs">{children}</div>
    </TabsContext.Provider>
  );
}

// Tab list
interface TabListProps {
  children: ReactNode;
  className?: string;
}

function TabList({ children, className }: TabListProps) {
  return (
    <div role="tablist" className={className}>
      {children}
    </div>
  );
}

// Individual tab
interface TabProps {
  id: string;
  children: ReactNode;
  disabled?: boolean;
}

function Tab({ id, children, disabled }: TabProps) {
  const { activeTab, setActiveTab } = useTabsContext();
  const isActive = activeTab === id;

  return (
    <button
      role="tab"
      aria-selected={isActive}
      aria-controls={`panel-${id}`}
      id={`tab-${id}`}
      tabIndex={isActive ? 0 : -1}
      disabled={disabled}
      onClick={() => setActiveTab(id)}
      className={isActive ? "tab-active" : "tab"}
    >
      {children}
    </button>
  );
}

// Tab panel
interface TabPanelProps {
  id: string;
  children: ReactNode;
}

function TabPanel({ id, children }: TabPanelProps) {
  const { activeTab } = useTabsContext();
  const isActive = activeTab === id;

  if (!isActive) return null;

  return (
    <div
      role="tabpanel"
      id={`panel-${id}`}
      aria-labelledby={`tab-${id}`}
      tabIndex={0}
    >
      {children}
    </div>
  );
}

// Export compound component
export const TabsComponent = Object.assign(Tabs, {
  List: TabList,
  Tab,
  Panel: TabPanel,
});

// Usage example:
// <Tabs defaultTab="tab1">
//   <Tabs.List>
//     <Tabs.Tab id="tab1">Tab 1</Tabs.Tab>
//     <Tabs.Tab id="tab2">Tab 2</Tabs.Tab>
//   </Tabs.List>
//   <Tabs.Panel id="tab1">Content 1</Tabs.Panel>
//   <Tabs.Panel id="tab2">Content 2</Tabs.Panel>
// </Tabs>
```

### Render Props Pattern
```tsx
// components/DataFetcher.tsx
import { useState, useEffect, type ReactNode } from "react";

interface DataFetcherProps<T> {
  url: string;
  children: (state: {
    data: T | null;
    isLoading: boolean;
    error: Error | null;
    refetch: () => void;
  }) => ReactNode;
}

function DataFetcher<T>({ url, children }: DataFetcherProps<T>) {
  const [data, setData] = useState<T | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  const fetchData = async () => {
    setIsLoading(true);
    setError(null);
    
    try {
      const response = await fetch(url);
      if (!response.ok) throw new Error("Fetch failed");
      const json = await response.json();
      setData(json);
    } catch (e) {
      setError(e instanceof Error ? e : new Error("Unknown error"));
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, [url]);

  return <>{children({ data, isLoading, error, refetch: fetchData })}</>;
}

// Usage:
// <DataFetcher<User[]> url="/api/users">
//   {({ data, isLoading, error, refetch }) => {
//     if (isLoading) return <Spinner />;
//     if (error) return <Error message={error.message} retry={refetch} />;
//     return <UserList users={data!} />;
//   }}
// </DataFetcher>
```

### Polymorphic Component
```tsx
// components/Box.tsx
import { forwardRef, type ElementType, type ComponentPropsWithoutRef } from "react";

type BoxProps<E extends ElementType = "div"> = {
  as?: E;
  children?: React.ReactNode;
} & Omit<ComponentPropsWithoutRef<E>, "as">;

type BoxComponent = <E extends ElementType = "div">(
  props: BoxProps<E> & { ref?: React.Ref<Element> }
) => React.ReactNode;

const Box: BoxComponent = forwardRef(function Box<E extends ElementType = "div">(
  { as, children, ...props }: BoxProps<E>,
  ref: React.Ref<Element>
) {
  const Component = as || "div";
  return (
    <Component ref={ref} {...props}>
      {children}
    </Component>
  );
});

// Usage:
// <Box>Default div</Box>
// <Box as="section" id="main">Section element</Box>
// <Box as="a" href="/link">Anchor element</Box>
// <Box as={CustomComponent} customProp="value">Custom</Box>
```

---

## Custom Hooks

### useAsync Hook
```tsx
// hooks/useAsync.ts
import { useState, useCallback, useEffect } from "react";

interface AsyncState<T> {
  data: T | null;
  error: Error | null;
  status: "idle" | "loading" | "success" | "error";
}

interface UseAsyncReturn<T> extends AsyncState<T> {
  execute: () => Promise<void>;
  reset: () => void;
}

function useAsync<T>(
  asyncFn: () => Promise<T>,
  immediate = false
): UseAsyncReturn<T> {
  const [state, setState] = useState<AsyncState<T>>({
    data: null,
    error: null,
    status: "idle",
  });

  const execute = useCallback(async () => {
    setState({ data: null, error: null, status: "loading" });
    
    try {
      const data = await asyncFn();
      setState({ data, error: null, status: "success" });
    } catch (error) {
      setState({
        data: null,
        error: error instanceof Error ? error : new Error(String(error)),
        status: "error",
      });
    }
  }, [asyncFn]);

  const reset = useCallback(() => {
    setState({ data: null, error: null, status: "idle" });
  }, []);

  useEffect(() => {
    if (immediate) {
      execute();
    }
  }, [execute, immediate]);

  return { ...state, execute, reset };
}

export { useAsync };
```

### useDebounce Hook
```tsx
// hooks/useDebounce.ts
import { useState, useEffect } from "react";

function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => {
      clearTimeout(timer);
    };
  }, [value, delay]);

  return debouncedValue;
}

// With callback version
function useDebouncedCallback<T extends (...args: any[]) => any>(
  callback: T,
  delay: number
): T {
  const [timeoutId, setTimeoutId] = useState<NodeJS.Timeout | null>(null);

  const debouncedCallback = useCallback(
    (...args: Parameters<T>) => {
      if (timeoutId) {
        clearTimeout(timeoutId);
      }
      
      const id = setTimeout(() => {
        callback(...args);
      }, delay);
      
      setTimeoutId(id);
    },
    [callback, delay, timeoutId]
  ) as T;

  useEffect(() => {
    return () => {
      if (timeoutId) {
        clearTimeout(timeoutId);
      }
    };
  }, [timeoutId]);

  return debouncedCallback;
}

export { useDebounce, useDebouncedCallback };
```

### useLocalStorage Hook
```tsx
// hooks/useLocalStorage.ts
import { useState, useCallback, useEffect } from "react";

function useLocalStorage<T>(
  key: string,
  initialValue: T
): [T, (value: T | ((prev: T) => T)) => void, () => void] {
  // Get initial value
  const [storedValue, setStoredValue] = useState<T>(() => {
    if (typeof window === "undefined") return initialValue;
    
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch {
      return initialValue;
    }
  });

  // Set value
  const setValue = useCallback(
    (value: T | ((prev: T) => T)) => {
      setStoredValue((prev) => {
        const valueToStore = value instanceof Function ? value(prev) : value;
        
        if (typeof window !== "undefined") {
          window.localStorage.setItem(key, JSON.stringify(valueToStore));
        }
        
        return valueToStore;
      });
    },
    [key]
  );

  // Remove value
  const removeValue = useCallback(() => {
    setStoredValue(initialValue);
    if (typeof window !== "undefined") {
      window.localStorage.removeItem(key);
    }
  }, [key, initialValue]);

  // Sync across tabs
  useEffect(() => {
    const handleStorageChange = (e: StorageEvent) => {
      if (e.key === key && e.newValue !== null) {
        setStoredValue(JSON.parse(e.newValue));
      }
    };

    window.addEventListener("storage", handleStorageChange);
    return () => window.removeEventListener("storage", handleStorageChange);
  }, [key]);

  return [storedValue, setValue, removeValue];
}

export { useLocalStorage };
```

### useMediaQuery Hook
```tsx
// hooks/useMediaQuery.ts
import { useState, useEffect } from "react";

function useMediaQuery(query: string): boolean {
  const [matches, setMatches] = useState(() => {
    if (typeof window === "undefined") return false;
    return window.matchMedia(query).matches;
  });

  useEffect(() => {
    const mediaQuery = window.matchMedia(query);
    
    const handler = (event: MediaQueryListEvent) => {
      setMatches(event.matches);
    };

    // Modern browsers
    mediaQuery.addEventListener("change", handler);
    
    // Set initial value
    setMatches(mediaQuery.matches);

    return () => {
      mediaQuery.removeEventListener("change", handler);
    };
  }, [query]);

  return matches;
}

// Preset hooks
const useIsMobile = () => useMediaQuery("(max-width: 768px)");
const useIsTablet = () => useMediaQuery("(min-width: 769px) and (max-width: 1024px)");
const useIsDesktop = () => useMediaQuery("(min-width: 1025px)");
const usePrefersDark = () => useMediaQuery("(prefers-color-scheme: dark)");
const usePrefersReducedMotion = () => useMediaQuery("(prefers-reduced-motion: reduce)");

export { useMediaQuery, useIsMobile, useIsTablet, useIsDesktop, usePrefersDark, usePrefersReducedMotion };
```

---

## Performance Patterns

### Memoization
```tsx
import { memo, useMemo, useCallback, useState } from "react";

interface Item {
  id: string;
  name: string;
  price: number;
}

interface ItemListProps {
  items: Item[];
  onSelect: (id: string) => void;
  filter: string;
}

// Memoized child component
const ItemRow = memo(function ItemRow({
  item,
  onSelect,
}: {
  item: Item;
  onSelect: (id: string) => void;
}) {
  console.log(`Rendering item: ${item.id}`);
  
  return (
    <tr onClick={() => onSelect(item.id)}>
      <td>{item.name}</td>
      <td>${item.price}</td>
    </tr>
  );
});

// Parent component with proper memoization
function ItemList({ items, onSelect, filter }: ItemListProps) {
  // Memoize filtered items
  const filteredItems = useMemo(() => {
    return items.filter((item) =>
      item.name.toLowerCase().includes(filter.toLowerCase())
    );
  }, [items, filter]);

  // Memoize expensive calculation
  const totalPrice = useMemo(() => {
    return filteredItems.reduce((sum, item) => sum + item.price, 0);
  }, [filteredItems]);

  // Stable callback reference
  const handleSelect = useCallback(
    (id: string) => {
      onSelect(id);
    },
    [onSelect]
  );

  return (
    <div>
      <p>Total: ${totalPrice}</p>
      <table>
        <tbody>
          {filteredItems.map((item) => (
            <ItemRow key={item.id} item={item} onSelect={handleSelect} />
          ))}
        </tbody>
      </table>
    </div>
  );
}
```

### Virtualization
```tsx
// Using @tanstack/react-virtual
import { useVirtualizer } from "@tanstack/react-virtual";
import { useRef } from "react";

interface VirtualListProps<T> {
  items: T[];
  renderItem: (item: T, index: number) => React.ReactNode;
  estimateSize: number;
}

function VirtualList<T>({ items, renderItem, estimateSize }: VirtualListProps<T>) {
  const parentRef = useRef<HTMLDivElement>(null);

  const virtualizer = useVirtualizer({
    count: items.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => estimateSize,
    overscan: 5,
  });

  return (
    <div
      ref={parentRef}
      style={{ height: "400px", overflow: "auto" }}
    >
      <div
        style={{
          height: `${virtualizer.getTotalSize()}px`,
          width: "100%",
          position: "relative",
        }}
      >
        {virtualizer.getVirtualItems().map((virtualItem) => (
          <div
            key={virtualItem.key}
            style={{
              position: "absolute",
              top: 0,
              left: 0,
              width: "100%",
              height: `${virtualItem.size}px`,
              transform: `translateY(${virtualItem.start}px)`,
            }}
          >
            {renderItem(items[virtualItem.index], virtualItem.index)}
          </div>
        ))}
      </div>
    </div>
  );
}
```

### Code Splitting
```tsx
import { lazy, Suspense } from "react";

// Lazy load components
const Dashboard = lazy(() => import("./pages/Dashboard"));
const Settings = lazy(() => import("./pages/Settings"));
const Analytics = lazy(() => import("./pages/Analytics"));

// With named exports
const UserProfile = lazy(() =>
  import("./components/User").then((module) => ({
    default: module.UserProfile,
  }))
);

// Loading component
function PageLoader() {
  return (
    <div className="flex items-center justify-center h-full">
      <div className="animate-spin h-8 w-8 border-4 border-blue-500 rounded-full border-t-transparent" />
    </div>
  );
}

// Router with Suspense
function App() {
  return (
    <Suspense fallback={<PageLoader />}>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/settings" element={<Settings />} />
        <Route path="/analytics" element={<Analytics />} />
        <Route path="/profile" element={<UserProfile />} />
      </Routes>
    </Suspense>
  );
}
```

---

## Accessibility Patterns

### Focus Management
```tsx
import { useRef, useEffect } from "react";

interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  children: React.ReactNode;
  title: string;
}

function Modal({ isOpen, onClose, children, title }: ModalProps) {
  const modalRef = useRef<HTMLDivElement>(null);
  const previousActiveElement = useRef<HTMLElement | null>(null);

  // Trap focus and handle escape
  useEffect(() => {
    if (!isOpen) return;

    // Store currently focused element
    previousActiveElement.current = document.activeElement as HTMLElement;

    // Focus modal
    modalRef.current?.focus();

    // Handle escape key
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        onClose();
      }

      // Trap focus
      if (e.key === "Tab") {
        const focusableElements = modalRef.current?.querySelectorAll(
          'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
        );
        
        if (!focusableElements?.length) return;

        const firstElement = focusableElements[0] as HTMLElement;
        const lastElement = focusableElements[focusableElements.length - 1] as HTMLElement;

        if (e.shiftKey && document.activeElement === firstElement) {
          e.preventDefault();
          lastElement.focus();
        } else if (!e.shiftKey && document.activeElement === lastElement) {
          e.preventDefault();
          firstElement.focus();
        }
      }
    };

    document.addEventListener("keydown", handleKeyDown);

    return () => {
      document.removeEventListener("keydown", handleKeyDown);
      // Restore focus
      previousActiveElement.current?.focus();
    };
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    <div
      className="fixed inset-0 bg-black/50 flex items-center justify-center"
      onClick={onClose}
      role="presentation"
    >
      <div
        ref={modalRef}
        role="dialog"
        aria-modal="true"
        aria-labelledby="modal-title"
        tabIndex={-1}
        onClick={(e) => e.stopPropagation()}
        className="bg-white rounded-lg p-6 max-w-md w-full"
      >
        <h2 id="modal-title" className="text-xl font-bold mb-4">
          {title}
        </h2>
        {children}
        <button
          onClick={onClose}
          className="mt-4 px-4 py-2 bg-gray-200 rounded"
        >
          Close
        </button>
      </div>
    </div>
  );
}
```

### Accessible Form
```tsx
import { useId, useState } from "react";

interface FormFieldProps {
  label: string;
  error?: string;
  required?: boolean;
  children: (props: {
    id: string;
    "aria-describedby"?: string;
    "aria-invalid"?: boolean;
    "aria-required"?: boolean;
  }) => React.ReactNode;
}

function FormField({ label, error, required, children }: FormFieldProps) {
  const id = useId();
  const errorId = `${id}-error`;
  const descriptionId = `${id}-description`;

  return (
    <div className="mb-4">
      <label htmlFor={id} className="block font-medium mb-1">
        {label}
        {required && <span aria-hidden="true" className="text-red-500 ml-1">*</span>}
      </label>
      
      {children({
        id,
        "aria-describedby": error ? errorId : undefined,
        "aria-invalid": error ? true : undefined,
        "aria-required": required,
      })}
      
      {error && (
        <p id={errorId} role="alert" className="text-red-500 text-sm mt-1">
          {error}
        </p>
      )}
    </div>
  );
}

// Usage
function ContactForm() {
  const [errors, setErrors] = useState<Record<string, string>>({});

  return (
    <form>
      <FormField label="Name" error={errors.name} required>
        {(props) => (
          <input
            type="text"
            className="w-full border rounded p-2"
            {...props}
          />
        )}
      </FormField>

      <FormField label="Email" error={errors.email} required>
        {(props) => (
          <input
            type="email"
            className="w-full border rounded p-2"
            {...props}
          />
        )}
      </FormField>

      <FormField label="Message" error={errors.message}>
        {(props) => (
          <textarea
            className="w-full border rounded p-2"
            rows={4}
            {...props}
          />
        )}
      </FormField>

      <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">
        Send Message
      </button>
    </form>
  );
}
```

---

## State Management

### Context + Reducer Pattern
```tsx
import {
  createContext,
  useContext,
  useReducer,
  type ReactNode,
  type Dispatch,
} from "react";

// Types
interface User {
  id: string;
  name: string;
  email: string;
}

interface AuthState {
  user: User | null;
  isLoading: boolean;
  error: string | null;
}

type AuthAction =
  | { type: "LOGIN_START" }
  | { type: "LOGIN_SUCCESS"; payload: User }
  | { type: "LOGIN_ERROR"; payload: string }
  | { type: "LOGOUT" };

// Reducer
function authReducer(state: AuthState, action: AuthAction): AuthState {
  switch (action.type) {
    case "LOGIN_START":
      return { ...state, isLoading: true, error: null };
    case "LOGIN_SUCCESS":
      return { user: action.payload, isLoading: false, error: null };
    case "LOGIN_ERROR":
      return { user: null, isLoading: false, error: action.payload };
    case "LOGOUT":
      return { user: null, isLoading: false, error: null };
    default:
      return state;
  }
}

// Context
const AuthContext = createContext<{
  state: AuthState;
  dispatch: Dispatch<AuthAction>;
} | null>(null);

// Provider
function AuthProvider({ children }: { children: ReactNode }) {
  const [state, dispatch] = useReducer(authReducer, {
    user: null,
    isLoading: false,
    error: null,
  });

  return (
    <AuthContext.Provider value={{ state, dispatch }}>
      {children}
    </AuthContext.Provider>
  );
}

// Hook
function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within AuthProvider");
  }
  return context;
}

// Action creators
function useAuthActions() {
  const { dispatch } = useAuth();

  const login = async (email: string, password: string) => {
    dispatch({ type: "LOGIN_START" });
    try {
      const response = await fetch("/api/login", {
        method: "POST",
        body: JSON.stringify({ email, password }),
      });
      const user = await response.json();
      dispatch({ type: "LOGIN_SUCCESS", payload: user });
    } catch (error) {
      dispatch({ type: "LOGIN_ERROR", payload: "Login failed" });
    }
  };

  const logout = () => {
    dispatch({ type: "LOGOUT" });
  };

  return { login, logout };
}

export { AuthProvider, useAuth, useAuthActions };
```

---

## Report Template

```markdown
# React Component Review — {{COMPONENT_NAME}}

**Date**: {{DATE}}
**Type**: {{COMPONENT_TYPE}}

## Summary

| Aspect | Status | Notes |
|--------|--------|-------|
| Structure | 🟢/🟡/🔴 | {{NOTES}} |
| Types | 🟢/🟡/🔴 | {{NOTES}} |
| Performance | 🟢/🟡/🔴 | {{NOTES}} |
| Accessibility | 🟢/🟡/🔴 | {{NOTES}} |

## Issues Found
{{ISSUES}}

## Recommendations
{{RECOMMENDATIONS}}

## Refactored Code
{{CODE}}
```

---

## Best Practices Checklist

### Structure
- [ ] Single responsibility
- [ ] Proper composition
- [ ] Reasonable component size
- [ ] Clear prop interface

### Performance
- [ ] Memoization where needed
- [ ] No unnecessary re-renders
- [ ] Code splitting for routes
- [ ] Virtualization for long lists

### Accessibility
- [ ] Semantic HTML
- [ ] ARIA attributes
- [ ] Keyboard navigation
- [ ] Focus management

### Testing
- [ ] Unit tests for logic
- [ ] Integration tests for interactions
- [ ] Accessibility tests

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | Missing key props, memory leaks, broken accessibility |
| **High** | 🟠 | Excessive re-renders, missing error boundaries |
| **Medium** | 🟡 | Missing memoization, suboptimal structure |
| **Low** | 🟢 | Minor naming, documentation gaps |

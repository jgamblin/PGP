# State Management — Zustand, Jotai & TanStack Query

> **Purpose**: Modern state management patterns for React applications  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Client state, server state, global state  
> **Last Updated**: 2026-03

---

## Mission

Help implement **scalable, maintainable** state management using modern libraries that embrace React's mental model.

---

## Guard Clauses

**If no state requirements provided:**
```
NO_STATE_CONTEXT

Provide state management context:
- What data needs to be managed
- Sync or async requirements
- Scope (local, feature, global)
- Current pain points

Cannot recommend patterns without context.
```

**If state management is well-designed:**
```
STATE_APPROVED

✅ State management review complete — well-architected.

Checks performed:
- Separation: ✓ (client vs server state)
- Simplicity: ✓ (minimal boilerplate)
- Performance: ✓ (selective updates)
- DX: ✓ (good debugging, TypeScript)

State architecture follows best practices.
```

---

## State Management Decision Tree

```text
┌─────────────────────────────────────────────────────────────┐
│                    What kind of state?                      │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
   Server State          UI State            Complex Forms
        │                     │                     │
        ▼                     ▼                     ▼
  TanStack Query       Local: useState       React Hook Form
  (fetch, cache,       Global: Zustand            + Zod
   sync, mutations)    Atomic: Jotai

Server State: Data from API (users, posts, settings)
→ Use TanStack Query

UI State: Theme, sidebar, modals, selections
→ Use Zustand (simple global) or Jotai (atomic)

Form State: Complex forms with validation
→ Use React Hook Form + Zod
```

---

## Copy-Paste Prompts

### Prompt: Design State Architecture
```text
Design state management for this feature:

Feature: {{FEATURE_DESCRIPTION}}

Data types:
{{DATA_TYPES}}

Requirements:
- {{SYNC_ASYNC}}
- {{PERSISTENCE_NEEDS}}
- {{PERFORMANCE_REQUIREMENTS}}

Provide:
1. State library recommendation with reasoning
2. Store/query structure
3. TypeScript types
4. Usage examples
5. Testing approach
```

### Prompt: Migrate to Modern State
```text
Migrate this Redux/Context code to modern state:

{{CURRENT_CODE}}

Target: {{ZUSTAND/JOTAI/TANSTACK}}

Requirements:
- Maintain existing behavior
- Improve TypeScript support
- Reduce boilerplate
- Better performance

Provide migration plan with code.
```

### Prompt: Review State Management
```text
Review this state management implementation:

{{CODE}}

Check for:
1. **Architecture**
   - Client vs server state separation
   - Appropriate library choice
   - Store organization

2. **Performance**
   - Unnecessary re-renders
   - Selector optimization
   - Caching strategy

3. **DX**
   - TypeScript usage
   - DevTools support
   - Testing approach

Rate: 🟢 Good | 🟡 Needs work | 🔴 Anti-pattern
```

---

## Zustand — Client State

### Basic Store
```typescript
// stores/counterStore.ts
import { create } from "zustand";

interface CounterState {
  count: number;
  increment: () => void;
  decrement: () => void;
  reset: () => void;
  incrementBy: (amount: number) => void;
}

export const useCounterStore = create<CounterState>((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
  decrement: () => set((state) => ({ count: state.count - 1 })),
  reset: () => set({ count: 0 }),
  incrementBy: (amount) => set((state) => ({ count: state.count + amount })),
}));

// Usage
function Counter() {
  const { count, increment, decrement } = useCounterStore();
  
  return (
    <div>
      <span>{count}</span>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
    </div>
  );
}
```

### Store with Slices
```typescript
// stores/appStore.ts
import { create } from "zustand";
import { devtools, persist } from "zustand/middleware";
import { immer } from "zustand/middleware/immer";

// User slice
interface UserSlice {
  user: User | null;
  setUser: (user: User | null) => void;
  updateProfile: (updates: Partial<User>) => void;
}

const createUserSlice = (set: any): UserSlice => ({
  user: null,
  setUser: (user) => set({ user }),
  updateProfile: (updates) =>
    set((state: any) => {
      if (state.user) {
        state.user = { ...state.user, ...updates };
      }
    }),
});

// UI slice
interface UISlice {
  theme: "light" | "dark";
  sidebarOpen: boolean;
  toggleTheme: () => void;
  toggleSidebar: () => void;
}

const createUISlice = (set: any): UISlice => ({
  theme: "light",
  sidebarOpen: true,
  toggleTheme: () =>
    set((state: any) => ({
      theme: state.theme === "light" ? "dark" : "light",
    })),
  toggleSidebar: () =>
    set((state: any) => ({ sidebarOpen: !state.sidebarOpen })),
});

// Notifications slice
interface NotificationsSlice {
  notifications: Notification[];
  addNotification: (notification: Omit<Notification, "id">) => void;
  removeNotification: (id: string) => void;
  clearNotifications: () => void;
}

const createNotificationsSlice = (set: any): NotificationsSlice => ({
  notifications: [],
  addNotification: (notification) =>
    set((state: any) => {
      state.notifications.push({
        ...notification,
        id: crypto.randomUUID(),
      });
    }),
  removeNotification: (id) =>
    set((state: any) => {
      state.notifications = state.notifications.filter(
        (n: Notification) => n.id !== id
      );
    }),
  clearNotifications: () => set({ notifications: [] }),
});

// Combined store
type AppStore = UserSlice & UISlice & NotificationsSlice;

export const useAppStore = create<AppStore>()(
  devtools(
    persist(
      immer((set) => ({
        ...createUserSlice(set),
        ...createUISlice(set),
        ...createNotificationsSlice(set),
      })),
      {
        name: "app-store",
        partialize: (state) => ({
          theme: state.theme,
          sidebarOpen: state.sidebarOpen,
        }),
      }
    )
  )
);
```

### Selectors for Performance
```typescript
// stores/todoStore.ts
import { create } from "zustand";
import { shallow } from "zustand/shallow";

interface Todo {
  id: string;
  text: string;
  completed: boolean;
}

interface TodoState {
  todos: Todo[];
  filter: "all" | "active" | "completed";
  addTodo: (text: string) => void;
  toggleTodo: (id: string) => void;
  removeTodo: (id: string) => void;
  setFilter: (filter: "all" | "active" | "completed") => void;
}

export const useTodoStore = create<TodoState>((set) => ({
  todos: [],
  filter: "all",
  addTodo: (text) =>
    set((state) => ({
      todos: [
        ...state.todos,
        { id: crypto.randomUUID(), text, completed: false },
      ],
    })),
  toggleTodo: (id) =>
    set((state) => ({
      todos: state.todos.map((todo) =>
        todo.id === id ? { ...todo, completed: !todo.completed } : todo
      ),
    })),
  removeTodo: (id) =>
    set((state) => ({
      todos: state.todos.filter((todo) => todo.id !== id),
    })),
  setFilter: (filter) => set({ filter }),
}));

// Computed selectors (outside component)
export const selectFilteredTodos = (state: TodoState) => {
  switch (state.filter) {
    case "active":
      return state.todos.filter((t) => !t.completed);
    case "completed":
      return state.todos.filter((t) => t.completed);
    default:
      return state.todos;
  }
};

export const selectTodoStats = (state: TodoState) => ({
  total: state.todos.length,
  completed: state.todos.filter((t) => t.completed).length,
  active: state.todos.filter((t) => !t.completed).length,
});

// Usage with selectors
function TodoList() {
  // Only re-renders when filtered todos change
  const filteredTodos = useTodoStore(selectFilteredTodos);
  
  return (
    <ul>
      {filteredTodos.map((todo) => (
        <TodoItem key={todo.id} todo={todo} />
      ))}
    </ul>
  );
}

function TodoStats() {
  // Uses shallow comparison for object
  const stats = useTodoStore(selectTodoStats, shallow);
  
  return (
    <div>
      {stats.completed} of {stats.total} completed
    </div>
  );
}

// Pick specific actions (doesn't cause re-renders)
function AddTodoForm() {
  const addTodo = useTodoStore((state) => state.addTodo);
  // Component doesn't re-render when todos change
}
```

### Async Actions
```typescript
// stores/authStore.ts
import { create } from "zustand";
import { persist } from "zustand/middleware";

interface AuthState {
  user: User | null;
  token: string | null;
  isLoading: boolean;
  error: string | null;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
  register: (data: RegisterData) => Promise<void>;
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set, get) => ({
      user: null,
      token: null,
      isLoading: false,
      error: null,
      
      login: async (email, password) => {
        set({ isLoading: true, error: null });
        
        try {
          const response = await api.login({ email, password });
          set({
            user: response.user,
            token: response.token,
            isLoading: false,
          });
        } catch (error) {
          set({
            isLoading: false,
            error: error instanceof Error ? error.message : "Login failed",
          });
          throw error;
        }
      },
      
      logout: () => {
        set({ user: null, token: null });
        // Clear other stores if needed
        useTodoStore.getState().reset?.();
      },
      
      register: async (data) => {
        set({ isLoading: true, error: null });
        
        try {
          const response = await api.register(data);
          set({
            user: response.user,
            token: response.token,
            isLoading: false,
          });
        } catch (error) {
          set({
            isLoading: false,
            error: error instanceof Error ? error.message : "Registration failed",
          });
          throw error;
        }
      },
    }),
    {
      name: "auth-store",
      partialize: (state) => ({ token: state.token }),
    }
  )
);
```

---

## Jotai — Atomic State

### Basic Atoms
```typescript
// atoms/counterAtoms.ts
import { atom, useAtom, useAtomValue, useSetAtom } from "jotai";

// Primitive atom
export const countAtom = atom(0);

// Derived atom (read-only)
export const doubleCountAtom = atom((get) => get(countAtom) * 2);

// Derived atom (read-write)
export const countWithActionsAtom = atom(
  (get) => get(countAtom),
  (get, set, action: "increment" | "decrement" | "reset") => {
    switch (action) {
      case "increment":
        set(countAtom, get(countAtom) + 1);
        break;
      case "decrement":
        set(countAtom, get(countAtom) - 1);
        break;
      case "reset":
        set(countAtom, 0);
        break;
    }
  }
);

// Usage
function Counter() {
  const [count, dispatch] = useAtom(countWithActionsAtom);
  const doubleCount = useAtomValue(doubleCountAtom);
  
  return (
    <div>
      <span>{count} (double: {doubleCount})</span>
      <button onClick={() => dispatch("increment")}>+</button>
      <button onClick={() => dispatch("decrement")}>-</button>
      <button onClick={() => dispatch("reset")}>Reset</button>
    </div>
  );
}
```

### Atoms with Async
```typescript
// atoms/userAtoms.ts
import { atom } from "jotai";
import { atomWithQuery, atomWithMutation } from "jotai-tanstack-query";

// Async atom (suspense)
export const userAtom = atom(async () => {
  const response = await fetch("/api/user");
  return response.json();
});

// With TanStack Query integration
export const userQueryAtom = atomWithQuery(() => ({
  queryKey: ["user"],
  queryFn: async () => {
    const response = await fetch("/api/user");
    return response.json();
  },
}));

export const updateUserMutationAtom = atomWithMutation(() => ({
  mutationFn: async (updates: Partial<User>) => {
    const response = await fetch("/api/user", {
      method: "PATCH",
      body: JSON.stringify(updates),
    });
    return response.json();
  },
}));

// Usage with Suspense
function UserProfile() {
  const [{ data: user }] = useAtom(userQueryAtom);
  const [, mutate] = useAtom(updateUserMutationAtom);
  
  return (
    <div>
      <h1>{user.name}</h1>
      <button onClick={() => mutate({ name: "New Name" })}>
        Update
      </button>
    </div>
  );
}
```

### Atom Families
```typescript
// atoms/todoAtoms.ts
import { atom } from "jotai";
import { atomFamily, selectAtom } from "jotai/utils";

interface Todo {
  id: string;
  text: string;
  completed: boolean;
}

// Base atom for all todos
export const todosAtom = atom<Todo[]>([]);

// Atom family for individual todos
export const todoAtomFamily = atomFamily((id: string) =>
  atom(
    (get) => get(todosAtom).find((t) => t.id === id),
    (get, set, update: Partial<Todo>) => {
      set(todosAtom, (prev) =>
        prev.map((t) => (t.id === id ? { ...t, ...update } : t))
      );
    }
  )
);

// Filtered atoms
export const filterAtom = atom<"all" | "active" | "completed">("all");

export const filteredTodosAtom = atom((get) => {
  const todos = get(todosAtom);
  const filter = get(filterAtom);
  
  switch (filter) {
    case "active":
      return todos.filter((t) => !t.completed);
    case "completed":
      return todos.filter((t) => t.completed);
    default:
      return todos;
  }
});

// Stats atom
export const todoStatsAtom = atom((get) => {
  const todos = get(todosAtom);
  return {
    total: todos.length,
    completed: todos.filter((t) => t.completed).length,
    active: todos.filter((t) => !t.completed).length,
  };
});

// Usage
function TodoItem({ id }: { id: string }) {
  const [todo, setTodo] = useAtom(todoAtomFamily(id));
  
  if (!todo) return null;
  
  return (
    <li>
      <input
        type="checkbox"
        checked={todo.completed}
        onChange={() => setTodo({ completed: !todo.completed })}
      />
      {todo.text}
    </li>
  );
}
```

### Persistence with Jotai
```typescript
// atoms/settingsAtoms.ts
import { atom } from "jotai";
import { atomWithStorage } from "jotai/utils";

// Persisted to localStorage
export const themeAtom = atomWithStorage<"light" | "dark">("theme", "light");

export const settingsAtom = atomWithStorage("settings", {
  notifications: true,
  language: "en",
  fontSize: 14,
});

// Derived atom that syncs to document
export const themeEffectAtom = atom(
  (get) => get(themeAtom),
  (get, set, newTheme: "light" | "dark") => {
    set(themeAtom, newTheme);
    document.documentElement.classList.toggle("dark", newTheme === "dark");
  }
);
```

---

## TanStack Query — Server State

### Basic Queries
```typescript
// hooks/useUsers.ts
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";

// Query keys factory
export const userKeys = {
  all: ["users"] as const,
  lists: () => [...userKeys.all, "list"] as const,
  list: (filters: UserFilters) => [...userKeys.lists(), filters] as const,
  details: () => [...userKeys.all, "detail"] as const,
  detail: (id: string) => [...userKeys.details(), id] as const,
};

// Fetch users
export function useUsers(filters: UserFilters = {}) {
  return useQuery({
    queryKey: userKeys.list(filters),
    queryFn: () => api.getUsers(filters),
    staleTime: 5 * 60 * 1000, // 5 minutes
  });
}

// Fetch single user
export function useUser(id: string) {
  return useQuery({
    queryKey: userKeys.detail(id),
    queryFn: () => api.getUser(id),
    enabled: Boolean(id),
  });
}

// Create user mutation
export function useCreateUser() {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: (data: CreateUserData) => api.createUser(data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: userKeys.lists() });
    },
  });
}

// Update user mutation
export function useUpdateUser() {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: ({ id, data }: { id: string; data: UpdateUserData }) =>
      api.updateUser(id, data),
    onSuccess: (data, { id }) => {
      // Update specific user cache
      queryClient.setQueryData(userKeys.detail(id), data);
      // Invalidate lists
      queryClient.invalidateQueries({ queryKey: userKeys.lists() });
    },
  });
}

// Delete user mutation
export function useDeleteUser() {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: (id: string) => api.deleteUser(id),
    onSuccess: (_, id) => {
      queryClient.removeQueries({ queryKey: userKeys.detail(id) });
      queryClient.invalidateQueries({ queryKey: userKeys.lists() });
    },
  });
}
```

### Optimistic Updates
```typescript
// hooks/useTodos.ts
export function useToggleTodo() {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: ({ id, completed }: { id: string; completed: boolean }) =>
      api.updateTodo(id, { completed }),
    
    // Optimistic update
    onMutate: async ({ id, completed }) => {
      // Cancel outgoing refetches
      await queryClient.cancelQueries({ queryKey: todoKeys.all });
      
      // Snapshot previous value
      const previousTodos = queryClient.getQueryData(todoKeys.lists());
      
      // Optimistically update
      queryClient.setQueryData(todoKeys.lists(), (old: Todo[] | undefined) =>
        old?.map((todo) =>
          todo.id === id ? { ...todo, completed } : todo
        )
      );
      
      // Return context with snapshot
      return { previousTodos };
    },
    
    // Rollback on error
    onError: (err, variables, context) => {
      if (context?.previousTodos) {
        queryClient.setQueryData(todoKeys.lists(), context.previousTodos);
      }
    },
    
    // Always refetch after error or success
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: todoKeys.all });
    },
  });
}
```

### Infinite Queries
```typescript
// hooks/usePosts.ts
export function usePosts() {
  return useInfiniteQuery({
    queryKey: ["posts"],
    queryFn: ({ pageParam = 1 }) =>
      api.getPosts({ page: pageParam, limit: 10 }),
    getNextPageParam: (lastPage, pages) =>
      lastPage.hasMore ? pages.length + 1 : undefined,
    initialPageParam: 1,
  });
}

// Usage
function PostList() {
  const {
    data,
    fetchNextPage,
    hasNextPage,
    isFetchingNextPage,
    status,
  } = usePosts();
  
  if (status === "pending") return <Spinner />;
  if (status === "error") return <Error />;
  
  return (
    <>
      {data.pages.map((page, i) => (
        <Fragment key={i}>
          {page.posts.map((post) => (
            <PostCard key={post.id} post={post} />
          ))}
        </Fragment>
      ))}
      <button
        onClick={() => fetchNextPage()}
        disabled={!hasNextPage || isFetchingNextPage}
      >
        {isFetchingNextPage
          ? "Loading..."
          : hasNextPage
          ? "Load More"
          : "No more posts"}
      </button>
    </>
  );
}
```

### Query Provider Setup
```typescript
// providers/QueryProvider.tsx
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 1000 * 60, // 1 minute
      gcTime: 1000 * 60 * 5, // 5 minutes (previously cacheTime)
      retry: (failureCount, error) => {
        if (error instanceof ApiError && error.status === 404) {
          return false;
        }
        return failureCount < 3;
      },
      refetchOnWindowFocus: false,
    },
    mutations: {
      retry: false,
    },
  },
});

export function QueryProvider({ children }: { children: React.ReactNode }) {
  return (
    <QueryClientProvider client={queryClient}>
      {children}
      <ReactQueryDevtools initialIsOpen={false} />
    </QueryClientProvider>
  );
}
```

---

## Combining Libraries

### Zustand + TanStack Query
```typescript
// stores/uiStore.ts
import { create } from "zustand";

// UI state in Zustand
interface UIStore {
  selectedUserId: string | null;
  isModalOpen: boolean;
  selectUser: (id: string | null) => void;
  openModal: () => void;
  closeModal: () => void;
}

export const useUIStore = create<UIStore>((set) => ({
  selectedUserId: null,
  isModalOpen: false,
  selectUser: (id) => set({ selectedUserId: id }),
  openModal: () => set({ isModalOpen: true }),
  closeModal: () => set({ isModalOpen: false }),
}));

// hooks/useSelectedUser.ts
// Combine Zustand selection with TanStack Query data
export function useSelectedUser() {
  const selectedUserId = useUIStore((s) => s.selectedUserId);
  
  return useQuery({
    queryKey: userKeys.detail(selectedUserId!),
    queryFn: () => api.getUser(selectedUserId!),
    enabled: Boolean(selectedUserId),
  });
}

// Usage in component
function UserModal() {
  const { isModalOpen, closeModal } = useUIStore();
  const { data: user, isLoading } = useSelectedUser();
  
  if (!isModalOpen) return null;
  
  return (
    <Dialog open={isModalOpen} onClose={closeModal}>
      {isLoading ? <Spinner /> : <UserDetails user={user} />}
    </Dialog>
  );
}
```

### Jotai + TanStack Query
```typescript
// atoms/queryAtoms.ts
import { atom } from "jotai";
import { atomWithQuery } from "jotai-tanstack-query";

// Selection atom
export const selectedUserIdAtom = atom<string | null>(null);

// Query atom that depends on selection
export const selectedUserQueryAtom = atomWithQuery((get) => {
  const id = get(selectedUserIdAtom);
  
  return {
    queryKey: ["user", id],
    queryFn: () => (id ? api.getUser(id) : null),
    enabled: Boolean(id),
  };
});

// Usage
function UserSelector() {
  const [selectedId, setSelectedId] = useAtom(selectedUserIdAtom);
  const [{ data: user, isPending }] = useAtom(selectedUserQueryAtom);
  
  return (
    <div>
      <select
        value={selectedId ?? ""}
        onChange={(e) => setSelectedId(e.target.value || null)}
      >
        <option value="">Select a user</option>
        {users.map((u) => (
          <option key={u.id} value={u.id}>
            {u.name}
          </option>
        ))}
      </select>
      
      {isPending && <Spinner />}
      {user && <UserCard user={user} />}
    </div>
  );
}
```

---

## React Hook Form + Zod

### Form with Validation
```typescript
// components/UserForm.tsx
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";

const userSchema = z.object({
  name: z.string().min(2, "Name must be at least 2 characters"),
  email: z.string().email("Invalid email address"),
  age: z.number().min(18, "Must be at least 18").max(120),
  role: z.enum(["admin", "user", "guest"]),
  preferences: z.object({
    newsletter: z.boolean(),
    notifications: z.boolean(),
  }),
});

type UserFormData = z.infer<typeof userSchema>;

interface UserFormProps {
  defaultValues?: Partial<UserFormData>;
  onSubmit: (data: UserFormData) => Promise<void>;
}

export function UserForm({ defaultValues, onSubmit }: UserFormProps) {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
    reset,
  } = useForm<UserFormData>({
    resolver: zodResolver(userSchema),
    defaultValues: {
      name: "",
      email: "",
      age: 18,
      role: "user",
      preferences: {
        newsletter: false,
        notifications: true,
      },
      ...defaultValues,
    },
  });
  
  const handleFormSubmit = async (data: UserFormData) => {
    await onSubmit(data);
    reset();
  };
  
  return (
    <form onSubmit={handleSubmit(handleFormSubmit)}>
      <div>
        <label htmlFor="name">Name</label>
        <input id="name" {...register("name")} />
        {errors.name && <span role="alert">{errors.name.message}</span>}
      </div>
      
      <div>
        <label htmlFor="email">Email</label>
        <input id="email" type="email" {...register("email")} />
        {errors.email && <span role="alert">{errors.email.message}</span>}
      </div>
      
      <div>
        <label htmlFor="age">Age</label>
        <input
          id="age"
          type="number"
          {...register("age", { valueAsNumber: true })}
        />
        {errors.age && <span role="alert">{errors.age.message}</span>}
      </div>
      
      <div>
        <label htmlFor="role">Role</label>
        <select id="role" {...register("role")}>
          <option value="user">User</option>
          <option value="admin">Admin</option>
          <option value="guest">Guest</option>
        </select>
        {errors.role && <span role="alert">{errors.role.message}</span>}
      </div>
      
      <fieldset>
        <legend>Preferences</legend>
        <label>
          <input type="checkbox" {...register("preferences.newsletter")} />
          Subscribe to newsletter
        </label>
        <label>
          <input type="checkbox" {...register("preferences.notifications")} />
          Enable notifications
        </label>
      </fieldset>
      
      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? "Saving..." : "Save"}
      </button>
    </form>
  );
}
```

### Form with TanStack Query
```typescript
// components/EditUserForm.tsx
export function EditUserForm({ userId }: { userId: string }) {
  const { data: user, isLoading } = useUser(userId);
  const updateUser = useUpdateUser();
  
  const form = useForm<UserFormData>({
    resolver: zodResolver(userSchema),
    values: user, // Syncs form when user data loads
  });
  
  const onSubmit = async (data: UserFormData) => {
    await updateUser.mutateAsync({ id: userId, data });
  };
  
  if (isLoading) return <Spinner />;
  
  return (
    <form onSubmit={form.handleSubmit(onSubmit)}>
      {/* Form fields */}
      <button
        type="submit"
        disabled={form.formState.isSubmitting || updateUser.isPending}
      >
        {updateUser.isPending ? "Updating..." : "Update"}
      </button>
      {updateUser.isError && (
        <div role="alert">{updateUser.error.message}</div>
      )}
    </form>
  );
}
```

---

## Best Practices Checklist

### State Architecture
- [ ] Server state uses TanStack Query
- [ ] Client state uses Zustand or Jotai
- [ ] Form state uses React Hook Form
- [ ] No duplicate state

### Performance
- [ ] Selectors prevent re-renders
- [ ] Queries are cached appropriately
- [ ] Mutations use optimistic updates
- [ ] Components only subscribe to needed state

### Developer Experience
- [ ] Full TypeScript coverage
- [ ] DevTools configured
- [ ] State is testable
- [ ] Clear naming conventions

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | Mixing server/client state incorrectly, no caching, memory leaks |
| **High** | 🟠 | Unnecessary re-renders, missing optimistic updates, poor error handling |
| **Medium** | 🟡 | Suboptimal selectors, missing TypeScript, no DevTools |
| **Low** | 🟢 | Naming improvements, documentation, minor refactors |

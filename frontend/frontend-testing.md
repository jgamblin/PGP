# Frontend Testing — Vitest, RTL & E2E

> **Purpose**: Modern frontend testing with Vitest, React Testing Library, and Playwright  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Unit tests, component tests, integration tests, E2E tests  
> **Last Updated**: 2026-03

---

## Mission

Generate **reliable, maintainable** frontend tests that validate behavior without coupling to implementation details.

---

## Guard Clauses

**If no testable code provided:**
```
NO_TESTABLE_CODE

Provide code to test:
- Component code
- Hook implementation
- Utility function
- User flow description

Cannot generate tests without context.
```

**If tests are comprehensive:**
```
TESTS_APPROVED

✅ Test suite review complete — comprehensive coverage.

Coverage:
- Unit tests: ✓ (utilities, hooks)
- Component tests: ✓ (user behavior)
- Integration tests: ✓ (feature flows)
- Edge cases: ✓ (errors, loading, empty states)

Tests follow best practices.
```

---

## Testing Philosophy

```text
The more your tests resemble the way your software is used,
the more confidence they can give you.
— Kent C. Dodds

✅ Test behavior, not implementation
✅ Query like users (roles, text, labels)
✅ Avoid testing implementation details
✅ Use real DOM events
✅ Focus on user outcomes
```

---

## Copy-Paste Prompts

### Prompt: Generate Component Tests
```text
Generate tests for this component:

{{COMPONENT_CODE}}

Requirements:
- Use Vitest + React Testing Library
- Test user interactions
- Test accessibility
- Cover edge cases

Include tests for:
1. Default rendering
2. User interactions (clicks, typing)
3. Loading states
4. Error states
5. Edge cases (empty data, long text)

Follow Testing Library best practices.
```

### Prompt: Generate Hook Tests
```text
Generate tests for this custom hook:

{{HOOK_CODE}}

Requirements:
- Use @testing-library/react-hooks
- Test all states
- Test cleanup
- Test error handling

Include tests for:
1. Initial state
2. State transitions
3. Side effects
4. Cleanup
5. Edge cases
```

### Prompt: Generate E2E Tests
```text
Generate Playwright E2E tests for:

User Flow: {{FLOW_DESCRIPTION}}

Pages involved:
{{PAGE_LIST}}

Requirements:
- Test happy path
- Test error scenarios
- Test accessibility
- Cross-browser compatibility

Use Page Object Model pattern.
```

### Prompt: Review Test Quality
```text
Review this test suite:

{{TESTS}}

Check for:
1. **Best Practices**
   - Testing behavior not implementation
   - Using accessible queries
   - Proper assertions
   - Test isolation

2. **Coverage**
   - Happy path
   - Edge cases
   - Error states
   - Accessibility

3. **Maintainability**
   - Clear test names
   - DRY without over-abstraction
   - Readable assertions

Rate: 🟢 Good | 🟡 Needs work | 🔴 Anti-pattern
```

---

## Vitest Configuration

### vitest.config.ts
```typescript
import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";
import { resolve } from "path";

export default defineConfig({
  plugins: [react()],
  test: {
    globals: true,
    environment: "jsdom",
    setupFiles: ["./src/test/setup.ts"],
    include: ["src/**/*.{test,spec}.{js,jsx,ts,tsx}"],
    exclude: ["node_modules", "dist", "e2e"],
    
    // Coverage
    coverage: {
      provider: "v8",
      reporter: ["text", "json", "html", "lcov"],
      exclude: [
        "node_modules/",
        "src/test/",
        "**/*.d.ts",
        "**/*.config.*",
        "**/types/*",
      ],
      thresholds: {
        global: {
          branches: 80,
          functions: 80,
          lines: 80,
          statements: 80,
        },
      },
    },
    
    // Performance
    pool: "threads",
    poolOptions: {
      threads: {
        singleThread: true,
      },
    },
    
    // Watch mode
    watch: false,
    
    // Reporters
    reporters: ["verbose", "html"],
    outputFile: {
      html: "./coverage/test-report.html",
    },
  },
  resolve: {
    alias: {
      "@": resolve(__dirname, "./src"),
    },
  },
});
```

### Test Setup File
```typescript
// src/test/setup.ts
import "@testing-library/jest-dom/vitest";
import { cleanup } from "@testing-library/react";
import { afterEach, beforeAll, vi } from "vitest";

// Cleanup after each test
afterEach(() => {
  cleanup();
});

// Mock window.matchMedia
beforeAll(() => {
  Object.defineProperty(window, "matchMedia", {
    writable: true,
    value: vi.fn().mockImplementation((query) => ({
      matches: false,
      media: query,
      onchange: null,
      addListener: vi.fn(),
      removeListener: vi.fn(),
      addEventListener: vi.fn(),
      removeEventListener: vi.fn(),
      dispatchEvent: vi.fn(),
    })),
  });
});

// Mock IntersectionObserver
beforeAll(() => {
  class MockIntersectionObserver {
    observe = vi.fn();
    unobserve = vi.fn();
    disconnect = vi.fn();
  }
  
  Object.defineProperty(window, "IntersectionObserver", {
    writable: true,
    value: MockIntersectionObserver,
  });
});

// Mock ResizeObserver
beforeAll(() => {
  class MockResizeObserver {
    observe = vi.fn();
    unobserve = vi.fn();
    disconnect = vi.fn();
  }
  
  Object.defineProperty(window, "ResizeObserver", {
    writable: true,
    value: MockResizeObserver,
  });
});

// Suppress console errors in tests (optional)
beforeAll(() => {
  vi.spyOn(console, "error").mockImplementation(() => {});
});
```

---

## Component Testing Patterns

### Basic Component Test
```typescript
// Button.test.tsx
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, it, expect, vi } from "vitest";
import { Button } from "./Button";

describe("Button", () => {
  it("renders with text", () => {
    render(<Button>Click me</Button>);
    
    expect(screen.getByRole("button", { name: /click me/i })).toBeInTheDocument();
  });
  
  it("calls onClick when clicked", async () => {
    const user = userEvent.setup();
    const onClick = vi.fn();
    
    render(<Button onClick={onClick}>Click me</Button>);
    
    await user.click(screen.getByRole("button", { name: /click me/i }));
    
    expect(onClick).toHaveBeenCalledTimes(1);
  });
  
  it("is disabled when disabled prop is true", () => {
    render(<Button disabled>Click me</Button>);
    
    expect(screen.getByRole("button", { name: /click me/i })).toBeDisabled();
  });
  
  it("renders loading state", () => {
    render(<Button loading>Click me</Button>);
    
    expect(screen.getByRole("button")).toHaveAttribute("aria-busy", "true");
    expect(screen.getByText(/loading/i)).toBeInTheDocument();
  });
  
  it("applies variant styles", () => {
    render(<Button variant="destructive">Delete</Button>);
    
    const button = screen.getByRole("button", { name: /delete/i });
    expect(button).toHaveClass("bg-red-500");
  });
});
```

### Form Component Test
```typescript
// LoginForm.test.tsx
import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, it, expect, vi, beforeEach } from "vitest";
import { LoginForm } from "./LoginForm";

describe("LoginForm", () => {
  const mockOnSubmit = vi.fn();
  
  beforeEach(() => {
    mockOnSubmit.mockClear();
  });
  
  it("renders email and password fields", () => {
    render(<LoginForm onSubmit={mockOnSubmit} />);
    
    expect(screen.getByLabelText(/email/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/password/i)).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /sign in/i })).toBeInTheDocument();
  });
  
  it("submits form with valid data", async () => {
    const user = userEvent.setup();
    render(<LoginForm onSubmit={mockOnSubmit} />);
    
    await user.type(screen.getByLabelText(/email/i), "user@example.com");
    await user.type(screen.getByLabelText(/password/i), "password123");
    await user.click(screen.getByRole("button", { name: /sign in/i }));
    
    await waitFor(() => {
      expect(mockOnSubmit).toHaveBeenCalledWith({
        email: "user@example.com",
        password: "password123",
      });
    });
  });
  
  it("shows validation errors for empty fields", async () => {
    const user = userEvent.setup();
    render(<LoginForm onSubmit={mockOnSubmit} />);
    
    await user.click(screen.getByRole("button", { name: /sign in/i }));
    
    expect(await screen.findByText(/email is required/i)).toBeInTheDocument();
    expect(await screen.findByText(/password is required/i)).toBeInTheDocument();
    expect(mockOnSubmit).not.toHaveBeenCalled();
  });
  
  it("shows error for invalid email format", async () => {
    const user = userEvent.setup();
    render(<LoginForm onSubmit={mockOnSubmit} />);
    
    await user.type(screen.getByLabelText(/email/i), "invalid-email");
    await user.type(screen.getByLabelText(/password/i), "password123");
    await user.click(screen.getByRole("button", { name: /sign in/i }));
    
    expect(await screen.findByText(/invalid email/i)).toBeInTheDocument();
  });
  
  it("disables submit button while submitting", async () => {
    const user = userEvent.setup();
    mockOnSubmit.mockImplementation(() => new Promise((resolve) => setTimeout(resolve, 100)));
    
    render(<LoginForm onSubmit={mockOnSubmit} />);
    
    await user.type(screen.getByLabelText(/email/i), "user@example.com");
    await user.type(screen.getByLabelText(/password/i), "password123");
    await user.click(screen.getByRole("button", { name: /sign in/i }));
    
    expect(screen.getByRole("button", { name: /signing in/i })).toBeDisabled();
  });
});
```

### Async Component Test
```typescript
// UserProfile.test.tsx
import { render, screen, waitFor } from "@testing-library/react";
import { describe, it, expect, vi, beforeEach } from "vitest";
import { UserProfile } from "./UserProfile";
import * as api from "@/lib/api";

// Mock the API module
vi.mock("@/lib/api");

describe("UserProfile", () => {
  beforeEach(() => {
    vi.resetAllMocks();
  });
  
  it("shows loading state initially", () => {
    vi.mocked(api.fetchUser).mockImplementation(
      () => new Promise(() => {}) // Never resolves
    );
    
    render(<UserProfile userId="123" />);
    
    expect(screen.getByRole("status")).toHaveTextContent(/loading/i);
  });
  
  it("displays user data after loading", async () => {
    vi.mocked(api.fetchUser).mockResolvedValue({
      id: "123",
      name: "John Doe",
      email: "john@example.com",
    });
    
    render(<UserProfile userId="123" />);
    
    expect(await screen.findByText("John Doe")).toBeInTheDocument();
    expect(screen.getByText("john@example.com")).toBeInTheDocument();
  });
  
  it("shows error message on API failure", async () => {
    vi.mocked(api.fetchUser).mockRejectedValue(new Error("Failed to fetch"));
    
    render(<UserProfile userId="123" />);
    
    expect(await screen.findByRole("alert")).toHaveTextContent(/failed to fetch/i);
  });
  
  it("refetches when userId changes", async () => {
    vi.mocked(api.fetchUser).mockResolvedValue({
      id: "123",
      name: "John Doe",
      email: "john@example.com",
    });
    
    const { rerender } = render(<UserProfile userId="123" />);
    
    await screen.findByText("John Doe");
    expect(api.fetchUser).toHaveBeenCalledWith("123");
    
    vi.mocked(api.fetchUser).mockResolvedValue({
      id: "456",
      name: "Jane Smith",
      email: "jane@example.com",
    });
    
    rerender(<UserProfile userId="456" />);
    
    expect(await screen.findByText("Jane Smith")).toBeInTheDocument();
    expect(api.fetchUser).toHaveBeenCalledWith("456");
  });
});
```

---

## Custom Hook Testing

### Hook Test Setup
```typescript
// useCounter.test.ts
import { renderHook, act } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import { useCounter } from "./useCounter";

describe("useCounter", () => {
  it("initializes with default value", () => {
    const { result } = renderHook(() => useCounter());
    
    expect(result.current.count).toBe(0);
  });
  
  it("initializes with provided value", () => {
    const { result } = renderHook(() => useCounter(10));
    
    expect(result.current.count).toBe(10);
  });
  
  it("increments count", () => {
    const { result } = renderHook(() => useCounter());
    
    act(() => {
      result.current.increment();
    });
    
    expect(result.current.count).toBe(1);
  });
  
  it("decrements count", () => {
    const { result } = renderHook(() => useCounter(5));
    
    act(() => {
      result.current.decrement();
    });
    
    expect(result.current.count).toBe(4);
  });
  
  it("resets to initial value", () => {
    const { result } = renderHook(() => useCounter(10));
    
    act(() => {
      result.current.increment();
      result.current.increment();
      result.current.reset();
    });
    
    expect(result.current.count).toBe(10);
  });
});
```

### Async Hook Test
```typescript
// useAsync.test.ts
import { renderHook, waitFor } from "@testing-library/react";
import { describe, it, expect, vi } from "vitest";
import { useAsync } from "./useAsync";

describe("useAsync", () => {
  it("handles successful async operation", async () => {
    const asyncFn = vi.fn().mockResolvedValue({ data: "success" });
    
    const { result } = renderHook(() => useAsync(asyncFn));
    
    expect(result.current.status).toBe("idle");
    
    // Execute the async function
    result.current.execute();
    
    expect(result.current.status).toBe("pending");
    
    await waitFor(() => {
      expect(result.current.status).toBe("success");
    });
    
    expect(result.current.data).toEqual({ data: "success" });
    expect(result.current.error).toBeNull();
  });
  
  it("handles failed async operation", async () => {
    const error = new Error("Something went wrong");
    const asyncFn = vi.fn().mockRejectedValue(error);
    
    const { result } = renderHook(() => useAsync(asyncFn));
    
    result.current.execute();
    
    await waitFor(() => {
      expect(result.current.status).toBe("error");
    });
    
    expect(result.current.error).toBe(error);
    expect(result.current.data).toBeNull();
  });
  
  it("executes immediately when immediate is true", async () => {
    const asyncFn = vi.fn().mockResolvedValue("data");
    
    const { result } = renderHook(() => useAsync(asyncFn, { immediate: true }));
    
    await waitFor(() => {
      expect(result.current.status).toBe("success");
    });
    
    expect(asyncFn).toHaveBeenCalledTimes(1);
  });
});
```

### Hook with Context
```typescript
// useAuth.test.tsx
import { renderHook, act, waitFor } from "@testing-library/react";
import { describe, it, expect, vi } from "vitest";
import { AuthProvider, useAuth } from "./useAuth";
import * as authApi from "@/lib/auth-api";

vi.mock("@/lib/auth-api");

const wrapper = ({ children }: { children: React.ReactNode }) => (
  <AuthProvider>{children}</AuthProvider>
);

describe("useAuth", () => {
  it("provides initial unauthenticated state", () => {
    const { result } = renderHook(() => useAuth(), { wrapper });
    
    expect(result.current.isAuthenticated).toBe(false);
    expect(result.current.user).toBeNull();
  });
  
  it("logs in user successfully", async () => {
    vi.mocked(authApi.login).mockResolvedValue({
      user: { id: "1", name: "John", email: "john@example.com" },
      token: "abc123",
    });
    
    const { result } = renderHook(() => useAuth(), { wrapper });
    
    act(() => {
      result.current.login("john@example.com", "password");
    });
    
    await waitFor(() => {
      expect(result.current.isAuthenticated).toBe(true);
    });
    
    expect(result.current.user?.name).toBe("John");
  });
  
  it("handles login error", async () => {
    vi.mocked(authApi.login).mockRejectedValue(new Error("Invalid credentials"));
    
    const { result } = renderHook(() => useAuth(), { wrapper });
    
    act(() => {
      result.current.login("john@example.com", "wrong");
    });
    
    await waitFor(() => {
      expect(result.current.error).toBe("Invalid credentials");
    });
    
    expect(result.current.isAuthenticated).toBe(false);
  });
  
  it("logs out user", async () => {
    vi.mocked(authApi.login).mockResolvedValue({
      user: { id: "1", name: "John", email: "john@example.com" },
      token: "abc123",
    });
    
    const { result } = renderHook(() => useAuth(), { wrapper });
    
    // Login first
    act(() => {
      result.current.login("john@example.com", "password");
    });
    
    await waitFor(() => {
      expect(result.current.isAuthenticated).toBe(true);
    });
    
    // Then logout
    act(() => {
      result.current.logout();
    });
    
    expect(result.current.isAuthenticated).toBe(false);
    expect(result.current.user).toBeNull();
  });
});
```

---

## E2E Testing with Playwright

### Playwright Configuration
```typescript
// playwright.config.ts
import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  testDir: "./e2e",
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: [
    ["html", { open: "never" }],
    ["json", { outputFile: "test-results/results.json" }],
  ],
  
  use: {
    baseURL: "http://localhost:3000",
    trace: "on-first-retry",
    screenshot: "only-on-failure",
    video: "on-first-retry",
  },
  
  projects: [
    // Setup project for authentication
    {
      name: "setup",
      testMatch: /.*\.setup\.ts/,
    },
    {
      name: "chromium",
      use: { ...devices["Desktop Chrome"] },
      dependencies: ["setup"],
    },
    {
      name: "firefox",
      use: { ...devices["Desktop Firefox"] },
      dependencies: ["setup"],
    },
    {
      name: "webkit",
      use: { ...devices["Desktop Safari"] },
      dependencies: ["setup"],
    },
    {
      name: "Mobile Chrome",
      use: { ...devices["Pixel 5"] },
      dependencies: ["setup"],
    },
  ],
  
  webServer: {
    command: "npm run dev",
    url: "http://localhost:3000",
    reuseExistingServer: !process.env.CI,
  },
});
```

### Page Object Model
```typescript
// e2e/pages/LoginPage.ts
import { type Page, type Locator, expect } from "@playwright/test";

export class LoginPage {
  private readonly page: Page;
  private readonly emailInput: Locator;
  private readonly passwordInput: Locator;
  private readonly submitButton: Locator;
  private readonly errorMessage: Locator;
  
  constructor(page: Page) {
    this.page = page;
    this.emailInput = page.getByLabel("Email");
    this.passwordInput = page.getByLabel("Password");
    this.submitButton = page.getByRole("button", { name: "Sign in" });
    this.errorMessage = page.getByRole("alert");
  }
  
  async goto() {
    await this.page.goto("/login");
  }
  
  async login(email: string, password: string) {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password);
    await this.submitButton.click();
  }
  
  async expectError(message: string) {
    await expect(this.errorMessage).toHaveText(message);
  }
  
  async expectLoggedIn() {
    await expect(this.page).toHaveURL("/dashboard");
  }
}

// e2e/pages/DashboardPage.ts
import { type Page, type Locator, expect } from "@playwright/test";

export class DashboardPage {
  private readonly page: Page;
  private readonly welcomeMessage: Locator;
  private readonly logoutButton: Locator;
  
  constructor(page: Page) {
    this.page = page;
    this.welcomeMessage = page.getByRole("heading", { name: /welcome/i });
    this.logoutButton = page.getByRole("button", { name: "Logout" });
  }
  
  async goto() {
    await this.page.goto("/dashboard");
  }
  
  async expectWelcomeMessage(name: string) {
    await expect(this.welcomeMessage).toContainText(name);
  }
  
  async logout() {
    await this.logoutButton.click();
  }
}
```

### E2E Test Examples
```typescript
// e2e/auth.spec.ts
import { test, expect } from "@playwright/test";
import { LoginPage } from "./pages/LoginPage";
import { DashboardPage } from "./pages/DashboardPage";

test.describe("Authentication", () => {
  test("user can log in with valid credentials", async ({ page }) => {
    const loginPage = new LoginPage(page);
    const dashboardPage = new DashboardPage(page);
    
    await loginPage.goto();
    await loginPage.login("user@example.com", "password123");
    
    await loginPage.expectLoggedIn();
    await dashboardPage.expectWelcomeMessage("John");
  });
  
  test("shows error for invalid credentials", async ({ page }) => {
    const loginPage = new LoginPage(page);
    
    await loginPage.goto();
    await loginPage.login("user@example.com", "wrongpassword");
    
    await loginPage.expectError("Invalid email or password");
  });
  
  test("user can log out", async ({ page }) => {
    const loginPage = new LoginPage(page);
    const dashboardPage = new DashboardPage(page);
    
    // Login first
    await loginPage.goto();
    await loginPage.login("user@example.com", "password123");
    await loginPage.expectLoggedIn();
    
    // Then logout
    await dashboardPage.logout();
    await expect(page).toHaveURL("/login");
  });
});

// e2e/navigation.spec.ts
test.describe("Navigation", () => {
  test("navigates between pages", async ({ page }) => {
    await page.goto("/");
    
    await page.getByRole("link", { name: "About" }).click();
    await expect(page).toHaveURL("/about");
    
    await page.getByRole("link", { name: "Contact" }).click();
    await expect(page).toHaveURL("/contact");
    
    await page.getByRole("link", { name: "Home" }).click();
    await expect(page).toHaveURL("/");
  });
  
  test("shows 404 for unknown routes", async ({ page }) => {
    await page.goto("/unknown-page");
    
    await expect(page.getByRole("heading", { name: /not found/i })).toBeVisible();
  });
});
```

### Visual Regression Testing
```typescript
// e2e/visual.spec.ts
import { test, expect } from "@playwright/test";

test.describe("Visual Regression", () => {
  test("homepage matches snapshot", async ({ page }) => {
    await page.goto("/");
    
    // Wait for content to load
    await page.waitForLoadState("networkidle");
    
    await expect(page).toHaveScreenshot("homepage.png", {
      fullPage: true,
      maxDiffPixelRatio: 0.02,
    });
  });
  
  test("login form matches snapshot", async ({ page }) => {
    await page.goto("/login");
    
    await expect(page.getByTestId("login-form")).toHaveScreenshot("login-form.png");
  });
  
  test("dark mode matches snapshot", async ({ page }) => {
    await page.goto("/");
    
    // Toggle dark mode
    await page.getByRole("button", { name: "Toggle theme" }).click();
    
    await expect(page).toHaveScreenshot("homepage-dark.png", {
      fullPage: true,
    });
  });
});
```

### Accessibility Testing
```typescript
// e2e/accessibility.spec.ts
import { test, expect } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

test.describe("Accessibility", () => {
  test("homepage has no accessibility violations", async ({ page }) => {
    await page.goto("/");
    
    const results = await new AxeBuilder({ page }).analyze();
    
    expect(results.violations).toEqual([]);
  });
  
  test("login form is accessible", async ({ page }) => {
    await page.goto("/login");
    
    const results = await new AxeBuilder({ page })
      .include(".login-form")
      .analyze();
    
    expect(results.violations).toEqual([]);
  });
  
  test("can navigate with keyboard only", async ({ page }) => {
    await page.goto("/login");
    
    // Tab to email field
    await page.keyboard.press("Tab");
    await expect(page.getByLabel("Email")).toBeFocused();
    
    // Tab to password field
    await page.keyboard.press("Tab");
    await expect(page.getByLabel("Password")).toBeFocused();
    
    // Tab to submit button
    await page.keyboard.press("Tab");
    await expect(page.getByRole("button", { name: "Sign in" })).toBeFocused();
  });
});
```

---

## Mocking Patterns

### API Mocking with MSW
```typescript
// src/test/mocks/handlers.ts
import { http, HttpResponse } from "msw";

export const handlers = [
  http.get("/api/users", () => {
    return HttpResponse.json([
      { id: "1", name: "John", email: "john@example.com" },
      { id: "2", name: "Jane", email: "jane@example.com" },
    ]);
  }),
  
  http.get("/api/users/:id", ({ params }) => {
    return HttpResponse.json({
      id: params.id,
      name: "John",
      email: "john@example.com",
    });
  }),
  
  http.post("/api/users", async ({ request }) => {
    const body = await request.json();
    return HttpResponse.json(
      { id: "3", ...body },
      { status: 201 }
    );
  }),
  
  http.delete("/api/users/:id", () => {
    return new HttpResponse(null, { status: 204 });
  }),
];

// src/test/mocks/server.ts
import { setupServer } from "msw/node";
import { handlers } from "./handlers";

export const server = setupServer(...handlers);

// src/test/setup.ts
import { server } from "./mocks/server";

beforeAll(() => server.listen({ onUnhandledRequest: "error" }));
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

### Timer Mocking
```typescript
// Debounce test
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, it, expect, vi, beforeEach, afterEach } from "vitest";
import { SearchInput } from "./SearchInput";

describe("SearchInput", () => {
  beforeEach(() => {
    vi.useFakeTimers();
  });
  
  afterEach(() => {
    vi.useRealTimers();
  });
  
  it("debounces search input", async () => {
    const onSearch = vi.fn();
    const user = userEvent.setup({ advanceTimers: vi.advanceTimersByTime });
    
    render(<SearchInput onSearch={onSearch} debounceMs={300} />);
    
    await user.type(screen.getByRole("searchbox"), "hello");
    
    // Should not be called immediately
    expect(onSearch).not.toHaveBeenCalled();
    
    // Advance time
    vi.advanceTimersByTime(300);
    
    expect(onSearch).toHaveBeenCalledWith("hello");
    expect(onSearch).toHaveBeenCalledTimes(1);
  });
});
```

---

## Test Utilities

### Custom Render
```typescript
// src/test/utils.tsx
import { render, RenderOptions } from "@testing-library/react";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter } from "react-router-dom";
import { ThemeProvider } from "@/components/ThemeProvider";

const createTestQueryClient = () =>
  new QueryClient({
    defaultOptions: {
      queries: {
        retry: false,
      },
    },
  });

interface CustomRenderOptions extends Omit<RenderOptions, "wrapper"> {
  route?: string;
}

export function renderWithProviders(
  ui: React.ReactElement,
  { route = "/", ...options }: CustomRenderOptions = {}
) {
  window.history.pushState({}, "Test page", route);
  
  const queryClient = createTestQueryClient();
  
  function Wrapper({ children }: { children: React.ReactNode }) {
    return (
      <QueryClientProvider client={queryClient}>
        <BrowserRouter>
          <ThemeProvider defaultTheme="light">
            {children}
          </ThemeProvider>
        </BrowserRouter>
      </QueryClientProvider>
    );
  }
  
  return {
    ...render(ui, { wrapper: Wrapper, ...options }),
    queryClient,
  };
}

// Re-export everything
export * from "@testing-library/react";
export { renderWithProviders as render };
```

### Test Data Factories
```typescript
// src/test/factories.ts
import { faker } from "@faker-js/faker";

export function createUser(overrides = {}) {
  return {
    id: faker.string.uuid(),
    name: faker.person.fullName(),
    email: faker.internet.email(),
    avatar: faker.image.avatar(),
    createdAt: faker.date.past().toISOString(),
    ...overrides,
  };
}

export function createPost(overrides = {}) {
  return {
    id: faker.string.uuid(),
    title: faker.lorem.sentence(),
    content: faker.lorem.paragraphs(3),
    author: createUser(),
    createdAt: faker.date.past().toISOString(),
    ...overrides,
  };
}

export function createUsers(count: number, overrides = {}) {
  return Array.from({ length: count }, () => createUser(overrides));
}
```

---

## Package.json Scripts

```json
{
  "scripts": {
    "test": "vitest",
    "test:ui": "vitest --ui",
    "test:run": "vitest run",
    "test:coverage": "vitest run --coverage",
    "test:watch": "vitest --watch",
    "e2e": "playwright test",
    "e2e:ui": "playwright test --ui",
    "e2e:debug": "playwright test --debug",
    "e2e:codegen": "playwright codegen localhost:3000"
  }
}
```

---

## Best Practices Checklist

### Component Tests
- [ ] Test user behavior, not implementation
- [ ] Use accessible queries (role, label, text)
- [ ] Test loading and error states
- [ ] Test edge cases
- [ ] Avoid snapshot tests for logic

### Hook Tests
- [ ] Test all state transitions
- [ ] Test cleanup/unmount behavior
- [ ] Test with different inputs
- [ ] Wrap in act() for state updates

### E2E Tests
- [ ] Use Page Object Model
- [ ] Test critical user journeys
- [ ] Include accessibility checks
- [ ] Test across browsers
- [ ] Keep tests independent

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | No tests, testing implementation details, flaky tests |
| **High** | 🟠 | Missing error state tests, no accessibility tests |
| **Medium** | 🟡 | Verbose tests, missing edge cases |
| **Low** | 🟢 | Minor naming improvements, documentation |

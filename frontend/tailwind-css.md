# Tailwind CSS — Utility-First Patterns & Optimization

> **Purpose**: Production-ready Tailwind CSS patterns and best practices  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Tailwind v4, custom plugins, optimization, design systems  
> **Last Updated**: 2026-03

---

## Mission

Help write **maintainable, performant Tailwind CSS** using utility-first patterns with proper component abstraction. Focus on design system configuration, custom utilities, and production optimization.

---

## Guard Clauses

**If no Tailwind context provided:**
```
NO_TAILWIND_CONTEXT

Please provide context:
- Tailwind version (v3 or v4)
- Framework (React, Vue, vanilla, etc.)
- Design system/brand requirements
- Component or layout to implement
- Or describe your Tailwind challenge
```

**If Tailwind is well-structured:**
```
TAILWIND_APPROVED

✅ Tailwind review complete — production ready.

Checks performed:
- Utilities: ✓ (consistent, not overused)
- Components: ✓ (extracted appropriately)
- Configuration: ✓ (design tokens defined)
- Performance: ✓ (purging, no unused styles)

Tailwind usage follows best practices.
```

---

## Quick Context Checklist

```
☐ Tailwind version (v3.4+ or v4)
☐ Build tooling (Vite, Next.js, etc.)
☐ Framework integration
☐ Design system requirements
☐ Dark mode approach
☐ Responsive breakpoints
☐ Custom fonts/colors needed
☐ Plugin requirements
```

---

## Copy-Paste Prompts

### Prompt: Review Tailwind Usage
```text
Review this Tailwind CSS usage:

{{CODE}}

Tailwind version: {{VERSION}}
Framework: {{FRAMEWORK}}

Check for:
1. **Utility Organization**
   - Logical ordering
   - Responsive variants
   - State variants (hover, focus, etc.)

2. **Component Extraction**
   - When to use @apply
   - Component vs utility balance
   - Reusability patterns

3. **Configuration**
   - Theme customization
   - Design token usage
   - Plugin utilization

4. **Performance**
   - Class count per element
   - Unused utilities
   - Bundle size concerns
```

### Prompt: Create Tailwind Component
```text
Create a Tailwind component for:

{{COMPONENT_DESCRIPTION}}

Requirements:
- Design: {{DESIGN_REQUIREMENTS}}
- Variants: {{VARIANTS_NEEDED}}
- States: {{STATES}}
- Responsive: {{BREAKPOINTS}}

Framework: {{FRAMEWORK}}
Dark mode: {{YES_NO}}

Provide both utility classes and extracted component CSS if needed.
```

### Prompt: Configure Tailwind Design System
```text
Set up Tailwind configuration for:

Brand colors:
{{COLORS}}

Typography:
{{FONTS_AND_SIZES}}

Spacing scale: {{SPACING}}
Breakpoints: {{BREAKPOINTS}}

Create:
1. tailwind.config.ts configuration
2. CSS custom properties integration
3. Example component using the system
```

### Prompt: Create Tailwind Plugin
```text
Create a Tailwind plugin for:

{{PLUGIN_DESCRIPTION}}

Features:
- Utilities: {{UTILITIES}}
- Components: {{COMPONENTS}}
- Variants: {{VARIANTS}}

Include:
- Plugin code
- Usage examples
- TypeScript types if applicable
```

### Prompt: Optimize Tailwind Build
```text
Optimize this Tailwind setup:

Config: {{TAILWIND_CONFIG}}
Build tool: {{BUILD_TOOL}}
Current bundle size: {{SIZE}}

Analyze and recommend:
1. Content path optimization
2. Unused utility removal
3. Custom CSS reduction
4. Production optimizations
```

---

## Tailwind v4 Configuration

### CSS-Based Configuration

```css
/* tailwind.css - v4 uses CSS for config */
@import "tailwindcss";

/* Theme customization via CSS */
@theme {
  /* Colors */
  --color-brand-50: oklch(97% 0.01 250);
  --color-brand-100: oklch(94% 0.02 250);
  --color-brand-500: oklch(55% 0.19 250);
  --color-brand-600: oklch(48% 0.19 250);
  --color-brand-900: oklch(25% 0.12 250);
  
  /* Semantic colors */
  --color-primary: var(--color-brand-500);
  --color-primary-hover: var(--color-brand-600);
  
  /* Typography */
  --font-display: "Cal Sans", system-ui, sans-serif;
  --font-body: "Inter", system-ui, sans-serif;
  --font-mono: "JetBrains Mono", monospace;
  
  /* Font sizes with line-height */
  --text-xs: 0.75rem;
  --text-xs--line-height: 1rem;
  --text-sm: 0.875rem;
  --text-sm--line-height: 1.25rem;
  --text-base: 1rem;
  --text-base--line-height: 1.5rem;
  
  /* Spacing scale */
  --spacing-px: 1px;
  --spacing-0: 0;
  --spacing-1: 0.25rem;
  --spacing-2: 0.5rem;
  --spacing-3: 0.75rem;
  --spacing-4: 1rem;
  --spacing-6: 1.5rem;
  --spacing-8: 2rem;
  
  /* Shadows */
  --shadow-sm: 0 1px 2px rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px rgb(0 0 0 / 0.1);
  
  /* Radii */
  --radius-sm: 0.25rem;
  --radius-md: 0.375rem;
  --radius-lg: 0.5rem;
  --radius-full: 9999px;
  
  /* Breakpoints */
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;
}
```

### Dark Mode in v4

```css
@theme {
  /* Light mode (default) */
  --color-bg: white;
  --color-text: var(--color-gray-900);
  --color-border: var(--color-gray-200);
}

/* Dark mode overrides */
@media (prefers-color-scheme: dark) {
  @theme {
    --color-bg: var(--color-gray-950);
    --color-text: var(--color-gray-100);
    --color-border: var(--color-gray-800);
  }
}

/* Or with class-based dark mode */
.dark {
  --color-bg: var(--color-gray-950);
  --color-text: var(--color-gray-100);
  --color-border: var(--color-gray-800);
}
```

---

## Tailwind v3 Configuration

### TypeScript Config (v3.4+)

```typescript
// tailwind.config.ts
import type { Config } from 'tailwindcss'
import defaultTheme from 'tailwindcss/defaultTheme'

export default {
  content: [
    './src/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx}',
  ],
  darkMode: 'class', // or 'media'
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#f0f9ff',
          100: '#e0f2fe',
          500: '#0ea5e9',
          600: '#0284c7',
          900: '#0c4a6e',
        },
        // Semantic colors
        primary: 'var(--color-primary)',
        background: 'var(--color-background)',
      },
      fontFamily: {
        display: ['Cal Sans', ...defaultTheme.fontFamily.sans],
        body: ['Inter', ...defaultTheme.fontFamily.sans],
      },
      fontSize: {
        '2xs': ['0.625rem', { lineHeight: '0.875rem' }],
      },
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
      },
      borderRadius: {
        '4xl': '2rem',
      },
      animation: {
        'fade-in': 'fadeIn 0.3s ease-out',
        'slide-up': 'slideUp 0.3s ease-out',
      },
      keyframes: {
        fadeIn: {
          from: { opacity: '0' },
          to: { opacity: '1' },
        },
        slideUp: {
          from: { transform: 'translateY(10px)', opacity: '0' },
          to: { transform: 'translateY(0)', opacity: '1' },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/container-queries'),
  ],
} satisfies Config
```

---

## Component Patterns

### Button Component (React + Tailwind)

```tsx
import { cva, type VariantProps } from 'class-variance-authority'
import { cn } from '@/lib/utils'

const buttonVariants = cva(
  // Base styles
  'inline-flex items-center justify-center rounded-md font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50',
  {
    variants: {
      variant: {
        default: 'bg-primary text-white hover:bg-primary-hover',
        secondary: 'bg-gray-100 text-gray-900 hover:bg-gray-200',
        outline: 'border border-gray-300 bg-transparent hover:bg-gray-50',
        ghost: 'hover:bg-gray-100',
        destructive: 'bg-red-500 text-white hover:bg-red-600',
      },
      size: {
        sm: 'h-8 px-3 text-sm',
        md: 'h-10 px-4 text-sm',
        lg: 'h-12 px-6 text-base',
        icon: 'h-10 w-10',
      },
    },
    defaultVariants: {
      variant: 'default',
      size: 'md',
    },
  }
)

interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  isLoading?: boolean
}

export function Button({
  className,
  variant,
  size,
  isLoading,
  children,
  ...props
}: ButtonProps) {
  return (
    <button
      className={cn(buttonVariants({ variant, size }), className)}
      disabled={isLoading}
      {...props}
    >
      {isLoading && (
        <svg className="mr-2 h-4 w-4 animate-spin" viewBox="0 0 24 24">
          {/* spinner SVG */}
        </svg>
      )}
      {children}
    </button>
  )
}
```

### Card Component

```tsx
import { cn } from '@/lib/utils'

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  variant?: 'default' | 'bordered' | 'elevated'
}

export function Card({ 
  className, 
  variant = 'default',
  children,
  ...props 
}: CardProps) {
  return (
    <div
      className={cn(
        'rounded-lg bg-white',
        {
          'border border-gray-200': variant === 'default' || variant === 'bordered',
          'shadow-lg': variant === 'elevated',
        },
        className
      )}
      {...props}
    >
      {children}
    </div>
  )
}

export function CardHeader({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) {
  return <div className={cn('px-6 py-4 border-b border-gray-100', className)} {...props} />
}

export function CardContent({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) {
  return <div className={cn('px-6 py-4', className)} {...props} />
}

export function CardFooter({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) {
  return <div className={cn('px-6 py-4 border-t border-gray-100', className)} {...props} />
}
```

### Input Component

```tsx
import { forwardRef } from 'react'
import { cn } from '@/lib/utils'

export interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  error?: string
}

export const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ className, type, error, ...props }, ref) => {
    return (
      <div className="w-full">
        <input
          type={type}
          className={cn(
            'flex h-10 w-full rounded-md border bg-white px-3 py-2 text-sm',
            'placeholder:text-gray-400',
            'focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-2',
            'disabled:cursor-not-allowed disabled:opacity-50',
            error
              ? 'border-red-500 focus:ring-red-500'
              : 'border-gray-300',
            className
          )}
          ref={ref}
          {...props}
        />
        {error && (
          <p className="mt-1 text-sm text-red-500">{error}</p>
        )}
      </div>
    )
  }
)
Input.displayName = 'Input'
```

---

## Utility Patterns

### cn() Helper Function

```typescript
// lib/utils.ts
import { type ClassValue, clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

// Usage
<div className={cn(
  'base-class',
  isActive && 'active-class',
  variant === 'primary' && 'primary-class',
  className // Allow override from props
)} />
```

### Responsive Patterns

```tsx
{/* Mobile-first responsive */}
<div className="
  grid 
  grid-cols-1 
  gap-4
  sm:grid-cols-2 
  md:grid-cols-3 
  lg:grid-cols-4
  xl:grid-cols-5
">

{/* Hide/show at breakpoints */}
<nav className="hidden md:flex">
  {/* Desktop nav */}
</nav>
<button className="md:hidden">
  {/* Mobile menu button */}
</button>

{/* Container with responsive padding */}
<div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
```

### State Variants

```tsx
{/* Interactive states */}
<button className="
  bg-primary 
  text-white
  hover:bg-primary-hover
  focus:ring-2 
  focus:ring-primary 
  focus:ring-offset-2
  active:scale-95
  disabled:opacity-50 
  disabled:cursor-not-allowed
">

{/* Group hover */}
<div className="group">
  <div className="group-hover:scale-105 transition-transform">
    <span className="group-hover:text-primary">Hover parent</span>
  </div>
</div>

{/* Peer states (sibling) */}
<input className="peer" />
<span className="hidden peer-invalid:block text-red-500">
  Invalid input
</span>
```

### Container Queries (v3.4+)

```tsx
{/* Container query component */}
<div className="@container">
  <div className="
    flex flex-col
    @sm:flex-row
    @md:items-center
    @lg:justify-between
  ">
    <h2 className="text-lg @md:text-xl @lg:text-2xl">
      Responsive to container
    </h2>
  </div>
</div>
```

---

## Custom Plugin Development

### Basic Plugin Structure

```typescript
// plugins/custom-utilities.ts
import plugin from 'tailwindcss/plugin'

export const customUtilities = plugin(
  // Add utilities
  function ({ addUtilities, addComponents, theme, matchUtilities }) {
    // Static utilities
    addUtilities({
      '.text-balance': {
        'text-wrap': 'balance',
      },
      '.text-pretty': {
        'text-wrap': 'pretty',
      },
      '.scrollbar-hide': {
        '-ms-overflow-style': 'none',
        'scrollbar-width': 'none',
        '&::-webkit-scrollbar': {
          display: 'none',
        },
      },
    })
    
    // Dynamic utilities with values
    matchUtilities(
      {
        'animate-delay': (value) => ({
          'animation-delay': value,
        }),
      },
      { values: theme('transitionDelay') }
    )
    
    // Components
    addComponents({
      '.btn': {
        padding: theme('spacing.2') + ' ' + theme('spacing.4'),
        borderRadius: theme('borderRadius.md'),
        fontWeight: theme('fontWeight.medium'),
      },
    })
  },
  // Extend theme
  {
    theme: {
      extend: {
        transitionDelay: {
          '400': '400ms',
          '600': '600ms',
        },
      },
    },
  }
)
```

### Variant Plugin

```typescript
// plugins/custom-variants.ts
import plugin from 'tailwindcss/plugin'

export const customVariants = plugin(function ({ addVariant }) {
  // Hocus (hover + focus)
  addVariant('hocus', ['&:hover', '&:focus'])
  
  // Parent state variants
  addVariant('group-hocus', ':merge(.group):is(:hover, :focus) &')
  
  // Data attribute variants
  addVariant('data-active', '&[data-active="true"]')
  addVariant('data-state-open', '&[data-state="open"]')
  
  // Aria variants
  addVariant('aria-selected', '&[aria-selected="true"]')
  addVariant('aria-expanded', '&[aria-expanded="true"]')
  
  // Child selector variants
  addVariant('children', '& > *')
  addVariant('children-hover', '& > *:hover')
  
  // Not variants
  addVariant('not-first', '&:not(:first-child)')
  addVariant('not-last', '&:not(:last-child)')
})
```

### Typography Plugin Customization

```typescript
// tailwind.config.ts
import typography from '@tailwindcss/typography'

export default {
  plugins: [
    typography({
      className: 'prose',
    }),
  ],
  theme: {
    extend: {
      typography: ({ theme }) => ({
        DEFAULT: {
          css: {
            '--tw-prose-body': theme('colors.gray.700'),
            '--tw-prose-headings': theme('colors.gray.900'),
            '--tw-prose-links': theme('colors.primary'),
            maxWidth: '75ch',
            a: {
              textDecoration: 'none',
              '&:hover': {
                textDecoration: 'underline',
              },
            },
            'code::before': {
              content: '""',
            },
            'code::after': {
              content: '""',
            },
          },
        },
        invert: {
          css: {
            '--tw-prose-body': theme('colors.gray.300'),
            '--tw-prose-headings': theme('colors.gray.100'),
          },
        },
      }),
    },
  },
}
```

---

## Animation Patterns

### Custom Animations

```css
/* In your CSS file */
@keyframes fade-in-up {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes shimmer {
  0% {
    background-position: -200% 0;
  }
  100% {
    background-position: 200% 0;
  }
}
```

```typescript
// tailwind.config.ts
{
  theme: {
    extend: {
      animation: {
        'fade-in-up': 'fade-in-up 0.5s ease-out',
        'shimmer': 'shimmer 2s linear infinite',
        'spin-slow': 'spin 3s linear infinite',
        'bounce-gentle': 'bounce 2s ease-in-out infinite',
      },
    },
  },
}
```

```tsx
{/* Skeleton loading */}
<div className="animate-shimmer bg-gradient-to-r from-gray-200 via-gray-100 to-gray-200 bg-[length:200%_100%]" />

{/* Staggered animation with delay utilities */}
{items.map((item, i) => (
  <div
    key={item.id}
    className="animate-fade-in-up"
    style={{ animationDelay: `${i * 100}ms` }}
  >
    {item.content}
  </div>
))}
```

---

## Optimization

### Content Configuration

```typescript
// tailwind.config.ts
export default {
  content: [
    // Include all component files
    './src/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
    
    // Include content files
    './content/**/*.{md,mdx}',
    
    // Include specific packages
    './node_modules/@acme/ui/**/*.js',
    
    // Safelist specific patterns
  ],
  safelist: [
    // Safelist dynamic classes
    { pattern: /^bg-(red|green|blue)-(100|500|900)$/ },
    { pattern: /^text-(red|green|blue)-(500|700)$/ },
    // Safelist with variants
    { pattern: /^grid-cols-(1|2|3|4|6|12)$/, variants: ['sm', 'md', 'lg'] },
  ],
}
```

### Production Optimizations

```typescript
// postcss.config.js
module.exports = {
  plugins: {
    'tailwindcss/nesting': {},
    tailwindcss: {},
    autoprefixer: {},
    ...(process.env.NODE_ENV === 'production' ? {
      cssnano: {
        preset: ['default', { discardComments: { removeAll: true } }],
      },
    } : {}),
  },
}
```

### Just-in-Time Optimizations

```tsx
// ❌ Avoid: Dynamic class construction
<div className={`bg-${color}-500`} />  // Won't work!

// ✅ Good: Use complete class names
const colorClasses = {
  red: 'bg-red-500',
  blue: 'bg-blue-500',
  green: 'bg-green-500',
}
<div className={colorClasses[color]} />

// ✅ Good: Use cn() for conditional classes
<div className={cn(
  'base-class',
  color === 'red' && 'bg-red-500',
  color === 'blue' && 'bg-blue-500',
)} />
```

---

## Common Layouts

### Centered Container

```tsx
<div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
  {/* Content */}
</div>
```

### Sticky Header Layout

```tsx
<div className="min-h-screen flex flex-col">
  <header className="sticky top-0 z-50 bg-white border-b">
    {/* Header */}
  </header>
  <main className="flex-1">
    {/* Content */}
  </main>
  <footer className="bg-gray-50">
    {/* Footer */}
  </footer>
</div>
```

### Sidebar Layout

```tsx
<div className="flex min-h-screen">
  <aside className="w-64 shrink-0 border-r bg-gray-50">
    {/* Sidebar */}
  </aside>
  <main className="flex-1 overflow-auto">
    {/* Content */}
  </main>
</div>
```

### Card Grid

```tsx
<div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
  {items.map(item => (
    <div key={item.id} className="rounded-lg border p-6 hover:shadow-lg transition-shadow">
      {/* Card content */}
    </div>
  ))}
</div>
```

---

## Severity Guide

| Severity | Issue | Impact |
|----------|-------|--------|
| 🔴 Critical | Dynamic class names not in safelist | Missing styles in production |
| 🔴 Critical | Wrong content paths | Purged necessary classes |
| 🟠 High | Overuse of @apply | Bloated CSS, defeats purpose |
| 🟠 High | No design tokens | Inconsistent UI |
| 🟡 Medium | Repeated utility groups | Maintenance burden |
| 🟡 Medium | Missing responsive variants | Poor mobile experience |
| 🟢 Low | Suboptimal class ordering | Readability only |

---

## Report Template

```markdown
## Tailwind CSS Review

### Configuration
- Version: [v3.x / v4]
- Framework: [React/Vue/etc.]
- Plugins: [list]

### Design System
| Token | Configured | Consistent |
|-------|------------|------------|
| Colors | | |
| Typography | | |
| Spacing | | |
| Shadows | | |

### Issues Found
1. [Severity] Issue description
   - Impact: 
   - Recommendation:

### Optimization Opportunities
1. [Area] Current → Recommended
```

---

## Related Prompts

- [modern-css.md](modern-css.md) — Native CSS features
- [typescript-patterns.md](typescript-patterns.md) — TypeScript for className utils
- [react-components.md](react-components.md) — React component patterns
- [frontend-testing.md](frontend-testing.md) — Visual regression testing

---

*Last updated: 2026-01*

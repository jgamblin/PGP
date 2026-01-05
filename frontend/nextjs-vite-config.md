# Next.js & Vite Configuration — Modern Build Tools

> **Purpose**: Production configuration for Next.js and Vite projects  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: Configuration, optimization, deployment  
> **Last Updated**: 2026-01

---

## Mission

Help configure **optimized, production-ready** Next.js and Vite projects with proper caching, code splitting, and deployment strategies.

---

## Guard Clauses

**If no framework context provided:**
```
NO_FRAMEWORK_CONTEXT

Please provide context:
- Framework (Next.js or Vite)
- Project type (static, SSR, SPA)
- Deployment target
- Or share existing configuration
```

**If configuration is well-optimized:**
```
CONFIG_APPROVED

✅ Build configuration review complete — production ready.

Checks performed:
- Performance: ✓ (code splitting, caching, compression)
- Security: ✓ (headers, CSP, env handling)
- SEO: ✓ (meta tags, sitemap, robots)
- DX: ✓ (fast HMR, clear errors)

Configuration follows best practices.
```

---

## Quick Context Checklist

```
☐ Framework version
☐ Rendering strategy (SSR/SSG/SPA)
☐ Styling solution
☐ State management
☐ API integration
☐ Deployment target
☐ Performance requirements
☐ SEO requirements
```

---

## Copy-Paste Prompts

### Prompt: Setup Next.js Project
```text
Set up a Next.js project with:

Features:
- {{FEATURES}}
- TypeScript strict mode
- Tailwind CSS
- {{STATE_MANAGEMENT}}

Requirements:
- SEO optimized
- Fast build times
- Proper caching
- Security headers

Generate:
1. next.config.js
2. Package.json scripts
3. Folder structure
4. Key configuration files
5. Deployment config
```

### Prompt: Setup Vite Project
```text
Set up a Vite project with:

Framework: {{FRAMEWORK}} (React/Vue/Svelte)
Features:
- {{FEATURES}}
- TypeScript
- {{STYLING}}

Requirements:
- Fast HMR
- Optimized production build
- Proper code splitting

Generate:
1. vite.config.ts
2. Package.json scripts
3. Folder structure
4. TypeScript config
5. Build optimization
```

### Prompt: Review Configuration
```text
Review this build configuration:

{{CONFIG}}

Check for:
1. **Performance**
   - Code splitting
   - Caching strategy
   - Asset optimization
   - Bundle size

2. **Security**
   - Security headers
   - CSP configuration
   - Env variable handling

3. **SEO**
   - Meta tags setup
   - Sitemap
   - Robots.txt

4. **DX**
   - HMR speed
   - Error handling
   - TypeScript integration

Rate each: 🟢 Good | 🟡 Needs attention | 🔴 Critical issue
```

---

## Next.js Configuration

### next.config.js (Complete)
```javascript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  // Strict mode for better error detection
  reactStrictMode: true,
  
  // Enable experimental features
  experimental: {
    typedRoutes: true,
    serverActions: {
      bodySizeLimit: '2mb',
    },
  },
  
  // Image optimization
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'images.example.com',
      },
      {
        protocol: 'https',
        hostname: '*.githubusercontent.com',
      },
    ],
    formats: ['image/avif', 'image/webp'],
    deviceSizes: [640, 750, 828, 1080, 1200, 1920, 2048, 3840],
    imageSizes: [16, 32, 48, 64, 96, 128, 256, 384],
  },
  
  // Security headers
  async headers() {
    return [
      {
        source: '/(.*)',
        headers: [
          {
            key: 'X-Frame-Options',
            value: 'DENY',
          },
          {
            key: 'X-Content-Type-Options',
            value: 'nosniff',
          },
          {
            key: 'Referrer-Policy',
            value: 'strict-origin-when-cross-origin',
          },
          {
            key: 'Permissions-Policy',
            value: 'camera=(), microphone=(), geolocation=()',
          },
        ],
      },
      {
        source: '/api/(.*)',
        headers: [
          {
            key: 'Cache-Control',
            value: 'no-store, max-age=0',
          },
        ],
      },
    ];
  },
  
  // Redirects
  async redirects() {
    return [
      {
        source: '/old-page',
        destination: '/new-page',
        permanent: true, // 308 redirect
      },
    ];
  },
  
  // Rewrites (proxying)
  async rewrites() {
    return [
      {
        source: '/api/v1/:path*',
        destination: `${process.env.API_URL}/:path*`,
      },
    ];
  },
  
  // Webpack customization
  webpack: (config, { dev, isServer }) => {
    // SVG as components
    config.module.rules.push({
      test: /\.svg$/,
      use: ['@svgr/webpack'],
    });
    
    // Bundle analyzer (dev only)
    if (process.env.ANALYZE === 'true') {
      const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');
      config.plugins.push(
        new BundleAnalyzerPlugin({
          analyzerMode: 'static',
          reportFilename: isServer
            ? '../analyze/server.html'
            : './analyze/client.html',
        })
      );
    }
    
    return config;
  },
  
  // Environment variables (public)
  env: {
    NEXT_PUBLIC_APP_NAME: process.env.NEXT_PUBLIC_APP_NAME,
  },
  
  // Output configuration
  output: 'standalone', // For Docker deployment
  
  // Compiler options
  compiler: {
    removeConsole: process.env.NODE_ENV === 'production',
  },
  
  // Internationalization
  i18n: {
    locales: ['en', 'es', 'fr'],
    defaultLocale: 'en',
  },
};

module.exports = nextConfig;
```

### App Directory Structure
```
app/
├── (auth)/
│   ├── login/
│   │   └── page.tsx
│   ├── register/
│   │   └── page.tsx
│   └── layout.tsx
├── (dashboard)/
│   ├── dashboard/
│   │   └── page.tsx
│   ├── settings/
│   │   └── page.tsx
│   └── layout.tsx
├── api/
│   ├── auth/
│   │   └── [...nextauth]/
│   │       └── route.ts
│   └── users/
│       ├── route.ts
│       └── [id]/
│           └── route.ts
├── globals.css
├── layout.tsx
├── loading.tsx
├── error.tsx
├── not-found.tsx
└── page.tsx

components/
├── ui/
│   ├── Button.tsx
│   ├── Input.tsx
│   └── index.ts
├── features/
│   ├── auth/
│   │   └── LoginForm.tsx
│   └── dashboard/
│       └── StatsCard.tsx
└── layouts/
    ├── Header.tsx
    └── Footer.tsx

lib/
├── utils.ts
├── api.ts
└── hooks/
    └── useAuth.ts
```

### Root Layout
```tsx
// app/layout.tsx
import type { Metadata, Viewport } from "next";
import { Inter } from "next/font/google";
import { Analytics } from "@vercel/analytics/react";
import "./globals.css";

const inter = Inter({
  subsets: ["latin"],
  display: "swap",
  variable: "--font-inter",
});

export const metadata: Metadata = {
  title: {
    default: "My App",
    template: "%s | My App",
  },
  description: "Description of my app",
  keywords: ["keyword1", "keyword2"],
  authors: [{ name: "Author Name" }],
  creator: "Company Name",
  metadataBase: new URL("https://example.com"),
  openGraph: {
    type: "website",
    locale: "en_US",
    siteName: "My App",
  },
  twitter: {
    card: "summary_large_image",
    creator: "@handle",
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
};

export const viewport: Viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#ffffff" },
    { media: "(prefers-color-scheme: dark)", color: "#000000" },
  ],
  width: "device-width",
  initialScale: 1,
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={inter.variable}>
      <body className="min-h-screen bg-background font-sans antialiased">
        {children}
        <Analytics />
      </body>
    </html>
  );
}
```

### API Route Handler
```tsx
// app/api/users/route.ts
import { NextResponse } from "next/server";
import { z } from "zod";

// Validation schema
const createUserSchema = z.object({
  name: z.string().min(1).max(100),
  email: z.string().email(),
});

export async function GET(request: Request) {
  try {
    const { searchParams } = new URL(request.url);
    const page = parseInt(searchParams.get("page") || "1");
    const limit = parseInt(searchParams.get("limit") || "10");
    
    // Fetch users
    const users = await db.user.findMany({
      skip: (page - 1) * limit,
      take: limit,
    });
    
    return NextResponse.json({ users, page, limit });
  } catch (error) {
    console.error("Error fetching users:", error);
    return NextResponse.json(
      { error: "Failed to fetch users" },
      { status: 500 }
    );
  }
}

export async function POST(request: Request) {
  try {
    const body = await request.json();
    
    // Validate input
    const validated = createUserSchema.parse(body);
    
    // Create user
    const user = await db.user.create({
      data: validated,
    });
    
    return NextResponse.json(user, { status: 201 });
  } catch (error) {
    if (error instanceof z.ZodError) {
      return NextResponse.json(
        { error: "Validation failed", details: error.errors },
        { status: 400 }
      );
    }
    
    console.error("Error creating user:", error);
    return NextResponse.json(
      { error: "Failed to create user" },
      { status: 500 }
    );
  }
}
```

### Server Actions
```tsx
// app/actions/user.ts
"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { z } from "zod";

const updateProfileSchema = z.object({
  name: z.string().min(1).max(100),
  bio: z.string().max(500).optional(),
});

export async function updateProfile(formData: FormData) {
  const rawData = {
    name: formData.get("name"),
    bio: formData.get("bio"),
  };
  
  // Validate
  const validated = updateProfileSchema.parse(rawData);
  
  // Update in database
  await db.user.update({
    where: { id: getCurrentUserId() },
    data: validated,
  });
  
  // Revalidate the profile page cache
  revalidatePath("/profile");
}

export async function deleteAccount() {
  const userId = getCurrentUserId();
  
  await db.user.delete({
    where: { id: userId },
  });
  
  redirect("/");
}
```

---

## Vite Configuration

### vite.config.ts (Complete)
```typescript
// vite.config.ts
import { defineConfig, loadEnv } from "vite";
import react from "@vitejs/plugin-react-swc";
import { resolve } from "path";
import { visualizer } from "rollup-plugin-visualizer";

export default defineConfig(({ command, mode }) => {
  // Load env variables
  const env = loadEnv(mode, process.cwd(), "");
  
  return {
    plugins: [
      react(),
      // Bundle analyzer
      mode === "analyze" &&
        visualizer({
          open: true,
          filename: "dist/stats.html",
          gzipSize: true,
          brotliSize: true,
        }),
    ].filter(Boolean),
    
    // Path aliases
    resolve: {
      alias: {
        "@": resolve(__dirname, "./src"),
        "@components": resolve(__dirname, "./src/components"),
        "@lib": resolve(__dirname, "./src/lib"),
        "@hooks": resolve(__dirname, "./src/hooks"),
      },
    },
    
    // Dev server
    server: {
      port: 3000,
      strictPort: true,
      host: true,
      proxy: {
        "/api": {
          target: env.API_URL || "http://localhost:8080",
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\/api/, ""),
        },
      },
    },
    
    // Preview server
    preview: {
      port: 4173,
      strictPort: true,
    },
    
    // Build options
    build: {
      target: "esnext",
      outDir: "dist",
      sourcemap: mode === "development",
      minify: "esbuild",
      
      // Chunk splitting
      rollupOptions: {
        output: {
          manualChunks: {
            vendor: ["react", "react-dom"],
            router: ["react-router-dom"],
            ui: ["@radix-ui/react-dialog", "@radix-ui/react-dropdown-menu"],
          },
          // Asset naming
          assetFileNames: (assetInfo) => {
            const info = assetInfo.name?.split(".") || [];
            const ext = info[info.length - 1];
            if (/png|jpe?g|svg|gif|tiff|bmp|ico/i.test(ext)) {
              return `assets/images/[name]-[hash][extname]`;
            }
            if (/woff2?|eot|ttf|otf/i.test(ext)) {
              return `assets/fonts/[name]-[hash][extname]`;
            }
            return `assets/[name]-[hash][extname]`;
          },
          chunkFileNames: "js/[name]-[hash].js",
          entryFileNames: "js/[name]-[hash].js",
        },
      },
      
      // Report compressed sizes
      reportCompressedSize: true,
      
      // Chunk size warning limit
      chunkSizeWarningLimit: 500,
    },
    
    // CSS options
    css: {
      devSourcemap: true,
      modules: {
        localsConvention: "camelCaseOnly",
      },
    },
    
    // Optimization
    optimizeDeps: {
      include: ["react", "react-dom", "react-router-dom"],
      exclude: ["@vite/client", "@vite/env"],
    },
    
    // Environment variables
    define: {
      __APP_VERSION__: JSON.stringify(process.env.npm_package_version),
    },
    
    // Test configuration (vitest)
    test: {
      globals: true,
      environment: "jsdom",
      setupFiles: ["./src/test/setup.ts"],
      include: ["src/**/*.{test,spec}.{js,mjs,cjs,ts,mts,cts,jsx,tsx}"],
      coverage: {
        provider: "v8",
        reporter: ["text", "json", "html"],
        exclude: ["node_modules/", "src/test/"],
      },
    },
  };
});
```

### Vite Project Structure
```
src/
├── components/
│   ├── ui/
│   │   ├── Button.tsx
│   │   ├── Input.tsx
│   │   └── index.ts
│   └── features/
│       └── auth/
│           └── LoginForm.tsx
├── hooks/
│   ├── useAuth.ts
│   └── useLocalStorage.ts
├── lib/
│   ├── api.ts
│   ├── utils.ts
│   └── constants.ts
├── pages/
│   ├── Home.tsx
│   ├── Dashboard.tsx
│   └── NotFound.tsx
├── routes/
│   └── index.tsx
├── stores/
│   └── authStore.ts
├── styles/
│   └── globals.css
├── test/
│   └── setup.ts
├── types/
│   └── index.ts
├── App.tsx
├── main.tsx
└── vite-env.d.ts
```

### Vite + React Router
```tsx
// src/routes/index.tsx
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { lazy, Suspense } from "react";

// Lazy load pages
const Home = lazy(() => import("@/pages/Home"));
const Dashboard = lazy(() => import("@/pages/Dashboard"));
const Settings = lazy(() => import("@/pages/Settings"));
const NotFound = lazy(() => import("@/pages/NotFound"));

// Layout components
import { RootLayout } from "@/components/layouts/RootLayout";
import { DashboardLayout } from "@/components/layouts/DashboardLayout";
import { PageLoader } from "@/components/ui/PageLoader";
import { ErrorBoundary } from "@/components/ErrorBoundary";

const router = createBrowserRouter([
  {
    path: "/",
    element: <RootLayout />,
    errorElement: <ErrorBoundary />,
    children: [
      {
        index: true,
        element: (
          <Suspense fallback={<PageLoader />}>
            <Home />
          </Suspense>
        ),
      },
      {
        path: "dashboard",
        element: <DashboardLayout />,
        children: [
          {
            index: true,
            element: (
              <Suspense fallback={<PageLoader />}>
                <Dashboard />
              </Suspense>
            ),
          },
          {
            path: "settings",
            element: (
              <Suspense fallback={<PageLoader />}>
                <Settings />
              </Suspense>
            ),
          },
        ],
      },
      {
        path: "*",
        element: (
          <Suspense fallback={<PageLoader />}>
            <NotFound />
          </Suspense>
        ),
      },
    ],
  },
]);

export function Routes() {
  return <RouterProvider router={router} />;
}
```

---

## Performance Optimization

### Next.js Image Optimization
```tsx
import Image from "next/image";

// Optimized image with blur placeholder
export function HeroImage() {
  return (
    <Image
      src="/hero.jpg"
      alt="Hero image"
      width={1200}
      height={600}
      priority // Load immediately for LCP
      placeholder="blur"
      blurDataURL="data:image/jpeg;base64,..."
      sizes="(max-width: 768px) 100vw, 1200px"
    />
  );
}

// Dynamic images
export function UserAvatar({ src, name }: { src: string; name: string }) {
  return (
    <Image
      src={src}
      alt={`${name}'s avatar`}
      width={48}
      height={48}
      className="rounded-full"
      loading="lazy"
    />
  );
}
```

### Font Optimization
```tsx
// Next.js - next/font
import { Inter, Roboto_Mono } from "next/font/google";

const inter = Inter({
  subsets: ["latin"],
  display: "swap",
  variable: "--font-inter",
});

const robotoMono = Roboto_Mono({
  subsets: ["latin"],
  display: "swap",
  variable: "--font-roboto-mono",
});

// In layout
<html className={`${inter.variable} ${robotoMono.variable}`}>
```

```css
/* Vite - CSS */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url('/fonts/inter-regular.woff2') format('woff2');
  unicode-range: U+0000-00FF;
}
```

### Bundle Optimization Scripts
```json
{
  "scripts": {
    "build": "next build",
    "build:analyze": "ANALYZE=true next build",
    "build:vite": "vite build",
    "build:vite:analyze": "vite build --mode analyze"
  }
}
```

---

## Environment Configuration

### Next.js Environment
```bash
# .env.local (not committed)
DATABASE_URL="postgresql://..."
API_SECRET="secret"

# .env (committed defaults)
NEXT_PUBLIC_APP_NAME="My App"
NEXT_PUBLIC_API_URL="https://api.example.com"
```

```typescript
// env.ts - Type-safe env access
import { z } from "zod";

const envSchema = z.object({
  DATABASE_URL: z.string().url(),
  API_SECRET: z.string().min(32),
  NEXT_PUBLIC_APP_NAME: z.string(),
  NEXT_PUBLIC_API_URL: z.string().url(),
});

export const env = envSchema.parse({
  DATABASE_URL: process.env.DATABASE_URL,
  API_SECRET: process.env.API_SECRET,
  NEXT_PUBLIC_APP_NAME: process.env.NEXT_PUBLIC_APP_NAME,
  NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL,
});
```

### Vite Environment
```bash
# .env
VITE_APP_NAME="My App"
VITE_API_URL="https://api.example.com"
```

```typescript
// vite-env.d.ts
/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_APP_NAME: string;
  readonly VITE_API_URL: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
```

---

## Deployment Configurations

### Vercel (vercel.json)
```json
{
  "framework": "nextjs",
  "regions": ["iad1"],
  "headers": [
    {
      "source": "/api/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "no-store" }
      ]
    },
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Frame-Options", "value": "DENY" }
      ]
    }
  ],
  "rewrites": [
    {
      "source": "/api/external/:path*",
      "destination": "https://external-api.com/:path*"
    }
  ]
}
```

### Docker (Next.js Standalone)
```dockerfile
# Dockerfile
FROM node:20-alpine AS base

FROM base AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

FROM base AS runner
WORKDIR /app
ENV NODE_ENV production

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs
EXPOSE 3000
ENV PORT 3000

CMD ["node", "server.js"]
```

### Nginx (Static Vite)
```nginx
server {
    listen 80;
    server_name example.com;
    root /var/www/dist;
    index index.html;

    # Gzip
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml;

    # Cache static assets
    location /assets/ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # SPA fallback
    location / {
        try_files $uri $uri/ /index.html;
    }

    # Security headers
    add_header X-Frame-Options "DENY" always;
    add_header X-Content-Type-Options "nosniff" always;
}
```

---

## Best Practices Checklist

### Performance
- [ ] Code splitting configured
- [ ] Images optimized
- [ ] Fonts optimized
- [ ] Caching headers set
- [ ] Bundle analyzed

### Security
- [ ] Security headers configured
- [ ] CSP implemented
- [ ] Environment variables secured
- [ ] CORS configured

### SEO
- [ ] Meta tags configured
- [ ] Sitemap generated
- [ ] robots.txt configured
- [ ] OpenGraph tags set

### DX
- [ ] Fast HMR
- [ ] TypeScript strict
- [ ] Path aliases configured
- [ ] Error boundaries set

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | No security headers, exposed secrets, no error handling |
| **High** | 🟠 | Missing code splitting, no caching, poor SEO |
| **Medium** | 🟡 | Suboptimal bundle size, missing optimizations |
| **Low** | 🟢 | Minor config improvements, documentation |

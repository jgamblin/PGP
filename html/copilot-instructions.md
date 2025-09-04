# 🧭 Frontend (HTML/CSS/JS) Prompt Set – Copilot Usage Guide

Context: Prompt library only. No actual build here. Copy this into a web/UI project to standardize accessibility + performance reviews. Adjust Core Web Vitals notes to reflect real metrics if available.

---
## 🎯 Primary Objectives (Order Matters)
1. Accessibility (WCAG 2.2 AA+ essentials) & keyboard operability
2. Semantic HTML structure & landmark correctness
3. Core Web Vitals performance (LCP, CLS, INP)
4. Component consistency (naming, props/attributes, CSS architecture)
5. Security (XSS surfaces, unsafe inline script usage)
6. Test coverage for interactive + conditional UI paths

---
## 🏗️ Example Frontend Repo Layout (Adjust After Copy)
```
web-app/
  src/
    components/
    pages/
    styles/            # BEM or utility-first mapping
    assets/
    hooks/             # (If using framework)
  tests/
    accessibility/
    components/
  public/
  .github/workflows/ci.yml
  README.md
```

---
## 🧪 Base Analysis Prompt (Accessibility-First)
```
You are an accessibility-first frontend reviewer.
Scope: <files/components>.
Tasks: Accessibility + semantic audit → performance hotspots → refactor suggestions.
Output format:
# Frontend Review
## Summary
## Critical Accessibility Violations (WCAG ref)
## Semantic / Landmark Issues
## Performance (Core Web Vitals focus)
## Security / XSS Surfaces
## CSS Architecture Observations (BEM or alt)
## Suggested Minimal Patches (top 2)
End with: Which area next?
```

Follow-ups:
- "Provide ARIA adjustments diff only."
- "List missing alt/aria-label with file:line."
- "Show layout shift (CLS) risk elements."

---
## ♿ Accessibility Checks (Ask Copilot)
- Missing/incorrect landmarks (`header`, `main`, `nav`, `footer`)
- Improper heading hierarchy (h1 → h2 ordering)
- Interactive elements not focusable (div/button misuse)
- Insufficient color contrast
- Missing form label associations
- Non-descriptive link/button text
- Focus trap or loss on modals
- Dynamic content without live region announcements

Prompt: "Accessibility-only scan; classify violations Critical/High/Medium with WCAG refs." 

---
## 💨 Performance Review Prompt
```
Identify potential Core Web Vitals issues:
- Large blocking scripts
- Non-deferred third-party scripts
- Unoptimized images (missing width/height, no lazy loading)
- Layout shift triggers (images without dimensions, late CSS)
- Render blocking CSS
Return each with file:line and fix suggestion.
```

---
## 🛡️ Security Surface Checklist
- Inline event handlers (`onclick=`, etc.)
- Unsanitized HTML insertion (`innerHTML`, `dangerouslySetInnerHTML`)
- Unescaped user data in templates
- External script injection patterns
Prompt: "List all potential XSS vectors with file:line; suggest safer alternative." 

---
## 🎨 CSS Architecture Guidance
Pick one baseline (declare early): BEM / utility-first / layered tokens.
Ask:
```
Audit class naming consistency. List violations & propose corrected names.
Highlight specificity wars (>3 selectors deep) and unused declarations if detectable.
```

---
## 🧩 Component Refactor Loop
1. Run audit
2. Approve 1–2 refactors (e.g. semantic wrapper + aria roles)
3. Request minimal diff
4. Ask for before/after accessibility justification
5. Generate tests (keyboard navigation & aria state)

---
## 🧪 Testing Patterns Prompt
```
Generate tests for component <Name>:
- Keyboard navigation sequence
- ARIA state toggling
- Conditional rendering branches
- Focus management on open/close events
Return only test code (e.g. Playwright / Testing Library) + short notes.
```

---
## 🗜️ Diff-Only Refactors
Ask:
```
Return unified diff.
Do not rewrap or reformat unrelated HTML.
Preserve existing spacing.
Add TODO comments instead of speculative rewrites.
```

---
## 🧠 When Output is Too Generic
Reply:
```
Regenerate with:
- Specific WCAG references
- Concrete before/after HTML snippets
- Explicit risk ranking
- Remove non-actionable wording
```

---
## 🔄 Example Session Flow
```
1. Initial accessibility + semantic audit
2. Apply minimal structural patch
3. Generate alt text + aria improvements
4. Performance (LCP + CLS risk) scan
5. Security (XSS) pass
6. Test generation (keyboard + dynamic state)
7. Final verification checklist
```

---
## ✅ Final Verification Checklist
Have Copilot produce PASS/FAIL:
- All interactive elements reachable via keyboard
- Headings hierarchical & singular h1 per page
- Images: alt text + explicit dimensions
- No unexpected layout shifts on load
- No inline script or event handler XSS risk
- Tests cover new conditional branches

Prompt: "Generate final verification checklist with PASS/FAIL + 1-line justification." 

---
## ♻️ Using Inside the Prompt Library
Inside this repo you only copy sections. After transplant, enrich with actual tooling (build commands, test runner, lighthouse thresholds). Keep diffs small. Accessibility first, then performance, then refinement.

# HTML-to-Frontend Compatibility Map

The `html/` directory remains available for backward compatibility. For modern stack-first guidance, use the `frontend/` directory as the primary source.

## Mapping

| Legacy Path (`html/`) | Preferred Modern Path (`frontend/`) | Notes |
|---|---|---|
| `agents.md` | `agents.md` | Frontend index and routing |
| `copilot-instructions.md` | `copilot-instructions.md` | Assistant configuration |
| `code-refactoring.md` | `typescript-patterns.md` | Refactoring patterns for typed frontend stacks |
| `documentation-generation.md` | `frontend-testing.md` | Pair with testing/docs workflows |
| `project-repo.md` | `nextjs-vite-config.md` | Project setup and build configuration |
| `pr-review-feedback.md` | `frontend-testing.md` | Review + validation workflow |
| `performance-core-web-vitals-audit.md` | `modern-css.md` | Performance-sensitive frontend patterns |
| `accessibility-check.md` | `react-components.md` | Accessibility patterns in component-driven apps |
| `component-design-system-review.md` | `react-components.md` | Design-system and component architecture |
| `semantic-markup-refinement.md` | `modern-css.md` | Semantic structure with modern frontend guidance |
| `navigation-consistency.md` | `state-management.md` | Navigation-state and interaction consistency |
| `bem-naming-convention.md` | `tailwind-css.md` | CSS architecture migration path |

## Compatibility Policy

- Existing `html/` files stay available in this release cycle.
- New frontend guidance should be authored in `frontend/`.
- `html/` updates should include links to modern `frontend/` counterparts.

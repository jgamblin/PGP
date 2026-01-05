# Deep Code Cleaning — Repository Hygiene & Cleanup

> **Purpose**: Identify and remove unused files, outdated scripts, and legacy artifacts  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Languages**: Any  
> **Last Updated**: 2025-12

---

## Mission

Help identify and safely remove **dead code, unused files, outdated documentation, and legacy artifacts** that accumulate over multiple iterations. Focus on making repositories cleaner, more navigable, and easier to maintain while preserving everything needed to run the current system.

---

## Guard Clauses

**If no repository context provided:**
```
NO_REPOSITORY_CONTEXT

Please provide repository context to analyze:
- Repository root path or structure
- Main entry points (package.json, setup.py, Makefile, etc.)
- Build/deployment configuration
- Or describe what the system currently does
```

**If repository is clean:**
```
REPOSITORY_CLEAN

✅ Deep cleaning analysis complete — no major cleanup needed.

Checks performed:
- Unused source files: ✓
- Orphaned scripts: ✓
- Outdated documentation: ✓
- Legacy configuration: ✓
- Dead dependencies: ✓
- Abandoned migrations: ✓

Repository is well-maintained. Consider documenting your cleanup process.
```

---

## Quick Context Checklist

```
☐ Repository structure
☐ Main entry points and build files
☐ Active branches (which is production?)
☐ Known deprecated features
☐ Files that MUST be preserved
☐ Last major refactoring date
```

---

## Copy-Paste Cleaning Prompts

### Prompt: Full Repository Audit
```text
Analyze this repository for cleanup opportunities:

Repository structure:
{{STRUCTURE}}

Main entry points: {{ENTRY_POINTS}}
Build command: {{BUILD_COMMAND}}
Active features: {{FEATURES}}

Identify:
1. Unused source files (not imported/required anywhere)
2. Orphaned scripts (one-off migrations, old utilities)
3. Dead code paths (unreachable functions, commented blocks)
4. Outdated documentation (references removed features)
5. Legacy configuration files (old build tools, deprecated configs)
6. Abandoned test files (tests for removed features)
7. Unused dependencies in manifest files
8. Old backup files (.bak, .old, .orig, ~files)

For each finding, provide:
- File path
- Why it appears unused
- Confidence level (🟢 Safe | 🟡 Verify | 🔴 Caution)
- Recommended action

Output as `REPOSITORY_CLEAN` if nothing found.
```

### Prompt: Dead Code Detection
```text
Find dead code in this codebase:

{{CODE_OR_STRUCTURE}}

Language: {{LANGUAGE}}

Check for:
1. Functions/methods never called
2. Classes never instantiated
3. Variables assigned but never used
4. Imports/requires that aren't used
5. Commented-out code blocks (>10 lines)
6. Feature flags for removed features
7. Conditional branches that never execute
8. Exported items never imported elsewhere

For each finding:
- Location (file:line)
- Type of dead code
- Why it's dead (no callers, impossible condition, etc.)
- Safe to remove? (🟢 Yes | 🟡 Verify | 🔴 Test first)
```

### Prompt: Orphaned File Detection
```text
Find orphaned files in this repository:

{{STRUCTURE}}

Entry points: {{ENTRY_POINTS}}
Build config: {{BUILD_CONFIG}}

Identify files that are:
1. Not imported by any other file
2. Not referenced in build configuration
3. Not included in package manifest
4. Not used by tests (that test active code)
5. Not required for deployment
6. Not documentation for active features

Exclude from removal:
- Configuration files (even if not explicitly imported)
- CI/CD files
- License and legal files
- Active README and docs
- Git-related files

Categorize as:
- 🗑️ Safe to delete
- 📦 Move to archive
- 🔍 Needs investigation
- ⚠️ Possibly needed (verify before removing)
```

### Prompt: Documentation Cleanup
```text
Audit documentation for outdated content:

{{DOCS_STRUCTURE}}

Current features: {{ACTIVE_FEATURES}}
Recent removals: {{REMOVED_FEATURES}}

Find:
1. READMEs referencing removed features
2. API docs for deprecated endpoints
3. Setup guides with outdated steps
4. Screenshots of old UI
5. Architecture diagrams that don't match code
6. Comments referencing old behavior
7. TODO/FIXME for completed or abandoned items
8. Changelog entries without corresponding code

Provide:
- File and section
- What's outdated
- Suggested update or removal
```

### Prompt: Dependency Cleanup
```text
Find unused dependencies:

{{DEPENDENCY_FILE}}

Codebase: {{CODE_STRUCTURE}}

Identify:
1. Packages listed but never imported
2. Dev dependencies used only by removed tests
3. Peer dependencies for removed features
4. Duplicate packages (same purpose, different names)
5. Vendored code that duplicates dependencies
6. Build tools for unused build targets

Also check for:
- Outdated lockfiles
- Conflicting version requirements
- Dependencies of dependencies no longer needed

Output:
| Package | Type | Status | Action |
| --- | --- | --- | --- |
| example | prod | unused | remove |
```

### Prompt: Script & Migration Cleanup
```text
Audit scripts and migrations:

Scripts directory: {{SCRIPTS}}
Migrations: {{MIGRATIONS}}
Current schema: {{SCHEMA}}

Find:
1. One-time migration scripts (already applied)
2. Data fix scripts (issue resolved)
3. Old deployment scripts (superseded)
4. Utility scripts referencing removed code
5. Seed data for old schema versions
6. Rollback scripts for ancient migrations
7. Test data generators for removed features

For migrations specifically:
- Can old migrations be squashed?
- Are there migrations that were never applied?
- Are rollback scripts still valid?

Categorize:
- 🗑️ Delete (safely archived in git history)
- 📁 Archive (move to /archive or similar)
- 🔄 Squash (combine with others)
- ✅ Keep (still needed)
```

### Prompt: Safe Cleanup Plan
```text
Create a safe cleanup plan for this repository:

Findings:
{{CLEANUP_FINDINGS}}

Branch strategy: {{BRANCH_STRATEGY}}
Deployment process: {{DEPLOYMENT}}

Generate:
1. **Pre-cleanup checklist**
   - Backup recommendations
   - Tests to run before
   - Stakeholders to notify

2. **Phased cleanup plan**
   - Phase 1: Obviously safe deletions
   - Phase 2: Verify-then-delete items
   - Phase 3: Consolidation and reorganization

3. **For each phase:**
   - Specific files to remove
   - Git commands (with --dry-run first)
   - Validation steps after removal
   - Rollback procedure if issues found

4. **Post-cleanup validation**
   - Build verification
   - Test suite execution
   - Deployment to staging
   - Documentation updates needed

Emphasize: Always keep git history intact for recovery.
```

---

## Analysis Approach

### Step 1: Map Active Code
```text
Starting from entry points, trace all:
- Imports and requires
- Dynamic imports/loads
- Configuration references
- Build tool inputs
- Test subjects

Everything reachable = active
Everything else = candidate for review
```

### Step 2: Categorize Findings
```text
🟢 Safe to Remove:
- Files not in import tree
- No references in configs
- Not in git blame for recent commits
- Clear legacy naming (.old, .bak, .deprecated)

🟡 Verify Before Removing:
- Referenced in comments only
- In import tree but functions unused
- Test files with unclear scope
- Config files for optional features

🔴 Investigate Carefully:
- Recently modified
- Unclear purpose
- Possible runtime dynamic loading
- Environment-specific files
```

### Step 3: Document Decisions
```text
For each removal decision, record:
- What: File or code path
- Why: Reason it's unused
- When: Git history reference
- Risk: What could break
- Recovery: How to restore if needed
```

---

## Common Cleanup Patterns

### Legacy Code Indicators
```text
Look for:
- "old_", "deprecated_", "legacy_" prefixes
- "_backup", "_old", "_v1" suffixes
- Dates in filenames (2019, 2020, etc.)
- "TODO: remove", "DEPRECATED" comments
- Version numbers in directory names
- "temp", "tmp", "test_delete" names
```

### Typically Safe to Remove
```text
- .bak, .orig, .old files
- Compiled artifacts (.pyc, .class, node_modules)
- IDE-specific files not in .gitignore
- Empty __init__.py with no side effects
- Test files for deleted source files
- Commented-out code blocks
- Console.log / print debugging statements
- Unused import statements
```

### Requires Verification
```text
- Configuration files (may be environment-specific)
- Database migrations (needed for schema history)
- API endpoints (may have external consumers)
- Utility functions (may be used dynamically)
- Shared libraries (may have external dependents)
```

---

## Cleanup Validation Commands

### General
```bash
# Check if build still works
make build  # or npm run build, cargo build, etc.

# Run full test suite
make test   # or npm test, pytest, etc.

# Verify no broken imports
# (language-specific static analysis)
```

### Git Commands for Safe Cleanup
```bash
# Preview what would be deleted (dry run)
git clean -n -d

# Find files not tracked by git
git ls-files --others --exclude-standard

# Find large files that might be artifacts
git rev-list --objects --all | git cat-file --batch-check

# Create safety branch before cleanup
git checkout -b cleanup/YYYY-MM-DD

# After cleanup, squash into single commit
git rebase -i main
```

### Finding Dead Code
```bash
# JavaScript/TypeScript - find unused exports
npx ts-prune

# Python - find unused code
vulture . --min-confidence 80

# General - find files not imported
madge --orphans --extensions js,ts src/

# Find TODO/FIXME comments
grep -r "TODO\|FIXME\|HACK\|XXX" --include="*.py" .
```

---

## Report Template

After analysis, generate:

```markdown
# Repository Cleanup Report — {{REPO_NAME}}

**Date**: {{DATE}}
**Analyzed by**: {{ANALYST}}
**Repository size before**: {{SIZE}}

## Executive Summary
- Total files analyzed: {{COUNT}}
- Files flagged for removal: {{REMOVAL_COUNT}}
- Estimated size reduction: {{SIZE_REDUCTION}}
- Risk level: 🟢 Low / 🟡 Medium / 🔴 High

## Findings by Category

### 🗑️ Safe to Delete ({{COUNT}})
| File | Reason | Last Modified | Size |
| --- | --- | --- | --- |

### 🔍 Needs Verification ({{COUNT}})
| File | Concern | Recommended Check |
| --- | --- | --- |

### 📦 Recommend Archive ({{COUNT}})
| File | Reason | Archive Location |
| --- | --- | --- |

## Cleanup Commands
```bash
# Phase 1: Safe deletions
git rm {{FILES}}

# Phase 2: After verification
git rm {{VERIFIED_FILES}}
```

## Validation Checklist
- [ ] Build passes
- [ ] Tests pass
- [ ] Application starts
- [ ] Key features verified
- [ ] No console errors

## Notes & Warnings
{{SPECIAL_CONSIDERATIONS}}
```

---

## Best Practices

### Before Cleanup
- Create a dedicated branch
- Document current test coverage
- Note current build time and artifact size
- Communicate with team about planned changes

### During Cleanup
- Remove in small, atomic commits
- Run tests after each batch removal
- Keep detailed commit messages
- Don't remove and refactor simultaneously

### After Cleanup
- Verify all CI/CD pipelines pass
- Deploy to staging before production
- Monitor error rates after deployment
- Update .gitignore if new patterns identified
- Document what was removed and why

---

## Appendix: Language-Specific Tools

### Python
```bash
vulture .                    # Find dead code
autoflake --remove-all-unused-imports  # Remove unused imports
isort --remove-unused        # Clean up imports
pip-autoremove               # Find unused packages
```

### JavaScript/TypeScript
```bash
npx depcheck                 # Find unused dependencies
npx ts-prune                 # Find unused exports
npx unimported               # Find unimported files
```

### Ruby
```bash
debride .                    # Find dead code
bundle clean                 # Remove unused gems
rubocop --only Lint/UnusedMethodArgument
```

### Go
```bash
go mod tidy                  # Remove unused dependencies
staticcheck ./...            # Find unused code
```

### General
```bash
tokei .                      # Count lines by language
dust .                       # Find large directories
fd -e bak -e old -e orig     # Find backup files
```

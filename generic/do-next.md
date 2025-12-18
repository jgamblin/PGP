# Project Next Steps — Re-engagement Planning

> **Purpose**: Get back into a project after time away  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Languages**: Any  
> **Last Updated**: 2025-12

---

## Mission

Help developers **re-engage with projects** after a break. Quickly assess project state, identify priorities, and create an actionable plan for the next work session.

---

## Guard Clauses

**If no project context provided:**
```
NO_PROJECT_CONTEXT

Please provide project information:
- Project directory or repository
- Last known state/where you left off
- Any known issues or blockers
- Available time for this session
```

**If project is in good shape:**
```
PROJECT_HEALTHY

✅ Project assessment complete — ready to continue.

Status:
- Tests passing: ✓
- No critical issues: ✓
- Dependencies up to date: ✓
- Clear next steps identified: ✓

Recommended: Start with [specific task].
```

---

## Quick Context Checklist

```
☐ How long since last work on project?
☐ What were you working on last?
☐ Any unfinished features/branches?
☐ How much time do you have now?
```

---

## Copy-Paste Re-engagement Prompts

### Prompt: Quick Project Assessment
```text
Assess this project's current state:

Project structure:
{{STRUCTURE}}

Recent git history:
{{GIT_LOG}}

Open issues/TODOs:
{{ISSUES}}

Tell me:
1. What's the overall health?
2. What was I working on last?
3. What needs immediate attention?
4. What's a good task for a {{TIME}} session?
```

### Prompt: What Should I Do Next?
```text
I'm returning to this project after {{TIME_AWAY}}.

Last time I was:
{{LAST_ACTIVITY}}

Current state:
{{CURRENT_STATE}}

Available time: {{AVAILABLE_TIME}}

Give me:
1. Quick wins I can complete
2. Important tasks to tackle
3. Things to avoid (rabbit holes)
4. Specific first step to take now
```

### Prompt: Catch Me Up
```text
Summarize what's happened in this project:

Recent commits:
{{GIT_LOG}}

Changed files:
{{CHANGED_FILES}}

Tell me:
1. What major changes were made?
2. What's new or different?
3. What might have broken?
4. What should I verify works?
```

### Prompt: Prioritize My Tasks
```text
Help prioritize these tasks:

{{TASK_LIST}}

Context:
- Deadline: {{DEADLINE}}
- Available time: {{TIME}}
- Dependencies: {{DEPENDENCIES}}

Rank by:
1. Impact (what matters most)
2. Urgency (what's time-sensitive)
3. Effort (what's achievable)

Give me top 3 to focus on.
```

### Prompt: Unblock Me
```text
I'm stuck on this project:

What I'm trying to do:
{{GOAL}}

What's blocking me:
{{BLOCKER}}

What I've tried:
{{ATTEMPTS}}

Help me:
1. Identify the root cause
2. Suggest alternative approaches
3. Find a minimal next step
4. Decide if I should pivot
```

---

## Re-engagement Framework

### 1. **Quick Health Check** (5 min)

```bash
# Run these commands to assess project state

# Check git status
git status
git log --oneline -10

# Check for uncommitted work
git stash list
git branch -a

# Check dependencies
npm outdated  # or pip list --outdated, etc.

# Run tests
npm test  # or pytest, etc.
```

### 2. **Priority Matrix**

| Urgency \ Impact | High Impact | Low Impact |
|------------------|-------------|------------|
| **Urgent** | 🔴 Do First | 🟡 Schedule |
| **Not Urgent** | 🟠 Plan Next | 🟢 Maybe Later |

### 3. **Session Planning by Time**

| Available Time | Recommended Focus |
|----------------|-------------------|
| **15 min** | Fix one small bug, review PR, update docs |
| **30 min** | Complete a quick feature, write tests, refactor |
| **1 hour** | Implement feature, fix complex bug, code review |
| **2+ hours** | Major feature, architecture work, deep debugging |

### 4. **Quick Win Checklist**

Look for these easy tasks to build momentum:

- [ ] Update outdated dependencies
- [ ] Fix a simple bug from issue tracker
- [ ] Add missing documentation
- [ ] Write tests for untested code
- [ ] Clean up TODOs and FIXMEs
- [ ] Improve error messages
- [ ] Refactor a messy function

---

## Common Re-engagement Scenarios

### Scenario: "I don't remember where I left off"

```text
1. Check git log: `git log --oneline -20`
2. Look for WIP branches: `git branch -a`
3. Check stash: `git stash list`
4. Search for TODOs: `grep -r "TODO" --include="*.{js,py,ts}"`
5. Review recent files: `git diff HEAD~5 --stat`
```

### Scenario: "Everything is broken"

```text
1. Check if tests pass: run test suite
2. Check dependencies: `npm install` / `pip install -r requirements.txt`
3. Check environment: verify env vars, config files
4. Check recent changes: `git log --oneline -5`
5. Try a clean slate: `git stash && npm install`
```

### Scenario: "I have too many things to do"

```text
1. List all tasks (issues, TODOs, ideas)
2. Mark what's actually blocking progress
3. Identify what can be deferred
4. Pick ONE thing to focus on
5. Set a timer and commit to that task
```

---

## Report Format

### Session Plan: `do-next-[YYYY-MM-DD].md`

```markdown
# Session Plan - [Date]

## Project Status
- **Last Activity**: [When and what]
- **Current State**: [Healthy/Issues/Blocked]
- **Available Time**: [Duration]

## Quick Health Check
- [ ] Tests passing
- [ ] Dependencies up to date
- [ ] No critical issues
- [ ] Clear next steps

## Session Goals

### Must Do
1. [Critical task with time estimate]

### Should Do
1. [Important task]
2. [Important task]

### Could Do
1. [Nice to have]

## First Step
[Specific, actionable first step to take right now]

## Notes
- [Any context for future sessions]
```

---

## Tips for Staying Engaged

1. **Leave breadcrumbs**: Before stopping, write a note about what to do next
2. **Small commits**: Commit often so history tells a story
3. **Use TODOs**: Mark incomplete work clearly in code
4. **Track time**: Know how long tasks actually take
5. **Set boundaries**: Define session end time before starting

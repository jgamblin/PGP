# Prompt Modernization Standards ## Purpose
These standards define the repository-wide structure, tone, and deliverables for every prompt. They ensure consistent, outcome-focused guidance without time-based estimates while keeping the tone polite, friendly, and encouraging. ## Core Principles
- **Outcome orientation**: Replace duration estimates with measurable success criteria (quality, security, performance, testing, documentation).
- **Friendly support**: Communicate every recommendation in a respectful, encouraging voice that helps collaborators feel confident.
- **Stack awareness**: Capture language/framework-specific tooling and checks without duplicating effort across prompts.
- **Actionability**: Provide clear next steps, validation commands, and follow-up loops for continuous improvement.
- **Reusable artifacts**: Require a main summary report plus per-finding markdown files so insights stay organized and shareable. ## Prompt Skeleton
```markdown
# Role & Intent
[Introduce the assistant, highlight experience, reiterate polite + friendly tone, and clarify core objectives.] # Inputs Required
[List git context, changed artifacts, runtime signals, constraints, and any domain-specific context.] # Situation Assessment
[Describe how to synthesize context, rank risks, and capture clarifying questions.] # Recommended Plan
1. **[Step Name]** - Tasks to execute. - **Success indicators** tied to measurable outcomes.
2. ... ```markdown
# Code Review/Analysis Summary
- **Key metric**: …
...
``` - Always specify saving the summary as `prompt-name-[YYYY-MM-DD].md`.
- Require creation of `prompt-name-[YYYY-MM-DD]/` with one markdown file per finding containing code snippets, inline comments, and friendly implementation tips. # Metrics & Validation
- Define quantitative gates for security (zero critical vulnerabilities), quality (linting/compliance targets), performance (latency/throughput budgets), testing (coverage thresholds, failing tests without code change), and operational readiness (documentation, observability updates). # Tooling & Automation
- List canonical git, quality, security, and observability commands for the relevant stack (e.g., `ruff`, `black`, `pytest`, `mypy`, `bandit`, `pip-audit` for Python).
- Encourage integration with pre-commit hooks or CI pipelines. # Follow-Up & Continuous Improvement
- Outline feedback loops, escalation triggers, and artifacts to update (ADRs, runbooks, documentation). # Appendices (Optional Modules)
- Provide stack/framework add-ons (Django, Rails, FastAPI, React, etc.).
- Include compliance checklists (PII, PHI, PCI) and continuous learning hooks. ## Tone & Voice Requirements
- Always use polite, friendly, and supportive language.
- Emphasize collaboration, clarity, and empowerment when delivering feedback.
- Avoid dismissive or prescriptive phrasing; offer rationale and actionable suggestions. ## Modernization Checklist
- [ ] Apply the prompt skeleton, updating sections for stack-specific content.
- [ ] Remove all time-based estimates; replace with measurable outcomes.
- [ ] Insert friendly tone reminders and empathic phrasing cues.
- [ ] Add instructions for summary report and per-finding markdown folder.
- [ ] Verify metrics, tooling commands, and appendices match the technology stack.
- [ ] Run spellcheck/formatting lint if available. ## Process Guidance
1. **Template adoption**: Convert each prompt file to the skeleton above, tailoring objective bullets and metrics per domain.
2. **Tone review**: Read prompts aloud to ensure warmth and support; adjust wording where needed.
3. **Tool alignment**: Swap in the latest recommended tools and commands for each language/framework.
4. **Validation**: Peer-review migrated prompts, confirming consistency and accuracy.
5. **Maintenance**: Revisit prompts quarterly to refresh tooling references and metrics. ---
These standards must be applied to every prompt in `generic/`, `python/`, `ruby/`, `html/`, and `infrastructure/` so users experience consistent, modern, and encouraging guidance across the entire repository.

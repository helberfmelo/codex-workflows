---
name: codex-workflows
description: Full workflow operating system for GPT Codex in VS Code. Route natural-language requests into structured workflows for brainstorm, plan, create, enhance, debug, test, deploy, preview, status, orchestrate, and UI/UX design. Use when a team wants repeatable execution phases, specialist handoffs, approval checkpoints, and stronger delivery consistency across projects.
---

# Codex Workflows

Run delivery as a workflow system, not ad-hoc prompting.

## Core Loop

1. Detect project context (`.agent`, stack files, test tooling, deployment clues).
2. Route request to one primary workflow.
3. Run workflow phases in order with explicit checkpoints.
4. Validate outputs (tests, lint, typecheck, security checks when available).
5. Return concise report with next action.

Use this report header:

```md
Applying workflow: `/workflow-name`
Reason: <short rationale>
Confidence: <high|medium|low>
```

## Routing Rules

- Use one primary workflow first.
- Add secondary workflows only if they increase correctness.
- If request is ambiguous, ask up to 3 high-value questions.
- Prefer deterministic routing through `scripts/route_workflow.py` when available.

Read `references/routing/intent-matrix.md` for full mapping.

## Workflow Catalog

- `/brainstorm`
- `/plan`
- `/create`
- `/enhance`
- `/debug`
- `/test`
- `/deploy`
- `/preview`
- `/status`
- `/orchestrate`
- `/ui-ux-pro-max`

Read detailed procedures in `references/workflows/`.

## Orchestration Policy

Use `/orchestrate` for multi-domain tasks or when uncertainty is high.

- Minimum 3 specialist perspectives.
- Planning phase first for complex changes.
- User checkpoint between plan and implementation.
- Final synthesis with verification evidence.

Read `references/orchestration/phase-gates.md`.

## Project Integration

If local `.agent` exists, prioritize local instructions in this order:

1. `.agent/workflows/<workflow>.md`
2. `.agent/skills/*/SKILL.md` related to task
3. `.agent/rules/*.md`
4. `.agent/ARCHITECTURE.md`

If local `.agent` is missing, use repository templates:

- `templates/.agent/` (full, Antigravity-compatible template baseline)
- `templates/minimal/.agent/` (lightweight starter profile)

Bootstrap these templates with `scripts/bootstrap_project_agent.py`.

## Compatibility Profiles

Use `scripts/bootstrap_project_agent.py` with one of:

- `--profile antigravity-compat`: full compatibility pack with agents, skills, workflows, scripts, rules, and shared assets.
- `--profile minimal`: lightweight starter `.agent` template.

Full compatibility pack location:

- `packs/antigravity-compat/.agent/`

## Output Contract

Always include:

- Workflow selected + reason + confidence
- Completed phases
- Files changed
- Verifications run and result
- Risks or assumptions
- Next immediate action

Use report templates from `references/templates/output-templates.md`.

---
name: codex-workflows
description: Route user requests to workflow-driven execution in Codex for VS Code. Use when the user asks to brainstorm, plan, create, enhance, debug, test, deploy, preview, check status, orchestrate multi-domain tasks, or run advanced UI/UX design flow. Apply in any project, and prefer local .agent/workflows when available.
---

# Codex Workflows

Run workflow-based delivery in Codex with explicit phases, checkpoints, and verification.

## Quick Start

1. Detect if `.agent/workflows` exists in the repository.
2. Classify user intent to one primary workflow.
3. Announce selected workflow in one line.
4. Execute phases in order.
5. Return deliverables and validation summary.

Use this format:

```md
Applying workflow: `/workflow-name`
Reason: <short rationale>
```

## Workflow Selection

Select one primary workflow first. Add secondary workflows only when required.

- Brainstorm intent: use `/brainstorm`.
- Planning intent: use `/plan`.
- New build intent: use `/create`.
- Existing feature update intent: use `/enhance`.
- Failure investigation intent: use `/debug`.
- Test generation or execution intent: use `/test`.
- Release intent: use `/deploy`.
- Local run and health intent: use `/preview`.
- Progress dashboard intent: use `/status`.
- Multi-domain complex execution intent: use `/orchestrate`.
- Advanced visual design intent: use `/ui-ux-pro-max`.

When intent is ambiguous, ask up to 3 focused clarifying questions, then continue.

## Execution Rules

- Follow phase-based execution. Do not skip discovery for unclear requests.
- For complex tasks, require plan approval before broad implementation.
- Keep outputs concise, actionable, and file-referenced.
- Prefer deterministic checks: tests, lint, typecheck, and security checks where available.
- If `.agent` scripts exist, prefer them over re-implementing equivalent logic.

## Orchestration Rules

Use `/orchestrate` when two or more strong domains are present, for example security + backend + frontend.

- Use at least 3 specialist perspectives.
- Create plan first for high-complexity work.
- Require user approval between planning and implementation.
- End with verification and a unified report.

## Local Repository Integration

If `.agent` exists, load local files in this order:

1. `.agent/workflows/<workflow>.md`
2. `.agent/skills/*/SKILL.md` relevant to the workflow
3. `.agent/ARCHITECTURE.md` for global constraints

If `.agent` does not exist, run this skill with `references/workflow-playbook.md`.

## Output Contract

Always include:

- Selected workflow and reason
- Phases completed
- Files changed (if any)
- Verification run and result
- Next immediate step

## Reference

Read `references/workflow-playbook.md` for detailed phase templates and workflow-specific checklists.

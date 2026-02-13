---
description: Codex-native planning workflow for converting ambiguous requests into executable, verifiable plans.
---

# /plan - Codex-Native Planning Blueprint

$ARGUMENTS

---

## Objective

Produce an implementation-ready plan before coding.

This workflow is planning-only. Do not write production code while running `/plan`.

---

## Planning Intake

Capture:

1. Target outcome:
- what success looks like
- who uses it
2. Constraints:
- stack limitations
- deadlines
- compliance/security constraints
3. Non-goals:
- what should not be changed now

If critical inputs are missing, ask up to 3 focused questions and continue.

---

## Plan File Rules

Create one file:

- `docs/PLAN-{slug}.md`

Slug rules:

1. Use 2 to 4 core terms from the request.
2. Lowercase and hyphen-separated.
3. Keep under 36 characters.
4. Avoid generic slugs (`plan`, `task`, `project`).

Examples:

- `docs/PLAN-auth-hardening.md`
- `docs/PLAN-payment-retry-strategy.md`
- `docs/PLAN-rust-cli-release-flow.md`

---

## Required Plan Sections

The generated plan must include:

1. Problem statement
- current pain
- expected outcome
2. Scope
- in scope
- out of scope
3. Architecture impact
- components touched
- contract/data changes
4. Work breakdown
- ordered tasks
- dependencies
5. Validation matrix
- command-level checks per task
6. Rollback strategy
- how to revert safely
7. Risks and assumptions
- risk score `low|medium|high`
8. Acceptance criteria
- explicit pass conditions

---

## Definition of Done for /plan

Planning is complete only if:

- file exists at `docs/PLAN-{slug}.md`;
- all required sections are filled with concrete details;
- each task has an owner lens (`backend`, `frontend`, `security`, `qa`, `ops`, etc.);
- validation matrix contains runnable commands;
- acceptance criteria are testable.

---

## Output Contract

Return this structure:

```markdown
## Planning Summary

### Plan File
`docs/PLAN-{slug}.md`

### Scope Snapshot
- In: [...]
- Out: [...]

### Workstreams
1. [workstream]
2. [workstream]
3. [workstream]

### Verification Matrix
- `[command]` -> [target]

### Risks
- [risk]: [mitigation]

### Next Action
[what to run next, usually /orchestrate or /create]
```

---

## Usage Examples

```text
/plan harden authentication for API and admin panel
/plan migrate release flow to tag-driven automation
/plan add stack validation packs for python services
```


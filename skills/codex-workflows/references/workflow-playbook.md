# Workflow Playbook

This reference defines how to execute each workflow in Codex.

## 1) /brainstorm

Goal: explore options before implementation.

Phases:
1. Define problem, users, constraints.
2. Generate at least 3 options.
3. Compare tradeoffs and recommend one.

Deliverable: option matrix with effort and risks.

## 2) /plan

Goal: produce implementation plan only.

Phases:
1. Clarify scope with focused questions.
2. Create task breakdown and milestones.
3. Define verification gates and owners.

Deliverable: plan file (for example `docs/PLAN-<slug>.md`).
Rule: do not implement code during planning-only flow.

## 3) /create

Goal: build a new app or major capability.

Phases:
1. Requirement discovery.
2. Plan and architecture selection.
3. Implementation across backend/frontend/data.
4. Validation and preview.

Deliverable: runnable feature baseline plus checks summary.

## 4) /enhance

Goal: improve existing app incrementally.

Phases:
1. Inspect current state.
2. Propose diff and impact.
3. Apply changes.
4. Re-test affected areas.

Deliverable: targeted improvements with regression checks.

## 5) /debug

Goal: find root cause and apply minimal safe fix.

Phases:
1. Capture symptom, reproduction, expected behavior.
2. Rank hypotheses.
3. Test hypotheses.
4. Fix and add prevention.

Deliverable: root-cause report plus patch plus preventive test.

## 6) /test

Goal: generate and or run tests.

Phases:
1. Identify test target and boundaries.
2. Cover happy path, edge cases, and failure cases.
3. Run tests and summarize failures.

Deliverable: test files and execution summary.

## 7) /deploy

Goal: release safely.

Phases:
1. Pre-flight checks (type, lint, tests, security).
2. Build and deploy to target environment.
3. Post-deploy verification and rollback readiness.

Deliverable: deploy report with environment and status.

## 8) /preview

Goal: manage local preview server.

Phases:
1. Start, status, stop, or restart server.
2. Check health endpoint.
3. Report URL and runtime status.

Deliverable: preview status block.

## 9) /status

Goal: show project progress snapshot.

Phases:
1. Read current scope and completed items.
2. Show in-progress and pending work.
3. Include preview and test status if available.

Deliverable: concise status board.

## 10) /orchestrate

Goal: solve complex multi-domain work with coordinated specialists.

Phases:
1. Planning phase (sequential).
2. Approval checkpoint.
3. Implementation phase (parallel where possible).
4. Verification and synthesis.

Minimum: use 3 specialist perspectives for true orchestration.
Deliverable: orchestration report with contributions and outcomes.

## 11) /ui-ux-pro-max

Goal: design with high-quality style system and implementation guidance.

Phases:
1. Extract product, audience, style, and platform.
2. Generate design system choices.
3. Implement components and validate accessibility and performance.

Deliverable: design tokens plus component guidance plus implementation steps.

## Intent Mapping

Map intent keywords to primary workflow:

- ideate, options, compare -> `/brainstorm`
- plan, roadmap, break down -> `/plan`
- build from scratch, new app -> `/create`
- improve, refactor, add feature -> `/enhance`
- bug, error, broken -> `/debug`
- tests, coverage -> `/test`
- release, production, rollback -> `/deploy`
- run locally, preview URL -> `/preview`
- progress, what is done -> `/status`
- complex, end-to-end, multi-team -> `/orchestrate`
- design system, UI direction -> `/ui-ux-pro-max`

## Source Alignment

This playbook is inspired by Antigravity Kit workflows and adapted for Codex in VS Code.

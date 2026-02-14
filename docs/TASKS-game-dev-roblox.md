# Tasks: Game Development + Roblox Workflow

Date: 2026-02-14
Mode: `/orchestrate`
Scope: add first-class game development support in codex-workflows, including a Roblox-specific workflow.

## Stage 1: Baseline and Gap Confirmation

Status: `completed`

Tasks:

- [x] Confirm existing codex-native agents/skills/workflows for game and Roblox.
- [x] Confirm routing and quality gates impacted by adding workflows.
- [x] Define implementation sequence and validations.

Acceptance:

- Baseline recorded and no ambiguity about missing assets.

## Stage 2: Core Assets (Agents, Skills, Workflows)

Status: `completed`

Tasks:

- [x] Add codex-native agent(s) for game and Roblox.
- [x] Add codex-native skill(s) for general game development and Roblox delivery.
- [x] Add `/game-dev` workflow across codex-native + references + compat/template tracks.
- [x] Add `/roblox-game-dev` workflow across codex-native + references + compat/template tracks.

Acceptance:

- New game + Roblox workflows exist in all parity-checked tracks.
- New codex-native game assets are materialized under `.agent/agents` and `.agent/skills`.

## Stage 3: Routing, Gates, and Tests

Status: `completed`

Tasks:

- [x] Extend workflow router rules for game and Roblox intent detection.
- [x] Update native quality checker expected workflow set and section requirements.
- [x] Update native assets checker expected workflow set and required skill/agent guards.
- [x] Add/adjust tests to cover routing and validation for new workflows.

Acceptance:

- Routing selects `/game-dev` or `/roblox-game-dev` for relevant prompts.
- Test suite and validation scripts pass with the expanded catalog.

## Stage 4: Documentation and Website (All Locales)

Status: `completed`

Tasks:

- [x] Update root docs (`README.md`, architecture/comparison/workflow contract where relevant).
- [x] Update workflow catalog docs for EN/PT/ES/FR/ZH.
- [x] Sync `docs/*` into `website/docs/*/reference/source`.
- [x] Build docs portal and confirm locale parity.

Acceptance:

- Catalog and counts reflect the new workflows.
- Website docs build successfully and locales remain aligned.

## Stage 5: Final Validation, Commit, Push

Status: `completed`

Tasks:

- [x] Run full validation (`tests`, workflow parity, quality, assets, docs build).
- [x] Commit with release-grade message.
- [x] Push to `origin/main`.

Acceptance:

- Clean validation evidence captured.
- Remote repository updated with all requested changes.

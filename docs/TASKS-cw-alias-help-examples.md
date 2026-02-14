# Tasks: `cw` Alias + `/help` + `/examples`

Date: 2026-02-14
Mode: `/orchestrate`
Scope: implement short activation alias for all workflows and utility commands for help/examples.

## Stage 1: Design and Baseline

Status: `completed`

Tasks:

- [x] Confirm current explicit activation patterns and router behavior.
- [x] Define alias scope: `cw`, `codex-workflow`, `codex-workflows`.
- [x] Define utility commands: `cw /help` and `cw /examples`.

Acceptance:

- A clear implementation plan exists for router, tests, docs, and deployment.

## Stage 2: Router Implementation

Status: `completed`

Tasks:

- [x] Extend explicit activation parsing to accept `cw` and `codex-workflow`.
- [x] Add utility command parsing for `/help` and `/examples`.
- [x] Implement terminal-style help and examples output.
- [x] Keep existing `codex-workflows /<workflow>` activation working.

Acceptance:

- `cw /<workflow>` resolves like current explicit workflow activation.
- `cw /help` and `cw /examples` produce deterministic outputs.

## Stage 3: Validation and Tests

Status: `completed`

Tasks:

- [x] Add tests for alias activation (`cw`, singular/plural name forms).
- [x] Add tests for `/help` and `/examples`.
- [x] Run targeted and full test suites.

Acceptance:

- Router tests pass for both baseline and fast routers.
- Full validation suite remains green.

## Stage 4: Documentation + Website (All Locales)

Status: `completed`

Tasks:

- [x] Update root documentation with alias and utility command usage.
- [x] Update website docs (EN/PT/ES/FR/ZH) for quickstart/workflows/installation.
- [x] Sync reference docs and build website.

Acceptance:

- All public docs show alias and utility commands consistently.
- Locale parity remains intact.

## Stage 5: Release Delivery

Status: `completed`

Tasks:

- [x] Commit all changes with release-appropriate message.
- [x] Push to `origin/main`.
- [x] Confirm deploy trigger path and final repository status.

Acceptance:

- Remote repository updated and deploy workflow triggered by docs changes.

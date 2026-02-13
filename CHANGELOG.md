# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog and this project follows Semantic Versioning.

## [Unreleased]

### Added

- Skill upgrade to workflow operating system model.
- Routing matrix and orchestration phase gate references.
- Per-workflow knowledge files under `references/workflows/`.
- Output report templates for standard and orchestration flows.
- `route_workflow.py` deterministic workflow classifier.
- `bootstrap_project_agent.py` to scaffold `.agent` into any project.
- `bootstrap_project_agent.py --profile` support (`minimal`, `antigravity-compat`).
- Built-in `.agent` templates with workflows, rules, and architecture.
- Full compatibility pack at `skills/codex-workflows/packs/antigravity-compat/.agent`.
- `sync_compat_pack.py` to refresh compatibility pack from a local `.agent` source.
- Upgraded `templates/.agent` to full detailed workflows and full `.agent` structure.
- Added separate lightweight profile at `templates/minimal/.agent`.
- `docs/ARCHITECTURE.md` and `docs/COMPARISON.md`.
- Compatibility governance:
  - `build_compat_manifest.py`
  - `check_compat_drift.py`
  - `compat/manifest.json`
- Workflow integrity:
  - `check_workflow_parity.py`
  - `docs/WORKFLOW_CONTRACT.md`
- Performance and runtime:
  - `route_workflow_fast.py`
  - `routing_data.py`
  - `benchmark_router.py`
  - `docs/PERFORMANCE.md`
- Quality and CI:
  - `.github/workflows/ci.yml`
  - `tests/test_route_workflow.py`
  - `tests/test_bootstrap_profiles.py`
  - `tests/test_sync_compat_pack.py`
  - `scripts/ci_validate_skill.py`
- Operations and release docs:
  - `docs/COMPATIBILITY.md`
  - `docs/OPERATIONS.md`
  - `docs/RELEASE.md`
  - `docs/ROBUSTNESS-CHECKLIST.md`
- Codex-native domain packs:
  - `skills/codex-backend-pack`
  - `skills/codex-frontend-pack`
  - `skills/codex-security-pack`
  - `skills/codex-qa-pack`

## [1.0.0] - 2026-02-13

### Added

- Initial public release of `codex-workflows` skill.
- Workflow routing for `/brainstorm`, `/plan`, `/create`, `/enhance`, `/debug`, `/test`, `/deploy`, `/preview`, `/status`, `/orchestrate`, and `/ui-ux-pro-max`.
- Skill metadata in `agents/openai.yaml`.
- Workflow reference playbook in `references/workflow-playbook.md`.
- Installation and usage documentation.

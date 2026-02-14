# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog and this project follows Semantic Versioning.

## [Unreleased]

### Added

- `cw` CLI Windows reliability improvements (Python candidate priority/fallback).
- Node unit tests for CLI candidate/fallback behavior: `tests/test_cw_cli_node.js`.
- Cross-platform installer E2E matrix in CI:
  - `cw-install-e2e-matrix` (Linux/macOS/Windows)
  - real install path via `npx @codex-workflow/cw`
- Release automation now syncs `package.json` version with release version.
- Release workflow npm publish automation on `v*` tag push using `NPM_TOKEN`.
- New larger blueprint examples:
  - `examples/real-world/*`
- New quick wins by profile:
  - `examples/quick-wins/*`
- Release workflow now supports auto-publish on `v*` tag push.
- Web docs portal at `website/` using VitePress.
- GitHub Pages deployment workflow for portal: `.github/workflows/docs.yml`.
- CI build gate for portal in `.github/workflows/ci.yml`.
- Technical docs mirror sync script: `website/scripts/sync_reference_docs.py`.
- Portal UI/UX upgrade with premium visual theme and professional navigation.
- Multilingual docs support (English + Portuguese/Brazil).
- Composer wrapper channel:
  - `composer.json`
  - `scripts/composer_install.php`
- Added Docs badge to `README.md` and stronger EN/PT-BR language switch CTA in top navigation.
- Expanded multilingual docs to Spanish, French, and Chinese.
- New default bootstrap profile: `codex-native`.
- Codex-native rewritten workflow set for all 11 commands under:
  - `skills/codex-workflows/templates/codex-native/.agent/workflows/`
- Codex-native quality checker:
  - `skills/codex-workflows/scripts/check_codex_native_quality.py`
- CI enforcement for codex-native workflow quality in `.github/workflows/ci.yml`.
- New unit tests:
  - `tests/test_codex_native_quality.py`
- Operations CLI command:
  - `python skills/codex-workflows/scripts/codex_workflows_ops.py check-codex-native`
- Website docs updates (EN/PT/ES/FR/ZH) to reflect codex-native default and quality validation steps.
- Source docs parity for all website locales (EN/PT/ES/FR/ZH), including:
  - `architecture`, `comparison`, `workflow-contract`, `community`, `operations`, `release`, `robustness-checklist`, `compatibility`, `performance`.
- Codex-native profile independence:
  - `bootstrap_project_agent.py` now sources `templates/codex-native/.agent` directly for default profile.
  - Added codex-native profile assets:
    - `skills/codex-workflows/templates/codex-native/.agent/ARCHITECTURE.md`
    - `skills/codex-workflows/templates/codex-native/.agent/rules/CODEX.md`
    - `skills/codex-workflows/templates/codex-native/.agent/scripts/auto_preview.py`
- Unified repository CLI:
  - `scripts/codexwf.py` with `install`, `init`, `status`, `validate`, and `docs-sync`.
  - tests: `tests/test_codexwf_cli.py`
- Public governance templates:
  - `.github/ISSUE_TEMPLATE/bug_report.yml`
  - `.github/ISSUE_TEMPLATE/feature_request.yml`
  - `.github/ISSUE_TEMPLATE/config.yml`
  - `.github/PULL_REQUEST_TEMPLATE.md`
  - `.github/CODEOWNERS`
- Community docs:
  - `docs/COMMUNITY.md`
  - `website/docs/reference/community.md` + locale variants (`pt`, `es`, `fr`, `zh`)

### Fixed

- GitHub Actions shell reliability on Linux/macOS by removing backslash-based command continuations in workflow steps.
- Cross-platform E2E install workflow now resolves `python/python3` dynamically and runs `npx @codex-workflow/cw` from isolated temp workspace.
- Added `.gitattributes` LF rules for GitHub workflow files to avoid CRLF-induced CI regressions.

## [1.1.0] - 2026-02-13

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
- Stack validation packs:
  - `skills/codex-node-validation-pack`
  - `skills/codex-python-validation-pack`
  - `skills/codex-rust-validation-pack`
- Stack validator tests:
  - `tests/test_stack_validators.py`
- Release automation:
  - `scripts/release_automation.py`
  - `.github/workflows/release.yml`
  - `tests/test_release_automation.py`
- End-to-end real project examples:
  - `examples/node-auth-api/README.md`
  - `examples/python-fastapi-orders/README.md`
  - `examples/rust-events-cli/README.md`
- Runnable stack fixtures for CI matrix:
  - `examples/projects/node-service`
  - `examples/projects/python-service`
  - `examples/projects/rust-service`
- CI stack matrix (Node/Python/Rust) executing real pack checks:
  - `.github/workflows/ci.yml`
- All-in-one installation automation:
  - `scripts/install_all_in_one.py`
  - README and operations docs updated with one-command install flow

## [1.0.0] - 2026-02-13

### Added

- Initial public release of `codex-workflows` skill.
- Workflow routing for `/brainstorm`, `/plan`, `/create`, `/enhance`, `/debug`, `/test`, `/deploy`, `/preview`, `/status`, `/orchestrate`, and `/ui-ux-pro-max`.
- Skill metadata in `agents/openai.yaml`.
- Workflow reference playbook in `references/workflow-playbook.md`.
- Installation and usage documentation.

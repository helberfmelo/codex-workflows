# Source: docs/ROBUSTNESS-CHECKLIST.md

# Robustness Checklist

Date: 2026-02-13

## Structure parity

- [x] Full compatibility pack exists
Evidence: `skills/codex-workflows/packs/antigravity-compat/.agent/`
- [x] Full template exists
Evidence: `skills/codex-workflows/templates/.agent/`
- [x] Minimal template exists
Evidence: `skills/codex-workflows/templates/minimal/.agent/`
- [x] Codex-native template overlay exists
Evidence: `skills/codex-workflows/templates/codex-native/.agent/workflows/`

## Workflow quality

- [x] Full workflow files are detailed (not stubs)
Evidence: `skills/codex-workflows/templates/.agent/workflows/orchestrate.md`
- [x] Workflow parity checker exists
Evidence: `skills/codex-workflows/scripts/check_workflow_parity.py`
- [x] Codex-native workflow set is fully rewritten
Evidence: `skills/codex-workflows/templates/codex-native/.agent/workflows/*.md`
- [x] Codex-native quality checker exists
Evidence: `skills/codex-workflows/scripts/check_codex_native_quality.py`

## Sync and routing automation

- [x] Compatibility sync script exists
Evidence: `skills/codex-workflows/scripts/sync_compat_pack.py`
- [x] Manifest build/check scripts exist
Evidence: `skills/codex-workflows/scripts/build_compat_manifest.py`, `skills/codex-workflows/scripts/check_compat_drift.py`
- [x] Baseline and fast routers exist
Evidence: `skills/codex-workflows/scripts/route_workflow.py`, `skills/codex-workflows/scripts/route_workflow_fast.py`

## Documentation and operations

- [x] Architecture documented
Evidence: `docs/ARCHITECTURE.md`
- [x] Compatibility maintenance documented
Evidence: `docs/COMPATIBILITY.md`
- [x] Operations runbook documented
Evidence: `docs/OPERATIONS.md`
- [x] Release runbook documented
Evidence: `docs/RELEASE.md`
- [x] Workflow contract documented
Evidence: `docs/WORKFLOW_CONTRACT.md`
- [x] Web docs portal exists and is deployable
Evidence: `website/`, `.github/workflows/docs.yml`
- [x] Web docs are multilingual (EN + PT-BR + ES + FR + ZH)
Evidence: `website/docs/index.md`, `website/docs/pt/index.md`, `website/docs/es/index.md`, `website/docs/fr/index.md`, `website/docs/zh/index.md`

## Quality and CI

- [x] CI workflow exists
Evidence: `.github/workflows/ci.yml`
- [x] CI enforces codex-native quality check
Evidence: `.github/workflows/ci.yml`, `skills/codex-workflows/scripts/check_codex_native_quality.py`
- [x] CI stack matrix exists with real example projects
Evidence: `.github/workflows/ci.yml`, `examples/projects/node-service`, `examples/projects/python-service`, `examples/projects/rust-service`
- [x] Release workflow exists
Evidence: `.github/workflows/release.yml`
- [x] Unit tests for routing/bootstrap/sync exist
Evidence: `tests/test_route_workflow.py`, `tests/test_bootstrap_profiles.py`, `tests/test_sync_compat_pack.py`
- [x] Unit tests for stack validators and release automation exist
Evidence: `tests/test_stack_validators.py`, `tests/test_release_automation.py`
- [x] Skill validator for CI exists
Evidence: `scripts/ci_validate_skill.py`

## Stack validation and examples

- [x] Stack validation packs for Node/Python/Rust exist
Evidence: `skills/codex-node-validation-pack`, `skills/codex-python-validation-pack`, `skills/codex-rust-validation-pack`
- [x] End-to-end examples catalog exists
Evidence: `examples/README.md`, `examples/node-auth-api/README.md`, `examples/python-fastapi-orders/README.md`, `examples/rust-events-cli/README.md`
- [x] All-in-one installer exists
Evidence: `scripts/install_all_in_one.py`
- [x] Composer wrapper installation channel exists
Evidence: `composer.json`, `scripts/composer_install.php`

## Outcome

Checklist status: Pass (all required controls present with file-level evidence).

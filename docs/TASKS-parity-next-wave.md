# Tasks: Parity Next Wave (Post v1.2.0)

Date: 2026-02-14
Scope: close the remaining robustness/professionalism gaps from the latest comparison against `vudovn/antigravity-kit`.

## Baseline Findings

- `codex-workflows` has strong workflow contracts, CI gates, release automation, and multilingual docs.
- Copy-risk on runtime workflow references is low (native vs compat similarity far below threshold).
- Remaining gap at analysis time: `codex-native` template had no native `agents/` or `skills/` layer.

## Stage 1: Codex-Native Capability Layer

Status: `completed`

Tasks:

- [x] Add native `agents/` catalog under `templates/codex-native/.agent/agents`.
- [x] Add native `skills/` catalog under `templates/codex-native/.agent/skills`.
- [x] Update bootstrap tests to validate native assets are materialized in default profile.

Acceptance:

- `bootstrap_project_agent.py --profile codex-native` produces `.agent/agents` and `.agent/skills`.
- Unit tests pass for bootstrap profile behavior.

## Stage 2: Native Asset Governance Gates

Status: `completed`

Tasks:

- [x] Add `check_codex_native_assets.py` for structural checks (agents/skills/workflows/rules/scripts).
- [x] Add tests for the new gate.
- [x] Wire checks into CI and unified CLIs.

Acceptance:

- CI includes native asset gate.
- `python scripts/codexwf.py validate --tests` passes.

## Stage 3: Final Docs and Portal Sync (Last)

Status: `completed`

Tasks:

- [x] Update root docs for native capability layer and new governance gate.
- [x] Sync website source docs after all code changes.
- [x] Keep EN/PT/ES/FR/ZH docs aligned.
- [x] Build portal and verify locale parity.

Acceptance:

- `python scripts/codexwf.py docs-sync --build` passes.
- `python scripts/codexwf.py status --json` shows no locale gaps.

## Stage 4: Final Validation and Comparison Evidence

Status: `completed`

Tasks:

- [x] Run full validation bundle.
- [x] Re-run comparison metrics and record residual gaps.
- [x] Mark all stages completed with evidence.

Acceptance:

- `python -m unittest discover -s tests -p "test_*.py"` passes.
- `python scripts/codexwf.py validate --tests --docs` passes.
- Comparison confirms robust parity posture with reduced copy-risk.

## Stage 5: Native Catalog Expansion to Parity Targets

Status: `completed`

Tasks:

- [x] Expand codex-native agents catalog from 12 to 20.
- [x] Expand codex-native skills catalog from 8 to 37.
- [x] Raise all structural gate thresholds in CI, CLIs, and tests.
- [x] Re-validate codex-native quality and structural checks.

Acceptance:

- `check_codex_native_assets.py` defaults require `--min-agents 20 --min-skills 37`.
- CI and local CLIs use the same 20/37 thresholds.
- Full unit test suite passes.

## Evidence (2026-02-14)

- Native capability assets added:
  - `skills/codex-workflows/templates/codex-native/.agent/agents/*.md` (`20` files)
  - `skills/codex-workflows/templates/codex-native/.agent/skills/*/SKILL.md` (`37` directories)
- New governance gate:
  - `skills/codex-workflows/scripts/check_codex_native_assets.py`
  - `tests/test_codex_native_assets.py`
- CI and CLIs wired:
  - `.github/workflows/ci.yml`
  - `scripts/codexwf.py`
  - `skills/codex-workflows/scripts/codex_workflows_ops.py`
- Validation results:
  - `python -m unittest discover -s tests -p "test_*.py"` -> pass (`32 tests`)
  - `python scripts/codexwf.py validate --tests` -> pass
  - `python skills/codex-workflows/scripts/check_codex_native_assets.py --native-root skills/codex-workflows/templates/codex-native/.agent --min-agents 20 --min-skills 37` -> pass
  - `python scripts/codexwf.py status --json` -> locale parity pass (`missing=0` for PT/ES/FR/ZH)
- Comparison metrics:
  - `codex_native_agents=20` vs `ant_agents=20`
  - `codex_native_skills=37` vs `ant_skills=37`
  - `refs_vs_compat_identical=0`
  - `refs_vs_compat_max_similarity=0.118106`

## Residual Gaps (Next Cycle)

- Add benchmark threshold history for routing/bootstrap performance trends.

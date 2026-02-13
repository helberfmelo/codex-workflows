# PLAN: Robustness Parity for Codex Workflows

Date: 2026-02-13
Repository: `D:\Projetos\codex-workflows-skill`
Mode: `/orchestrate` (Phase 1 + Phase 2 only)

## Objective

Evolve `codex-workflows` to be as robust as (or more robust than) Antigravity Kit for the VS Code + GPT Codex reality.

## Phase 1: Diagnostic Summary

### Baseline Evidence

- Source `.agent` (local baseline): 20 agents, 37 skills, 11 workflows, ~200 files.
- `packs/antigravity-compat/.agent`: 20 agents, 37 skills, 11 workflows, 198 files.
- `templates/.agent` (full): 20 agents, 37 skills, 11 workflows, 199 files.
- Missing in pack/template vs source: only 2 `__pycache__` binaries (`.pyc`) intentionally excluded.
- `references/workflows/*.md`: 11 files; detailed content present (e.g. `orchestrate.md` 176 lines, `ui-ux-pro-max.md` 215 lines).
- Script surface: `route_workflow.py`, `bootstrap_project_agent.py`, `sync_compat_pack.py`.
- Performance spot check: router CLI average ~264 ms/call (50 runs, cold process spawn pattern).
- Size: `skills/codex-workflows` ~2.94 MB; compatibility pack ~1.45 MB.

### Gap Analysis by Domain

1. Structure
- Status: strong parity on `.agent` structure (full pack + full template + minimal template).
- Gap: no versioned manifest tying compatibility pack to source revision/fingerprint.

2. Workflows
- Status: full workflow content in references and full template.
- Gap: no automated drift checker ensuring `references/workflows` and full template/workflow pack remain in sync.

3. Skills
- Status: full skill corpus included in compatibility pack/template.
- Gap: no codex-native domain packs at root level (only one top-level skill package).

4. Scripts/Automation
- Status: router + bootstrap + sync exist.
- Gap: missing unified operations CLI (`status/check/sync/bootstrap/validate`) and missing health/check scripts for maintainers.

5. Docs/Operations
- Status: README + architecture + comparison + changelog exist.
- Gap: no formal operations runbook, release runbook, or compatibility maintenance guide.

6. Performance
- Status: router works and detects multi-domain orchestration.
- Gap: no benchmark script, no performance SLO, no optimization mode for routing.

7. Quality/CI
- Status: skill quick validation works manually.
- Gap: no CI pipeline (`.github/workflows` absent), no tests for custom scripts, no checklist gate automation.

## Phase 2: Detailed Plan (Stop for approval after this section)

## Stream A: Compatibility Governance (P0)

Deliverables:
- `skills/codex-workflows/compat/manifest.json`
- `skills/codex-workflows/scripts/check_compat_drift.py`
- `skills/codex-workflows/scripts/build_compat_manifest.py`
- `docs/COMPATIBILITY.md`

Acceptance criteria:
- Manifest lists source path, file counts, and checksums.
- Drift checker fails if pack/template diverges from manifest.
- Compatibility update process documented and reproducible.

## Stream B: Workflow Integrity (P0)

Deliverables:
- `skills/codex-workflows/scripts/check_workflow_parity.py`
- `docs/WORKFLOW_CONTRACT.md`

Acceptance criteria:
- Automated check confirms parity among:
  - `references/workflows/*.md`
  - `templates/.agent/workflows/*.md`
  - `packs/antigravity-compat/.agent/workflows/*.md`
- Fails on missing/changed files.

## Stream C: Runtime and Performance (P1)

Deliverables:
- `skills/codex-workflows/scripts/benchmark_router.py`
- `skills/codex-workflows/scripts/route_workflow_fast.py` (cached/optimized classifier)
- `docs/PERFORMANCE.md`

Acceptance criteria:
- Benchmark script produces reproducible numbers.
- Fast router median latency improves over current baseline.
- Performance targets documented.

## Stream D: Quality and CI (P1)

Deliverables:
- `.github/workflows/ci.yml`
- `tests/test_route_workflow.py`
- `tests/test_bootstrap_profiles.py`
- `tests/test_sync_compat_pack.py`

Acceptance criteria:
- CI runs lint + tests + skill validation.
- Tests cover routing behavior, profile bootstrap, and sync safety.
- CI blocks regressions.

## Stream E: Operations and Release (P1)

Deliverables:
- `docs/OPERATIONS.md`
- `docs/RELEASE.md`
- `docs/ROBUSTNESS-CHECKLIST.md`

Acceptance criteria:
- Operational procedures documented (bootstrap, sync, validation, recovery).
- Release process standardized (versioning, changelog, tag checklist).
- Robustness checklist closes with explicit file evidence.

## Stream F: Codex-native Domain Packs (P2)

Deliverables:
- `skills/codex-backend-pack/`
- `skills/codex-frontend-pack/`
- `skills/codex-security-pack/`
- `skills/codex-qa-pack/`

Acceptance criteria:
- Domain packs installable independently.
- Router can recommend secondary pack by domain.
- Improves maintainability over single monolith skill.

## Execution Order for Phase 3

1. Stream A (governance)
2. Stream B (workflow integrity)
3. Stream D (quality/CI)
4. Stream C (performance)
5. Stream E (operations/release)
6. Stream F (domain packs)

## Phase 4 Validation Plan

- `quick_validate.py` for all skill folders.
- Run new script test suite.
- Run drift/parity checks.
- Fill and publish `docs/ROBUSTNESS-CHECKLIST.md` with evidence.
- Final status report with pass/fail matrix.

## Minimum Acceptance Criteria Coverage

- Workflows completos (não stubs): covered by Stream B checks.
- Perfis bootstrap (full/minimal): maintained and tested in Stream D.
- Automações de sync e roteamento: hardened in Streams A/C/D.
- Documentação de arquitetura e operação: extended in Stream E.
- Checklist comparativo fechado com evidências: delivered in Stream E + Phase 4.

## Phase 3 Implementation Summary (Executed)

Implemented streams:

- Stream A: compatibility governance
  - Added `compat/manifest.json`
  - Added `build_compat_manifest.py` and `check_compat_drift.py`
- Stream B: workflow integrity
  - Added `check_workflow_parity.py`
  - Added `docs/WORKFLOW_CONTRACT.md`
- Stream C: performance/runtime
  - Added `route_workflow_fast.py`, `routing_data.py`, `benchmark_router.py`
  - Updated baseline router to avoid false positives and emit `recommended_packs`
- Stream D: quality/CI
  - Added `.github/workflows/ci.yml`
  - Added tests for routing/bootstrap/sync
  - Added `scripts/ci_validate_skill.py`
- Stream E: operations/release
  - Added `docs/COMPATIBILITY.md`, `docs/OPERATIONS.md`, `docs/RELEASE.md`, `docs/PERFORMANCE.md`
  - Added `docs/ROBUSTNESS-CHECKLIST.md`
- Stream F: codex-native domain packs
  - Added `codex-backend-pack`, `codex-frontend-pack`, `codex-security-pack`, `codex-qa-pack`

## Phase 4 Validation Results (Executed)

Status: PASS

Evidence:

- `quick_validate.py` pass for all 5 skill folders.
- `python scripts/ci_validate_skill.py --skills-root skills` -> pass.
- `python -m unittest discover -s tests -p "test_*.py"` -> pass.
- `python skills/codex-workflows/scripts/check_workflow_parity.py ...` -> pass.
- `python skills/codex-workflows/scripts/check_compat_drift.py ... --source .agent` -> pass.
- `python skills/codex-workflows/scripts/benchmark_router.py --iterations 10000` -> speedup observed in current run (`~1.53x`).

## Phase 5 Summary (Executed)

- Added default bootstrap profile `codex-native`.
- Preserved `antigravity-compat` and `minimal` profiles.
- Implemented profile overlay logic so codex-native can evolve independently while keeping compatibility baseline.

## Phase 6 Summary (Executed)

- Rewrote codex-native workflow files for all commands:
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
- Added codex-native quality gate script:
  - `skills/codex-workflows/scripts/check_codex_native_quality.py`
- Added CI enforcement of codex-native quality:
  - `.github/workflows/ci.yml`
- Added dedicated tests:
  - `tests/test_codex_native_quality.py`
- Updated root docs and website docs (EN/PT/ES/FR/ZH) to reflect codex-native default and new quality checks.

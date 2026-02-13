# Tasks: Comparison Remediation (Codex vs Antigravity)

Date: 2026-02-13
Scope: close the gaps found in the latest robustness/professionalism/copy-risk comparison.

## Goals

- Keep `codex-workflows` robust and operationally complete.
- Make default experience clearly `codex-native`.
- Keep compatibility mode explicit and isolated.
- Reduce direct-copy risk in runtime workflow sources.
- Update docs and website only after all code/contract changes are complete.

## Stage 1: Workflow Contract Separation

Status: `completed`

Tasks:

- [x] Make `references/workflows/*.md` follow codex-native contracts (not compat contracts).
- [x] Keep compatibility parity only between:
  - `templates/.agent/workflows/*.md`
  - `packs/antigravity-compat/.agent/workflows/*.md`
- [x] Enforce native parity between:
  - `references/workflows/*.md`
  - `templates/codex-native/.agent/workflows/*.md`

Acceptance:

- `check_workflow_parity.py` passes with the new split contract.
- `references/workflows/*.md` are no longer identical to compatibility workflows.

## Stage 2: Copy-Risk Guardrails

Status: `completed`

Tasks:

- [x] Strengthen `check_codex_native_quality.py` to enforce a max similarity threshold versus compat workflows.
- [x] Add/adjust tests for the stricter quality gate.
- [x] Wire the stricter checks into CI and local unified CLIs.

Acceptance:

- CI/local validation fails if codex-native workflows drift too close to compatibility text.
- Unit tests cover the updated behavior.

## Stage 3: Packaging and Operations Alignment

Status: `completed`

Tasks:

- [x] Ensure operational commands and release checks reflect split contract and stricter native gate.
- [x] Ensure install/bootstrap defaults keep `codex-native` as first-class path and compatibility as opt-in.

Acceptance:

- `codexwf validate --tests` passes.
- `.github/workflows/ci.yml` uses updated checks and passes logically.

## Stage 4: Documentation and Website Final Sync (Last)

Status: `completed`

Tasks:

- [x] Update repository docs (`README.md`, `docs/*.md`) to describe new contract and anti-copy guardrails.
- [x] Keep compatibility wording explicit but non-dominant outside compatibility sections.
- [x] Sync website source docs to EN/PT/ES/FR/ZH after all adjustments.
- [x] Build website and verify docs parity.

Acceptance:

- `python scripts/codexwf.py docs-sync --build` passes.
- `python scripts/codexwf.py status --json` shows locale parity without missing pages.

## Stage 5: Final Validation and Evidence

Status: `completed`

Tasks:

- [x] Run end-to-end validation bundle.
- [x] Produce short evidence summary with file references and command results.

Acceptance:

- `python -m unittest discover -s tests -p "test_*.py"` passes.
- `python scripts/codexwf.py validate --tests --docs` passes.
- Final comparison no longer reports `references/workflows` as copy-equivalent to compat workflows.

## Evidence (2026-02-13)

- `python skills/codex-workflows/scripts/check_workflow_parity.py --references skills/codex-workflows/references/workflows --native skills/codex-workflows/templates/codex-native/.agent/workflows --template skills/codex-workflows/templates/.agent/workflows --pack skills/codex-workflows/packs/antigravity-compat/.agent/workflows` -> pass.
- `python skills/codex-workflows/scripts/check_codex_native_quality.py --native skills/codex-workflows/templates/codex-native/.agent/workflows --compat skills/codex-workflows/packs/antigravity-compat/.agent/workflows --max-similarity 0.35` -> pass.
- `python -m unittest discover -s tests -p "test_*.py"` -> pass (`29 tests`).
- `python scripts/codexwf.py validate --tests --docs` -> pass.
- Similarity audit (`references` vs `compat`): identical files `0`, max similarity `0.118106` (`brainstorm.md`).

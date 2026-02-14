# Profile: QA and Reliability Engineer

## Objective

Increase confidence quickly by targeting regressions, flaky areas, and release controls.

## 90-Minute Quick Win Plan

1. Failure analysis

`cw /debug analyze recurring defects and classify by root cause category.`

2. Test strategy update

`cw /test create a high-value test matrix for critical paths and known regressions.`

3. Release safety protocol

`cw /deploy define pre-release, canary, rollback, and post-release verification gates.`

4. Operational visibility

`cw /preview propose lightweight observability checks for release validation.`

## Deliverables Checklist

- defect taxonomy and root-cause summary;
- prioritized regression test matrix;
- release safety protocol;
- observability checks and ownership.

## Validation Commands

`python scripts/codexwf.py validate --tests`

`python skills/codex-workflows/scripts/check_codex_native_quality.py --native skills/codex-workflows/templates/codex-native/.agent/workflows --compat skills/codex-workflows/packs/antigravity-compat/.agent/workflows --max-similarity 0.35`

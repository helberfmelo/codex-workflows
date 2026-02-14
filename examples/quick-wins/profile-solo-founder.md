# Profile: Solo Founder

## Objective

Ship an MVP feature with acceptable reliability in one focused session.

## 90-Minute Quick Win Plan

1. Plan and scope in one pass

`cw /orchestrate design MVP scope, acceptance criteria, and release risk list for this feature.`

2. Build critical path only

`cw /create implement only the critical happy path plus required API/data model changes.`

3. Add minimal safety net

`cw /test add high-value tests for auth, billing, and failure-path basics.`

4. Prepare release checklist

`cw /deploy produce go/no-go checklist with rollback and monitoring actions.`

## Deliverables Checklist

- one-page execution plan;
- implemented feature on critical path;
- core tests for business risk areas;
- release checklist and rollback steps.

## Validation Commands

`python scripts/codexwf.py validate --tests`

`python scripts/codexwf.py status --json`

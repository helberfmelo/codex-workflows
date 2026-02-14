# Profile: Startup Product Team

## Objective

Coordinate product, backend, frontend, and QA to deliver one production-ready increment.

## 2-Hour Quick Win Plan

1. Cross-domain alignment

`cw /orchestrate decompose this feature into backend/frontend/qa/security tracks with phase gates.`

2. Backend implementation focus

`cw /create implement backend contracts and migrations for phase 1.`

3. Frontend integration and UX pass

`cw /enhance integrate frontend flow and apply usability fixes for the main user journey.`

4. Confidence gate

`cw /test generate contract and integration tests, then summarize release blockers.`

## Deliverables Checklist

- phased plan with owners and dependencies;
- backend contract and schema changes;
- frontend integration notes and UX deltas;
- blocker list with decision recommendations.

## Validation Commands

`python scripts/codexwf.py validate --tests`

`python skills/codex-node-validation-pack/scripts/validate_node_stack.py --project . --run`

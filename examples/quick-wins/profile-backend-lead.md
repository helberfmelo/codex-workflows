# Profile: Backend Team Lead

## Objective

Stabilize service architecture and quality gates for sustained team velocity.

## 120-Minute Quick Win Plan

1. Architecture and risk map

`cw /plan produce service boundaries, dependency map, and technical risk matrix.`

2. Hotspot hardening

`cw /debug investigate top 3 failure hotspots and propose deterministic remediations.`

3. Quality contract

`cw /test enforce coverage targets, integration tests, and lint/type policies.`

4. Delivery governance

`cw /status report what is green/yellow/red and list next execution wave.`

## Deliverables Checklist

- architecture map with risk ranking;
- remediation plan for top failures;
- test and policy gate definitions;
- execution dashboard with priorities.

## Validation Commands

`python scripts/codexwf.py validate --tests`

`python skills/codex-python-validation-pack/scripts/validate_python_stack.py --project . --run`

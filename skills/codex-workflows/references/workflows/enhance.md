---
description: Codex-native enhancement workflow for improving existing features without uncontrolled regressions.
---

# /enhance - Codex-Native Iteration Upgrade

$ARGUMENTS

---

## Objective

Improve existing behavior safely and measurably.

Use `/enhance` for:

- performance improvements;
- UX refinements;
- reliability hardening;
- incremental capability upgrades.

---

## Baseline First

Before changing code, capture:

1. current behavior snapshot;
2. known pain points;
3. baseline metrics (where applicable);
4. current test status.

Without baseline evidence, enhancement quality cannot be validated.

---

## Enhancement Flow

### Step 1: Target Definition

- define improvement goals;
- define non-goals;
- define measurable success signal.

### Step 2: Delta Plan

- list exact code areas to touch;
- list risk hotspots;
- define rollback approach.

### Step 3: Incremental Changes

- implement smallest high-value change first;
- re-check behavior after each increment.

### Step 4: Validation and Regression Guard

- run relevant tests/checks;
- add or update tests for changed behavior.

---

## Output Contract

```markdown
## Enhancement Report

### Baseline
- Current behavior: ...
- Baseline metric(s): ...

### Improvement Target
- Goal: ...
- Success signal: ...

### Changes Applied
- `path/to/file`: [what changed]

### Validation
- `[command]` -> [pass|fail]

### Regression Guard
- [test/check added or updated]

### Result
- Target achieved: [yes|partial|no]
- Follow-up: [next action]
```

---

## Quality Bar

Before closing:

- baseline evidence present;
- improvement target measurable;
- regression guard documented;
- impact and residual risk stated.


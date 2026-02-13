---
description: Codex-native deployment workflow for release readiness, controlled rollout, and rollback safety.
---

# /deploy - Codex-Native Release Control

$ARGUMENTS

---

## Objective

Ship changes with operational safety and traceable verification.

Use `/deploy` for:

- release candidate validation;
- production or staging rollout preparation;
- deployment incident prevention.

---

## Pre-Deploy Checklist

Required before rollout:

1. latest tests pass;
2. critical lint/type/security checks pass;
3. release notes/changelog updated;
4. rollback path documented;
5. environment config reviewed.

If any critical check fails, deployment is blocked.

---

## Rollout Strategy

Select one strategy and justify:

- full rollout;
- canary;
- phased rollout by environment or traffic slice.

For risky changes, default to canary or phased rollout.

---

## Verification Windows

Define:

1. immediate checks (0-15 min);
2. short window checks (15-60 min);
3. post-release checks (same day).

Each window must have measurable success and alert thresholds.

---

## Output Contract

```markdown
## Deploy Report

### Release Scope
[what is being released]

### Pre-Deploy Status
- Tests: [pass|fail]
- Lint/Type/Security: [pass|fail]
- Changelog/Notes: [ready|missing]
- Rollback Plan: [ready|missing]

### Rollout Strategy
- Strategy: [full|canary|phased]
- Reason: ...

### Validation Windows
- 0-15 min: ...
- 15-60 min: ...
- same day: ...

### Commands and Evidence
- `[command]` -> [pass|fail]

### Go/No-Go
- Decision: [go|no-go]
- Blocking factors: [...]
```

---

## Quality Bar

Before closing:

- explicit go/no-go decision;
- rollback path visible;
- verification windows defined;
- evidence commands included.


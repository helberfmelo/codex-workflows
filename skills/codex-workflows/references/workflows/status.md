---
description: Codex-native status workflow for producing a clear delivery snapshot with progress, risks, and next steps.
---

# /status - Codex-Native Delivery Snapshot

$ARGUMENTS

---

## Objective

Provide a decision-ready view of current project state.

Use `/status` for:

- sprint or milestone checkpoints;
- release readiness checks;
- stakeholder updates.

---

## Required Inputs

Collect:

1. current objective(s);
2. completed work evidence;
3. pending work;
4. blockers and risks;
5. verification state.

If evidence is missing, mark the item as unverified.

---

## Reporting Dimensions

Report status by:

- scope progress (`done|in-progress|blocked`);
- quality signal (tests/checks);
- risk level (`low|medium|high`);
- timeline confidence (`high|medium|low`).

---

## Output Contract

```markdown
## Status Report

### Objective
[current delivery objective]

### Progress
- Done: [...]
- In progress: [...]
- Blocked: [...]

### Verification State
- `[command]` -> [pass|fail|not run]

### Risks
- [risk]: [impact] / [mitigation]

### Timeline Confidence
- Confidence: [high|medium|low]
- Reason: ...

### Next 3 Actions
1. ...
2. ...
3. ...
```

---

## Quality Bar

Before closing:

- progress statements backed by evidence;
- blockers are explicit;
- next actions are concrete and ordered.


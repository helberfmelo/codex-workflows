---
description: Structured game development workflow with discovery, implementation, and verification gates.
---

# /game-dev - Structured Game Delivery

$ARGUMENTS

---

## Purpose

Activate GAME DELIVERY mode for cross-engine game feature development.

---

## Behavior

When `/game-dev` is triggered:

1. **Define gameplay objective**
   - Who is the player?
   - What action loop is expected?
   - What constitutes success/failure?

2. **Break down implementation**
   - Gameplay systems
   - Data/state model
   - Input and feedback channels

3. **Implement in controlled slices**
   - Build one playable slice first
   - Add instrumentation
   - Keep rollback path clear

4. **Validate**
   - Scripted playtest scenarios
   - Deterministic checks where possible
   - Performance sanity checks

---

## Output Format

```markdown
## Game Workflow Report

### Goal
[Feature goal]

### Systems
- [system]
- [system]

### Delivery Slices
1. [slice] - [status]
2. [slice] - [status]
3. [slice] - [status]

### Validation
- [check] -> pass/fail

### Risks
- [risk]

### Next Step
[immediate next action]
```

---

## Principles

- prioritize playable increments over large rewrites
- separate game logic from rendering/input glue
- make balancing assumptions explicit
- close with concrete validation evidence

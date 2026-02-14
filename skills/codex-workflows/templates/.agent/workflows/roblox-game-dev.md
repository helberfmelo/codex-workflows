---
description: Structured Roblox workflow for Luau implementation, secure remotes, and release readiness.
---

# /roblox-game-dev - Structured Roblox Delivery

$ARGUMENTS

---

## Purpose

Activate ROBLOX DELIVERY mode for Roblox Studio projects.

---

## Behavior

When `/roblox-game-dev` is triggered:

1. **Establish boundaries**
   - What is server-only?
   - What is client-visible?
   - Which remotes are required?

2. **Implement feature slice**
   - Create one end-to-end scenario
   - Centralize shared Luau modules
   - Validate inputs at remote boundaries

3. **Harden persistence**
   - DataStore retries and fallback
   - Server-side economy rules
   - Abuse-path checks

4. **Run publish gate**
   - Studio simulation checks
   - Warnings/errors review
   - Rollback and hotfix notes

---

## Output Format

```markdown
## Roblox Workflow Report

### Scope
[feature scope]

### Boundary Decisions
- server-only: [items]
- remotes: [items]

### Delivery Steps
1. [step] - [status]
2. [step] - [status]
3. [step] - [status]
4. [step] - [status]

### Validation
- [studio check] -> pass/fail

### Risks
- [risk]

### Next Step
[immediate next action]
```

---

## Principles

- keep authoritative state on server
- harden all remote inputs
- treat DataStore limits as design constraints
- do not close without validation evidence

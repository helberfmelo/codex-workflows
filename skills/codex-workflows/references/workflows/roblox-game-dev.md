---
description: Codex-native workflow for Roblox game development with Luau architecture, secure remotes, and publish readiness checks.
---

# /roblox-game-dev - Codex-Native Roblox Delivery

$ARGUMENTS

---

## Objective

Build and ship Roblox features with secure client/server boundaries and platform-compliant operation.

Use this workflow for:

- Roblox Studio game features;
- Luau service/module architecture;
- DataStore-backed progression and economy;
- exploit-hardening and publish readiness.

---

## Roblox Scope Inputs

Confirm these inputs before coding:

1. game mode and target session length;
2. trust model (server-authoritative rules);
3. remote communication map (RemoteEvent/RemoteFunction);
4. persistence design (DataStore keys, retry/backoff);
5. moderation/safety constraints and release target.

If trust boundaries are unclear, stop and route to `/plan`.

---

## Roblox Build Protocol

### Phase 1: Architecture and Boundaries

- map scripts/services by runtime context;
- define what never runs on client;
- document replication decisions.

### Phase 2: Feature Slice in Luau

- implement one vertical feature slice;
- isolate shared modules for deterministic behavior;
- protect remotes with strict input validation.

### Phase 3: Persistence and Abuse Hardening

- implement DataStore error handling and fallback behavior;
- validate currency/progression mutation rules on server only;
- test exploit-prone paths with adversarial scenarios.

### Phase 4: Studio Validation and Publish Gate

- run Studio test matrix (solo/server-client simulation);
- verify telemetry and runtime warnings;
- prepare release notes and rollback plan.

---

## Output Contract

```markdown
## Roblox Dev Report

### Feature Scope
[feature delivered]

### Trust Boundary Decisions
- server authoritative rules: [listed]
- remote hardening status: [done|partial]

### Phase Results
1. Architecture/Boundaries: [done|partial]
2. Feature Slice: [done|partial]
3. Persistence/Hardening: [done|partial]
4. Validation/Publish Gate: [done|partial]

### Files Changed
- `path/to/file`: [purpose]

### Validation Evidence
- `[studio test command or checklist]` -> [pass|fail]

### Open Risks
- [risk]

### Next Action
[single immediate next step]
```

---

## Quality Bar

Before closing:

- server/client trust boundaries are explicit;
- remotes and DataStore flows include failure handling;
- exploit-sensitive paths are validated;
- publish gate evidence is present.

---
description: Codex-native workflow for general game development with systems-first slicing and iterative playability validation.
---

# /game-dev - Codex-Native Game Delivery

$ARGUMENTS

---

## Objective

Deliver game features safely and incrementally, preserving playability and technical stability.

Use this workflow for:

- game prototypes and vertical slices;
- gameplay systems (combat, movement, progression, inventory);
- balancing and optimization passes;
- platform-agnostic game architecture work.

---

## Game Delivery Inputs

Before implementation, confirm:

1. target genre and player fantasy;
2. core loop definition (30-60 second cycle);
3. win/loss or progression conditions;
4. engine/runtime constraints;
5. validation approach (playtest script, simulation, deterministic tests).

If core loop or success criteria are missing, route to `/plan` first.

---

## Development Loop

### Phase 1: Systems Blueprint

- map entities, state machines, and event flows;
- define authoritative state boundaries;
- identify save/progression contracts.

### Phase 2: Playable Increment

- implement one playable scenario end-to-end;
- keep diffs scoped to one system slice at a time;
- expose instrumentation hooks for balancing.

### Phase 3: Balance and Performance Pass

- tune numeric parameters with explicit baselines;
- check frame-time and memory pressure hotspots;
- validate input responsiveness and failure handling.

### Phase 4: Validation and Handoff

- execute deterministic checks and scripted playtest steps;
- record reproducible findings;
- capture known limitations and next iteration target.

---

## Output Contract

```markdown
## Game Dev Report

### Scope
[game system or feature delivered]

### Core Loop Alignment
- loop definition: [confirmed|partial]
- progression signal: [confirmed|partial]

### Implementation Slices
1. Systems Blueprint: [done|partial]
2. Playable Increment: [done|partial]
3. Balance/Performance: [done|partial]
4. Validation/Handoff: [done|partial]

### Files Changed
- `path/to/file`: [purpose]

### Validation Evidence
- `[command or playtest script]` -> [pass|fail]

### Risks
- [risk]

### Next Action
[single immediate next step]
```

---

## Quality Bar

Before closing:

- one playable increment is demonstrated;
- loop and progression assumptions are explicit;
- performance-sensitive changes are acknowledged;
- validation evidence is concrete (not hypothetical).

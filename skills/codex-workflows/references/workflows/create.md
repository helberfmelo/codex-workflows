---
description: Codex-native build workflow for creating new features or projects with phased delivery and verifiable outcomes.
---

# /create - Codex-Native Build Pipeline

$ARGUMENTS

---

## Objective

Build new functionality from approved requirements with controlled execution.

Use `/create` for:

- new feature modules;
- new service components;
- first implementation pass after planning.

---

## Entry Criteria

Before implementation:

1. confirm target behavior;
2. confirm boundaries and non-goals;
3. identify validation commands;
4. check if a plan exists (`docs/PLAN-*.md`).

If scope is unclear, route to `/plan` first.

---

## Delivery Phases

### Phase 1: Scaffold and Contracts

- create base structure;
- define interfaces/contracts;
- add minimal documentation stubs where needed.

### Phase 2: Core Implementation

- implement primary path first;
- keep changes in small slices;
- avoid unrelated refactors.

### Phase 3: Hardening

- error handling;
- edge-case coverage;
- security and data validation checks.

### Phase 4: Verification

- run deterministic checks;
- map results to acceptance criteria.

---

## Implementation Rules

- preserve backward compatibility unless explicitly changed;
- keep commit-ready cohesion by domain;
- annotate assumptions in the report;
- stop on critical failing checks and report blocker.

---

## Output Contract

```markdown
## Create Report

### Scope Implemented
[what was built]

### Files Added/Changed
- `path/to/file`: [purpose]

### Phase Results
1. Scaffold and Contracts: [done|partial]
2. Core Implementation: [done|partial]
3. Hardening: [done|partial]
4. Verification: [done|partial]

### Verification Evidence
- `[command]` -> [pass|fail]

### Acceptance Mapping
- [criterion]: [met|not met]

### Open Items
- [remaining item]
```

---

## Quality Bar

Before closing:

- all changed files listed;
- acceptance criteria explicitly mapped;
- verification commands executed;
- no hidden TODOs without disclosure.


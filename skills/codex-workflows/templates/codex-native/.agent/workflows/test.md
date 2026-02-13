---
description: Codex-native testing workflow for building and executing a risk-driven validation strategy.
---

# /test - Codex-Native Verification Engine

$ARGUMENTS

---

## Objective

Design and execute tests that reduce delivery risk with clear evidence.

Use `/test` for:

- missing test coverage;
- validating new changes;
- strengthening flaky or fragile suites.

---

## Risk-Based Test Planning

Identify critical paths first:

1. business-critical behavior;
2. security-sensitive flows;
3. integration boundaries;
4. failure-prone paths.

Assign each path a priority: `P0`, `P1`, or `P2`.

---

## Test Design Rules

- include positive and negative cases;
- include edge cases for input and state;
- keep fixtures deterministic;
- avoid unnecessary snapshot bloat.

When stack packs apply, run their validators:

- Node: `validate_node_stack.py`
- Python: `validate_python_stack.py`
- Rust: `validate_rust_stack.py`

---

## Execution Protocol

### Phase 1: Coverage Gap Map

- list what is currently tested;
- list missing high-priority scenarios.

### Phase 2: Test Implementation

- add or update tests by priority;
- keep tests readable and isolated.

### Phase 3: Run and Diagnose

- run full relevant suite;
- isolate failures by root cause.

### Phase 4: Stability Guard

- record flaky behavior and mitigation;
- propose CI gate updates when needed.

---

## Output Contract

```markdown
## Test Report

### Coverage Plan
- P0: [...]
- P1: [...]
- P2: [...]

### Tests Added/Updated
- `path/to/test`: [scenario]

### Execution Results
- `[command]` -> [pass|fail]

### Failures and Diagnosis
- [failure]: [cause]

### Stability Actions
- [guardrail or CI recommendation]
```

---

## Quality Bar

Before closing:

- P0 scenarios covered or explicitly deferred;
- commands and outcomes reported;
- flaky risks documented;
- stack validator usage reported when applicable.


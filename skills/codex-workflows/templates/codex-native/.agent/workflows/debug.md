---
description: Codex-native debugging workflow with hypothesis tracking, deterministic checks, and root-cause closure.
---

# /debug - Codex-Native Incident Investigation

$ARGUMENTS

---

## Objective

Resolve failures through evidence, not guesswork.

Use this workflow for:

- runtime errors;
- failing tests with unclear cause;
- regressions after recent changes;
- production incidents requiring safe remediation.

---

## Investigation Protocol

### Step 1: Symptom Capture

Record:

1. observed behavior;
2. expected behavior;
3. where it occurs (environment, endpoint, command, screen);
4. first known bad point in time (if known).

If reproduction is unclear, stop and collect reproducible steps first.

---

### Step 2: Evidence Collection

Collect concrete evidence before proposing fixes:

- stack traces and logs;
- failing command output;
- touched files and recent diffs;
- environment variables and configuration deltas.

Do not hide missing evidence. Mark unknowns explicitly.

---

### Step 3: Hypothesis Backlog

Create at least 3 ranked hypotheses:

1. most likely;
2. plausible alternative;
3. edge-condition possibility.

For each hypothesis define:

- validation step;
- expected observation if true;
- next move if false.

---

### Step 4: Deterministic Validation

Test hypotheses one by one.

Rules:

- change one variable at a time;
- log pass/fail per test step;
- eliminate disproven hypotheses explicitly.

If all hypotheses fail, generate a new set based on new evidence and continue.

---

### Step 5: Fix, Guardrail, Verification

After root cause is confirmed:

1. apply the minimal safe fix;
2. add guardrail:
- test
- assertion
- lint/type rule
- monitoring alert
3. re-run relevant checks and show results.

---

## Root Cause Closure Criteria

Only mark as resolved when all are true:

- root cause is clearly stated;
- fix is linked to root cause;
- regression guardrail added or justified;
- verification commands pass.

---

## Output Contract

Return:

```markdown
## Debug Report

### Symptom
[what is broken]

### Reproduction
1. [step]
2. [step]
3. [step]

### Evidence
- [log/trace/command result]

### Hypotheses
1. [hypothesis] - [status: confirmed|rejected]
2. [hypothesis] - [status: confirmed|rejected]
3. [hypothesis] - [status: confirmed|rejected]

### Root Cause
[single precise cause statement]

### Fix Applied
- `path/to/file`: [change summary]

### Guardrail
- [test/assertion/check added]

### Verification
- `[command]` -> [pass|fail]

### Residual Risk
- [risk or "none identified"]
```

---

## Usage Examples

```text
/debug login endpoint returns 500 on valid credentials
/debug flaky ci failure in python type checks
/debug rust binary panics when config file is missing
```


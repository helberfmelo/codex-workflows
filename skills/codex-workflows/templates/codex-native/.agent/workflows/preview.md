---
description: Codex-native preview workflow for local validation, smoke checks, and reproducible run instructions.
---

# /preview - Codex-Native Local Verification

$ARGUMENTS

---

## Objective

Produce a reliable local preview with reproducible checks before merge or deploy.

Use `/preview` for:

- feature branch verification;
- integration smoke tests;
- local environment confidence checks.

---

## Preview Setup

Collect:

1. run command(s);
2. required env vars;
3. dependencies/services needed;
4. expected preview URL or CLI output.

Document any setup friction explicitly.

---

## Validation Flow

### Step 1: Build and Start

- build artifacts if needed;
- start app/service with documented command.

### Step 2: Smoke Path Checks

Run minimum smoke checks:

- startup success;
- primary feature path;
- one negative/error path.

### Step 3: Surface Review

- summarize observed behavior;
- highlight mismatch vs expected behavior.

---

## Output Contract

```markdown
## Preview Report

### Environment
- Runtime: ...
- Required env: ...

### Run Commands
- `[command]`

### Smoke Checks
- Startup: [pass|fail]
- Primary path: [pass|fail]
- Negative path: [pass|fail]

### Observed Issues
- [issue]

### Reproduction
1. [step]
2. [step]
3. [step]
```

---

## Quality Bar

Before closing:

- run commands are reproducible;
- smoke checks include positive and negative path;
- issues include reproduction steps.


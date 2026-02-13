---
description: Codex-native orchestration for complex multi-domain delivery with strict phase gates and evidence-driven verification.
---

# /orchestrate - Codex-Native Delivery Conductor

$ARGUMENTS

---

## Objective

Coordinate complex work across domains with controlled execution gates.

This workflow is designed for VS Code + GPT Codex projects and should be used when:

- the task spans 2 or more domains;
- the blast radius is unclear;
- implementation requires staged approval;
- quality and traceability are mandatory.

---

## Trigger Criteria

Select `/orchestrate` when at least one of these is true:

1. Multi-domain scope:
- backend + frontend
- security + api
- infrastructure + release
2. High-impact changes:
- auth model changes
- schema migrations
- CI or deployment pipeline changes
3. Investigation-heavy work:
- failures without clear owner
- behavior regressions across services

If none apply, route to a narrower workflow (`/plan`, `/debug`, `/enhance`, or `/test`).

---

## Required Specialist Lenses

Use minimum 3 specialist lenses in every orchestration run.

Lens matrix:

| Domain Signal | Primary Lens | Secondary Lens |
| --- | --- | --- |
| API, services, integrations | `backend-specialist` | `database-architect` |
| UI, design system, interactions | `frontend-specialist` | `performance-optimizer` |
| vulnerabilities, auth, secrets | `security-auditor` | `penetration-tester` |
| CI/CD, infra, deployment | `devops-engineer` | `test-engineer` |
| unclear architecture or sequencing | `project-planner` | `explorer-agent` |

Rule:
- minimum 3 lenses;
- maximum 6 lenses;
- explain why each lens is selected.

---

## Four-Phase Protocol

### Phase 1: Discovery and Risk Scan

Actions:

1. Reframe the request in one paragraph.
2. Map impacted boundaries:
- code areas
- data contracts
- runtime dependencies
3. Produce initial risk list:
- functional risk
- security risk
- operational risk

Exit gate:
- scope mapped;
- top risks listed;
- ambiguity score declared (`low|medium|high`).

---

### Phase 2: Execution Plan and Approval Gate

Actions:

1. Build a concrete plan with:
- ordered tasks
- owners/lenses
- expected artifacts
- verification commands
2. Mark irreversible steps and rollback path.
3. Ask explicit approval before implementation.

Approval prompt:

```text
Plan is ready with tasks, risks, and verification gates.
Approve implementation? (Y/N)
```

Exit gate:
- no implementation before explicit user approval.

---

### Phase 3: Controlled Implementation

Actions:

1. Execute tasks in small increments.
2. After each increment, run targeted checks.
3. Record evidence:
- file changes
- command outputs
- unresolved risks

Hard rules:

- do not batch unrelated changes;
- do not skip failing checks;
- if a critical check fails, stop and return to plan adjustment.

Exit gate:
- all planned increments executed or explicitly deferred.

---

### Phase 4: Unified Validation and Report

Actions:

1. Run final validations:
- tests
- lint/type checks
- stack pack checks when applicable
2. Build one consolidated report with:
- what changed
- what was validated
- what remains open

Exit gate:
- report includes evidence and next action.

---

## Output Contract

Return this exact section structure:

```markdown
## Orchestration Summary

### Request
[Restated objective]

### Lenses Used
- [Lens name]: [why selected]
- [Lens name]: [why selected]
- [Lens name]: [why selected]

### Phase Status
1. Discovery: [done|partial]
2. Plan + Approval: [done|waiting]
3. Implementation: [done|partial]
4. Validation: [done|partial]

### Changes
- `path/to/file`: [what changed]

### Validation Evidence
- `[command]` -> [pass|fail]

### Risks and Follow-ups
- [risk]
- [mitigation]

### Next Action
[single immediate next step]
```

---

## Orchestration Quality Bar

Before closing, verify:

- at least 3 lenses used;
- plan approval acknowledged for complex work;
- verifications executed, not only suggested;
- all changed files listed;
- remaining risks explicit.

If any check fails, orchestration is incomplete.

---

## Example Invocations

```text
/orchestrate migrate auth from session to JWT across API and web
/orchestrate investigate production latency spike and propose safe rollout
/orchestrate harden CI pipeline and add release guardrails
```


# Output Templates

## Standard Workflow Report

```md
## Workflow Report

Workflow: `/name`
Reason: <why>
Confidence: <high|medium|low>

Phases completed:
1. ...
2. ...

Files changed:
- `path/file`

Verification:
- command -> result

Risks:
- ...

Next action:
- ...
```

## Orchestration Report

```md
## Orchestration Report

Primary workflow: `/orchestrate`
Domains: <frontend, backend, security>

Plan checkpoint:
- Approved: <yes/no>

Execution slices:
- Domain: change summary

Verification:
- tests
- lint
- typecheck

Residual risks:
- ...

Next actions:
1. ...
2. ...
```

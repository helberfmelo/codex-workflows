# Workflows

Supported catalog:

- `/brainstorm`
- `/plan`
- `/create`
- `/enhance`
- `/debug`
- `/test`
- `/deploy`
- `/preview`
- `/status`
- `/orchestrate`
- `/ui-ux-pro-max`

## Recommended prompt pattern

For deterministic behavior, always use explicit skill + workflow:

- `Use codex-workflows in /<workflow> and <goal>`
- `Use codex-workflows in /<workflow> and <objective>`

## Routing rules

- explicit activation has priority;
- multi-domain requests tend to `/orchestrate`;
- ambiguous requests default to `/plan`.

Reference files:

- `skills/codex-workflows/scripts/route_workflow.py`
- `skills/codex-workflows/scripts/route_workflow_fast.py`
- `skills/codex-workflows/references/workflow-playbook.md`

# Architecture

## Goal

Provide a workflow operating system for GPT Codex in VS Code with:

- intent routing
- phase-based execution
- orchestration gates
- reusable local project templates

## Layers

1. Skill Core
- `skills/codex-workflows/SKILL.md`
- Activation and top-level execution contract

2. Routing and Governance
- `references/routing/intent-matrix.md`
- `references/orchestration/phase-gates.md`

3. Workflow Knowledge Base
- `references/workflows/*.md`
- `references/templates/output-templates.md`

4. Automation Scripts
- `scripts/route_workflow.py`
- `scripts/bootstrap_project_agent.py`

5. Project Template
- `templates/.agent/...`
- Bootstraps local workflow files for projects without `.agent`

## Execution Model

User request -> route workflow -> run phases -> validate -> report

For complex tasks:

User request -> /orchestrate -> discovery -> planning gate -> implementation -> verification -> synthesis

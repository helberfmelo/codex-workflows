# Workflows

Catalogo suportado:

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

## Recomendacao de uso

Para maior previsibilidade, sempre explicite skill + workflow:

- `Use codex-workflows in /<workflow> and <goal>`
- `Use codex-workflows em /<workflow> e <objetivo>`

## Regras de roteamento

- modo explicito tem prioridade;
- tarefas multi-dominio tendem a `/orchestrate`;
- quando ambiguo, tende a `/plan`.

Arquivos de referencia:

- `skills/codex-workflows/scripts/route_workflow.py`
- `skills/codex-workflows/scripts/route_workflow_fast.py`
- `skills/codex-workflows/references/workflow-playbook.md`

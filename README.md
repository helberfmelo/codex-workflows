# Codex Workflows Skill

Workflow operating system for GPT Codex in VS Code.

It routes natural-language requests into repeatable execution workflows:

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

## Positioning

This project is inspired by Antigravity Kit patterns and adapted to Codex skill format for VS Code.

- Designed for GPT Codex skill loading and routing
- Not a fork of Antigravity Kit
- Not affiliated with the Antigravity IDE

## What Is Included

```text
skills/
  codex-workflows/
    SKILL.md
    agents/openai.yaml
    scripts/
      route_workflow.py
      bootstrap_project_agent.py
    references/
      workflow-playbook.md
      workflows/*.md
      routing/intent-matrix.md
      orchestration/phase-gates.md
      templates/output-templates.md
    templates/.agent/
      ARCHITECTURE.md
      rules/CODEX.md
      workflows/*.md
      scripts/auto_preview.py
```

## Installation

### Option 1: Install from GitHub URL (recommended)

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --url https://github.com/helberfmelo/codex-workflows/tree/main/skills/codex-workflows
```

Windows (PowerShell):

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" `
  --url "https://github.com/helberfmelo/codex-workflows/tree/main/skills/codex-workflows"
```

### Option 2: Install by repo and path

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo helberfmelo/codex-workflows \
  --path skills/codex-workflows
```

## Quick Start

1. Restart Codex after installation.
2. Prompt with workflow intent, for example:
- `Use codex-workflows and run /orchestrate for this feature`
- `Apply /debug workflow for this failing test`
3. Optional: bootstrap local `.agent` in any project:

```bash
python ~/.codex/skills/codex-workflows/scripts/bootstrap_project_agent.py --project .
```

4. Optional: classify request intent deterministically:

```bash
python ~/.codex/skills/codex-workflows/scripts/route_workflow.py "add secure login with tests" --json
```

## Behavior Notes

- Slash-like terms (for example `/orchestrate`) are interpreted as workflow intent in prompts.
- They are not native Codex CLI slash commands.
- If a project has local `.agent` files, local instructions have priority.

## Comparison to Antigravity

See `docs/COMPARISON.md` for a detailed comparison and adaptation strategy.

## Contributing

See `CONTRIBUTING.md`.

## Changelog

See `CHANGELOG.md`.

## Compatibility

- GPT Codex with skills support
- VS Code Codex workflow
- Windows, macOS, Linux

## License

MIT

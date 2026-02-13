# Codex Workflows Skill

Workflow router skill for GPT Codex in VS Code.

It maps natural-language requests to workflow-style execution patterns:

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

The skill is inspired by Antigravity Kit workflow concepts and adapted to Codex skill format.

## Repository Structure

```text
skills/
  codex-workflows/
    SKILL.md
    agents/openai.yaml
    references/workflow-playbook.md
```

## Installation

### Option 1: Install from GitHub URL (recommended)

Use Codex `skill-installer`:

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

### Option 3: Manual install

Copy `skills/codex-workflows` to:

- macOS/Linux: `~/.codex/skills/codex-workflows`
- Windows: `%USERPROFILE%\.codex\skills\codex-workflows`

Then restart Codex.

## Usage

After restart, use prompts such as:

- `Use codex-workflows to run /plan for this feature`
- `/orchestrate implement secure login with tests`
- `Apply /debug workflow to this error`
- `Apply /deploy workflow with pre-flight checks`

## Behavior Notes

- Slash-like terms (for example `/orchestrate`) are interpreted as workflow intent in prompts.
- They are not native CLI slash commands in Codex.
- The skill prioritizes local `.agent/workflows` files when present.

## Compatibility

- GPT Codex with skill support
- VS Code Codex workflow
- Windows, macOS, Linux

## License

MIT

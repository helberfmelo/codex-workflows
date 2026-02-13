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
      route_workflow_fast.py
      routing_data.py
      bootstrap_project_agent.py
      sync_compat_pack.py
      build_compat_manifest.py
      check_compat_drift.py
      check_workflow_parity.py
      benchmark_router.py
      codex_workflows_ops.py
    compat/
      manifest.json
    packs/
      antigravity-compat/.agent/** (full compatibility pack)
    references/
      workflow-playbook.md
      workflows/*.md
      routing/intent-matrix.md
      orchestration/phase-gates.md
      templates/output-templates.md
    templates/.agent/** (full template baseline)
    templates/minimal/.agent/** (lightweight starter)
  codex-backend-pack/
  codex-frontend-pack/
  codex-security-pack/
  codex-qa-pack/
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
python ~/.codex/skills/codex-workflows/scripts/bootstrap_project_agent.py --project . --profile antigravity-compat
```

Minimal profile:

```bash
python ~/.codex/skills/codex-workflows/scripts/bootstrap_project_agent.py --project . --profile minimal
```

4. Optional: classify request intent deterministically:

```bash
python ~/.codex/skills/codex-workflows/scripts/route_workflow.py "add secure login with tests" --json
```

5. Optional: refresh compatibility pack from a local Antigravity `.agent` source:

```bash
python ~/.codex/skills/codex-workflows/scripts/sync_compat_pack.py --source /path/to/.agent
```

6. Validate compatibility and workflow parity:

```bash
python ~/.codex/skills/codex-workflows/scripts/check_workflow_parity.py \
  --references ~/.codex/skills/codex-workflows/references/workflows \
  --template ~/.codex/skills/codex-workflows/templates/.agent/workflows \
  --pack ~/.codex/skills/codex-workflows/packs/antigravity-compat/.agent/workflows
```

```bash
python ~/.codex/skills/codex-workflows/scripts/check_compat_drift.py \
  --manifest ~/.codex/skills/codex-workflows/compat/manifest.json \
  --pack ~/.codex/skills/codex-workflows/packs/antigravity-compat/.agent \
  --template-full ~/.codex/skills/codex-workflows/templates/.agent
```

7. Benchmark routing runtime:

```bash
python ~/.codex/skills/codex-workflows/scripts/benchmark_router.py --iterations 10000
```

## Behavior Notes

- Slash-like terms (for example `/orchestrate`) are interpreted as workflow intent in prompts.
- They are not native Codex CLI slash commands.
- If a project has local `.agent` files, local instructions have priority.

## Comparison to Antigravity

See `docs/COMPARISON.md` for a detailed comparison and adaptation strategy.

## Compatibility Scope

This repository includes a full compatibility pack under `skills/codex-workflows/packs/antigravity-compat/.agent` copied from a local Antigravity installation baseline to enable near-equivalent structure and workflows in Codex projects.

## Domain Packs

Independent packs are available for targeted installation:

- `skills/codex-backend-pack`
- `skills/codex-frontend-pack`
- `skills/codex-security-pack`
- `skills/codex-qa-pack`

The routers also return `recommended_packs` based on detected domains.

## CI and Quality Gates

- CI pipeline: `.github/workflows/ci.yml`
- Skill validation: `scripts/ci_validate_skill.py`
- Unit tests: `tests/test_*.py`

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

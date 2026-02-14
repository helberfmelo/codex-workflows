# Codex Workflows Skill

[![Docs](https://img.shields.io/badge/docs-live-0f5f87?logo=githubpages&logoColor=white)](https://helberfmelo.github.io/codex-workflows/)
[![Release](https://img.shields.io/github/v/release/helberfmelo/codex-workflows)](https://github.com/helberfmelo/codex-workflows/releases)

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

This project applies workflow-operating-system patterns to the Codex skill format for VS Code.

- Designed for GPT Codex skill loading and routing
- Independent repository and implementation

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
      check_codex_native_quality.py
      check_codex_native_assets.py
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
    templates/codex-native/.agent/** (default codex-native profile with native agents and skills)
    templates/.agent/** (full template baseline)
    templates/minimal/.agent/** (lightweight starter)
  codex-backend-pack/
  codex-frontend-pack/
  codex-security-pack/
  codex-qa-pack/
  codex-node-validation-pack/
  codex-python-validation-pack/
  codex-rust-validation-pack/
scripts/
  codexwf.py
  release_automation.py
  install_all_in_one.py
examples/
  node-auth-api/
  python-fastapi-orders/
  rust-events-cli/
  projects/
    node-service/
    python-service/
    rust-service/
website/
  docs/
  .vitepress/
  scripts/sync_reference_docs.py
```

## Installation

### Option 1: All-in-one install (recommended)

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo helberfmelo/codex-workflows \
  --path \
    skills/codex-workflows \
    skills/codex-backend-pack \
    skills/codex-frontend-pack \
    skills/codex-security-pack \
    skills/codex-qa-pack \
    skills/codex-node-validation-pack \
    skills/codex-python-validation-pack \
    skills/codex-rust-validation-pack
```

Windows (PowerShell):

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" `
  --repo "helberfmelo/codex-workflows" `
  --path `
    "skills/codex-workflows" `
    "skills/codex-backend-pack" `
    "skills/codex-frontend-pack" `
    "skills/codex-security-pack" `
    "skills/codex-qa-pack" `
    "skills/codex-node-validation-pack" `
    "skills/codex-python-validation-pack" `
    "skills/codex-rust-validation-pack"
```

This installs the orchestration core plus all domain and stack packs in one command.

### Option 2: All-in-one helper script from this repository

```bash
python scripts/install_all_in_one.py
```

Unified CLI alternative:

```bash
python scripts/codexwf.py install
```

The helper script:

- auto-detects `CODEX_HOME` (or `~/.codex`)
- skips already-installed skills safely
- installs only missing packs

Dry run:

```bash
python scripts/install_all_in_one.py --dry-run
```

Install from a specific tag/ref:

```bash
python scripts/install_all_in_one.py --ref v1.1.0
```

### Option 3: Install only the core skill (minimal)

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo helberfmelo/codex-workflows \
  --path skills/codex-workflows
```

### Option 4: Composer wrapper (PHP teams, optional)

Composer wrappers call the same official Codex Python installer.

Install all packs:

```bash
composer codex:install-all
```

Install only core:

```bash
composer codex:install-core
```

Install from a specific tag/ref:

```bash
composer codex:install-all -- --ref=v1.1.0
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

This default profile is `codex-native` and uses an independent codex-native `.agent` template with:

- 11 rewritten workflow contracts (`/brainstorm` to `/ui-ux-pro-max`)
- native `agents/` capability catalog
- native `skills/` capability catalog

Equivalent via unified CLI (inside this repository):

```bash
python scripts/codexwf.py init --project .
```

Compatibility profile:

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

5. Optional: refresh compatibility pack from a local `.agent` compatibility source:

```bash
python ~/.codex/skills/codex-workflows/scripts/sync_compat_pack.py --source /path/to/.agent
```

6. Validate compatibility and workflow parity:

```bash
python ~/.codex/skills/codex-workflows/scripts/check_workflow_parity.py \
  --references ~/.codex/skills/codex-workflows/references/workflows \
  --native ~/.codex/skills/codex-workflows/templates/codex-native/.agent/workflows \
  --template ~/.codex/skills/codex-workflows/templates/.agent/workflows \
  --pack ~/.codex/skills/codex-workflows/packs/antigravity-compat/.agent/workflows
```

```bash
python ~/.codex/skills/codex-workflows/scripts/check_compat_drift.py \
  --manifest ~/.codex/skills/codex-workflows/compat/manifest.json \
  --pack ~/.codex/skills/codex-workflows/packs/antigravity-compat/.agent \
  --template-full ~/.codex/skills/codex-workflows/templates/.agent
```

7. Validate codex-native workflow quality:

```bash
python ~/.codex/skills/codex-workflows/scripts/check_codex_native_quality.py \
  --native ~/.codex/skills/codex-workflows/templates/codex-native/.agent/workflows \
  --compat ~/.codex/skills/codex-workflows/packs/antigravity-compat/.agent/workflows \
  --max-similarity 0.35
```

8. Validate codex-native structural assets:

```bash
python ~/.codex/skills/codex-workflows/scripts/check_codex_native_assets.py \
  --native-root ~/.codex/skills/codex-workflows/templates/codex-native/.agent \
  --min-agents 10 \
  --min-skills 8
```

9. Benchmark routing runtime:

```bash
python ~/.codex/skills/codex-workflows/scripts/benchmark_router.py --iterations 10000
```

10. Run stack validation packs:

```bash
python ~/.codex/skills/codex-node-validation-pack/scripts/validate_node_stack.py --project .
python ~/.codex/skills/codex-python-validation-pack/scripts/validate_python_stack.py --project .
python ~/.codex/skills/codex-rust-validation-pack/scripts/validate_rust_stack.py --project .
```

11. Unified maintenance commands:

```bash
python scripts/codexwf.py status
python scripts/codexwf.py validate --tests
python scripts/codexwf.py docs-sync --build
```

## Web Portal (/website)

Portal de documentacao implementado dentro do proprio repositorio, em `website/`.

Idiomas:

- English (default)
- Portugues (Brasil) em `/pt/`
- Espanol em `/es/`
- Francais em `/fr/`
- 中文 em `/zh/`

Rodar localmente:

```bash
cd website
npm install
npm run docs:dev
```

Build local:

```bash
cd website
npm run docs:build
```

Deploy:

- workflow dedicado: `.github/workflows/docs.yml`
- publica build no branch `gh-pages`
- configure o GitHub Pages para usar `gh-pages` na primeira vez
- release e CI continuam separados em `.github/workflows/release.yml` e `.github/workflows/ci.yml`

## Prompting Best Practices

Use explicit skill + workflow phrasing for the most reliable behavior.

1. For complex tasks, start with:
- `Use codex-workflows in /orchestrate and <your objective>`
2. For focused tasks, keep the workflow explicit:
- `Use codex-workflows and run /debug for this error`
- `Use codex-workflows and run /plan for this feature`
3. This works for any workflow name in the catalog, not only `/orchestrate`.
4. Supported explicit trigger formats:
- `Use codex-workflows in /<workflow>`
- `Use codex-workflows em /<workflow>`
5. In a new chat/session, repeat the activation line in the first message.
6. In the same chat, short continuation prompts are enough:
- `Continue with codex-workflows /orchestrate from current plan`
7. Treat `/orchestrate`, `/debug`, `/plan`, etc. as intent labels in prompts, not native CLI slash commands.

Recommended activation template:

```text
Use codex-workflows in /orchestrate and execute this goal: <goal>.
Keep phase gates, verify outputs, and return a concise report.
```

Automation note:
- Explicit-trigger behavior is covered in `tests/test_route_workflow.py` for both router implementations.

## Behavior Notes

- Slash-like terms (for example `/orchestrate`) are interpreted as workflow intent in prompts.
- They are not native Codex CLI slash commands.
- If a project has local `.agent` files, local instructions have priority.

## Comparison to Antigravity

See `docs/COMPARISON.md` for a detailed comparison and adaptation strategy.

## Compatibility Scope

This repository includes a full compatibility pack under `skills/codex-workflows/packs/antigravity-compat/.agent` for optional interoperability with Antigravity-style `.agent` projects.

The default bootstrap path `codex-native` is independent from the compatibility pack and is sourced from `skills/codex-workflows/templates/codex-native/.agent`.

Workflow contracts are split:

- Native parity: `references/workflows/*.md` <-> `templates/codex-native/.agent/workflows/*.md`
- Compatibility parity: `templates/.agent/workflows/*.md` <-> `packs/antigravity-compat/.agent/workflows/*.md`

Native capability layer is also validated:

- `templates/codex-native/.agent/agents/*.md`
- `templates/codex-native/.agent/skills/*/SKILL.md`

## Domain Packs

Independent packs are available for targeted installation:

- `skills/codex-backend-pack`
- `skills/codex-frontend-pack`
- `skills/codex-security-pack`
- `skills/codex-qa-pack`
- `skills/codex-node-validation-pack`
- `skills/codex-python-validation-pack`
- `skills/codex-rust-validation-pack`

The routers also return `recommended_packs` based on detected domains.

## Release Automation

Use `scripts/release_automation.py` to automate changelog cut, commit, tag, and optional push.

Dry run:

```bash
python scripts/release_automation.py --version 1.1.0
```

Apply and publish:

```bash
python scripts/release_automation.py --version 1.1.0 --apply --commit --tag --push
```

GitHub Actions release workflow:

- `.github/workflows/release.yml` (`workflow_dispatch`)
- Auto publish on tag push (`v*`) using `docs/releases/<tag>.md` when available

## End-to-End Examples

- `examples/node-auth-api/README.md`
- `examples/python-fastapi-orders/README.md`
- `examples/rust-events-cli/README.md`
- `examples/projects/README.md` (real runnable fixtures used by CI matrix)

## CI and Quality Gates

- CI pipeline: `.github/workflows/ci.yml`
- Release pipeline: `.github/workflows/release.yml`
- Real stack matrix on fixtures: Node/Python/Rust in `.github/workflows/ci.yml`
- Skill validation: `scripts/ci_validate_skill.py`
- Unit tests: `tests/test_*.py`

## Contributing

See `CONTRIBUTING.md`.

## Community and Governance

- Issue templates:
  - `.github/ISSUE_TEMPLATE/bug_report.yml`
  - `.github/ISSUE_TEMPLATE/feature_request.yml`
- Pull request template:
  - `.github/PULL_REQUEST_TEMPLATE.md`
- Code ownership:
  - `.github/CODEOWNERS`

## Changelog

See `CHANGELOG.md`.

## Compatibility

- GPT Codex with skills support
- VS Code Codex workflow
- Windows, macOS, Linux

## License

MIT



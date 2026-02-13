# Installation

## Requirements

- Codex with skill support
- Python available in your environment
- GitHub access

## All-in-one (recommended)

Install the `codex-workflows` core plus all official packs in one command:

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

PowerShell:

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

## Local helper script (all-in-one)

Inside this repository:

```bash
python scripts/install_all_in_one.py
```

Dry run:

```bash
python scripts/install_all_in_one.py --dry-run
```

Specific tag/ref:

```bash
python scripts/install_all_in_one.py --ref v1.1.0
```

Unified CLI alternative:

```bash
python scripts/codexwf.py install
```

## Minimal installation

Install only the core workflow skill:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo helberfmelo/codex-workflows \
  --path skills/codex-workflows
```

## Post-install

1. Restart VS Code/Codex.
2. Activate with an explicit prompt:
`Use codex-workflows in /orchestrate and <objective>`.

Optional local bootstrap via unified CLI:

```bash
python scripts/codexwf.py init --project .
```

## Optional Composer channel (PHP users)

If your team prefers Composer scripts, use:

```bash
composer codex:install-all
```

This wrapper calls the same official Python installer under the hood.

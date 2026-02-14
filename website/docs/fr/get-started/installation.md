# Installation

## Prerequis

- Codex avec support skills
- Python disponible
- acces GitHub

## NPM all-in-one recommande

```bash
npx @codex-workflow/cw
```

Core uniquement :

```bash
npx @codex-workflow/cw --core-only
```

Diagnostic :

```bash
npx @codex-workflow/cw doctor
```

## All-in-One via Python direct (alternative)

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

Alternative CLI unifiee:

```bash
python scripts/codexwf.py install
```

## Canal Composer optionnel

```bash
composer codex:install-all
```

Bootstrap local optionnel:

```bash
python scripts/codexwf.py init --project .
```

## Post-installation

Activation recommandee:

- `cw /orchestrate <objectif>`
- `cw /help`
- `cw /examples`
- `Use codex-workflows in /orchestrate and <objective>`

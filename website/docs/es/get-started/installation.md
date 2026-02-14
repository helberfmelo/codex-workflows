# Instalacion

## Requisitos

- Codex con soporte a skills
- Python disponible
- acceso a GitHub

## NPM all-in-one recomendado

```bash
npx @codex-workflow/cw
```

Solo core:

```bash
npx @codex-workflow/cw --core-only
```

Diagnostico:

```bash
npx @codex-workflow/cw doctor
```

Fallback Windows:

```bash
npx @codex-workflow/cw --python-exec python
```

## All-in-One por Python directo (alternativa)

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

Alternativa con CLI unificada:

```bash
python scripts/codexwf.py install
```

## Canal Composer opcional

```bash
composer codex:install-all
```

Bootstrap local opcional:

```bash
python scripts/codexwf.py init --project .
```

## Post-instalacion

Activacion recomendada:

- `cw /orchestrate <objetivo>`
- `cw /help`
- `cw /examples`
- `Use codex-workflows in /orchestrate and <objective>`

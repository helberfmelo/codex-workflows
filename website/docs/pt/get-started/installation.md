# Instalacao

## Requisitos

- Codex com suporte a skills
- Python disponivel no ambiente
- acesso ao GitHub

## NPM all-in-one (recomendado)

```bash
npx @codex-workflow/cw
```

Somente core:

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

## All-in-one via Python direto (alternativa)

Instala `codex-workflows` + todos os packs oficiais em um unico comando:

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

## Helper local all-in-one

```bash
python scripts/install_all_in_one.py
```

Alternativa via CLI unificada:

```bash
python scripts/codexwf.py install
```

Dry run:

```bash
python scripts/install_all_in_one.py --dry-run
```

## Instalacao minima

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo helberfmelo/codex-workflows \
  --path skills/codex-workflows
```

## Pos-instalacao

1. Reinicie VS Code/Codex.
2. Ative com prompt explicito:
`cw /orchestrate <objetivo>`
`cw /help`
`cw /examples`
`Use codex-workflows em /orchestrate e <objetivo>`.

Bootstrap local opcional via CLI unificada:

```bash
python scripts/codexwf.py init --project .
```

## Canal opcional via Composer

```bash
composer codex:install-all
```

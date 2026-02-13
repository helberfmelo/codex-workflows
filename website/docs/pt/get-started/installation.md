# Instalacao

## Requisitos

- Codex com suporte a skills
- Python disponivel no ambiente
- acesso ao GitHub

## All-in-one (recomendado)

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
`Use codex-workflows em /orchestrate e <objetivo>`.

## Canal opcional via Composer

```bash
composer codex:install-all
```

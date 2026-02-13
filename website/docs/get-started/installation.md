# Instalacao

## Requisito

- Codex com suporte a skills
- Python disponivel no ambiente
- acesso ao GitHub

## All-in-one (recomendado)

Instala o core `codex-workflows` + todos os packs oficiais em um unico comando:

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

## Helper local (all-in-one)

Dentro do repositorio:

```bash
python scripts/install_all_in_one.py
```

Dry run:

```bash
python scripts/install_all_in_one.py --dry-run
```

Ref/tag especifica:

```bash
python scripts/install_all_in_one.py --ref v1.1.0
```

## Instalacao minima

Somente workflow core:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo helberfmelo/codex-workflows \
  --path skills/codex-workflows
```

## Pos-instalacao

1. Reinicie VS Code/Codex.
2. Ative com prompt explicito:
`Use codex-workflows em /orchestrate e <objetivo>`.

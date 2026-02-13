# Installation

## Prerequis

- Codex avec support skills
- Python disponible
- acces GitHub

## All-in-One recommande

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

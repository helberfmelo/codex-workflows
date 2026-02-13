# Quickstart

1. Activation explicite:
`Use codex-workflows in /orchestrate and <objective>`

2. Bootstrap local (profil par defaut `codex-native`):

```bash
python ~/.codex/skills/codex-workflows/scripts/bootstrap_project_agent.py --project .
```

Ce chemin par defaut est independant du pack de compatibilite.

Compatibilite:

```bash
python ~/.codex/skills/codex-workflows/scripts/bootstrap_project_agent.py --project . --profile antigravity-compat
```

3. Validation stack:

```bash
python ~/.codex/skills/codex-node-validation-pack/scripts/validate_node_stack.py --project . --run
python ~/.codex/skills/codex-python-validation-pack/scripts/validate_python_stack.py --project . --run
python ~/.codex/skills/codex-rust-validation-pack/scripts/validate_rust_stack.py --project . --run
```

4. Verifier la qualite codex-native:

```bash
python ~/.codex/skills/codex-workflows/scripts/check_codex_native_quality.py \
  --native ~/.codex/skills/codex-workflows/templates/codex-native/.agent/workflows \
  --compat ~/.codex/skills/codex-workflows/packs/antigravity-compat/.agent/workflows \
  --max-similarity 0.35
```



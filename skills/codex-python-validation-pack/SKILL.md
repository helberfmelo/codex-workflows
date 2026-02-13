---
name: codex-python-validation-pack
description: Python stack validation pack for Codex projects. Use when the task needs stack-specific quality checks for Python codebases, including lint/test/typecheck/build checks inferred from project metadata.
---

# Codex Python Validation Pack

Use this pack when the target repository is Python based.

## Validation Scope

- Detect Python project markers (`pyproject.toml`, `setup.py`, requirements files, source files)
- Build an ordered validation checklist based on configured tools
- Optionally execute checks and report pass/fail

## Script

Primary script:

- `scripts/validate_python_stack.py`

## Typical Usage

```bash
python ~/.codex/skills/codex-python-validation-pack/scripts/validate_python_stack.py --project .
python ~/.codex/skills/codex-python-validation-pack/scripts/validate_python_stack.py --project . --run
```

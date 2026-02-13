---
name: codex-node-validation-pack
description: Node.js and TypeScript validation pack for Codex projects. Use when the task needs stack-specific quality checks for Node codebases, including lint/test/build/typecheck/security checks from package scripts.
---

# Codex Node Validation Pack

Use this pack when the target repository is Node.js or TypeScript based.

## Validation Scope

- Detect project scripts from `package.json`
- Build an ordered validation checklist
- Optionally execute checks and report pass/fail

## Script

Primary script:

- `scripts/validate_node_stack.py`

## Typical Usage

```bash
python ~/.codex/skills/codex-node-validation-pack/scripts/validate_node_stack.py --project .
python ~/.codex/skills/codex-node-validation-pack/scripts/validate_node_stack.py --project . --run
```


---
name: codex-rust-validation-pack
description: Rust stack validation pack for Codex projects. Use when the task needs stack-specific quality checks for Rust codebases, including fmt/clippy/test/build and optional security audit checks.
---

# Codex Rust Validation Pack

Use this pack when the target repository is Rust based.

## Validation Scope

- Detect Cargo project metadata (`Cargo.toml`)
- Build an ordered validation checklist for package/workspace projects
- Optionally execute checks and report pass/fail

## Script

Primary script:

- `scripts/validate_rust_stack.py`

## Typical Usage

```bash
python ~/.codex/skills/codex-rust-validation-pack/scripts/validate_rust_stack.py --project .
python ~/.codex/skills/codex-rust-validation-pack/scripts/validate_rust_stack.py --project . --run
```

# Contributing

Thanks for contributing to `codex-workflows`.

## Development Flow

1. Fork the repository.
2. Create a branch from `main`.
3. Make focused changes.
4. Update docs when behavior changes.
5. Open a pull request with clear context.

## Pull Request Checklist

- Scope is small and focused.
- `skills/codex-workflows/SKILL.md` is updated when workflow logic changes.
- `skills/codex-workflows/references/workflow-playbook.md` is kept in sync.
- `README.md` examples remain valid.
- `CHANGELOG.md` has an entry under `Unreleased`.

## Style Guidelines

- Keep naming lowercase with hyphens for skills.
- Prefer concise and deterministic instructions.
- Keep workflow phases explicit.
- Avoid tool-specific assumptions when not required.

## Validation

If you have local Codex system skills installed, validate with:

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/codex-workflows
```

Windows (PowerShell):

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "skills/codex-workflows"
```

## Reporting Issues

Open an issue with:

- Environment (OS, Codex setup)
- Prompt used
- Expected behavior
- Actual behavior
- Minimal reproduction

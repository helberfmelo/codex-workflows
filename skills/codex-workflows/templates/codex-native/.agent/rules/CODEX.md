# Codex-Native Rules

This ruleset is layered and cumulative:

1. `global/*` applies to every task.
2. `domains/*` applies when the domain is present.
3. `workflows/*` applies when that workflow is selected.

Execution order:

- Start with global rules.
- Merge relevant domain rules.
- Apply selected workflow rule as the final gate.

Core constraints:

- Keep evidence-based decisions and reproducible checks.
- Keep change scope small and reversible where possible.
- Raise risk before applying high-impact operations.
- Prefer codex-native defaults unless compatibility is explicitly required.

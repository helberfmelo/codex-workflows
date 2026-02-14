# Tasks: Ecosystem Maturity (/orchestrate)

Date: 2026-02-14
Owner: codex-workflows

## Phases

1. CLI Reliability Phase (cw v1.2.2)
- Make Windows execution deterministic.
- Prioritize `python` before `python3` on Windows.
- Improve fallback discovery for Python launchers.

2. Cross-Platform Installation Assurance Phase
- Add E2E CI for `npx @codex-workflow/cw`.
- Execute real installation path on Linux/macOS/Windows.
- Validate resulting installed skill directories.

3. Release Automation Phase
- Extend release flow to sync package version + changelog.
- Add npm publish automation with token-based publish step.
- Keep GitHub release and npm release aligned by tag.

4. Adoption and Developer Experience Phase
- Add larger real-world examples.
- Add quick wins by user profile with copy/paste prompts.
- Improve onboarding path from installation to first outcome.

5. Documentation and Portal Parity Phase
- Update README + technical docs.
- Sync website docs in EN/PT/ES/FR/ZH.
- Validate docs build and regression tests.

## Task List

- [x] T1. CLI v1.2.2 Windows reliability improvements
- [x] T1.1 Add/adjust automated tests for CLI fallback behavior
- [x] T2. CI matrix E2E install via npm package command
- [x] T2.1 Validate install artifacts in CI jobs
- [x] T3. Release automation updates (version sync + npm publish)
- [x] T3.1 Add tests for release automation package version sync
- [x] T4. Add larger examples and quick wins by profile
- [x] T5. Update docs + website locales + reference sync
- [x] T5.1 Full validation and push
- [x] T6. Make repository root `.agent` optional for manifest maintenance
- [x] T6.1 Add automated tests for manifest source fallback resolution
- [x] T6.2 Update operations/compatibility docs + website mirrored source docs

## Validation Gate (done at each phase)

- `python -m unittest discover -s tests -p "test_*.py"`
- `npm run docs:build` (website)
- `npm pack --dry-run` (root package)
- CI YAML lint by running workflows in GitHub on push

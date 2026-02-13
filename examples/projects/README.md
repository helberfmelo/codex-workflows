# Real Stack Fixtures for CI

This folder contains runnable sample projects used by CI matrix jobs:

- `node-service`: Node.js scripts + tests (`npm run lint/typecheck/test/build`)
- `python-service`: Python package with lint/typecheck/tests
- `rust-service`: Cargo project with fmt/clippy/test/build

These fixtures validate that stack packs execute real checks, not stub commands.

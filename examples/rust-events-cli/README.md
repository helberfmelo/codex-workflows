# E2E Example: Rust Events CLI

## Scenario

Build a Rust command-line app to process event logs:

- parse JSONL events at scale;
- validate schema and reject malformed payloads;
- aggregate metrics by tenant and event type;
- expose benchmark and reliability report.

## Prompt Sequence

1. Design and decomposition:

`Use codex-workflows in /orchestrate and define architecture for a Rust CLI that ingests JSONL events with strict validation and performance targets.`

2. Build core:

`Continue with codex-workflows /create and implement parser, domain model, and aggregation pipeline.`

3. Performance pass:

`Use codex-workflows in /enhance to optimize allocations, improve throughput, and add benchmarks.`

4. Delivery:

`Use codex-workflows in /deploy and prepare release notes, versioning plan, and rollback strategy for the CLI package.`

## Expected Deliverables

- Rust crate structure and modules
- parsing and validation pipeline
- unit tests + benchmark harness
- release plan with risk controls
- final orchestration summary

## Validation Commands

`python skills/codex-rust-validation-pack/scripts/validate_rust_stack.py --project .`

`python skills/codex-rust-validation-pack/scripts/validate_rust_stack.py --project . --run`

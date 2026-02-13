# Source: docs/PERFORMANCE.md

# Performance

This project tracks router performance at script level.

## Baseline metric (2026-02-13)

- `route_workflow.py` CLI cold process average around 264 ms/call in local Windows environment.
- This includes Python interpreter startup overhead.

## Benchmark command

`python skills/codex-workflows/scripts/benchmark_router.py --iterations 10000`

The benchmark compares in-process functions:

- baseline: `route_workflow.route`
- optimized: `route_workflow_fast.route`

## Target

- Keep `route_workflow_fast` average in-process latency below baseline.
- Preserve routing correctness against baseline on representative queries.

## Performance guidance

- Prefer in-process router use when possible.
- Avoid repeatedly spawning Python for each single routing request.
- Keep routing rules data-driven (`routing_data.py`) to simplify optimization.

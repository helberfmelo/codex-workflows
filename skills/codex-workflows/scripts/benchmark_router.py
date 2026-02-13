#!/usr/bin/env python3
"""Benchmark baseline and fast workflow routers in-process."""
from __future__ import annotations

import argparse
import statistics
import time

import route_workflow
import route_workflow_fast

DEFAULT_QUERIES = [
    "build secure login api with frontend and tests",
    "debug why checkout fails in production",
    "plan roadmap for dashboard refactor",
    "deploy release with rollback plan",
    "design system for a fintech app",
]


def benchmark(fn, queries: list[str], iterations: int) -> dict[str, float]:
    samples_ms: list[float] = []
    q_len = len(queries)
    for i in range(iterations):
        q = queries[i % q_len]
        t0 = time.perf_counter()
        fn(q)
        samples_ms.append((time.perf_counter() - t0) * 1000.0)
    return {
        "avg_ms": statistics.fmean(samples_ms),
        "median_ms": statistics.median(samples_ms),
        "p95_ms": statistics.quantiles(samples_ms, n=20)[18] if len(samples_ms) >= 20 else max(samples_ms),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--iterations", type=int, default=10000, help="Iterations per implementation")
    args = parser.parse_args()

    baseline = benchmark(route_workflow.route, DEFAULT_QUERIES, args.iterations)
    fast = benchmark(route_workflow_fast.route, DEFAULT_QUERIES, args.iterations)
    speedup = baseline["avg_ms"] / fast["avg_ms"] if fast["avg_ms"] else 0.0

    print("Router benchmark (in-process)")
    print(f"iterations={args.iterations}")
    print(
        "baseline avg={avg_ms:.6f}ms median={median_ms:.6f}ms p95={p95_ms:.6f}ms".format(
            **baseline
        )
    )
    print(
        "fast     avg={avg_ms:.6f}ms median={median_ms:.6f}ms p95={p95_ms:.6f}ms".format(
            **fast
        )
    )
    print(f"speedup={speedup:.3f}x")


if __name__ == "__main__":
    main()


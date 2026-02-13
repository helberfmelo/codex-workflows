#!/usr/bin/env python3
"""Route a user request to the most likely codex workflow."""
from __future__ import annotations
import argparse
import json
from collections import defaultdict

RULES = {
    "/brainstorm": ["brainstorm", "idea", "option", "alternatives", "compare"],
    "/plan": ["plan", "roadmap", "milestone", "breakdown", "scope"],
    "/create": ["create", "build", "new app", "from scratch"],
    "/enhance": ["enhance", "improve", "refactor", "add feature", "upgrade"],
    "/debug": ["debug", "bug", "error", "broken", "regression", "fix issue"],
    "/test": ["test", "coverage", "unit", "integration", "e2e"],
    "/deploy": ["deploy", "production", "release", "rollback"],
    "/preview": ["preview", "run local", "start server", "localhost"],
    "/status": ["status", "progress", "what is done", "board"],
    "/orchestrate": ["orchestrate", "end to end", "complex", "multi domain"],
    "/ui-ux-pro-max": ["ui", "ux", "design system", "layout", "visual"],
}


def route(text: str) -> dict:
    low = text.lower()
    scores = defaultdict(int)
    hits = defaultdict(list)
    for wf, patterns in RULES.items():
        for p in patterns:
            if p in low:
                scores[wf] += 1
                hits[wf].append(p)

    if not scores:
        return {
            "workflow": "/plan",
            "confidence": "low",
            "reason": "No strong keyword match; defaulting to planning.",
            "secondary": []
        }

    ordered = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
    primary, top = ordered[0]
    secondary = [wf for wf, score in ordered[1:3] if score >= max(1, top - 1)]
    confidence = "high" if top >= 3 else "medium"

    return {
        "workflow": primary,
        "confidence": confidence,
        "reason": f"Matched: {', '.join(hits[primary])}",
        "secondary": secondary,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="User request to classify")
    parser.add_argument("--json", action="store_true", help="Print JSON")
    args = parser.parse_args()
    result = route(args.query)
    if args.json:
        print(json.dumps(result, ensure_ascii=True))
        return
    print(f"workflow={result['workflow']}")
    print(f"confidence={result['confidence']}")
    print(f"reason={result['reason']}")
    print(f"secondary={','.join(result['secondary'])}")


if __name__ == "__main__":
    main()

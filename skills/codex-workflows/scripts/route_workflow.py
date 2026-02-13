#!/usr/bin/env python3
"""Route a user request to the most likely codex workflow."""
from __future__ import annotations
import argparse
import json
from collections import defaultdict
from routing_data import (
    DOMAIN_HINTS,
    DOMAIN_TO_PACK,
    RULES,
    detect_domains,
    detect_explicit_workflow,
    tokenize,
)


def recommend_packs(domains: set[str]) -> list[str]:
    packs = {DOMAIN_TO_PACK[d] for d in domains if d in DOMAIN_TO_PACK}
    return sorted(packs)


def route(text: str) -> dict:
    low = text.lower()
    tokens = tokenize(low)
    scores = defaultdict(int)
    hits = defaultdict(list)
    matched_domains = detect_domains(low, DOMAIN_HINTS)
    packs = recommend_packs(matched_domains)

    explicit_workflow = detect_explicit_workflow(text, set(RULES.keys()))
    if explicit_workflow:
        return {
            "workflow": explicit_workflow,
            "confidence": "high",
            "reason": f"Explicit workflow activation detected: {explicit_workflow}",
            "secondary": [],
            "domains": sorted(matched_domains),
            "recommended_packs": packs,
            "explicit_activation": True,
        }

    for wf, patterns in RULES.items():
        for p in patterns:
            if " " in p:
                matched = p in low
            else:
                matched = p in tokens
            if matched:
                scores[wf] += 1
                hits[wf].append(p)

    if len(matched_domains) >= 2 and "/orchestrate" not in scores:
        return {
            "workflow": "/orchestrate",
            "confidence": "high",
            "reason": f"Detected multi-domain task: {', '.join(sorted(matched_domains))}",
            "secondary": [],
            "domains": sorted(matched_domains),
            "recommended_packs": packs,
            "explicit_activation": False,
        }

    if not scores:
        return {
            "workflow": "/plan",
            "confidence": "low",
            "reason": "No strong keyword match; defaulting to planning.",
            "secondary": [],
            "domains": sorted(matched_domains),
            "recommended_packs": packs,
            "explicit_activation": False,
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
        "domains": sorted(matched_domains),
        "recommended_packs": packs,
        "explicit_activation": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="User request to classify")
    parser.add_argument("--json", action="store_true", help="Print JSON")
    parser.add_argument("--show-domains", action="store_true", help="Print detected domains and pack hints")
    args = parser.parse_args()
    result = route(args.query)
    if args.json:
        print(json.dumps(result, ensure_ascii=True))
        return
    print(f"workflow={result['workflow']}")
    print(f"confidence={result['confidence']}")
    print(f"reason={result['reason']}")
    print(f"secondary={','.join(result['secondary'])}")
    if args.show_domains:
        print(f"domains={','.join(result['domains'])}")
        print(f"recommended_packs={','.join(result['recommended_packs'])}")
        print(f"explicit_activation={str(result['explicit_activation']).lower()}")


if __name__ == "__main__":
    main()

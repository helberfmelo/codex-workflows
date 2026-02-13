#!/usr/bin/env python3
"""Fast in-process workflow router with token scoring."""
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


def _compile_indexes() -> tuple[dict[str, list[tuple[str, str]]], list[tuple[str, str]]]:
    singles: dict[str, list[tuple[str, str]]] = defaultdict(list)
    phrases: list[tuple[str, str]] = []
    for workflow, patterns in RULES.items():
        for pattern in patterns:
            if " " in pattern:
                phrases.append((pattern, workflow))
            else:
                singles[pattern].append((workflow, pattern))
    return singles, phrases


SINGLE_KEYWORDS, PHRASE_KEYWORDS = _compile_indexes()


def recommend_packs(domains: set[str]) -> list[str]:
    packs = {DOMAIN_TO_PACK[d] for d in domains if d in DOMAIN_TO_PACK}
    return sorted(packs)


def route(text: str) -> dict:
    tokens = tokenize(text)
    low = text.lower()
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

    for token in tokens:
        for workflow, pattern in SINGLE_KEYWORDS.get(token, []):
            scores[workflow] += 1
            hits[workflow].append(pattern)
    for phrase, workflow in PHRASE_KEYWORDS:
        if phrase in low:
                scores[workflow] += 1
                hits[workflow].append(phrase)

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

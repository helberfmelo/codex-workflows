#!/usr/bin/env python3
"""Shared constants and helpers for workflow routing."""
from __future__ import annotations

import re

TOKEN_RE = re.compile(r"[a-z0-9]+")
EXPLICIT_WORKFLOW_PATTERNS = (
    re.compile(r"use\s+codex-workflows\s+(?:in|em)\s+/[`'\"\[]?([a-z0-9][a-z0-9\-]*)[`'\"\]]?", re.IGNORECASE),
    re.compile(r"use\s+codex-workflows\s+(?:and\s+run|e\s+execute)\s+/[`'\"\[]?([a-z0-9][a-z0-9\-]*)[`'\"\]]?", re.IGNORECASE),
)

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

DOMAIN_HINTS = {
    "frontend": ["frontend", "ui", "ux", "css", "tailwind", "react", "vue", "layout"],
    "backend": ["backend", "api", "endpoint", "server", "fastapi", "express", "nestjs"],
    "security": ["auth", "login", "jwt", "token", "security", "vulnerability", "owasp"],
    "database": ["database", "schema", "sql", "migration", "prisma", "postgres"],
    "testing": ["test", "coverage", "unit", "integration", "playwright", "cypress"],
    "devops": ["deploy", "ci", "cd", "docker", "kubernetes", "production"],
}

DOMAIN_TO_PACK = {
    "frontend": "codex-frontend-pack",
    "backend": "codex-backend-pack",
    "security": "codex-security-pack",
    "database": "codex-backend-pack",
    "testing": "codex-qa-pack",
    "devops": "codex-qa-pack",
}


def tokenize(text: str) -> set[str]:
    return set(TOKEN_RE.findall(text.lower()))


def detect_domains(text: str, domain_hints: dict[str, list[str]] | None = None) -> set[str]:
    hints = domain_hints or DOMAIN_HINTS
    domains = set()
    low = text.lower()
    for domain, patterns in hints.items():
        if any(p in low for p in patterns):
            domains.add(domain)
    return domains


def detect_explicit_workflow(
    text: str, valid_workflows: set[str] | None = None
) -> str | None:
    allowed = valid_workflows or set(RULES.keys())
    for pattern in EXPLICIT_WORKFLOW_PATTERNS:
        match = pattern.search(text)
        if not match:
            continue
        workflow = "/" + match.group(1).lower().strip()
        if workflow in allowed:
            return workflow
    return None

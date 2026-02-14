#!/usr/bin/env python3
"""Shared constants and helpers for workflow routing."""
from __future__ import annotations

import re

TOKEN_RE = re.compile(r"[a-z0-9]+")
EXPLICIT_TARGET_PATTERNS = (
    re.compile(r"use\s+codex-workflows?\s+(?:in|em)\s+/[`'\"\[]?([a-z0-9][a-z0-9\-]*)[`'\"\]]?", re.IGNORECASE),
    re.compile(r"use\s+codex-workflows?\s+(?:and\s+run|e\s+execute)\s+/[`'\"\[]?([a-z0-9][a-z0-9\-]*)[`'\"\]]?", re.IGNORECASE),
    re.compile(r"\bcodex-workflows?\s+/[`'\"\[]?([a-z0-9][a-z0-9\-]*)[`'\"\]]?", re.IGNORECASE),
    re.compile(r"\bcw\s+/[`'\"\[]?([a-z0-9][a-z0-9\-]*)[`'\"\]]?", re.IGNORECASE),
)

RULES = {
    "/brainstorm": ["brainstorm", "idea", "option", "alternatives", "compare"],
    "/plan": ["plan", "roadmap", "milestone", "breakdown", "scope"],
    "/create": ["create", "build", "new app", "from scratch"],
    "/enhance": ["enhance", "improve", "refactor", "add feature", "upgrade"],
    "/game-dev": ["game", "gameplay", "core loop", "unity", "godot", "unreal", "level design"],
    "/roblox-game-dev": ["roblox", "roblox studio", "luau", "remoteevent", "remotefunction", "datastore"],
    "/debug": ["debug", "bug", "error", "broken", "regression", "fix issue"],
    "/test": ["test", "coverage", "unit", "integration", "e2e"],
    "/deploy": ["deploy", "production", "release", "rollback"],
    "/preview": ["preview", "run local", "start server", "localhost"],
    "/status": ["status", "progress", "what is done", "board"],
    "/orchestrate": ["orchestrate", "end to end", "complex", "multi domain"],
    "/ui-ux-pro-max": ["ui", "ux", "design system", "layout", "visual"],
}

UTILITY_COMMANDS = {"/help", "/examples"}

WORKFLOW_SUMMARIES = {
    "/brainstorm": "Explore options before coding decisions",
    "/plan": "Break scope into executable milestones",
    "/create": "Build new features from approved plans",
    "/enhance": "Improve existing behavior with minimal risk",
    "/game-dev": "Deliver gameplay systems with iterative validation",
    "/roblox-game-dev": "Build Roblox features with secure remotes",
    "/debug": "Find root causes and fix regressions",
    "/test": "Design and run risk-based tests",
    "/deploy": "Release safely with rollback readiness",
    "/preview": "Run locally and verify behavior",
    "/status": "Report progress, risks, and next actions",
    "/orchestrate": "Coordinate multi-domain delivery with phase gates",
    "/ui-ux-pro-max": "Design premium interfaces with UX rigor",
}

EXAMPLE_INVOCATIONS = (
    "cw /orchestrate harden auth flow end-to-end",
    "cw /game-dev prototype combat loop with progression",
    "cw /roblox-game-dev secure DataStore economy updates",
    "codex-workflow /debug investigate flaky checkout test",
    "codex-workflows /plan roadmap for release hardening",
    "Use codex-workflows em /test e aumentar cobertura",
)

DOMAIN_HINTS = {
    "frontend": ["frontend", "ui", "ux", "css", "tailwind", "react", "vue", "layout"],
    "backend": ["backend", "api", "endpoint", "server", "fastapi", "express", "nestjs"],
    "security": ["auth", "login", "jwt", "token", "security", "vulnerability", "owasp"],
    "database": ["database", "schema", "sql", "migration", "prisma", "postgres"],
    "testing": ["test", "coverage", "unit", "integration", "playwright", "cypress"],
    "devops": ["deploy", "ci", "cd", "docker", "kubernetes", "production"],
    "game": ["game", "gameplay", "unity", "godot", "unreal", "roblox", "luau"],
}

STACK_HINTS = {
    "node": ["node", "nodejs", "javascript", "typescript", "npm", "pnpm", "yarn", "package.json"],
    "python": ["python", "django", "flask", "pyproject", "poetry", "pytest", "pydantic"],
    "rust": ["rust", "cargo", "cargo.toml", "clippy", "tokio", "actix"],
}

DOMAIN_TO_PACK = {
    "frontend": "codex-frontend-pack",
    "backend": "codex-backend-pack",
    "security": "codex-security-pack",
    "database": "codex-backend-pack",
    "testing": "codex-qa-pack",
    "devops": "codex-qa-pack",
}

STACK_TO_PACK = {
    "node": "codex-node-validation-pack",
    "python": "codex-python-validation-pack",
    "rust": "codex-rust-validation-pack",
}


def tokenize(text: str) -> set[str]:
    return set(TOKEN_RE.findall(text.lower()))


def _normalized_target(raw_target: str) -> str:
    target = raw_target.lower().strip()
    if not target.startswith("/"):
        target = "/" + target
    return target


def detect_domains(text: str, domain_hints: dict[str, list[str]] | None = None) -> set[str]:
    hints = domain_hints or DOMAIN_HINTS
    domains = set()
    low = text.lower()
    tokens = tokenize(low)
    for domain, patterns in hints.items():
        matched = False
        for pattern in patterns:
            p = pattern.lower()
            if " " in p or len(p) > 2:
                if p in low:
                    matched = True
                    break
            else:
                if p in tokens:
                    matched = True
                    break
        if matched:
            domains.add(domain)
    return domains


def detect_stack_packs(
    text: str,
    stack_hints: dict[str, list[str]] | None = None,
    stack_to_pack: dict[str, str] | None = None,
) -> set[str]:
    hints = stack_hints or STACK_HINTS
    mapping = stack_to_pack or STACK_TO_PACK
    low = text.lower()
    packs = set()
    for stack, patterns in hints.items():
        if stack in mapping and any(p in low for p in patterns):
            packs.add(mapping[stack])
    return packs


def detect_explicit_workflow(
    text: str, valid_workflows: set[str] | None = None
) -> str | None:
    allowed = valid_workflows or set(RULES.keys())
    for pattern in EXPLICIT_TARGET_PATTERNS:
        match = pattern.search(text)
        if not match:
            continue
        workflow = _normalized_target(match.group(1))
        if workflow in allowed:
            return workflow
    return None


def detect_explicit_command(
    text: str, valid_commands: set[str] | None = None
) -> str | None:
    allowed = valid_commands or set(UTILITY_COMMANDS)
    for pattern in EXPLICIT_TARGET_PATTERNS:
        match = pattern.search(text)
        if not match:
            continue
        command = _normalized_target(match.group(1))
        if command in allowed:
            return command
    return None


def render_help_text() -> str:
    lines = [
        "codex-workflows router help",
        "",
        "Usage:",
        "  cw /<workflow> <objective>",
        "  codex-workflow /<workflow> <objective>",
        "  codex-workflows /<workflow> <objective>",
        "  Use codex-workflows in /<workflow> and <objective>",
        "",
        "Utility commands:",
        "  cw /help      Show this help message",
        "  cw /examples  Show workflows and examples",
        "",
        f"Available workflows ({len(RULES)}):",
    ]
    for workflow in sorted(RULES):
        lines.append(f"  {workflow}")
    lines.extend(
        [
            "",
            "Tip:",
            "  Use explicit workflow + objective for deterministic routing.",
        ]
    )
    return "\n".join(lines)


def render_examples_text() -> str:
    lines = [
        "codex-workflows router examples",
        "",
        "Workflows:",
    ]
    for workflow in sorted(RULES):
        summary = WORKFLOW_SUMMARIES.get(workflow, "No summary available")
        lines.append(f"  {workflow:<18} {summary}")
    lines.extend(["", "Examples:"])
    for example in EXAMPLE_INVOCATIONS:
        lines.append(f"  {example}")
    return "\n".join(lines)

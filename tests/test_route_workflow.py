from __future__ import annotations

import importlib.util
import pathlib
import sys
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "skills" / "codex-workflows" / "scripts"
sys.path.insert(0, str(SCRIPTS))


def load_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module


route_workflow = load_module(SCRIPTS / "route_workflow.py", "route_workflow")
route_workflow_fast = load_module(SCRIPTS / "route_workflow_fast.py", "route_workflow_fast")


class RouteWorkflowTests(unittest.TestCase):
    def test_multidomain_routes_to_orchestrate(self):
        result = route_workflow.route("build secure login api with frontend and tests")
        self.assertEqual(result["workflow"], "/orchestrate")
        self.assertIn("security", result["domains"])
        self.assertIn("backend", result["domains"])
        self.assertIn("frontend", result["domains"])
        self.assertIn("codex-security-pack", result["recommended_packs"])

    def test_unknown_defaults_to_plan(self):
        result = route_workflow.route("hello there")
        self.assertEqual(result["workflow"], "/plan")
        self.assertEqual(result["confidence"], "low")

    def test_fast_router_workflow_parity(self):
        queries = [
            "debug checkout bug in production",
            "plan roadmap for billing revamp",
            "deploy release and prepare rollback",
            "design system for new dashboard",
        ]
        for q in queries:
            base = route_workflow.route(q)
            fast = route_workflow_fast.route(q)
            self.assertEqual(base["workflow"], fast["workflow"])


if __name__ == "__main__":
    unittest.main()


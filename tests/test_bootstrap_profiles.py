from __future__ import annotations

import pathlib
import subprocess
import sys
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "codex-workflows" / "scripts" / "bootstrap_project_agent.py"


class BootstrapProfileTests(unittest.TestCase):
    def test_minimal_profile_bootstrap(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = pathlib.Path(tmp)
            subprocess.run(
                [sys.executable, str(SCRIPT), "--project", str(project), "--profile", "minimal"],
                check=True,
            )
            wf = project / ".agent" / "workflows" / "brainstorm.md"
            self.assertTrue(wf.exists())
            line_count = len(wf.read_text(encoding="utf-8").splitlines())
            self.assertLess(line_count, 20)

    def test_full_profile_bootstrap(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = pathlib.Path(tmp)
            subprocess.run(
                [sys.executable, str(SCRIPT), "--project", str(project), "--profile", "antigravity-compat"],
                check=True,
            )
            wf = project / ".agent" / "workflows" / "brainstorm.md"
            self.assertTrue(wf.exists())
            line_count = len(wf.read_text(encoding="utf-8").splitlines())
            self.assertGreater(line_count, 40)

    def test_existing_requires_force(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = pathlib.Path(tmp)
            subprocess.run(
                [sys.executable, str(SCRIPT), "--project", str(project), "--profile", "minimal"],
                check=True,
            )
            second = subprocess.run(
                [sys.executable, str(SCRIPT), "--project", str(project), "--profile", "minimal"],
                check=False,
            )
            self.assertNotEqual(second.returncode, 0)


if __name__ == "__main__":
    unittest.main()


from __future__ import annotations

import pathlib
import subprocess
import sys
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "codex-workflows" / "scripts" / "sync_compat_pack.py"


class SyncCompatPackTests(unittest.TestCase):
    def test_sync_copies_agent_and_strips_pycache(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = pathlib.Path(tmp)
            source = base / "source" / ".agent"
            dest = base / "dest" / ".agent"
            (source / "workflows").mkdir(parents=True)
            (source / "workflows" / "brainstorm.md").write_text("# test\n", encoding="utf-8")
            (source / "scripts" / "__pycache__").mkdir(parents=True)
            (source / "scripts" / "__pycache__" / "x.pyc").write_bytes(b"abc")

            subprocess.run(
                [sys.executable, str(SCRIPT), "--source", str(source), "--dest", str(dest)],
                check=True,
            )

            self.assertTrue((dest / "workflows" / "brainstorm.md").exists())
            self.assertFalse((dest / "scripts" / "__pycache__").exists())


if __name__ == "__main__":
    unittest.main()


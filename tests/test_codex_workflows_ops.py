from __future__ import annotations

import importlib.util
import pathlib
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "codex-workflows" / "scripts" / "codex_workflows_ops.py"


def load_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module


ops = load_module(SCRIPT, "codex_workflows_ops")


class CodexWorkflowsOpsTests(unittest.TestCase):
    def test_resolve_manifest_source_prefers_explicit_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            explicit = root / "explicit" / ".agent"
            explicit.mkdir(parents=True)
            source, used_fallback = ops.resolve_manifest_source(
                str(explicit),
                cwd=root / "cwd",
                pack_root=root / "pack",
            )
            self.assertEqual(source, explicit.resolve())
            self.assertFalse(used_fallback)

    def test_resolve_manifest_source_uses_cwd_agent_when_available(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            cwd = root / "cwd"
            (cwd / ".agent").mkdir(parents=True)
            source, used_fallback = ops.resolve_manifest_source(
                None,
                cwd=cwd,
                pack_root=root / "pack",
            )
            self.assertEqual(source, (cwd / ".agent").resolve())
            self.assertFalse(used_fallback)

    def test_resolve_manifest_source_falls_back_to_pack_when_no_agent_exists(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            cwd = root / "cwd"
            cwd.mkdir(parents=True)
            pack = root / "pack"
            pack.mkdir(parents=True)
            source, used_fallback = ops.resolve_manifest_source(
                None,
                cwd=cwd,
                pack_root=pack,
            )
            self.assertEqual(source, pack.resolve())
            self.assertTrue(used_fallback)

    def test_resolve_manifest_source_raises_for_missing_explicit_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            with self.assertRaises(FileNotFoundError):
                ops.resolve_manifest_source(
                    str(root / "missing" / ".agent"),
                    cwd=root / "cwd",
                    pack_root=root / "pack",
                )


if __name__ == "__main__":
    unittest.main()

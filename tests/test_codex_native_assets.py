from __future__ import annotations

import importlib.util
import pathlib
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "codex-workflows" / "scripts" / "check_codex_native_assets.py"


def load_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module


assets = load_module(SCRIPT, "check_codex_native_assets")


class CodexNativeAssetsTests(unittest.TestCase):
    def test_real_repository_passes(self):
        native_root = ROOT / "skills" / "codex-workflows" / "templates" / "codex-native" / ".agent"
        errors = assets.validate(native_root=native_root, min_agents=20, min_skills=37)
        self.assertEqual(errors, [])

    def test_missing_agents_folder_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = pathlib.Path(tmp)
            (base / "workflows").mkdir(parents=True, exist_ok=True)
            (base / "rules").mkdir(parents=True, exist_ok=True)
            (base / "scripts").mkdir(parents=True, exist_ok=True)
            (base / "skills").mkdir(parents=True, exist_ok=True)
            (base / "ARCHITECTURE.md").write_text("# x\n", encoding="utf-8")
            (base / "rules" / "CODEX.md").write_text("# x\n", encoding="utf-8")
            (base / "scripts" / "auto_preview.py").write_text("print('x')\n", encoding="utf-8")
            for wf in assets.EXPECTED_WORKFLOWS:
                (base / "workflows" / wf).write_text("# x\n", encoding="utf-8")
            errors = assets.validate(native_root=base, min_agents=1, min_skills=0)
            self.assertTrue(any("missing required path" in err and "agents" in err for err in errors))

    def test_invalid_skill_frontmatter_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = pathlib.Path(tmp)
            (base / "workflows").mkdir(parents=True, exist_ok=True)
            (base / "rules").mkdir(parents=True, exist_ok=True)
            (base / "scripts").mkdir(parents=True, exist_ok=True)
            (base / "agents").mkdir(parents=True, exist_ok=True)
            (base / "skills" / "x").mkdir(parents=True, exist_ok=True)
            (base / "ARCHITECTURE.md").write_text("# x\n", encoding="utf-8")
            (base / "rules" / "CODEX.md").write_text("# x\n", encoding="utf-8")
            (base / "scripts" / "auto_preview.py").write_text("print('x')\n", encoding="utf-8")
            for wf in assets.EXPECTED_WORKFLOWS:
                (base / "workflows" / wf).write_text("# x\n", encoding="utf-8")
            (base / "agents" / "a.md").write_text("# x\n", encoding="utf-8")
            (base / "skills" / "x" / "SKILL.md").write_text("# x\n", encoding="utf-8")
            errors = assets.validate(native_root=base, min_agents=1, min_skills=1)
            self.assertTrue(any("invalid frontmatter" in err for err in errors))


if __name__ == "__main__":
    unittest.main()


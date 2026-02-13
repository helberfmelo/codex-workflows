from __future__ import annotations

import importlib.util
import pathlib
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "codex-workflows" / "scripts" / "check_codex_native_quality.py"


def load_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module


quality = load_module(SCRIPT, "check_codex_native_quality")


def build_workflow_content(required_sections: list[str]) -> str:
    parts = [
        "---",
        "description: sample workflow",
        "---",
        "",
        "# /sample",
        "",
    ]
    for section in required_sections:
        parts.extend([section, "- sample line 1", "- sample line 2", ""])
    return "\n".join(parts)


class CodexNativeQualityTests(unittest.TestCase):
    def test_real_repository_passes_quality_validation(self):
        native = ROOT / "skills" / "codex-workflows" / "templates" / "codex-native" / ".agent" / "workflows"
        compat = ROOT / "skills" / "codex-workflows" / "packs" / "antigravity-compat" / ".agent" / "workflows"
        errors = quality.validate(native_dir=native, compat_dir=compat, min_lines=45)
        self.assertEqual(errors, [])

    def test_missing_native_workflow_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = pathlib.Path(tmp)
            native = tmp_path / "native"
            compat = tmp_path / "compat"
            native.mkdir()
            compat.mkdir()

            first_name = next(iter(quality.EXPECTED_WORKFLOWS))
            (native / first_name).write_text("---\ndescription: x\n---\n# x\n", encoding="utf-8")
            (compat / first_name).write_text("---\ndescription: x\n---\n# x\n", encoding="utf-8")

            errors = quality.validate(native_dir=native, compat_dir=compat, min_lines=1)
            self.assertTrue(any("missing native workflow" in err for err in errors))

    def test_identical_to_compat_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = pathlib.Path(tmp)
            native = tmp_path / "native"
            compat = tmp_path / "compat"
            native.mkdir()
            compat.mkdir()

            for filename, sections in quality.EXPECTED_WORKFLOWS.items():
                content = build_workflow_content(sections)
                (native / filename).write_text(content, encoding="utf-8")
                (compat / filename).write_text(content, encoding="utf-8")

            errors = quality.validate(native_dir=native, compat_dir=compat, min_lines=1)
            self.assertTrue(any("identical to compat baseline" in err for err in errors))


if __name__ == "__main__":
    unittest.main()


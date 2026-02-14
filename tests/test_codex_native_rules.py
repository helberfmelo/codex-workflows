from __future__ import annotations

import importlib.util
import pathlib
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "codex-workflows" / "scripts" / "check_codex_native_rules.py"


def load_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module


rules_check = load_module(SCRIPT, "check_codex_native_rules")


def write_rule(path: pathlib.Path, title: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = f"# {title}\n\nThis rule defines deterministic and evidence-based constraints for robust execution.\n"
    path.write_text(content, encoding="utf-8")


class CodexNativeRulesTests(unittest.TestCase):
    def test_real_repository_passes(self):
        native_root = ROOT / "skills" / "codex-workflows" / "templates" / "codex-native" / ".agent"
        errors = rules_check.validate_rules(native_root)
        self.assertEqual(errors, [])

    def test_detects_missing_workflow_rule(self):
        with tempfile.TemporaryDirectory() as tmp:
            native_root = pathlib.Path(tmp) / ".agent"
            write_rule(native_root / "rules" / "CODEX.md", "Entry")
            for idx in range(4):
                write_rule(native_root / "rules" / "global" / f"g{idx}.md", f"Global {idx}")
            for idx in range(6):
                write_rule(native_root / "rules" / "domains" / f"d{idx}.md", f"Domain {idx}")
            write_rule(native_root / "workflows" / "orchestrate.md", "Workflow spec")

            errors = rules_check.validate_rules(native_root)
            self.assertTrue(any("missing workflow rules" in err for err in errors))

    def test_detects_small_rule_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            native_root = pathlib.Path(tmp) / ".agent"
            write_rule(native_root / "workflows" / "plan.md", "Workflow spec")
            write_rule(native_root / "rules" / "workflows" / "plan.md", "Workflow rule")
            for idx in range(4):
                write_rule(native_root / "rules" / "global" / f"g{idx}.md", f"Global {idx}")
            for idx in range(6):
                write_rule(native_root / "rules" / "domains" / f"d{idx}.md", f"Domain {idx}")
            small = native_root / "rules" / "CODEX.md"
            small.parent.mkdir(parents=True, exist_ok=True)
            small.write_text("# tiny\n", encoding="utf-8")

            errors = rules_check.validate_rules(native_root)
            self.assertTrue(any("entry rule" in err for err in errors))


if __name__ == "__main__":
    unittest.main()

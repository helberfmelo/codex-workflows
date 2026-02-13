from __future__ import annotations

import importlib.util
import pathlib
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "codexwf.py"


def load_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module


codexwf = load_module(SCRIPT, "codexwf")


class CodexwfCliTests(unittest.TestCase):
    def test_locale_parity_counts_zero_missing(self):
        with tempfile.TemporaryDirectory() as tmp:
            docs = pathlib.Path(tmp)
            (docs / "reference").mkdir(parents=True, exist_ok=True)
            (docs / "reference" / "workflows.md").write_text("# x\n", encoding="utf-8")
            (docs / "get-started").mkdir(parents=True, exist_ok=True)
            (docs / "get-started" / "quickstart.md").write_text("# y\n", encoding="utf-8")
            for lang in ["pt", "es", "fr", "zh"]:
                (docs / lang / "reference").mkdir(parents=True, exist_ok=True)
                (docs / lang / "reference" / "workflows.md").write_text("# x\n", encoding="utf-8")
                (docs / lang / "get-started").mkdir(parents=True, exist_ok=True)
                (docs / lang / "get-started" / "quickstart.md").write_text("# y\n", encoding="utf-8")

            report = codexwf.locale_parity_counts(docs)
            self.assertEqual(report["en_count"], 2)
            for lang in ["pt", "es", "fr", "zh"]:
                self.assertEqual(report["locales"][lang]["missing"], 0)

    def test_parser_registers_expected_commands(self):
        parser = codexwf.build_parser()
        for argv in [
            ["status"],
            ["status", "--json"],
            ["validate"],
            ["validate", "--tests", "--docs"],
            ["init", "--project", ".", "--profile", "codex-native"],
            ["docs-sync", "--build"],
            ["install", "--dry-run"],
        ]:
            ns = parser.parse_args(argv)
            self.assertTrue(callable(ns.func))


if __name__ == "__main__":
    unittest.main()


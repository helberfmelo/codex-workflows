from __future__ import annotations

import importlib.util
import pathlib
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "codex-workflows" / "scripts" / "check_workflow_parity.py"


def load_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module


parity = load_module(SCRIPT, "check_workflow_parity")


def write_workflow(path: pathlib.Path, body: str) -> None:
    path.write_text(f"---\ndescription: x\n---\n\n# /x\n\n{body}\n", encoding="utf-8")


class WorkflowParityContractTests(unittest.TestCase):
    def test_real_repository_passes_split_contract(self):
        refs = ROOT / "skills" / "codex-workflows" / "references" / "workflows"
        native = ROOT / "skills" / "codex-workflows" / "templates" / "codex-native" / ".agent" / "workflows"
        template = ROOT / "skills" / "codex-workflows" / "templates" / ".agent" / "workflows"
        pack = ROOT / "skills" / "codex-workflows" / "packs" / "antigravity-compat" / ".agent" / "workflows"

        ref_map = parity.load_map(refs)
        native_map = parity.load_map(native)
        template_map = parity.load_map(template)
        pack_map = parity.load_map(pack)

        self.assertEqual(parity.check_pair("references", ref_map, "native", native_map), [])
        self.assertEqual(parity.check_pair("compat-template", template_map, "compat-pack", pack_map), [])

    def test_reference_native_mismatch_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = pathlib.Path(tmp)
            refs = tmp_path / "refs"
            native = tmp_path / "native"
            refs.mkdir()
            native.mkdir()
            write_workflow(refs / "plan.md", "reference")
            write_workflow(native / "plan.md", "native")
            errors = parity.check_pair("references", parity.load_map(refs), "native", parity.load_map(native))
            self.assertTrue(any("content mismatch" in err for err in errors))

    def test_compat_mismatch_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = pathlib.Path(tmp)
            template = tmp_path / "template"
            pack = tmp_path / "pack"
            template.mkdir()
            pack.mkdir()
            write_workflow(template / "debug.md", "template")
            write_workflow(pack / "debug.md", "pack")
            errors = parity.check_pair("compat-template", parity.load_map(template), "compat-pack", parity.load_map(pack))
            self.assertTrue(any("content mismatch" in err for err in errors))


if __name__ == "__main__":
    unittest.main()

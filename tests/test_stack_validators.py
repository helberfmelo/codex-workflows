from __future__ import annotations

import importlib.util
import pathlib
import tempfile
import unittest
from unittest import mock


ROOT = pathlib.Path(__file__).resolve().parents[1]


def load_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module


node_validator = load_module(
    ROOT / "skills" / "codex-node-validation-pack" / "scripts" / "validate_node_stack.py",
    "validate_node_stack",
)
python_validator = load_module(
    ROOT / "skills" / "codex-python-validation-pack" / "scripts" / "validate_python_stack.py",
    "validate_python_stack",
)
rust_validator = load_module(
    ROOT / "skills" / "codex-rust-validation-pack" / "scripts" / "validate_rust_stack.py",
    "validate_rust_stack",
)


class StackValidatorTests(unittest.TestCase):
    def test_node_detects_yarn_scripts(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = pathlib.Path(tmp)
            (project / "package.json").write_text(
                '{"scripts":{"lint":"eslint .","test":"vitest","build":"tsc -p tsconfig.json"}}',
                encoding="utf-8",
            )
            (project / "yarn.lock").write_text("lock", encoding="utf-8")
            checks = node_validator.build_checks(project)
            self.assertIn("yarn lint", checks)
            self.assertIn("yarn test", checks)
            self.assertIn("yarn build", checks)

    def test_python_builds_tool_aware_checks(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = pathlib.Path(tmp)
            (project / "tests").mkdir(parents=True)
            (project / "pyproject.toml").write_text(
                "\n".join(
                    [
                        "[tool.ruff]",
                        "line-length = 100",
                        "",
                        "[tool.black]",
                        "line-length = 100",
                        "",
                        "[tool.mypy]",
                        "python_version = \"3.12\"",
                        "",
                        "[tool.pytest.ini_options]",
                        "testpaths = [\"tests\"]",
                    ]
                ),
                encoding="utf-8",
            )
            checks = python_validator.build_checks(project)
            self.assertIn("python -m ruff check .", checks)
            self.assertIn("python -m black --check .", checks)
            self.assertIn("python -m mypy .", checks)
            self.assertIn("python -m pytest", checks)
            self.assertIn("python -m pip check", checks)

    def test_rust_includes_audit_when_available(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = pathlib.Path(tmp)
            (project / "Cargo.toml").write_text(
                "\n".join(
                    [
                        "[package]",
                        "name = \"demo\"",
                        "version = \"0.1.0\"",
                        "edition = \"2021\"",
                    ]
                ),
                encoding="utf-8",
            )
            (project / "Cargo.lock").write_text("# lock", encoding="utf-8")
            with mock.patch.object(rust_validator.shutil, "which", return_value="cargo-audit"):
                checks = rust_validator.build_checks(project)
            self.assertIn("cargo audit", checks)
            self.assertIn("cargo clippy --all-targets --all-features -- -D warnings", checks)


if __name__ == "__main__":
    unittest.main()

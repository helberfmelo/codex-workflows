from __future__ import annotations

import importlib.util
import pathlib
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


def load_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module


install_all = load_module(ROOT / "scripts" / "install_all_in_one.py", "install_all_in_one")


class InstallAllInOneTests(unittest.TestCase):
    def test_select_paths_to_install_skips_existing(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = pathlib.Path(tmp)
            (dest / "codex-workflows").mkdir()
            paths, skipped = install_all.select_paths_to_install(
                [
                    "skills/codex-workflows",
                    "skills/codex-backend-pack",
                ],
                dest,
            )
            self.assertEqual(paths, ["skills/codex-backend-pack"])
            self.assertEqual(skipped, ["codex-workflows"])

    def test_build_install_command_includes_paths_and_ref(self):
        cmd = install_all.build_install_command(
            python_exec="python",
            installer_script=pathlib.Path("/tmp/install.py"),
            repo="helberfmelo/codex-workflows",
            ref="main",
            method="auto",
            paths=["skills/codex-workflows", "skills/codex-qa-pack"],
            dest=pathlib.Path("/tmp/skills"),
        )
        self.assertIn("--path", cmd)
        self.assertIn("skills/codex-workflows", cmd)
        self.assertIn("skills/codex-qa-pack", cmd)
        self.assertIn("--ref", cmd)
        self.assertIn("main", cmd)
        self.assertIn("--dest", cmd)


if __name__ == "__main__":
    unittest.main()

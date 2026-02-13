from __future__ import annotations

import importlib.util
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


def load_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module


release_automation = load_module(ROOT / "scripts" / "release_automation.py", "release_automation")


class ReleaseAutomationTests(unittest.TestCase):
    def test_semver_validation(self):
        self.assertTrue(release_automation.is_semver("1.2.3"))
        self.assertTrue(release_automation.is_semver("1.2.3-rc.1"))
        self.assertFalse(release_automation.is_semver("v1.2.3"))
        self.assertFalse(release_automation.is_semver("1.2"))

    def test_cut_release_moves_unreleased_content(self):
        changelog = "\n".join(
            [
                "# Changelog",
                "",
                "## [Unreleased]",
                "",
                "### Added",
                "",
                "- New router mode",
                "",
                "## [1.0.0] - 2026-02-13",
                "",
                "### Added",
                "",
                "- Initial release",
                "",
            ]
        )
        new_text, notes = release_automation.cut_release(changelog, "1.1.0", "2026-02-14")
        self.assertIn("## [1.1.0] - 2026-02-14", new_text)
        self.assertIn("- New router mode", new_text)
        self.assertIn("## [Unreleased]\n\n### Added\n\n- Nothing yet.", new_text)
        self.assertIn("# Release v1.1.0", notes)

    def test_cut_release_rejects_existing_version(self):
        changelog = "\n".join(
            [
                "# Changelog",
                "",
                "## [Unreleased]",
                "",
                "### Added",
                "",
                "- New item",
                "",
                "## [1.1.0] - 2026-02-14",
            ]
        )
        with self.assertRaises(ValueError):
            release_automation.cut_release(changelog, "1.1.0", "2026-02-14")


if __name__ == "__main__":
    unittest.main()

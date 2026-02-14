from __future__ import annotations

import importlib.util
import pathlib
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "codex-workflows" / "scripts" / "build_compat_manifest.py"


def load_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module


manifest = load_module(SCRIPT, "build_compat_manifest")


class BuildCompatManifestTests(unittest.TestCase):
    def test_hash_file_normalizes_text_line_endings(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            lf_path = root / "lf.md"
            crlf_path = root / "crlf.md"
            lf_path.write_bytes(b"line-a\nline-b\n")
            crlf_path.write_bytes(b"line-a\r\nline-b\r\n")

            lf_hash, lf_size = manifest.hash_file(lf_path)
            crlf_hash, crlf_size = manifest.hash_file(crlf_path)

            self.assertEqual(lf_hash, crlf_hash)
            self.assertEqual(lf_size, crlf_size)
            self.assertEqual(lf_size, len(b"line-a\nline-b\n"))

    def test_hash_file_keeps_binary_payload_raw(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            bin_path = root / "data.bin"
            payload = b"\x00line-a\r\nline-b\r\n"
            bin_path.write_bytes(payload)

            file_hash, file_size = manifest.hash_file(bin_path)

            self.assertEqual(file_hash, manifest.hashlib.sha256(payload).hexdigest())
            self.assertEqual(file_size, len(payload))

    def test_collect_is_stable_for_lf_and_crlf_variants(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            a = root / "a"
            b = root / "b"
            (a / "workflows").mkdir(parents=True)
            (b / "workflows").mkdir(parents=True)
            (a / "workflows" / "plan.md").write_bytes(b"phase-1\nphase-2\n")
            (b / "workflows" / "plan.md").write_bytes(b"phase-1\r\nphase-2\r\n")

            self.assertEqual(manifest.collect(a), manifest.collect(b))


if __name__ == "__main__":
    unittest.main()

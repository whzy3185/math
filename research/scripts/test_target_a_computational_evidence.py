from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from verify_target_a_computational_evidence import DEFAULT_MANIFEST, ComputationalEvidenceError, verify


class ComputationalEvidenceTests(unittest.TestCase):
    def test_committed_manifest(self) -> None:
        self.assertEqual(verify()["status"], "PASS")

    def test_tampered_hash_is_rejected(self) -> None:
        payload = json.loads(DEFAULT_MANIFEST.read_text(encoding="utf-8"))
        payload["files"][0]["sha256"] = "0" * 64
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "manifest.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(ComputationalEvidenceError, "COMPUTE_HASH_FAIL"):
                verify(path)


if __name__ == "__main__":
    unittest.main()

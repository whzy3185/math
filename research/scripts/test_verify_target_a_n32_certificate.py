import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from verify_target_a_n32_certificate import (
    DEFAULT_CERTIFICATE,
    DEFAULT_WITNESS,
    N32CertificateError,
    verify_n32_certificate,
)


class N32CertificateVerifierTests(unittest.TestCase):
    def test_frozen_witness_passes(self) -> None:
        report = verify_n32_certificate()
        self.assertEqual(report["status"], "N32_COUNTEREXAMPLE_EXACT_PASS")
        self.assertEqual(report["positive_principal_minors"], 32)
        self.assertEqual(report["positive_ldl_pivots"], 32)

    def test_modified_witness_edge_sign_fails(self) -> None:
        witness = json.loads(DEFAULT_WITNESS.read_text(encoding="utf-8"))
        witness["step2"][0] *= -1
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "modified_witness.json"
            path.write_text(json.dumps(witness), encoding="utf-8")
            with self.assertRaisesRegex(N32CertificateError, "flux pattern mismatch"):
                verify_n32_certificate(path, DEFAULT_CERTIFICATE)


if __name__ == "__main__":
    unittest.main()

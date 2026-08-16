import json
import unittest
from pathlib import Path

from target_a_direct_generator_audit import audit_reference_equality


AUDIT = Path(__file__).resolve().parents[1] / "audit" / "target_a_n24_dual_generator_audit.json"


class N24DualGeneratorAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.expected = json.loads(AUDIT.read_text(encoding="utf-8"))

    def test_n24_ordered_streams_match(self):
        actual = audit_reference_equality(24)
        self.assertEqual(actual["status"], "PASS")
        self.assertEqual(actual["reference_q_bracelets"], self.expected["q_bracelets"])
        self.assertEqual(actual["production_q_bracelets"], self.expected["q_bracelets"])
        self.assertEqual(actual["spectral_states"], self.expected["spectral_states"])
        self.assertEqual(actual["represented_q_vectors"], self.expected["represented_q_vectors"])
        self.assertEqual(actual["represented_switching_classes"], self.expected["represented_switching_classes"])
        self.assertEqual(actual["reference_sha256"], self.expected["reference_sha256"])
        self.assertEqual(actual["production_sha256"], self.expected["production_sha256"])
        self.assertEqual(actual["first_mismatch"], self.expected["first_mismatch"])
        self.assertEqual(actual["checks"], self.expected["checks"])


if __name__ == "__main__":
    unittest.main()

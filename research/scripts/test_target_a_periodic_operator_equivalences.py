import copy
import json
import unittest

from verify_target_a_periodic_operator_equivalences import (
    DEFAULT_CERTIFICATE,
    PeriodicEquivalenceError,
    build_audit,
    lift,
    verify_certificate,
    verify_reflection,
    verify_translation,
    verify_zone_folding,
)


class PeriodicOperatorEquivalenceTests(unittest.TestCase):
    def test_full_audit_matches_certificate(self):
        certificate = json.loads(DEFAULT_CERTIFICATE.read_text(encoding="utf-8"))
        verify_certificate(certificate, build_audit())

    def test_target_doubled_cell_zone_folds(self):
        tau8 = (1, -1, 1, -1, -1, 1, -1, 1)
        self.assertEqual(verify_zone_folding(tau8 * 2, 8), 64)

    def test_translation_and_reflection(self):
        tau = lift((1, -1, -1, 1))
        verify_translation(tau, 3)
        verify_reflection(tau)

    def test_bad_certificate_rejected(self):
        actual = build_audit()
        bad = copy.deepcopy(actual)
        bad["repeated_words"] -= 1
        with self.assertRaises(PeriodicEquivalenceError):
            verify_certificate(bad, actual)

    def test_nonrepeated_zone_fold_rejected(self):
        with self.assertRaises(PeriodicEquivalenceError):
            verify_zone_folding((1, -1, 1, 1), 2)


if __name__ == "__main__":
    unittest.main()

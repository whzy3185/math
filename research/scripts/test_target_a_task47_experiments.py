from __future__ import annotations

import math
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

from target_a_task47_common import ETA, TARGET_Q, adaptive_radius_squared, canonical_q, primitive_period
from target_a_two_defect_geometry import run, two_defect_word
from target_a_finite_phase_slips import (
    _elementary_threshold_lower,
    _verify_rational_finite_bound,
    search_order,
    structured_seeds,
)
from target_a_high_period_moments_task47 import adaptive_first_positive, analyze_period
from target_a_high_period_certified_task47 import classify_candidate
from verify_target_a_task47 import verify


class Task47ExperimentTests(unittest.TestCase):
    def test_two_defect_canonicalization(self) -> None:
        q = two_defect_word(14, 5)
        self.assertEqual(math.prod(q), 1)
        self.assertEqual(canonical_q(q), canonical_q(tuple(reversed(q))))

    def test_period8_known_values(self) -> None:
        self.assertAlmostEqual(adaptive_radius_squared(TARGET_Q, 128)["value"], ETA, places=9)
        self.assertAlmostEqual(adaptive_radius_squared((-1,) * 8, 128)["value"], 8.0, places=9)
        self.assertGreater(adaptive_radius_squared(two_defect_word(8, 3), 128)["value"], 8.0)

    def test_zone_folded_target_recovery(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            payload = run(8, 16, 64, 4, Path(temporary))
        target_rows = [row for row in payload["records"] if row["repeated_target"]]
        self.assertEqual([(row["period"], row["separation"]) for row in target_rows], [(8, 4)])
        self.assertEqual(target_rows[0]["rigorous_certificate"]["status"], "CERTIFIED_R_EQ_ETA")

    def test_finite_seed_legality_and_positive_control(self) -> None:
        for family, q in structured_seeds(34):
            self.assertTrue(family.startswith("B"))
            self.assertEqual(math.prod(q), 1)
        result = search_order(32, beam_size=2, neighbor_limit=8, maximum_radius=2)
        self.assertLess(result["best"]["delta_squared"], 0)
        certificate = _verify_rational_finite_bound(
            {"n": 32, "alpha": result["best"]["alpha"], "quadrilaterals": list(TARGET_Q * 4)},
            Fraction(15609, 2000),
        )
        self.assertTrue(certificate["result"])
        self.assertGreater(_elementary_threshold_lower(34)[0], Fraction(39, 5))

    def test_known_moment_values_and_small_complete_partition(self) -> None:
        target = adaptive_first_positive(TARGET_Q, 10)
        self.assertIsNone(target["first_positive_k"])
        competitor = adaptive_first_positive(two_defect_word(8, 3), 10)
        self.assertIsNotNone(competitor["first_positive_k"])
        result = analyze_period((8, 8))
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["dihedral_orbits"], 18)

    def test_candidate_certification_sanity(self) -> None:
        target = classify_candidate({"period": 24, "canonical_q_code": sum((value == 1) << i for i, value in enumerate(TARGET_Q * 3))}, 128)
        self.assertEqual(target["classification"], "CERTIFIED_R_EQ_ETA")
        competitor_q = two_defect_word(18, 4)
        competitor = classify_candidate({"period": 18, "canonical_q_code": sum((value == 1) << i for i, value in enumerate(competitor_q))}, 128)
        self.assertEqual(competitor["classification"], "CERTIFIED_R_GT_ETA")

    def test_archived_task47_artifacts(self) -> None:
        report = verify()
        self.assertEqual(report["status"], "TARGET_A_TASK47_VERIFICATION_PASS")
        self.assertEqual(report["n22_spectral_states"], 97468)


if __name__ == "__main__":
    unittest.main()

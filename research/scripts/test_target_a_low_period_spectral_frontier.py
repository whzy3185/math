import copy
import hashlib
import json
import unittest

from target_a_low_period_spectral_frontier import (
    DEFAULT_RESULT,
    EXPECTED_ORBIT_COUNTS,
    canonical_q,
    is_target_phase,
    route_a_orbits,
    route_b_burnside,
    tau_lift,
    verify_bloch_identities,
    verify_geometric_equivalences,
)
from verify_target_a_low_period_spectral_frontier import (
    DEFAULT_SHARP,
    DEFAULT_SOURCE,
    LowPeriodVerificationError,
    _rational_gt_eta,
    verify_low_period_data,
)


class LowPeriodFrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = json.loads(DEFAULT_RESULT.read_text(encoding="utf-8"))
        cls.sharp_sha = hashlib.sha256(DEFAULT_SHARP.read_bytes()).hexdigest()
        cls.source_sha = hashlib.sha256(DEFAULT_SOURCE.read_bytes()).hexdigest()

    def verify(self, result=None, sharp_sha=None, source_sha=None):
        verify_low_period_data(
            self.result if result is None else result,
            self.sharp_sha if sharp_sha is None else sharp_sha,
            self.source_sha if source_sha is None else source_sha,
        )

    def assert_rejected(self, result=None, sharp_sha=None, source_sha=None):
        with self.assertRaises(LowPeriodVerificationError):
            self.verify(result, sharp_sha, source_sha)

    def test_positive_full_checker(self):
        self.verify()

    def test_two_orbit_routes_match_diagnostics(self):
        for p, expected in enumerate(EXPECTED_ORBIT_COUNTS, start=1):
            self.assertEqual(len(route_a_orbits(p)), expected)
            self.assertEqual(route_b_burnside(p)["orbit_count"], expected)

    def test_target_repetition_is_one_infinite_phase(self):
        target = canonical_q((1, -1, -1, -1) * 2)
        repeated = canonical_q((1, -1, -1, -1) * 4)
        self.assertTrue(is_target_phase(target, tau_lift(target)))
        self.assertTrue(is_target_phase(repeated, tau_lift(repeated)))
        self.assertEqual(self.result["target_repetition"]["representations"], ["P08-0006", "P16-0512"])

    def test_general_bloch_and_geometric_identities(self):
        for q in ((1,), (-1, -1, 1, 1), (1, -1, -1, -1, 1, -1, -1, -1)):
            tau = tau_lift(q)
            verify_bloch_identities(tau)
            verify_geometric_equivalences(q, tau)

    def test_certificate_partition(self):
        self.assertEqual(
            self.result["certificate_summary"],
            {
                "competitor_orbits": 2624,
                "Task42A_moment_excess": 1787,
                "endpoint_ternary_rayleigh": 824,
                "endpoint_small_integer_rayleigh": 13,
                "target_representations": 2,
                "uncertified": 0,
                "sturm_crosschecks": 24,
            },
        )

    def test_orbit_count_tamper_rejected(self):
        result = copy.deepcopy(self.result)
        result["phase_space"]["route_a_orbit_counts"][15] -= 1
        self.assert_rejected(result=result)

    def test_duplicate_canonical_representative_rejected(self):
        result = copy.deepcopy(self.result)
        rows = [row for row in result["orbits"] if row["p"] == 8]
        rows[1]["canonical_q_signs"] = rows[0]["canonical_q_signs"]
        rows[1]["canonical_q_bits"] = rows[0]["canonical_q_bits"]
        self.assert_rejected(result=result)

    def test_nondeterministic_orbit_id_rejected(self):
        result = copy.deepcopy(self.result)
        rows = [row for row in result["orbits"] if row["p"] == 8]
        rows[0]["orbit_id"], rows[1]["orbit_id"] = rows[1]["orbit_id"], rows[0]["orbit_id"]
        self.assert_rejected(result=result)

    def test_rayleigh_numerator_tamper_rejected(self):
        result = copy.deepcopy(self.result)
        row = next(row for row in result["orbits"] if row["exact_certificate"]["type"] == "EXACT_ENDPOINT_INTEGER_RAYLEIGH")
        row["exact_certificate"]["numerator"] += 1
        self.assert_rejected(result=result)

    def test_radical_comparison_rejects_lower_branch(self):
        # At r=0, u=3 and u^2>5; only the explicit r>4 guard rejects it.
        accepted, _ = _rational_gt_eta(0, 1)
        self.assertFalse(accepted)

    def test_moment_excess_tamper_rejected(self):
        result = copy.deepcopy(self.result)
        row = next(row for row in result["orbits"] if row["exact_certificate"]["type"] == "TASK42A_MOMENT_EXCESS")
        row["exact_certificate"]["value"] += 1
        self.assert_rejected(result=result)

    def test_primitive_period_tamper_rejected(self):
        result = copy.deepcopy(self.result)
        result["orbits"][100]["primitive_tau_period"] = 99
        self.assert_rejected(result=result)

    def test_fake_target_tie_rejected(self):
        result = copy.deepcopy(self.result)
        result["target_repetition"]["counted_as_distinct_minimizers"] = True
        self.assert_rejected(result=result)

    def test_sturm_polynomial_tamper_rejected(self):
        result = copy.deepcopy(self.result)
        result["sturm_crosschecks"][0]["squared_charpoly_coefficients"][-1] += 1
        self.assert_rejected(result=result)

    def test_numeric_preview_as_proof_rejected(self):
        result = copy.deepcopy(self.result)
        result["scope"]["numeric_previews_used_as_proof"] = True
        self.assert_rejected(result=result)

    def test_all_period_overclaim_rejected(self):
        result = copy.deepcopy(self.result)
        result["scope"]["all_period_global_optimality"] = "PROVED"
        self.assert_rejected(result=result)

    def test_dependency_sha_tamper_rejected(self):
        self.assert_rejected(sharp_sha="0" * 64)

    def test_source_sha_tamper_rejected(self):
        self.assert_rejected(source_sha="0" * 64)


if __name__ == "__main__":
    unittest.main()

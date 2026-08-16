import copy
import hashlib
import json
import unittest

import sympy as sp

from target_a_period8_pattern_classification import (
    ALL_UNBALANCED_Q,
    TARGET_Q,
    bloch_matrix,
    canonical_q,
    legal_q_vectors,
    primitive_period,
    raw_tau_fiber_audit,
    route_a_orbits,
    route_b_burnside,
    tau_lift,
)
from verify_target_a_period8_pattern_classification import (
    DEFAULT_AUDIT,
    DEFAULT_RESULT,
    DEFAULT_SHARP,
    DEFAULT_SOURCE,
    ClassificationVerificationError,
    verify_classification_data,
)


class Period8PatternClassificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = json.loads(DEFAULT_RESULT.read_text(encoding="utf-8"))
        cls.audit = json.loads(DEFAULT_AUDIT.read_text(encoding="utf-8"))
        sharp_bytes = DEFAULT_SHARP.read_bytes()
        cls.sharp = json.loads(sharp_bytes)
        cls.sharp_sha = hashlib.sha256(sharp_bytes).hexdigest()
        cls.source_sha = hashlib.sha256(DEFAULT_SOURCE.read_bytes()).hexdigest()

    def verify(self, result=None, audit=None, sharp_sha=None):
        verify_classification_data(
            self.result if result is None else result,
            self.audit if audit is None else audit,
            self.sharp,
            self.sharp_sha if sharp_sha is None else sharp_sha,
            self.source_sha,
        )

    def assert_rejected(self, result=None, audit=None, sharp_sha=None):
        with self.assertRaises(ClassificationVerificationError):
            self.verify(result, audit, sharp_sha)

    def test_positive_full_checker(self):
        self.verify()

    def test_phase_space_is_derived(self):
        fibers = raw_tau_fiber_audit()
        self.assertEqual(fibers["raw_tau_count"], 256)
        self.assertEqual(fibers["distinct_q_count"], 128)
        self.assertEqual(fibers["lifts_per_q"], [2])
        self.assertEqual(len(legal_q_vectors()), 128)

    def test_enumeration_routes_agree(self):
        route_a = route_a_orbits()
        route_b = route_b_burnside()
        self.assertEqual(len(route_a), route_b["orbit_count"])
        self.assertEqual(route_b["shell_orbit_counts"], {"0": 1, "2": 4, "4": 8, "6": 4, "8": 1})

    def test_target_period_doubling(self):
        canonical = canonical_q(TARGET_Q)
        tau = tau_lift(canonical)
        self.assertEqual(primitive_period(canonical), 4)
        self.assertEqual(primitive_period(tau), 8)

    def test_all_unbalanced_square_has_eight_attainment(self):
        tau = tau_lift(ALL_UNBALANCED_Q)
        matrix = bloch_matrix(tau, sp.Integer(1))
        vector = sp.Matrix([-1] * 8)
        self.assertEqual((vector.T * matrix**2 * vector)[0], 8 * (vector.T * vector)[0])

    def test_delete_orbit_rejected(self):
        result = copy.deepcopy(self.result)
        result["orbits"].pop()
        self.assert_rejected(result=result)

    def test_duplicate_orbit_rejected(self):
        result = copy.deepcopy(self.result)
        result["orbits"][-1] = copy.deepcopy(result["orbits"][0])
        self.assert_rejected(result=result)

    def test_wrong_orbit_count_rejected(self):
        result = copy.deepcopy(self.result)
        result["phase_space"]["d8_orbit_count"] = 17
        self.assert_rejected(result=result)

    def test_wrong_shell_count_rejected(self):
        result = copy.deepcopy(self.result)
        result["phase_space"]["shell_counts"]["4"] = 7
        self.assert_rejected(result=result)

    def test_wrong_orbit_size_rejected(self):
        result = copy.deepcopy(self.result)
        result["orbits"][1]["orbit_size"] = 4
        self.assert_rejected(result=result)

    def test_wrong_reflection_canonicalization_rejected(self):
        result = copy.deepcopy(self.result)
        target = next(row for row in result["orbits"] if row["target_phase"])
        target["canonical_q_bits"] = "00100010"
        self.assert_rejected(result=result)

    def test_rotated_target_recognition_failure_rejected(self):
        result = copy.deepcopy(self.result)
        target = next(row for row in result["orbits"] if row["target_phase"])
        target["target_phase"] = False
        self.assert_rejected(result=result)

    def test_broken_tau_closure_rejected(self):
        result = copy.deepcopy(self.result)
        result["orbits"][2]["tau_lift_tau0_plus"][-1] *= -1
        self.assert_rejected(result=result)

    def test_wrong_tau_to_q_reconstruction_rejected(self):
        result = copy.deepcopy(self.result)
        result["orbits"][3]["canonical_q_signs"][0] *= -1
        self.assert_rejected(result=result)

    def test_modified_rayleigh_vector_rejected(self):
        result = copy.deepcopy(self.result)
        certificate = result["orbits"][1]["exact_lower_certificate"]
        certificate["vector"][0] += 1
        self.assert_rejected(result=result)

    def test_modified_rayleigh_numerator_rejected(self):
        result = copy.deepcopy(self.result)
        result["orbits"][1]["exact_lower_certificate"]["numerator"] += 1
        self.assert_rejected(result=result)

    def test_modified_rayleigh_denominator_rejected(self):
        result = copy.deepcopy(self.result)
        result["orbits"][1]["exact_lower_certificate"]["denominator"] += 1
        self.assert_rejected(result=result)

    def test_false_rayleigh_comparison_rejected(self):
        result = copy.deepcopy(self.result)
        result["orbits"][1]["exact_lower_certificate"]["comparison_to_8"] = "<"
        self.assert_rejected(result=result)

    def test_runner_lower_bound_mislabeled_exact_rejected(self):
        audit = copy.deepcopy(self.audit)
        audit["all_unbalanced_exact_certificate"]["status"] = "LOWER_BOUND_ONLY"
        self.assert_rejected(audit=audit)

    def test_better_competitor_with_unique_claim_rejected(self):
        result = copy.deepcopy(self.result)
        result["ranking"]["classes_better_than_target"] = ["P8-02"]
        self.assert_rejected(result=result)

    def test_tie_with_unique_claim_rejected(self):
        result = copy.deepcopy(self.result)
        result["ranking"]["ties_with_target"] = ["P8-03"]
        self.assert_rejected(result=result)

    def test_modified_task40a_sha_rejected(self):
        self.assert_rejected(sharp_sha="0" * 64)

    def test_finite_size_overclaim_rejected(self):
        result = copy.deepcopy(self.result)
        result["scope_boundary"]["finite_size_global_optimality"] = "PROVED"
        self.assert_rejected(result=result)

    def test_all_period_overclaim_rejected(self):
        result = copy.deepcopy(self.result)
        result["scope_boundary"]["all_period_global_optimality"] = "PROVED"
        self.assert_rejected(result=result)

    def test_all_signings_overclaim_rejected(self):
        result = copy.deepcopy(self.result)
        result["scope_boundary"]["all_signings_global_optimality"] = "PROVED"
        self.assert_rejected(result=result)


if __name__ == "__main__":
    unittest.main()

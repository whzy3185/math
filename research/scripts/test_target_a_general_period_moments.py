import copy
import hashlib
import json
import unittest

from target_a_general_period_moments import (
    DEFAULT_RESULT,
    closed_walk_moments,
    closed_walk_q_expansion,
    defect_statistics,
    derive_general_a2_formula,
    formula_moments,
    laurent_constant_term_moments,
    tau_lift,
)
from verify_target_a_general_period_moments import (
    DEFAULT_SOURCE,
    GeneralPeriodVerificationError,
    verify_general_period_data,
)


class GeneralPeriodMomentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = json.loads(DEFAULT_RESULT.read_text(encoding="utf-8"))
        cls.source_sha = hashlib.sha256(DEFAULT_SOURCE.read_bytes()).hexdigest()

    def verify(self, result=None, source_sha=None):
        verify_general_period_data(
            self.result if result is None else result,
            self.source_sha if source_sha is None else source_sha,
        )

    def assert_rejected(self, result=None, source_sha=None):
        with self.assertRaises(GeneralPeriodVerificationError):
            self.verify(result, source_sha)

    def test_positive_full_checker(self):
        self.verify()

    def test_short_period_degeneracies(self):
        for q in ((1,), (-1, -1), (1, 1), (-1, -1, 1, 1)):
            self.assertEqual(closed_walk_moments(q), formula_moments(q))

    def test_general_a2_formula(self):
        proof = derive_general_a2_formula()
        self.assertEqual(proof["checked_tau_words"], 510)
        self.assertEqual(proof["checked_rows"], 3586)

    def test_symbolic_walk_coefficients(self):
        self.assertEqual(
            closed_walk_q_expansion(6)["translation_class_coefficients"],
            {"const": 238, "0": 156, "0,1": 24, "0,2": 12},
        )

    def test_laurent_constant_term_route(self):
        q = (1, -1, -1, 1, -1, -1)
        self.assertEqual(laurent_constant_term_moments(q), closed_walk_moments(q))

    def test_tau_flip_has_same_moments(self):
        q = (1, -1, -1, -1, 1, -1, -1, -1)
        tau = tau_lift(q)
        self.assertEqual(tau_lift(q), tau)
        self.assertEqual(closed_walk_moments(q), [32, 192, 1280])

    def test_cyclic_statistics_at_small_period(self):
        self.assertEqual(defect_statistics((1,)), {"d": 1, "a": 1, "b": 1})
        self.assertEqual(defect_statistics((-1, -1)), {"d": 0, "a": 0, "b": 0})

    def test_corrupt_m3_coefficient_rejected(self):
        result = copy.deepcopy(self.result)
        result["moment_identities"]["defect_basis_identities"]["M3"] = "118*p+168*d+95*a+48*b"
        self.assert_rejected(result=result)

    def test_corrupt_raw_expansion_rejected(self):
        result = copy.deepcopy(self.result)
        result["moment_identities"]["expansions"][2]["raw_coefficients"]["-3"] += 1
        self.assert_rejected(result=result)

    def test_wrong_density_direction_rejected(self):
        result = copy.deepcopy(self.result)
        result["obstructions"]["density_necessary_condition"] = "d<=3*p/4 implies R(Q)<=8"
        self.assert_rejected(result=result)

    def test_nonpositive_excess_overclaim_rejected(self):
        result = copy.deepcopy(self.result)
        result["obstructions"]["logical_limits"]["nonpositive_excess_proves_R_le_8"] = True
        self.assert_rejected(result=result)

    def test_sufficiency_overclaim_rejected(self):
        result = copy.deepcopy(self.result)
        result["scope"]["conditions_sufficient_for_sub_eight"] = "PROVED"
        self.assert_rejected(result=result)

    def test_global_optimality_overclaim_rejected(self):
        result = copy.deepcopy(self.result)
        result["scope"]["all_period_global_optimality"] = "PROVED"
        self.assert_rejected(result=result)

    def test_numerical_quadrature_rejected(self):
        result = copy.deepcopy(self.result)
        result["machine_checks"]["arithmetic"] = "numerical quadrature"
        self.assert_rejected(result=result)

    def test_source_hash_tamper_rejected(self):
        self.assert_rejected(source_sha="0" * 64)


if __name__ == "__main__":
    unittest.main()

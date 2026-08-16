import copy
import hashlib
import json
import unittest

from target_a_period8_structural_mechanism import (
    TARGET_Q,
    canonical_q,
    closed_walk_moments,
    cyclic_separation,
    defect_statistics,
    derive_a2_local_formula,
    derive_moment_formulas,
    d2_moment_hierarchy,
    high_defect_proof,
    target_chiral_symmetry,
    tau_lift,
)
from verify_target_a_period8_structural_mechanism import (
    DEFAULT_CLASSIFICATION,
    DEFAULT_CLASSIFICATION_AUDIT,
    DEFAULT_RESULT,
    DEFAULT_SHARP,
    DEFAULT_SOURCE,
    StructuralVerificationError,
    verify_structural_data,
)


class Period8StructuralMechanismTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = json.loads(DEFAULT_RESULT.read_text(encoding="utf-8"))
        cls.sharp_bytes = DEFAULT_SHARP.read_bytes()
        cls.classification_bytes = DEFAULT_CLASSIFICATION.read_bytes()
        cls.audit_bytes = DEFAULT_CLASSIFICATION_AUDIT.read_bytes()
        cls.sharp = json.loads(cls.sharp_bytes)
        cls.classification = json.loads(cls.classification_bytes)
        cls.audit = json.loads(cls.audit_bytes)
        cls.hashes = {
            "sharp": hashlib.sha256(cls.sharp_bytes).hexdigest(),
            "classification": hashlib.sha256(cls.classification_bytes).hexdigest(),
            "classification_audit": hashlib.sha256(cls.audit_bytes).hexdigest(),
        }
        cls.source_sha = hashlib.sha256(DEFAULT_SOURCE.read_bytes()).hexdigest()

    def verify(self, result=None, classification=None, hashes=None):
        verify_structural_data(
            self.result if result is None else result,
            self.sharp,
            self.classification if classification is None else classification,
            self.audit,
            self.hashes if hashes is None else hashes,
            self.source_sha,
        )

    def assert_rejected(self, result=None, classification=None, hashes=None):
        with self.assertRaises(StructuralVerificationError):
            self.verify(result, classification, hashes)

    def test_positive_full_checker(self):
        self.verify()

    def test_a2_formula_derives_from_all_tau_words(self):
        formula = derive_a2_local_formula()
        self.assertEqual(formula["status"], "FLUX_SQUARE_LOCAL_FORMULA_PASS")
        self.assertEqual(formula["cancelled_odd_coupling_checks"], 4096)
        self.assertEqual(formula["activated_odd_coupling_checks"], 4096)

    def test_moment_formulas_are_derived(self):
        formulas = derive_moment_formulas()
        self.assertEqual(formulas["M2_coefficients_automatically_derived"], [160, 16])
        self.assertEqual(formulas["M3_coefficients_automatically_derived"], [944, 168, 96, 48])

    def test_high_defect_proof(self):
        proof = high_defect_proof()
        self.assertEqual(proof["d4"]["F2_lower_bound"], 16)
        self.assertEqual(proof["d6"]["F2_lower_bound"], 288)
        self.assertEqual(proof["d8"]["F1_value"], 32)

    def test_d2_exact_hierarchy(self):
        hierarchy = d2_moment_hierarchy()
        self.assertEqual(hierarchy["first_positive_indices_for_s1_s2_s3"], [4, 6, 9])
        self.assertIsNone(hierarchy["rows"][3]["first_positive_F_index"])

    def test_target_chiral_data(self):
        target = canonical_q(TARGET_Q)
        self.assertEqual(cyclic_separation(target), 4)
        self.assertEqual(defect_statistics(target)["d"], 2)
        self.assertEqual(tau_lift(target), (1, -1, 1, -1, -1, 1, -1, 1))
        self.assertEqual(target_chiral_symmetry()["J_squared"], "I")

    def test_closed_walk_dynamics_is_exact(self):
        target = canonical_q(TARGET_Q)
        self.assertEqual(closed_walk_moments(target, 3), [32, 192, 1280])

    def test_flip_a2_index_rejected(self):
        result = copy.deepcopy(self.result)
        result["A2_local_formula"]["coefficients_by_displacement"]["+1"] = "tau_i*(1+Q_i)"
        self.assert_rejected(result=result)

    def test_negative_q_marked_activated_rejected(self):
        result = copy.deepcopy(self.result)
        result["A2_local_formula"]["interpretation"] = "Q=-1 activates odd-distance coupling"
        self.assert_rejected(result=result)

    def test_corrupt_m2_coefficient_rejected(self):
        result = copy.deepcopy(self.result)
        result["moment_framework"]["M2_coefficients_automatically_derived"][1] = 15
        self.assert_rejected(result=result)

    def test_corrupt_m3_coefficient_rejected(self):
        result = copy.deepcopy(self.result)
        result["moment_framework"]["M3_coefficients_automatically_derived"][2] = 95
        self.assert_rejected(result=result)

    def test_numerical_quadrature_rejected(self):
        result = copy.deepcopy(self.result)
        result["moment_framework"]["constant_term_method"] = "numerical quadrature"
        self.assert_rejected(result=result)

    def test_negative_excess_used_as_upper_bound_rejected(self):
        result = copy.deepcopy(self.result)
        result["moment_framework"]["negative_F_not_sufficient_for_upper_bound"] = False
        self.assert_rejected(result=result)

    def test_first_ten_moments_used_for_target_rejected(self):
        result = copy.deepcopy(self.result)
        result["moment_framework"]["finite_moments_do_not_prove_target_bound"] = False
        self.assert_rejected(result=result)

    def test_wrong_d2_separation_rejected(self):
        result = copy.deepcopy(self.result)
        result["d2_separation_table"]["rows"][1]["separation"] = 3
        self.assert_rejected(result=result)

    def test_wrong_first_positive_moment_rejected(self):
        result = copy.deepcopy(self.result)
        result["d2_separation_table"]["rows"][2]["first_positive_F_index"] = 8
        self.assert_rejected(result=result)

    def test_corrupt_target_antiperiodicity_rejected(self):
        result = copy.deepcopy(self.result)
        result["target_symmetry"]["tau"][-1] *= -1
        self.assert_rejected(result=result)

    def test_false_j_square_rejected(self):
        result = copy.deepcopy(self.result)
        result["target_symmetry"]["J_squared"] = "not I"
        self.assert_rejected(result=result)

    def test_false_chiral_anticommutation_rejected(self):
        result = copy.deepcopy(self.result)
        result["target_symmetry"]["anticommutation"] = "mismatch but marked PASS"
        self.assert_rejected(result=result)

    def test_chiral_symmetry_alone_claimed_optimal_rejected(self):
        result = copy.deepcopy(self.result)
        result["antiperiod4_classification"]["mechanism_boundary"] = "every anti-period4 phase is optimal"
        self.assert_rejected(result=result)

    def test_omitted_q_from_trichotomy_rejected(self):
        result = copy.deepcopy(self.result)
        result["task40b_crosscheck"]["legal_q_compared"] = 127
        self.assert_rejected(result=result)

    def test_all_unbalanced_below_eight_rejected(self):
        result = copy.deepcopy(self.result)
        result["all_unbalanced_baseline"]["sharp_squared_constant"] = "7"
        self.assert_rejected(result=result)

    def test_non_target_d2_sub_eight_rejected(self):
        result = copy.deepcopy(self.result)
        result["d2_separation_table"]["rows"][0]["conclusion"] = "Task 40A gives R=eta<8"
        self.assert_rejected(result=result)

    def test_task40b_disagreement_ignored_rejected(self):
        result = copy.deepcopy(self.result)
        result["task40b_crosscheck"]["mismatch_count"] = 1
        self.assert_rejected(result=result)

    def test_dependency_sha_tamper_rejected(self):
        hashes = copy.deepcopy(self.hashes)
        hashes["classification"] = "0" * 64
        self.assert_rejected(hashes=hashes)

    def test_all_period_overclaim_rejected(self):
        result = copy.deepcopy(self.result)
        result["scope"]["all_period_global_optimality"] = "PROVED"
        self.assert_rejected(result=result)

    def test_finite_global_overclaim_rejected(self):
        result = copy.deepcopy(self.result)
        result["scope"]["finite_size_global_optimality"] = "PROVED"
        self.assert_rejected(result=result)

    def test_all_signings_overclaim_rejected(self):
        result = copy.deepcopy(self.result)
        result["scope"]["all_signings_global_optimality"] = "PROVED"
        self.assert_rejected(result=result)


if __name__ == "__main__":
    unittest.main()

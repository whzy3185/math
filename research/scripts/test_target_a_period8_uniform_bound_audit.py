import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))

from target_a_period8_uniform_bound_audit import (
    ALPHA_VALUES,
    BOUND,
    DEFAULT_FLOQUET_AUDIT,
    DEFAULT_POLYNOMIAL_SNAPSHOT,
    UniformBoundAuditError,
    algebraic_n32_threshold_certificate,
    load_floquet_dependency,
    positive_coefficient_certificate,
    run_independent_audit,
    spectral_implication,
    taylor_threshold_crosscheck,
    threshold_above_bound,
    threshold_formula_from_spec,
    threshold_monotonicity_certificate,
    validate_alpha_coverage,
    validate_family_domain,
    validate_positive_coefficient_map,
    vertex_crosscheck,
)
from verify_target_a_period8_infinite_family import verify_infinite_family


N_RULE = "n=8L with integer L>=4"
THEOREM = (
    "For every integer L>=4 and alpha in {-1,+1}, the period-8 signing on "
    "C_(8L)(1,2) satisfies rho(A)^2 < 1561/200 < rho_-(8L)^2."
)


class IndependentUniformBoundAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.dependency = load_floquet_dependency()
        cls.polynomial = cls.dependency["polynomial"]
        cls.y = cls.dependency["y"]
        cls.c = cls.dependency["c"]
        cls.positivity = positive_coefficient_certificate(
            cls.polynomial, cls.y, cls.c
        )
        cls.vertex = vertex_crosscheck(cls.polynomial, cls.y, cls.c)
        cls.formula = threshold_formula_from_spec()
        cls.threshold = algebraic_n32_threshold_certificate(
            cls.formula["expression"], cls.formula["n_symbol"]
        )
        cls.directory = tempfile.TemporaryDirectory()
        root = Path(cls.directory.name)
        cls.audit = run_independent_audit(
            positivity_snapshot_path=root / "positivity.json",
            audit_path=root / "audit.json",
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.directory.cleanup()

    def test_01_task38_dependency_hashes_and_status_pass(self) -> None:
        self.assertEqual(
            self.dependency["audit"]["status"],
            "PERIOD8_FLOQUET_DETERMINANT_INDEPENDENTLY_AUDITED",
        )
        self.assertEqual(
            self.dependency["snapshot"]["status"],
            "PERIOD8_INDEPENDENT_POLYNOMIAL_FROZEN",
        )

    def test_02_polynomial_is_reconstructed_from_coefficient_map(self) -> None:
        self.assertEqual(sp.Poly(self.polynomial, self.y, self.c).degree(self.y), 4)
        self.assertEqual(sp.Poly(self.polynomial, self.y, self.c).degree(self.c), 2)

    def test_03_positive_coefficient_certificate_passes(self) -> None:
        self.assertEqual(
            self.positivity["status"], "POSITIVE_COEFFICIENT_CERTIFICATE_PASS"
        )
        self.assertTrue(self.positivity["all_coefficients_nonnegative"])
        self.assertTrue(self.positivity["strict_positive_constant"])

    def test_04_positive_expansion_has_expected_derived_coefficients(self) -> None:
        coefficients = {
            (row["u_degree"], row["t_degree"]): sp.Rational(row["coefficient"])
            for row in self.positivity["monomial_coefficient_map"]
        }
        self.assertEqual(coefficients[(2, 1)], 2)
        self.assertEqual(coefficients[(0, 1)], sp.Rational(119121, 20000))
        self.assertEqual(coefficients[(0, 0)], sp.Rational(84332641, 1600000000))

    def test_05_certificate_proves_stronger_region(self) -> None:
        self.assertIn("c<=2", self.positivity["proved_region"])

    def test_06_vertex_crosscheck_passes(self) -> None:
        self.assertEqual(self.vertex["status"], "VERTEX_CROSSCHECK_PASS")
        self.assertEqual(self.vertex["vertex_at_B"], "199121/40000")
        self.assertTrue(self.vertex["all_boundary_coefficients_positive"])

    def test_07_spectral_implication_is_strict(self) -> None:
        report = spectral_implication(self.dependency, self.positivity)
        self.assertEqual(report["status"], "UNIFORM_SPECTRAL_BOUND_PASS")
        self.assertIn("< 1561/200", report["strict_full_bound"])

    def test_08_threshold_formula_is_derived_from_spec(self) -> None:
        self.assertEqual(
            self.formula["squared_formula"],
            "2*cos(2*pi/n) + 2*cos(4*pi/n) + 4",
        )
        self.assertTrue(all(self.formula["identity_checks"]))

    def test_09_n32_radical_and_minimal_polynomial_pass(self) -> None:
        self.assertEqual(self.threshold["status"], "N32_THRESHOLD_ALGEBRAIC_PASS")
        self.assertTrue(self.threshold["formula_equals_radical_exactly"])
        self.assertEqual(self.threshold["minimal_polynomial_coefficients"][0], "1")
        self.assertEqual(self.threshold["minimal_polynomial_coefficients"][-1], "25022")

    def test_10_n32_sturm_interval_is_exact(self) -> None:
        self.assertEqual(
            self.threshold["isolating_interval"],
            {"lower": "7809/1000", "upper": "781/100"},
        )
        self.assertEqual(self.threshold["root_count"], 1)
        self.assertTrue(self.threshold["radical_in_interval_exact"])
        self.assertTrue(self.threshold["B_below_lower"])

    def test_11_threshold_monotonicity_passes(self) -> None:
        report = threshold_monotonicity_certificate()
        self.assertEqual(report["status"], "THRESHOLD_MONOTONICITY_PASS")
        self.assertTrue(report["strictly_increasing"])

    def test_12_taylor_crosscheck_rederives_rational_lower(self) -> None:
        report = taylor_threshold_crosscheck()
        self.assertEqual(report["status"], "TAYLOR_THRESHOLD_CROSSCHECK_PASS")
        self.assertEqual(
            report["threshold_squared_rational_lower"],
            "1178731111/150994944",
        )

    def test_13_family_domain_and_both_holonomies_pass(self) -> None:
        self.assertTrue(validate_family_domain(4, ALPHA_VALUES, N_RULE, THEOREM))
        self.assertTrue(validate_alpha_coverage(ALPHA_VALUES))

    def test_14_complete_audit_has_final_status(self) -> None:
        self.assertEqual(
            self.audit["status"],
            "PERIOD8_INFINITE_FAMILY_INDEPENDENTLY_AUDITED",
        )
        self.assertEqual(
            self.audit["checker"]["status"],
            "TARGET_A_PERIOD8_INFINITE_FAMILY_PASS",
        )

    def test_15_frozen_infinite_family_checker_passes(self) -> None:
        report = verify_infinite_family()
        self.assertEqual(report["status"], "TARGET_A_PERIOD8_INFINITE_FAMILY_PASS")

    def test_16_altered_P_coefficient_fails_dependency(self) -> None:
        data = json.loads(DEFAULT_POLYNOMIAL_SNAPSHOT.read_text(encoding="utf-8"))
        data["P_independent_coefficient_map"][0]["coefficient"] = "2"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "polynomial.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(UniformBoundAuditError, "FLOQUET_DEPENDENCY_FAIL"):
                load_floquet_dependency(polynomial_snapshot_path=path)

    def test_17_negative_constant_fails_positivity_certificate(self) -> None:
        rows = copy.deepcopy(self.positivity["monomial_coefficient_map"])
        constant = next(
            row for row in rows if row["u_degree"] == 0 and row["t_degree"] == 0
        )
        constant["coefficient"] = "-1"
        with self.assertRaisesRegex(
            UniformBoundAuditError, "POSITIVE_COEFFICIENT_CERTIFICATE_FAIL"
        ):
            validate_positive_coefficient_map(rows)

    def test_18_starting_at_L3_fails_threshold_theorem(self) -> None:
        self.assertFalse(validate_family_domain(3, ALPHA_VALUES, N_RULE, THEOREM))
        self.assertFalse(threshold_above_bound(24))

    def test_19_n30_is_not_in_the_certified_threshold_range(self) -> None:
        self.assertFalse(threshold_above_bound(30))

    def test_20_corrupted_task38_audit_sha_fails_dependency(self) -> None:
        data = json.loads(DEFAULT_FLOQUET_AUDIT.read_text(encoding="utf-8"))
        data["hermitian_check"] = False
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "floquet.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(UniformBoundAuditError, "FLOQUET_DEPENDENCY_FAIL"):
                load_floquet_dependency(audit_path=path)

    def test_21_missing_alpha_minus_fails_family_completeness(self) -> None:
        self.assertFalse(validate_alpha_coverage([1]))
        self.assertFalse(validate_family_domain(4, [1], N_RULE, THEOREM))

    def test_22_empty_root_interval_fails_algebraic_threshold(self) -> None:
        with self.assertRaisesRegex(UniformBoundAuditError, "isolat|endpoint"):
            algebraic_n32_threshold_certificate(
                self.formula["expression"],
                self.formula["n_symbol"],
                sp.Rational(7),
                sp.Rational(71, 10),
            )

    def test_23_all_even_claim_fails_domain_validation(self) -> None:
        overbroad = "For all even n>=32 the period-8 family is a counterexample."
        self.assertFalse(validate_family_domain(4, ALPHA_VALUES, N_RULE, overbroad))


if __name__ == "__main__":
    unittest.main()

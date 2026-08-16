import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))

from target_a_period8_sharp_constant import (
    DEFAULT_FAMILY,
    DEFAULT_RESULT,
    OLD_BOUND,
    SharpConstantError,
    derive_endpoint_candidate,
    global_band_edge_certificate,
    holonomy_consequences,
    load_dependencies,
    old_bound_comparison,
    run_sharp_constant_proof,
    sharp_positivity_certificate,
    top_root_monotonicity_certificate,
    validate_band_edge_claim,
    validate_candidate_is_largest,
    validate_sharp_bound_claim,
    validate_sharp_coefficient_map,
)
from verify_target_a_period8_sharp_constant import (
    SharpConstantVerificationError,
    verify_sharp_constant,
)


class Period8SharpConstantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.dependency = load_dependencies()
        cls.P = cls.dependency["P"]
        cls.y = cls.dependency["y"]
        cls.c = cls.dependency["c"]
        cls.endpoint = derive_endpoint_candidate(cls.P, cls.y, cls.c)
        cls.eta = cls.endpoint["eta"]
        cls.rho = cls.endpoint["rho_star"]
        cls.positivity = sharp_positivity_certificate(
            cls.P, cls.y, cls.c, cls.eta
        )
        cls.band = global_band_edge_certificate(
            cls.P, cls.y, cls.c, cls.eta, cls.positivity
        )
        cls.monotonicity = top_root_monotonicity_certificate(
            cls.P, cls.y, cls.c
        )
        cls.holonomies = holonomy_consequences(
            cls.P, cls.y, cls.c, cls.eta, cls.monotonicity
        )
        cls.directory = tempfile.TemporaryDirectory()
        cls.temp_result = Path(cls.directory.name) / "result.json"
        cls.result = run_sharp_constant_proof(result_path=cls.temp_result)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.directory.cleanup()

    def _modified_result_fails(self, mutate, pattern: str) -> None:
        data = json.loads(DEFAULT_RESULT.read_text(encoding="utf-8"))
        mutate(data)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "result.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(SharpConstantVerificationError, pattern):
                verify_sharp_constant(result_path=path)

    def test_01_dependencies_are_pinned_and_audited(self) -> None:
        self.assertEqual(
            self.dependency["floquet"]["status"],
            "PERIOD8_FLOQUET_DETERMINANT_INDEPENDENTLY_AUDITED",
        )
        self.assertEqual(
            self.dependency["family"]["status"],
            "PERIOD8_INFINITE_FAMILY_INDEPENDENTLY_AUDITED",
        )

    def test_02_endpoint_translation_is_biquadratic(self) -> None:
        self.assertEqual(
            self.endpoint["translated_polynomial"], "x**4 - 20*x**2 + 80"
        )
        self.assertEqual(self.endpoint["w_polynomial"], "w**2 - 20*w + 80")

    def test_03_eta_is_largest_exact_endpoint_root(self) -> None:
        roots = [sp.sympify(value) for value in self.endpoint["ordered_endpoint_roots"]]
        self.assertTrue(validate_candidate_is_largest(self.eta, roots))
        self.assertEqual(
            sp.simplify(self.eta - (4 + sp.sqrt(10 + 2 * sp.sqrt(5)))), 0
        )

    def test_04_eta_minimal_polynomial_and_interval_pass(self) -> None:
        self.assertEqual(
            self.endpoint["eta_minimal_polynomial"],
            "Y**4 - 16*Y**3 + 76*Y**2 - 96*Y + 16",
        )
        self.assertEqual(
            self.endpoint["eta_isolating_interval"],
            {"lower": "1951/250", "upper": "1561/200"},
        )

    def test_05_rho_minimal_and_even_polynomials_pass(self) -> None:
        self.assertEqual(
            self.endpoint["rho_minimal_polynomial"],
            "R**4 - 2*R**3 - 6*R**2 + 12*R - 4",
        )
        self.assertEqual(
            self.endpoint["rho_even_polynomial_relation"],
            "R**8 - 16*R**6 + 76*R**4 - 96*R**2 + 16",
        )
        self.assertEqual(sp.simplify(self.rho**2 - self.eta), 0)

    def test_06_sharp_positive_coefficient_certificate_passes(self) -> None:
        self.assertEqual(
            self.positivity["status"], "SHARP_POSITIVITY_CERTIFICATE_PASS"
        )
        self.assertTrue(
            self.positivity["all_nonconstant_coefficients_strictly_positive"]
        )
        self.assertTrue(self.positivity["constant_coefficient_zero"])

    def test_07_sharp_equality_condition_is_unique(self) -> None:
        self.assertEqual(
            self.positivity["equality_conditions"],
            "u=0 and t=0, equivalently y=eta and c=2",
        )
        self.assertEqual(self.band["unique_Bloch_parameter"], "z=1")

    def test_08_global_band_edge_is_attained(self) -> None:
        self.assertEqual(self.band["status"], "GLOBAL_BAND_EDGE_UPPER_PASS")
        self.assertEqual(sp.simplify(self.P.subs({self.y: self.eta, self.c: 2})), 0)

    def test_09_top_root_endpoint_factorizations_pass(self) -> None:
        self.assertEqual(self.monotonicity["y0"], "sqrt(2) + 6")
        self.assertEqual(
            self.monotonicity["P_y0_c_factorization"],
            "(c + 2)*(c - 8*sqrt(2) + 5)",
        )

    def test_10_top_root_is_strictly_increasing(self) -> None:
        self.assertEqual(
            self.monotonicity["status"], "TOP_BAND_MONOTONICITY_PROVED"
        )
        self.assertEqual(
            self.monotonicity["c_vertex_at_y0"], "-7/2 + 4*sqrt(2)"
        )

    def test_11_alpha_plus_has_exact_finite_attainment(self) -> None:
        report = self.holonomies["alpha_plus"]
        self.assertEqual(
            report["status"], "PLUS_HOLONOMY_EXACT_FINITE_CONSTANT_PROVED"
        )
        self.assertEqual(report["attainment_z"], "z=1")
        self.assertEqual(sp.simplify(sp.sympify(report["finite_formula_squared"]) - self.eta), 0)

    def test_12_alpha_minus_band_location_and_limit_pass(self) -> None:
        report = self.holonomies["alpha_minus"]
        self.assertEqual(
            report["status"], "MINUS_HOLONOMY_FINITE_BAND_EDGE_PROVED"
        )
        self.assertEqual(report["maximizing_c"], "2*cos(pi/L)")
        self.assertTrue(report["strict_below_eta"])
        self.assertEqual(sp.simplify(sp.sympify(report["limit"]) - self.eta), 0)

    def test_13_old_rational_bound_is_strict_but_not_sharp(self) -> None:
        report = old_bound_comparison(self.eta)
        self.assertTrue(report["eta_strictly_below_old_bound"])
        self.assertFalse(report["old_bound_is_sharp"])

    def test_14_complete_result_has_final_status(self) -> None:
        self.assertEqual(
            self.result["status"], "PERIOD8_SHARP_SPECTRAL_CONSTANT_PROVED"
        )

    def test_15_independent_checker_passes(self) -> None:
        report = verify_sharp_constant()
        self.assertEqual(report["status"], "TARGET_A_PERIOD8_SHARP_CONSTANT_PASS")

    def test_16_smaller_endpoint_root_fails_largest_check(self) -> None:
        roots = [sp.sympify(value) for value in self.endpoint["ordered_endpoint_roots"]]
        self.assertFalse(validate_candidate_is_largest(roots[-2], roots))

    def test_17_modified_eta_radical_fails_root_check(self) -> None:
        self._modified_result_fails(
            lambda data: data["eta_squared"].__setitem__("exact_radical", "5"),
            "rho_star|endpoint root",
        )

    def test_18_negative_sharp_coefficient_fails_certificate(self) -> None:
        rows = copy.deepcopy(self.positivity["coefficient_map"])
        rows[0]["coefficient"] = "-1"
        with self.assertRaisesRegex(SharpConstantError, "SHARP_POSITIVITY_CERTIFICATE_FAIL"):
            validate_sharp_coefficient_map(rows)

    def test_19_claimed_attainment_below_c2_fails(self) -> None:
        self.assertFalse(validate_band_edge_claim(sp.Rational(3, 2)))
        self._modified_result_fails(
            lambda data: data.__setitem__("c_endpoint", 1),
            "band-edge endpoint",
        )

    def test_20_alpha_minus_finite_attainment_claim_fails(self) -> None:
        self._modified_result_fails(
            lambda data: data["alpha_minus"].__setitem__("strict_below_eta", False),
            "alpha=-1",
        )

    def test_21_alpha_minus_maximizing_c_equal_two_fails(self) -> None:
        self._modified_result_fails(
            lambda data: data["alpha_minus"].__setitem__("maximizing_c", "2"),
            "alpha=-1",
        )

    def test_22_corrupted_task39_sha_fails_dependency(self) -> None:
        data = json.loads(DEFAULT_FAMILY.read_text(encoding="utf-8"))
        data["status"] = "CORRUPTED"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "family.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(SharpConstantError, "SHARP_DEPENDENCY_FAIL"):
                load_dependencies(family_path=path)

    def test_23_old_rational_bound_cannot_be_claimed_sharp(self) -> None:
        self.assertFalse(validate_sharp_bound_claim(OLD_BOUND, self.eta))
        self._modified_result_fails(
            lambda data: data["old_rational_bound_comparison"].__setitem__(
                "old_bound_is_sharp", True
            ),
            "old rational bound",
        )


if __name__ == "__main__":
    unittest.main()

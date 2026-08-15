import copy
import tempfile
import unittest
from pathlib import Path

import sympy as sp

from target_a_floquet_independent_audit import (
    FloquetAuditError,
    TAU_PERIOD,
    boundary_derivation,
    boundary_polynomial_matches,
    build_floquet_block,
    compare_coefficient_maps,
    completeness_check,
    derive_cell_transitions,
    determinant_structure,
    determinant_via_bareiss,
    determinant_via_sympy,
    finite_direct_sum_check,
    hermitian_on_unit_circle,
    operator_derivation_check,
    polynomial_coefficient_map,
    reduce_determinant_to_y_c,
    run_independent_audit,
)


class IndependentFloquetAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.x, cls.y, cls.z, cls.c = sp.symbols("x y z c")
        cls.transitions = derive_cell_transitions()
        cls.block = build_floquet_block(cls.transitions, cls.z)
        cls.determinant = determinant_via_sympy(cls.block, cls.x)
        cls.polynomial = reduce_determinant_to_y_c(
            cls.determinant, cls.x, cls.z, cls.y, cls.c
        )
        cls.directory = tempfile.TemporaryDirectory()
        root = Path(cls.directory.name)
        cls.audit = run_independent_audit(
            root / "transitions.json",
            root / "snapshot.json",
            audit_path=root / "audit.json",
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.directory.cleanup()

    def test_01_transition_table_has_four_hops_per_residue(self) -> None:
        self.assertEqual(len(self.transitions), 32)
        for residue in range(8):
            rows = [row for row in self.transitions if row["output_residue"] == residue]
            self.assertEqual({row["delta"] for row in rows}, {-2, -1, 1, 2})

    def test_02_transition_coefficients_reconstruct_operator(self) -> None:
        row_zero = {row["delta"]: row for row in self.transitions if row["output_residue"] == 0}
        self.assertEqual(row_zero[-2]["coefficient"], TAU_PERIOD[-2])
        self.assertEqual(row_zero[-1]["coefficient"], 1)
        self.assertEqual(row_zero[1]["coefficient"], 1)
        self.assertEqual(row_zero[2]["coefficient"], TAU_PERIOD[0])

    def test_03_hamilton_gauge_equals_twisted_operator(self) -> None:
        report = operator_derivation_check(self.transitions)
        self.assertEqual(report["status"], "OPERATOR_DERIVATION_PASS")
        self.assertTrue(all(report["exact_finite_equivalence"].values()))

    def test_04_bloch_boundary_is_derived_for_both_holonomies(self) -> None:
        self.assertEqual(boundary_derivation(4, 1)["derived_relation"], "z^4=+1")
        self.assertEqual(boundary_derivation(4, -1)["derived_relation"], "z^4=-1")

    def test_05_block_is_built_from_cell_shifts(self) -> None:
        self.assertEqual(self.block[0, 6], 1 / self.z)
        self.assertEqual(self.block[6, 0], self.z)
        self.assertEqual(self.block[1, 7], -1 / self.z)
        self.assertEqual(self.block[7, 1], -self.z)

    def test_06_block_is_symbolically_hermitian_on_unit_circle(self) -> None:
        self.assertTrue(hermitian_on_unit_circle(self.block, self.z))

    def test_07_two_determinant_routes_match_exactly(self) -> None:
        bareiss = determinant_via_bareiss(self.block, self.x)
        self.assertEqual(sp.expand(self.determinant - bareiss), 0)

    def test_08_determinant_is_inversion_symmetric(self) -> None:
        structure = determinant_structure(self.determinant, self.x, self.z)
        self.assertTrue(structure["inversion_symmetric"])

    def test_09_determinant_is_even_in_x(self) -> None:
        structure = determinant_structure(self.determinant, self.x, self.z)
        self.assertTrue(structure["even_in_x"])

    def test_10_y_c_reduction_reconstructs_laurent_determinant(self) -> None:
        reconstructed = self.polynomial.subs(
            {self.y: self.x**2, self.c: self.z + self.z**-1}
        )
        self.assertEqual(sp.expand(reconstructed - self.determinant), 0)

    def test_11_alpha_plus_finite_direct_sum_matches(self) -> None:
        report = finite_direct_sum_check(4, 1, self.transitions)
        self.assertTrue(report["complete"])
        self.assertTrue(report["charpoly_match"])

    def test_12_alpha_minus_finite_direct_sum_matches(self) -> None:
        report = finite_direct_sum_check(4, -1, self.transitions)
        self.assertTrue(report["complete"])
        self.assertTrue(report["charpoly_match"])

    def test_13_frozen_polynomial_comparison_passes(self) -> None:
        self.assertEqual(
            self.audit["frozen_polynomial_comparison_status"],
            "FLOQUET_POLYNOMIAL_MATCH_PASS",
        )
        self.assertTrue(all(row["match"] for row in self.audit["coefficient_comparison"]))

    def test_14_snapshot_precedes_old_evidence_and_root_link_passes(self) -> None:
        self.assertTrue(self.audit["independent_snapshot_frozen_before_old_evidence_read"])
        self.assertEqual(
            self.audit["squared_eigenvalue_root_link_status"],
            "SQUARED_EIGENVALUE_ROOT_LINK_PASS",
        )
        self.assertFalse(self.audit["uniform_bound_audited"])

    def test_15_flipped_tau_changes_determinant(self) -> None:
        altered_tau = list(TAU_PERIOD)
        altered_tau[0] *= -1
        altered_block = build_floquet_block(derive_cell_transitions(tuple(altered_tau)), self.z)
        altered_determinant = determinant_via_sympy(altered_block, self.x)
        self.assertNotEqual(sp.expand(altered_determinant - self.determinant), 0)

    def test_16_altered_cell_shift_fails_consistency(self) -> None:
        altered = copy.deepcopy(self.transitions)
        altered[0]["cell_shift"] += 1
        with self.assertRaisesRegex(FloquetAuditError, "cell shift mismatch"):
            finite_direct_sum_check(4, 1, self.transitions, altered)

    def test_17_wrong_alpha_root_set_fails_boundary_check(self) -> None:
        wrong_root_set = self.z**4 - 1
        self.assertFalse(boundary_polynomial_matches(4, -1, wrong_root_set, self.z))

    def test_18_wrong_wrap_power_fails_hermitian_check(self) -> None:
        altered = self.block.copy()
        altered[0, 6] = self.z
        self.assertFalse(hermitian_on_unit_circle(altered, self.z))

    def test_19_altered_frozen_coefficient_fails_comparison(self) -> None:
        independent = polynomial_coefficient_map(self.polynomial, self.y, self.c)
        altered = copy.deepcopy(independent)
        altered[-1]["coefficient"] = "39"
        with self.assertRaisesRegex(FloquetAuditError, "CRITICAL_FLOQUET_MISMATCH"):
            compare_coefficient_maps(independent, altered)

    def test_20_missing_bloch_block_fails_completeness(self) -> None:
        self.assertFalse(completeness_check(4, 3))


if __name__ == "__main__":
    unittest.main()

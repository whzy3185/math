"""Deterministic Task 52 certificates, regressions, and claim boundaries."""

from __future__ import annotations

import csv
import json
import math
import subprocess
from pathlib import Path

import sympy as sp


RESEARCH = Path(__file__).resolve().parents[1]
ROOT = RESEARCH.parent
PROOF = RESEARCH / "proofs" / "task52"
CERT = PROOF / "certificates"
EXP = RESEARCH / "experiments" / "task52"
ENTRY = "ac4c69b796c9dc14d1307a092d1e0faa093081f2"
C6_RIGHT = sp.Rational(7905369311620328, 10**15)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def proof_text(name: str) -> str:
    return (PROOF / name).read_text(encoding="utf-8")


def test_01_baseline_head_is_ancestor():
    assert subprocess.run(["git", "merge-base", "--is-ancestor", ENTRY, "HEAD"], cwd=ROOT).returncode == 0


def test_02_manuscript_freeze():
    assert subprocess.run([
        "git", "diff", "--quiet", ENTRY, "--",
        "research/paper/manuscript_tex_pub", "research/paper/manuscript_tex_pub_zh",
    ], cwd=ROOT).returncode == 0


def test_03_c6_polynomial_coefficients():
    y = sp.symbols("y")
    polynomial = sp.Poly(load(CERT / "plus_minus_two_algebra.json")["polynomial"], y)
    assert polynomial.all_coeffs() == [16, -520, 6913, -48448, 191768, -423904, 484528, -270464, 137856, -19968, 256]


def test_04_c6_isolating_interval():
    interval = load(CERT / "plus_minus_two_algebra.json")["q_plus_2_root_interval"]
    assert list(map(sp.Rational, interval)) == [sp.Rational(7905369311620327, 10**15), C6_RIGHT]


def test_05_all_c6_polynomial_real_roots():
    data = load(CERT / "c6_root_geometry.json")
    assert data["real_root_count"] == 8 and len(data["real_roots"]) == 8


def test_06_translation_sector_canonical_encoding():
    sectors = load(CERT / "translation_charge.json")["canonical_bulk_sectors"]
    assert len(sectors) == 4 and all(row["Q_cell"].count(1) == 1 for row in sectors)


def test_07_charge_to_sector_transition():
    data = load(CERT / "translation_charge.json")
    assert all(row["exact_rule_holds"] for row in data["transitions"])


def test_08_composition_of_sector_charges():
    assert load(CERT / "translation_charge.json")["composition_checks"] == {"tested_pairs": 289, "all_pass": True}


def test_09_gap2_transfer():
    data = load(RESEARCH / "experiments" / "task51" / "single_charge_symbolic.json")["records"]["2"]
    assert data["determinant"] == "1" and data["charge"] == -2


def test_10_gap2_evans_construction():
    checks = load(CERT / "plus_minus_two_algebra.json")["gap2_evans_certificate"]["checks"]
    assert all(checks.values())


def test_11_q_minus_2_root_isolation():
    interval = list(map(sp.Rational, load(CERT / "plus_minus_two_algebra.json")["q_minus_2_root_interval"]))
    assert interval[1] - interval[0] == sp.Rational(1, 10**15)


def test_12_q_minus_2_above_8():
    assert sp.Rational(load(CERT / "plus_minus_two_algebra.json")["q_minus_2_root_interval"][0]) > 8


def test_13_q_minus_2_common_polynomial_relation():
    data = load(CERT / "plus_minus_two_algebra.json")
    assert data["status"] == "PLUS_MINUS_TWO_COMMON_POLYNOMIAL_PROVED" and data["checks"]["resultants_identical"]


def test_14_q_plus_4_root_interval():
    row = load(CERT / "single_gap_exact_comparisons.json")["records"]["8"]
    assert row["status"] == "COMPUTER_ASSISTED_PROVED" and len(row["y_interval"]) == 2


def test_15_q_plus_4_above_c6():
    assert load(CERT / "single_gap_exact_comparisons.json")["proved_comparisons"]["c_plus_4_gt_c6"]


def test_16_q_plus_6_above_c6():
    assert load(CERT / "single_gap_exact_comparisons.json")["proved_comparisons"]["c_plus_6_gt_c6"]


def test_17_q_plus_8_above_c6():
    assert load(CERT / "single_gap_exact_comparisons.json")["proved_comparisons"]["c_plus_8_gt_c6"]


def test_18_q_minus_1_comparison():
    assert load(CERT / "single_gap_exact_comparisons.json")["proved_comparisons"]["c_minus_1_gt_c6"]


def test_19_gap_plus_eight_transfer_identity():
    data = load(CERT / "charge_recurrence.json")
    assert len(data["records"]) == 8 and all(row["checks"]["all_33_exact_integer_evaluations"] for row in data["records"])


def test_20_charge_recurrence_regression():
    data = load(CERT / "charge_recurrence.json")
    assert data["status"] == "GAP_PLUS_EIGHT_EXACT_EXTERIOR_RECURRENCE_PROVED"
    assert all(row["exterior_recurrence_order_bound"] == 6 for row in data["records"])


def test_21_primitive_interface_canonicalization():
    rows = load(EXP / "primitive_interface_search.json")["records"]
    assert all(row["word"] == row["canonical_word"] for row in rows)


def test_22_primitive_interface_legality():
    data = load(EXP / "primitive_interface_search.json")
    assert sum(data["canonical_word_counts"].values()) == 606


def test_23_primitive_total_charge_calculation():
    rows = load(EXP / "primitive_interface_search.json")["records"]
    assert all(sum(row["charges"]) == row["total_charge"] for row in rows)


def fixed_rows(r: int):
    return [row for row in load(EXP / "fixed_r_full_spectrum_scan.json")["rows"] if row["r"] == r]


def test_24_r2_legal_construction():
    assert all(row["legal_even_defect_count"] and row["charge_congruence"] for row in fixed_rows(2))


def test_25_r3_legal_construction():
    assert all(row["legal_even_defect_count"] and row["charge_congruence"] for row in fixed_rows(3))


def test_26_r4_stress_construction():
    assert load(EXP / "fixed_r_full_spectrum_scan.json")["r4_stress"] == "PASS_NUMERICAL_CLUSTER_EXISTENCE"


def test_27_alpha_plus_one():
    assert all(any(row["alpha"] == 1 for row in fixed_rows(r)) for r in (1, 2, 3, 4))


def test_28_alpha_minus_one():
    assert all(any(row["alpha"] == -1 for row in fixed_rows(r)) for r in (1, 2, 3, 4))


def test_29_orientation_reversal():
    assert max(row["orientation_reversal_rho_error"] for row in load(EXP / "fixed_r_full_spectrum_scan.json")["rows"]) < 1e-12


def test_30_bulk_propagation_error_boundary():
    text = proof_text("TARGET_A_BULK_PROPAGATION_AND_RESOLVENT_BOUNDS.md")
    assert "(9/25)^L" in text and "global DtN" in text


def test_31_r2_interface_count():
    assert all(row["cluster_contains_r_levels"] for row in fixed_rows(2) if row["defect_count"] >= 48)


def test_32_r3_interface_count():
    assert all(row["cluster_contains_r_levels"] for row in fixed_rows(3) if row["defect_count"] >= 48)


def test_33_r2_spectral_cap_not_overclaimed():
    assert "full spectral cap: OPEN" in proof_text("TARGET_A_TASK52_SYNTHESIS.md")


def test_34_r3_spectral_cap_not_overclaimed():
    assert "sufficient target achieved: NO" in proof_text("TARGET_A_TASK52_SYNTHESIS.md")


def test_35_effective_r2_reconstruction():
    cases = [row for row in load(EXP / "fixed_r_high_precision_evans.json")["cases"] if row["r"] == 2]
    assert len(cases) == 2 and max(float(row["finite_matrix_transfer_max_difference"]) for row in cases) < 1e-12


def test_36_effective_r3_reconstruction():
    cases = [row for row in load(EXP / "fixed_r_high_precision_evans.json")["cases"] if row["r"] == 3]
    assert len(cases) == 2 and all(len(row["precision_ladder"][-1]["y"]) == 3 for row in cases)


def test_37_residue_2_family():
    text = proof_text("TARGET_A_COMMON_RESIDUE_UPPER_THEOREM.md")
    assert "8k+2" in text and "does **not** prove" in text


def test_38_residue_4_family():
    assert "8k+4" in proof_text("TARGET_A_COMMON_RESIDUE_UPPER_THEOREM.md")


def test_39_residue_6_family():
    assert "8k+6" in proof_text("TARGET_A_COMMON_RESIDUE_UPPER_THEOREM.md")


def test_40_limsup_inequality_boundary():
    text = proof_text("TARGET_A_COMMON_RESIDUE_UPPER_THEOREM.md")
    assert "limsup" in text and "CONDITIONAL_FIXED_R_GLOBAL_CAP" in text


def test_41_threshold_rho_minus_comparison():
    n = 100
    threshold = 4 + 2 * math.cos(2 * math.pi / n) + 2 * math.cos(4 * math.pi / n)
    assert float(C6_RIGHT) < threshold < 8


def test_42_c6_weighted_moment_algebra():
    data = load(EXP / "c6_weighted_moments.json")
    assert data["status"] == "C6_WEIGHTED_MOMENT_FORMS_EXACT" and list(data["forms"]) == ["F1", "F2", "F3", "F4", "F5"]


def test_43_c6_local_motif_evaluator():
    counts = [row["translation_class_count"] for row in load(EXP / "c6_weighted_moments.json")["forms"].values()]
    assert counts == [2, 4, 10, 27, 76]


def test_44_low_energy_grammar_overlap_consistency():
    data = load(EXP / "c6_low_energy_grammar.json")
    assert data["overlap_automaton"] == {"window_length": 11, "nodes": 105, "edges": 164}


def test_45_truncated_g6_lower_bound():
    text = proof_text("TARGET_A_DENSE_SPARSE_RIGIDITY_BLUEPRINT.md")
    assert "rho(A)^2 >= c6-C' (9/25)^L" in text


def test_46_period10_above_c6():
    data = load(EXP / "p24_c6_audit.json")["period10_exact"]
    assert data["status"] == "PERIOD10_BAND_EDGE_GT_C6_PROVED" and all(data["checks"].values())


def test_47_q1_q2_sector_decomposition():
    data = load(RESEARCH / "experiments" / "task51" / "recurrence_exact_structure.json")
    assert data["status"] == "ORDER9_EXACT_1_PLUS_4_PLUS_4_PROVED" and data["bezout"]["exact"]


def test_48_dominant_recurrence_root_boundary():
    text = proof_text("TARGET_A_DOMINANT_MODE_FINITE_RING_THEOREM.md")
    assert "fixed-sign dominant modal" in text and "INSURANCE_ROUTE_PARTIAL" in text


def test_49_exact_finite_prefix():
    data = load(RESEARCH / "experiments" / "task51" / "recurrence_shift_signs.json")
    assert data["global_k_le_32_result"] == "STRONG"


def test_50_finite_evans_fallback_boundary():
    assert "No finite-Evans/Rouche winding certificate was" in proof_text("TARGET_A_DOMINANT_MODE_FINITE_RING_THEOREM.md")


def test_51_task51_regression():
    assert load(RESEARCH / "reproducibility" / "task51" / "verification.json")["status"] == "TARGET_A_TASK51_VERIFY_PASS"


def test_52_task50_regression():
    assert load(RESEARCH / "proofs" / "task50" / "certificates" / "g6_interface_certificate.json")["status"] == "G6_INTERFACE_THEOREM_PROVED"


def test_53_task49_regression():
    assert load(RESEARCH / "experiments" / "task49" / "interface_mechanism" / "summary.json")["gate"] == "INTERFACE_MECHANISM_READY_FOR_PROOF"


def test_54_task48a_regression():
    assert load(RESEARCH / "experiments" / "task48a" / "interface" / "summary.json")["INTERFACE_THEOREM_SIGNAL"] == "STRONG"


def test_55_task47_regression():
    assert "TARGET_A_TASK47_EXPERIMENTS_COMPLETE" in (RESEARCH / "experiments" / "TARGET_A_TASK47_SYNTHESIS.md").read_text()


def test_56_minimality_verifier_artifact():
    assert load(RESEARCH / "counterexamples" / "target_a_minimality_certificate.json")["overall_status"] == "PASS"


def test_57_computational_evidence_verifier_artifact():
    assert load(RESEARCH / "reproducibility" / "target_a_computational_evidence_manifest.json")["status"] == "TARGET_A_COMPUTATIONAL_EVIDENCE_COMPLETE"


def test_58_submission_artifact_verifier():
    assert load(RESEARCH / "reproducibility" / "target_a_submission_artifact_manifest.json")["status"] == "TARGET_A_SUBMISSION_ARTIFACT_MANIFEST_COMPLETE"


def test_59_elementary_completeness_boundary():
    data = load(EXP / "primitive_interface_search.json")
    assert not data["completeness_achieved"] and data["status"].endswith("STRONGLY_SUPPORTED")


def test_60_large_gap_threat_search():
    data = load(EXP / "large_gap_scan.json")
    assert data["range"] == [13, 76] and not data["any_cost_below_c6"]


def test_61_precision_ladders():
    assert all([row["digits"] for row in case["precision_ladder"]] == [80, 120, 160] for case in load(EXP / "fixed_r_high_precision_evans.json")["cases"])


def test_62_p24_no_numerical_below_c6():
    assert load(EXP / "p24_c6_audit.json")["numerical_non_target_below_c6"] == []


def test_63_root_geometry_simple():
    data = load(CERT / "c6_root_geometry.json")
    assert data["discriminant_nonzero"] and data["all_roots_simple"] and data["physical_root_count_proved"] == 2


def test_64_final_status_is_partial():
    assert "TARGET_A_TASK52_PARTIAL_PROGRESS" in proof_text("TARGET_A_TASK52_SYNTHESIS.md")

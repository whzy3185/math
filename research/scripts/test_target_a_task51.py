"""Deterministic regression and evidence-boundary tests for Task 51."""

from __future__ import annotations

import csv
import json
import subprocess
from pathlib import Path

import numpy as np
import sympy as sp

from target_a_task51_crystallization import local_rayleigh_matrix


RESEARCH = Path(__file__).resolve().parents[1]
TASK51 = RESEARCH / "experiments" / "task51"
DISCOVERY = RESEARCH / "discovery" / "task51"
PROOF51 = RESEARCH / "proofs" / "task51" / "certificates"
BASELINE = "82895863a59f8014d547544a7b3bb18aaa0cc8e5"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_task50_regression():
    assert load(RESEARCH / "proofs" / "task50" / "certificates" / "g6_interface_certificate.json")["status"] == "G6_INTERFACE_THEOREM_PROVED"


def test_task49_regression():
    assert load(RESEARCH / "experiments" / "task49" / "interface_mechanism" / "summary.json")["gate"] == "INTERFACE_MECHANISM_READY_FOR_PROOF"


def test_task48a_regression():
    assert load(RESEARCH / "experiments" / "task48a" / "interface" / "summary.json")["INTERFACE_THEOREM_SIGNAL"] == "STRONG"


def test_task47_regression():
    assert "TARGET_A_TASK47_EXPERIMENTS_COMPLETE" in (RESEARCH / "experiments" / "TARGET_A_TASK47_SYNTHESIS.md").read_text()


def test_order9_exact_factorization():
    data = load(TASK51 / "recurrence_exact_structure.json")
    assert data["factorization_identity_exact"] and data["status"] == "ORDER9_EXACT_1_PLUS_4_PLUS_4_PROVED"


def test_projected_recurrence_reconstruction():
    data = load(TASK51 / "recurrence_exact_structure.json")
    assert data["bezout"]["exact"] and all(row["Q1Q2_delta_checks"] >= 20 for row in data["sequence_checks"])


def test_reciprocal_four_to_two_reduction():
    assert all(row["lift_identity_exact"] for row in load(TASK51 / "recurrence_exact_structure.json")["reciprocal_reductions"])


def test_shifted_sign_evaluator():
    data = load(TASK51 / "recurrence_shift_signs.json")
    assert data["global_prefix_result"] == data["global_k_le_32_result"] == "STRONG"


def test_charge_conservation_identities():
    data = load(TASK51 / "charge_conservation.json")
    assert data["status"] == "EXACT_CHARGE_CONSERVATION_PROVED"
    assert [row["n_mod_8"] for row in data["rows"]] == [0, 2, 4, 6]


def test_charge_generator_g6_regression():
    assert load(TASK51 / "single_charge_symbolic.json")["G6_regression"] is True


def test_charge_generator_g10_regression():
    assert load(TASK51 / "single_charge_symbolic.json")["G10_regression"] is True


def test_deterministic_gap2_result():
    gap2 = load(TASK51 / "single_charge_summary.json")["gap2"]
    assert gap2["R_squared"] > 8 and gap2["width_120_to_180_difference"] < 1e-10


def test_defect_rank_inertia():
    data = load(TASK51 / "finite_rank_inertia.json")
    assert data["status"] == "NEUTRAL_FINITE_DEFECT_RANK_INERTIA_EXACT"
    assert all(row["positive_inertia"] + row["negative_inertia"] == row["rank"] for row in data["rows"])


def test_three_g6_legality_and_comparison():
    data = load(TASK51 / "multi_slip_summary.json")
    assert data["three_G6_beats_G10"] and data["three_G6_minus_G10_at_fixed_defect_count"] < -0.07


def test_mixed_charge_legality():
    data = load(TASK51 / "charge_conservation.json")
    assert next(row for row in data["rows"] if row["n_mod_8"] == 6)["nearest_negative_total_charge"] == -2


def test_selected_birman_schwinger_reconstruction():
    data = load(TASK51 / "green_birman_crosscheck.json")
    assert data["determinant_lemma_sign_match"] and data["determinant_lemma_log_error"] < 1e-10


def test_selected_green_crosscheck():
    assert load(TASK51 / "green_birman_crosscheck.json")["green_inverse_solve_max_error"] < 1e-12


def test_multi_slip_effective_reconstruction():
    rows = list(csv.DictReader((TASK51 / "multi_slip_clusters.csv").open()))
    assert max(float(row["effective_reconstruction_error"]) for row in rows) < 2e-14


def test_pairwise_resolution_guard():
    data = load(TASK51 / "multi_slip_summary.json")
    assert data["pairwise_scalar_diagnostic"]["classification"] == "BELOW_DOUBLE_RESOLUTION"
    assert data["many_body_classification"] == "UNRESOLVED"


def test_subeight_phase_classifier():
    data = load(TASK51 / "subeight_periodic_summary.json")
    assert data["primitive_R_lt_8_count"] == 13 and 24 in data["primitive_periods"]


def test_m4_independent_closed_walk_check():
    data = load(TASK51 / "higher_moment_motifs.json")
    assert data["status"] == "M4_M5_M6_EXACT_LOCAL_MOTIF_EXPANSIONS_PROVED"
    assert data["expansions"]["M4"]["translation_class_count"] == 10


def test_local_window_global_sign_equivalence():
    word = (1, -1, 1, 1, -1, -1, 1, -1)
    left = local_rayleigh_matrix(word, 6)
    right = local_rayleigh_matrix(tuple(-value for value in word), 6)
    diagonal = np.diag([(-1) ** index for index in range(6)])
    assert np.array_equal(right, diagonal @ left @ diagonal)


def test_debruijn_consistency():
    data = load(TASK51 / "local_rayleigh_debruijn.json")
    assert data["target_cycle_present"] and data["de_bruijn_bounded_cycle_count_period_le_16"] == 30


def test_cycle_polytope_fail_closed():
    text = (DISCOVERY / "TARGET_A_CRYSTALLIZATION_PROGRAM.md").read_text()
    assert "Motif-frequency/cycle polytope | PROMISING" in text and "ARBITRARY_PERIOD_REMAINS_OPEN" in text


def test_transparent_defect_enumeration():
    data = load(TASK51 / "transparent_defect_search.json")
    assert data["motif_count"] == 11 and not data["transparent_defect_found"]


def test_c6_exact_polynomial():
    data = load(PROOF51 / "c6_exact_evans_elimination.json")["c6"]
    y = sp.symbols("y")
    polynomial = sp.Poly(data["c6_polynomial"], y)
    assert data["status"] == "C6_DEGREE10_EVANS_POLYNOMIAL_PROVED"
    assert polynomial.degree() == 10 and polynomial.is_irreducible


def test_manuscript_freeze():
    result = subprocess.run([
        "git", "diff", "--quiet", BASELINE, "--",
        "research/paper/manuscript_tex_pub", "research/paper/manuscript_tex_pub_zh",
    ], cwd=RESEARCH.parent)
    assert result.returncode == 0

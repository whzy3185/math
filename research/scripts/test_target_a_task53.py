"""Focused positive and tamper tests for Target A Task 53."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from target_a_task53_global import residue_gap_word, slip_separations, tent_normalization
from target_a_task53_p24 import exact_bloch_matrix, exact_rayleigh, q_from_bits
from target_a_low_period_spectral_frontier import tau_lift
from verify_target_a_task53_a1 import CERTIFICATE as A1_CERT, verify as verify_a1
from verify_target_a_task53_a2 import CERTIFICATE as A2_CERT, verify as verify_a2
from verify_target_a_task53_a3 import CERTIFICATE as A3_CERT, verify as verify_a3
from verify_target_a_task53_global import CERTIFICATE as GLOBAL_CERT, verify as verify_global
from verify_target_a_task53_p24 import CERTIFICATE as P24_CERT, verify as verify_p24
from verify_target_a_task53_s1 import CERTIFICATE as S1_CERT, verify as verify_s1
from verify_target_a_task53_s4 import CERTIFICATE as S4_CERT, verify as verify_s4


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def tampered(tmp_path: Path, source: Path, mutation) -> Path:
    data = copy.deepcopy(load(source))
    mutation(data)
    path = tmp_path / source.name
    path.write_text(json.dumps(data, indent=2) + "\n")
    return path


@pytest.fixture(scope="module")
def positive_checks() -> dict[str, dict[str, bool]]:
    return {
        "a1": verify_a1(),
        "a2": verify_a2(),
        "a3": verify_a3(),
        "global": verify_global(),
        "p24": verify_p24(),
        "s1": verify_s1(),
        "s4": verify_s4(),
    }


@pytest.mark.parametrize("module", ["a1", "a2", "a3", "global", "p24", "s1", "s4"])
def test_01_module_checkers_pass(positive_checks, module):
    assert all(positive_checks[module].values())


@pytest.mark.parametrize("radius", range(4, 20))
def test_02_tent_normalization_formula(radius):
    direct = 1 + 2 * sum(((radius - j) / radius) ** 2 for j in range(1, radius))
    assert abs(float(tent_normalization(radius)) - direct) < 1e-12


@pytest.mark.parametrize("residue", [2, 4, 6])
@pytest.mark.parametrize("k", [4, 7, 13, 29])
def test_03_residue_words_are_legal(residue, k):
    word = residue_gap_word(residue, k)
    assert sum(word) == 8 * k + residue
    assert len(word) % 2 == 0
    assert word.count(6) == residue // 2
    assert min(slip_separations(word)) > 0


@pytest.mark.parametrize("index", range(16))
def test_04_each_p24_witness_is_exact(index):
    row = load(P24_CERT)["witnesses"][index]
    tau = tau_lift(q_from_bits(row["q_bits"]))
    matrix = exact_bloch_matrix(tau, row["bloch_root"])
    vector = [(int(real), int(imag)) for real, imag in row["gaussian_integer_vector"]]
    assert exact_rayleigh(matrix, vector) == (row["numerator_A2"], row["denominator"])
    assert int(row["strict_margin_numerator_against_c6_upper"]) > 0


def test_10_corrupt_bulk_polynomial_fails(tmp_path):
    path = tampered(tmp_path, A1_CERT, lambda d: d.__setitem__("characteristic_polynomial", "z**4+1"))
    with pytest.raises(AssertionError):
        verify_a1(path)


def test_11_modify_c6_interval_fails(tmp_path):
    path = tampered(tmp_path, A1_CERT, lambda d: d.__setitem__("energy_interval", ["7", "16"]))
    with pytest.raises(AssertionError):
        verify_a1(path)


def test_12_remove_grassmann_chart_fails(tmp_path):
    path = tampered(tmp_path, A2_CERT, lambda d: d["atlas"].pop())
    with pytest.raises(AssertionError):
        verify_a2(path)


def test_13_exchange_stable_branch_fails(tmp_path):
    path = tampered(tmp_path, A2_CERT, lambda d: d.__setitem__("branch_selector", "smaller_t_larger_P"))
    with pytest.raises(AssertionError):
        verify_a2(path)


def test_14_replace_g6_by_gap2_fails(tmp_path):
    path = tampered(tmp_path, A2_CERT, lambda d: d.__setitem__("physical_matching", "gap2 cut"))
    with pytest.raises(AssertionError):
        verify_a2(path)


def test_15_mutate_transfer_chart_order_fails(tmp_path):
    path = tampered(tmp_path, A3_CERT, lambda d: d["candidate_records"][0].__setitem__("cofactor_rows", [0, 2, 3]))
    with pytest.raises(AssertionError):
        verify_a3(path)


def test_16_corrupt_physical_classification_fails(tmp_path):
    path = tampered(tmp_path, A3_CERT, lambda d: d["candidate_records"][1].__setitem__("classification", "PHYSICAL"))
    with pytest.raises(AssertionError):
        verify_a3(path)


def test_20_corrupt_ims_constant_fails(tmp_path):
    path = tampered(tmp_path, GLOBAL_CERT, lambda d: d["ims"].__setitem__("C_IMS", 575))
    with pytest.raises(AssertionError):
        verify_global(path)


def test_21_remove_range_four_margin_fails(tmp_path):
    path = tampered(tmp_path, GLOBAL_CERT, lambda d: d["patch_classification"].__setitem__("range_four_margin", "removed"))
    with pytest.raises(AssertionError):
        verify_global(path)


def test_22_force_two_interface_patch_fails(tmp_path):
    path = tampered(tmp_path, GLOBAL_CERT, lambda d: d["patch_classification"].__setitem__("no_fourth_class", "two interfaces allowed"))
    with pytest.raises(AssertionError):
        verify_global(path)


def test_23_move_holonomy_cut_without_gauge_fails(tmp_path):
    path = tampered(tmp_path, GLOBAL_CERT, lambda d: d["patch_classification"].__setitem__("equivalences", "translation only"))
    with pytest.raises(AssertionError):
        verify_global(path)


def test_24_mutate_gap_sum_fails(tmp_path):
    path = tampered(tmp_path, GLOBAL_CERT, lambda d: d["residues"][0]["samples"][0].__setitem__("gap_sum", 1))
    with pytest.raises(AssertionError):
        verify_global(path)


def test_25_mutate_residue_class_fails(tmp_path):
    path = tampered(tmp_path, GLOBAL_CERT, lambda d: d["residues"][1].__setitem__("residue", 0))
    with pytest.raises(AssertionError):
        verify_global(path)


def test_26_break_parity_legality_fails(tmp_path):
    path = tampered(tmp_path, GLOBAL_CERT, lambda d: d["residues"][2]["samples"][0].__setitem__("q_legal", False))
    with pytest.raises(AssertionError):
        verify_global(path)


def test_27_corrupt_eventual_threshold_fails(tmp_path):
    path = tampered(tmp_path, GLOBAL_CERT, lambda d: d["eventual_all_even"].__setitem__("N", 2498))
    with pytest.raises(AssertionError):
        verify_global(path)


def test_30_remove_primitive_orbit_fails(tmp_path):
    path = tampered(tmp_path, P24_CERT, lambda d: d["residual_subeight_keys"].pop())
    with pytest.raises(AssertionError):
        verify_p24(path)


def test_31_replace_rayleigh_witness_fails(tmp_path):
    path = tampered(tmp_path, P24_CERT, lambda d: d["witnesses"][0].__setitem__("gaussian_integer_vector", [[0, 0]] * d["witnesses"][0]["period"]))
    with pytest.raises(AssertionError):
        verify_p24(path)


def test_32_corrupt_frontier_c6_endpoint_fails(tmp_path):
    path = tampered(tmp_path, P24_CERT, lambda d: d.__setitem__("c6_upper", "8"))
    with pytest.raises(AssertionError):
        verify_p24(path)


def test_33_remove_witness_fails(tmp_path):
    path = tampered(tmp_path, P24_CERT, lambda d: d["witnesses"].pop())
    with pytest.raises(AssertionError):
        verify_p24(path)


def test_34_duality_overclaim_fails(tmp_path):
    path = tampered(tmp_path, S1_CERT, lambda d: d.__setitem__("status", "PLUS_MINUS_TWO_UNSQUARED_DUALITY_PROVED"))
    with pytest.raises(AssertionError):
        verify_s1(path)


def test_35_new_moment_overclaim_fails(tmp_path):
    path = tampered(tmp_path, S4_CERT, lambda d: d.__setitem__("M7_M8_generated", True))
    with pytest.raises(AssertionError):
        verify_s4(path)

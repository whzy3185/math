"""Positive and fail-closed tests for the Task 55 exact-2r checker."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from verify_target_a_task55_exact_2r import CERTIFICATE, load_strict, verify


def load() -> dict:
    return load_strict(CERTIFICATE)


def tampered(tmp_path: Path, mutation) -> Path:
    data = copy.deepcopy(load())
    mutation(data)
    path = tmp_path / "exact_2r_cluster.json"
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return path


def must_fail(tmp_path: Path, mutation) -> None:
    with pytest.raises((AssertionError, ValueError, KeyError, TypeError)):
        verify(tampered(tmp_path, mutation))


def test_01_independent_checker_passes():
    assert all(verify().values())


def test_02_dimension_tamper_fails(tmp_path):
    must_fail(tmp_path, lambda data: data["rank_two_input"].__setitem__("H_c6_riesz_rank", 1))


def test_03_exact_window_dimension_tamper_fails(tmp_path):
    must_fail(tmp_path, lambda data: data["counting"]["r_records"][1].__setitem__("localized_columns", 2))


def test_04_K_symmetry_tamper_fails(tmp_path):
    must_fail(
        tmp_path,
        lambda data: data["rank_two_input"]["operator_identities"].__setitem__(1, "KA=AK"),
    )


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("tail_basis_condition_bound", 16),
        ("floquet_cell_rate_q", "2/5"),
        ("normalized_tail_bound", "72*q^ell"),
        ("single_column_residual", "1751*q^ell"),
        ("ims_error_at_D0", "1/200"),
        ("fixed_window_radius", "1/200"),
        ("Q_resolvent_bound", 399),
        ("minimum_interface_distance_D0", 1039),
        ("ell_at_D0", 30),
    ],
)
def test_10_constant_tamper_fails(tmp_path, field, value):
    must_fail(tmp_path, lambda data: data["constants"].__setitem__(field, value))


def test_11_gram_tamper_fails(tmp_path):
    must_fail(tmp_path, lambda data: data["gram"].__setitem__("columns", "m=r"))


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("spectral_equation", "H_eff(z)-zP"),
        ("exact_gram_formula", "H_eff(z)-c6 I_r=T1+R2"),
        ("first_order_bound", "||T1||<=3504*q^ell"),
        ("second_order_bound", "||R2(z)||<q^ell"),
        ("cluster_bound", "|lambda_j-c6|<3504*r*q^ell"),
    ],
)
def test_20_feshbach_tamper_fails(tmp_path, field, value):
    must_fail(tmp_path, lambda data: data["feshbach"].__setitem__(field, value))


def test_30_residue_tamper_fails(tmp_path):
    must_fail(tmp_path, lambda data: data["exponential_tail"]["residue_endpoints"][2].__setitem__("residue", 4))


def test_31_residue_endpoint_tamper_fails(tmp_path):
    must_fail(tmp_path, lambda data: data["exponential_tail"]["residue_endpoints"][2].__setitem__("first_eligible_n", 3118))


def test_32_N_exp_tamper_fails(tmp_path):
    must_fail(tmp_path, lambda data: data["exponential_tail"].__setitem__("N_exp", 3118))


def test_33_dependency_hash_tamper_fails(tmp_path):
    must_fail(
        tmp_path,
        lambda data: data["dependencies"]["artifacts"][1].__setitem__("sha256", "0" * 64),
    )


def test_34_monodromy_hash_tamper_fails(tmp_path):
    must_fail(
        tmp_path,
        lambda data: data["bulk_floquet"]["phase_records"][7].__setitem__("right_monodromy_sha256", "0" * 64),
    )


def test_35_phase_count_tamper_fails(tmp_path):
    must_fail(tmp_path, lambda data: data["bulk_floquet"]["phase_records"].pop())


def test_36_status_only_fails(tmp_path):
    must_fail(tmp_path, lambda data: data.__setitem__("checks", {"status": True}))


def test_37_legacy_exact_r_field_fails(tmp_path):
    must_fail(tmp_path, lambda data: data.__setitem__("exact_r", {"dimension": "r"}))


def test_38_pending_integration_status_fails(tmp_path):
    must_fail(
        tmp_path,
        lambda data: data.__setitem__(
            "integration_status", "PENDING_INDEPENDENT_CHECKER_PASS"
        ),
    )


def test_40_float_acceptance_fails(tmp_path):
    must_fail(tmp_path, lambda data: data["constants"].__setitem__("q", 0.36))


def test_41_duplicate_json_key_fails(tmp_path):
    text = CERTIFICATE.read_text(encoding="utf-8")
    text = text.replace('  "status":', '  "status": "duplicate",\n  "status":', 1)
    path = tmp_path / "duplicate_exact_2r.json"
    path.write_text(text, encoding="utf-8")
    with pytest.raises(ValueError):
        verify(path)

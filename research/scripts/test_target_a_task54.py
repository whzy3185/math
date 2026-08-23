"""Focused positive and fail-closed tests for Target A Task 54."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import pytest

from target_a_task54_threshold import (
    N_STAR,
    N_TAIL,
    exact_ims_error,
    exact_tent_translation_difference,
    radius_from_separation,
    separation,
    threshold_lower,
)
from verify_target_a_task54_exact_r import CERTIFICATE as EXACT_R_CERT, verify as verify_exact_r
from verify_target_a_task54_isolation import CERTIFICATE as ISOLATION_CERT, verify as verify_isolation
from verify_target_a_task54_threshold import CERTIFICATE, verify as verify_threshold


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def tampered(tmp_path: Path, mutation) -> Path:
    data = copy.deepcopy(load(CERTIFICATE))
    mutation(data)
    path = tmp_path / "tampered_threshold.json"
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return path


def tampered_source(tmp_path: Path, source: Path, mutation) -> Path:
    data = copy.deepcopy(load(source))
    mutation(data)
    path = tmp_path / source.name
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return path


def test_01_isolation_checker_passes():
    assert all(verify_isolation().values())


def test_02_exact_r_arithmetic_checker_passes():
    assert all(verify_exact_r().values())


def test_03_threshold_checker_passes():
    assert all(verify_threshold().values())


@pytest.mark.parametrize("distance", [1, 2, 3, 4])
def test_10_exact_tent_differences_are_positive(distance):
    assert exact_tent_translation_difference(17, distance) > 0


@pytest.mark.parametrize("radius", [4, 5, 17, 64, 255])
def test_11_exact_ims_closed_form(radius):
    assert exact_ims_error(radius) == Fraction(
        240 * radius - 342, radius * (2 * radius * radius + 1)
    )


@pytest.mark.parametrize("distance", [18, 26, 100, 239, 500])
def test_12_radius_satisfies_strict_patch_condition(distance):
    radius = radius_from_separation(distance)
    assert 2 * (radius + 4) < distance


@pytest.mark.parametrize(
    ("n", "expected"),
    [(242, 242), (244, 122), (246, 82), (238, 78)],
)
def test_13_residue_specific_separation(n, expected):
    assert separation(n) == expected


def test_14_thresholds_remain_distinct():
    data = load(CERTIFICATE)
    assert data["N_Task53"] == 2500
    assert data["N_tail"] == N_TAIL == 240
    assert data["N_star"] == N_STAR == 48


def test_15_all_finite_rows_have_strict_rational_sandwich():
    rows = load(CERTIFICATE)["finite_tail"]["records"]
    assert len(rows) == 96
    assert all(
        Fraction(row["rational_upper_on_rho_squared"]) < threshold_lower(row["n"])
        for row in rows
    )


def test_20_remove_one_order_fails(tmp_path):
    path = tampered(tmp_path, lambda data: data["finite_tail"]["records"].pop(17))
    with pytest.raises(AssertionError):
        verify_threshold(path)


def test_21_change_gap_word_fails(tmp_path):
    path = tampered(
        tmp_path,
        lambda data: data["finite_tail"]["records"][5]["gap_word"].__setitem__(0, 2),
    )
    with pytest.raises((AssertionError, ValueError)):
        verify_threshold(path)


def test_22_alter_spectral_upper_bound_fails(tmp_path):
    path = tampered(
        tmp_path,
        lambda data: data["finite_tail"]["records"][0].__setitem__(
            "rational_upper_on_rho_squared", "8"
        ),
    )
    with pytest.raises(AssertionError):
        verify_threshold(path)


def test_23_change_analytic_tail_fails(tmp_path):
    path = tampered(tmp_path, lambda data: data.__setitem__("N_tail", 238))
    with pytest.raises(AssertionError):
        verify_threshold(path)


def test_24_break_radius_geometry_fails(tmp_path):
    path = tampered(
        tmp_path,
        lambda data: data["analytic"].__setitem__("radius", "R=floor(D/4)"),
    )
    with pytest.raises(AssertionError):
        verify_threshold(path)


def test_25_corrupt_endpoint_fails(tmp_path):
    path = tampered(
        tmp_path,
        lambda data: data["analytic"]["endpoint_checks"]["6"].__setitem__("strict", False),
    )
    with pytest.raises(AssertionError):
        verify_threshold(path)


def test_26_false_minimality_wording_is_absent():
    data = load(CERTIFICATE)
    assert "not a globally minimal" in data["scope"]


@pytest.mark.parametrize(
    ("field", "value"),
    [("pivot_count", 1), ("pivot_sha256", "0" * 64),
     ("family", "WRONG"), ("antibalanced_rational_lower", "7")],
)
def test_27_corrupt_record_metadata_fails(tmp_path, field, value):
    path = tampered(
        tmp_path,
        lambda data: data["finite_tail"]["records"][0].__setitem__(field, value),
    )
    with pytest.raises(AssertionError):
        verify_threshold(path)


def test_28_empty_stored_checks_fail(tmp_path):
    path = tampered(tmp_path, lambda data: data.__setitem__("checks", {}))
    with pytest.raises(AssertionError):
        verify_threshold(path)


def test_29_oversized_rational_fails(tmp_path):
    path = tampered(
        tmp_path,
        lambda data: data["finite_tail"]["records"][0].__setitem__(
            "rational_upper_on_rho_squared", f"{10**15}/1"
        ),
    )
    with pytest.raises(AssertionError):
        verify_threshold(path)


def test_30_change_delta6_fails(tmp_path):
    path = tampered_source(tmp_path, ISOLATION_CERT, lambda data: data.__setitem__("delta6", "1/50"))
    with pytest.raises(AssertionError):
        verify_isolation(path)


def test_31_remove_isolation_factor_fails(tmp_path):
    path = tampered_source(
        tmp_path, ISOLATION_CERT,
        lambda data: data["candidate_classification"]["factors"].pop(),
    )
    with pytest.raises(AssertionError):
        verify_isolation(path)


def test_32_empty_isolation_checks_fail(tmp_path):
    path = tampered_source(tmp_path, ISOLATION_CERT, lambda data: data.__setitem__("checks", {}))
    with pytest.raises(AssertionError):
        verify_isolation(path)


def test_33_change_exact_r_distance_fails(tmp_path):
    path = tampered_source(
        tmp_path, EXACT_R_CERT,
        lambda data: data["constants"].__setitem__("minimum_complete_bulk_cells_ell0", 32),
    )
    with pytest.raises(AssertionError):
        verify_exact_r(path)


def test_34_empty_exact_r_checks_fail(tmp_path):
    path = tampered_source(tmp_path, EXACT_R_CERT, lambda data: data.__setitem__("checks", {}))
    with pytest.raises(AssertionError):
        verify_exact_r(path)


def test_35_coordinated_gap_word_metadata_tamper_fails(tmp_path):
    data = copy.deepcopy(load(CERTIFICATE))
    row = data["finite_tail"]["records"][0]
    row["gap_word"][:2] = [2, 6]
    q = [-1] * row["n"]
    position = 0
    for gap in row["gap_word"]:
        q[position] = 1
        position += gap
    row["q_sha256"] = hashlib.sha256(
        "".join("1" if value == 1 else "0" for value in q).encode()
    ).hexdigest()
    digest = hashlib.sha256()
    for record in data["finite_tail"]["records"]:
        digest.update(json.dumps(record, sort_keys=True, separators=(",", ":")).encode())
    data["finite_tail"]["ordered_record_sha256"] = digest.hexdigest()
    path = tmp_path / "coordinated_family_tamper.json"
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    with pytest.raises(AssertionError):
        verify_threshold(path)


@pytest.mark.parametrize(
    ("mutation"),
    [
        lambda data: data.__setitem__("c6_interval", ["7", "8"]),
        lambda data: data["candidate_classification"].__setitem__(
            "secondary_interval", ["7", "8"]
        ),
        lambda data: data["resolvent"].__setitem__("reduced_kernel_constant", 1199),
    ],
)
def test_36_isolation_bound_fields_fail_closed(tmp_path, mutation):
    path = tampered_source(tmp_path, ISOLATION_CERT, mutation)
    with pytest.raises(AssertionError):
        verify_isolation(path)

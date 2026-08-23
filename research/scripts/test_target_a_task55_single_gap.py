"""Focused positive and fail-closed tests for Task 55 single-gap algebra."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from verify_target_a_task55_single_gap import CERTIFICATE, load_strict, verify


def load() -> dict:
    return load_strict(CERTIFICATE)


def tampered(tmp_path: Path, mutation) -> Path:
    data = copy.deepcopy(load())
    mutation(data)
    path = tmp_path / "single_gap_structure.json"
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return path


def test_01_independent_checker_passes():
    assert all(verify().values())


def test_02_status_keeps_hierarchy_open():
    assert load()["status"] == "TASK55_SINGLE_GAP_ALGEBRA_PROVED_HIERARCHY_OPEN"


def test_03_symbol_name_tamper_fails(tmp_path):
    path = tampered(tmp_path, lambda data: data["symbol_contract"].__setitem__(0, "lambda"))
    with pytest.raises(AssertionError):
        verify(path)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("product_order", "right multiplication"),
        ("step", "wrong transfer"),
        ("q", "wrong interface"),
    ],
)
def test_04_transfer_convention_tamper_fails(tmp_path, field, value):
    path = tampered(
        tmp_path, lambda data: data["transfer_convention"].__setitem__(field, value)
    )
    with pytest.raises(AssertionError):
        verify(path)


def test_05_evans_cut_tamper_fails(tmp_path):
    path = tampered(
        tmp_path,
        lambda data: data["transfer_convention"]["evans_cut"].__setitem__("start", "-7"),
    )
    with pytest.raises(AssertionError):
        verify(path)


def test_06_exterior_basis_tamper_fails(tmp_path):
    path = tampered(
        tmp_path,
        lambda data: data["transfer_convention"]["exterior_basis"].__setitem__(0, [1, 0]),
    )
    with pytest.raises(AssertionError):
        verify(path)


def test_07_quotient_identity_tamper_fails(tmp_path):
    path = tampered(
        tmp_path,
        lambda data: data["unsquared_duality"].__setitem__(
            "identity", "e6(lam,P)=e2(lam,P)"
        ),
    )
    with pytest.raises(AssertionError):
        verify(path)


def test_08_reduced_core_tamper_fails(tmp_path):
    path = tampered(
        tmp_path,
        lambda data: data["unsquared_duality"].__setitem__("reduced_e2", "P"),
    )
    with pytest.raises(AssertionError):
        verify(path)


def test_09_common_norm_tamper_fails(tmp_path):
    path = tampered(
        tmp_path,
        lambda data: data["unsquared_duality"].__setitem__("common_norm", "1"),
    )
    with pytest.raises(AssertionError):
        verify(path)


def test_10_residue_class_tamper_fails(tmp_path):
    path = tampered(
        tmp_path,
        lambda data: data["gap_plus_eight"]["residue_to_matrix_class"].__setitem__(
            "3", "even"
        ),
    )
    with pytest.raises(AssertionError):
        verify(path)


def test_11_matrix_entry_tamper_fails(tmp_path):
    path = tampered(
        tmp_path,
        lambda data: data["gap_plus_eight"]["matrix_classes"][0]["C_entries"][0].__setitem__(
            0, "0"
        ),
    )
    with pytest.raises(AssertionError):
        verify(path)


def test_12_matrix_digest_tamper_fails(tmp_path):
    path = tampered(
        tmp_path,
        lambda data: data["gap_plus_eight"]["matrix_classes"][1].__setitem__(
            "W_sha256", "0" * 64
        ),
    )
    with pytest.raises(AssertionError):
        verify(path)


def test_13_krylov_witness_tamper_fails(tmp_path):
    path = tampered(
        tmp_path,
        lambda data: data["gap_plus_eight"]["matrix_classes"][0].__setitem__(
            "krylov_minor_at_lam_3", 0
        ),
    )
    with pytest.raises(AssertionError):
        verify(path)


def test_14_recurrence_tamper_fails(tmp_path):
    path = tampered(
        tmp_path,
        lambda data: data["gap_plus_eight"].__setitem__("order_five_recurrence", "t**5-1"),
    )
    with pytest.raises(AssertionError):
        verify(path)


def test_15_supersession_reason_tamper_fails(tmp_path):
    path = tampered(
        tmp_path,
        lambda data: data["supersedes"].__setitem__("reason", "Task 53 was conclusive"),
    )
    with pytest.raises(AssertionError):
        verify(path)


def test_16_empty_checks_fail(tmp_path):
    path = tampered(tmp_path, lambda data: data.__setitem__("checks", {}))
    with pytest.raises(AssertionError):
        verify(path)


def test_17_duplicate_json_key_fails(tmp_path):
    text = CERTIFICATE.read_text(encoding="utf-8")
    text = text.replace('  "status":', '  "status": "duplicate",\n  "status":', 1)
    path = tmp_path / "duplicate_key.json"
    path.write_text(text, encoding="utf-8")
    with pytest.raises(ValueError):
        verify(path)

"""Focused positive and fail-closed tests for Task 55 orders 34--46."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from verify_target_a_task55_orders_34_46 import CERTIFICATE, load, verify


def certificate_data() -> dict:
    return load(CERTIFICATE)


def tampered(tmp_path: Path, mutation, name: str = "tampered.json") -> Path:
    data = copy.deepcopy(certificate_data())
    mutation(data)
    path = tmp_path / name
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return path


def row(data: dict, n: int) -> dict:
    return next(item for item in data["orders"] if item["n"] == n)


def test_01_independent_checker_passes():
    assert all(verify().values())


def test_02_status_contract_is_n40_only():
    data = certificate_data()
    assert data["status"] == "TASK55_ORDERS_34_46_PARTIAL_N40_ONLY"
    assert data["evidence"] == "COMPUTER_ASSISTED_PROVED_FOR_N40_ONLY"
    assert row(data, 40)["status"] == "CERTIFIED_COUNTEREXAMPLE"
    assert all(
        item["status"] == "OPEN_BOUNDED_SEARCH_ONLY"
        for item in data["orders"]
        if item["n"] != 40
    )


@pytest.mark.parametrize(
    "mutation",
    [
        lambda data: data["orders"].pop(0),
        lambda data: data["orders"].insert(1, copy.deepcopy(data["orders"][0])),
        lambda data: data["orders"].__setitem__(
            slice(0, 2), [data["orders"][1], data["orders"][0]]
        ),
    ],
    ids=["missing", "duplicate", "out-of-order"],
)
def test_10_order_set_tamper_fails(tmp_path, mutation):
    path = tampered(tmp_path, mutation)
    with pytest.raises(AssertionError):
        verify(path)


def test_11_global_status_tamper_fails(tmp_path):
    path = tampered(
        tmp_path,
        lambda data: data.__setitem__("status", "TASK55_ALL_ORDERS_CLASSIFIED"),
    )
    with pytest.raises(AssertionError):
        verify(path)


def test_12_n40_status_tamper_fails(tmp_path):
    path = tampered(
        tmp_path,
        lambda data: row(data, 40).__setitem__("status", "OPEN_BOUNDED_SEARCH_ONLY"),
    )
    with pytest.raises(AssertionError):
        verify(path)


def test_13_open_order_cannot_be_promoted(tmp_path):
    path = tampered(
        tmp_path,
        lambda data: row(data, 46).__setitem__("status", "CERTIFIED_COUNTEREXAMPLE"),
    )
    with pytest.raises(AssertionError):
        verify(path)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("q_bits", "0" + "100010001000100010001000100010001000100"),
        ("alpha", 1),
        ("rational_upper_on_rho_squared", "777/100"),
        ("pivot_sha256", "0" * 64),
        ("certificate_matrix_sha256", "0" * 64),
        ("legacy_candidate_sha256", "0" * 64),
        ("legacy_certificate_sha256", "0" * 64),
    ],
)
def test_20_n40_certificate_tamper_fails(tmp_path, field, value):
    path = tampered(
        tmp_path,
        lambda data: row(data, 40).__setitem__(field, value),
        name=f"tampered_{field}.json",
    )
    with pytest.raises(AssertionError):
        verify(path)


def test_21_bounded_search_cannot_become_nonexistence_proof(tmp_path):
    path = tampered(
        tmp_path,
        lambda data: row(data, 34).__setitem__(
            "logical_scope", "No counterexample exists at this order."
        ),
    )
    with pytest.raises(AssertionError):
        verify(path)


def test_22_all_even_ge32_overclaim_fails(tmp_path):
    path = tampered(
        tmp_path,
        lambda data: data["classification"].__setitem__(
            "all_even_n_ge_32_fail", "PROVED"
        ),
    )
    with pytest.raises(AssertionError):
        verify(path)


def test_23_duplicate_json_key_fails(tmp_path):
    text = CERTIFICATE.read_text(encoding="utf-8")
    text = text.replace(
        '  "status":', '  "status": "duplicate",\n  "status":', 1
    )
    path = tmp_path / "duplicate_key.json"
    path.write_text(text, encoding="utf-8")
    with pytest.raises(ValueError, match="duplicate JSON key"):
        verify(path)

"""Positive and fail-closed tests for the Task 55 small-order verifier."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from verify_target_a_task55_small_order_exact import (
    CERTIFICATE,
    _digest,
    _stream_sha256,
    load_strict,
    verify,
)


def certificate_data() -> dict:
    return load_strict(CERTIFICATE)


def order(data: dict, n: int) -> dict:
    return next(row for row in data["orders"] if row["n"] == n)


def table(data: dict, support: int) -> dict:
    return next(row for row in data["window_tables"] if row["support_length"] == support)


def refresh_payload_hash(data: dict) -> None:
    core = {key: value for key, value in data.items() if key != "payload_core_sha256"}
    data["payload_core_sha256"] = _digest(core)


def refresh_terminal_hashes(data: dict, n: int, index: int | None = None) -> None:
    terminals = order(data, n)["terminal_records"]
    if index is not None:
        record = terminals[index]
        unhashed = {key: value for key, value in record.items() if key != "record_sha256"}
        record["record_sha256"] = _digest(unhashed)
    order(data, n)["terminal_records_sha256"] = _digest(terminals)
    refresh_payload_hash(data)


def write_fixture(tmp_path: Path, data: dict, name: str) -> Path:
    path = tmp_path / name
    path.write_text(
        json.dumps(data, ensure_ascii=True, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="ascii",
    )
    return path


def test_01_independent_verifier_passes() -> None:
    report = verify()
    assert report["status"] == "TARGET_A_TASK55_SMALL_ORDER_EXACT_VERIFY_PASS"
    assert report["terminal_unresolved"] == 0
    assert [row["n"] for row in report["orders"]] == [34, 36, 38, 42, 44, 46]


@pytest.mark.parametrize("mutation", ["missing", "duplicate", "out_of_order"])
def test_10_window_row_set_tamper_fails(tmp_path: Path, mutation: str) -> None:
    data = copy.deepcopy(certificate_data())
    rows = table(data, 12)["rows"]
    if mutation == "missing":
        rows.pop(0)
    elif mutation == "duplicate":
        rows.insert(1, copy.deepcopy(rows[0]))
    else:
        rows[0], rows[1] = rows[1], rows[0]
    table(data, 12)["rows_sha256"] = _stream_sha256(rows)
    refresh_payload_hash(data)
    with pytest.raises(AssertionError):
        verify(write_fixture(tmp_path, data, f"window_rows_{mutation}.json"))


@pytest.mark.parametrize("mutation", ["missing", "duplicate", "out_of_order"])
def test_11_allowed_window_set_tamper_fails(tmp_path: Path, mutation: str) -> None:
    data = copy.deepcopy(certificate_data())
    partition = order(data, 38)["local_window_partition"]
    windows = partition["surviving_window_codes"]
    if mutation == "missing":
        windows.pop(0)
    elif mutation == "duplicate":
        windows.insert(1, windows[0])
    else:
        windows[0], windows[1] = windows[1], windows[0]
    partition["surviving_window_codes_sha256"] = _digest(windows)
    refresh_payload_hash(data)
    with pytest.raises(AssertionError):
        verify(write_fixture(tmp_path, data, f"allowed_windows_{mutation}.json"))


@pytest.mark.parametrize("mutation", ["missing", "duplicate", "out_of_order"])
def test_12_closed_walk_set_tamper_fails(tmp_path: Path, mutation: str) -> None:
    data = copy.deepcopy(certificate_data())
    row = order(data, 42)
    walks = row["rooted_even_Q_codes"]
    if mutation == "missing":
        walks.pop(0)
    elif mutation == "duplicate":
        walks.insert(1, walks[0])
    else:
        walks[0], walks[1] = walks[1], walks[0]
    row["rooted_even_Q_codes_sha256"] = _digest(walks)
    refresh_payload_hash(data)
    with pytest.raises(AssertionError):
        verify(write_fixture(tmp_path, data, f"closed_walks_{mutation}.json"))


@pytest.mark.parametrize("mutation", ["missing", "duplicate", "out_of_order"])
def test_13_terminal_set_tamper_fails(tmp_path: Path, mutation: str) -> None:
    data = copy.deepcopy(certificate_data())
    terminals = order(data, 38)["terminal_records"]
    if mutation == "missing":
        terminals.pop(0)
    elif mutation == "duplicate":
        terminals.insert(1, copy.deepcopy(terminals[0]))
    else:
        terminals[0], terminals[1] = terminals[1], terminals[0]
    refresh_terminal_hashes(data, 38)
    with pytest.raises(AssertionError):
        verify(write_fixture(tmp_path, data, f"terminals_{mutation}.json"))


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("canonical_q_code", 1),
        ("alpha", 0),
        ("integer_vector", [1] + [0] * 33),
    ],
)
def test_20_terminal_semantic_tamper_fails(
    tmp_path: Path, field: str, value: object
) -> None:
    data = copy.deepcopy(certificate_data())
    order(data, 34)["terminal_records"][1][field] = value
    refresh_terminal_hashes(data, 34, 1)
    with pytest.raises(AssertionError):
        verify(write_fixture(tmp_path, data, f"terminal_{field}.json"))


def test_21_threshold_tamper_fails(tmp_path: Path) -> None:
    data = copy.deepcopy(certificate_data())
    order(data, 46)["threshold_squared"]["strict_rational_upper"] = "8"
    refresh_payload_hash(data)
    with pytest.raises(AssertionError):
        verify(write_fixture(tmp_path, data, "threshold.json"))


def test_22_threshold_polynomial_tamper_fails(tmp_path: Path) -> None:
    data = copy.deepcopy(certificate_data())
    order(data, 44)["threshold_squared"]["minimal_polynomial_coefficients"][0] = "2"
    refresh_payload_hash(data)
    with pytest.raises(AssertionError):
        verify(write_fixture(tmp_path, data, "threshold_polynomial.json"))


def test_23_window_vector_tamper_fails(tmp_path: Path) -> None:
    data = copy.deepcopy(certificate_data())
    table(data, 13)["rows"][100][3][0] += 1
    table(data, 13)["rows_sha256"] = _stream_sha256(table(data, 13)["rows"])
    refresh_payload_hash(data)
    with pytest.raises(AssertionError):
        verify(write_fixture(tmp_path, data, "window_vector.json"))


def test_24_hash_tamper_fails(tmp_path: Path) -> None:
    data = copy.deepcopy(certificate_data())
    table(data, 14)["rows_sha256"] = "0" * 64
    refresh_payload_hash(data)
    with pytest.raises(AssertionError):
        verify(write_fixture(tmp_path, data, "rows_hash.json"))


def test_25_terminal_unresolved_tamper_fails(tmp_path: Path) -> None:
    data = copy.deepcopy(certificate_data())
    order(data, 42)["terminal_unresolved"] = 1
    data["global_checks"]["terminal_unresolved_total"] = 1
    refresh_payload_hash(data)
    with pytest.raises(AssertionError):
        verify(write_fixture(tmp_path, data, "terminal_unresolved.json"))


def test_26_duplicate_json_key_fails(tmp_path: Path) -> None:
    text = CERTIFICATE.read_text(encoding="ascii")
    text = text.replace(
        '{"arithmetic_boundary":',
        '{"schema_version":1,"arithmetic_boundary":',
        1,
    )
    path = tmp_path / "duplicate_key.json"
    path.write_text(text, encoding="ascii")
    with pytest.raises(ValueError, match="duplicate JSON key"):
        verify(path)


def test_27_float_and_bool_integer_tamper_fail(tmp_path: Path) -> None:
    raw = CERTIFICATE.read_text(encoding="ascii")
    float_path = tmp_path / "float.json"
    float_path.write_text(raw.replace('"schema_version":1', '"schema_version":1.0', 1), encoding="ascii")
    with pytest.raises(ValueError, match="floating JSON number"):
        verify(float_path)

    data = copy.deepcopy(certificate_data())
    order(data, 34)["terminal_records"][1]["alpha"] = True
    refresh_terminal_hashes(data, 34, 1)
    with pytest.raises(AssertionError):
        verify(write_fixture(tmp_path, data, "bool_alpha.json"))

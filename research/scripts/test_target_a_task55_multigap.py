"""Positive and fail-closed tamper tests for Task 55 Lane D."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from verify_target_a_task55_multigap import MANIFEST, STREAM, load_json_bytes, verify


def stream_rows() -> list[list[list[int]]]:
    return [json.loads(line) for line in STREAM.read_text(encoding="ascii").splitlines()]


def write_rows(tmp_path: Path, rows: list[list[list[int]]]) -> Path:
    path = tmp_path / "multigap_support18.jsonl"
    path.write_text(
        "".join(json.dumps(row, separators=(",", ":")) + "\n" for row in rows),
        encoding="ascii",
    )
    return path


def tampered_manifest(tmp_path: Path, mutation) -> Path:
    data = copy.deepcopy(load_json_bytes(MANIFEST.read_bytes()))
    mutation(data)
    path = tmp_path / "multigap_support18_manifest.json"
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="ascii")
    return path


def test_01_independent_checker_passes() -> None:
    assert all(verify().values())


def test_02_scope_boundary_is_explicitly_open() -> None:
    data = load_json_bytes(MANIFEST.read_bytes())
    assert data["scope"]["total_count"] == 31008
    assert data["three_three_local_lemma"]["status"] == "ANALYTIC_PROVED_ARBITRARY_FINITE_CORE_LENGTH"
    assert data["proof_boundary"]["universal_B0_to_B2"] == "OPEN"


@pytest.mark.parametrize("mutation", ["delete", "duplicate", "disorder"])
def test_03_line_set_tamper_fails(tmp_path: Path, mutation: str) -> None:
    rows = stream_rows()
    if mutation == "delete":
        del rows[17]
    elif mutation == "duplicate":
        rows.insert(18, copy.deepcopy(rows[17]))
    else:
        rows[17], rows[18] = rows[18], rows[17]
    with pytest.raises(AssertionError):
        verify(stream_path=write_rows(tmp_path, rows))


def test_04_word_tamper_fails(tmp_path: Path) -> None:
    rows = stream_rows()
    rows[1][0][-1] += 1
    with pytest.raises(AssertionError):
        verify(stream_path=write_rows(tmp_path, rows))


def test_05_vector_tamper_fails(tmp_path: Path) -> None:
    rows = stream_rows()
    rows[0][1][0] += 1
    with pytest.raises(AssertionError):
        verify(stream_path=write_rows(tmp_path, rows))


def test_06_noncanonical_reflection_fails(tmp_path: Path) -> None:
    rows = stream_rows()
    index = next(i for i, row in enumerate(rows) if row[0] < list(reversed(row[0])))
    rows[index][0].reverse()
    with pytest.raises(AssertionError):
        verify(stream_path=write_rows(tmp_path, rows))


def test_07_gap_four_fails(tmp_path: Path) -> None:
    rows = stream_rows()
    rows[1][0] = [1, 4, 1]
    with pytest.raises(AssertionError):
        verify(stream_path=write_rows(tmp_path, rows))


def test_08_zero_charge_subword_fails(tmp_path: Path) -> None:
    rows = stream_rows()
    rows[1][0] = [1, 7]
    with pytest.raises(AssertionError):
        verify(stream_path=write_rows(tmp_path, rows))


def test_09_wrong_support_length_fails(tmp_path: Path) -> None:
    rows = stream_rows()
    rows[0][1].pop()
    with pytest.raises((AssertionError, ValueError)):
        verify(stream_path=write_rows(tmp_path, rows))


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("tau_anchor", "tau_0=-1"),
        ("support", "I_g=[-1,S+2] intersect Z"),
    ],
)
def test_10_open_interface_manifest_tamper_fails(
    tmp_path: Path, field: str, value: str
) -> None:
    path = tampered_manifest(
        tmp_path,
        lambda data: data["open_interface"].__setitem__(field, value),
    )
    with pytest.raises(AssertionError):
        verify(manifest_path=path)


def test_11_threshold_tamper_fails(tmp_path: Path) -> None:
    path = tampered_manifest(
        tmp_path,
        lambda data: data["strict_threshold"].__setitem__("numerator", 7905369311620327),
    )
    with pytest.raises(AssertionError):
        verify(manifest_path=path)


@pytest.mark.parametrize("field", ["word_sha256", "sha256"])
def test_12_digest_tamper_fails(tmp_path: Path, field: str) -> None:
    path = tampered_manifest(
        tmp_path,
        lambda data: data["stream"].__setitem__(field, "0" * 64),
    )
    with pytest.raises(AssertionError):
        verify(manifest_path=path)


def test_13_duplicate_manifest_key_fails(tmp_path: Path) -> None:
    text = MANIFEST.read_text(encoding="ascii")
    text = text.replace('  "status":', '  "status": "duplicate",\n  "status":', 1)
    path = tmp_path / "duplicate_manifest.json"
    path.write_text(text, encoding="ascii")
    with pytest.raises(ValueError):
        verify(manifest_path=path)


def test_14_trailing_json_fails(tmp_path: Path) -> None:
    lines = STREAM.read_text(encoding="ascii").splitlines(keepends=True)
    lines[0] = lines[0].rstrip("\n") + "[]\n"
    path = tmp_path / "trailing.jsonl"
    path.write_text("".join(lines), encoding="ascii")
    with pytest.raises((json.JSONDecodeError, ValueError)):
        verify(stream_path=path)


@pytest.mark.parametrize("bad_value", [1.5, True, 10**100])
def test_15_forbidden_scalar_fails(tmp_path: Path, bad_value) -> None:
    rows = stream_rows()
    rows[0][1][0] = bad_value
    with pytest.raises(ValueError):
        verify(stream_path=write_rows(tmp_path, rows))


def test_16_whole_vector_sign_tamper_fails(tmp_path: Path) -> None:
    rows = stream_rows()
    rows[0][1] = [-value for value in rows[0][1]]
    with pytest.raises(AssertionError):
        verify(stream_path=write_rows(tmp_path, rows))


def test_17_local_lemma_tamper_fails(tmp_path: Path) -> None:
    path = tampered_manifest(
        tmp_path,
        lambda data: data["three_three_local_lemma"]["cases"][2].__setitem__("N_lower_bound", 837),
    )
    with pytest.raises(AssertionError):
        verify(manifest_path=path)


def test_18_reference_cell_claim_cannot_be_upgraded(tmp_path: Path) -> None:
    path = tampered_manifest(
        tmp_path,
        lambda data: data["proof_boundary"].__setitem__(
            "reference_cell_insertion_removal", "SPECTRAL_EQUIVALENCE"
        ),
    )
    with pytest.raises(AssertionError):
        verify(manifest_path=path)


@pytest.mark.parametrize("encoding_tamper", ["bom", "crlf"])
def test_19_stream_encoding_tamper_fails(
    tmp_path: Path, encoding_tamper: str
) -> None:
    raw = STREAM.read_bytes()
    raw = b"\xef\xbb\xbf" + raw if encoding_tamper == "bom" else raw.replace(b"\n", b"\r\n")
    path = tmp_path / "bad_encoding.jsonl"
    path.write_bytes(raw)
    with pytest.raises(ValueError):
        verify(stream_path=path)


def test_20_c6_dependency_digest_tamper_fails(tmp_path: Path) -> None:
    path = tampered_manifest(
        tmp_path,
        lambda data: data["c6_dependency"].__setitem__("sha256", "0" * 64),
    )
    with pytest.raises(AssertionError):
        verify(manifest_path=path)

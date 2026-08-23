"""Positive and fail-closed tests for the G6 rank-doubling correction."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from verify_target_a_task53_a3 import (
    CERTIFICATE as G6_CERTIFICATE,
    verify as verify_g6,
    verify_symmetry,
)
from verify_target_a_task54_exact_r import (
    CERTIFICATE as RETRACTION_CERTIFICATE,
    verify as verify_retraction,
)


def tampered(tmp_path: Path, source: Path, mutation) -> Path:
    data = json.loads(source.read_text(encoding="utf-8"))
    data = copy.deepcopy(data)
    mutation(data)
    path = tmp_path / source.name
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return path


def test_01_full_g6_global_edge_checker_passes():
    assert all(verify_g6().values())


def test_02_symmetry_checker_passes():
    assert all(verify_symmetry().values())


def test_03_exact_r_retraction_checker_passes():
    assert all(verify_retraction().values())


def test_10_multiplicity_tamper_fails(tmp_path):
    path = tampered(
        tmp_path, G6_CERTIFICATE,
        lambda data: data.__setitem__("squared_level_multiplicity", 1),
    )
    with pytest.raises(AssertionError):
        verify_symmetry(path)


def test_11_anticommutation_tamper_fails(tmp_path):
    path = tampered(
        tmp_path, G6_CERTIFICATE,
        lambda data: data["negative_spectrum_bridge"]["window_records"][0].__setitem__(
            "K_anticommutes_with_A", False
        ),
    )
    with pytest.raises(AssertionError):
        verify_symmetry(path)


def test_12_matrix_hash_tamper_fails(tmp_path):
    path = tampered(
        tmp_path, G6_CERTIFICATE,
        lambda data: data["negative_spectrum_bridge"]["window_records"][1].__setitem__(
            "A_sha256", "0" * 64
        ),
    )
    with pytest.raises(AssertionError):
        verify_symmetry(path)


def test_13_remove_window_fails(tmp_path):
    path = tampered(
        tmp_path, G6_CERTIFICATE,
        lambda data: data["negative_spectrum_bridge"]["window_records"].pop(),
    )
    with pytest.raises(AssertionError):
        verify_symmetry(path)


def test_14_wrong_operator_norm_fails(tmp_path):
    path = tampered(
        tmp_path, G6_CERTIFICATE,
        lambda data: data.__setitem__("global_argument", "Finally ||H6||<=4."),
    )
    with pytest.raises(AssertionError):
        verify_symmetry(path)


def test_15_duplicate_g6_key_fails(tmp_path):
    text = G6_CERTIFICATE.read_text(encoding="utf-8")
    text = text.replace('  "status":', '  "status": "duplicate",\n  "status":', 1)
    path = tmp_path / "duplicate_g6.json"
    path.write_text(text, encoding="utf-8")
    with pytest.raises(ValueError):
        verify_symmetry(path)


def test_20_retraction_status_tamper_fails(tmp_path):
    path = tampered(
        tmp_path, RETRACTION_CERTIFICATE,
        lambda data: data.__setitem__("status", "EXACT_R_R123_BY_COMPLEMENT_GAP_PROVED"),
    )
    with pytest.raises(AssertionError):
        verify_retraction(path)


def test_21_retraction_rank_tamper_fails(tmp_path):
    path = tampered(
        tmp_path, RETRACTION_CERTIFICATE,
        lambda data: data["rank_correction"].__setitem__("single_H_level_rank", 1),
    )
    with pytest.raises(AssertionError):
        verify_retraction(path)


def test_22_retraction_feshbach_dimension_tamper_fails(tmp_path):
    path = tampered(
        tmp_path, RETRACTION_CERTIFICATE,
        lambda data: data["feshbach"].__setitem__("required_dimension", "r"),
    )
    with pytest.raises(AssertionError):
        verify_retraction(path)


def test_23_duplicate_retraction_key_fails(tmp_path):
    text = RETRACTION_CERTIFICATE.read_text(encoding="utf-8")
    text = text.replace('  "status":', '  "status": "duplicate",\n  "status":', 1)
    path = tmp_path / "duplicate_retraction.json"
    path.write_text(text, encoding="utf-8")
    with pytest.raises(ValueError):
        verify_retraction(path)

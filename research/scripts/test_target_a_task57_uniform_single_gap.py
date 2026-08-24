"""Fail-closed tests for the Task 57 uniform single-gap checker."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from verify_target_a_task57_uniform_single_gap import CERTIFICATE, load_strict, verify


def tampered(tmp_path: Path, mutation) -> Path:
    data = copy.deepcopy(load_strict(CERTIFICATE))
    mutation(data)
    path = tmp_path / "uniform_single_gap_separation.json"
    path.write_text(json.dumps(data) + "\n", encoding="utf-8")
    return path


def must_fail(tmp_path: Path, mutation) -> None:
    with pytest.raises((AssertionError, ValueError, KeyError, TypeError)):
        verify(tampered(tmp_path, mutation))


def test_checker_passes() -> None:
    assert all(verify().values())


@pytest.mark.parametrize("index", range(7))
def test_each_numerator_tamper_fails(tmp_path: Path, index: int) -> None:
    must_fail(tmp_path, lambda data: data["rows"][index].__setitem__("witness_numerator", 0))


def test_delta_tamper_fails(tmp_path: Path) -> None:
    must_fail(tmp_path, lambda data: data.__setitem__("uniform_delta", "1/251"))


def test_minimum_class_tamper_fails(tmp_path: Path) -> None:
    must_fail(tmp_path, lambda data: data.__setitem__("minimum_margin_gap_class", "g=7"))


def test_dependency_hash_tamper_fails(tmp_path: Path) -> None:
    must_fail(tmp_path, lambda data: data["dependencies"][0].__setitem__("sha256", "0" * 64))


def test_duplicate_key_fails(tmp_path: Path) -> None:
    text = CERTIFICATE.read_text(encoding="utf-8")
    text = text.replace('  "status":', '  "status": "duplicate",\n  "status":', 1)
    path = tmp_path / "duplicate.json"
    path.write_text(text, encoding="utf-8")
    with pytest.raises(ValueError):
        verify(path)

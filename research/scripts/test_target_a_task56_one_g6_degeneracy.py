from __future__ import annotations

import json
from pathlib import Path

import pytest

from verify_target_a_task56_one_g6_degeneracy import DEPENDENCY, THEOREM, matrix_controls, verify


def test_verifier_passes() -> None:
    assert all(verify().values())


@pytest.mark.parametrize("n", [10, 18, 42, 106, 1042])
def test_exact_finite_controls(n: int) -> None:
    assert all(matrix_controls(n).values())


def test_wrong_residue_rejected() -> None:
    with pytest.raises(AssertionError):
        matrix_controls(1040)


@pytest.mark.parametrize(
    "old,new",
    [
        ("n>=1042", "n>=1034"),
        ("K_n A_n=-A_n K_n", "K_n A_n=A_n K_n"),
        ("multiplicity exactly two", "multiplicity exactly one"),
        ("D=n", "D=n-8"),
    ],
)
def test_theorem_tampering_rejected(tmp_path: Path, old: str, new: str) -> None:
    text = THEOREM.read_text(encoding="utf-8")
    assert old in text
    path = tmp_path / "theorem.md"
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    with pytest.raises(AssertionError):
        verify(theorem_path=path)


@pytest.mark.parametrize(
    "field,value",
    [
        ("integration_status", "PENDING_INDEPENDENT_CHECKER_PASS"),
        ("evidence", "HIGH_PRECISION_DISCOVERY"),
    ],
)
def test_dependency_status_tampering_rejected(tmp_path: Path, field: str, value: str) -> None:
    data = json.loads(DEPENDENCY.read_text(encoding="utf-8"))
    data[field] = value
    path = tmp_path / "dependency.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(AssertionError):
        verify(dependency_path=path)


def test_dependency_constant_tampering_rejected(tmp_path: Path) -> None:
    data = json.loads(DEPENDENCY.read_text(encoding="utf-8"))
    data["constants"]["minimum_interface_distance_D0"] = 1041
    path = tmp_path / "dependency.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(AssertionError):
        verify(dependency_path=path)

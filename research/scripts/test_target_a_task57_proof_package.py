"""Structural tamper tests for the canonical Task 57 proof package."""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from verify_target_a_task57_proof_package import PACKAGE, verify


def copied(tmp_path: Path) -> Path:
    target = tmp_path / "proof_completion"
    shutil.copytree(PACKAGE, target)
    return target


def test_package_passes() -> None:
    assert all(verify().values())


def test_missing_universal_file_fails(tmp_path: Path) -> None:
    package = copied(tmp_path)
    (package / "02_small_order_34_46" / "FULL_PROOF.md").unlink()
    with pytest.raises(AssertionError):
        verify(package)


def test_task_dependency_in_canonical_dag_fails(tmp_path: Path) -> None:
    package = copied(tmp_path)
    path = package / "TARGET_A_FINAL_PROOF_DEPENDENCY_GRAPH.md"
    path.write_text(path.read_text(encoding="utf-8") + "\nTask 53 result\n", encoding="utf-8")
    with pytest.raises(AssertionError):
        verify(package)


def test_missing_terminal_explanation_fails(tmp_path: Path) -> None:
    package = copied(tmp_path)
    for path in (package / "02_small_order_34_46").glob("*.md"):
        path.write_text(path.read_text(encoding="utf-8").replace("64", "sixty-four"), encoding="utf-8")
    with pytest.raises(AssertionError):
        verify(package)


def test_uniform_gap_weakened_fails(tmp_path: Path) -> None:
    package = copied(tmp_path)
    for path in (package / "06_single_gap").glob("*.md"):
        path.write_text(path.read_text(encoding="utf-8").replace("c_6+1/250", "c_6+1/251"), encoding="utf-8")
    with pytest.raises(AssertionError):
        verify(package)


def test_periodic_scope_removed_fails(tmp_path: Path) -> None:
    package = copied(tmp_path)
    for path in (package / "09_moments_periodic").glob("*.md"):
        path.write_text(path.read_text(encoding="utf-8").replace("p<=24", "bounded periods"), encoding="utf-8")
    with pytest.raises(AssertionError):
        verify(package)

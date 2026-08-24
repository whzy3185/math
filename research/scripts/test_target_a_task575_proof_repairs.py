"""Tamper tests for Task 57.5 proof-connection repairs."""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from verify_target_a_task575_proof_repairs import PACKAGE, verify


def copied(tmp_path: Path) -> Path:
    target = tmp_path / "proof_completion"
    shutil.copytree(PACKAGE, target)
    return target


def replace_all(directory: Path, old: str, new: str) -> None:
    for path in directory.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if old in text:
            path.write_text(text.replace(old, new), encoding="utf-8")


def test_real_package_passes() -> None:
    assert all(verify().values())


def test_remove_attainment_dependency_fails(tmp_path: Path) -> None:
    package = copied(tmp_path)
    path = package / "01_even_order_classification" / "DEPENDENCIES.md"
    path.write_text(path.read_text(encoding="utf-8").replace("CANDIDATE_ATTAINMENT_LEMMA.md", "REMOVED_BRIDGE.md"), encoding="utf-8")
    with pytest.raises(AssertionError):
        verify(package, check_git=False)


def test_expand_essential_spectrum_fails(tmp_path: Path) -> None:
    package = copied(tmp_path)
    path = package / "05_g6_edge" / "ESSENTIAL_SPECTRUM_LEMMA.md"
    path.write_text(path.read_text(encoding="utf-8").replace("sigma_ess(H_6)", "unsupported_set(H_6)"), encoding="utf-8")
    with pytest.raises(AssertionError):
        verify(package, check_git=False)


def test_remove_reflection_fails(tmp_path: Path) -> None:
    package = copied(tmp_path)
    replace_all(package / "07_exact_2r", "reflected", "reversed-case-removed")
    with pytest.raises(AssertionError):
        verify(package, check_git=False)


def test_remove_seam_fails(tmp_path: Path) -> None:
    package = copied(tmp_path)
    replace_all(package / "07_exact_2r", "seam", "cut-removed")
    with pytest.raises(AssertionError):
        verify(package, check_git=False)


def test_regress_2r_to_r_fails(tmp_path: Path) -> None:
    package = copied(tmp_path)
    replace_all(package / "07_exact_2r", "2r", "r")
    with pytest.raises(AssertionError):
        verify(package, check_git=False)


def test_change_seven_to_six_fails(tmp_path: Path) -> None:
    package = copied(tmp_path)
    for name in ("TARGET_A_JGT_THEOREM_HIERARCHY.md", "TARGET_A_JGT_PROOF_ARCHITECTURE.md"):
        path = package / name
        path.write_text(path.read_text(encoding="utf-8").replace("seven", "six"), encoding="utf-8")
    with pytest.raises(AssertionError):
        verify(package, check_git=False)


@pytest.mark.parametrize(
    "hazard",
    [
        "research/proofs/task52/TARGET_A_MULTI_SLIP_INTERACTION_ASYMPTOTICS.md",
        "research/proofs/task54/TARGET_A_COMMON_RESIDUE_LIMIT_SCOPE.md",
    ],
)
def test_remove_import_hazard_fails(tmp_path: Path, hazard: str) -> None:
    package = copied(tmp_path)
    path = package / "TARGET_A_MANUSCRIPT_IMPORT_SAFETY.md"
    path.write_text(path.read_text(encoding="utf-8").replace(hazard, "removed/hazard.md"), encoding="utf-8")
    with pytest.raises(AssertionError):
        verify(package, check_git=False)

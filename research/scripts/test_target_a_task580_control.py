"""Tamper tests for the Task 58.0 manuscript control layer."""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from verify_target_a_task580_control import CONTROL, verify


def copied(tmp_path: Path) -> Path:
    target = tmp_path / "task58"
    shutil.copytree(CONTROL, target)
    return target


def test_control_layer_passes() -> None:
    assert all(verify().values())


@pytest.mark.parametrize(
    "file_name,old,new",
    [
        ("TASK58_FIRST_SUBMISSION_SCOPE.md", "DO_NOT_IMPORT_FIRST_SUBMISSION", "REMOVED_SCOPE"),
        ("TASK58_SOURCE_IMPORT_MAP.md", "T8.0", "REMOVED_CLAIM"),
        ("TASK58_MATHEMATICAL_CONTRACT.md", "m_n<rho_-(n)", "m_n<theta_n"),
        ("TASK58_STALE_CLAIM_BLACKLIST.md", "codimension-r", "removed-stale-token"),
        ("TASK58_JGT_VISUAL_STYLE_CONTRACT.md", "no footnotes", "footnotes allowed"),
        ("TASK58_CURRENT_HANDOFF.md", "Task 58.1", "Task 58.3"),
    ],
)
def test_tamper_fails(tmp_path: Path, file_name: str, old: str, new: str) -> None:
    control = copied(tmp_path)
    path = control / file_name
    text = path.read_text(encoding="utf-8")
    assert old in text
    changed = text.replace(old, new)
    if old == "no footnotes":
        changed = changed.replace("No footnotes", "Footnotes allowed")
    path.write_text(changed, encoding="utf-8")
    with pytest.raises(AssertionError):
        verify(control, check_git=False)

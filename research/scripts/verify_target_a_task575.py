"""Unified referee entry point for Task 57 plus the Task 57.5 repairs."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
SCRIPTS = REPO / "research" / "scripts"


def run(script: str) -> None:
    environment = os.environ.copy()
    old_path = environment.get("PYTHONPATH", "")
    environment["PYTHONPATH"] = str(SCRIPTS) + (os.pathsep + old_path if old_path else "")
    completed = subprocess.run(
        [sys.executable, str(SCRIPTS / script)],
        cwd=REPO,
        env=environment,
        check=False,
    )
    if completed.returncode:
        raise SystemExit(f"TASK575_CHECKER_FAILED:{script}:{completed.returncode}")


def main() -> None:
    run("verify_target_a_task57.py")
    run("verify_target_a_task575_proof_repairs.py")
    print("TARGET_A_TASK575_VERIFY_PASS inherited_checkers=13 repair_gates=1")


if __name__ == "__main__":
    main()

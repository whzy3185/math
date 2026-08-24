"""Minimal referee verification entry point for the Task 57 proof package."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
SCRIPTS = REPO / "research" / "scripts"

CHECKERS = (
    "verify_target_a_period8_sharp_constant.py",
    "verify_target_a_minimality_certificate.py",
    "verify_target_a_n32_certificate.py",
    "verify_target_a_task53_a3.py",
    "verify_target_a_task53_p24.py",
    "verify_target_a_task54_threshold.py",
    "verify_target_a_task55_orders_34_46.py",
    "verify_target_a_task55_small_order_exact.py",
    "verify_target_a_task55_exact_2r.py",
    "verify_target_a_task56_single_gap.py",
    "verify_target_a_task56_one_g6_degeneracy.py",
    "verify_target_a_task57_uniform_single_gap.py",
    "verify_target_a_task57_proof_package.py",
)


def main() -> None:
    environment = os.environ.copy()
    old_path = environment.get("PYTHONPATH", "")
    environment["PYTHONPATH"] = str(SCRIPTS) + (os.pathsep + old_path if old_path else "")
    for checker in CHECKERS:
        path = SCRIPTS / checker
        if not path.is_file():
            raise FileNotFoundError(path)
        completed = subprocess.run(
            [sys.executable, str(path)],
            cwd=REPO,
            env=environment,
            text=True,
            check=False,
        )
        if completed.returncode:
            raise SystemExit(f"TASK57_CHECKER_FAILED:{checker}:{completed.returncode}")
    print(f"TARGET_A_TASK57_VERIFY_PASS checkers={len(CHECKERS)}")


if __name__ == "__main__":
    main()

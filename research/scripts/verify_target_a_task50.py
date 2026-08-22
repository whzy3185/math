"""Fail-closed final verifier for Target A Task 50."""

from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path


RESEARCH = Path(__file__).resolve().parents[1]
PROOFS = RESEARCH / "proofs" / "task50"
CERTS = PROOFS / "certificates"
BASELINE = "7f05eddc618bb0e9d772626aa87f4f0f3c17d276"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run() -> None:
    bulk = load(CERTS / "bulk_hyperbolicity_certificates.json")
    require(bulk["status"] == "BULK_HYPERBOLICITY_PROVED", "bulk gate failed")
    require(all(bulk[name]["checks"].values() for name in ("G6","G10")), "bulk rational check failed")
    for name, status in (("g6","G6_INTERFACE_THEOREM_PROVED"),("g10","G10_INTERFACE_THEOREM_PROVED")):
        cert = load(CERTS / f"{name}_interface_certificate.json")
        require(cert["status"] == status and all(cert["checks"].values()), f"{name} interface gate failed")
        require(Fraction(cert["y_interval"][1]) < 8, f"{name} is not below 8")
    independent = load(RESEARCH / "reproducibility" / "task50" / "interface_checker_output.json")
    require(independent["status"] == "TARGET_A_TASK50_INTERFACE_INDEPENDENT_CHECK_PASS", "independent checker failed")
    finite = load(CERTS / "finite_ring_recurrence.json")
    require(finite["status"] == "SINGLE_INTERFACE_BOUND_INCOMPLETE", "finite gate was unsafely upgraded")
    require("TWO_INTERFACE_BOUND_INCOMPLETE" in (PROOFS / "TARGET_A_TWO_INTERFACE_BOUND_STATUS.md").read_text(), "two-interface boundary missing")
    require("ALL_EVEN_THEOREM_INCOMPLETE" in (PROOFS / "TARGET_A_EVENTUAL_THRESHOLD_STATUS.md").read_text(), "all-even boundary missing")
    synthesis = (PROOFS / "TARGET_A_TASK50_SYNTHESIS.md").read_text(encoding="utf-8")
    require("TARGET_A_TASK50_EXACT_INTERFACE_PROVED_FINITE_RING_PENDING" in synthesis, "final status mismatch")
    require(
        subprocess.run(["git","diff","--quiet",BASELINE,"--","research/paper/manuscript_tex_pub","research/paper/manuscript_tex_pub_zh"],cwd=RESEARCH.parent).returncode == 0,
        "manuscript freeze failed",
    )
    print("TARGET_A_TASK50_VERIFY_PASS")


if __name__ == "__main__":
    run()

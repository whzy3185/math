"""Build the reproducible Task 50 exact-proof certificate manifest."""

from __future__ import annotations

import hashlib
import json
import platform
from pathlib import Path

import sympy as sp

from target_a_task47_common import write_json


RESEARCH = Path(__file__).resolve().parents[1]
CERTIFICATES = RESEARCH / "proofs" / "task50" / "certificates"
OUTPUT = RESEARCH / "reproducibility" / "task50"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run() -> dict:
    files = sorted(CERTIFICATES.glob("*.json"))
    payload = {
        "status": "TARGET_A_TASK50_CERTIFICATE_PACKAGE_READY",
        "environment": {
            "python": platform.python_version(),
            "sympy": sp.__version__,
            "integer_rational_arithmetic": "fractions.Fraction and SymPy ZZ/QQ",
            "sqrt_enclosures": "integer isqrt with 120-decimal outward rational endpoints",
        },
        "certificates": [
            {"path": str(path.relative_to(RESEARCH)), "sha256": sha256(path), "bytes": path.stat().st_size}
            for path in files
        ],
        "proved_gates": [
            "BULK_HYPERBOLICITY_PROVED",
            "G6_INTERFACE_THEOREM_PROVED",
            "G10_INTERFACE_THEOREM_PROVED",
        ],
        "incomplete_gates": [
            "SINGLE_INTERFACE_BOUND_INCOMPLETE",
            "TWO_INTERFACE_BOUND_INCOMPLETE",
            "ALL_EVEN_THEOREM_INCOMPLETE",
        ],
        "independent_checker": "research/scripts/verify_target_a_task50_interface.py",
        "checker_output": "research/reproducibility/task50/interface_checker_output.json",
        "formal_manuscript_dependency": False,
    }
    OUTPUT.mkdir(parents=True, exist_ok=True)
    write_json(OUTPUT / "certificate_manifest.json", payload)
    print(payload["status"])
    return payload


if __name__ == "__main__":
    run()

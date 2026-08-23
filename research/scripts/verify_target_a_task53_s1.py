"""Independent exact checker for the Task 53 S1 stop classification."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

from target_a_task52_exact import elimination_resultant


RESEARCH = Path(__file__).resolve().parents[1]
CERTIFICATE = RESEARCH / "proofs" / "task53" / "certificates" / "plus_minus_two_structure.json"


def verify(path: Path = CERTIFICATE) -> dict[str, bool]:
    data = json.loads(path.read_text())
    left, left_record = elimination_resultant(2)
    right, right_record = elimination_resultant(6)
    checks = {
        "resultant_reconstructed": sp.expand(left - right) == 0,
        "factor_multisets_reconstructed": left_record["factors"] == right_record["factors"],
        "negative_search_recorded": len(data["tested_exact_transformations"]) == 4 and not any(
            row["equal_up_to_nonzero_scalar"] for row in data["tested_exact_transformations"]
        ),
        "no_duality_overclaim": data["status"] == "PLUS_MINUS_TWO_ELIMINATION_EQUALITY_ONLY",
        "s3_stopped": data["s3_decision"].startswith("RECURRENCE_ROUTE_WEAK"),
        "artifact_checks_true": all(data["checks"].values()),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return checks


def main() -> None:
    verify()
    print("TARGET_A_TASK53_S1_VERIFY_PASS")


if __name__ == "__main__":
    main()

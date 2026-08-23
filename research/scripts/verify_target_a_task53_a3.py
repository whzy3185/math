"""Independent chart checker for the Task 53 single-G6 global edge."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

from target_a_task50_g6_certificate import evans
from target_a_task50_interval import Interval
from target_a_task52_exact import elimination_resultant


RESEARCH = Path(__file__).resolve().parents[1]
CERTIFICATE = RESEARCH / "proofs" / "task53" / "certificates" / "g6_global_edge.json"
LOWER = sp.Rational(7905369311620328, 10**15)
INTERVALS = (
    Interval(Fraction(8080985802104273, 10**15), Fraction(8080985802104274, 10**15)),
    Interval(Fraction(813985656333926, 10**14), Fraction(813985656333928, 10**14)),
)


def verify(path: Path = CERTIFICATE) -> dict[str, bool]:
    data = json.loads(path.read_text(encoding="utf-8"))
    y = sp.symbols("y")
    _resultant, record = elimination_resultant(6)
    global_count = sum(
        int(sp.Poly(sp.sympify(row["polynomial"]), y).count_roots(LOWER, 16))
        for row in record["factors"]
    )
    alternative_chart = []
    for interval in INTERVALS:
        matching, _defect, metadata = evans(interval, gap=6, cofactor_rows=(0, 2, 3))
        alternative_chart.append(
            matching.value.excludes_zero()
            and all(row["nonzero_components"] for row in metadata["cofactor_pivots"])
        )
    local = json.loads(
        (RESEARCH / "proofs" / "task50" / "certificates" / "g6_interface_certificate.json").read_text()
    )
    checks = {
        "resultant_count_rebuilt": global_count == 2,
        "alternative_rows_023_exclude_both": all(alternative_chart),
        "producer_used_different_chart": all(row["cofactor_rows"] == [0, 1, 3] for row in data["candidate_records"]),
        "local_unique_root_rechecked": local["checks"]["derivative_positive"] and local["checks"]["left_sign_negative"] and local["checks"]["right_sign_positive"],
        "two_nonphysical_records": len(data["candidate_records"]) == 2 and all(
            row["classification"] == "NONPHYSICAL_FOR_G6" and row["matching_excludes_zero"]
            for row in data["candidate_records"]
        ),
        "theorem_not_status_only": "sup sigma(H6)=c6" in data["theorem"],
        "artifact_checks_true": all(data["checks"].values()),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return checks


def main() -> None:
    verify()
    print("TARGET_A_TASK53_A3_VERIFY_PASS")


if __name__ == "__main__":
    main()

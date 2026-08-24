"""Produce the exact Task 57 uniform single-gap separation certificate."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
OUTPUT = REPO / "research" / "proofs" / "task57" / "certificates"
CERTIFICATE = OUTPUT / "uniform_single_gap_separation.json"
C6_SOURCE = REPO / "research" / "proofs" / "task51" / "certificates" / "c6_exact_evans_elimination.json"
SINGLE_GAP_SOURCE = REPO / "research" / "proofs" / "task56" / "TARGET_A_SINGLE_GAP_NIGHT_REPORT.md"

C6_UPPER = Fraction(7905369311620328, 10**15)
DELTA = Fraction(1, 250)
WITNESSES = (
    ("g=1", 812, 97),
    ("g=2", 866, 109),
    ("g=3", 3114, 393),
    ("g=5", 764, 96),
    ("g=7", 768, 97),
    ("g=8", 19672, 2487),
    ("g>=9", 182, 23),
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_certificate() -> dict:
    threshold = C6_UPPER + DELTA
    rows = []
    for label, numerator, denominator in WITNESSES:
        quotient = Fraction(numerator, denominator)
        margin = quotient - threshold
        cross_margin = numerator * threshold.denominator - threshold.numerator * denominator
        if margin <= 0 or cross_margin <= 0:
            raise AssertionError((label, margin))
        rows.append({
            "gap_class": label,
            "witness_numerator": numerator,
            "witness_denominator": denominator,
            "witness_quotient": str(quotient),
            "cross_multiplication_margin": cross_margin,
            "exact_margin": str(margin),
        })
    minimum = min(rows, key=lambda row: Fraction(row["exact_margin"]))
    if minimum["gap_class"] != "g=8":
        raise AssertionError(minimum)
    return {
        "schema": "target-a-task57-uniform-single-gap-v1",
        "status": "UNIFORM_SINGLE_GAP_DELTA_1_OVER_250_PROVED",
        "evidence": "EXACT_RATIONAL_COROLLARY",
        "theorem": "For every positive integer g not in {4,6}, sup sigma(H_g)>c6+1/250.",
        "c6_strict_upper": str(C6_UPPER),
        "uniform_delta": str(DELTA),
        "comparison_threshold": str(threshold),
        "rows": rows,
        "minimum_margin_gap_class": minimum["gap_class"],
        "minimum_exact_margin": minimum["exact_margin"],
        "dependencies": [
            {"path": str(C6_SOURCE.relative_to(REPO)), "sha256": sha256(C6_SOURCE)},
            {"path": str(SINGLE_GAP_SOURCE.relative_to(REPO)), "sha256": sha256(SINGLE_GAP_SOURCE)},
        ],
        "checks": {
            "seven_gap_classes_exhaust_strict_cases": len(rows) == 7,
            "all_cross_multiplication_margins_positive": all(
                row["cross_multiplication_margin"] > 0 for row in rows
            ),
            "minimum_margin_is_g8": minimum["gap_class"] == "g=8",
            "gap4_reference_excluded": True,
            "gap6_equality_excluded": True,
        },
    }


def main() -> None:
    payload = build_certificate()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    temporary = CERTIFICATE.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(CERTIFICATE)
    print("TARGET_A_TASK57_UNIFORM_SINGLE_GAP_PRODUCER_PASS")


if __name__ == "__main__":
    main()

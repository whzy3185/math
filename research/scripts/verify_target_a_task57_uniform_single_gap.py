"""Independent exact checker for the Task 57 uniform single-gap corollary."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[2]
CERTIFICATE = REPO / "research" / "proofs" / "task57" / "certificates" / "uniform_single_gap_separation.json"
THEOREM = REPO / "research" / "proofs" / "task57" / "TARGET_A_UNIFORM_SINGLE_GAP_SEPARATION.md"
C6_SOURCE = REPO / "research" / "proofs" / "task51" / "certificates" / "c6_exact_evans_elimination.json"
SINGLE_GAP_SOURCE = REPO / "research" / "proofs" / "task56" / "TARGET_A_SINGLE_GAP_NIGHT_REPORT.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate key: {key}")
        result[key] = value
    return result


def load_strict(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=strict_object)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(path: Path = CERTIFICATE) -> dict[str, bool]:
    data = load_strict(path)
    expected = (
        ("g=1", 812, 97),
        ("g=2", 866, 109),
        ("g=3", 3114, 393),
        ("g=5", 764, 96),
        ("g=7", 768, 97),
        ("g=8", 19672, 2487),
        ("g>=9", 182, 23),
    )
    c6_upper = Fraction(7905369311620328, 10**15)
    delta = Fraction(1, 250)
    threshold = c6_upper + delta
    rows = data.get("rows", [])
    require(len(rows) == len(expected), "row count")
    margins = []
    for row, (label, numerator, denominator) in zip(rows, expected):
        quotient = Fraction(numerator, denominator)
        margin = quotient - threshold
        cross = numerator * threshold.denominator - threshold.numerator * denominator
        require(row.get("gap_class") == label, "gap class")
        require(row.get("witness_numerator") == numerator, "numerator")
        require(row.get("witness_denominator") == denominator, "denominator")
        require(row.get("witness_quotient") == str(quotient), "quotient")
        require(row.get("cross_multiplication_margin") == cross > 0, "cross margin")
        require(row.get("exact_margin") == str(margin) and margin > 0, "exact margin")
        margins.append((margin, label))
    minimum = min(margins)
    require(minimum[1] == "g=8", "minimum class")
    require(data.get("status") == "UNIFORM_SINGLE_GAP_DELTA_1_OVER_250_PROVED", "status")
    require(data.get("evidence") == "EXACT_RATIONAL_COROLLARY", "evidence")
    require(data.get("c6_strict_upper") == str(c6_upper), "c6 upper")
    require(data.get("uniform_delta") == str(delta), "delta")
    require(data.get("comparison_threshold") == str(threshold), "threshold")
    require(data.get("minimum_margin_gap_class") == "g=8", "minimum metadata")
    require(data.get("minimum_exact_margin") == str(minimum[0]), "minimum margin")
    expected_dependencies = [
        {"path": str(C6_SOURCE.relative_to(REPO)), "sha256": sha256(C6_SOURCE)},
        {"path": str(SINGLE_GAP_SOURCE.relative_to(REPO)), "sha256": sha256(SINGLE_GAP_SOURCE)},
    ]
    require(data.get("dependencies") == expected_dependencies, "dependency binding")
    c6_source = load_strict(C6_SOURCE).get("c6", {})
    require(c6_source.get("status") == "C6_DEGREE10_EVANS_POLYNOMIAL_PROVED", "c6 status")
    require(c6_source.get("unique_root_in_interval") is True, "c6 root isolation")
    require(c6_source.get("c6_interval", [None, None])[1] == str(c6_upper), "c6 upper source")
    checks = data.get("checks", {})
    require(set(checks) == {
        "seven_gap_classes_exhaust_strict_cases",
        "all_cross_multiplication_margins_positive",
        "minimum_margin_is_g8",
        "gap4_reference_excluded",
        "gap6_equality_excluded",
    } and all(value is True for value in checks.values()), "checks")
    theorem = THEOREM.read_text(encoding="utf-8")
    require("sup sigma(H_g)>c6+1/250" in theorem, "theorem statement")
    require("174815250030533/310875000000000000" in theorem, "minimum exact margin")
    return {
        "strict_parser": True,
        "seven_exact_comparisons": True,
        "minimum_margin_g8": True,
        "dependency_hashes": True,
        "c6_source_interval_rebuilt": True,
        "theorem_contract": True,
    }


if __name__ == "__main__":
    require(all(verify().values()), "verification")
    print("TARGET_A_TASK57_UNIFORM_SINGLE_GAP_VERIFY_PASS")

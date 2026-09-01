"""Verify the exact arithmetic and row accounting of the analytic tail compression."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
CERT = REPO / "research/proofs/task54/TARGET_A_TASK54_EVENTUAL_THRESHOLD_CERTIFICATE.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def orders(residue: int, lower: int, upper: int) -> list[int]:
    return [n for n in range(lower, upper + 1, 2) if n % 8 == residue]


def verify() -> dict[str, int]:
    data = json.loads(CERT.read_text(encoding="utf-8"))
    analytic = data["analytic"]
    endpoint = analytic["endpoint_checks"]
    last = analytic["last_analytic_failures"]
    require(last == {"0": 32, "2": 90, "4": 164, "6": 238},
            "unexpected residue threshold ledger")
    require(endpoint["2"]["n"] == 242 and endpoint["4"]["n"] == 244 and endpoint["6"]["n"] == 246,
            "certificate endpoint convention changed")

    eta_upper = Fraction(1561, 200)
    n32_lower = Fraction(8) - Fraction(5 * 987, 100 * 256)
    require(eta_upper < n32_lower, "period-eight family does not reach n=32")
    benchmark_lower = Fraction(8) - Fraction(200, 48 * 48)
    require(eta_upper < benchmark_lower, "period-eight comparison is not strict")

    finite = data["finite_tail"]["records"]
    require(len(finite) == 96, "old bridge is not the expected 96 rows")
    remaining = (
        orders(2, 48, 90)
        + orders(4, 48, 164)
        + orders(6, 48, 238)
    )
    require(len(orders(2, 48, 90)) == 6, "residue-two count mismatch")
    require(len(orders(4, 48, 164)) == 15, "residue-four count mismatch")
    require(len(orders(6, 48, 238)) == 24, "residue-six count mismatch")
    require(len(remaining) == 45, "compressed bridge count mismatch")
    require({row["n"] for row in finite}.issuperset(remaining),
            "compressed finite rows are absent from the old bridge")
    return {"old_rows": len(finite), "removed_rows": len(finite) - len(remaining), "remaining_rows": len(remaining)}


if __name__ == "__main__":
    print("TARGET_A_TAIL_COMPRESSION_PASS", verify())

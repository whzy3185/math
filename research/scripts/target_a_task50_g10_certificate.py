"""Rigorous G10 Evans zero certificate using the validated G6 route."""

from __future__ import annotations

import json
import platform
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp

from target_a_task47_common import write_json
from target_a_task50_g6_certificate import evans, symbolic_defect_transfer
from target_a_task50_interval import Interval, interval_record


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "proofs" / "task50" / "certificates"
GAP = 10
Y_LEFT = Fraction(7977104370400546, 10**15)
Y_RIGHT = Fraction(7977104370400547, 10**15)


def run() -> dict[str, Any]:
    interval = Interval(Y_LEFT, Y_RIGHT)
    left_value, _left_defect, left_meta = evans(Interval.point(Y_LEFT), GAP)
    right_value, _right_defect, right_meta = evans(Interval.point(Y_RIGHT), GAP)
    enclosure, _defect, interval_meta = evans(interval, GAP)
    checks = {
        "ordered_rational_interval": Y_LEFT < Y_RIGHT,
        "inside_bulk_G10_interval": Fraction(7977, 1000) < Y_LEFT < Y_RIGHT < Fraction(3989, 500),
        "left_sign_negative": left_value.value.sign() == -1,
        "right_sign_positive": right_value.value.sign() == 1,
        "derivative_positive": enclosure.derivative.lo > 0,
        "all_cofactor_vectors_nonzero": all(row["nonzero_components"] for row in interval_meta["cofactor_pivots"]),
        "upper_endpoint_below_8": Y_RIGHT < 8,
    }
    if not all(checks.values()):
        raise AssertionError(f"G10 interval Evans certificate failed: {checks}")
    symbolic = symbolic_defect_transfer(GAP)
    if symbolic["determinant"] != "1":
        raise AssertionError("G10 defect transfer is not unimodular")
    payload = {
        "status": "G10_INTERFACE_THEOREM_PROVED",
        "method": "exact rational interval Evans determinant with automatic derivative enclosure",
        "arithmetic": {
            "rational_endpoints": True,
            "sqrt_outward_decimal_digits": 120,
            "python": platform.python_version(),
            "sympy": sp.__version__,
        },
        "y_interval": [str(Y_LEFT), str(Y_RIGHT)],
        "left_evans": interval_record(left_value.value),
        "right_evans": interval_record(right_value.value),
        "derivative_on_interval": interval_record(enclosure.derivative),
        "interval_metadata": interval_meta,
        "endpoint_metadata": {"left": left_meta, "right": right_meta},
        "checks": checks,
        "localization": {
            "bulk_cell_rate": "4/15",
            "statement": "the matched state decays by at most C*(4/15)^|j| in period-eight bulk cells",
        },
        "defect_transfer": symbolic,
        "proof_boundary": "Existence and simplicity use IVT plus a strictly positive interval derivative; no floating value or empirical constant enters acceptance.",
    }
    OUTPUT.mkdir(parents=True, exist_ok=True)
    write_json(OUTPUT / "g10_defect_transfer.json", symbolic)
    write_json(OUTPUT / "g10_interface_certificate.json", payload)
    print(json.dumps({
        "status": payload["status"],
        "interval": payload["y_interval"],
        "left_sign": left_value.value.sign(),
        "right_sign": right_value.value.sign(),
        "derivative_sign": enclosure.derivative.sign(),
    }, indent=2))
    return payload


if __name__ == "__main__":
    run()

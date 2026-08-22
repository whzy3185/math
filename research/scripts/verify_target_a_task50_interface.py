"""Independent-coordinate verifier for the Task 50 interface certificates."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

from target_a_task47_common import write_json
from target_a_task50_bulk import TAU, monodromy
from target_a_task50_g6_certificate import evans
from target_a_task50_interval import Interval, interval_record


RESEARCH = Path(__file__).resolve().parents[1]
CERTIFICATES = RESEARCH / "proofs" / "task50" / "certificates"
OUTPUT = RESEARCH / "reproducibility" / "task50"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(name: str):
    return json.loads((CERTIFICATES / name).read_text(encoding="utf-8"))


def verify_bulk() -> dict:
    lam, y, z = sp.symbols("lambda y z")
    matrix = monodromy(lam)
    characteristic = sp.Poly(matrix.charpoly(z).as_expr(), z)
    expected = sp.Poly(
        z**4
        + (-2 * y**2 + 16 * y - 13) * z**3
        + (y**4 - 16 * y**3 + 80 * y**2 - 128 * y + 40) * z**2
        + (-2 * y**2 + 16 * y - 13) * z
        + 1,
        z,
    )
    require(sp.Poly(characteristic.as_expr().subs(lam**2, y), z) == expected, "independent M8 mismatch")
    require(tuple(load("bulk_symbolic.json")["tau_cell"]) == TAU, "tau cell mismatch")
    bulk = load("bulk_hyperbolicity_certificates.json")
    for family in ("G6", "G10"):
        require(all(bulk[family]["checks"].values()), f"stored {family} bulk check failed")
    return {"characteristic_reproduced": True, "stored_rational_checks": True}


def verify_interface(filename: str, gap: int) -> dict:
    payload = load(filename)
    left, right = map(Fraction, payload["y_interval"])
    # The independent coordinate chart takes cofactors of the last three
    # monodromy rows, rather than the first three rows used by the producer.
    left_value, _left_defect, left_meta = evans(Interval.point(left), gap, (1, 2, 3))
    right_value, _right_defect, right_meta = evans(Interval.point(right), gap, (1, 2, 3))
    enclosure, _defect, interval_meta = evans(Interval(left, right), gap, (1, 2, 3))
    require(left_value.value.sign() * right_value.value.sign() == -1, f"G{gap} alternate chart has no sign change")
    require(enclosure.derivative.excludes_zero(), f"G{gap} alternate derivative contains zero")
    require(all(row["nonzero_components"] for row in interval_meta["cofactor_pivots"]), f"G{gap} alternate cofactors vanish")
    require(right < 8, f"G{gap} upper endpoint is not below 8")
    return {
        "gap": gap,
        "cofactor_rows": [1, 2, 3],
        "left_evans": interval_record(left_value.value),
        "right_evans": interval_record(right_value.value),
        "derivative": interval_record(enclosure.derivative),
        "left_metadata": left_meta,
        "right_metadata": right_meta,
        "status": "INDEPENDENT_COORDINATE_CHECK_PASS",
    }


def run() -> dict:
    payload = {
        "status": "TARGET_A_TASK50_INTERFACE_INDEPENDENT_CHECK_PASS",
        "bulk": verify_bulk(),
        "G6": verify_interface("g6_interface_certificate.json", 6),
        "G10": verify_interface("g10_interface_certificate.json", 10),
        "independence_boundary": "The checker uses the last-three-row cofactor chart; the producer uses the first-three-row chart. Both share the exact rational interval kernel.",
    }
    OUTPUT.mkdir(parents=True, exist_ok=True)
    write_json(OUTPUT / "interface_checker_output.json", payload)
    print(payload["status"])
    return payload


if __name__ == "__main__":
    run()

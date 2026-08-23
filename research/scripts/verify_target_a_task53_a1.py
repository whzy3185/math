"""Independent reconstruction checker for Task 53 Gate A1."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


RESEARCH = Path(__file__).resolve().parents[1]
CERTIFICATE = RESEARCH / "proofs" / "task53" / "certificates" / "bulk_global_hyperbolicity.json"
C6_UPPER = sp.Rational(7905369311620328, 10**15)


def verify(path: Path = CERTIFICATE) -> dict[str, bool]:
    data = json.loads(path.read_text(encoding="utf-8"))
    y, z, w = sp.symbols("y z w")
    chi = sp.Poly(sp.sympify(data["characteristic_polynomial"]), z)
    expected_a = -2 * y**2 + 16 * y - 13
    expected_b = y**4 - 16 * y**3 + 80 * y**2 - 128 * y + 40
    expected = sp.Poly(z**4 + expected_a * z**3 + expected_b * z**2 + expected_a * z + 1, z)
    reduced = sp.Poly(w**2 + expected_a * w + expected_b - 2, w)
    dw = sp.factor(sp.discriminant(reduced.as_expr(), w))
    dz = sp.factor(sp.discriminant(expected.as_expr(), z))
    eta_poly = sp.Poly(reduced.as_expr().subs(w, 2), y)
    critical_poly = sp.Poly(12 * y**2 - 96 * y - 17, y)
    critical = 4 + sp.sqrt(627) / 6
    checks = {
        "polynomial_reconstructed": chi == expected,
        "reciprocal": expected.all_coeffs() == list(reversed(expected.all_coeffs())),
        "lift_reconstructed": sp.Poly(sp.expand(z**2 * reduced.as_expr().subs(w, z + 1 / z)), z) == expected,
        "discriminant_reconstructed": str(dw) == data["w_discriminant"] and str(dz) == data["z_discriminant"],
        "eta_is_largest_plus_endpoint_root": eta_poly.count_roots(C6_UPPER, 16) == 0,
        "minus_endpoint_absent": sp.Poly(reduced.as_expr().subs(w, -2), y).count_roots(C6_UPPER, 16) == 0,
        "one_critical_energy": critical_poly.count_roots(C6_UPPER, 16) == 1,
        "critical_inside": C6_UPPER < critical < 16,
        "critical_w": sp.simplify(-expected_a.subs(y, critical) / 2) == sp.Rational(95, 12),
        "three_geometry_cells": len(data["root_geometry"]) == 3,
        "dimensions": all(row["stable_dimension"] == row["unstable_dimension"] == 2 for row in data["root_geometry"]),
        "artifact_interval_bound": data["energy_interval"] == [str(C6_UPPER), "16"],
        "artifact_checks_true": all(data["checks"].values()),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return checks


def main() -> None:
    verify()
    print("TARGET_A_TASK53_A1_VERIFY_PASS")


if __name__ == "__main__":
    main()

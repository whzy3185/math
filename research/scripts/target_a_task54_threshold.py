"""Task 54 analytic threshold and compressed exact finite-tail certificates."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np

from target_a_flux_search import signing_from_q
from target_a_reproduce import numpy_matrix
from target_a_task47_common import write_json
from target_a_task48a_common import canonical_code, q_from_gaps, sparse_exact_ldl_positive
from target_a_task53_global import residue_gap_word


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "proofs" / "task54"
G6_GLOBAL_EDGE = RESEARCH / "proofs" / "task53" / "certificates" / "g6_global_edge.json"
C6_UPPER = Fraction(7905369311620328, 10**15)
ETA_UPPER = Fraction(1561, 200)
N_TAIL = 240
N_STAR = 48


def exact_tent_translation_difference(radius: int, distance: int) -> Fraction:
    denominator = radius * (2 * radius * radius + 1)
    numerators = {
        1: 6 * radius,
        2: 6 * (4 * radius - 3),
        3: 18 * (3 * radius - 4),
        4: 12 * (8 * radius - 15),
    }
    return Fraction(numerators[distance], denominator)


def exact_ims_error(radius: int) -> Fraction:
    return (
        2 * exact_tent_translation_difference(radius, 1)
        + exact_tent_translation_difference(radius, 2)
        + 2 * exact_tent_translation_difference(radius, 3)
        + exact_tent_translation_difference(radius, 4)
    )


def separation(n: int) -> int | None:
    residue = n % 8
    if residue == 0:
        return None
    k = (n - residue) // 8
    if residue == 2:
        return n
    if residue == 4:
        return n // 2
    if residue == 6:
        return 6 + 4 * ((2 * k - 3) // 3)
    raise ValueError("even order required")


def radius_from_separation(distance: int) -> int:
    return (distance - 9) // 2


def threshold_lower(n: int) -> Fraction:
    return Fraction(8) - Fraction(200, n * n)


def analytic_upper(n: int) -> Fraction:
    if n % 8 == 0:
        return ETA_UPPER
    radius = radius_from_separation(separation(n))
    return C6_UPPER + exact_ims_error(radius)


def gap_word(n: int) -> tuple[str, list[int]]:
    residue = n % 8
    if residue == 0:
        return "PERIOD_EIGHT", [4] * (n // 4)
    labels = {2: "ONE_G6", 4: "TWO_BALANCED_G6", 6: "THREE_BALANCED_G6"}
    return labels[residue], residue_gap_word(residue, (n - residue) // 8)


def _digest_pivots(pivots: list[Fraction]) -> str:
    payload = "\n".join(f"{value.numerator}/{value.denominator}" for value in pivots).encode()
    return hashlib.sha256(payload).hexdigest()


def finite_witness(n: int) -> dict[str, Any]:
    family, gaps = gap_word(n)
    q = q_from_gaps(n, gaps)
    alpha = -1 if n % 4 == 0 else 1
    lower = threshold_lower(n)
    denominator = 10**6
    bound = Fraction((lower.numerator * denominator) // lower.denominator - 1, denominator)
    signing = signing_from_q(canonical_code(q), n, alpha)
    canonical = canonical_code(q)
    matrix = numpy_matrix(signing).astype(np.int64)
    certificate_matrix = (
        bound.numerator * np.eye(n, dtype=np.int64)
        - bound.denominator * (matrix @ matrix)
    )
    ldl = sparse_exact_ldl_positive(certificate_matrix)
    if not ldl["positive"] or not bound < lower:
        raise AssertionError((n, family, bound, lower, ldl["pivots"][-1]))
    q_bytes = "".join("1" if value == 1 else "0" for value in q).encode()
    matrix_bytes = (
        json.dumps(certificate_matrix.tolist(), separators=(",", ":")) + "\n"
    ).encode()
    return {
        "n": n,
        "residue": n % 8,
        "family": family,
        "gap_word": gaps,
        "alpha": alpha,
        "canonical_q_hex": hex(canonical),
        "rational_upper_on_rho_squared": str(bound),
        "antibalanced_rational_lower": str(lower),
        "exact_sparse_ldl_positive": True,
        "pivot_count": len(ldl["pivots"]),
        "pivot_sha256": _digest_pivots(ldl["pivots"]),
        "q_sha256": hashlib.sha256(q_bytes).hexdigest(),
        "certificate_matrix_sha256": hashlib.sha256(matrix_bytes).hexdigest(),
        "certificate_matrix_encoding": "canonical compact JSON integer rows with LF",
    }


def build_certificate() -> dict[str, Any]:
    g6_global_edge = json.loads(G6_GLOBAL_EDGE.read_text(encoding="utf-8"))
    translation_formulas = {
        str(distance): str(exact_tent_translation_difference(17, distance))
        for distance in range(1, 5)
    }
    endpoints = {}
    for n in (240, 242, 244, 246):
        endpoints[str(n % 8)] = {
            "n": n,
            "separation": separation(n),
            "radius": None if n % 8 == 0 else radius_from_separation(separation(n)),
            "upper": str(analytic_upper(n)),
            "threshold_lower": str(threshold_lower(n)),
            "strict": analytic_upper(n) < threshold_lower(n),
        }
    last_failures = {}
    for residue in (0, 2, 4, 6):
        tested = [n for n in range(8, 247, 2) if n % 8 == residue]
        admissible = [
            n for n in tested
            if residue == 0 or radius_from_separation(separation(n)) >= 4
        ]
        failures = [n for n in admissible if analytic_upper(n) >= threshold_lower(n)]
        last_failures[str(residue)] = max(failures) if failures else None

    witnesses = [finite_witness(n) for n in range(N_STAR, N_TAIL, 2)]
    ordered_digest = hashlib.sha256()
    for row in witnesses:
        ordered_digest.update(json.dumps(row, sort_keys=True, separators=(",", ":")).encode())

    checks = {
        "exact_error_closed_form": all(
            exact_ims_error(radius) == Fraction(240 * radius - 342, radius * (2 * radius * radius + 1))
            for radius in range(4, 400)
        ),
        "simple_error_bound_120_over_R2": all(
            exact_ims_error(radius) <= Fraction(120, radius * radius)
            for radius in range(4, 400)
        ),
        "maximal_simple_radius_condition": all(
            2 * (radius_from_separation(distance) + 4) < distance
            for distance in range(12, 500)
        ),
        "all_analytic_endpoint_checks": all(row["strict"] for row in endpoints.values()),
        "last_failure_table": last_failures == {"0": 32, "2": 90, "4": 164, "6": 238},
        "finite_tail_complete": [row["n"] for row in witnesses] == list(range(48, 240, 2)),
        "all_finite_ldl_positive": all(row["exact_sparse_ldl_positive"] for row in witnesses),
        "all_finite_bounds_strict": all(
            Fraction(row["rational_upper_on_rho_squared"]) < Fraction(row["antibalanced_rational_lower"])
            for row in witnesses
        ),
        "g6_negative_spectrum_bridge_bound": (
            g6_global_edge["status"] == "GATE_A3_PASS_G6_GLOBAL_EDGE_PROVED"
            and g6_global_edge["squared_level_multiplicity"] == 2
            and g6_global_edge["negative_spectrum_bridge"]["tau_identity_exact"]
            and all(
                row["K_anticommutes_with_A"] and row["K_commutes_with_H"]
                for row in g6_global_edge["negative_spectrum_bridge"]["window_records"]
            )
        ),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "status": "TASK54_EVENTUAL_THRESHOLD_N_STAR_48_PROVED",
        "evidence": "COMPUTER_ASSISTED_PROVED",
        "N_Task53": 2500,
        "N_tail": N_TAIL,
        "N_star": N_STAR,
        "N_observed": N_STAR,
        "analytic": {
            "g6_global_edge_dependency": {
                "path": "research/proofs/task53/certificates/g6_global_edge.json",
                "sha256": hashlib.sha256(G6_GLOBAL_EDGE.read_bytes()).hexdigest(),
                "status": g6_global_edge["status"],
                "squared_level_multiplicity": g6_global_edge["squared_level_multiplicity"],
                "negative_spectrum_bridge": "K^2=-I and KA=-AK",
            },
            "tent_normalization": "(2R^2+1)/(3R)",
            "translation_differences_at_R17": translation_formulas,
            "exact_ims_error": "(240R-342)/(R(2R^2+1))",
            "simple_ims_error": "<=120/R^2",
            "patch_condition": "2(R+4)<D",
            "radius": "R=floor((D-9)/2)",
            "separations": {"2": "n", "4": "n/2", "6": "6+4 floor((2k-3)/3)"},
            "endpoint_checks": endpoints,
            "last_analytic_failures": last_failures,
            "monotonicity": (
                "Within each residue subsequence D and R are nondecreasing, the exact IMS error "
                "decreases for R>=4, and 8-200/n^2 increases."
            ),
        },
        "finite_tail": {
            "orders": [N_STAR, N_TAIL - 2],
            "count": len(witnesses),
            "certificate_method": "exact sparse rational LDL of pI-qA^2 for t=p/q",
            "acceptance": "rho(A)^2<p/q<8-200/n^2<rho_-(n)^2",
            "ordered_record_sha256": ordered_digest.hexdigest(),
            "records": witnesses,
        },
        "theorem": "Every even n>=48 has an explicit certified counterexample.",
        "scope": (
            "N_star=48 is a proved contiguous explicit-witness threshold, not a globally minimal "
            "counterexample onset. N_observed records the same structured-family census only."
        ),
        "checks": checks,
    }


def run() -> dict[str, Any]:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    payload = build_certificate()
    write_json(OUTPUT / "TARGET_A_TASK54_EVENTUAL_THRESHOLD_CERTIFICATE.json", payload)
    print(json.dumps({"status": payload["status"], "finite_rows": payload["finite_tail"]["count"]}, indent=2))
    return payload


if __name__ == "__main__":
    run()

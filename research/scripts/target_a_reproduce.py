"""Reproduce the finite checks reported for Target A.

The exhaustive loop uses floating eigensolvers only to propose an integer
Rayleigh vector.  Acceptance of every non-optimizer class is certified by a
rational Rayleigh quotient above a certified algebraic upper bound.  Any
uncertain class falls back to the exact verifier.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from target_a_verifier import (  # noqa: E402
    Signing,
    exact_sign,
    flux_invariants,
    is_strict_counterexample,
    rational_interval,
    signed_adjacency,
    threshold_squared,
)


def signing_from_class_code(n: int, code: int) -> Signing:
    """Unique spanning-tree gauge: n-1 step-1 signs fixed positive."""
    step1 = [1] * n
    step1[-1] = -1 if code & 1 else 1
    step2 = [-1 if code & (1 << (i + 1)) else 1 for i in range(n)]
    return Signing(n, tuple(step1), tuple(step2))


def signing_from_flux(n: int, tau0: int, alpha: int) -> Signing:
    step1 = [1] * n
    step1[-1] = alpha
    triangles = [tau0 * ((-1) ** i) for i in range(n)]
    step2 = [
        triangles[i] * step1[i] * step1[(i + 1) % n]
        for i in range(n)
    ]
    return Signing(n, tuple(step1), tuple(step2))


def numpy_matrix(signing: Signing) -> np.ndarray:
    n = signing.n
    matrix = np.zeros((n, n), dtype=np.int64)
    for i, sign in enumerate(signing.step1):
        j = (i + 1) % n
        matrix[i, j] = matrix[j, i] = sign
    for i, sign in enumerate(signing.step2):
        j = (i + 2) % n
        matrix[i, j] = matrix[j, i] = sign
    return matrix


def integer_rayleigh_lower_bound(matrix: np.ndarray, scale: int = 10**9) -> Fraction:
    values, vectors = np.linalg.eigh(matrix.astype(float))
    index = int(np.argmax(np.abs(values)))
    vector = np.rint(vectors[:, index] * scale).astype(np.int64)
    if not np.any(vector):
        vector[index % len(vector)] = 1
    image = matrix @ vector
    numerator = sum(int(x) * int(x) for x in image)
    denominator = sum(int(x) * int(x) for x in vector)
    return Fraction(numerator, denominator)


def exact_optimizer_check(signing: Signing) -> dict[str, object]:
    matrix = signed_adjacency(signing)
    square = matrix * matrix
    threshold = threshold_squared(signing.n)
    x = sp.Symbol("x")
    polynomial = sp.Poly(square.charpoly(x).as_expr(), x, domain=sp.ZZ)
    if sp.simplify(polynomial.as_expr().subs(x, threshold)) != 0:
        raise AssertionError("paper optimizer does not have threshold^2 as an eigenvalue")
    intervals = polynomial.intervals(eps=sp.Rational(1, 10**25))
    containing = []
    for interval, multiplicity in intervals:
        left, right = interval
        if exact_sign(threshold - left) >= 0 and exact_sign(right - threshold) >= 0:
            containing.append((interval, multiplicity))
    if not containing or containing[-1] != intervals[-1]:
        raise AssertionError("threshold^2 is not the largest eigenvalue of A^2")
    return {
        "charpoly_A2": str(polynomial.as_expr()),
        "threshold_root_interval": [str(containing[-1][0][0]), str(containing[-1][0][1])],
        "multiplicity": containing[-1][1],
    }


def reproduce_n(n: int, exhaustive: bool) -> dict[str, object]:
    started = time.time()
    threshold = threshold_squared(n)
    lower, upper = rational_interval(threshold, digits=25)
    optimizer_codes = set()
    optimizer_details = []
    for tau0 in (1, -1):
        signing = signing_from_flux(n, tau0, -1)
        code = (1 if signing.step1[-1] == -1 else 0)
        for i, sign in enumerate(signing.step2):
            if sign == -1:
                code |= 1 << (i + 1)
        optimizer_codes.add(code)
        optimizer_details.append(exact_optimizer_check(signing))

    constraint_rows = []
    for i in range(n):
        row = 0
        # In tree gauge, Q_i flux is a linear form in free signs.
        for code_bit in range(n + 1):
            probe = signing_from_class_code(n, 1 << code_bit)
            base = signing_from_class_code(n, 0)
            q_probe = flux_invariants(probe)["quadrilaterals"][i]
            q_base = flux_invariants(base)["quadrilaterals"][i]
            if q_probe != q_base:
                row |= 1 << code_bit
        constraint_rows.append(row)
    rank = gf2_rank(constraint_rows)
    if rank != n - 1:
        raise AssertionError(f"quadrilateral constraint rank {rank} != n-1")

    result: dict[str, object] = {
        "n": n,
        "switching_classes": 1 << (n + 1),
        "quadrilateral_constraint_rank": rank,
        "quadrilateral_solution_classes": 1 << ((n + 1) - rank),
        "threshold_squared_interval": [str(lower), str(upper)],
        "optimizer_class_codes": sorted(optimizer_codes),
        "optimizer_exact_checks": optimizer_details,
        "exhaustive": exhaustive,
    }
    if not exhaustive:
        result["status"] = "STRUCTURAL_PASS"
        result["elapsed_seconds"] = time.time() - started
        return result

    rayleigh_certified = 0
    exact_fallbacks = 0
    counterexamples = []
    smallest_numeric = float("inf")
    smallest_codes: list[int] = []
    total = 1 << (n + 1)
    for code in range(total):
        if code in optimizer_codes:
            continue
        signing = signing_from_class_code(n, code)
        matrix = numpy_matrix(signing)
        values = np.linalg.eigvalsh(matrix.astype(float))
        rho = float(np.max(np.abs(values)))
        if rho < smallest_numeric - 1e-11:
            smallest_numeric = rho
            smallest_codes = [code]
        elif abs(rho - smallest_numeric) <= 1e-11:
            smallest_codes.append(code)
        bound = integer_rayleigh_lower_bound(matrix)
        if bound >= upper:
            rayleigh_certified += 1
            continue
        exact_fallbacks += 1
        is_counterexample, detail = is_strict_counterexample(signing)
        if is_counterexample:
            counterexamples.append({"code": code, "detail": detail})
            break
    result.update(
        {
            "rayleigh_certified_nonoptimizers": rayleigh_certified,
            "exact_fallbacks": exact_fallbacks,
            "counterexamples": counterexamples,
            "smallest_nonoptimizer_numeric_rho": smallest_numeric,
            "smallest_nonoptimizer_codes": smallest_codes[:20],
            "status": "PASS" if not counterexamples else "FAIL",
            "elapsed_seconds": time.time() - started,
        }
    )
    return result


def gf2_rank(rows: list[int]) -> int:
    rows = rows[:]
    rank = 0
    while rows:
        pivot = max(rows)
        if pivot == 0:
            break
        rows.remove(pivot)
        lead = pivot.bit_length() - 1
        rows = [row ^ pivot if (row >> lead) & 1 else row for row in rows]
        rank += 1
    return rank


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=18)
    parser.add_argument("--structural-only", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    ns = [n for n in (8, 10, 12, 14, 16, 18) if n <= args.max_n]
    results = [reproduce_n(n, not args.structural_only) for n in ns]
    payload = {
        "method": "exact optimizer roots + rational Rayleigh certificates + exact fallback",
        "results": results,
        "overall": "PASS" if all(r["status"].endswith("PASS") for r in results) else "FAIL",
    }
    text = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    raise SystemExit(0 if payload["overall"] == "PASS" else 1)


if __name__ == "__main__":
    main()

"""Verify a Target A counterexample through a rational spectral sandwich.

For a rational t=q/p, positivity of qI-pA^2 proves rho(A)^2 < t.
The conjectured threshold squared is independently enclosed in a certified
rational interval.  If its lower endpoint exceeds t, the candidate is a
strict counterexample without doing algebraic-number arithmetic on A.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp

from target_a_verifier import (
    flux_invariants,
    parse_candidate,
    rational_interval,
    serialize,
    signed_adjacency,
    threshold_squared,
)


def bareiss_leading_minors(matrix: list[list[int]]) -> list[int]:
    """Return leading principal determinants using fraction-free elimination."""
    work = [row[:] for row in matrix]
    n = len(work)
    previous = 1
    pivots = []
    for k in range(n - 1):
        pivot = work[k][k]
        pivots.append(pivot)
        if pivot == 0:
            return pivots + [0] * (n - len(pivots))
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = work[i][j] * pivot - work[i][k] * work[k][j]
                quotient, remainder = divmod(numerator, previous)
                if remainder:
                    raise ArithmeticError("Bareiss division was not exact")
                work[i][j] = quotient
        previous = pivot
    pivots.append(work[-1][-1])
    return pivots


def rational_ldl_diagonal(matrix: list[list[int]]) -> list[Fraction]:
    """Independent exact LDL^T decomposition with unit lower factor."""
    n = len(matrix)
    lower = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    diagonal: list[Fraction] = []
    for j in range(n):
        lower[j][j] = Fraction(1)
        pivot = Fraction(matrix[j][j]) - sum(
            lower[j][k] * lower[j][k] * diagonal[k] for k in range(j)
        )
        diagonal.append(pivot)
        if pivot == 0:
            return diagonal
        for i in range(j + 1, n):
            numerator = Fraction(matrix[i][j]) - sum(
                lower[i][k] * lower[j][k] * diagonal[k] for k in range(j)
            )
            lower[i][j] = numerator / pivot
    return diagonal


def verify_rational_sandwich(candidate_path: Path, bound: Fraction) -> dict[str, Any]:
    candidate_data = json.loads(candidate_path.read_text(encoding="utf-8"))
    signing = parse_candidate(candidate_data)
    adjacency = signed_adjacency(signing)
    square = adjacency * adjacency
    # For bound=q/p, positivity of qI-pA^2 gives rho(A)^2 < q/p.
    integer_certificate = bound.numerator * sp.eye(signing.n) - bound.denominator * square
    rows = [[int(integer_certificate[i, j]) for j in range(signing.n)] for i in range(signing.n)]
    leading_minors = bareiss_leading_minors(rows)
    positive_definite = len(leading_minors) == signing.n and all(value > 0 for value in leading_minors)
    ldl_diagonal = rational_ldl_diagonal(rows)
    ldl_positive = len(ldl_diagonal) == signing.n and all(value > 0 for value in ldl_diagonal)
    cumulative = Fraction(1)
    ldl_matches_bareiss = True
    for index, pivot in enumerate(ldl_diagonal):
        cumulative *= pivot
        if cumulative.denominator != 1 or cumulative.numerator != leading_minors[index]:
            ldl_matches_bareiss = False
            break

    threshold_lower, threshold_upper = rational_interval(threshold_squared(signing.n), digits=30)
    threshold_above_bound = threshold_lower > bound
    candidate_bytes = serialize(signing)
    matrix_bytes = (json.dumps(rows, separators=(",", ":")) + "\n").encode()
    result = positive_definite and ldl_positive and ldl_matches_bareiss and threshold_above_bound
    return {
        "result": result,
        "decision": "COUNTEREXAMPLE_VERIFIED" if result else "CERTIFICATE_FAILED",
        "n": signing.n,
        "rational_bound_on_rho_squared": str(bound),
        "matrix_inequality": (
            f"{bound.numerator} I - {bound.denominator} A^2 is positive definite"
        ),
        "positive_definite_by_sylvester": positive_definite,
        "positive_definite_by_rational_ldl": ldl_positive,
        "ldl_matches_bareiss_minors": ldl_matches_bareiss,
        "rational_ldl_diagonal": [str(value) for value in ldl_diagonal],
        "leading_principal_minor_determinants": [str(value) for value in leading_minors],
        "threshold_squared_interval": [str(threshold_lower), str(threshold_upper)],
        "threshold_lower_exceeds_bound": threshold_above_bound,
        "flux": flux_invariants(signing),
        "candidate_sha256": hashlib.sha256(candidate_bytes).hexdigest(),
        "certificate_matrix_sha256": hashlib.sha256(matrix_bytes).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--bound", default="791/100")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    bound = Fraction(args.bound)
    report = verify_rational_sandwich(args.candidate, bound)
    text = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    raise SystemExit(0 if report["result"] else 1)


if __name__ == "__main__":
    main()

"""Independently verify the frozen exact Target A counterexample at n=32."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp
from sympy.polys.numberfields import to_number_field


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WITNESS = RESEARCH_ROOT / "counterexamples" / "target_a_n32_period8.json"
DEFAULT_CERTIFICATE = (
    RESEARCH_ROOT / "counterexamples" / "target_a_n32_period8_certificate.json"
)
BOUND = Fraction(1561, 200)
TAU_PERIOD = (1, 1, -1, 1, -1, -1, 1, -1)
Q_PERIOD = (1, -1, -1, -1)


class N32CertificateError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise N32CertificateError(message)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _parse_fraction(value: str) -> Fraction:
    try:
        return Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as error:
        raise N32CertificateError(f"invalid rational value: {value!r}") from error


def _exact_positive(value: sp.Expr) -> bool:
    root = to_number_field(sp.simplify(value)).to_root()
    if root.is_positive is True:
        return True
    relation = sp.simplify(root > 0)
    return relation is sp.true


def _bareiss_leading_minors(matrix: list[list[int]]) -> list[int]:
    work = [row[:] for row in matrix]
    previous = 1
    pivots: list[int] = []
    for k in range(len(work) - 1):
        pivot = work[k][k]
        pivots.append(pivot)
        _require(pivot != 0, f"zero Bareiss pivot at index {k}")
        for i in range(k + 1, len(work)):
            for j in range(k + 1, len(work)):
                numerator = work[i][j] * pivot - work[i][k] * work[k][j]
                quotient, remainder = divmod(numerator, previous)
                _require(remainder == 0, f"non-exact Bareiss division at index {k}")
                work[i][j] = quotient
        previous = pivot
    pivots.append(work[-1][-1])
    return pivots


def _rational_ldl_diagonal(matrix: list[list[int]]) -> list[Fraction]:
    n = len(matrix)
    lower = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    diagonal: list[Fraction] = []
    for j in range(n):
        lower[j][j] = Fraction(1)
        pivot = Fraction(matrix[j][j]) - sum(
            lower[j][k] * lower[j][k] * diagonal[k] for k in range(j)
        )
        _require(pivot != 0, f"zero LDL pivot at index {j}")
        diagonal.append(pivot)
        for i in range(j + 1, n):
            numerator = Fraction(matrix[i][j]) - sum(
                lower[i][k] * lower[j][k] * diagonal[k] for k in range(j)
            )
            lower[i][j] = numerator / pivot
    return diagonal


def _load_witness(path: Path) -> tuple[int, tuple[int, ...], tuple[int, ...]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    _require(set(data) == {"n", "step1", "step2"}, "unexpected witness fields")
    n = data["n"]
    step1 = data["step1"]
    step2 = data["step2"]
    _require(type(n) is int and n == 32, "witness order is not 32")
    _require(isinstance(step1, list) and len(step1) == n, "invalid step1 list")
    _require(isinstance(step2, list) and len(step2) == n, "invalid step2 list")
    _require(
        all(type(sign) is int and sign in (-1, 1) for sign in step1 + step2),
        "edge signs must be integers in {-1,+1}",
    )
    return n, tuple(step1), tuple(step2)


def _adjacency(n: int, step1: tuple[int, ...], step2: tuple[int, ...]) -> list[list[int]]:
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i, sign in enumerate(step1):
        j = (i + 1) % n
        _require(matrix[i][j] == 0, "duplicate step1 edge")
        matrix[i][j] = matrix[j][i] = sign
    for i, sign in enumerate(step2):
        j = (i + 2) % n
        _require(matrix[i][j] == 0, "overlapping edge families")
        matrix[i][j] = matrix[j][i] = sign

    for i in range(n):
        for j in range(n):
            distance = min((i - j) % n, (j - i) % n)
            expected_support = distance in (1, 2)
            _require(matrix[i][j] == matrix[j][i], "adjacency is not symmetric")
            _require(matrix[i][i] == 0, "adjacency diagonal is not zero")
            _require((matrix[i][j] != 0) == expected_support, "support is not C_32(1,2)")
            if expected_support:
                _require(matrix[i][j] in (-1, 1), "non-sign adjacency entry")
    return matrix


def _flux(
    n: int, step1: tuple[int, ...], step2: tuple[int, ...]
) -> dict[str, Any]:
    triangles = tuple(
        step1[i] * step1[(i + 1) % n] * step2[i] for i in range(n)
    )
    quadrilaterals = tuple(
        triangles[i] * triangles[(i + 1) % n] for i in range(n)
    )
    alpha = 1
    for sign in step1:
        alpha *= sign
    return {
        "triangles": list(triangles),
        "quadrilaterals": list(quadrilaterals),
        "alpha": alpha,
    }


def _certificate_matrix(adjacency: list[list[int]]) -> list[list[int]]:
    n = len(adjacency)
    square = [
        [sum(adjacency[i][k] * adjacency[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)
    ]
    return [
        [
            (BOUND.numerator if i == j else 0) - BOUND.denominator * square[i][j]
            for j in range(n)
        ]
        for i in range(n)
    ]


def verify_n32_certificate(
    witness_path: Path = DEFAULT_WITNESS,
    certificate_path: Path = DEFAULT_CERTIFICATE,
) -> dict[str, Any]:
    certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
    n, step1, step2 = _load_witness(witness_path)
    adjacency = _adjacency(n, step1, step2)
    flux = _flux(n, step1, step2)

    expected_tau = list(TAU_PERIOD * (n // len(TAU_PERIOD)))
    expected_q = list(Q_PERIOD * (n // len(Q_PERIOD)))
    _require(flux["triangles"] == expected_tau, "triangle flux pattern mismatch")
    _require(flux["quadrilaterals"] == expected_q, "quadrilateral flux pattern mismatch")
    _require(flux["alpha"] == 1, "Hamilton holonomy mismatch")
    _require(certificate.get("flux") == flux, "saved certificate flux mismatch")
    _require(certificate.get("n") == 32, "saved certificate order mismatch")
    _require(
        certificate.get("rational_bound_on_rho_squared") == "1561/200",
        "saved rational bound mismatch",
    )

    canonical_witness = (
        json.dumps(
            {"n": n, "step1": list(step1), "step2": list(step2)},
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode()
    _require(
        hashlib.sha256(canonical_witness).hexdigest() == certificate.get("candidate_sha256"),
        "canonical witness SHA-256 mismatch",
    )

    matrix = _certificate_matrix(adjacency)
    matrix_bytes = (json.dumps(matrix, separators=(",", ":")) + "\n").encode()
    _require(
        hashlib.sha256(matrix_bytes).hexdigest()
        == certificate.get("certificate_matrix_sha256"),
        "certificate matrix SHA-256 mismatch",
    )
    leading_minors = _bareiss_leading_minors(matrix)
    ldl_diagonal = _rational_ldl_diagonal(matrix)
    _require(len(leading_minors) == n and all(value > 0 for value in leading_minors), "Sylvester check failed")
    _require(len(ldl_diagonal) == n and all(value > 0 for value in ldl_diagonal), "LDL check failed")
    cumulative = Fraction(1)
    for index, pivot in enumerate(ldl_diagonal):
        cumulative *= pivot
        _require(
            cumulative.denominator == 1
            and cumulative.numerator == leading_minors[index],
            f"Bareiss/LDL mismatch at index {index}",
        )
    _require(
        [str(value) for value in leading_minors]
        == certificate.get("leading_principal_minor_determinants"),
        "saved Bareiss minors mismatch",
    )
    _require(
        [str(value) for value in ldl_diagonal]
        == certificate.get("rational_ldl_diagonal"),
        "saved LDL diagonal mismatch",
    )

    threshold_squared = 4 * (
        sp.cos(sp.pi / n) ** 2 + sp.cos(2 * sp.pi / n) ** 2
    )
    _require(
        _exact_positive(threshold_squared - sp.Rational(BOUND.numerator, BOUND.denominator)),
        "exact threshold comparison failed",
    )
    saved_interval = certificate.get("threshold_squared_interval")
    _require(isinstance(saved_interval, list) and len(saved_interval) == 2, "invalid threshold interval")
    lower, upper = (_parse_fraction(value) for value in saved_interval)
    _require(lower > BOUND and lower < upper, "saved threshold interval does not clear bound")
    _require(
        _exact_positive(threshold_squared - sp.Rational(lower.numerator, lower.denominator)),
        "saved lower endpoint is not below threshold",
    )
    _require(
        _exact_positive(sp.Rational(upper.numerator, upper.denominator) - threshold_squared),
        "saved upper endpoint is not above threshold",
    )

    return {
        "status": "N32_COUNTEREXAMPLE_EXACT_PASS",
        "n": n,
        "witness_sha256": _sha256(witness_path),
        "certificate_sha256": _sha256(certificate_path),
        "candidate_sha256": certificate["candidate_sha256"],
        "certificate_matrix_sha256": certificate["certificate_matrix_sha256"],
        "flux": flux,
        "positive_principal_minors": len(leading_minors),
        "positive_ldl_pivots": len(ldl_diagonal),
        "rho_squared_upper_bound": "1561/200",
        "threshold_squared_interval": saved_interval,
        "exact_inequality": "rho(A)^2 < 1561/200 < rho_-(32)^2",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--witness", type=Path, default=DEFAULT_WITNESS)
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    args = parser.parse_args()
    try:
        verify_n32_certificate(args.witness, args.certificate)
    except Exception as error:
        print(f"N32 certificate verification failed: {error}", file=sys.stderr)
        print("N32_CERTIFICATE_FAIL")
        raise SystemExit(1)
    print("N32_CERTIFICATE_PASS")


if __name__ == "__main__":
    main()

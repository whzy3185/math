"""Exact verifier for Target A (arXiv:2607.18334, Conjecture 3).

Floating point is never used in the final yes/no decision.  The strict
inequality rho(A)^2 < rho_-(n)^2 is tested with Sylvester's criterion over
real algebraic numbers.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp
from sympy.polys.numberfields import to_number_field


@dataclass(frozen=True)
class Signing:
    n: int
    step1: tuple[int, ...]
    step2: tuple[int, ...]


def parse_candidate(data: dict[str, Any]) -> Signing:
    n = data.get("n")
    step1 = data.get("step1")
    step2 = data.get("step2")
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError("n must be an integer")
    if n < 8 or n % 2:
        raise ValueError("Target A requires even n >= 8")
    if not isinstance(step1, list) or not isinstance(step2, list):
        raise ValueError("step1 and step2 must be JSON lists")
    if len(step1) != n or len(step2) != n:
        raise ValueError("each sign list must have length n")
    if any(type(x) is not int or x not in (-1, 1) for x in step1 + step2):
        raise ValueError("every edge sign must be the integer +1 or -1")
    return Signing(n, tuple(step1), tuple(step2))


def signed_adjacency(signing: Signing) -> sp.Matrix:
    n = signing.n
    matrix = sp.zeros(n)
    for i, sign in enumerate(signing.step1):
        j = (i + 1) % n
        matrix[i, j] = matrix[j, i] = sign
    for i, sign in enumerate(signing.step2):
        j = (i + 2) % n
        if matrix[i, j] != 0:
            raise AssertionError("edge families unexpectedly overlap")
        matrix[i, j] = matrix[j, i] = sign
    return matrix


def threshold_squared(n: int) -> sp.Expr:
    return sp.simplify(4 * (sp.cos(sp.pi / n) ** 2 + sp.cos(2 * sp.pi / n) ** 2))


def exact_sign(value: sp.Expr) -> int:
    value = sp.simplify(value)
    if value == 0:
        return 0
    root = sp.simplify(to_number_field(value).to_root())
    if root.is_positive is True:
        return 1
    if root.is_negative is True:
        return -1
    positive = sp.simplify(root > 0)
    negative = sp.simplify(root < 0)
    if positive is sp.true:
        return 1
    if negative is sp.true:
        return -1
    raise ArithmeticError(f"SymPy could not determine an exact sign: {root}")


def rational_interval(value: sp.Expr, digits: int = 30) -> tuple[Fraction, Fraction]:
    """Return a certified rational isolating interval for a real algebraic value."""
    x = sp.Symbol("x")
    polynomial = sp.Poly(sp.minimal_polynomial(value, x), x, domain=sp.QQ)
    epsilon = sp.Rational(1, 10**digits)
    intervals = polynomial.intervals(eps=epsilon)
    approximation = float(sp.N(value, 18))
    candidates: list[tuple[sp.Rational, sp.Rational]] = []
    for (left, right), _multiplicity in intervals:
        if float(left) <= approximation <= float(right):
            candidates.append((left, right))
    for left, right in candidates:
        if exact_sign(value - left) >= 0 and exact_sign(right - value) >= 0:
            return Fraction(left.p, left.q), Fraction(right.p, right.q)
    raise ArithmeticError("failed to isolate the requested algebraic root")


def flux_invariants(signing: Signing) -> dict[str, Any]:
    n = signing.n
    triangles = []
    for i in range(n):
        triangles.append(
            signing.step1[i]
            * signing.step1[(i + 1) % n]
            * signing.step2[i]
        )
    alpha = 1
    for sign in signing.step1:
        alpha *= sign
    quadrilaterals = [triangles[i] * triangles[(i + 1) % n] for i in range(n)]
    return {"triangles": triangles, "alpha": alpha, "quadrilaterals": quadrilaterals}


def canonical_tree_gauge(signing: Signing) -> Signing:
    """Switch so step-1 edges 0,...,n-2 are +1."""
    n = signing.n
    d = [1] * n
    for i in range(n - 1):
        d[i + 1] = d[i] * signing.step1[i]
    step1 = tuple(d[i] * signing.step1[i] * d[(i + 1) % n] for i in range(n))
    step2 = tuple(d[i] * signing.step2[i] * d[(i + 2) % n] for i in range(n))
    assert all(sign == 1 for sign in step1[:-1])
    return Signing(n, step1, step2)


def is_strict_counterexample(signing: Signing) -> tuple[bool, dict[str, Any]]:
    """Decide rho(A)^2 < threshold^2 exactly via Sylvester's criterion."""
    matrix = signed_adjacency(signing)
    square = matrix * matrix
    threshold = threshold_squared(signing.n)
    x = sp.Symbol("x")
    minor_signs: list[int] = []
    for size in range(1, signing.n + 1):
        principal = square[:size, :size]
        characteristic = principal.charpoly(x).as_expr()
        sign = exact_sign(characteristic.subs(x, threshold))
        minor_signs.append(sign)
        if sign <= 0:
            return False, {
                "decision": "NOT_COUNTEREXAMPLE",
                "reason": "Sylvester leading principal minor is non-positive",
                "first_nonpositive_minor": size,
                "minor_signs": minor_signs,
            }
    return True, {
        "decision": "COUNTEREXAMPLE_VERIFIED",
        "reason": "all leading principal minors of threshold^2 I - A^2 are positive",
        "minor_signs": minor_signs,
    }


def serialize(signing: Signing) -> bytes:
    payload = {"n": signing.n, "step1": list(signing.step1), "step2": list(signing.step2)}
    return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()


def verification_report(signing: Signing) -> dict[str, Any]:
    result, detail = is_strict_counterexample(signing)
    canonical = canonical_tree_gauge(signing)
    matrix = signed_adjacency(signing)
    payload = serialize(signing)
    return {
        "result": result,
        **detail,
        "n": signing.n,
        "threshold_squared": str(threshold_squared(signing.n)),
        "characteristic_polynomial": str(matrix.charpoly().as_expr()),
        "flux": flux_invariants(signing),
        "canonical_tree_gauge": {
            "step1": list(canonical.step1),
            "step2": list(canonical.step2),
        },
        "candidate_sha256": hashlib.sha256(payload).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", type=Path)
    args = parser.parse_args()
    data = json.loads(args.candidate.read_text(encoding="utf-8"))
    report = verification_report(parse_candidate(data))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report["result"] else 1)


if __name__ == "__main__":
    main()

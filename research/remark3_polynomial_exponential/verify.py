#!/usr/bin/env python3
"""Exact finite-data certificates for the Remark 3 manuscript.

The supplied factorization MUST be complete into irreducibles over C for the
classification enumeration to be exhaustive. Identity of the supplied product
is checked; irreducibility itself is not certified by this program. Regression
examples use explicit linear factors. This is not a formal proof of the analytic
theorem and does not attempt floating-point or general entire-function search.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import product
import json
from pathlib import Path
import platform
from typing import Iterator, Sequence

import sympy as sp

Expr = sp.Expr


def zero(expr: Expr) -> bool:
    return sp.expand(expr) == 0


def partitions(n: int) -> Iterator[tuple[tuple[int, ...], ...]]:
    """Each set partition once, with blocks ordered by their minimum."""
    if n < 1:
        raise ValueError("n must be positive")
    blocks: list[list[int]] = []

    def visit(i: int):
        if i == n:
            yield tuple(tuple(b) for b in blocks)
            return
        for b in blocks:
            b.append(i)
            yield from visit(i + 1)
            b.pop()
        blocks.append([i])
        yield from visit(i + 1)
        blocks.pop()

    yield from visit(0)


def allocations(e: int, weights: Sequence[int]) -> list[tuple[int, ...]]:
    if e < 0 or not weights or any(m <= 0 for m in weights):
        raise ValueError("Require e >= 0 and positive integer weights")
    if len(weights) == 1:
        return [(e // weights[0],)] if e % weights[0] == 0 else []
    return [(a,) + tail for a in range(e // weights[0] + 1)
            for tail in allocations(e - a * weights[0], weights[1:])]


@dataclass
class Family:
    blocks: tuple[tuple[int, ...], ...]
    factors: tuple[Expr, ...]
    phases: tuple[Expr, ...]
    kappas: tuple[Expr, ...]
    block_weights: tuple[int, ...]
    scale_rhs: Expr

    def report(self) -> dict:
        return {
            "blocks_zero_based": [list(b) for b in self.blocks],
            "R_i": [str(v) for v in self.factors],
            "h_B": [str(v) for v in self.phases],
            "kappa_i": [str(v) for v in self.kappas],
            "M_B": list(self.block_weights),
            "scale_constraint_rhs": str(self.scale_rhs),
        }


def classify(variables: Sequence[sp.Symbol], P: Expr, G: Expr,
             factorization: Sequence[tuple[Expr, int]],
             scalar: Expr = sp.Integer(1),
             weights: Sequence[int] | None = None) -> list[Family]:
    """Enumerate canonical data; coefficients must support exact comparison.

    factorization is an explicit C-irreducible factorization of P/scalar.
    The caller, not this routine, is responsible for its irreducibility.
    """
    variables = tuple(variables)
    n = len(variables)
    weights = tuple(weights or (1,) * n)
    P, G, scalar = map(sp.sympify, (P, G, scalar))
    if n < 1 or len(set(variables)) != n or len(weights) != n:
        raise ValueError("Invalid variables or weights")
    if any(not isinstance(m, int) or m <= 0 for m in weights):
        raise ValueError("Weights must be positive Python integers")
    if zero(P) or zero(scalar):
        raise ValueError("P=0 is the separately classified degenerate case")
    sp.Poly(P, *variables)
    sp.Poly(G, *variables)
    for f, e in factorization:
        if not isinstance(e, int) or e <= 0 or sp.Poly(f, *variables).total_degree() == 0:
            raise ValueError("Factors must be nonconstant polynomials with positive multiplicity")
    expected = scalar * sp.prod(f ** e for f, e in factorization)
    if not zero(P - expected):
        raise ValueError("The supplied factorization does not multiply to P")
    G0 = G.subs(dict.fromkeys(variables, 0))
    factor_choices = [allocations(e, weights) for _, e in factorization]
    families: list[Family] = []
    for blocks in partitions(n):
        block_weights = tuple(sum(weights[i] for i in b) for b in blocks)
        GB = tuple(sp.expand(G.subs({variables[j]: 0 for j in range(n) if j not in b}) - G0)
                   for b in blocks)
        if not zero(G - G0 - sum(GB)):
            continue
        phases = tuple(g / m for g, m in zip(GB, block_weights))
        for choice in product(*factor_choices):
            R = tuple(sp.expand(sp.prod(f ** choice[k][i]
                      for k, (f, _) in enumerate(factorization))) for i in range(n))
            if any(not zero(sp.diff(R[i], variables[j]))
                   for b in blocks for i in b for j in range(n) if j not in b):
                continue
            kappas = [sp.Integer(0)] * n
            valid = True
            for b, h in zip(blocks, phases):
                adjacency = {i: [] for i in b}
                for idx, i in enumerate(b):
                    for j in b[idx + 1:]:
                        a = sp.expand(sp.diff(R[i], variables[j]) + R[i] * sp.diff(h, variables[j]))
                        other = sp.expand(sp.diff(R[j], variables[i]) + R[j] * sp.diff(h, variables[i]))
                        if zero(a) and zero(other):
                            continue
                        if zero(a) or zero(other):
                            valid = False
                            break
                        ratio = sp.cancel(sp.Poly(a, *variables).LC() / sp.Poly(other, *variables).LC())
                        if not zero(a - ratio * other):
                            valid = False
                            break
                        adjacency[i].append((j, ratio))
                        adjacency[j].append((i, 1 / ratio))
                    if not valid:
                        break
                if not valid:
                    break
                root = b[0]
                assigned = {root: sp.Integer(1)}
                queue = [root]
                for i in queue:
                    for j, ratio in adjacency[i]:
                        proposed = sp.cancel(assigned[i] * ratio)
                        if j in assigned:
                            if sp.cancel(assigned[j] - proposed) != 0:
                                valid = False
                                break
                        else:
                            assigned[j] = proposed
                            queue.append(j)
                    if not valid:
                        break
                if not valid or len(assigned) != len(b):
                    valid = False
                    break
                for i in b:
                    kappas[i] = assigned[i]
            if not valid:
                continue
            scale_rhs = sp.cancel(scalar * sp.exp(G0) /
                                  sp.prod(kappas[i] ** weights[i] for i in range(n)))
            family = Family(blocks, R, phases, tuple(kappas), block_weights, scale_rhs)
            check_certificate(variables, P, G, weights, family)
            families.append(family)
    return families


def check_certificate(variables: Sequence[sp.Symbol], P: Expr, G: Expr,
                      weights: Sequence[int], family: Family) -> None:
    """Verify polynomial closure, separated phases and the scalar product."""
    phase_sum = sum(m * h for m, h in zip(family.block_weights, family.phases))
    G0 = G.subs(dict.fromkeys(variables, 0))
    assert zero(phase_sum - G + G0), "Phase identity failed"
    polynomial_product = sp.prod((family.kappas[i] * family.factors[i]) ** weights[i]
                                 for i in range(len(variables)))
    assert sp.simplify(family.scale_rhs * polynomial_product - sp.exp(G0) * P) == 0
    for b, h in zip(family.blocks, family.phases):
        for i in b:
            for j in b:
                fi = family.kappas[i] * family.factors[i]
                fj = family.kappas[j] * family.factors[j]
                assert zero(sp.diff(fi, variables[j]) + fi * sp.diff(h, variables[j])
                            - sp.diff(fj, variables[i]) - fj * sp.diff(h, variables[i]))


def run_tests() -> dict:
    x, y, z = sp.symbols("x y z")
    cases = [
        ("xy_exp_2xy", (x, y), x*y, 2*x*y, [(x, 1), (y, 1)], (1, 1), 1),
        ("xy_polynomial", (x, y), x*y, sp.Integer(0), [(x, 1), (y, 1)], (1, 1), 2),
        ("no_solution_exp_xy", (x, y), sp.Integer(1), x*y, [], (1, 1), 0),
        ("linear_phase_two_strata", (x, y), sp.Integer(1), x+y, [], (1, 1), 2),
        ("separated_quadratic_phase", (x, y), sp.Integer(1), x*x+y*y, [], (1, 1), 1),
        ("weighted_cube_roots", (x, y), x*y*y, 3*x*y, [(x, 1), (y, 2)], (2, 1), 1),
        ("three_variable_blocks", (x, y, z), x*y, 2*x*y+z*z, [(x, 1), (y, 1)], (1, 1, 1), 1),
        ("three_variable_affine", (x, y, z), sp.Integer(1), sp.Integer(0), [], (1, 1, 1), 1),
        ("one_variable_weighted", (x,), x*x, 2*x, [(x, 2)], (2,), 1),
    ]
    reports = []
    for name, variables, P, G, factors, weights, expected in cases:
        result = classify(variables, P, G, factors, weights=weights)
        assert len(result) == expected, (name, len(result), expected)
        reports.append({"test": name, "passed": True, "family_count": len(result),
                        "families": [f.report() for f in result]})

    u = sp.exp(x*y)
    assert sp.simplify(sp.diff(u, x)*sp.diff(u, y) - x*y*sp.exp(2*x*y)) == 0
    assert sp.simplify(sp.diff(u, x)**2*sp.diff(u, y) - x*y*y*sp.exp(3*x*y)) == 0
    assert sp.simplify(sp.diff(u, x)/sp.diff(u, y) - y/x) == 0
    reports.append({"test": "non_ridge_and_weighted_direct_identities", "passed": True})

    # Non-symmetric A checks the transpose, not only a diagonal special case.
    A = sp.Matrix([[1, 2], [3, 5]])
    w = A.T.inv() * sp.Matrix([x, y])
    uu = sp.exp(w[0]*w[1])
    D = A * sp.Matrix([sp.diff(uu, x), sp.diff(uu, y)])
    assert sp.simplify(D[0]*D[1] - w[0]*w[1]*sp.exp(2*w[0]*w[1])) == 0
    reports.append({"test": "invertible_nonsymmetric_transpose", "passed": True,
                    "A": str(A), "A_inverse_transpose_z": [str(a) for a in w]})

    for degree in range(0, 9):
        u = x**(degree+1)/sp.Integer(degree+1) + y + z
        assert zero(sp.diff(u, x)*sp.diff(u, y)*sp.diff(u, z)-x**degree)
        assert sp.Poly(u, x, y, z).total_degree() == degree+1
    reports.append({"test": "degree_sharpness_D_0_through_8", "passed": True, "instances": 9})

    # Both cases are outside the main theorem; only their explicit identities are checked.
    u = x + sp.exp(sp.exp(y))
    assert sp.diff(u, x)**2 == 1
    u = sp.exp(y + sp.exp(x))
    assert sp.simplify(sp.diff(u, x)*sp.diff(u, y) - sp.exp(x+2*y+2*sp.exp(x))) == 0
    reports.append({"test": "singular_matrix_and_transcendental_phase_boundaries", "passed": True})

    try:
        classify((x, y), sp.Integer(0), sp.Integer(0), [])
    except ValueError:
        pass
    else:
        raise AssertionError("Degenerate P=0 must not enter the finite solver")
    reports.append({"test": "zero_polynomial_guard", "passed": True})

    return {"status": "passed", "scope": "finite exact symbolic regression tests, not a proof assistant",
            "factorization_scope": "explicit linear factors, irreducible over C",
            "python": platform.python_version(), "sympy": sp.__version__,
            "test_groups": len(reports), "results": reports}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("verification_results.json"))
    args = parser.parse_args()
    result = run_tests()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(f"PASS: {result['test_groups']} exact test groups; {args.output}")


if __name__ == "__main__":
    main()

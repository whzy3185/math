"""Exact checks for the Remark 3 manuscript (not a proof assistant).

The general enumerator requires a COMPLETE factorization over C supplied by the
caller. The irreducible criterion assumes C-irreducibility for its negative
conclusion; the routine deliberately does not infer it from Q-factorization.
No floating-point input is accepted. All tested coefficients are exact rationals.
"""
from __future__ import annotations
import argparse
import itertools
import json
import platform
from pathlib import Path
from typing import Iterator, Sequence
import sympy as s


def zero(expr: s.Expr) -> bool:
    return s.cancel(s.expand(expr)) == 0


def validate(P, G, variables, weights):
    P, G = s.sympify(P), s.sympify(G)
    if not variables or len(set(variables)) != len(variables):
        raise ValueError("Distinct nonempty coordinate list required")
    if len(weights) != len(variables) or any(type(m) is not int or m <= 0 for m in weights):
        raise ValueError("Positive integer weights required")
    if P == 0:
        raise ValueError("P=0 is the separate degenerate theorem")
    if P.atoms(s.Float) or G.atoms(s.Float):
        raise ValueError("Floating point input is not an exact certificate")
    s.Poly(P, *variables); s.Poly(G, *variables)
    return P, G


def partitions(n: int) -> Iterator[tuple[tuple[int, ...], ...]]:
    if n == 0:
        yield ()
        return
    for p in partitions(n - 1):
        yield p + ((n - 1,),)
        for k in range(len(p)):
            yield p[:k] + (p[k] + (n - 1,),) + p[k + 1:]


def allocations(total: int, weights: Sequence[int]) -> Iterator[tuple[int, ...]]:
    if len(weights) == 1:
        if total % weights[0] == 0:
            yield (total // weights[0],)
        return
    for e in range(total // weights[0] + 1):
        for tail in allocations(total - weights[0] * e, weights[1:]):
            yield (e,) + tail


def canonical_families(P, G, variables, weights, scalar, factors):
    """Enumerate canonical data, assuming factors=[(C-irreducible, multiplicity)]."""
    P, G = validate(P, G, variables, weights)
    n = len(variables)
    scalar = s.sympify(scalar)
    factors = [(s.sympify(f), m) for f, m in factors]
    if scalar == 0 or any(type(m) is not int or m <= 0 for _, m in factors):
        raise ValueError("Invalid factorization data")
    if not zero(P - scalar * s.prod(f**m for f, m in factors)):
        raise ValueError("Factorization does not multiply to P")
    G0 = G.subs(dict.fromkeys(variables, 0))
    factor_allocations = [list(allocations(m, weights)) for _, m in factors]
    found = []
    for pi in partitions(n):
        masses = [sum(weights[i] for i in B) for B in pi]
        parts = [s.expand(G.subs({variables[j]: 0 for j in range(n) if j not in B}) - G0) for B in pi]
        if not zero(G - G0 - sum(parts)):
            continue
        phases = [q / mass for q, mass in zip(parts, masses)]
        for allocation in itertools.product(*factor_allocations):
            R = [s.prod(factors[nu][0]**allocation[nu][i] for nu in range(len(factors))) for i in range(n)]
            kappas = [None] * n
            accepted = True
            for B, h in zip(pi, phases):
                if any(not zero(s.diff(R[i], variables[j])) for i in B for j in range(n) if j not in B):
                    accepted = False; break
                edges = {i: [] for i in B}
                for i, j in itertools.combinations(B, 2):
                    a = s.expand(s.diff(R[i], variables[j]) + R[i] * s.diff(h, variables[j]))
                    b = s.expand(s.diff(R[j], variables[i]) + R[j] * s.diff(h, variables[i]))
                    if (a == 0) != (b == 0):
                        accepted = False; break
                    if a == 0:
                        continue
                    ratio = s.cancel(a / b)
                    if ratio == 0 or any(not zero(s.diff(ratio, x)) for x in variables):
                        accepted = False; break
                    edges[i].append((j, ratio))
                    edges[j].append((i, 1 / ratio))
                if not accepted:
                    break
                root = min(B)
                kappas[root] = s.Integer(1)
                stack = [root]
                while stack and accepted:
                    i = stack.pop()
                    for j, ratio in edges[i]:
                        value = s.cancel(kappas[i] * ratio)
                        if kappas[j] is None:
                            kappas[j] = value; stack.append(j)
                        elif not zero(kappas[j] - value):
                            accepted = False; break
                if not accepted or any(kappas[i] is None for i in B):
                    accepted = False; break
            if not accepted:
                continue
            K = s.cancel(s.exp(G0) * scalar / s.prod(kappas[i]**weights[i] for i in range(n)))
            found.append({"partition": pi, "phases": phases, "R": R, "kappa": kappas,
                          "masses": masses, "K": K})
    return found


def irreducible_criterion(P, G, variables, weights):
    """Return exact sufficient data; rejection is necessary only under C-irreducibility.

    Full coordinate support is checked here. Irreducibility is an external
    hypothesis and is NEVER certified by this function.
    """
    P, G = validate(P, G, variables, weights)
    if len(variables) < 2 or any(zero(s.diff(P, x)) for x in variables):
        raise ValueError("The irreducible full-support theorem does not apply")
    active = [i for i, x in enumerate(variables) if not zero(s.diff(G, x))]
    if len(active) != 1:
        return None
    k = active[0]
    if weights[k] != 1:
        return None
    M = sum(weights)
    h = G / M
    hp = s.diff(h, variables[k])
    lambdas = {}
    for j, x in enumerate(variables):
        if j == k:
            continue
        value = s.cancel(s.diff(P, x) / hp)
        if value == 0 or any(not zero(s.diff(value, y)) for y in variables):
            return None
        lambdas[j] = value
    b = s.expand(P.subs({x: 0 for j, x in enumerate(variables) if j != k}))
    if not zero(P - b - hp * sum(lambdas[j] * variables[j] for j in lambdas)):
        return None
    root_rhs = s.cancel(1 / s.prod(lambdas[j]**weights[j] for j in lambdas))
    return {"k": k, "h": h, "b": b, "lambdas": lambdas, "root_degree": M,
            "root_rhs": root_rhs, "irreducibility_assumed_not_computed": True}


def elementary_primitive(h, Q, variables, pivot):
    """Recover the UNIQUE polynomial R when h_pivot is a nonzero constant."""
    alpha = s.diff(h, variables[pivot])
    if alpha == 0 or any(not zero(s.diff(alpha, x)) for x in variables):
        raise ValueError("A nonzero constant phase derivative is required")
    for i, j in itertools.combinations(range(len(variables)), 2):
        if not zero(s.diff(Q[i], variables[j]) + Q[i]*s.diff(h, variables[j])
                    - s.diff(Q[j], variables[i]) - Q[j]*s.diff(h, variables[i])):
            raise ValueError("Polynomial one-form is not twisted-closed")
    R, derivative, ell = s.Integer(0), s.expand(Q[pivot]), 0
    while derivative != 0:
        R += (-1)**ell * derivative / alpha**(ell + 1)
        derivative = s.diff(derivative, variables[pivot]); ell += 1
    R = s.expand(R)
    assert all(zero(s.diff(R, x) + R*s.diff(h, x) - Q[i]) for i, x in enumerate(variables))
    return R


def run_checks():
    records = []
    def check(name, condition, detail=""):
        if not bool(condition):
            raise AssertionError(name)
        records.append({"name": name, "passed": True, "detail": detail})
    x, y, z = s.symbols("x y z")
    cases = [
        ("xy_exp", x*y, 2*x*y, (x,y), (1,1), 1, [(x,1),(y,1)], 1),
        ("xy_polynomial", x*y, 0, (x,y), (1,1), 1, [(x,1),(y,1)], 2),
        ("no_zero_phase_obstruction", 1, x*y, (x,y), (1,1), 1, [], 0),
        ("irred_two", x+y, 2*x, (x,y), (1,1), 1, [(x+y,1)], 1),
        ("irred_special_primitive", x*y+1, x*x, (x,y), (1,1), 1, [(x*y+1,1)], 1),
        ("irred_three", x+y+z, 3*x, (x,y,z), (1,1,1), 1, [(x+y+z,1)], 1),
        ("irred_weighted", x+y+z, 6*x, (x,y,z), (1,2,3), 1, [(x+y+z,1)], 1),
        ("irred_wrong_phase", x+y, x+y, (x,y), (1,1), 1, [(x+y,1)], 0),
        ("irred_no_unit_weight", x+y, 4*x, (x,y), (2,2), 1, [(x+y,1)], 0),
        ("weighted_xy", x*y*y, 3*x*y, (x,y), (2,1), 1, [(x,1),(y,2)], 1),
        ("one_variable", x*x, 2*x, (x,), (2,), 1, [(x,2)], 1),
        ("constant_phase_offset", x+y, 2*x+2, (x,y), (1,1), 1, [(x+y,1)], 1),
        ("three_variable_polynomial", x*y*z, 0, (x,y,z), (1,1,1), 1, [(x,1),(y,1),(z,1)], 4),
        ("affine_two_partitions", 1, 2*x+2*y, (x,y), (1,1), 1, [], 2),
    ]
    for name, P, G, vv, mu, scalar, factors, expected in cases:
        families = canonical_families(P,G,vv,mu,scalar,factors)
        check(name, len(families) == expected, f"canonical families={len(families)}")
        for f in families:
            for B, h in zip(f["partition"], f["phases"]):
                Q = [s.expand(f["kappa"][i]*f["R"][i]) for i in B]
                assert all(zero(s.diff(Q[a], vv[j])+Q[a]*s.diff(h,vv[j])
                                -s.diff(Q[b],vv[i])-Q[b]*s.diff(h,vv[i]))
                           for a,i in enumerate(B) for b,j in enumerate(B))
    # Constructed full-support irreducible families, with proof of irreducibility
    # supplied in the manuscript: primitive degree-one in L, gcd(h', 1+x*h')=1.
    for n in range(2,6):
        vv = s.symbols(f"w0:{n}")
        for k in range(n):
            for degree in range(1,5):
                mu = tuple(1 if j == k else 1 + (j % 3) for j in range(n))
                h = vv[k]**degree + s.Rational(1,3)
                L = sum(s.Rational(j+1,2)*vv[j] for j in range(n) if j != k)
                b = 1 + vv[k]*s.diff(h,vv[k])
                P = s.expand(b+s.diff(h,vv[k])*L)
                G = sum(mu)*h
                cert = irreducible_criterion(P,G,vv,mu)
                ok = cert is not None and cert["k"] == k and cert["root_degree"] == sum(mu)
                V = s.exp(h)*(vv[k]+L)
                stripped = [s.simplify(s.diff(V,w)/s.exp(h)) for w in vv]
                ok = ok and zero(stripped[k]-P)
                ok = ok and all(zero(stripped[j]-cert["lambdas"][j]) for j in range(n) if j != k)
                ok = ok and zero(s.prod(stripped[j]**mu[j] for j in range(n))*cert["root_rhs"]-P)
                check(f"constructed_n{n}_k{k}_degree{degree}", ok, f"exact classes modulo constants={sum(mu)}")
    for n in range(2,6):
        vv = s.symbols(f"q0:{n}")
        P = 1 + sum(w*w for w in vv)
        for d in range(1,4):
            check(f"quadric_n{n}_phase_degree{d}",
                  irreducible_criterion(P,vv[0]**d,vv,(1,)*n) is None,
                  "finite check; arbitrary polynomial G is handled by the analytic theorem")
    for name, h, R, vv, pivot in [
        ("elementary_linear", x+2*y, x**3+x*y+2*y+1, (x,y), 0),
        ("elementary_nonlinear", 2*x+y*y, x*x*y+y**3+1, (x,y), 0),
        ("elementary_three", z+x*y, x*x*z+y*z*z+3, (x,y,z), 2),
    ]:
        Q = [s.expand(s.diff(R,w)+R*s.diff(h,w)) for w in vv]
        check(name, zero(elementary_primitive(h,Q,vv,pivot)-R))
    # Explicit integral example, differentiated exactly using its special function.
    E = s.sqrt(s.pi/2)*s.erfi(x/s.sqrt(2))
    V = y*s.exp(x*x/2)+E
    check("special_function_gradient", zero(s.diff(V,x)-(x*y+1)*s.exp(x*x/2))
          and zero(s.diff(V,y)-s.exp(x*x/2)))
    # Matrix-chain-rule test: z=A^T w, u(z)=v(A^{-T}z).
    A = s.Matrix([[1,2],[3,5]])
    z1,z2 = s.symbols("z1 z2")
    w = A.T.inv()*s.Matrix([z1,z2])
    u = s.exp(w[0])*(w[0]+w[1]-1)
    directional = A*s.Matrix([s.diff(u,z1),s.diff(u,z2)])
    check("matrix_transpose_and_no_determinant", zero(directional[0]*directional[1]
          -(w[0]+w[1])*s.exp(2*w[0])))
    for name, thunk in [
        ("reject_float",lambda: validate(x+y,s.Float(1.0)*x,(x,y),(1,1))),
        ("reject_zero_P",lambda: validate(0,x,(x,y),(1,1))),
        ("reject_wrong_factorization",lambda: canonical_families(x+y,x,(x,y),(1,1),1,[(x,1)])),
        ("reject_missing_full_support",lambda: irreducible_criterion(x,x+y,(x,y),(1,1))),
        ("reject_nonconstant_pivot",lambda: elementary_primitive(x*x/2,[x*y+1,1],(x,y),0)),
        ("reject_nonclosed_form",lambda: elementary_primitive(x,[y,0],(x,y),0)),
    ]:
        rejected = False
        try:
            thunk()
        except ValueError:
            rejected = True
        check(name, rejected)
    return {"status":"passed", "count":len(records), "python":platform.python_version(),
            "sympy":s.__version__, "evidence":"exact finite symbolic checks, not formal proofs",
            "irreducibility":"assumed when using the negative irreducible criterion; test inputs justified in manuscript",
            "checks":records}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="verification_results.json")
    args = parser.parse_args()
    report = run_checks()
    Path(args.output).write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(f'{report["count"]} exact checks passed; saved {args.output}')

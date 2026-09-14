#!/usr/bin/env python3
"""Exact audit for PERIOD8_FULL_CLASS_JUMP4_VARIATIONAL_THEOREM.md.

Run, for example:

  uv run --with sympy python \
    research/paper_rebuild/circulant_all_jump_20260909/verify_period8_full_class_jump4.py

The script uses no floating-point spectral acceptance test.
"""

from itertools import product
import sympy as sp


def prod(xs):
    out = 1
    for x in xs:
        out *= x
    return out


def lift_flux(q):
    tau = [sp.Integer(1)]
    for i in range(7):
        tau.append(tau[-1] * q[i])
    assert tau[-1] * tau[0] == q[7]
    return tau


def endpoint_fiber(q, eps):
    """Exact 8 x 8 fiber at z=eps, eps in {+1,-1}."""
    tau = lift_flux(q)
    H = sp.zeros(8)
    for i in range(7):
        H[i, i + 1] = H[i + 1, i] = 1
    H[7, 0] = H[0, 7] = eps
    for j in range(4):
        c = tau[j] + eps * tau[j + 4]
        H[j, j + 4] = H[j + 4, j] = c
    return H


def moment_signature(q):
    ans = []
    for eps in (1, -1):
        H = endpoint_fiber(q, eps)
        H2 = H * H
        H4 = H2 * H2
        H6 = H4 * H2
        tr2 = sp.trace(H2)
        tr4 = sp.trace(H4)
        tr6 = sp.trace(H6)
        ans.extend((8 * tr2 - tr4, 8 * tr4 - tr6))
    return tuple(int(sp.expand(v)) for v in ans)


def dihedral_canonical(q):
    q = tuple(q)
    words = []
    for k in range(8):
        r = q[k:] + q[:k]
        words.append(r)
        words.append(tuple(reversed(r)))
    return min(words)


def plus_positions(q):
    return tuple(i for i, x in enumerate(q) if x == 1)


def main():
    legal = [q for q in product((-1, 1), repeat=8) if prod(q) == 1]
    assert len(legal) == 128

    orbits = {}
    for q in legal:
        orbits.setdefault(dihedral_canonical(q), []).append(q)
    assert len(orbits) == 18

    # Fourth-moment sum identity.
    for q in legal:
        d = sum(x == 1 for x in q)
        D4p, _, D4m, _ = moment_signature(q)
        assert D4p + D4m == 160 - 32 * d

    # Necessary endpoint moment inequalities leave exactly four orbits.
    survivors = []
    for rep in orbits:
        sig = moment_signature(rep)
        if all(v >= 0 for v in sig):
            survivors.append((rep, sig))

    expected = {
        (-1, -1, -1, -1, -1, -1, -1, -1),
        (-1, -1, -1, -1, -1, -1, 1, 1),
        (-1, -1, -1, -1, -1, 1, -1, 1),
        (-1, -1, -1, -1, 1, -1, -1, 1),
    }
    assert {rep for rep, _ in survivors} == expected

    # Exact full d=4 orbit table in theorem order.
    d4_expected = {
        "-+-+-+-+": (-48, -864, 80, 224),
        "--++--++": (-48, -1056, 80, 224),
        "--+-++-+": (16, 64, 16, -32),
        "--+-+-++": (-16, -448, 48, 96),
        "--+--+++": (-16, -640, 48, 192),
        "---++-++": (48, 192, -16, -640),
        "---+-+++": (48, 96, -16, -544),
        "----++++": (16, -128, 16, -32),
    }
    got = {}
    for rep in orbits:
        if sum(x == 1 for x in rep) == 4:
            word = "".join("+" if x == 1 else "-" for x in rep)
            got[word] = moment_signature(rep)
    assert got == d4_expected

    # The two remaining unwanted two-defect classes cross 8 already at z=1.
    q_dist1 = (-1, -1, -1, -1, -1, -1, 1, 1)
    q_dist3 = (-1, -1, -1, -1, 1, -1, -1, 1)
    for q, expected_det in ((q_dist1, -2**10), (q_dist3, -(2**11) * 3**2)):
        H = endpoint_fiber(q, 1)
        det = sp.factor((8 * sp.eye(8) - H * H).det())
        assert det == expected_det

    # Exact dispersion for the unique surviving distance-two orbit.
    y, c, X, W = sp.symbols("y c X W")
    x = (y - c - 4) / 2
    a = (y + c - 4) / 2
    Z = 2 * x * a - 3  # N=m=1: T1(t)=t, U0(t)=1.
    P = sp.expand(4 * (Z**2 - 1 + (c - 2)) + (2 - c))
    expected_P = (
        y**4 - 16*y**3 + (84 - 2*c**2)*y**2
        + (-160 + 16*c**2)*y + c**4 - 20*c**2 + 3*c + 90
    )
    assert sp.expand(P - expected_P) == 0

    shifted = sp.expand(P.subs(y, X + 4))
    expected_shifted = X**4 - (12 + 2*c**2)*X**2 + c**4 + 12*c**2 + 3*c + 26
    assert sp.expand(shifted - expected_shifted) == 0

    quad = W**2 - (12 + 2*c**2)*W + c**4 + 12*c**2 + 3*c + 26
    disc = sp.factor(sp.discriminant(quad, W))
    assert disc == 4 * (10 - 3*c)

    # Endpoint comparison for the top branch.
    f_minus2 = 6 + (-2)**2 + sp.sqrt(10 - 3*(-2))
    f_plus2 = 6 + 2**2 + sp.sqrt(10 - 3*2)
    assert f_minus2 == 14
    assert f_plus2 == 12
    assert sp.simplify(4 + sp.sqrt(f_minus2) - (4 + sp.sqrt(14))) == 0

    print("PASS: 128 legal words -> 18 dihedral orbits -> 4 moment survivors")
    print("PASS: distance-1 and distance-3 exact determinant obstructions")
    print("PASS: optimal distance-2 edge = 4 + sqrt(14)")


if __name__ == "__main__":
    main()

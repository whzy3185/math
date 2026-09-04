#!/usr/bin/env python3
"""Exact finite audit for the minimal-period-below-eight theorem.

The script enumerates legal local-flux words only for p <= 7, applies the
proved M1--M3 inequalities, reduces by the dihedral action, and verifies one
exact Rayleigh or determinant certificate for each surviving non-balanced
orbit. It is not a search over finite graph signings.
"""

from itertools import product
from math import prod

import sympy as sp


def orbit_rep(q):
    p = len(q)
    images = []
    for k in range(p):
        shifted = q[k:] + q[:k]
        images.extend((shifted, tuple(reversed(shifted))))
    return min(images)


def moment_survivors(p):
    survivors = []
    for q in product((-1, 1), repeat=p):
        if prod(q) != 1:
            continue
        positive = [x == 1 for x in q]
        d = sum(positive)
        a = sum(positive[i] and positive[(i + 1) % p] for i in range(p))
        b = sum(positive[i] and positive[(i + 2) % p] for i in range(p))
        e1 = 16 * d - 12 * p
        e2 = 40 * d + 96 * a + 48 * b - 42 * p
        if e1 <= 0 and e2 <= 0:
            survivors.append(q)
    return sorted({orbit_rep(q) for q in survivors})


def tau_from_q(q):
    tau = [1]
    for value in q[:-1]:
        tau.append(tau[-1] * value)
    assert tau[-1] * q[-1] == tau[0]
    return tau


def fiber(tau, z):
    p = len(tau)
    matrix = sp.zeros(p)
    for r in range(p):
        transitions = (
            (-1, 1),
            (1, 1),
            (-2, tau[(r - 2) % p]),
            (2, tau[r]),
        )
        for displacement, coefficient in transitions:
            cell_shift, residue = divmod(r + displacement, p)
            matrix[r, residue] += coefficient * z**cell_shift
    return matrix


EXPECTED = {
    1: [],
    2: [(-1, -1)],
    3: [(-1, -1, 1)],
    4: [(-1, -1, -1, -1)],
    5: [(-1, -1, -1, -1, 1)],
    6: [
        (-1, -1, -1, -1, -1, -1),
        (-1, -1, -1, -1, 1, 1),
        (-1, -1, -1, 1, -1, 1),
        (-1, -1, 1, -1, -1, 1),
    ],
    7: [
        (-1, -1, -1, -1, -1, -1, 1),
        (-1, -1, -1, 1, -1, 1, 1),
        (-1, -1, 1, -1, -1, 1, 1),
        (-1, -1, 1, -1, 1, -1, 1),
    ],
}


RAYLEIGH = {
    (5, (-1, -1, -1, -1, 1)): (sp.Integer(1), [1, 1, 1, 0, 1], -4),
    (6, (-1, -1, -1, -1, 1, 1)): (sp.Integer(1), [1, 1, 1, 0, 1, 1], -12),
    (6, (-1, -1, -1, 1, -1, 1)): (sp.Integer(-1), [0, 0, 2, -1, 2, -2], -4),
    (6, (-1, -1, 1, -1, -1, 1)): (
        sp.I,
        [3 + sp.I, 3, 3 + 2 * sp.I, 1 + 3 * sp.I, 2 + 2 * sp.I, 4 * sp.I],
        -4,
    ),
    (7, (-1, -1, -1, -1, -1, -1, 1)): (sp.Integer(1), [1, 1, 1, 0, 1, 0, 1], -2),
    (7, (-1, -1, -1, 1, -1, 1, 1)): (sp.Integer(1), [1, 1, 1, 0, 0, 1, 1], -4),
    (7, (-1, -1, 1, -1, -1, 1, 1)): (sp.Integer(1), [1, 1, 1, 1, 1, 1, 1], -8),
    (7, (-1, -1, 1, -1, 1, -1, 1)): (sp.Integer(-1), [1, 1, 1, 1, 1, 1, -1], -8),
}


def main():
    for p in range(1, 8):
        assert moment_survivors(p) == EXPECTED[p]

    # All-negative legal words occur only for even p. Their tau lift is the
    # alternating period-two phase, whose squared edge is exactly eight.
    for p in (2, 4, 6):
        assert tau_from_q((-1,) * p) == [1 if i % 2 == 0 else -1 for i in range(p)]

    # The p=3 survivor has a compact determinant certificate.
    q3 = (-1, -1, 1)
    z3 = sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
    h3 = fiber(tau_from_q(q3), z3)
    assert sp.simplify(h3 - sp.conjugate(h3).T) == sp.zeros(3)
    assert sp.simplify((8 * sp.eye(3) - h3**2).det()) == -1

    for (p, q), (z, vector, expected) in RAYLEIGH.items():
        h = fiber(tau_from_q(q), z)
        assert sp.simplify(h - sp.conjugate(h).T) == sp.zeros(p)
        v = sp.Matrix(vector)
        value = sp.simplify((sp.conjugate(v).T * (8 * sp.eye(p) - h**2) * v)[0])
        assert value == expected

    print("MINIMAL_PERIOD_BELOW_EIGHT_EXACT_AUDIT_PASS")


if __name__ == "__main__":
    main()

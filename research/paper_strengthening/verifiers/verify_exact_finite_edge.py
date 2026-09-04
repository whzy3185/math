#!/usr/bin/env python3
"""Independent symbolic audit of the positive-holonomy exact edge.

This file does not import project constructors or stored certificates.
It rebuilds the polynomial and z=1 fiber directly from displayed data.
"""

import sympy as sp


def main() -> None:
    y, c, u, t, x = sp.symbols("y c u t x", real=True)
    a = sp.sqrt(5)
    s = sp.sqrt(10 + 2 * a)
    eta = 4 + s

    P = y**4 - 16 * y**3 + (80 - 2 * c) * y**2 + (-128 + 16 * c) * y + c**2 - 13 * c + 38
    boundary = (y**2 - 8 * y + 6 - 2 * a) * (y**2 - 8 * y + 6 + 2 * a)
    assert sp.simplify(P.subs(c, 2) - boundary) == 0
    assert sp.simplify(P.subs({y: eta, c: 2})) == 0

    positive_form = (
        u**4
        + 4 * s * u**3
        + 2 * u**2 * t
        + (40 + 12 * a) * u**2
        + 4 * s * u * t
        + 8 * a * s * u
        + t**2
        + (4 * a - 3) * t
    )
    assert sp.simplify(P.subs({y: eta + u, c: 2 - t}) - positive_form) == 0

    z = sp.Integer(1)
    H = sp.Matrix([
        [0, 1, 1, 0, 0, 0, z**-1, z**-1],
        [1, 0, 1, 1, 0, 0, 0, -z**-1],
        [1, 1, 0, 1, -1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 0, -1, 1, 0, 1, -1, 0],
        [0, 0, 0, 1, 1, 0, 1, -1],
        [z, 0, 0, 0, -1, 1, 0, 1],
        [z, -z, 0, 0, 0, -1, 1, 0],
    ])
    assert H == H.T
    cp = H.charpoly()
    charpoly = sp.expand(cp.as_expr().subs(cp.gen, x))
    charpoly_difference = sp.factor(charpoly - P.subs({y: x**2, c: 2}))
    assert charpoly_difference == 0, charpoly_difference
    assert sp.simplify(charpoly.subs(x, sp.sqrt(eta))) == 0
    assert sp.simplify(charpoly.subs(x, -sp.sqrt(eta))) == 0
    assert sp.simplify(sp.diff(charpoly, x).subs(x, sp.sqrt(eta))) != 0
    assert sp.simplify(sp.diff(charpoly, x).subs(x, -sp.sqrt(eta))) != 0

    # The positive-holonomy finite grid always contains z=1.
    for L in range(1, 33):
        assert z**L == 1

    print("EXACT_FINITE_EDGE_SYMBOLIC_AUDIT_PASS")


if __name__ == "__main__":
    main()

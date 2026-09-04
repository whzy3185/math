#!/usr/bin/env python3
"""Independent symbolic audit of the closed period-eight dispersion law."""

import sympy as sp


def main() -> None:
    X, y, c = sp.symbols("X y c", real=True)
    P = y**4 - 16*y**3 + (80-2*c)*y**2 + (-128+16*c)*y + c**2 - 13*c + 38
    shifted = X**4 - (16+2*c)*X**2 + c**2 + 19*c + 38
    assert sp.expand(P.subs(y, X+4) - shifted) == 0

    discriminant = sp.expand((16+2*c)**2 - 4*(c**2+19*c+38))
    assert discriminant == 104 - 12*c

    Wplus = 8 + c + sp.sqrt(26 - 3*c)
    Wminus = 8 + c - sp.sqrt(26 - 3*c)
    assert sp.simplify(Wplus**2 - (16+2*c)*Wplus + c**2+19*c+38) == 0
    assert sp.simplify(Wminus**2 - (16+2*c)*Wminus + c**2+19*c+38) == 0

    r = 4 + sp.sqrt(Wplus)
    assert sp.simplify(P.subs(y, r)) == 0
    assert sp.simplify(r.subs(c, 2) - (4 + sp.sqrt(10+2*sp.sqrt(5)))) == 0

    # Exact derivative formula; positivity on [-2,2] follows from
    # sqrt(26-3c) >= sqrt(20) > 3/2.
    Wprime = sp.diff(Wplus, c)
    assert sp.simplify(Wprime - (1 - sp.Rational(3, 2)/sp.sqrt(26-3*c))) == 0

    theta, L = sp.symbols("theta L", real=True, positive=True)
    cminus = 2 * sp.cos(sp.pi/L)
    rminus = 4 + sp.sqrt(8+cminus+sp.sqrt(26-3*cminus))
    assert sp.simplify(sp.limit(rminus, L, sp.oo) - r.subs(c, 2)) == 0

    print("PERIOD8_CLOSED_DISPERSION_SYMBOLIC_AUDIT_PASS")


if __name__ == "__main__":
    main()

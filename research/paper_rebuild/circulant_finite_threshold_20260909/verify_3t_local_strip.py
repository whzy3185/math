#!/usr/bin/env python3
"""Exact local certificates for the q=3t six-boundary obstruction.

Checks the five switching/permutation types of the 9-vertex three-column strip
used in SIX_BOUNDARY_TRIANGLE_3T.md.  The t=3 Gram-kernel argument is analytic
and needs no enumeration.
"""

import sympy as sp

x = sp.symbols("x")


def strip(a, b):
    A = sp.zeros(9)
    # Three all-negative chord triangles.
    for col in range(3):
        vs = [3 * col + r for r in range(3)]
        for i in range(3):
            for j in range(i + 1, 3):
                A[vs[i], vs[j]] = A[vs[j], vs[i]] = -1
    # Two signed row matchings.
    for r in range(3):
        A[r, 3 + r] = A[3 + r, r] = a[r]
        A[3 + r, 6 + r] = A[6 + r, 3 + r] = b[r]
    return A


reps = {
    "I": ((-1, -1, -1), (-1, -1, -1)),
    "II": ((-1, -1, -1), (-1, -1, +1)),
    "III": ((-1, -1, +1), (-1, -1, -1)),
    "IV": ((-1, -1, +1), (-1, -1, +1)),
    "V": ((-1, -1, +1), (-1, +1, -1)),
}

expected = {
    "I": (x - 1)**2 * (x + 2) * (x**2 - 2*x - 1)**2 * (x**2 + 4*x + 2),
    "II": (x - 1) * (x**2 - 2*x - 1)
        * (x**6 + 3*x**5 - 7*x**4 - 19*x**3 + 12*x**2 + 22*x - 4),
    "III": (x - 1) * (x**2 - 2*x - 1)
        * (x**6 + 3*x**5 - 7*x**4 - 19*x**3 + 12*x**2 + 22*x - 4),
    "IV": (x - 1)**2 * (x + 2) * (x**2 - 2*x - 1)
        * (x**4 + 2*x**3 - 7*x**2 - 8*x + 14),
    "V": (x - 2) * (x - 1) * (x**2 + 2*x - 1)
        * (x**5 + x**4 - 9*x**3 - 5*x**2 + 18*x + 2),
}

for name, (a, b) in reps.items():
    A = strip(a, b)
    p = sp.factor(A.charpoly(x).as_expr())
    assert sp.expand(p - expected[name]) == 0
    print(name, p)

p5 = x**5 + x**4 - 9*x**3 - 5*x**2 + 18*x + 2
assert p5.subs(x, 2) == -6

# Exact kernel identities for the two-column t=3 argument.
K = sp.eye(3) - sp.ones(3)
R = sp.eye(3) + sp.ones(3)  # 2I-K

for diag, expected_nullity in [((-1, -1, -1), 2), ((-1, -1, +1), 1)]:
    D = sp.diag(*diag)
    G2 = sp.BlockMatrix([[R, -D], [-D, R]]).as_explicit()
    assert 6 - G2.rank() == expected_nullity
    print("two-column matching", diag, "kernel basis", G2.nullspace())

print("All q=3t local exact certificates passed.")

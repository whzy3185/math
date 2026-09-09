#!/usr/bin/env python3
"""Exact finite checks supporting SUB_SQRT6_CLASSIFICATION.md.

The script verifies only finite algebraic statements used in the proof:

1. all-negative-triangle switching classes for C_n(1,2), n=6,7,8;
2. their exact characteristic polynomials;
3. the N=14 anticommuting defect characteristic polynomials for s=2,3,4,5
   and both Hamilton holonomies alpha=+-1.

No floating eigenvalue is used as a certificate.  SymPy characteristic polynomials
and exact factorization are the accepted outputs.
"""

from itertools import combinations, product
import sympy as sp

x = sp.symbols("x")


def circulant_edges(n, step=2):
    E = set()
    for i in range(n):
        for d in (1, step):
            j = (i + d) % n
            if i != j:
                E.add(tuple(sorted((i, j))))
    return sorted(E)


def triangles(n, E):
    E = set(E)
    out = []
    for a, b, c in combinations(range(n), 3):
        if all(tuple(sorted(e)) in E for e in ((a, b), (a, c), (b, c))):
            out.append((a, b, c))
    return out


def path_gauge_all_negative_triangle_classes(n):
    E = circulant_edges(n, 2)
    tree = [(i, i + 1) for i in range(n - 1)]
    non_tree = [e for e in E if e not in tree]
    tris = triangles(n, E)

    classes = []
    for signs in product((-1, 1), repeat=len(non_tree)):
        M = sp.zeros(n)
        for i, j in tree:
            M[i, j] = M[j, i] = 1
        for sign, (i, j) in zip(signs, non_tree):
            M[i, j] = M[j, i] = sign
        if all(M[a, b] * M[b, c] * M[c, a] == -1 for a, b, c in tris):
            classes.append((tuple(signs), sp.factor(M.charpoly(x).as_expr())))
    return non_tree, tris, classes


def signed_shift(N, alpha):
    T = sp.zeros(N)
    for i in range(N - 1):
        T[i, i + 1] = 1
    T[N - 1, 0] = alpha
    assert T**N == alpha * sp.eye(N)
    return T


def alternating_D(N):
    return sp.diag(*[(-1) ** i for i in range(N)])


def anti_defect(N, s, alpha):
    T = signed_shift(N, alpha)
    D = alternating_D(N)
    assert D * T == -T * D
    B = T**2 + T**(-2) + (-1) ** s * (T ** (2 * s) + T ** (-2 * s))
    return sp.Matrix(B)


def main():
    expected = {
        6: [x**3 * (x - 2) ** 2 * (x + 4)],
        7: [
            (x + 4) * (x**3 - 2 * x**2 - x + 1) ** 2,
            x * (x**3 - 7 * x + 7) ** 2,
        ],
        8: [
            (x**4 - 8 * x**2 + 8 * x - 2) ** 2,
            x * (x - 2) ** 2 * (x + 4) * (x**2 - 2) ** 2,
        ],
    }

    print("Small parity-component checks")
    for n in (6, 7, 8):
        non_tree, tris, classes = path_gauge_all_negative_triangle_classes(n)
        polys = [sp.factor(p) for _, p in classes]
        assert sorted(map(str, polys)) == sorted(map(str, map(sp.factor, expected[n])))
        print(f"n={n}: triangles={len(tris)}, classes={len(classes)}")
        print("  non-tree edges:", non_tree)
        for signs, poly in classes:
            print("  signs=", signs)
            print("  charpoly=", poly)

    print("\nN=14 anticommuting defect checks")
    good = {(3, -1), (4, -1), (5, 1)}
    target = sp.factor(x**2 * (x**3 - 7 * x + 7) ** 4)
    for s in (2, 3, 4, 5):
        for alpha in (-1, 1):
            B = anti_defect(14, s, alpha)
            poly = sp.factor(B.charpoly(x).as_expr())
            print(f"s={s}, alpha={alpha}: {poly}")
            if (s, alpha) in good:
                assert poly == target
            if s == 2:
                assert poly != target

    print("\nAll exact checks passed.")


if __name__ == "__main__":
    main()

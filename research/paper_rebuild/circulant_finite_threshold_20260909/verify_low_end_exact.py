#!/usr/bin/env python3
"""Exact checks for the low-end finite spectral hierarchy.

This script is reproducibility support only.  The manuscript proofs of the
universal lower bounds are analytic.  Here we verify the explicit equality
certificates used at (N,s)=(5,2), (10,3), and (8,2).
"""

import sympy as sp


def conference_core():
    return sp.Matrix([
        [0, -1,  1,  1, -1],
        [-1, 0, -1,  1,  1],
        [1, -1,  0, -1,  1],
        [1,  1, -1,  0, -1],
        [-1, 1,  1, -1,  0],
    ])


def circulant_signing_hamilton_gauge(N, s, alpha, tau):
    """Signed adjacency matrix in Hamilton gauge.

    Step-1 edges i--i+1 are +1 for i=0,...,N-2 and the seam N-1--0 has
    sign alpha.  The step-s edge i--i+s has sign tau[i].
    """
    assert len(tau) == N
    assert 2 <= s < N / 2
    assert alpha in (-1, 1)
    A = sp.zeros(N)
    for i in range(N - 1):
        A[i, i + 1] = A[i + 1, i] = 1
    A[N - 1, 0] = A[0, N - 1] = alpha
    for i, t in enumerate(tau):
        assert t in (-1, 1)
        j = (i + s) % N
        A[i, j] = A[j, i] = t
    return A


def check_c5():
    W = conference_core()
    assert W * W == 5 * sp.eye(5) - sp.ones(5)
    cp = sp.factor(W.charpoly().as_expr())
    assert cp == sp.Symbol('lambda') * (sp.Symbol('lambda')**2 - 5)**2
    return cp


def check_c10_s3():
    W = conference_core()
    Z = sp.zeros(5)
    A = Z.row_join(W).col_join(W.row_join(Z))
    A2 = A * A
    target = sp.diag(5 * sp.eye(5) - sp.ones(5),
                     5 * sp.eye(5) - sp.ones(5))
    assert A2 == target
    x = sp.Symbol('lambda')
    cp = sp.factor(A.charpoly().as_expr())
    assert cp == x**2 * (x**2 - 5)**4
    return cp


def check_c8_s2_second_gap():
    tau = (-1, 1, -1, 1, -1, 1, 1, -1)
    A = circulant_signing_hamilton_gauge(8, 2, -1, tau)
    x = sp.Symbol('lambda')
    cp = sp.factor(A.charpoly().as_expr())
    assert cp == (x**4 - 8*x**2 + 14)**2

    B = A*A - 4*sp.eye(8)
    cpB = sp.factor(B.charpoly().as_expr())
    assert cpB == (x**2 - 2)**4
    return cp, cpB


def main():
    print('C5(1,2):', check_c5())
    print('C10(1,3):', check_c10_s3())
    cp, cpB = check_c8_s2_second_gap()
    print('C8(1,2) adjacency:', cp)
    print('C8(1,2) defect:', cpB)
    print('all exact checks passed')


if __name__ == '__main__':
    main()

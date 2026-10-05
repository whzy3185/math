#!/usr/bin/env python3
"""Exact verifier for the antiperiodic period-eight circulant construction.

Reconstructed from the retained derivation and verification record after a
workspace reset on 2026-10-05. The finite-size formula is inherited from the
existing mathematics repository; this continuation applies it to Conjecture 28
of the 22 September 2026 v2 manuscript. All generated certificates are recomputed
by this script.
Floating-point illustrations are optional and do not enter the proof.
"""
from pathlib import Path
import json
import sympy as sp

OUT = Path(__file__).resolve().parent
PATTERN = [1, 1, -1, 1, -1, -1, 1, -1]


def signed_matrix(m, antiperiodic=True):
    assert isinstance(m, int) and m >= 1
    n = 8*m
    A = [[0]*n for _ in range(n)]
    for i in range(n):
        for step, sign in [(1, 1), (2, PATTERN[i % 8])]:
            j = (i + step) % n
            if antiperiodic and i + step >= n:
                sign = -sign
            assert A[i][j] == 0 and i != j
            A[i][j] = A[j][i] = sign
    assert all(sum(v != 0 for v in row) == 4 for row in A)
    assert all(A[i][j] == A[j][i] for i in range(n) for j in range(n))
    triangles = [A[i][(i+1) % n]*A[(i+1) % n][(i+2) % n]*A[(i+2) % n][i]
                 for i in range(n)]
    assert triangles == PATTERN*m
    holonomy = 1
    for i in range(n):
        holonomy *= A[i][(i+1) % n]
    assert holonomy == (-1 if antiperiodic else 1)
    return A


def leading_principal_minors(B):
    """Integer Bareiss elimination; kth pivot is leading minor of size k+1."""
    M = [row[:] for row in B]
    n = len(M)
    previous = 1
    minors = []
    for k in range(n):
        pivot = M[k][k]
        assert pivot > 0, (k, pivot)
        minors.append(pivot)
        if k == n-1:
            break
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = pivot*M[i][j] - M[i][k]*M[k][j]
                assert numerator % previous == 0
                M[i][j] = numerator // previous
        for i in range(k+1, n):
            M[i][k] = 0
        previous = pivot
    return minors


def main():
    A = signed_matrix(4)
    cert = {
        'n': 32,
        'step2_pattern': PATTERN,
        'wrap_edges_flipped': [[31, 0], [30, 0], [31, 1]],
        'threshold': {'numerator': 279, 'denominator': 100},
        'matrix': A,
        'provenance': 'Recomputed after 2026-10-05 workspace reset; not a recovered historical output.'
    }
    for sign in [-1, 1]:
        B = [[279*int(i == j) + sign*100*A[i][j] for j in range(32)]
             for i in range(32)]
        minors = leading_principal_minors(B)
        label = 'plus' if sign == 1 else 'minus'
        cert[f'leading_minors_279I_{label}_100A'] = minors
        # Separate determinant algorithm cross-checks selected principal minors.
        for k in [1, 2, 3, 4, 8, 16, 24, 32]:
            assert minors[k-1] == sp.det(sp.Matrix(B)[:k, :k])
    print('PASS: all 64 leading principal minors of 279I +/- 100A are positive.')

    x, z, s = sp.symbols('x z s')
    H = sp.Matrix([
        [0, 1, 1, 0, 0, 0, 1/z, 1/z],
        [1, 0, 1, 1, 0, 0, 0, -1/z],
        [1, 1, 0, 1, -1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 0, -1, 1, 0, 1, -1, 0],
        [0, 0, 0, 1, 1, 0, 1, -1],
        [z, 0, 0, 0, -1, 1, 0, 1],
        [z, -z, 0, 0, 0, -1, 1, 0]
    ])
    P = x**8-16*x**6+80*x**4-128*x**2+38+s*(-2*x**4+16*x**2-13)+s**2
    assert sp.cancel(H.charpoly(x).as_expr()-P.subs(s, z+1/z)) == 0
    f = x**4-2*x**3-6*x**2+12*x-4
    assert sp.expand(P.subs(s, 2)-f*f.subs(x, -x)) == 0
    print('PASS: symbolic 8x8 block determinant and endpoint factorization.')

    B = sp.zeros(8)
    B[6, 0] = 1
    B[7, 0] = 1
    B[7, 1] = -1
    C0 = H.subs(z, 1)-B-B.T
    assert H == C0+z*B+B.T/z
    for m in range(1, 6):
        T = sp.zeros(m)
        for j in range(m-1):
            T[j, j+1] = 1
        T[m-1, 0] = -1
        assert T**m == -sp.eye(m)
        tensor_A = (sp.kronecker_product(sp.eye(m), C0)
                    + sp.kronecker_product(T, B)
                    + sp.kronecker_product(T.T, B.T))
        assert tensor_A == sp.Matrix(signed_matrix(m))
    print('PASS: exact antiperiodic block assembly for m=1,2,3,4,5.')

    t, u = sp.symbols('t u')
    shifted = sum(coef*(t+4)**(power[0]//2)
                  for power, coef in sp.Poly(P, x).terms())
    assert sp.expand(shifted-(t**4-(16+2*s)*t**2+s**2+19*s+38)) == 0
    radical_product = (u-(8+s+sp.sqrt(26-3*s)))*(u-(8+s-sp.sqrt(26-3*s)))
    assert sp.expand(radical_product-(u**2-(16+2*s)*u+s**2+19*s+38)) == 0
    print('PASS: exact nested-radical reduction for every Floquet phase.')

    Q = sp.expand(P.subs(s, sp.sqrt(2))*P.subs(s, -sp.sqrt(2)))
    assert sp.expand(sp.Matrix(A).charpoly(x).as_expr()-Q**2) == 0
    assert Q.subs(x, -x) == Q
    cert['characteristic_polynomial_square_root'] = str(Q)
    print('PASS: direct 32x32 characteristic polynomial is Q(x)^2, where')
    print('Q =', Q)

    q = sp.Rational(279, 100)
    h = -2*x**4+16*x**2-9
    assert f.subs(x, q) < 0
    assert f.subs(x, sp.Rational(14, 5)) > 0
    assert h.subs(x, q) < 0
    cert['f_279_over_100'] = str(f.subs(x, q))
    cert['f_14_over_5'] = str(f.subs(x, sp.Rational(14, 5)))
    cert['h_279_over_100'] = str(h.subs(x, q))
    cert['proof_conclusion'] = 'rho(A32) < 279/100 < r_*'
    (OUT/'exact_n32_certificate.json').write_text(json.dumps(cert, indent=2)+'\n')
    print('f(2.79) =', f.subs(x, q))
    print('f(2.8) =', f.subs(x, sp.Rational(14, 5)))
    print('h(2.79) =', h.subs(x, q))
    print('PASS: rational separation rho(A32)<2.79<r*.')

    try:
        import numpy as np
    except ImportError:
        return
    for m in [1, 2, 3, 4, 5, 8, 16]:
        ev = np.linalg.eigvalsh(signed_matrix(m))
        print(f'illustration m={m}: rho={max(abs(ev)):.15f}')


if __name__ == '__main__':
    main()

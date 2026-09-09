#!/usr/bin/env python3
"""Exact certificates for the currently proved m(N,s)^2=6 examples.

Checks:
  * finite anti-periodic constructions for (12,4) and (20,8);
  * explicit Hamilton-gauge signing for (16,3);
  * exact characteristic-polynomial factors;
  * the multiplier 5 maps C_16(1,3) to C_16(1,5).

All accepted identities use SymPy exact integer arithmetic.
"""

import sympy as sp

x = sp.symbols("x")


def signed_shift(N, alpha=-1):
    T = sp.zeros(N)
    for i in range(N - 1):
        T[i, i + 1] = 1
    T[N - 1, 0] = alpha
    assert T ** N == alpha * sp.eye(N)
    return T


def alternating_construction(N, s):
    T = signed_shift(N, -1)
    D = sp.diag(*[(-1) ** i for i in range(N)])
    assert D * T == -T * D
    A = T + T ** -1 + D * (T ** s) + (T ** (-s)) * D
    return sp.Matrix(A)


def hamilton_gauge_A(N, s, alpha, tau):
    assert len(tau) == N
    A = sp.zeros(N)
    for i in range(N - 1):
        A[i, i + 1] = A[i + 1, i] = 1
    A[N - 1, 0] = A[0, N - 1] = alpha
    for i, sign in enumerate(tau):
        j = (i + s) % N
        A[i, j] = A[j, i] = sign
    return A


def main():
    expected = {
        (12, 4): (x**2 - 6) ** 2 * (x**4 - 6*x**2 + 6) ** 2,
        (20, 8): (x**2 - 6) ** 2
        * (x**8 - 14*x**6 + 66*x**4 - 114*x**2 + 41) ** 2,
    }

    for pair, target in expected.items():
        N, s = pair
        A = alternating_construction(N, s)
        p = sp.factor(A.charpoly(x).as_expr())
        assert sp.expand(p - target) == 0
        B = A * A - 4 * sp.eye(N)
        # 2I-B = 6I-A^2 must be PSD.  The displayed A polynomial shows
        # that 6 is the largest squared eigenvalue; also verify det=0.
        assert (6 * sp.eye(N) - A * A).det() == 0
        print(f"{pair}: chi_A = {p}")

    tau = [-1, 1, -1, 1, -1, 1, -1, -1,
            1, -1, 1, -1, -1, -1, 1, -1]
    A = hamilton_gauge_A(16, 3, -1, tau)
    target = x**2 * (x - 2) * (x + 2) * (x**2 - 6)**4 * (x**2 - 2)**2
    p = sp.factor(A.charpoly(x).as_expr())
    assert sp.expand(p - target) == 0

    B = A * A - 4 * sp.eye(16)
    target_B = x**2 * (x - 2)**8 * (x + 2)**4 * (x + 4)**2
    pB = sp.factor(B.charpoly(x).as_expr())
    assert sp.expand(pB - target_B) == 0

    # Equality-boundary warning: there really are off-diagonal entries of size 2.
    offdiag_twos = []
    for i in range(16):
        for j in range(i + 1, 16):
            if abs(B[i, j]) == 2:
                offdiag_twos.append((i, j, int(B[i, j])))
    assert len(offdiag_twos) == 2
    print("(16,3): chi_A =", p)
    print("(16,3): chi_B =", pB)
    print("size-2 defect entries =", offdiag_twos)

    # Multiplier 5 sends the undirected generator set {+-1,+-3} to {+-1,+-5}.
    mod = 16
    image = {((5 * d) % mod) for d in (1, -1, 3, -3)}
    target_gen = {(d % mod) for d in (1, -1, 5, -5)}
    assert image == target_gen
    print("multiplier 5 identifies C_16(1,3) and C_16(1,5)")

    print("All exact six-boundary certificates passed.")


if __name__ == "__main__":
    main()

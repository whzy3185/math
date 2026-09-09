#!/usr/bin/env python3
"""Exact global certificate for m(12,2)^2 = 5 + sqrt(3).

Hamilton-path gauge gives exactly 2^13 labelled switching classes.  For each
class we form B=A^2-4I and test

    (1+sqrt(3)) I - B >= 0

by exact Schur complements in the ordered quadratic field Q(sqrt(3)).
Exactly two gauge representatives pass.  Their characteristic polynomial is
then checked exactly with SymPy.

Floating point arithmetic is never used for acceptance/rejection.
"""

from dataclasses import dataclass
from fractions import Fraction
import sympy as sp


@dataclass(frozen=True)
class Q3:
    """a + b*sqrt(3), with exact rational a,b."""

    a: Fraction
    b: Fraction

    def __init__(self, a=0, b=0):
        object.__setattr__(self, "a", a if isinstance(a, Fraction) else Fraction(a))
        object.__setattr__(self, "b", b if isinstance(b, Fraction) else Fraction(b))

    def __add__(self, other):
        other = other if isinstance(other, Q3) else Q3(other)
        return Q3(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q3(-self.a, -self.b)

    def __sub__(self, other):
        other = other if isinstance(other, Q3) else Q3(other)
        return self + (-other)

    def __rsub__(self, other):
        return Q3(other) - self

    def __mul__(self, other):
        other = other if isinstance(other, Q3) else Q3(other)
        return Q3(
            self.a * other.a + 3 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def inverse(self):
        den = self.a * self.a - 3 * self.b * self.b
        assert den != 0
        return Q3(self.a / den, -self.b / den)

    def __truediv__(self, other):
        other = other if isinstance(other, Q3) else Q3(other)
        return self * other.inverse()

    def is_zero(self):
        return self.a == 0 and self.b == 0

    def sign(self):
        """Exact sign in the real embedding sqrt(3)>0."""
        a, b = self.a, self.b
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1

        # Opposite signs: compare |a| with |b| sqrt(3) by squaring.
        delta = a * a - 3 * b * b
        if delta == 0:
            return 0
        if a > 0:  # b<0
            return 1 if delta > 0 else -1
        return -1 if delta > 0 else 1  # a<0<b


def exact_psd(matrix):
    """PSD test by exact positive-pivot Schur complements over Q(sqrt(3))."""
    M = [[z if isinstance(z, Q3) else Q3(z) for z in row] for row in matrix]

    while M:
        n = len(M)
        pivot = None
        for i in range(n):
            sig = M[i][i].sign()
            if sig < 0:
                return False
            if sig > 0 and pivot is None:
                pivot = i

        if pivot is None:
            # A PSD matrix with all diagonal entries zero must be the zero matrix.
            return all(M[i][j].is_zero() for i in range(n) for j in range(n))

        if pivot != 0:
            M[0], M[pivot] = M[pivot], M[0]
            for row in M:
                row[0], row[pivot] = row[pivot], row[0]

        d = M[0][0]
        v = [M[i][0] for i in range(1, n)]
        M = [
            [M[i][j] - v[i - 1] * v[j - 1] / d for j in range(1, n)]
            for i in range(1, n)
        ]

    return True


def hamilton_gauge_A(alpha, tau):
    N, s = 12, 2
    A = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N - 1):
        A[i][i + 1] = A[i + 1][i] = 1
    A[N - 1][0] = A[0][N - 1] = alpha
    for i, sign in enumerate(tau):
        j = (i + s) % N
        A[i][j] = A[j][i] = sign
    return A


def defect(A):
    N = len(A)
    B = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            B[i][j] = sum(A[i][k] * A[k][j] for k in range(N))
            if i == j:
                B[i][j] -= 4
    return B


def below_or_at_threshold(B):
    c = Q3(1, 1)  # 1 + sqrt(3)
    N = len(B)
    M = [[Q3(-B[i][j]) for j in range(N)] for i in range(N)]
    for i in range(N):
        M[i][i] = M[i][i] + c
    return exact_psd(M)


def sympy_A(alpha, tau):
    N, s = 12, 2
    A = sp.zeros(N)
    for i in range(N - 1):
        A[i, i + 1] = A[i + 1, i] = 1
    A[N - 1, 0] = A[0, N - 1] = alpha
    for i, sign in enumerate(tau):
        j = (i + s) % N
        A[i, j] = A[j, i] = sign
    return A


def main():
    survivors = []

    for alpha in (-1, 1):
        for mask in range(1 << 12):
            tau = [1 if (mask >> i) & 1 else -1 for i in range(12)]
            A = hamilton_gauge_A(alpha, tau)
            B = defect(A)
            if below_or_at_threshold(B):
                survivors.append((alpha, mask, tau))

    assert len(survivors) == 2, survivors
    assert {a for a, _, _ in survivors} == {-1}

    tau0 = survivors[0][2]
    tau1 = survivors[1][2]
    assert tau1 == [-z for z in tau0]

    x = sp.symbols("x")
    target = (x**2 - 2) ** 2 * (x**4 - 10 * x**2 + 22) ** 2
    for alpha, mask, tau in survivors:
        p = sp.factor(sympy_A(alpha, tau).charpoly(x).as_expr())
        assert sp.expand(p - target) == 0
        print("survivor", alpha, mask, tau)
        print("chi_A =", p)

    print("Exactly two of 8192 switching classes satisfy defect index <= 1+sqrt(3).")
    print("Therefore m(12,2)^2 = 5+sqrt(3).")


if __name__ == "__main__":
    main()

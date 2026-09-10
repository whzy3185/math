#!/usr/bin/env python3
"""Exact Bernstein verifier for the N=3 finite phase diagram.

No floating point is used.  The script constructs the threshold polynomial

    f_m(t) = F_{3,m}(-2+4t) - 2

from the single-square identity, converts it to the Bernstein basis of its
exact degree 2m+6, and checks all coefficients for 24 <= m <= 49.
"""

from fractions import Fraction
from math import comb


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    n = max(len(a), len(b))
    out = [0] * n
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return trim(out)


def sub(a, b):
    n = max(len(a), len(b))
    out = [0] * n
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] -= x
    return trim(out)


def scale(a, c):
    return trim([c * x for x in a])


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def cheb_T(n, x):
    """T_n(x(t)) as an integer-coefficient polynomial in t."""
    if n == 0:
        return [1]
    if n == 1:
        return x[:]
    a = [1]
    b = x[:]
    for _ in range(1, n):
        a, b = b, sub(scale(mul(x, b), 2), a)
    return b


def cheb_U(n, x):
    """U_n(x(t)) as an integer-coefficient polynomial in t."""
    if n == -1:
        return [0]
    if n == 0:
        return [1]
    a = [1]
    b = scale(x, 2)
    if n == 1:
        return b
    for _ in range(1, n):
        a, b = b, sub(scale(mul(x, b), 2), a)
    return b


def bernstein_coefficients(power_coeffs, degree):
    """Convert sum_j a_j t^j to degree-`degree` Bernstein coefficients."""
    a = list(power_coeffs) + [0] * (degree + 1 - len(power_coeffs))
    out = []
    for k in range(degree + 1):
        bk = Fraction(0, 1)
        for j in range(k + 1):
            if a[j]:
                bk += Fraction(a[j] * comb(k, j), comb(degree, j))
        out.append(bk)
    return out


def threshold_polynomial_N3(m):
    # d = -2 + 4t, so x=(4-d)/2=3-2t and y=(4+d)/2=1+2t.
    x = [3, -2]
    y = [1, 2]
    k = [0, 4, -4]  # (x-1)(y-1)=4t(1-t)
    one_minus_t = [1, -1]

    T3x = cheb_T(3, x)
    Tmy = cheb_T(m, y)
    U2x = cheb_U(2, x)
    p = cheb_U(m - 1, y)

    Z = add(mul(T3x, Tmy), mul(k, mul(U2x, p)))

    # Single-square identity:
    # F-2 = 4 Z^2 - 16(1-t)p^2 - 4.
    f = sub(scale(mul(Z, Z), 4), scale(mul(one_minus_t, mul(p, p)), 16))
    f = sub(f, [4])
    return trim(f)


def verify_one(m):
    f = threshold_polynomial_N3(m)
    degree = 2 * m + 6
    assert len(f) - 1 <= degree

    b = bernstein_coefficients(f, degree)
    endpoint_margin = Fraction(39200 - 16 * m * m, 1)

    # f(0) is the first Bernstein coefficient.
    assert b[0] == endpoint_margin
    assert endpoint_margin > 0
    assert all(x >= endpoint_margin for x in b)

    return min(b), max(b), len(b)


def main():
    for m in range(24, 50):
        mn, mx, count = verify_one(m)
        print(
            f"m={m:2d}: degree={2*m+6:3d}, coefficients={count:3d}, "
            f"min={mn}, max={mx}"
        )
    print("All N=3 Bernstein certificates verified exactly for 24 <= m <= 49.")


if __name__ == "__main__":
    main()

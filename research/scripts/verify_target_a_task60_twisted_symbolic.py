"""Symbolic Chebyshev and asymptotic audit for Task 60.1."""

from __future__ import annotations

import sympy as sp


def verify(*, tamper: bool = False) -> dict[str, int]:
    z = sp.symbols("z", real=True)
    polynomial_checks = 0
    for chord in range(2, 11):
        epsilon = (-1) ** chord
        spectral_polynomial = (
            4 + 2 * z + 2 * epsilon * sp.chebyshevt(chord, z)
        )
        derivative = sp.diff(spectral_polynomial, z)
        expected = 2 + 2 * epsilon * chord * sp.chebyshevu(
            chord - 1, z
        )
        if tamper and chord == 5:
            expected += 1
        if sp.expand_trig(sp.simplify(derivative - expected)) != 0:
            raise AssertionError(f"Chebyshev derivative mismatch at s={chord}")
        polynomial_checks += 1

    z3 = 1 / sp.sqrt(3)
    critical3 = 3 * sp.chebyshevu(2, z3) - 1
    if sp.simplify(critical3) != 0:
        raise AssertionError("s=3 critical point mismatch")
    maximum3 = 4 + 2 * z3 - 2 * sp.chebyshevt(3, z3)
    expected3 = 4 + 16 / (3 * sp.sqrt(3))
    if sp.simplify(maximum3 - expected3) != 0:
        raise AssertionError("s=3 exact maximum mismatch")

    h = sp.symbols("h", positive=True)
    chord = sp.symbols("s", integer=True, positive=True)
    even_dispersion = (
        4 + 2 * sp.cos(2 * sp.pi * h)
        + 2 * sp.cos(2 * chord * sp.pi * h)
    )
    series = sp.series(even_dispersion, h, 0, 6).removeO()
    expected_series = (
        8
        - 4 * sp.pi**2 * (1 + chord**2) * h**2
        + sp.Rational(4, 3) * sp.pi**4 * (1 + chord**4) * h**4
    )
    if sp.simplify(series - expected_series) != 0:
        raise AssertionError("even-s asymptotic expansion mismatch")

    return {
        "polynomial_checks": polynomial_checks,
        "s3_checks": 2,
        "asymptotic_checks": 1,
    }


if __name__ == "__main__":
    result = verify()
    print(
        "TARGET_A_TASK60_TWISTED_SYMBOLIC_PASS "
        f"polynomials={result['polynomial_checks']} "
        f"s3={result['s3_checks']} "
        f"asymptotic={result['asymptotic_checks']}"
    )

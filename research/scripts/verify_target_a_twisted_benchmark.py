"""Independent symbolic checks for the article's twisted-benchmark lemma."""

from __future__ import annotations

import sympy as sp


def verify():
    t, phi, lam = sp.symbols("t phi lam", real=True)
    a = 2 * sp.cos(t)
    b = 2 * sp.cos(2 * t)
    block = sp.Matrix([[a, b], [b, -a]])
    g = sp.cos(t) ** 2 + sp.cos(2 * t) ** 2
    u = sp.symbols("u", real=True)
    checks = {
        "block_characteristic_polynomial": sp.trigsimp(
            sp.expand((lam * sp.eye(2) - block).det() - (lam**2 - 4 * g))
        )
        == 0,
        "cosine_square_reduction": sp.expand(
            (4 * u**2 - 3 * u + 1).subs(u, sp.cos(t) ** 2) - g
        ).trigsimp()
        == 0,
        "derivative_factorization": sp.trigsimp(
            sp.diff(g, t) + sp.sin(2 * t) * (1 + 4 * sp.cos(2 * t))
        )
        == 0,
        "final_identity": sp.trigsimp(
            4 * g.subs(t, phi)
            - (4 + 2 * sp.cos(2 * phi) + 2 * sp.cos(4 * phi))
        )
        == 0,
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return {"status": "TWISTED_BENCHMARK_AUDIT_PASS", "checks": checks}


if __name__ == "__main__":
    print(verify())

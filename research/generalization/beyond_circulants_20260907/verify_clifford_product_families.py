#!/usr/bin/env python3
"""Audit representative Clifford-product signed graph identities.

Exact integer matrix multiplication certifies the anticommutation and flat
square identities. Floating eigensolvers are used only to compare the stated
closed spectral-radius formula on non-flat even tori.
"""

from __future__ import annotations

import math
import numpy as np


def anti_cycle(n: int) -> np.ndarray:
    assert n >= 4 and n % 2 == 0
    A = np.zeros((n, n), dtype=np.int64)
    for i in range(n - 1):
        A[i, i + 1] = A[i + 1, i] = 1
    A[0, n - 1] = A[n - 1, 0] = -1
    return A


def parity(n: int) -> np.ndarray:
    return np.diag([1 if i % 2 == 0 else -1 for i in range(n)]).astype(np.int64)


def clifford(mats: list[np.ndarray], pars: list[np.ndarray]) -> np.ndarray:
    dims = [M.shape[0] for M in mats]
    out = np.zeros((int(np.prod(dims)), int(np.prod(dims))), dtype=np.int64)
    for j, M in enumerate(mats):
        ops = []
        for k in range(len(mats)):
            if k < j:
                ops.append(pars[k])
            elif k == j:
                ops.append(M)
            else:
                ops.append(np.eye(dims[k], dtype=np.int64))
        term = ops[0]
        for op in ops[1:]:
            term = np.kron(term, op)
        out += term
    return out


def check_even_torus(lengths: tuple[int, ...]) -> None:
    mats = [anti_cycle(n) for n in lengths]
    pars = [parity(n) for n in lengths]
    for A, D in zip(mats, pars):
        assert np.array_equal(D @ A, -(A @ D))

    S = clifford(mats, pars)
    rho = float(np.max(np.abs(np.linalg.eigvalsh(S.astype(float)))))
    expected_sq = 4.0 * sum(math.cos(math.pi / n) ** 2 for n in lengths)
    assert abs(rho * rho - expected_sq) < 1e-10


def check_flat_c4(d: int) -> None:
    mats = [anti_cycle(4) for _ in range(d)]
    pars = [parity(4) for _ in range(d)]
    S = clifford(mats, pars)
    target = 2 * d * np.eye(S.shape[0], dtype=np.int64)
    assert np.array_equal(S @ S, target)


def check_hypercube(d: int) -> None:
    X = np.array([[0, 1], [1, 0]], dtype=np.int64)
    D = np.diag([1, -1]).astype(np.int64)
    S = clifford([X] * d, [D] * d)
    target = d * np.eye(S.shape[0], dtype=np.int64)
    assert np.array_equal(S @ S, target)


def main() -> None:
    for lengths in ((4, 6), (6, 8), (4, 6, 8)):
        check_even_torus(lengths)
    for d in (1, 2, 3):
        check_flat_c4(d)
    for d in (1, 2, 3, 4, 5):
        check_hypercube(d)
    print("Clifford product identities passed")
    print("even tori checked: (4,6), (6,8), (4,6,8)")
    print("flat C4^d checked for d=1,2,3")
    print("hypercube A^2=dI checked for d=1,...,5")


if __name__ == "__main__":
    main()

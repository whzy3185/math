#!/usr/bin/env python3
"""Exhaustive exact obstruction for all signings of C_21(1,7).

The floating eigensolver is used ONLY to propose a short integer witness.
Every accepted case is certified by the exact integer inequality

    w^T (8 I - A^2) w < 0.

Hence the correctness of a successful run does not depend on the accuracy of
the floating eigenvalue itself.

Enumeration reduction:
- switch to Hamilton gauge;
- a signing is encoded by (Q, anchor, alpha), with prod Q = +1;
- graph translation rotates Q, so one binary necklace per rotation class
  suffices;
- both anchors and both Hamilton holonomies are still scanned.

The run checks 49,940 admissible Q-necklaces and 199,760 gauge representatives.
It also verifies the uniform rational Rayleigh lower bound

    rho(A)^2 >= 8 + 18/131 = 1066/131 > 8.
"""

from __future__ import annotations

import numpy as np


N = 21
S = 7
SCALE = 16


def necklaces(n: int, k: int = 2):
    """Generate k-ary necklaces of length n, one representative per rotation."""
    a = [0] * (n + 1)

    def gen(t: int, p: int):
        if t > n:
            if n % p == 0:
                yield a[1 : n + 1].copy()
        else:
            a[t] = a[t - p]
            yield from gen(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                yield from gen(t + 1, t)

    yield from gen(1, 1)


def tau_from_q(q: np.ndarray, anchor: int) -> np.ndarray:
    tau = np.empty(N, dtype=np.int64)
    tau[0] = anchor
    for i in range(N - 1):
        tau[i + 1] = q[i] * tau[i]
    assert q[N - 1] * tau[N - 1] == tau[0]
    return tau


def adjacency(tau: np.ndarray, alpha: int) -> np.ndarray:
    """Seam-safe Hamilton-gauge adjacency using quasiperiodic wrap factors."""
    A = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        for step, coeff in (
            (+1, 1),
            (-1, 1),
            (+S, int(tau[i])),
            (-S, int(tau[(i - S) % N])),
        ):
            d = i + step
            j = d % N
            wrap = alpha if (d < 0 or d >= N) else 1
            A[i, j] += coeff * wrap
    assert np.array_equal(A, A.T)
    return A


def exact_witness(C: np.ndarray) -> tuple[np.ndarray, int, int]:
    """Find an integer vector and verify its quadratic form exactly.

    np.linalg.eigh only proposes the direction.  The returned q and norm are
    integer dot products.  A successful return satisfies q < 0 and the
    uniform 18/131 excess bound.
    """
    _, vecs = np.linalg.eigh(C.astype(np.float64))
    w = np.rint(SCALE * vecs[:, 0]).astype(np.int64)
    norm = int(w @ w)
    qform = int(w @ (C @ w))
    assert norm > 0
    assert qform < 0
    # -qform/norm >= 18/131, checked without floating arithmetic.
    assert 131 * (-qform) >= 18 * norm
    return w, qform, norm


def main() -> None:
    necklace_count = 0
    representative_count = 0
    weakest_num = None
    weakest_den = None
    weakest_data = None

    for bits in necklaces(N):
        # bit 1 means Q_i=+1; bit 0 means Q_i=-1.
        # prod Q=+1 iff the number of negative entries is even.
        if bits.count(0) % 2 != 0:
            continue
        necklace_count += 1
        q = np.array([1 if b else -1 for b in bits], dtype=np.int64)

        for anchor in (+1, -1):
            tau = tau_from_q(q, anchor)
            for alpha in (+1, -1):
                A = adjacency(tau, alpha)
                C = 8 * np.eye(N, dtype=np.int64) - A @ A
                _, qform, norm = exact_witness(C)
                representative_count += 1

                num = -qform
                den = norm
                if weakest_num is None or num * weakest_den < weakest_num * den:
                    weakest_num, weakest_den = num, den
                    defects = tuple(int(i) for i in np.where(q == 1)[0])
                    weakest_data = (defects, anchor, alpha, qform, norm)

    assert necklace_count == 49_940
    assert representative_count == 199_760
    assert weakest_num * 131 >= 18 * weakest_den

    print(f"Q necklaces checked: {necklace_count}")
    print(f"Hamilton-gauge representatives checked: {representative_count}")
    print(
        "weakest exact witness ratio: "
        f"{-weakest_data[3]}/{weakest_data[4]} "
        f"for defects={weakest_data[0]}, anchor={weakest_data[1]}, "
        f"alpha={weakest_data[2]}"
    )
    print("uniform theorem: rho(A)^2 >= 1066/131 > 8 for every signing")
    print("C_21(1,7) exhaustive exact obstruction passed")


if __name__ == "__main__":
    main()

import itertools

import numpy as np


def adjacency_from_tau(tau: tuple[int, ...]) -> np.ndarray:
    n = len(tau)
    matrix = np.zeros((n, n), dtype=np.int64)
    for i in range(n):
        for distance, sign in ((1, 1), (2, tau[i])):
            j = (i + distance) % n
            matrix[i, j] = matrix[j, i] = sign
    return matrix


def test_fourth_moment_identity_on_all_short_generic_lifts() -> None:
    for n in (10, 12):
        for tau in itertools.product((-1, 1), repeat=n):
            adjacency = adjacency_from_tau(tau)
            q_positive = sum(tau[i] * tau[(i + 1) % n] == 1 for i in range(n))
            assert int(np.trace(np.linalg.matrix_power(adjacency, 4))) == 20 * n + 16 * q_positive

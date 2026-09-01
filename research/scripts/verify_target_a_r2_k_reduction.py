"""Exact structural comparison of the K-reduced residue-two family."""

from __future__ import annotations

import numpy as np

from target_a_flux_search import signing_from_q
from target_a_reproduce import numpy_matrix
from target_a_task48a_common import canonical_code, q_from_gaps
from target_a_task54_threshold import gap_word


def _basis(n: int) -> tuple[np.ndarray, np.ndarray]:
    a = n - 3
    used: set[int] = set()
    plus = []
    minus = []
    for i in range(n):
        j = (a - i) % n
        if i in used:
            continue
        used.update((i, j))
        u_plus = np.zeros(n, dtype=complex)
        u_minus = np.zeros(n, dtype=complex)
        u_plus[i] = u_minus[i] = 2 ** -0.5
        u_plus[j] = 1j * (-1) ** i * 2 ** -0.5
        u_minus[j] = -1j * (-1) ** i * 2 ** -0.5
        plus.append(u_plus)
        minus.append(u_minus)
    return np.column_stack(plus), np.column_stack(minus)


def reduce(n: int) -> dict[str, object]:
    family, gaps = gap_word(n)
    if family != "ONE_G6" or n % 8 != 2:
        raise AssertionError("wrong residue-two family")
    q = q_from_gaps(n, gaps)
    adjacency = numpy_matrix(signing_from_q(canonical_code(q), n, 1)).astype(complex)
    plus, minus = _basis(n)
    if not np.allclose(plus.conj().T @ adjacency @ plus, 0):
        raise AssertionError("K positive sector is not off-diagonal")
    if not np.allclose(minus.conj().T @ adjacency @ minus, 0):
        raise AssertionError("K negative sector is not off-diagonal")
    block = minus.conj().T @ adjacency @ plus
    squared = block.conj().T @ block
    size = n // 2
    complex_entries = sum(abs(value.imag) > 1e-12 for value in squared.flatten())
    long_links = [
        (i, j)
        for i in range(size)
        for j in range(i + 1, size)
        if abs(squared[i, j]) > 1e-12 and j - i > 4
    ]
    return {
        "n": n,
        "reduced_dimension": size,
        "off_diagonal_block_is_complex_symmetric": bool(np.allclose(block, block.T)),
        "generic_block_row_degree": max(sum(abs(block[i, j]) > 1e-12 for j in range(size)) for i in range(size)),
        "squared_complex_entry_count": complex_entries,
        "squared_long_boundary_links": long_links,
    }


def verify() -> dict[str, object]:
    rows = [reduce(n) for n in (50, 58)]
    if not all(row["off_diagonal_block_is_complex_symmetric"] for row in rows):
        raise AssertionError("unexpected K block symmetry")
    if not all(row["generic_block_row_degree"] == 4 for row in rows):
        raise AssertionError("unexpected K block bandwidth")
    if not all(row["squared_complex_entry_count"] > 0 for row in rows):
        raise AssertionError("K reduction unexpectedly became real")
    if not all(len(row["squared_long_boundary_links"]) == 4 for row in rows):
        raise AssertionError("unexpected K boundary structure")
    return {
        "status": "R2_K_REDUCTION_COMPARISON_PASS",
        "rows": rows,
        "decision": "keep real block-Schur route; stop K-reduced propagation route",
    }


if __name__ == "__main__":
    print(verify())

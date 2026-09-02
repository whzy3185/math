"""Exact block-template checks for the standard residue-four two-G6 family."""

from __future__ import annotations

from fractions import Fraction

import numpy as np

from target_a_flux_search import signing_from_q
from target_a_reproduce import numpy_matrix
from target_a_task48a_common import canonical_code, q_from_gaps
from target_a_task54_threshold import gap_word


CAP = Fraction(2679, 338)
ORDERS = (52, 60, 68, 76)
ARC_ORDERS = (76, 92, 108)


def matrix(n):
    family, gaps = gap_word(n)
    if family != "TWO_BALANCED_G6" or n % 8 != 4:
        raise AssertionError("wrong residue-four family")
    q = q_from_gaps(n, gaps)
    adjacency = numpy_matrix(signing_from_q(canonical_code(q), n, -1)).astype(np.int64)
    square = adjacency @ adjacency
    return [
        [Fraction(CAP.numerator if i == j else 0, CAP.denominator) - Fraction(int(square[i, j])) for j in range(n)]
        for i in range(n)
    ]


def blocks(n):
    return [list(range(4))] + [list(range(4 + 8 * j, 12 + 8 * j)) for j in range((n - 4) // 8)]


def block_nonzero(data, left, right):
    return any(data[i][j] != 0 for i in left for j in right)


def cyclic_distance(i, j, count):
    difference = abs(i - j)
    return min(difference, count - difference)


def verify():
    checks = {}
    for n in ORDERS:
        data = matrix(n)
        partition = blocks(n)
        count = len(partition)
        checks[f"n{n}_partition"] = len(partition[0]) == 4 and all(len(block) == 8 for block in partition[1:])
        checks[f"n{n}_covers_vertices"] = sorted(vertex for block in partition for vertex in block) == list(range(n))
        checks[f"n{n}_block_tridiagonal"] = all(
            not block_nonzero(data, partition[i], partition[j])
            for i in range(count)
            for j in range(count)
            if i != j and cyclic_distance(i, j, count) > 1
        )
        checks[f"n{n}_two_g6_word"] = gap_word(n)[1].count(6) == 2

    def arc_templates(n):
        data = matrix(n)
        partition = blocks(n)

        def block(i, j):
            return tuple(tuple(data[row][column] for column in partition[j]) for row in partition[i])

        diagonal = [block(i, i) for i in range(len(partition))]
        links = [block(i, i + 1) for i in range(len(partition) - 1)]
        templates = []
        start = 1
        while start < len(diagonal):
            stop = start + 1
            while stop < len(diagonal) and diagonal[stop] == diagonal[start]:
                stop += 1
            if stop - start >= 2:
                templates.append((diagonal[start], links[start]))
            start = stop
        if len(templates) != 2:
            raise AssertionError(f"unexpected R4 arc decomposition at n={n}")
        return tuple(templates)

    arc_base = arc_templates(ARC_ORDERS[0])
    checks.update({f"n{n}_same_two_bulk_arcs": arc_templates(n) == arc_base for n in ARC_ORDERS})
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "status": "R4_TWO_ARC_TEMPLATE_PASS",
        "orders": ORDERS,
        "block_shape": "one 4-site boundary block plus 8-site cyclic bulk cells",
        "bulk_arc_templates": "two exact 8-site templates stable at n=76,92,108",
        "conclusion": "exact cyclic block-tridiagonal template; no cap theorem asserted",
        "checks": checks,
    }


if __name__ == "__main__":
    print(verify())

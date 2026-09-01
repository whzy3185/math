"""Exact finite audit for the three proposed uniform residue caps."""

from __future__ import annotations

from fractions import Fraction

import numpy as np

from target_a_flux_search import signing_from_q
from target_a_reproduce import numpy_matrix
from target_a_task48a_common import (
    canonical_code,
    q_from_gaps,
    sparse_exact_ldl_positive,
)
from target_a_task54_threshold import gap_word


CAPS = {
    2: Fraction(198, 25),
    4: Fraction(2679, 338),
    6: Fraction(5782, 729),
}


def verify() -> dict[str, object]:
    counts: dict[int, int] = {}
    for residue, cap in CAPS.items():
        count = 0
        for n in range(48, 240, 2):
            if n % 8 != residue:
                continue
            _family, gaps = gap_word(n)
            q = q_from_gaps(n, gaps)
            alpha = -1 if n % 4 == 0 else 1
            adjacency = numpy_matrix(
                signing_from_q(canonical_code(q), n, alpha)
            ).astype(np.int64)
            certificate = (
                cap.numerator * np.eye(n, dtype=np.int64)
                - cap.denominator * (adjacency @ adjacency)
            )
            result = sparse_exact_ldl_positive(certificate)
            if not result["positive"] or len(result["pivots"]) != n:
                raise AssertionError(f"uniform cap failed at n={n}")
            count += 1
        if count != 24:
            raise AssertionError(f"unexpected residue-{residue} count: {count}")
        counts[residue] = count
    return {
        "status": "UNIFORM_CAP_EXACT_FINITE_VERIFY_PASS",
        "caps": {str(key): str(value) for key, value in CAPS.items()},
        "counts": {str(key): value for key, value in counts.items()},
        "total": sum(counts.values()),
    }


if __name__ == "__main__":
    print(verify())

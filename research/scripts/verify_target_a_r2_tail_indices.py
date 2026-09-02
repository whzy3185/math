"""Exact indexing and coarse-constant checks for the residue-two tail draft."""

from __future__ import annotations

from fractions import Fraction

from verify_target_a_r2_bulk_invariant_box import E_PLUS


SEED_BLOCK_COUNT = 102
ENTRANCE_SINGLE_STEPS = 24
Q = Fraction(2, 3)


def frobenius_squared(matrix):
    return sum(entry * entry for row in matrix for entry in row)


def verify():
    terminal_index = SEED_BLOCK_COUNT - 1
    propagated_updates = terminal_index - 1
    transfers_after_entrance = propagated_updates - ENTRANCE_SINGLE_STEPS
    checks = {
        "seed_block_count_even": SEED_BLOCK_COUNT % 2 == 0,
        "terminal_index_odd": terminal_index % 2 == 1,
        "post_entrance_updates_even": transfers_after_entrance % 2 == 0,
        "complete_two_cell_transfers": transfers_after_entrance // 2 == 38,
        "terminal_coupling_is_plus": terminal_index % 2 == 1,
        "coupling_frobenius_squared_below_sixteen": frobenius_squared(E_PLUS) < 16,
        "q76_below_one_over_125000": Q**76 < Fraction(1, 125000),
        "quadratic_series_below_one_over_billion": (
            Fraction(48, 10**8) * Q**76 / (1 - Q**2) < Fraction(1, 10**9)
        ),
        "terminal_cross_bound_below_one_over_million": (
            24 * Fraction(4, 10**4) * Q**38 < Fraction(1, 10**6)
        ),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "status": "R2_TAIL_INDEX_AND_CONSTANTS_PASS",
        "checks": checks,
    }


if __name__ == "__main__":
    print(verify())

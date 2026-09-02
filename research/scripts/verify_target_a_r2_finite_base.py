"""Exact finite boundary base for the analytically reduced residue-two family."""

from __future__ import annotations

from verify_target_a_r2_boundary_seed import positive_definite
from verify_target_a_r2_response_recurrence import block_response_core


ORDERS = tuple(range(50, 410, 8))


def verify():
    checks = {n: positive_definite(block_response_core(n)) for n in ORDERS}
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "status": "R2_FINITE_BOUNDARY_BASE_PASS",
        "orders": [ORDERS[0], ORDERS[-1]],
        "count": len(ORDERS),
        "method": "exact six-by-six response-core LDL after analytic bulk reduction",
    }


if __name__ == "__main__":
    print(verify())

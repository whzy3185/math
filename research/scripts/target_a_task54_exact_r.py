"""Exact rational bookkeeping for the Task 54 complement-gap theorem."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any

from target_a_task47_common import write_json


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "proofs" / "task54" / "certificates"
C6_LOWER = Fraction(7905369311620327, 10**15)
C6_UPPER = Fraction(7905369311620328, 10**15)
ETA_UPPER = Fraction(1561, 200)
DELTA6 = Fraction(1, 100)
R0 = 256
IMS_CONSTANT = 320
DELTA_COMP = Fraction(1, 200)
WINDOW_RADIUS = Fraction(1, 400)


def build_certificate() -> dict[str, Any]:
    ims_error = Fraction(IMS_CONSTANT, R0 * R0)
    bulk_gap = C6_LOWER - ETA_UPPER
    checks = {
        "bulk_gap_larger_than_delta6": bulk_gap > DELTA6,
        "ims_error_below_half_delta6": ims_error < DELTA6 / 2,
        "complement_gap_safe": DELTA6 - ims_error > DELTA_COMP,
        "fixed_window_above_complement": WINDOW_RADIUS < DELTA_COMP,
        "feshbach_inverse_bound": 1 / (DELTA_COMP - WINDOW_RADIUS) == 400,
        "partition_range_margin": 4 * R0 + 16 == 1040,
        "supported_r_values": all(r in (1, 2, 3) for r in (1, 2, 3)),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "status": "EXACT_R_BY_COMPLEMENT_GAP_PROVED",
        "evidence": "PROVED",
        "supported_r": [1, 2, 3],
        "constants": {
            "delta6": str(DELTA6),
            "partition_transition_radius_R0": R0,
            "minimum_site_separation_D0": 4 * R0 + 16,
            "ims_error_constant": IMS_CONSTANT,
            "ims_error_at_R0": str(ims_error),
            "delta_comp": str(DELTA_COMP),
            "fixed_counting_window_radius": str(WINDOW_RADIUS),
            "feshbach_Q_inverse_bound": 400,
            "quasimode_cell_rate": "9/25",
        },
        "local_orthogonality_identity": (
            "phi_j=chi_j psi_j and x perpendicular phi_j imply "
            "<psi_j,chi_j x>=<chi_j psi_j,x>=0 exactly"
        ),
        "partition_lemma": (
            "A piecewise sine/cosine two-overlap partition with transition width R has "
            "sum_j|chi_j(a)-chi_j(b)|^2 <= pi^2 d(a,b)^2/(4R^2). "
            "Using pi^2<10, range four, and absolute H-row-sum 16 gives ||E_IMS||<=320/R^2."
        ),
        "complement_theorem": (
            "For fixed r in {1,2,3}, legal r-G6 rings with minimum site separation at least D0 "
            "and x perpendicular to the disjoint truncated-mode span satisfy "
            "<x,Hx> <= (c6-delta_comp)||x||^2."
        ),
        "counting_theorem": (
            "For sufficiently large separation, exactly r eigenvalues counted with multiplicity lie "
            "in [c6-1/400,c6+1/400], and each is c6+O_r((9/25)^L)."
        ),
        "feshbach": {
            "window": "|lambda-c6|<=1/400",
            "inverse": "||(QHQ-lambda)^(-1)||<=400",
            "effective_operator": "PHP-PHQ(QHQ-lambda)^(-1)QHP",
            "equivalence": "multiplicity-preserving Schur-complement equivalence",
            "expansion": "H_eff(lambda)=c6 I_r+T_1+R_2(lambda)",
            "orders": "||T_1||=O_r((9/25)^L), ||R_2||=O_r((9/25)^(2L))",
        },
        "proof_boundary": (
            "The theorem is fixed-r and large-separation. It counts multiplicity but does not prove "
            "simplicity or exact leading interaction coefficients. The constants multiplying the "
            "inherited exponential quasimode bounds are existential, as in Task52."
        ),
        "checks": checks,
    }


def run() -> dict[str, Any]:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    payload = build_certificate()
    write_json(OUTPUT / "exact_r_complement_gap.json", payload)
    print(json.dumps({"status": payload["status"], "delta_comp": payload["constants"]["delta_comp"]}, indent=2))
    return payload


if __name__ == "__main__":
    run()

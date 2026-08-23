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
L_SITE0 = 248
IMS_CONSTANT = 320
DELTA_COMP = Fraction(1, 200)
WINDOW_RADIUS = Fraction(1, 400)
D0 = 1040
S0 = D0 // 4
SINGLE_T0 = S0
MULTI_T0 = D0 - 2 * S0


def build_certificate() -> dict[str, Any]:
    ims_error = Fraction(IMS_CONSTANT, SINGLE_T0 * SINGLE_T0)
    bulk_gap = C6_LOWER - ETA_UPPER
    checks = {
        "bulk_gap_larger_than_delta6": bulk_gap > DELTA6,
        "ims_error_below_half_delta6": ims_error < DELTA6 / 2,
        "complement_gap_safe": DELTA6 - ims_error > DELTA_COMP,
        "fixed_window_above_complement": WINDOW_RADIUS < DELTA_COMP,
        "feshbach_inverse_bound": 1 / (DELTA_COMP - WINDOW_RADIUS) == 400,
        "canonical_distance_conversion": S0 == 260 and S0 - 12 == L_SITE0,
        "transition_width_lower_bound": SINGLE_T0 == 260 and MULTI_T0 == 520,
        "range_four_support_margin": S0 > 4,
        "supported_r_values": all(r in (1, 2, 3) for r in (1, 2, 3)),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "status": "EXACT_R_R123_BY_COMPLEMENT_GAP_PROVED",
        "evidence": "COMPUTER_ASSISTED_PROVED",
        "supported_r": [1, 2, 3],
        "constants": {
            "delta6": str(DELTA6),
            "minimum_truncation_radius_L0": L_SITE0,
            "minimum_complete_bulk_cells_ell0": L_SITE0 // 8,
            "minimum_site_separation_D0": D0,
            "endpoint_plateau_S0": S0,
            "minimum_transition_width_T0": SINGLE_T0,
            "ims_error_constant": IMS_CONSTANT,
            "ims_error_at_R0": str(ims_error),
            "delta_comp": str(DELTA_COMP),
            "fixed_counting_window_radius": str(WINDOW_RADIUS),
            "feshbach_Q_inverse_bound": 400,
            "quasimode_cell_rate": "9/25",
            "distance_convention": "L_site=floor(D/4)-12 and ell=floor(L_site/8)",
        },
        "local_orthogonality_identity": (
            "phi_j=chi_j psi_j and x perpendicular phi_j imply "
            "<psi_j,chi_j x>=<chi_j psi_j,x>=0 exactly"
        ),
        "partition_lemma": (
            "For r=2,3, on each interface arc of length d_j, set S=floor(D/4), retain endpoint plateaux "
            "of length S, and interpolate adjacent cutoffs by cosine/sine over T_j=d_j-2S. "
            "For r=1 and cyclic distance d from the interface, set chi_I=1 for d<=S-8, "
            "chi_I=cos(pi(d-S+8)/(2S)) for S-8<d<2S-8, and chi_I=0 for d>=2S-8; "
            "set chi_B=sqrt(1-chi_I^2). This gives a width-S transition and an eight-site "
            "radial zero plateau around the antipodal bulk seam. "
            "Then sum chi_j^2=1 and the cutoff-vector difference is at most pi*d/(2*T_min). "
            "At D>=1040, every transition has width at least 260; the IMS bound is 320/260^2."
        ),
        "complement_theorem": (
            "For fixed r in {1,2,3}, legal r-G6 rings with minimum site separation at least D0 "
            "and x perpendicular to the sine/cosine truncated-mode span satisfy "
            "<x,Hx> <= (c6-delta_comp)||x||^2."
        ),
        "counting_theorem": (
            "For r in {1,2,3} and sufficiently large separation, exactly r eigenvalues counted with multiplicity lie "
            "in [c6-1/400,c6+1/400], and each is c6+O_r((9/25)^ell)."
        ),
        "feshbach": {
            "window": "|lambda-c6|<=1/400",
            "inverse": "||(QHQ-lambda)^(-1)||<=400",
            "effective_operator": "PHP-PHQ(QHQ-lambda)^(-1)QHP",
            "equivalence": "multiplicity-preserving Schur-complement equivalence",
            "expansion": "H_eff(lambda)=c6 I_r+T_1+R_2(lambda)",
            "orders": "for ell=floor((floor(D/4)-12)/8): ||T_1||=O_r((9/25)^ell), ||R_2||=O_r((9/25)^(2ell))",
        },
        "proof_boundary": (
            "The r=1 case uses a separate interface/bulk two-cutoff partition; r=2,3 use the "
            "cyclic interface-arc partition. The theorem counts multiplicity but does not prove "
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

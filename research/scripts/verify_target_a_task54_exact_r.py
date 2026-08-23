"""Independent arithmetic and scope checker for Task 54 exact-r."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


RESEARCH = Path(__file__).resolve().parents[1]
CERTIFICATE = RESEARCH / "proofs" / "task54" / "certificates" / "exact_r_complement_gap.json"


def verify(path: Path = CERTIFICATE) -> dict[str, bool]:
    data = json.loads(path.read_text(encoding="utf-8"))
    constants = data["constants"]
    error = Fraction(constants["ims_error_constant"], constants["minimum_transition_width_T0"] ** 2)
    expected_check_keys = {
        "bulk_gap_larger_than_delta6", "ims_error_below_half_delta6",
        "complement_gap_safe", "fixed_window_above_complement",
        "feshbach_inverse_bound", "canonical_distance_conversion",
        "transition_width_lower_bound", "range_four_support_margin",
        "supported_r_values",
    }
    checks = {
        "status_exact": data["status"] == "EXACT_R_R123_BY_COMPLEMENT_GAP_PROVED",
        "evidence_inherits_isolation": data["evidence"] == "COMPUTER_ASSISTED_PROVED",
        "r_scope_exact": data["supported_r"] == [1, 2, 3],
        "distance_geometry_rebuilt": (
            constants["minimum_site_separation_D0"] == 1040
            and constants["endpoint_plateau_S0"] == 260
            and constants["minimum_truncation_radius_L0"] == 248
            and constants["minimum_complete_bulk_cells_ell0"] == 31
            and constants["minimum_transition_width_T0"] == 260
            and constants["distance_convention"]
            == "L_site=floor(D/4)-12 and ell=floor(L_site/8)"
        ),
        "ims_error_rebuilt": str(error) == constants["ims_error_at_R0"],
        "complement_margin_rebuilt": Fraction(1, 100) - error > Fraction(constants["delta_comp"]),
        "counting_window_rebuilt": Fraction(constants["fixed_counting_window_radius"]) < Fraction(constants["delta_comp"]),
        "inverse_bound_rebuilt": 1 / (Fraction(constants["delta_comp"]) - Fraction(constants["fixed_counting_window_radius"])) == constants["feshbach_Q_inverse_bound"],
        "no_simplicity_overclaim": "does not prove simplicity" in data["proof_boundary"],
        "r1_partition_explicit": "r=1 case uses a separate" in data["proof_boundary"],
        "r1_partition_discrete_formula": "chi_I=cos(pi(d-S+8)/(2S))" in data["partition_lemma"],
        "stored_checks_exact_and_true": (
            set(data["checks"]) == expected_check_keys and all(data["checks"].values())
        ),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return checks


if __name__ == "__main__":
    verify()
    print("TARGET_A_TASK54_EXACT_R_VERIFY_PASS")

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
    error = Fraction(constants["ims_error_constant"], constants["partition_transition_radius_R0"] ** 2)
    checks = {
        "r_scope_exact": data["supported_r"] == [1, 2, 3],
        "ims_error_rebuilt": str(error) == constants["ims_error_at_R0"],
        "complement_margin_rebuilt": Fraction(1, 100) - error > Fraction(constants["delta_comp"]),
        "counting_window_rebuilt": Fraction(constants["fixed_counting_window_radius"]) < Fraction(constants["delta_comp"]),
        "inverse_bound_rebuilt": 1 / (Fraction(constants["delta_comp"]) - Fraction(constants["fixed_counting_window_radius"])) == constants["feshbach_Q_inverse_bound"],
        "no_simplicity_overclaim": "does not prove simplicity" in data["proof_boundary"],
        "stored_checks_true": all(data["checks"].values()),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return checks


if __name__ == "__main__":
    verify()
    print("TARGET_A_TASK54_EXACT_R_VERIFY_PASS")

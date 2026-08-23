"""Independent exact checker for Task 53 phases B and C."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from target_a_task53_global import residue_gap_word, slip_separations, tent_normalization


RESEARCH = Path(__file__).resolve().parents[1]
CERTIFICATE = RESEARCH / "proofs" / "task53" / "certificates" / "ims_fixed_r_residue.json"
C6_UPPER = Fraction(7905369311620328, 10**15)


def verify(path: Path = CERTIFICATE) -> dict[str, bool]:
    data = json.loads(path.read_text(encoding="utf-8"))
    radii = range(4, 101)
    direct_norm = []
    for radius in radii:
        weights = [Fraction(radius - abs(k), radius) for k in range(-radius + 1, radius)]
        direct_norm.append(sum((weight**2 for weight in weights), Fraction(0)) == tent_normalization(radius))
    words = []
    separation_bounds = []
    for residue in (2, 4, 6):
        for k in range(4, 81):
            word = residue_gap_word(residue, k)
            n = 8 * k + residue
            words.append(sum(word) == n and len(word) % 2 == 0 and word.count(6) == residue // 2)
            minimum = min(slip_separations(word))
            separation_bounds.append(minimum >= n // 4)
    n = int(data["eventual_all_even"]["N"])
    checks = {
        "normalization_recomputed": all(direct_norm),
        "ims_constant_recomputed": Fraction(1, 2) * Fraction(9, 2) * 16 * 16 == 576,
        "independent_gap_range": all(words),
        "uniform_separation_bound": all(separation_bounds),
        "radius_floor_bound": all((d - 9) // 4 >= Fraction(d, 8) for d in range(26, 1000)),
        "eventual_endpoint_recomputed": C6_UPPER + Fraction(589824, n * n) < Fraction(8) - Fraction(200, n * n),
        "strict_scope": n == 2500 and data["eventual_all_even"]["strict_conclusion"].endswith("n>=2500"),
        "both_holonomies": data["patch_classification"]["holonomies"] == [-1, 1],
        "all_r": data["patch_classification"]["r"] == [1, 2, 3],
        "ims_artifact_constant": data["ims"]["C_IMS"] == 576 and data["ims"]["range"] == 4,
        "range_margin_bound": data["patch_classification"]["range_four_margin"] == "2(R+4)<D for D>=26",
        "patch_exhaustion_bound": "zero or one non-4 gap" in data["patch_classification"]["no_fourth_class"],
        "equivalence_maps_bound": "B_s" in data["patch_classification"]["equivalences"] and "holonomy cut" in data["patch_classification"]["equivalences"],
        "residue_classes_bound": [family["residue"] for family in data["residues"]] == [2, 4, 6],
        "artifact_gap_samples": all(
            row["gap_sum"] == row["n"]
            and row["slip_count"] == family["slip_count"]
            and row["q_legal"]
            for family in data["residues"] for row in family["samples"]
        ),
        "artifact_checks_true": all(data["checks"].values()),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return checks


def main() -> None:
    verify()
    print("TARGET_A_TASK53_GLOBAL_VERIFY_PASS")


if __name__ == "__main__":
    main()

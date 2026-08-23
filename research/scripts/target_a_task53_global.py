"""Exact analytic constants for Task 53 phases B and C."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any

from target_a_task47_common import write_json


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "proofs" / "task53" / "certificates"
C6_UPPER = Fraction(7905369311620328, 10**15)
C_IMS = 576
EVENTUAL_N = 2500


def tent_normalization(radius: int) -> Fraction:
    if radius < 1:
        raise ValueError("radius must be positive")
    return Fraction(2 * radius * radius + 1, 3 * radius)


def residue_gap_word(residue: int, k: int) -> list[int]:
    if residue == 2:
        if k < 1:
            raise ValueError("k is too small")
        return [6] + [4] * (2 * k - 1)
    if residue == 4:
        if k < 1:
            raise ValueError("k is too small")
        return [6] + [4] * (k - 1) + [6] + [4] * (k - 1)
    if residue == 6:
        if k < 2:
            raise ValueError("k is too small")
        total = 2 * k - 3
        counts = [total // 3, (total + 1) // 3, (total + 2) // 3]
        word = []
        for count in counts:
            word.extend([6] + [4] * count)
        return word
    raise ValueError("residue must be 2, 4, or 6")


def slip_separations(word: list[int]) -> list[int]:
    slip_indices = [index for index, gap in enumerate(word) if gap == 6]
    if len(slip_indices) == 1:
        return [sum(word)]
    separations = []
    for position, start in enumerate(slip_indices):
        stop = slip_indices[(position + 1) % len(slip_indices)]
        total = word[start]
        index = (start + 1) % len(word)
        while index != stop:
            total += word[index]
            index = (index + 1) % len(word)
        separations.append(total)
    return separations


def partition_radius(minimum_separation: int) -> int:
    return (minimum_separation - 9) // 4


def build_certificate() -> dict[str, Any]:
    sample_radii = range(4, 65)
    normalization_checks = [
        tent_normalization(radius)
        == 1 + 2 * sum((Fraction(j, radius) ** 2 for j in range(1, radius)), Fraction(0))
        for radius in sample_radii
    ]
    residues = []
    for residue in (2, 4, 6):
        sample_rows = []
        for k in range(4, 41):
            word = residue_gap_word(residue, k)
            n = 8 * k + residue
            separations = slip_separations(word)
            defect_count = len(word)
            sample_rows.append({
                "k": k,
                "n": n,
                "gap_word": word,
                "gap_sum": sum(word),
                "defect_count": defect_count,
                "q_legal": (n - defect_count) % 2 == 0,
                "slip_count": word.count(6),
                "separations": separations,
                "minimum_separation": min(separations),
            })
        residues.append({
            "residue": residue,
            "slip_count": residue // 2,
            "formula": {
                2: "[6,4^(2k-1)]",
                4: "[6,4^(k-1),6,4^(k-1)]",
                6: "[6,4^floor((2k-3)/3),6,4^floor((2k-2)/3),6,4^floor((2k-1)/3)]",
            }[residue],
            "samples": sample_rows,
            "limsup_bound": "c6",
        })

    eventual_left = C6_UPPER + Fraction(589824, EVENTUAL_N**2)
    eventual_right = Fraction(8) - Fraction(200, EVENTUAL_N**2)
    checks = {
        "tent_normalization_exact": all(normalization_checks),
        "ims_constant_from_row_bound": C_IMS == Fraction(1, 2) * Fraction(9, 2) * 4**2 * 16,
        "all_gap_samples_sum_to_order": all(
            row["gap_sum"] == row["n"] for family in residues for row in family["samples"]
        ),
        "all_gap_samples_legal": all(
            row["q_legal"] and row["defect_count"] % 2 == 0
            for family in residues for row in family["samples"]
        ),
        "correct_slip_counts": all(
            row["slip_count"] == family["slip_count"]
            for family in residues for row in family["samples"]
        ),
        "eventual_rational_inequality": eventual_left < eventual_right,
        "eventual_n_even": EVENTUAL_N % 2 == 0,
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "status": "GATES_B1_B2_B3_AND_C_PASS",
        "evidence": "PROVED",
        "ims": {
            "identity": "H=sum_j chi_j H chi_j + (1/2)sum_j[chi_j,[chi_j,H]]",
            "entry_identity": "[chi,[chi,H]]_ab=(chi(a)-chi(b))^2 H_ab",
            "range": 4,
            "absolute_row_sum_H": 16,
            "generic_collision_free_minimum_order": 9,
            "tent_normalization": "(2R^2+1)/(3R)",
            "cutoff_vector_difference": "sum_j(chi_j(a)-chi_j(b))^2 <= 9 d(a,b)^2/(2R^2)",
            "C_IMS": C_IMS,
            "error": "576/R^2",
            "cyclic_scope": "n>2R+4; all cutoff translates are taken modulo n",
        },
        "patch_classification": {
            "classes": ["PURE_BULK", "FORWARD_G6", "REFLECTED_G6"],
            "r": [1, 2, 3],
            "holonomies": [-1, 1],
            "radius": "R=floor((D-9)/4), where D is the minimum cyclic interface separation in sites",
            "range_four_margin": "2(R+4)<D for D>=26",
            "equivalences": (
                "Translate the nearest positive Q defect to 0; use a diagonal tree-gauge to set all "
                "step-1 signs on the proper arc to +1; translate B_s to B_0; reflect the arc when "
                "the gap-6 orientation is reversed. A holonomy cut inside the arc is moved out by "
                "the same diagonal gauge."
            ),
            "no_fourth_class": (
                "A radius-(R+4) arc meets zero or one non-4 gap. Zero gives a translated bulk sector; "
                "one gives one of the two oriented G6 models."
            ),
        },
        "fixed_r_cap": {
            "theorem": "rho(A_ring)^2 <= c6 + 576/R^2 for r=1,2,3 and alpha=+/-1",
            "minimum_separation": "D>=26",
            "asymptotic_form": "R>=D/8, hence rho^2 <= c6 + 36864/D^2",
            "proof": (
                "Each localized quadratic form is bounded by c6 using the bulk or global G6 edge; "
                "the operator-norm IMS remainder supplies the displayed error."
            ),
        },
        "residues": residues,
        "eventual_all_even": {
            "N": EVENTUAL_N,
            "upper": "m_n^2 <= c6_upper + 589824/n^2 for all even n>=N",
            "antibalanced_lower": "rho_-(n)^2 >= 8-200/n^2, using sin(x)<=x and pi^2<10",
            "endpoint_check": {"left": str(eventual_left), "right": str(eventual_right)},
            "strict_conclusion": "m_n<rho_-(n) for every even n>=2500",
        },
        "charge_fractionalization": {
            "two_slips": "limsup level <=c6<c_(+4)",
            "three_slips": "limsup level <=c6<c_(+6)=c10",
            "scope": "asymptotic constructions, not minimization over all charge decompositions",
        },
        "checks": checks,
    }


def run() -> dict[str, Any]:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    payload = build_certificate()
    write_json(OUTPUT / "ims_fixed_r_residue.json", payload)
    print(json.dumps({"status": payload["status"], "N": payload["eventual_all_even"]["N"]}, indent=2))
    return payload


if __name__ == "__main__":
    run()

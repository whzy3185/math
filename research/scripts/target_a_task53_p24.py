"""Exact Rayleigh witnesses and completeness audit for Task 53 side module S2."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
from typing import Any

import numpy as np
import sympy as sp

from target_a_low_period_spectral_frontier import (
    bloch_laurent_matrix,
    canonical_q,
    evaluate_bloch,
    tau_lift,
)
from target_a_task47_common import write_json


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "proofs" / "task53" / "certificates"
C6_UPPER = sp.Rational(7905369311620328, 10**15)
ROOTS = (("1", 1.0 + 0.0j), ("-1", -1.0 + 0.0j), ("i", 1.0j), ("-i", -1.0j))


def q_from_bits(bits: str) -> tuple[int, ...]:
    return tuple(1 if bit == "1" else -1 for bit in bits)


def canonical_key(q: tuple[int, ...]) -> tuple[int, str]:
    word = canonical_q(q)
    return len(word), "".join("1" if value == 1 else "0" for value in word)


def exact_bloch_matrix(tau: tuple[int, ...], root: str) -> sp.Matrix:
    z = {"1": sp.Integer(1), "-1": sp.Integer(-1), "i": sp.I, "-i": -sp.I}[root]
    laurent = bloch_laurent_matrix(tau)
    return sp.Matrix([
        [sum(sp.Integer(coefficient) * z**power for power, coefficient in entry.items()) for entry in row]
        for row in laurent
    ])


def exact_rayleigh(matrix: sp.Matrix, vector: list[tuple[int, int]]) -> tuple[int, int]:
    column = sp.Matrix([sp.Integer(real) + sp.I * sp.Integer(imag) for real, imag in vector])
    image = matrix * column
    numerator = sp.expand((sp.conjugate(image).T * image)[0])
    denominator = sp.expand((sp.conjugate(column).T * column)[0])
    if not (numerator.is_Integer and denominator.is_Integer and denominator > 0):
        raise AssertionError("nonintegral Gaussian Rayleigh data")
    return int(numerator), int(denominator)


def discover_witness(q: tuple[int, ...]) -> dict[str, Any]:
    tau = tau_lift(q)
    laurent = bloch_laurent_matrix(tau)
    best = None
    for name, root in ROOTS:
        values, vectors = np.linalg.eigh(evaluate_bloch(laurent, root))
        index = int(np.argmax(np.abs(values)))
        score = float(values[index] ** 2)
        if best is None or score > best[0]:
            best = (score, name, vectors[:, index])
    assert best is not None
    _score, name, vector = best
    gaussian = [(int(round(20 * value.real)), int(round(20 * value.imag))) for value in vector]
    numerator, denominator = exact_rayleigh(exact_bloch_matrix(tau, name), gaussian)
    if sp.Integer(numerator) * C6_UPPER.q <= C6_UPPER.p * sp.Integer(denominator):
        raise AssertionError("discovered witness does not beat c6_upper")
    return {
        "period": len(q),
        "q_bits": canonical_key(q)[1],
        "tau": list(tau),
        "bloch_root": name,
        "gaussian_integer_vector": [[real, imag] for real, imag in gaussian],
        "numerator_A2": numerator,
        "denominator": denominator,
        "rayleigh_quotient": f"{numerator}/{denominator}",
        "strict_margin_numerator_against_c6_upper": str(
            sp.Integer(numerator) * C6_UPPER.q - C6_UPPER.p * sp.Integer(denominator)
        ),
    }


def build_certificate() -> dict[str, Any]:
    csv_path = RESEARCH / "experiments" / "task51" / "subeight_periodic_phases.csv"
    csv_rows = list(csv.DictReader(csv_path.open(encoding="utf-8")))
    residual_keys = set()
    for row in csv_rows:
        if row["band_at_8"] != "R_LT_8":
            continue
        period = int(row["primitive_Q_period"])
        q = q_from_bits(row["Q_bits"][:period])
        key = canonical_key(q)
        if not (key[0] == 4 and int(row["primitive_tau_period"]) == 8):
            residual_keys.add(key)

    low_path = RESEARCH / "proofs" / "target_a_low_period_spectral_frontier.json"
    low = json.loads(low_path.read_text())
    weak_old_keys = set()
    for row in low["orbits"]:
        if row["target_infinite_phase"]:
            continue
        quotient = row["exact_certificate"].get("quotient")
        if quotient is not None and sp.Rational(quotient) <= C6_UPPER:
            weak_old_keys.add((int(row["p"]), row["canonical_q_bits"]))

    witness_keys = sorted(residual_keys | weak_old_keys)
    witnesses = [discover_witness(q_from_bits(bits)) for _period, bits in witness_keys]
    witness_map = {(row["period"], row["q_bits"]): row for row in witnesses}

    low_counts = {"moment_gt_8": 0, "old_rayleigh_gt_c6": 0, "new_witness": 0, "target": 0}
    for row in low["orbits"]:
        if row["target_infinite_phase"]:
            low_counts["target"] += 1
            continue
        certificate = row["exact_certificate"]
        if certificate["type"] == "TASK42A_MOMENT_EXCESS":
            low_counts["moment_gt_8"] += 1
        elif sp.Rational(certificate["quotient"]) > C6_UPPER:
            low_counts["old_rayleigh_gt_c6"] += 1
        elif (int(row["p"]), row["canonical_q_bits"]) in witness_map:
            low_counts["new_witness"] += 1
        else:
            raise AssertionError(f"uncovered low-period orbit {row['orbit_id']}")

    high_counts = {"legal_orbits": 0, "moment_gt_8": 0, "survivors_gt_c6": 0, "target": 0}
    for period in range(17, 25):
        closure = json.loads((RESEARCH / "experiments" / "exact_frontier" / f"p{period}_closure.json").read_text())
        high_counts["legal_orbits"] += int(closure["legal_dihedral_orbits"])
        high_counts["moment_gt_8"] += int(closure["moment_excluded_through_F16"])
        if int(closure["moment_excluded_through_F16"]) + len(closure["survivors"]) != int(closure["legal_dihedral_orbits"]):
            raise AssertionError("high-period closure count mismatch")
        for row in closure["survivors"]:
            certificate_path = RESEARCH.parent / row["certificate_file"]
            certificate = json.loads(certificate_path.read_text())
            if certificate["target_repetition"]:
                high_counts["target"] += 1
            else:
                quotient = sp.Rational(certificate["certificate"]["rayleigh_lower_bound"])
                if quotient <= C6_UPPER:
                    raise AssertionError("high-period survivor certificate does not beat c6")
                high_counts["survivors_gt_c6"] += 1

    checks = {
        "task51_candidate_rows_unchanged": len(csv_rows) == 199,
        "primitive_subeight_non_target_count": len(residual_keys) == 12,
        "weak_old_low_period_count": len(weak_old_keys) == 5,
        "new_witness_count": len(witnesses) == 16,
        "all_new_witnesses_strict": all(int(row["strict_margin_numerator_against_c6_upper"]) > 0 for row in witnesses),
        "low_frontier_complete": sum(low_counts.values()) == len(low["orbits"]),
        "high_frontier_complete": high_counts["moment_gt_8"] + high_counts["survivors_gt_c6"] + high_counts["target"] == high_counts["legal_orbits"],
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "status": "P24_C6_FRONTIER_PROVED",
        "evidence": "COMPUTER_ASSISTED_PROVED",
        "theorem": "The period-eight target is the only primitive phase through period 24 with R(Q)<c6.",
        "scope": "primitive Q phases up to dihedral equivalence and tau negation; repetitions are normalized by primitive period and zone folding",
        "c6_upper": str(C6_UPPER),
        "source_hashes": {
            "task51_csv_sha256": hashlib.sha256(csv_path.read_bytes()).hexdigest(),
            "low_frontier_sha256": hashlib.sha256(low_path.read_bytes()).hexdigest(),
        },
        "residual_subeight_keys": [[period, bits] for period, bits in sorted(residual_keys)],
        "weak_old_keys": [[period, bits] for period, bits in sorted(weak_old_keys)],
        "witnesses": witnesses,
        "low_period_audit": low_counts,
        "high_period_audit": high_counts,
        "proof_boundary": "This is a bounded p<=24 theorem. It makes no all-period extrapolation.",
        "checks": checks,
    }


def run() -> dict[str, Any]:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    payload = build_certificate()
    write_json(OUTPUT / "p24_c6_frontier.json", payload)
    print(json.dumps({"status": payload["status"], "witnesses": len(payload["witnesses"])}, indent=2))
    return payload


if __name__ == "__main__":
    run()

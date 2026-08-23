"""Task 55 exact n=40 certificate and honest 34--46 partial classification."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np

from target_a_task47_common import write_json


REPO = Path(__file__).resolve().parents[2]
RESEARCH = REPO / "research"
OUTPUT = RESEARCH / "proofs" / "task55"
Q40_BITS = "1000100010001000100010001000100010001000"
ALPHA40 = -1
BOUND40 = Fraction(15541, 2000)
THRESHOLD40_LOWER = Fraction(63, 8)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def q_from_bits(bits: str) -> tuple[int, ...]:
    return tuple(1 if bit == "1" else -1 for bit in bits)


def signing_matrix(q: tuple[int, ...], alpha: int) -> np.ndarray:
    n = len(q)
    tau = [1]
    for index in range(n - 1):
        tau.append(tau[-1] * q[index])
    if tau[-1] * q[-1] != 1:
        raise AssertionError("illegal cyclic Q word")
    step1 = [1] * n
    step1[-1] = alpha
    step2 = [
        tau[index] * step1[index] * step1[(index + 1) % n]
        for index in range(n)
    ]
    matrix = np.zeros((n, n), dtype=np.int64)
    for index in range(n):
        for distance, sign in ((1, step1[index]), (2, step2[index])):
            target = (index + distance) % n
            matrix[index, target] = matrix[target, index] = sign
    return matrix


def canonical_code(q: tuple[int, ...]) -> int:
    bits = tuple(value == 1 for value in q)
    candidates = []
    for source in (bits, tuple(reversed(bits))):
        for shift in range(len(q)):
            word = source[shift:] + source[:shift]
            candidates.append(sum(int(value) << index for index, value in enumerate(word)))
    return min(candidates)


def pivot_digest(pivots: list[Fraction]) -> str:
    payload = "\n".join(
        f"{value.numerator}/{value.denominator}" for value in pivots
    ).encode()
    return hashlib.sha256(payload).hexdigest()


def natural_ldl(matrix: np.ndarray) -> list[Fraction]:
    """Return the exact pivots of unpermuted symmetric LDL elimination."""
    n = matrix.shape[0]
    active = [
        {column: Fraction(int(matrix[row, column])) for column in range(n) if matrix[row, column]}
        for row in range(n)
    ]
    pivots = []
    for k in range(n):
        pivot = active[k].get(k, Fraction(0))
        if pivot <= 0:
            return pivots + [pivot]
        pivots.append(pivot)
        neighbors = [row for row in range(k + 1, n) if active[row].get(k, 0)]
        for left in neighbors:
            for right in neighbors:
                if right < left:
                    continue
                value = (
                    active[left].get(right, Fraction(0))
                    - active[left][k] * active[right][k] / pivot
                )
                if value:
                    active[left][right] = active[right][left] = value
                else:
                    active[left].pop(right, None)
                    active[right].pop(left, None)
        for row in neighbors:
            active[row].pop(k, None)
        active[k] = {k: pivot}
    return pivots


def exact_n40_record() -> dict[str, Any]:
    q = q_from_bits(Q40_BITS)
    adjacency = signing_matrix(q, ALPHA40)
    certificate_matrix = (
        BOUND40.numerator * np.eye(40, dtype=np.int64)
        - BOUND40.denominator * (adjacency @ adjacency)
    )
    pivots = natural_ldl(certificate_matrix)
    if len(pivots) != 40 or not all(pivot > 0 for pivot in pivots) or not BOUND40 < THRESHOLD40_LOWER:
        raise AssertionError("n=40 exact certificate failed")
    matrix_bytes = (json.dumps(certificate_matrix.tolist(), separators=(",", ":")) + "\n").encode()
    candidate = RESEARCH / "experiments" / "finite_phase_slips" / "candidates" / "n40_a-1.json"
    legacy = RESEARCH / "experiments" / "finite_phase_slips" / "certificates" / "n40_a-1.json"
    return {
        "n": 40,
        "status": "CERTIFIED_COUNTEREXAMPLE",
        "q_bits": Q40_BITS,
        "canonical_q_code": canonical_code(q),
        "alpha": ALPHA40,
        "gap_word": [4] * 10,
        "rational_upper_on_rho_squared": str(BOUND40),
        "rational_lower_on_conjectured_threshold_squared": str(THRESHOLD40_LOWER),
        "strict_margin": str(THRESHOLD40_LOWER - BOUND40),
        "certificate_statement": "15541 I-2000 A^2 is positive definite",
        "pivot_count": len(pivots),
        "pivot_sha256": pivot_digest(pivots),
        "certificate_matrix_sha256": hashlib.sha256(matrix_bytes).hexdigest(),
        "legacy_candidate_path": str(candidate.relative_to(REPO)),
        "legacy_candidate_sha256": sha256(candidate),
        "legacy_certificate_path": str(legacy.relative_to(REPO)),
        "legacy_certificate_sha256": sha256(legacy),
    }


def build_certificate() -> dict[str, Any]:
    open_rows = [
        (34, 1, "286331153", "0.07072256857384751"),
        (36, -1, "1145311505", "0.05197864446122491"),
        (38, 1, "4567863569", "0.0438583156"),
        (42, 1, "73300775185", "0.015267281028362056"),
        (44, -1, "293199745297", "0.011507122838066"),
        (46, 1, "1169373073681", "0.004990282450388"),
    ]
    orders = []
    for n in (34, 36, 38, 40, 42, 44, 46):
        if n == 40:
            orders.append(exact_n40_record())
            continue
        row = next(row for row in open_rows if row[0] == n)
        orders.append({
            "n": n,
            "status": "OPEN_BOUNDED_SEARCH_ONLY",
            "best_observed_alpha": row[1],
            "best_observed_canonical_q_code": row[2],
            "best_observed_positive_margin": row[3],
            "logical_scope": "No counterexample found in recorded searches; nonexistence is not proved.",
        })
    checks = {
        "all_orders_present": [row["n"] for row in orders] == [34, 36, 38, 40, 42, 44, 46],
        "only_n40_certified": [row["n"] for row in orders if row["status"] == "CERTIFIED_COUNTEREXAMPLE"] == [40],
        "all_other_orders_explicitly_open": all(
            row["status"] == "OPEN_BOUNDED_SEARCH_ONLY"
            for row in orders if row["n"] != 40
        ),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "schema_version": 1,
        "status": "TASK55_ORDERS_34_46_PARTIAL_N40_ONLY",
        "evidence": "COMPUTER_ASSISTED_PROVED_FOR_N40_ONLY",
        "orders": orders,
        "bounded_search_provenance": {
            "beam_canonical_states": 1145182,
            "annealing_canonical_states": 1439618,
            "n46_hamming6_raw_states": 9366819,
            "n46_hamming6_canonical_survivors": 3987,
            "n46_hamming6_raw_sha256": "6a503ede1e06ba9db063c2b88db1f0e08dd03bebc1416b50a73d70cef7a35a0e",
            "n46_hamming6_survivor_sha256": "67b6baeddd9078c44fcc75cfd2a32a6f52d45e6b5979436fce3f425194bcb6b1",
            "local_language": {
                "42": {"labelled_closed_walks": 266231, "legal_words": 133309, "canonical_classes": 1740},
                "44": {"labelled_closed_walks": 2530357, "legal_words": 1265397, "canonical_classes": 14830},
                "46": {"labelled_closed_walks": 4945921, "legal_words": 2473237, "canonical_classes": 27509},
            },
            "evidence": "EXPERIMENTAL_BOUNDED_NEGATIVE",
        },
        "classification": {
            "known_holds": "all even 8<=n<=30",
            "known_first_failure": 32,
            "task55_interval_failures": [40],
            "task55_interval_open": [34, 36, 38, 42, 44, 46],
            "known_eventual_failure": "all even n>=48",
            "all_even_n_ge_32_fail": "NOT_PROVED",
        },
        "checks": checks,
    }


def run() -> dict[str, Any]:
    payload = build_certificate()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    write_json(OUTPUT / "TARGET_A_ORDERS_34_46_CERTIFICATES.json", payload)
    print(json.dumps({"status": payload["status"], "certified": [40]}, indent=2))
    return payload


if __name__ == "__main__":
    run()

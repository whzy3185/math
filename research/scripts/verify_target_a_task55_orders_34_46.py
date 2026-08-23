"""Independent exact checker for the Task 55 partial 34--46 classification."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np


REPO = Path(__file__).resolve().parents[2]
RESEARCH = REPO / "research"
CERTIFICATE = RESEARCH / "proofs" / "task55" / "TARGET_A_ORDERS_34_46_CERTIFICATES.json"


def strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=strict_object)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def independent_canonical_code(q: tuple[int, ...]) -> int:
    bits = tuple(value == 1 for value in q)
    words = []
    for source in (bits, tuple(reversed(bits))):
        for shift in range(len(q)):
            rotated = source[shift:] + source[:shift]
            words.append(sum(int(value) << index for index, value in enumerate(rotated)))
    return min(words)


def adjacency(q: tuple[int, ...], alpha: int) -> np.ndarray:
    n = len(q)
    tau = [1]
    for index in range(n - 1):
        tau.append(tau[-1] * q[index])
    if tau[-1] * q[-1] != 1:
        raise AssertionError("illegal Q")
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


def natural_ldl(matrix: np.ndarray) -> list[Fraction]:
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


def pivot_digest(pivots: list[Fraction]) -> str:
    payload = "\n".join(
        f"{value.numerator}/{value.denominator}" for value in pivots
    ).encode()
    return hashlib.sha256(payload).hexdigest()


def verify(path: Path = CERTIFICATE) -> dict[str, bool]:
    data = load(path)
    orders = data["orders"]
    n40 = next(row for row in orders if row["n"] == 40)
    q = tuple(1 if bit == "1" else -1 for bit in n40["q_bits"])
    matrix = adjacency(q, n40["alpha"])
    bound = Fraction(n40["rational_upper_on_rho_squared"])
    threshold_lower = Fraction(n40["rational_lower_on_conjectured_threshold_squared"])
    certificate_matrix = (
        bound.numerator * np.eye(40, dtype=np.int64)
        - bound.denominator * (matrix @ matrix)
    )
    pivots = natural_ldl(certificate_matrix)
    matrix_bytes = (json.dumps(certificate_matrix.tolist(), separators=(",", ":")) + "\n").encode()
    candidate = REPO / n40["legacy_candidate_path"]
    legacy = REPO / n40["legacy_certificate_path"]
    checks = {
        "status_exact": data["status"] == "TASK55_ORDERS_34_46_PARTIAL_N40_ONLY",
        "orders_exact": [row["n"] for row in orders] == [34, 36, 38, 40, 42, 44, 46],
        "only_n40_certified": [row["n"] for row in orders if row["status"] == "CERTIFIED_COUNTEREXAMPLE"] == [40],
        "all_unresolved_remain_open": all(
            row["status"] == "OPEN_BOUNDED_SEARCH_ONLY"
            and "nonexistence is not proved" in row["logical_scope"]
            for row in orders if row["n"] != 40
        ),
        "all_even_ge32_not_overclaimed": data["classification"]["all_even_n_ge_32_fail"] == "NOT_PROVED",
        "q_canonicalized": independent_canonical_code(q) == n40["canonical_q_code"] == 73300775185,
        "gap_word_bound": n40["gap_word"] == [4] * 10,
        "exact_ldl_positive": len(pivots) == 40 and all(value > 0 for value in pivots),
        "strict_spectral_sandwich": bound == Fraction(15541, 2000)
        and threshold_lower == Fraction(63, 8)
        and bound < threshold_lower
        and n40["strict_margin"] == str(threshold_lower - bound),
        "matrix_hash_rebuilt": hashlib.sha256(matrix_bytes).hexdigest()
        == n40["certificate_matrix_sha256"],
        "pivot_hash_rebuilt": pivot_digest(pivots) == n40["pivot_sha256"],
        "legacy_files_bound": candidate.is_file() and legacy.is_file()
        and sha256(candidate) == n40["legacy_candidate_sha256"]
        and sha256(legacy) == n40["legacy_certificate_sha256"],
        "stored_checks_exact_and_true": set(data["checks"])
        == {"all_orders_present", "only_n40_certified", "all_other_orders_explicitly_open"}
        and all(data["checks"].values()),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return checks


def main() -> None:
    verify()
    print("TARGET_A_TASK55_ORDERS_34_46_VERIFY_PASS")


if __name__ == "__main__":
    main()

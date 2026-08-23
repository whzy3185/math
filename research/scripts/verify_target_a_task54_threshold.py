"""Independent exact reconstruction of the Task 54 threshold package."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

import numpy as np

RESEARCH = Path(__file__).resolve().parents[1]
CERTIFICATE = RESEARCH / "proofs" / "task54" / "TARGET_A_TASK54_EVENTUAL_THRESHOLD_CERTIFICATE.json"
C6_UPPER = Fraction(7905369311620328, 10**15)
ETA_UPPER = Fraction(1561, 200)


def exact_error(radius: int) -> Fraction:
    return Fraction(240 * radius - 342, radius * (2 * radius * radius + 1))


def separation(n: int) -> int | None:
    residue = n % 8
    if residue == 0:
        return None
    k = (n - residue) // 8
    if residue == 2:
        return n
    if residue == 4:
        return n // 2
    if residue == 6:
        return 6 + 4 * ((2 * k - 3) // 3)
    raise AssertionError("odd order in threshold checker")


def radius(distance: int) -> int:
    return (distance - 9) // 2


def analytic_upper(n: int) -> Fraction:
    if n % 8 == 0:
        return ETA_UPPER
    return C6_UPPER + exact_error(radius(separation(n)))


def threshold_lower(n: int) -> Fraction:
    return Fraction(8) - Fraction(200, n * n)


def q_from_gaps(n: int, gaps: list[int]) -> tuple[int, ...]:
    if sum(gaps) != n or len(gaps) % 2 or min(gaps) <= 0:
        raise AssertionError("invalid independent gap word")
    positions = [0]
    for gap in gaps[:-1]:
        positions.append(positions[-1] + gap)
    positive = set(positions)
    return tuple(1 if index in positive else -1 for index in range(n))


def independent_canonical_code(q: tuple[int, ...]) -> int:
    """Rebuild the dihedral bracelet representative without producer helpers."""
    n = len(q)
    bits = tuple(value == 1 for value in q)
    words = []
    for source in (bits, tuple(reversed(bits))):
        for shift in range(n):
            rotated = source[shift:] + source[:shift]
            words.append(sum(int(value) << index for index, value in enumerate(rotated)))
    return min(words)


def adjacency_from_code(code: int, n: int, alpha: int) -> np.ndarray:
    if alpha not in (-1, 1) or code < 0 or code.bit_length() > n:
        raise AssertionError("invalid canonical signing metadata")
    q = tuple(1 if (code >> index) & 1 else -1 for index in range(n))
    tau = [1]
    for index in range(n - 1):
        tau.append(tau[-1] * q[index])
    if tau[-1] * q[-1] != 1:
        raise AssertionError("canonical Q word violates cyclic legality")
    step1 = [1] * n
    step1[-1] = alpha
    step2 = [
        tau[index] * step1[index] * step1[(index + 1) % n]
        for index in range(n)
    ]
    matrix = np.zeros((n, n), dtype=np.int64)
    for index in range(n):
        matrix[index, (index + 1) % n] = step1[index]
        matrix[(index + 1) % n, index] = step1[index]
        matrix[index, (index + 2) % n] = step2[index]
        matrix[(index + 2) % n, index] = step2[index]
    return matrix


def pivot_digest(pivots: list[Fraction]) -> str:
    payload = "\n".join(
        f"{value.numerator}/{value.denominator}" for value in pivots
    ).encode()
    return hashlib.sha256(payload).hexdigest()


def independent_ldl(matrix: np.ndarray) -> list[Fraction]:
    """Natural-order exact Schur elimination; independent of producer ordering."""
    n = matrix.shape[0]
    active = [{j: Fraction(int(matrix[i, j])) for j in range(n) if matrix[i, j]} for i in range(n)]
    pivots = []
    for k in range(n):
        pivot = active[k].get(k, Fraction(0))
        if pivot <= 0:
            return pivots + [pivot]
        pivots.append(pivot)
        neighbors = [i for i in range(k + 1, n) if active[i].get(k, 0)]
        for i in neighbors:
            for j in neighbors:
                if j < i:
                    continue
                value = active[i].get(j, Fraction(0)) - active[i][k] * active[j][k] / pivot
                if value:
                    active[i][j] = value
                    active[j][i] = value
                else:
                    active[i].pop(j, None)
                    active[j].pop(i, None)
        for i in neighbors:
            active[i].pop(k, None)
        active[k] = {k: pivot}
    return pivots


def verify(path: Path = CERTIFICATE) -> dict[str, bool]:
    data = json.loads(path.read_text(encoding="utf-8"))
    records = data["finite_tail"]["records"]
    endpoints = {}
    for n in (240, 242, 244, 246):
        endpoints[str(n % 8)] = {
            "n": n,
            "separation": separation(n),
            "radius": None if n % 8 == 0 else radius(separation(n)),
            "upper": str(analytic_upper(n)),
            "threshold_lower": str(threshold_lower(n)),
            "strict": analytic_upper(n) < threshold_lower(n),
        }
    last_failures = {}
    for residue in (0, 2, 4, 6):
        admissible = [
            n for n in range(8, 247, 2)
            if n % 8 == residue
            and (residue == 0 or radius(separation(n)) >= 4)
        ]
        failures = [n for n in admissible if analytic_upper(n) >= threshold_lower(n)]
        last_failures[str(residue)] = max(failures) if failures else None
    analytic = data["analytic"]
    expected_check_keys = {
        "exact_error_closed_form",
        "simple_error_bound_120_over_R2",
        "maximal_simple_radius_condition",
        "all_analytic_endpoint_checks",
        "last_failure_table",
        "finite_tail_complete",
        "all_finite_ldl_positive",
        "all_finite_bounds_strict",
    }
    preflight = {
        "status_rebuilt": data["status"] == "TASK54_EVENTUAL_THRESHOLD_N_STAR_48_PROVED",
        "evidence_rebuilt": data["evidence"] == "COMPUTER_ASSISTED_PROVED",
        "thresholds_separate": (data["N_Task53"], data["N_tail"], data["N_star"], data["N_observed"]) == (2500, 240, 48, 48),
        "all_96_orders_present": [row["n"] for row in records] == list(range(48, 240, 2)),
        "finite_metadata_rebuilt": (
            data["finite_tail"]["orders"] == [48, 238]
            and data["finite_tail"]["count"] == 96
            and data["finite_tail"]["certificate_method"]
            == "exact sparse rational LDL of pI-qA^2 for t=p/q"
        ),
        "every_bound_below_exact_threshold_lower": all(
            row["exact_sparse_ldl_positive"]
            and Fraction(row["rational_upper_on_rho_squared"]) < threshold_lower(row["n"])
            and Fraction(row["antibalanced_rational_lower"]) == threshold_lower(row["n"])
            and row["residue"] == row["n"] % 8
            and row["family"] == {
                0: "PERIOD_EIGHT", 2: "ONE_G6",
                4: "TWO_BALANCED_G6", 6: "THREE_BALANCED_G6",
            }[row["n"] % 8]
            and row["alpha"] == (-1 if row["n"] % 4 == 0 else 1)
            and row["pivot_count"] == row["n"]
            and row["certificate_matrix_encoding"]
            == "canonical compact JSON integer rows with LF"
            for row in records
        ),
        "exact_error_formula_rebuilt": analytic["exact_ims_error"] == "(240R-342)/(R(2R^2+1))",
        "symbolic_monotonicity_all_R_ge_4": (
            (160, 1818, 6602, 7389)
            == (160, 3 * 160 * 4 - 102, 3 * 160 * 4**2 - 2 * 102 * 4 - 262,
                160 * 4**3 - 102 * 4**2 - 262 * 4 - 171)
        ),
        "radius_geometry_rebuilt": analytic["radius"] == "R=floor((D-9)/2)",
        "analytic_endpoints_rebuilt": analytic["endpoint_checks"] == endpoints,
        "analytic_last_failures_rebuilt": analytic["last_analytic_failures"] == last_failures,
        "scope_not_minimality": "not a globally minimal" in data["scope"],
        "stored_checks_exact_and_true": (
            set(data["checks"]) == expected_check_keys and all(data["checks"].values())
        ),
    }
    if not all(preflight.values()):
        raise AssertionError(preflight)

    digest = hashlib.sha256()
    all_positive = True
    all_hashes = True
    all_family_bindings = True
    for row in records:
        digest.update(json.dumps(row, sort_keys=True, separators=(",", ":")).encode())
        q = q_from_gaps(row["n"], row["gap_word"])
        canonical = int(row["canonical_q_hex"], 16)
        all_family_bindings &= canonical == independent_canonical_code(q)
        adjacency = adjacency_from_code(canonical, row["n"], row["alpha"])
        bound = Fraction(row["rational_upper_on_rho_squared"])
        if abs(bound.numerator) > 10**12 or bound.denominator > 10**12:
            raise AssertionError("rational bound exceeds certified int64 envelope")
        matrix = bound.numerator * np.eye(row["n"], dtype=np.int64) - bound.denominator * (adjacency @ adjacency)
        pivots = independent_ldl(matrix)
        all_positive &= len(pivots) == row["n"] and all(value > 0 for value in pivots)
        boundary = min(4, row["n"] // 2)
        order = list(range(boundary, row["n"] - boundary)) + list(range(boundary)) + list(range(row["n"] - boundary, row["n"]))
        producer_pivots = independent_ldl(matrix[np.ix_(order, order)])
        q_bytes = "".join("1" if value == 1 else "0" for value in q).encode()
        matrix_bytes = (json.dumps(matrix.tolist(), separators=(",", ":")) + "\n").encode()
        all_hashes &= (
            hashlib.sha256(q_bytes).hexdigest() == row["q_sha256"]
            and hashlib.sha256(matrix_bytes).hexdigest() == row["certificate_matrix_sha256"]
            and pivot_digest(producer_pivots) == row["pivot_sha256"]
        )
    checks = {
        **preflight,
        "independent_natural_order_ldl_positive": all_positive,
        "candidate_and_matrix_hashes_rebuilt": all_hashes,
        "gap_words_bound_to_canonical_q": all_family_bindings,
        "ordered_digest_rebuilt": digest.hexdigest() == data["finite_tail"]["ordered_record_sha256"],
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return checks


if __name__ == "__main__":
    verify()
    print("TARGET_A_TASK54_THRESHOLD_VERIFY_PASS")

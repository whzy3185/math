"""Controlled non-theorem exploration of Target A periods 17 through 24."""

from __future__ import annotations

import argparse
import hashlib
import heapq
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any, Iterator

import numpy as np


RESEARCH_DIR = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = RESEARCH_DIR / "experiments" / "target_a_high_period_exploration.json"
LARGE_ORDER_N24_EVIDENCE = (
    RESEARCH_DIR
    / "reproducibility"
    / "target_a_large_order_completeness"
    / "n24.json"
)
TARGET_Q = (1, -1, -1, -1, 1, -1, -1, -1)
ETA = 4 + math.sqrt(10 + 2 * math.sqrt(5))


def _fixed_weight_necklaces(n: int, weight: int) -> Iterator[tuple[int, int]]:
    bits = [0] * (n + 1)

    def generate(position: int, period: int, ones: int) -> Iterator[tuple[int, int]]:
        remaining = n - position + 1
        if ones > weight or ones + remaining < weight:
            return
        if position > n:
            if n % period == 0 and ones == weight:
                code = 0
                for index in range(1, n + 1):
                    code = (code << 1) | bits[index]
                yield code, period
            return
        bits[position] = bits[position - period]
        yield from generate(position + 1, period, ones + bits[position])
        if bits[position - period] == 0:
            bits[position] = 1
            yield from generate(position + 1, position, ones + 1)

    yield from generate(1, 1, 0)


def _rotate(code: int, shift: int, n: int) -> int:
    mask = (1 << n) - 1
    shift %= n
    return code & mask if shift == 0 else ((code << shift) | (code >> (n - shift))) & mask


def _reverse(code: int, n: int) -> int:
    result = 0
    for _ in range(n):
        result = (result << 1) | (code & 1)
        code >>= 1
    return result


def _dihedral_orbit(code: int, p: int) -> set[int]:
    reflected = _reverse(code, p)
    return {_rotate(code, shift, p) for shift in range(p)} | {
        _rotate(reflected, shift, p) for shift in range(p)
    }


def _cycle_lengths(permutation: tuple[int, ...]) -> list[int]:
    visited = [False] * len(permutation)
    lengths = []
    for start in range(len(permutation)):
        if visited[start]:
            continue
        length = 0
        current = start
        while not visited[current]:
            visited[current] = True
            current = permutation[current]
            length += 1
        lengths.append(length)
    return lengths


def independent_burnside_orbit_count(p: int) -> int:
    fixed_sum = 0
    permutations = [
        tuple((index + shift) % p for index in range(p)) for shift in range(p)
    ] + [
        tuple((shift - index) % p for index in range(p)) for shift in range(p)
    ]
    required_parity = p % 2
    for permutation in permutations:
        even, odd = 1, 0
        for length in _cycle_lengths(permutation):
            if length % 2:
                even, odd = even + odd, even + odd
            else:
                even, odd = 2 * even, 2 * odd
        fixed_sum += (even, odd)[required_parity]
    if fixed_sum % (2 * p):
        raise AssertionError("nonintegral independent Burnside count")
    return fixed_sum // (2 * p)


def direct_visited_orbit_records(p: int) -> dict[int, int]:
    visited = bytearray(1 << p)
    records: dict[int, int] = {}
    required_parity = p % 2
    for code in range(1 << p):
        if visited[code] or code.bit_count() % 2 != required_parity:
            continue
        orbit = _dihedral_orbit(code, p)
        for member in orbit:
            visited[member] = 1
        records[min(orbit)] = len(orbit)
    return records


def independent_coverage_audit(
    p: int, primary_records: dict[int, int]
) -> dict[str, Any]:
    burnside_count = independent_burnside_orbit_count(p)
    audit: dict[str, Any] = {
        "burnside_method": "independent permutation-cycle decomposition with parity dynamic programming",
        "burnside_orbits": burnside_count,
        "burnside_matches_primary": burnside_count == len(primary_records),
    }
    if p <= 23:
        direct_records = direct_visited_orbit_records(p)
        audit.update(
            {
                "record_method": "direct full-integer-space visited-orbit partition",
                "record_count": len(direct_records),
                "canonical_record_set_equal": direct_records == primary_records,
            }
        )
    elif p == 24:
        evidence = json.loads(LARGE_ORDER_N24_EVIDENCE.read_text(encoding="utf-8"))
        evidence_checks = evidence.get("checks", {})
        audit.update(
            {
                "record_method": "reused C full-integer-space record audit",
                "record_evidence_path": str(LARGE_ORDER_N24_EVIDENCE.relative_to(RESEARCH_DIR.parent)),
                "record_evidence_sha256": hashlib.sha256(
                    LARGE_ORDER_N24_EVIDENCE.read_bytes()
                ).hexdigest(),
                "record_count": evidence.get(
                    "number_of_canonical_dihedral_representatives"
                ),
                "canonical_record_set_equal": evidence.get("status") == "PASS"
                and all(evidence_checks.values())
                and evidence.get("number_of_canonical_dihedral_representatives")
                == len(primary_records),
            }
        )
    else:
        audit.update(
            {
                "record_method": "not run above period 24",
                "record_count": None,
                "canonical_record_set_equal": False,
            }
        )
    return audit


def orbit_representatives(p: int) -> Iterator[tuple[int, int]]:
    for weight in range(p % 2, p + 1, 2):
        for code, rotation_size in _fixed_weight_necklaces(p, weight):
            reflected = _reverse(code, p)
            reflected_minimum = min(_rotate(reflected, shift, p) for shift in range(rotation_size))
            if code > reflected_minimum:
                continue
            yield code, rotation_size if code == reflected_minimum else 2 * rotation_size


def q_word(code: int, p: int) -> tuple[int, ...]:
    return tuple(1 if (code >> index) & 1 else -1 for index in range(p))


def tau_lift(q: tuple[int, ...]) -> tuple[int, ...]:
    tau = [1]
    for sign in q[:-1]:
        tau.append(tau[-1] * sign)
    if tau[-1] * q[-1] != tau[0]:
        raise ValueError("illegal periodic Q word")
    return tuple(tau)


def primitive_period(word: tuple[int, ...]) -> int:
    n = len(word)
    for period in range(1, n + 1):
        if n % period == 0 and all(word[index] == word[index % period] for index in range(n)):
            return period
    raise AssertionError("word has no primitive period")


def statistics(q: tuple[int, ...]) -> dict[str, Any]:
    p = len(q)
    positions = [index for index, sign in enumerate(q) if sign == 1]
    d = len(positions)
    a = sum(q[index] == q[(index + 1) % p] == 1 for index in range(p))
    b = sum(q[index] == q[(index + 2) % p] == 1 for index in range(p))
    gaps = (
        sorted((positions[(index + 1) % d] - positions[index]) % p for index in range(d))
        if positions
        else []
    )
    return {
        "d": d,
        "a": a,
        "b": b,
        "cyclic_defect_gaps": gaps,
        "F1": 16 * d - 12 * p,
        "F2": 40 * d + 96 * a + 48 * b - 42 * p,
    }


def _candidate_key(code: int, data: dict[str, Any], p: int) -> tuple[Any, ...]:
    gaps = data["cyclic_defect_gaps"]
    spread = max(gaps) - min(gaps) if gaps else p
    return (
        max(data["F1"], 0) + max(data["F2"], 0),
        abs(4 * data["d"] - p),
        data["a"] + data["b"],
        spread,
        code,
    )


def _floquet_matrix(tau: tuple[int, ...], theta: float) -> np.ndarray:
    p = len(tau)
    z = complex(math.cos(theta), math.sin(theta))
    matrix = np.zeros((p, p), dtype=np.complex128)
    for row in range(p):
        transitions = (
            (row - 1, 1),
            (row + 1, 1),
            (row - 2, tau[(row - 2) % p]),
            (row + 2, tau[row]),
        )
        for source, coefficient in transitions:
            cell, column = divmod(source, p)
            matrix[row, column] += coefficient * z**cell
    return matrix


def numerical_radius_squared(q: tuple[int, ...], grid: int) -> tuple[float, int]:
    tau = tau_lift(q)
    best = -math.inf
    best_index = 0
    for index in range(grid):
        theta = 2 * math.pi * index / grid
        eigenvalues = np.linalg.eigvalsh(_floquet_matrix(tau, theta))
        value = float(max(abs(eigenvalues[0]), abs(eigenvalues[-1])) ** 2)
        if value > best:
            best = value
            best_index = index
    return best, best_index


def _canonical_code(q: tuple[int, ...]) -> int:
    p = len(q)
    code = sum((sign == 1) << index for index, sign in enumerate(q))
    reflected = _reverse(code, p)
    return min(
        [_rotate(code, shift, p) for shift in range(p)]
        + [_rotate(reflected, shift, p) for shift in range(p)]
    )


def explore_period(p: int, candidate_limit: int, coarse_grid: int, fine_grid: int) -> dict[str, Any]:
    orbit_count = 0
    represented_words = 0
    f1_positive = 0
    f2_positive_after_f1 = 0
    low_moment_residual = 0
    primitive_tau_distribution: Counter[int] = Counter()
    heap: list[tuple[tuple[Any, ...], int, int, dict[str, Any]]] = []
    repeated_target_code = None
    primary_records: dict[int, int] = {}
    if p % 8 == 0:
        repeated_target_code = _canonical_code(TARGET_Q * (p // 8))

    for code, orbit_size in orbit_representatives(p):
        if code in primary_records:
            raise AssertionError("duplicate primary orbit record")
        primary_records[code] = orbit_size
        q = q_word(code, p)
        data = statistics(q)
        orbit_count += 1
        represented_words += orbit_size
        primitive_tau_distribution[primitive_period(tau_lift(q))] += 1
        if data["F1"] > 0:
            f1_positive += 1
            continue
        if data["F2"] > 0:
            f2_positive_after_f1 += 1
            continue
        low_moment_residual += 1
        key = _candidate_key(code, data, p)
        item = (tuple(-value if isinstance(value, (int, float)) else value for value in key), code, orbit_size, data)
        if len(heap) < candidate_limit:
            heapq.heappush(heap, item)
        elif item > heap[0]:
            heapq.heapreplace(heap, item)

    selected = [(code, orbit_size, data) for _key, code, orbit_size, data in heap]
    if repeated_target_code is not None and all(code != repeated_target_code for code, _, _ in selected):
        q = q_word(repeated_target_code, p)
        orbit = _dihedral_orbit(repeated_target_code, p)
        selected.append((repeated_target_code, len(orbit), statistics(q)))

    coarse_rows = []
    for code, orbit_size, data in selected:
        q = q_word(code, p)
        value, index = numerical_radius_squared(q, coarse_grid)
        coarse_rows.append(
            {
                "canonical_q_code": code,
                "canonical_q_bits": "".join("1" if sign == 1 else "0" for sign in q),
                "orbit_size": orbit_size,
                "statistics": data,
                "primitive_tau_period": primitive_period(tau_lift(q)),
                "coarse_R_squared": value,
                "coarse_grid_index": index,
                "target_repetition": code == repeated_target_code,
            }
        )
    coarse_rows.sort(key=lambda row: row["coarse_R_squared"])
    refined = []
    for row in coarse_rows[: min(16, len(coarse_rows))]:
        q = q_word(row["canonical_q_code"], p)
        value, index = numerical_radius_squared(q, fine_grid)
        refined.append(
            {
                **row,
                "refined_R_squared": value,
                "refined_grid_index": index,
                "comparison_to_eta": value - ETA,
                "evidence_label": "NUMERICAL ONLY",
            }
        )
    refined.sort(key=lambda row: row["refined_R_squared"])
    if repeated_target_code is not None:
        for row in refined:
            if row["target_repetition"]:
                row["exact_zone_folded_R_squared"] = "4+sqrt(10+2*sqrt(5))"
                row["evidence_label"] = "EXACT BY PREVIOUS PERIOD-8 THEOREM AND ZONE FOLDING"

    coverage_audit = independent_coverage_audit(p, primary_records)
    checks = {
        "complete_dihedral_orbit_coverage": represented_words == 1 << (p - 1),
        "independent_burnside_count_matches": coverage_audit[
            "burnside_matches_primary"
        ],
        "independent_canonical_record_set_matches": coverage_audit[
            "canonical_record_set_equal"
        ],
        "exact_partition": f1_positive + f2_positive_after_f1 + low_moment_residual == orbit_count,
        "target_repetition_recognized_when_available": p % 8 != 0
        or any(row["target_repetition"] for row in coarse_rows),
    }
    return {
        "period": p,
        "status": "EXPERIMENTAL_NON_THEOREM",
        "legal_q_words": 1 << (p - 1),
        "dihedral_orbits": orbit_count,
        "represented_q_words": represented_words,
        "exact_low_moment_partition": {
            "F1_positive_implies_R_above_8": f1_positive,
            "F2_positive_after_F1_implies_R_above_8": f2_positive_after_f1,
            "not_excluded_by_F1_or_F2": low_moment_residual,
        },
        "primitive_tau_period_distribution": {
            str(key): primitive_tau_distribution[key] for key in sorted(primitive_tau_distribution)
        },
        "independent_exact_coverage_audit": coverage_audit,
        "numerical_protocol": {
            "selected_residual_candidates": len(coarse_rows),
            "selection": "deterministic rank by moment excess, defect density near p/4, local clustering, gap regularity, then code",
            "coarse_bloch_grid": coarse_grid,
            "refined_candidates": len(refined),
            "refined_bloch_grid": fine_grid,
            "coverage_warning": "numerical ranking is not an exhaustive spectral exclusion of the low-moment residual set",
        },
        "refined_candidates": refined,
        "checks": checks,
    }


def run(periods: list[int], output: Path, candidate_limit: int, coarse_grid: int, fine_grid: int) -> dict[str, Any]:
    results = [explore_period(p, candidate_limit, coarse_grid, fine_grid) for p in periods]
    payload = {
        "schema_version": 1,
        "status": "CONTROLLED_HIGH_PERIOD_EXPLORATION_COMPLETE",
        "theorem_status": "NO_THEOREM_EXTENSION",
        "periods": periods,
        "exact_components": [
            "complete legal-Q dihedral orbit counts",
            "orbit multiplicity sums",
            "independent Burnside counts and record-level orbit audits",
            "primitive tau-period distributions",
            "F1 and F2 integer moment exclusions",
            "period-8 repetitions identified by exact zone folding",
        ],
        "numerical_component": "deterministically selected residual candidates evaluated on stated finite Bloch grids",
        "eta": "4+sqrt(10+2*sqrt(5))",
        "results": results,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    _write_json(output, payload)
    return payload


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--periods", nargs="+", type=int, default=list(range(17, 25)))
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--candidate-limit", type=int, default=256)
    parser.add_argument("--coarse-grid", type=int, default=128)
    parser.add_argument("--fine-grid", type=int, default=2048)
    args = parser.parse_args()
    payload = run(args.periods, args.output, args.candidate_limit, args.coarse_grid, args.fine_grid)
    print(payload["status"])


if __name__ == "__main__":
    main()

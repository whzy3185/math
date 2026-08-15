"""Full audit of the constant-memory Target A bracelet generator."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import struct
import sys
import time
import tracemalloc
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

from target_a_bracelets import enumerate_direct_q_orbits
from target_a_flux_search import enumerate_q_orbits


def fixed_weight_bracelet_counts(n: int) -> dict[int, int]:
    counts = {}
    for weight in range(0, n + 1, 2):
        rotation_fixed = 0
        for shift in range(n):
            cycles = math.gcd(n, shift)
            cycle_length = n // cycles
            if weight % cycle_length == 0:
                rotation_fixed += math.comb(cycles, weight // cycle_length)

        edge_axis_fixed = math.comb(n // 2, weight // 2)
        vertex_axis_fixed = 0
        transposed_pairs = (n - 2) // 2
        for fixed_ones in range(3):
            paired_ones = weight - fixed_ones
            if paired_ones < 0 or paired_ones % 2:
                continue
            selected_pairs = paired_ones // 2
            if selected_pairs <= transposed_pairs:
                vertex_axis_fixed += math.comb(2, fixed_ones) * math.comb(
                    transposed_pairs, selected_pairs
                )

        numerator = rotation_fixed + (n // 2) * (
            edge_axis_fixed + vertex_axis_fixed
        )
        if numerator % (2 * n):
            raise AssertionError("fixed-weight Burnside count is not integral")
        counts[weight] = numerator // (2 * n)
    return counts


def stream_digest(records: Iterable[tuple[int, int, int]]) -> str:
    digest = hashlib.sha256()
    for defect_count, code, orbit_size in records:
        digest.update(struct.pack("<HQQ", defect_count, code, orbit_size))
    return digest.hexdigest()


def direct_records(n: int) -> Iterable[tuple[int, int, int]]:
    for defect_count in range(0, n + 1, 2):
        for code, orbit_size in enumerate_direct_q_orbits(n, defect_count):
            yield defect_count, code, orbit_size


def reference_records(n: int) -> list[tuple[int, int, int]]:
    shells: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
    for code, orbit_size in enumerate_q_orbits(n):
        shells[code.bit_count()].append((code.bit_count(), code, orbit_size))
    return [record for weight in sorted(shells) for record in sorted(shells[weight])]


def audit_reference_equality(n: int) -> dict[str, Any]:
    started = time.time()
    reference = reference_records(n)
    production = list(direct_records(n))
    first_mismatch = None
    if reference != production:
        for index, (old, new) in enumerate(zip(reference, production)):
            if old != new:
                first_mismatch = {"index": index, "reference": old, "production": new}
                break
        if first_mismatch is None:
            first_mismatch = {
                "index": min(len(reference), len(production)),
                "reference_length": len(reference),
                "production_length": len(production),
            }

    shell_counts = defaultdict(int)
    represented_q_vectors = 0
    for weight, _code, orbit_size in production:
        shell_counts[weight] += 1
        represented_q_vectors += orbit_size
    checks = {
        "records_identical": reference == production,
        "canonical_code_defect_orbit_size_identical": reference == production,
        "shell_counts_identical": all(
            sum(1 for record in reference if record[0] == weight) == count
            for weight, count in shell_counts.items()
        ),
        "represented_q_vectors_complete": represented_q_vectors == 1 << (n - 1),
        "burnside_shell_counts_match": dict(shell_counts) == fixed_weight_bracelet_counts(n),
    }
    return {
        "n": n,
        "reference_q_bracelets": len(reference),
        "production_q_bracelets": len(production),
        "spectral_states": 2 * len(production),
        "represented_q_vectors": represented_q_vectors,
        "represented_switching_classes": 4 * represented_q_vectors,
        "shell_counts": {str(key): shell_counts[key] for key in sorted(shell_counts)},
        "reference_sha256": stream_digest(reference),
        "production_sha256": stream_digest(production),
        "first_mismatch": first_mismatch,
        "checks": checks,
        "status": "PASS" if all(checks.values()) else "FAIL",
        "elapsed_seconds": time.time() - started,
    }


def audit_burnside_stream(n: int, *, measure_memory: bool = True) -> dict[str, Any]:
    expected_shells = fixed_weight_bracelet_counts(n)
    observed_shells = defaultdict(int)
    represented_q_vectors = 0
    total = 0
    digest = hashlib.sha256()
    previous_weight = -1
    previous_code = -1
    ordered = True
    even_parity = True
    started = time.time()
    if measure_memory:
        tracemalloc.start()
    for weight, code, orbit_size in direct_records(n):
        if weight != previous_weight:
            if weight <= previous_weight:
                ordered = False
            previous_weight = weight
            previous_code = -1
        if code <= previous_code:
            ordered = False
        previous_code = code
        even_parity = even_parity and code.bit_count() == weight and weight % 2 == 0
        observed_shells[weight] += 1
        represented_q_vectors += orbit_size
        total += 1
        digest.update(struct.pack("<HQQ", weight, code, orbit_size))
    peak_traced_memory = None
    if measure_memory:
        _current, peak_traced_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

    checks = {
        "shell_counts_match_burnside": dict(observed_shells) == expected_shells,
        "total_matches_burnside": total == sum(expected_shells.values()),
        "spectral_state_count_matches": 2 * total == 2 * sum(expected_shells.values()),
        "represented_q_vectors_complete": represented_q_vectors == 1 << (n - 1),
        "represented_switching_classes_complete": 4 * represented_q_vectors
        == 1 << (n + 1),
        "strict_shell_then_code_order": ordered,
        "all_records_have_even_parity": even_parity,
    }
    return {
        "n": n,
        "q_bracelets": total,
        "spectral_states": 2 * total,
        "represented_q_vectors": represented_q_vectors,
        "represented_switching_classes": 4 * represented_q_vectors,
        "shell_counts": {str(key): observed_shells[key] for key in sorted(observed_shells)},
        "burnside_shell_counts": {str(key): expected_shells[key] for key in sorted(expected_shells)},
        "ordered_stream_sha256": digest.hexdigest(),
        "peak_tracemalloc_bytes": peak_traced_memory,
        "checks": checks,
        "status": "PASS" if all(checks.values()) else "FAIL",
        "elapsed_seconds": time.time() - started,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    started = time.time()
    reference_audits = [
        audit_reference_equality(n) for n in (8, 10, 12, 14, 16, 18, 20, 22)
    ]
    burnside_audits = [audit_burnside_stream(n) for n in (24, 26, 28, 30)]
    all_audits = reference_audits + burnside_audits
    payload = {
        "algorithm": (
            "fixed-weight FKM necklace recursion + reflected-orientation minimum; "
            "O(n) working memory"
        ),
        "reference_generator": "visited bytearray over all 2^n Q-codes",
        "production_generator": "target_a_bracelets.enumerate_direct_q_orbits",
        "python": sys.version,
        "platform": platform.platform(),
        "reference_audits_n8_22": reference_audits,
        "burnside_audits_n24_30": burnside_audits,
        "status": "PASS" if all(item["status"] == "PASS" for item in all_audits) else "DIRECT_GENERATOR_AUDIT_FAIL",
        "elapsed_seconds": time.time() - started,
    }
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    raise SystemExit(0 if payload["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()

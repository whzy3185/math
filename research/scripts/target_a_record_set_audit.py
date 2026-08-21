"""Record-level equality audit for the two Target A orbit generators."""

from __future__ import annotations

import argparse
import hashlib
import json
import mmap
import os
import platform
import shutil
import struct
import subprocess
import tempfile
import time
from collections import Counter
from pathlib import Path
from typing import Any

from target_a_bracelets import enumerate_direct_q_orbits


SCRIPT_DIR = Path(__file__).resolve().parent
C_SOURCE = SCRIPT_DIR / "target_a_independent_orbit_scan.c"
PRIMARY_SOURCE = SCRIPT_DIR / "target_a_bracelets.py"
DEFAULT_OUTPUT_DIR = (
    SCRIPT_DIR.parent / "reproducibility" / "target_a_large_order_completeness"
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _build_checker(binary: Path) -> dict[str, str]:
    compiler = shutil.which("cc")
    if compiler is None:
        raise RuntimeError("a C11 compiler named 'cc' is required")
    command = [compiler, "-O3", "-std=c11", "-Wall", "-Wextra", str(C_SOURCE), "-o", str(binary)]
    subprocess.run(command, check=True)
    version = subprocess.run(
        [compiler, "--version"], check=True, text=True, capture_output=True
    ).stdout.splitlines()[0]
    return {"compiler": compiler, "compiler_version": version, "source_sha256": _sha256(C_SOURCE)}


def _primary_table(n: int, path: Path) -> dict[str, Any]:
    universe = 1 << n
    fd = os.open(path, os.O_RDWR | os.O_CREAT | os.O_TRUNC, 0o600)
    try:
        os.ftruncate(fd, universe)
        table = mmap.mmap(fd, universe, access=mmap.ACCESS_WRITE)
    finally:
        os.close(fd)

    started = time.time()
    representative_count = 0
    represented_q_vectors = 0
    duplicate_records = 0
    parity_failures = 0
    defect_histogram: Counter[int] = Counter()
    orbit_histogram: Counter[int] = Counter()
    ordered_digest = hashlib.sha256()
    try:
        for defects in range(0, n + 1, 2):
            previous = -1
            for code, orbit_size in enumerate_direct_q_orbits(n, defects):
                if code <= previous:
                    raise AssertionError("FKM stream is not strictly ordered within its shell")
                previous = code
                if table[code] != 0:
                    duplicate_records += 1
                if code.bit_count() != defects or defects % 2:
                    parity_failures += 1
                if not 1 <= orbit_size <= 2 * n:
                    raise AssertionError("invalid orbit size")
                table[code] = orbit_size
                representative_count += 1
                represented_q_vectors += orbit_size
                defect_histogram[defects] += 1
                orbit_histogram[orbit_size] += 1
                ordered_digest.update(struct.pack("<HQQ", defects, code, orbit_size))
        table.flush()
    finally:
        table.close()

    return {
        "algorithm": "fixed-weight FKM necklace recursion with reflection filtering",
        "enumeration_order": "even defect shell, then increasing canonical integer",
        "representatives": representative_count,
        "represented_q_vectors": represented_q_vectors,
        "defect_count_histogram": {str(k): defect_histogram[k] for k in sorted(defect_histogram)},
        "orbit_size_histogram": {str(k): orbit_histogram[k] for k in sorted(orbit_histogram)},
        "ordered_stream_sha256": ordered_digest.hexdigest(),
        "duplicate_records": duplicate_records,
        "parity_failures": parity_failures,
        "elapsed_seconds": time.time() - started,
    }


def audit_order(n: int, work_dir: Path, binary: Path) -> dict[str, Any]:
    if n < 8 or n > 30 or n % 2:
        raise ValueError("n must be an even integer in [8,30]")
    started = time.time()
    table_path = work_dir / f"n{n}_primary_orbit_size.bin"
    primary = _primary_table(n, table_path)
    independent_started = time.time()
    process = subprocess.run(
        [str(binary), str(n), str(table_path)],
        check=False,
        text=True,
        capture_output=True,
    )
    try:
        independent = json.loads(process.stdout)
    except json.JSONDecodeError as error:
        raise RuntimeError(
            f"independent scanner emitted invalid JSON (exit {process.returncode}): {process.stderr}"
        ) from error
    independent["elapsed_seconds"] = time.time() - independent_started
    independent["stderr"] = process.stderr

    expected_q_vectors = 1 << (n - 1)
    checks = {
        "independent_scanner_passed": process.returncode == 0 and independent["status"] == "PASS",
        "primary_has_no_duplicates": primary["duplicate_records"] == 0,
        "primary_parity_is_legal": primary["parity_failures"] == 0,
        "all_primary_records_consumed": independent["consumed_primary_records"] == primary["representatives"],
        "no_independent_record_missing_from_primary": independent["missing_primary_records"] == 0,
        "canonical_representative_counts_equal": independent["independent_representatives"] == primary["representatives"],
        "record_orbit_sizes_equal": independent["orbit_size_mismatches"] == 0,
        "canonical_words_verified_by_full_scan": independent["canonicality_failures"] == 0,
        "defect_histograms_equal": independent["defect_count_histogram"] == primary["defect_count_histogram"],
        "orbit_histograms_equal": independent["orbit_size_histogram"] == primary["orbit_size_histogram"],
        "legal_q_word_count_complete": independent["legal_q_words"] == expected_q_vectors,
        "primary_multiplicity_complete": primary["represented_q_vectors"] == expected_q_vectors,
        "independent_multiplicity_complete": independent["represented_q_vectors"] == expected_q_vectors,
    }
    result = {
        "schema_version": 1,
        "order": n,
        "state_representation": "even-parity binary Q word; bit 1 means Q_i=+1",
        "quotient_representation": "one representative per dihedral orbit, with both alpha=-1,+1 retained",
        "comparison_method": "ordering-independent exact set consumption through a disk-mapped orbit-size table",
        "hash_role": "reproducibility only; PASS is decided by exact record consumption, not digest equality",
        "primary": primary,
        "independent": independent,
        "number_of_legal_q_words": expected_q_vectors,
        "number_of_canonical_dihedral_representatives": primary["representatives"],
        "canonical_spectral_states": 2 * primary["representatives"],
        "holonomy_coverage": [-1, 1],
        "sum_of_represented_q_vectors": primary["represented_q_vectors"],
        "sum_of_represented_switching_classes": 4 * primary["represented_q_vectors"],
        "expected_switching_classes": 1 << (n + 1),
        "terminal_traversal_check": {
            "independent_integer_range_scanned": [0, (1 << n) - 1],
            "every_even_parity_word_visited": independent["legal_q_words"] == expected_q_vectors,
            "remaining_primary_records": primary["representatives"] - independent["consumed_primary_records"],
        },
        "checks": checks,
        "record_level_set_equality": all(checks.values()),
        "status": "PASS" if all(checks.values()) else "FAIL",
        "elapsed_seconds": time.time() - started,
    }
    table_path.unlink(missing_ok=True)
    return result


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def run_audit(orders: list[int], output_dir: Path, work_dir: Path) -> dict[str, Any]:
    binary = work_dir / "target_a_independent_orbit_scan"
    build = _build_checker(binary)
    results = []
    for n in orders:
        result = audit_order(n, work_dir, binary)
        detail_path = output_dir / f"n{n}.json"
        _write_json(detail_path, result)
        results.append((result, detail_path))
    repository_head = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=SCRIPT_DIR.parent.parent,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    summary = {
        "schema_version": 1,
        "purpose": "independent record-level equality and completeness audit for large Target A orbit sets",
        "primary_route": "Python fixed-weight FKM necklace recursion",
        "independent_route": "C full integer-space scan with direct dihedral orbit construction",
        "independence": {
            "canonicalization_code_shared": False,
            "canonicalization_traversal_shared": False,
            "group_action_specification_shared": True,
            "binary_q_semantics_shared": True,
            "traversal_order_shared": False,
            "shell_decomposition_shared": False,
            "data_structures_shared": False,
            "implementation_language_shared": False,
        },
        "build": build,
        "execution_provenance": {
            "repository_head": repository_head,
            "command": "python research/scripts/target_a_record_set_audit.py --n "
            + " ".join(str(n) for n in orders),
            "driver_sha256": _sha256(Path(__file__)),
            "primary_generator_sha256": _sha256(PRIMARY_SOURCE),
            "note": "source and detail hashes, rather than worktree cleanliness, bind this recorded run",
        },
        "python": platform.python_version(),
        "platform": platform.platform(),
        "orders": orders,
        "results": [
            {
                "order": item["order"],
                "status": item["status"],
                "record_level_set_equality": item["record_level_set_equality"],
                "canonical_representatives": item["number_of_canonical_dihedral_representatives"],
                "canonical_spectral_states": item["canonical_spectral_states"],
                "represented_switching_classes": item["sum_of_represented_switching_classes"],
                "elapsed_seconds": item["elapsed_seconds"],
                "file": path.name,
                "file_sha256": _sha256(path),
            }
            for item, path in results
        ],
        "status": "PASS" if all(item["status"] == "PASS" for item, _path in results) else "FAIL",
    }
    _write_json(output_dir / "summary.json", summary)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, nargs="+", default=[24, 26, 28, 30])
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--work-dir", type=Path)
    args = parser.parse_args()

    if args.work_dir:
        args.work_dir.mkdir(parents=True, exist_ok=True)
        summary = run_audit(args.n, args.output_dir, args.work_dir)
    else:
        with tempfile.TemporaryDirectory(prefix="target-a-record-set-") as temporary:
            summary = run_audit(args.n, args.output_dir, Path(temporary))
    print(json.dumps(summary, indent=2))
    raise SystemExit(0 if summary["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()

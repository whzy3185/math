"""Production exhaustive minimality search for Target A.

The reference flux search intentionally retains its visited-array orbit
enumerator.  This driver streams the audited direct bracelet generator,
checks every reconstructed state, and writes resumable immutable checkpoint
chunks without materializing a shell or the complete quotient space.
"""

from __future__ import annotations

import argparse
import hashlib
import heapq
import json
import math
import os
import platform
import resource
import shlex
import struct
import subprocess
import sys
import time
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable, Iterator

import numpy as np
import sympy as sp

from target_a_bracelets import enumerate_direct_q_orbits
from target_a_flux_search import (
    exact_even_traces,
    q_code_from_signing,
    q_vector,
    signing_from_q,
    triangle_flux_from_q,
)
from target_a_reproduce import exact_optimizer_check, numpy_matrix
from target_a_verifier import (
    Signing,
    is_strict_counterexample,
    rational_interval,
    signed_adjacency,
    threshold_squared,
)


SCHEMA_VERSION = 1
GENERATOR_NAME = "target_a_bracelets.enumerate_direct_q_orbits"
ZERO_SHA256 = "0" * 64
N24_SHELL_COUNTS = {
    0: 1,
    2: 12,
    4: 256,
    6: 2920,
    8: 15581,
    10: 41272,
    12: 56822,
    14: 41272,
    16: 15581,
    18: 2920,
    20: 256,
    22: 12,
    24: 1,
}
N26_SHELL_COUNTS = {
    0: 1,
    2: 13,
    4: 328,
    6: 4576,
    8: 30415,
    10: 102817,
    12: 186616,
    14: 186616,
    16: 102817,
    18: 30415,
    20: 4576,
    22: 328,
    24: 13,
    26: 1,
}
N28_SHELL_COUNTS = {
    0: 1,
    2: 14,
    4: 413,
    6: 6916,
    8: 56021,
    10: 235378,
    12: 544802,
    14: 718146,
    16: 544802,
    18: 235378,
    20: 56021,
    22: 6916,
    24: 413,
    26: 14,
    28: 1,
}
N30_SHELL_COUNTS = {
    0: 1,
    2: 15,
    4: 511,
    6: 10133,
    8: 98254,
    10: 502303,
    12: 1444147,
    14: 2427036,
    16: 2427036,
    18: 1444147,
    20: 502303,
    22: 98254,
    24: 10133,
    26: 511,
    28: 15,
    30: 1,
}


class SearchAbort(RuntimeError):
    def __init__(self, status: str, message: str):
        super().__init__(message)
        self.status = status


def _canonical_json(payload: Any) -> bytes:
    return json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _durable_json_write(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    data = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    with temporary.open("w", encoding="utf-8") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, path)
    directory_fd = os.open(path.parent, os.O_RDONLY)
    try:
        os.fsync(directory_fd)
    finally:
        os.close(directory_fd)


def _git_value(*args: str) -> str:
    return subprocess.check_output(
        ("git", *args), text=True, stderr=subprocess.DEVNULL
    ).strip()


def _peak_rss_bytes() -> int:
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == "darwin":
        return int(peak)
    return int(peak) * 1024


def fixed_weight_bracelet_counts(n: int) -> dict[int, int]:
    """Independent fixed-weight Burnside targets for even n."""
    if n < 2 or n % 2:
        raise ValueError("n must be positive and even")
    counts: dict[int, int] = {}
    for weight in range(0, n + 1, 2):
        rotation_fixed = 0
        for shift in range(n):
            cycles = math.gcd(n, shift)
            cycle_length = n // cycles
            if weight % cycle_length == 0:
                rotation_fixed += math.comb(cycles, weight // cycle_length)

        edge_axis_fixed = math.comb(n // 2, weight // 2)
        vertex_axis_fixed = 0
        paired_positions = (n - 2) // 2
        for fixed_ones in range(3):
            remainder = weight - fixed_ones
            if remainder < 0 or remainder % 2:
                continue
            pairs = remainder // 2
            if pairs <= paired_positions:
                vertex_axis_fixed += math.comb(2, fixed_ones) * math.comb(
                    paired_positions, pairs
                )
        numerator = rotation_fixed + (n // 2) * (
            edge_axis_fixed + vertex_axis_fixed
        )
        if numerator % (2 * n):
            raise AssertionError("nonintegral Burnside shell count")
        counts[weight] = numerator // (2 * n)
    return counts


def expected_search_space(n: int) -> dict[str, Any]:
    shells = fixed_weight_bracelet_counts(n)
    if n == 24 and shells != N24_SHELL_COUNTS:
        raise SearchAbort("SEARCH_SPACE_MISMATCH", "n=24 Burnside constants disagree")
    if n == 26 and shells != N26_SHELL_COUNTS:
        raise SearchAbort("SEARCH_SPACE_MISMATCH", "n=26 Burnside constants disagree")
    if n == 28 and shells != N28_SHELL_COUNTS:
        raise SearchAbort("SEARCH_SPACE_MISMATCH", "n=28 Burnside constants disagree")
    if n == 30 and shells != N30_SHELL_COUNTS:
        raise SearchAbort("SEARCH_SPACE_MISMATCH", "n=30 Burnside constants disagree")
    q_bracelets = sum(shells.values())
    return {
        "shell_counts": shells,
        "q_bracelets": q_bracelets,
        "spectral_states": 2 * q_bracelets,
        "q_vectors": 1 << (n - 1),
        "switching_classes": 1 << (n + 1),
    }


def validate_search_space(n: int) -> dict[str, Any]:
    """Count the direct stream before any spectral matrix is built."""
    expected = expected_search_space(n)
    observed_shells: dict[int, int] = {}
    represented_q_vectors = 0
    previous_weight = -1
    previous_code = -1
    for weight in range(0, n + 1, 2):
        count = 0
        previous_code = -1
        for code, orbit_size in enumerate_direct_q_orbits(n, weight):
            if weight <= previous_weight or code <= previous_code:
                raise SearchAbort(
                    "SEARCH_SPACE_MISMATCH", "direct generator order mismatch"
                )
            previous_code = code
            count += 1
            represented_q_vectors += orbit_size
        previous_weight = weight
        observed_shells[weight] = count
    q_bracelets = sum(observed_shells.values())
    checks = {
        "shell_counts": observed_shells == expected["shell_counts"],
        "q_bracelets": q_bracelets == expected["q_bracelets"],
        "spectral_states": 2 * q_bracelets == expected["spectral_states"],
        "represented_q_vectors": represented_q_vectors == expected["q_vectors"],
        "represented_switching_classes": 4 * represented_q_vectors
        == expected["switching_classes"],
    }
    if not all(checks.values()):
        raise SearchAbort(
            "SEARCH_SPACE_MISMATCH", f"search-space checks failed: {checks}"
        )
    return {
        **expected,
        "observed_shell_counts": observed_shells,
        "represented_q_vectors": represented_q_vectors,
        "checks": checks,
    }


def iter_spectral_states(n: int) -> Iterator[tuple[int, int, int, int]]:
    for defect_count in range(0, n + 1, 2):
        for code, orbit_size in enumerate_direct_q_orbits(n, defect_count):
            for alpha in (-1, 1):
                yield defect_count, code, orbit_size, alpha


def _input_bytes(state: tuple[int, int, int, int]) -> bytes:
    defect_count, code, orbit_size, alpha = state
    return struct.pack("<HQQb", defect_count, code, orbit_size, alpha)


def _integer_rayleigh_certificate(
    matrix: np.ndarray, eigenvector: np.ndarray, scale: int = 10**9
) -> tuple[Fraction, list[int]]:
    vector = np.rint(eigenvector * scale).astype(np.int64)
    if not np.any(vector):
        vector[int(np.argmax(np.abs(eigenvector)))] = 1
    image = matrix @ vector
    numerator = sum(int(value) ** 2 for value in image)
    denominator = sum(int(value) ** 2 for value in vector)
    return Fraction(numerator, denominator), [int(value) for value in vector]


def _top_key(item: dict[str, Any]) -> tuple[float, int, int]:
    return (
        float(item["numeric_rho_preview"]),
        int(item["canonical_q_code"]),
        int(item["alpha"]),
    )


def _push_top(
    heap: list[tuple[float, int, int, dict[str, Any]]],
    item: dict[str, Any],
    limit: int = 100,
) -> None:
    rho, code, alpha = _top_key(item)
    heapq.heappush(heap, (-rho, -code, -alpha, item))
    if len(heap) > limit:
        heapq.heappop(heap)


def _sorted_top(
    heap: Iterable[tuple[float, int, int, dict[str, Any]]],
) -> list[dict[str, Any]]:
    return sorted((entry[3] for entry in heap), key=_top_key)


def _basic_near_minimizer(
    n: int,
    defect_count: int,
    code: int,
    orbit_size: int,
    alpha: int,
    rho: float,
    threshold_rho: float,
    bound: Fraction,
    period4_distance: int,
) -> dict[str, Any]:
    return {
        "canonical_q_code": code,
        "alpha": alpha,
        "defect_count": defect_count,
        "dihedral_orbit_size": orbit_size,
        "numeric_rho_preview": rho,
        "numeric_gap_preview": rho - threshold_rho,
        "distance_to_period4_Q_pattern": period4_distance,
        "exact_Rayleigh_certificate": {
            "numerator": bound.numerator,
            "denominator": bound.denominator,
            "value": str(bound),
        },
    }


def cyclic_gaps(positions: list[int], n: int) -> list[int]:
    if not positions:
        return []
    return [
        (positions[(index + 1) % len(positions)] - positions[index]) % n
        for index in range(len(positions))
    ]


@lru_cache(maxsize=None)
def _period4_pattern_codes(n: int) -> tuple[int, ...]:
    """Return the distinct dihedral images of the length-n (+---)... code."""
    mask = (1 << n) - 1
    base = period4_reference_code(n)
    reflected = 0
    for index in range(n):
        if (base >> index) & 1:
            reflected |= 1 << (n - 1 - index)

    def rotate(code: int, shift: int) -> int:
        if shift == 0:
            return code
        return ((code << shift) | (code >> (n - shift))) & mask

    return tuple(
        sorted(
            {rotate(base, shift) for shift in range(n)}
            | {rotate(reflected, shift) for shift in range(n)}
        )
    )


def period4_reference_code(n: int) -> int:
    """The exact length-n truncation of the infinite (+---) pattern."""
    return sum(1 << index for index in range(0, n, 4))


def distance_to_period4_q_code(code: int, n: int) -> int:
    return min((code ^ pattern).bit_count() for pattern in _period4_pattern_codes(n))


def distance_to_period4_q_pattern(q: tuple[int, ...]) -> int:
    """Minimum Hamming distance to (+---)... under D_n."""
    code = sum(1 << index for index, value in enumerate(q) if value == 1)
    return distance_to_period4_q_code(code, len(q))


def validate_period4_diagnostic(n: int, code: int, distance: int) -> None:
    pattern_weight = period4_reference_code(n).bit_count()
    expected_distance_parity = (code.bit_count() + pattern_weight) % 2
    if distance % 2 != expected_distance_parity:
        raise SearchAbort(
            "DIAGNOSTIC_PARITY_ERROR",
            (
                f"n={n} period-4 distance parity mismatch: "
                f"Q weight {code.bit_count()}, pattern weight {pattern_weight}, "
                f"distance {distance}"
            ),
        )


def _update_best_by_distance(
    best: dict[int, dict[str, Any]], item: dict[str, Any]
) -> None:
    distance = int(item["distance_to_period4_Q_pattern"])
    if distance not in best or _top_key(item) < _top_key(best[distance]):
        best[distance] = item


def _expand_near_minimizer(n: int, item: dict[str, Any]) -> dict[str, Any]:
    code = int(item["canonical_q_code"])
    alpha = int(item["alpha"])
    q = q_vector(code, n)
    tau = triangle_flux_from_q(code, n)
    matrix = numpy_matrix(signing_from_q(code, n, alpha))
    positions = [index for index, value in enumerate(q) if value == 1]
    return {
        **item,
        "canonical_Q": list(q),
        "tau": list(tau),
        "defect_positions": positions,
        "cyclic_defect_gaps": cyclic_gaps(positions, n),
        "distance_to_period4_Q_pattern": item.get(
            "distance_to_period4_Q_pattern", distance_to_period4_q_pattern(q)
        ),
        **exact_even_traces(matrix),
    }


def _checkpoint_content_hash(payload: dict[str, Any]) -> str:
    core = dict(payload)
    core.pop("content_sha256", None)
    return hashlib.sha256(_canonical_json(core)).hexdigest()


def _chain_hash(
    previous: str,
    input_digest: str,
    certificate_digest: str,
    chunk_index: int,
    completed_states: int,
) -> str:
    return hashlib.sha256(
        _canonical_json(
            {
                "previous_chain_sha256": previous,
                "ordered_input_sha256": input_digest,
                "ordered_certificate_sha256": certificate_digest,
                "chunk_index": chunk_index,
                "completed_states": completed_states,
            }
        )
    ).hexdigest()


def _chunk_paths(checkpoint_dir: Path) -> list[Path]:
    return sorted(checkpoint_dir.glob("chunk_*.json"))


def _write_manifest(
    checkpoint_dir: Path,
    n: int,
    git_commit: str,
    chunks: list[dict[str, Any]],
    status: str,
) -> tuple[dict[str, Any], str]:
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "n": n,
        "git_commit": git_commit,
        "baseline_git_commit": git_commit,
        "status": status,
        "chunks": [
            {
                "filename": f"chunk_{chunk['chunk_index']:06d}.json",
                "content_sha256": chunk["content_sha256"],
                "chain_sha256": chunk["chain_sha256"],
            }
            for chunk in chunks
        ],
    }
    path = checkpoint_dir / "manifest.json"
    _durable_json_write(path, manifest)
    return manifest, _sha256_file(path)


def _load_and_validate_chunks(
    checkpoint_dir: Path,
    n: int,
    git_commit: str,
    expected_shells: dict[int, int],
) -> list[dict[str, Any]]:
    chunks = []
    previous_chain = ZERO_SHA256
    for expected_index, path in enumerate(_chunk_paths(checkpoint_dir)):
        try:
            chunk = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise SearchAbort(
                "CHECKPOINT_VALIDATION_FAIL", f"cannot read {path}: {error}"
            ) from error
        checks = {
            "schema": chunk.get("schema_version") == SCHEMA_VERSION,
            "git_commit": chunk.get("git_commit") == git_commit,
            "baseline_git_commit": chunk.get(
                "baseline_git_commit", chunk.get("git_commit")
            )
            == git_commit,
            "n": chunk.get("n") == n,
            "chunk_index": chunk.get("chunk_index") == expected_index,
            "known_shell": chunk.get("defect_count") in expected_shells,
            "shell_target": chunk.get("expected_shell_q_bracelets")
            == expected_shells.get(chunk.get("defect_count")),
            "previous_chain": chunk.get("previous_chain_sha256") == previous_chain,
            "content_hash": chunk.get("content_sha256")
            == _checkpoint_content_hash(chunk),
        }
        expected_chain = _chain_hash(
            previous_chain,
            str(chunk.get("ordered_input_sha256")),
            str(chunk.get("ordered_certificate_sha256")),
            expected_index,
            int(chunk.get("completed_states", -1)),
        )
        checks["chain_hash"] = chunk.get("chain_sha256") == expected_chain
        if not all(checks.values()):
            raise SearchAbort(
                "CHECKPOINT_VALIDATION_FAIL",
                f"checkpoint {path.name} failed checks: {checks}",
            )
        previous_chain = chunk["chain_sha256"]
        chunks.append(chunk)

    manifest_path = checkpoint_dir / "manifest.json"
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise SearchAbort(
                "CHECKPOINT_VALIDATION_FAIL", f"invalid manifest: {error}"
            ) from error
        if (
            manifest.get("schema_version") != SCHEMA_VERSION
            or manifest.get("n") != n
            or manifest.get("git_commit", manifest.get("baseline_git_commit"))
            != git_commit
            or manifest.get("baseline_git_commit", manifest.get("git_commit"))
            != git_commit
        ):
            raise SearchAbort("CHECKPOINT_VALIDATION_FAIL", "manifest metadata mismatch")
        entries = manifest.get("chunks", [])
        if len(entries) > len(chunks):
            raise SearchAbort("CHECKPOINT_VALIDATION_FAIL", "manifest has missing chunks")
        for entry, chunk in zip(entries, chunks):
            if (
                entry.get("content_sha256") != chunk["content_sha256"]
                or entry.get("chain_sha256") != chunk["chain_sha256"]
            ):
                raise SearchAbort(
                    "CHECKPOINT_VALIDATION_FAIL", "manifest chunk digest mismatch"
                )
    return chunks


def _replay_checkpoint_inputs(
    n: int,
    chunks: list[dict[str, Any]],
) -> tuple[Iterator[tuple[int, int, int, int]], hashlib._Hash]:
    states = iter_spectral_states(n)
    global_input = hashlib.sha256()
    for chunk in chunks:
        digest = hashlib.sha256()
        first = None
        last = None
        for _ in range(chunk["completed_states"]):
            try:
                state = next(states)
            except StopIteration as error:
                raise SearchAbort(
                    "CHECKPOINT_VALIDATION_FAIL", "checkpoint passes end of stream"
                ) from error
            if first is None:
                first = state
            last = state
            encoded = _input_bytes(state)
            digest.update(encoded)
            global_input.update(encoded)
        checks = {
            "input_digest": digest.hexdigest() == chunk["ordered_input_sha256"],
            "first_q": first is not None and first[1] == chunk["first_canonical_q"],
            "first_alpha": first is not None and first[3] == chunk["first_alpha"],
            "last_q": last is not None and last[1] == chunk["last_canonical_q"],
            "last_alpha": last is not None and last[3] == chunk["last_alpha"],
            "defect_count": first is not None
            and last is not None
            and first[0] == last[0] == chunk["defect_count"],
        }
        if not all(checks.values()):
            raise SearchAbort(
                "CHECKPOINT_VALIDATION_FAIL",
                f"checkpoint cursor failed checks: {checks}",
            )
    return states, global_input


def determine_completion_status(
    n: int,
    expected: dict[str, Any],
    completed_q_bracelets: int,
    completed_spectral_states: int,
    represented_q_vectors: int,
    shell_counts_completed: dict[int, int],
    rayleigh_certified: int,
    exact_fallbacks: int,
    counterexamples: list[dict[str, Any]],
    optimizer_exact_check: dict[str, Any] | None,
) -> str:
    if counterexamples:
        return f"COUNTEREXAMPLE_FOUND_AT_N{n}"
    complete = (
        completed_q_bracelets == expected["q_bracelets"]
        and completed_spectral_states == expected["spectral_states"]
        and represented_q_vectors == expected["q_vectors"]
        and 4 * represented_q_vectors == expected["switching_classes"]
        and shell_counts_completed == expected["shell_counts"]
        and rayleigh_certified + exact_fallbacks
        == expected["spectral_states"] - 1
        and optimizer_exact_check is not None
    )
    return f"VERIFIED_NO_COUNTEREXAMPLE_AT_N{n}" if complete else "INCOMPLETE"


def _counterexample_record(
    n: int,
    defect_count: int,
    code: int,
    orbit_size: int,
    alpha: int,
    signing: Signing,
    matrix: np.ndarray,
    vector: list[int],
    bound: Fraction,
    detail: dict[str, Any],
    threshold_lower: Fraction,
    threshold_upper: Fraction,
) -> dict[str, Any]:
    exact_matrix = signed_adjacency(signing)
    return {
        "method": (
            "direct (Q,alpha)/D_n stream + one dense eigh + exact rational "
            "Rayleigh certificates + exact Sylvester fallback"
        ),
        "n": n,
        "defect_count": defect_count,
        "canonical_q_code": code,
        "canonical_Q": list(q_vector(code, n)),
        "tau": list(triangle_flux_from_q(code, n)),
        "alpha": alpha,
        "dihedral_orbit_size": orbit_size,
        "signing": {"step1": list(signing.step1), "step2": list(signing.step2)},
        "integer_adjacency_matrix": matrix.tolist(),
        "integer_adjacency_square": (matrix @ matrix).tolist(),
        "characteristic_polynomial": str(exact_matrix.charpoly().as_expr()),
        "characteristic_polynomial_A2": str(
            (exact_matrix * exact_matrix).charpoly().as_expr()
        ),
        "threshold_squared_interval": [
            str(threshold_lower),
            str(threshold_upper),
        ],
        "integer_Rayleigh_vector": vector,
        "Rayleigh_certificate": str(bound),
        "exact_certificate": detail,
    }


def run_minimality_search(
    n: int,
    checkpoint_dir: Path | None = None,
    *,
    resume: bool = False,
    chunk_size: int = 20_000,
    stop_after_states: int | None = None,
    git_commit_override: str | None = None,
) -> dict[str, Any]:
    if n < 8 or n % 2:
        raise ValueError("n must be even and at least 8")
    if chunk_size < 2:
        raise ValueError("chunk_size must be at least 2")
    started = time.time()
    expected_audit = validate_search_space(n)
    expected = expected_search_space(n)
    git_commit = git_commit_override or _git_value("rev-parse", "HEAD")
    try:
        branch = _git_value("branch", "--show-current")
    except subprocess.CalledProcessError:
        branch = "UNKNOWN"

    checkpoint_dir = checkpoint_dir or Path(f"research/logs/checkpoints/n{n}")
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    existing_paths = _chunk_paths(checkpoint_dir)
    if existing_paths and not resume:
        raise SearchAbort(
            "CHECKPOINT_VALIDATION_FAIL",
            "checkpoint chunks already exist; use --resume or a clean directory",
        )
    chunks = (
        _load_and_validate_chunks(
            checkpoint_dir, n, git_commit, expected["shell_counts"]
        )
        if resume
        else []
    )
    states, global_input_digest = _replay_checkpoint_inputs(n, chunks)

    completed_states = sum(chunk["completed_states"] for chunk in chunks)
    completed_q_bracelets = sum(chunk["completed_q_bracelets"] for chunk in chunks)
    represented_q_vectors = sum(chunk["represented_q_vectors"] for chunk in chunks)
    rayleigh_certified = sum(chunk["rayleigh_certified"] for chunk in chunks)
    exact_fallbacks = sum(chunk["exact_fallbacks"] for chunk in chunks)
    counterexamples = [
        record for chunk in chunks for record in chunk.get("counterexample_records", [])
    ]
    fallback_records = [
        record for chunk in chunks for record in chunk.get("fallback_records", [])
    ]
    shell_counts_completed = {weight: 0 for weight in expected["shell_counts"]}
    for chunk in chunks:
        shell_counts_completed[chunk["defect_count"]] += chunk[
            "completed_q_bracelets"
        ]
    optimizer_checks = [
        chunk["optimizer_exact_check"]
        for chunk in chunks
        if chunk.get("optimizer_exact_check") is not None
    ]
    optimizer_exact_check = optimizer_checks[0] if optimizer_checks else None
    if any(item != optimizer_exact_check for item in optimizer_checks):
        raise SearchAbort(
            "CHECKPOINT_VALIDATION_FAIL", "optimizer checkpoint records disagree"
        )

    top_heap: list[tuple[float, int, int, dict[str, Any]]] = []
    best_by_distance: dict[int, dict[str, Any]] = {}
    for chunk in chunks:
        for item in chunk.get("top_near_minimizers", []):
            _push_top(top_heap, item)
        diagnostic_records = chunk.get(
            "best_numeric_by_period4_distance",
            chunk.get("top_near_minimizers", []),
        )
        for item in diagnostic_records:
            if "distance_to_period4_Q_pattern" not in item:
                item = {
                    **item,
                    "distance_to_period4_Q_pattern": distance_to_period4_q_code(
                        int(item["canonical_q_code"]), n
                    ),
                }
            _update_best_by_distance(best_by_distance, item)

    threshold_expr = threshold_squared(n)
    threshold_lower, threshold_upper = rational_interval(threshold_expr, digits=25)
    threshold_rho = math.sqrt(float(sp.N(threshold_expr, 18)))
    previous_chain = chunks[-1]["chain_sha256"] if chunks else ZERO_SHA256
    certificate_manifest_digest = hashlib.sha256()
    for chunk in chunks:
        certificate_manifest_digest.update(
            bytes.fromhex(chunk["ordered_certificate_sha256"])
        )

    current: dict[str, Any] | None = None
    chunk_started = time.time()

    def start_chunk(state: tuple[int, int, int, int]) -> dict[str, Any]:
        return {
            "defect_count": state[0],
            "first_canonical_q": state[1],
            "first_alpha": state[3],
            "last_canonical_q": state[1],
            "last_alpha": state[3],
            "completed_states": 0,
            "completed_q_bracelets": 0,
            "represented_q_vectors": 0,
            "rayleigh_certified": 0,
            "exact_fallbacks": 0,
            "counterexample_records": [],
            "fallback_records": [],
            "optimizer_exact_check": None,
            "input_digest": hashlib.sha256(),
            "certificate_digest": hashlib.sha256(),
            "top_heap": [],
            "best_by_distance": {},
        }

    def flush_chunk() -> None:
        nonlocal current, previous_chain, chunk_started
        if current is None or current["completed_states"] == 0:
            return
        chunk_index = len(chunks)
        input_sha = current["input_digest"].hexdigest()
        certificate_sha = current["certificate_digest"].hexdigest()
        chain_sha = _chain_hash(
            previous_chain,
            input_sha,
            certificate_sha,
            chunk_index,
            current["completed_states"],
        )
        payload = {
            "schema_version": SCHEMA_VERSION,
            "git_commit": git_commit,
            "baseline_git_commit": git_commit,
            "n": n,
            "defect_count": current["defect_count"],
            "expected_shell_q_bracelets": expected["shell_counts"][
                current["defect_count"]
            ],
            "chunk_index": chunk_index,
            "first_canonical_q": current["first_canonical_q"],
            "last_canonical_q": current["last_canonical_q"],
            "first_alpha": current["first_alpha"],
            "last_alpha": current["last_alpha"],
            "completed_states": current["completed_states"],
            "completed_q_bracelets": current["completed_q_bracelets"],
            "represented_q_vectors": current["represented_q_vectors"],
            "rayleigh_certified": current["rayleigh_certified"],
            "exact_fallbacks": current["exact_fallbacks"],
            "counterexamples": len(current["counterexample_records"]),
            "counterexample_records": current["counterexample_records"],
            "fallback_records": current["fallback_records"],
            "optimizer_exact_check": current["optimizer_exact_check"],
            "top_near_minimizers": _sorted_top(current["top_heap"]),
            "best_numeric_by_period4_distance": [
                current["best_by_distance"][distance]
                for distance in sorted(current["best_by_distance"])
            ],
            "ordered_input_sha256": input_sha,
            "ordered_certificate_sha256": certificate_sha,
            "previous_chain_sha256": previous_chain,
            "chain_sha256": chain_sha,
            "elapsed_seconds": time.time() - chunk_started,
        }
        payload["content_sha256"] = _checkpoint_content_hash(payload)
        path = checkpoint_dir / f"chunk_{chunk_index:06d}.json"
        if path.exists():
            raise SearchAbort(
                "CHECKPOINT_VALIDATION_FAIL", f"refusing to replace {path.name}"
            )
        _durable_json_write(path, payload)
        chunks.append(payload)
        certificate_manifest_digest.update(bytes.fromhex(certificate_sha))
        previous_chain = chain_sha
        _write_manifest(checkpoint_dir, n, git_commit, chunks, "IN_PROGRESS")
        current = None
        chunk_started = time.time()

    stopped_early = False
    last_period4_code = None
    last_period4_distance = None
    for state in states:
        defect_count, code, orbit_size, alpha = state
        if current is not None and defect_count != current["defect_count"]:
            flush_chunk()
        if current is None:
            current = start_chunk(state)

        signing = signing_from_q(code, n, alpha)
        reconstructed_code, reconstructed_alpha = q_code_from_signing(signing)
        if reconstructed_code != code or reconstructed_alpha != alpha:
            raise SearchAbort(
                "STATE_CONSTRUCTION_ERROR",
                f"roundtrip failed for Q={code}, alpha={alpha}",
            )
        if code != last_period4_code:
            last_period4_code = code
            last_period4_distance = distance_to_period4_q_code(code, n)
        if last_period4_distance is None:
            raise AssertionError("period-4 diagnostic cache was not initialized")
        period4_distance = last_period4_distance
        validate_period4_diagnostic(n, code, period4_distance)

        encoded_input = _input_bytes(state)
        current["input_digest"].update(encoded_input)
        global_input_digest.update(encoded_input)
        matrix = numpy_matrix(signing)
        is_optimizer = defect_count == 0 and alpha == -1
        certificate_record: dict[str, Any]
        if is_optimizer:
            optimizer_exact_check = exact_optimizer_check(signing)
            current["optimizer_exact_check"] = optimizer_exact_check
            certificate_record = {
                "state": [defect_count, code, orbit_size, alpha],
                "decision": "OPTIMIZER_EXACT_EQUALITY",
                "detail": optimizer_exact_check,
            }
        else:
            values, vectors = np.linalg.eigh(matrix.astype(float))
            extremal_index = int(np.argmax(np.abs(values)))
            rho = float(abs(values[extremal_index]))
            bound, integer_vector = _integer_rayleigh_certificate(
                matrix, vectors[:, extremal_index]
            )
            near_item = _basic_near_minimizer(
                n,
                defect_count,
                code,
                orbit_size,
                alpha,
                rho,
                threshold_rho,
                bound,
                period4_distance,
            )
            _push_top(top_heap, near_item)
            _push_top(current["top_heap"], near_item)
            _update_best_by_distance(best_by_distance, near_item)
            _update_best_by_distance(current["best_by_distance"], near_item)
            if bound >= threshold_upper:
                rayleigh_certified += 1
                current["rayleigh_certified"] += 1
                certificate_record = {
                    "state": [defect_count, code, orbit_size, alpha],
                    "decision": "RAYLEIGH_CERTIFIED",
                    "numerator": bound.numerator,
                    "denominator": bound.denominator,
                }
            else:
                exact_fallbacks += 1
                current["exact_fallbacks"] += 1
                is_counterexample, detail = is_strict_counterexample(signing)
                fallback = {
                    "state": [defect_count, code, orbit_size, alpha],
                    "integer_Rayleigh_vector": integer_vector,
                    "Rayleigh_certificate": str(bound),
                    "exact_result": detail,
                }
                fallback_records.append(fallback)
                current["fallback_records"].append(fallback)
                certificate_record = {
                    "state": [defect_count, code, orbit_size, alpha],
                    "decision": detail["decision"],
                    "detail": detail,
                }
                if is_counterexample:
                    candidate = _counterexample_record(
                        n,
                        defect_count,
                        code,
                        orbit_size,
                        alpha,
                        signing,
                        matrix,
                        integer_vector,
                        bound,
                        detail,
                        threshold_lower,
                        threshold_upper,
                    )
                    counterexamples.append(candidate)
                    current["counterexample_records"].append(candidate)

        current["certificate_digest"].update(_canonical_json(certificate_record))
        current["last_canonical_q"] = code
        current["last_alpha"] = alpha
        current["completed_states"] += 1
        completed_states += 1
        if alpha == 1:
            current["completed_q_bracelets"] += 1
            current["represented_q_vectors"] += orbit_size
            completed_q_bracelets += 1
            represented_q_vectors += orbit_size
            shell_counts_completed[defect_count] += 1

        if counterexamples:
            flush_chunk()
            break
        if current is not None and current["completed_states"] >= chunk_size:
            flush_chunk()
        if stop_after_states is not None and completed_states >= stop_after_states:
            flush_chunk()
            stopped_early = True
            break
    else:
        flush_chunk()

    status = determine_completion_status(
        n,
        expected,
        completed_q_bracelets,
        completed_states,
        represented_q_vectors,
        shell_counts_completed,
        rayleigh_certified,
        exact_fallbacks,
        counterexamples,
        optimizer_exact_check,
    )
    if stopped_early and status.startswith("VERIFIED_NO_COUNTEREXAMPLE"):
        raise AssertionError("an intentionally incomplete run passed")
    _manifest, manifest_sha256 = _write_manifest(
        checkpoint_dir, n, git_commit, chunks, status
    )
    expanded_top = [
        _expand_near_minimizer(n, item) for item in _sorted_top(top_heap)
    ]
    expanded_best_by_distance = [
        _expand_near_minimizer(n, best_by_distance[distance])
        for distance in sorted(best_by_distance)
    ]
    completion = Fraction(completed_states, expected["spectral_states"])
    script_path = Path(__file__).resolve()
    generator_path = script_path.with_name("target_a_bracelets.py")
    return {
        "schema_version": SCHEMA_VERSION,
        "n": n,
        "status": status,
        "git_commit": git_commit,
        "baseline_git_commit": git_commit,
        "branch": branch,
        "command": shlex.join((sys.executable, *sys.argv)),
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "numpy": np.__version__,
            "sympy": sp.__version__,
        },
        "python": sys.version,
        "platform": platform.platform(),
        "numpy": np.__version__,
        "sympy": sp.__version__,
        "expected_q_bracelets": expected["q_bracelets"],
        "completed_q_bracelets": completed_q_bracelets,
        "expected_spectral_states": expected["spectral_states"],
        "completed_spectral_states": completed_states,
        "represented_q_vectors": represented_q_vectors,
        "represented_switching_classes": 4 * represented_q_vectors,
        "shell_counts_expected": {
            str(key): value for key, value in expected["shell_counts"].items()
        },
        "shell_counts_completed": {
            str(key): value for key, value in shell_counts_completed.items()
        },
        "search_space_audit": expected_audit,
        "threshold_squared_interval": [
            str(threshold_lower),
            str(threshold_upper),
        ],
        "threshold_squared_lower": str(threshold_lower),
        "threshold_squared_upper": str(threshold_upper),
        "threshold_numeric_rho_preview": threshold_rho,
        "optimizer": {"defect_count": 0, "canonical_q_code": 0, "alpha": -1},
        "optimizer_exact_check": optimizer_exact_check,
        "rayleigh_certified": rayleigh_certified,
        "exact_fallbacks": exact_fallbacks,
        "fallback_records": fallback_records,
        "counterexamples": counterexamples,
        "top_near_minimizers": expanded_top,
        "best_numeric_by_period4_distance": expanded_best_by_distance,
        "near_minimizer_ranking_status": "OBSERVED_NUMERIC_ORDER_ONLY",
        "period4_diagnostic": {
            "convention": "exact length-n truncation of (+,-,-,-,...) at index 0",
            "reference_code": period4_reference_code(n),
            "reference_Q": [
                1 if index % 4 == 0 else -1 for index in range(n)
            ],
            "reference_defect_count": period4_reference_code(n).bit_count(),
            "distance": "minimum Hamming distance over rotations and reflections",
            "distance_parity_rule": (
                "distance parity equals Q-weight parity plus reference-weight parity"
            ),
        },
        "checkpoint_chunks": len(chunks),
        "checkpoint_manifest_sha256": manifest_sha256,
        "checkpoint_final_chain_sha256": previous_chain,
        "final_checkpoint_chain_sha256": previous_chain,
        "ordered_input_sha256": global_input_digest.hexdigest(),
        "ordered_certificate_sha256": certificate_manifest_digest.hexdigest(),
        "elapsed_seconds": time.time() - started,
        "peak_rss": _peak_rss_bytes(),
        "generator_name": GENERATOR_NAME,
        "generator_source_sha256": _sha256_file(generator_path),
        "search_script_sha256": _sha256_file(script_path),
        "completion_fraction": (
            completion.numerator
            if completion.denominator == 1
            else f"{completion.numerator}/{completion.denominator}"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--checkpoint-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--chunk-size", type=int, default=20_000)
    parser.add_argument("--stop-after-states", type=int)
    args = parser.parse_args()
    try:
        payload = run_minimality_search(
            args.n,
            args.checkpoint_dir,
            resume=args.resume,
            chunk_size=args.chunk_size,
            stop_after_states=args.stop_after_states,
        )
    except SearchAbort as error:
        payload = {
            "n": args.n,
            "status": error.status,
            "error": str(error),
        }
    _durable_json_write(args.output, payload)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    success = payload["status"].startswith("VERIFIED_NO_COUNTEREXAMPLE_AT_N")
    incomplete = payload["status"] == "INCOMPLETE"
    raise SystemExit(0 if success or incomplete else 1)


if __name__ == "__main__":
    main()

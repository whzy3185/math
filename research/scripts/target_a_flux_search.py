"""Search Target A in quadrilateral-flux coordinates modulo dihedral symmetry.

A spectral state is encoded by (Q, alpha), where Q_i is the product of two
adjacent triangle fluxes and alpha is the step-1 Hamilton-cycle holonomy.
The parity constraint product(Q_i) = 1 leaves 2^(n-1) Q-vectors.  The missing
choice of the initial triangle flux is global edge negation, which preserves
the spectral radius.  Rotations and reflections are quotiented by binary
bracelet canonicalization.

Floating eigensolvers rank states and propose integer Rayleigh vectors.  Every
non-optimizer exclusion is certified by exact rational arithmetic against a
certified algebraic upper bound for the conjectured threshold.  Uncertain
states fall back to the independent exact verifier.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterator

import numpy as np
import sympy as sp

from target_a_reproduce import integer_rayleigh_lower_bound, numpy_matrix
from target_a_verifier import (
    Signing,
    is_strict_counterexample,
    rational_interval,
    threshold_squared,
)


def reverse_n_bits(code: int, n: int) -> int:
    result = 0
    for _ in range(n):
        result = (result << 1) | (code & 1)
        code >>= 1
    return result


def rotate_left(code: int, shift: int, n: int) -> int:
    mask = (1 << n) - 1
    shift %= n
    if shift == 0:
        return code & mask
    return ((code << shift) | (code >> (n - shift))) & mask


def dihedral_orbit(code: int, n: int) -> tuple[int, ...]:
    reflected = reverse_n_bits(code, n)
    return tuple(
        sorted(
            {rotate_left(code, shift, n) for shift in range(n)}
            | {rotate_left(reflected, shift, n) for shift in range(n)}
        )
    )


def canonical_q_code(code: int, n: int) -> int:
    return min(dihedral_orbit(code, n))


def enumerate_q_orbits(
    n: int, max_defects: int | None = None
) -> Iterator[tuple[int, int]]:
    """Yield (canonical Q code, orbit size) for even-defect bracelets."""
    visited = bytearray(1 << n)
    for code in range(1 << n):
        defects = code.bit_count()
        if defects % 2 or (max_defects is not None and defects > max_defects):
            continue
        if visited[code]:
            continue
        orbit = dihedral_orbit(code, n)
        if orbit[0] != code:
            raise AssertionError("ascending orbit enumeration lost canonicality")
        for member in orbit:
            visited[member] = 1
        yield code, len(orbit)


def q_vector(code: int, n: int) -> tuple[int, ...]:
    """Bit 1 denotes a defect Q_i=+1; bit 0 denotes Q_i=-1."""
    return tuple(1 if (code >> i) & 1 else -1 for i in range(n))


def triangle_flux_from_q(code: int, n: int, tau0: int = 1) -> tuple[int, ...]:
    q = q_vector(code, n)
    tau = [tau0]
    for i in range(n - 1):
        tau.append(tau[-1] * q[i])
    if tau[-1] * q[-1] != tau0:
        raise ValueError("Q-vector violates product(Q_i)=1")
    return tuple(tau)


def signing_from_q(code: int, n: int, alpha: int) -> Signing:
    if alpha not in (-1, 1):
        raise ValueError("alpha must be +1 or -1")
    step1 = [1] * n
    step1[-1] = alpha
    tau = triangle_flux_from_q(code, n)
    step2 = [tau[i] * step1[i] * step1[(i + 1) % n] for i in range(n)]
    return Signing(n, tuple(step1), tuple(step2))


def q_code_from_signing(signing: Signing) -> tuple[int, int]:
    n = signing.n
    tau = [
        signing.step1[i]
        * signing.step1[(i + 1) % n]
        * signing.step2[i]
        for i in range(n)
    ]
    code = 0
    for i in range(n):
        if tau[i] * tau[(i + 1) % n] == 1:
            code |= 1 << i
    alpha = math.prod(signing.step1)
    return code, alpha


def circular_gaps(positions: list[int], n: int) -> list[int]:
    if not positions:
        return []
    return [
        (positions[(i + 1) % len(positions)] - positions[i]) % n
        for i in range(len(positions))
    ]


def exact_even_traces(matrix: np.ndarray) -> dict[str, int]:
    square = matrix @ matrix
    fourth = square @ square
    sixth = fourth @ square
    eighth = fourth @ fourth
    return {
        "trace_A4": int(np.trace(fourth)),
        "trace_A6": int(np.trace(sixth)),
        "trace_A8": int(np.trace(eighth)),
    }


def representative_detail(code: int, orbit_size: int, n: int, alpha: int) -> dict[str, Any]:
    q = q_vector(code, n)
    tau = triangle_flux_from_q(code, n)
    positions = [i for i, value in enumerate(q) if value == 1]
    matrix = numpy_matrix(signing_from_q(code, n, alpha))
    detail: dict[str, Any] = {
        "canonical_q_code": code,
        "dihedral_orbit_size": orbit_size,
        "canonical_Q": list(q),
        "triangle_flux_tau0_plus": list(tau),
        "defect_positions": positions,
        "cyclic_defect_gaps": circular_gaps(positions, n),
        **exact_even_traces(matrix),
    }
    if len(positions) == 2:
        separation = (positions[1] - positions[0]) % n
        detail["two_defect_distance"] = min(separation, n - separation)
    return detail


def count_orbits(n: int, max_defects: int | None = None) -> dict[str, Any]:
    by_defect: dict[int, int] = defaultdict(int)
    represented_q_vectors = 0
    for code, orbit_size in enumerate_q_orbits(n, max_defects):
        by_defect[code.bit_count()] += 1
        represented_q_vectors += orbit_size
    q_orbits = sum(by_defect.values())
    return {
        "n": n,
        "max_defects": max_defects,
        "q_orbits_by_defect": {str(d): by_defect[d] for d in sorted(by_defect)},
        "q_orbits": q_orbits,
        "spectral_states_with_alpha": 2 * q_orbits,
        "represented_q_vectors": represented_q_vectors,
        "represented_switching_classes": 4 * represented_q_vectors,
    }


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def analyze_shell(
    n: int,
    defect_count: int,
    representatives: list[tuple[int, int]],
    threshold_rho: float,
    threshold_upper: Any,
) -> dict[str, Any]:
    started = time.time()
    rows: dict[int, dict[str, Any]] = {}
    certified = 0
    exact_fallbacks = 0
    counterexamples: list[dict[str, Any]] = []
    two_defect_profile: list[dict[str, Any]] = []

    for alpha in (-1, 1):
        rows[alpha] = {
            "defect_count": defect_count,
            "alpha": alpha,
            "min_numeric_rho": float("inf"),
            "gap_from_optimizer": float("inf"),
            "attaining_q_orbits": 0,
            "minimizers": [],
        }

    for code, orbit_size in representatives:
        for alpha in (-1, 1):
            signing = signing_from_q(code, n, alpha)
            matrix = numpy_matrix(signing)
            values, vectors = np.linalg.eigh(matrix.astype(float))
            extremal_index = int(np.argmax(np.abs(values)))
            rho = float(abs(values[extremal_index]))
            row = rows[alpha]
            if rho < row["min_numeric_rho"] - 1e-11:
                row["min_numeric_rho"] = rho
                row["gap_from_optimizer"] = rho - threshold_rho
                row["attaining_q_orbits"] = 1
                row["minimizers"] = [(code, orbit_size)]
            elif abs(rho - row["min_numeric_rho"]) <= 1e-11:
                row["attaining_q_orbits"] += 1
                row["minimizers"].append((code, orbit_size))

            if defect_count == 2:
                two_defect_profile.append(
                    {
                        "alpha": alpha,
                        "numeric_rho": rho,
                        "gap_from_optimizer": rho - threshold_rho,
                        **representative_detail(code, orbit_size, n, alpha),
                    }
                )

            is_optimizer = defect_count == 0 and alpha == -1
            if is_optimizer:
                continue
            bound = integer_rayleigh_lower_bound(matrix, vectors[:, extremal_index])
            if bound >= threshold_upper:
                certified += 1
                continue
            exact_fallbacks += 1
            is_counterexample, detail = is_strict_counterexample(signing)
            if is_counterexample:
                counterexamples.append(
                    {
                        "canonical_q_code": code,
                        "dihedral_orbit_size": orbit_size,
                        "alpha": alpha,
                        "detail": detail,
                    }
                )

    atlas_rows = []
    for alpha in (-1, 1):
        row = rows[alpha]
        minimizers = row.pop("minimizers")
        row["minimizer_details"] = [
            representative_detail(code, orbit_size, n, alpha)
            for code, orbit_size in minimizers[:64]
        ]
        row["minimizer_details_truncated"] = len(minimizers) > 64
        atlas_rows.append(row)

    return {
        "n": n,
        "defect_count": defect_count,
        "q_orbits": len(representatives),
        "spectral_states": 2 * len(representatives),
        "represented_switching_classes": 4 * sum(size for _, size in representatives),
        "rayleigh_certified_nonoptimizers": certified,
        "exact_fallbacks": exact_fallbacks,
        "counterexamples": counterexamples,
        "atlas_rows": atlas_rows,
        "two_defect_profile": sorted(
            two_defect_profile,
            key=lambda item: (item["two_defect_distance"], item["alpha"]),
        ),
        "elapsed_seconds": time.time() - started,
    }


def search_flux_orbits(
    n: int,
    max_defects: int | None = None,
    checkpoint_dir: Path | None = None,
    resume: bool = False,
) -> dict[str, Any]:
    started = time.time()
    threshold_expr = threshold_squared(n)
    _, threshold_upper = rational_interval(threshold_expr, digits=25)
    threshold_rho = math.sqrt(float(sp.N(threshold_expr, 18)))
    grouped: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for code, orbit_size in enumerate_q_orbits(n, max_defects):
        grouped[code.bit_count()].append((code, orbit_size))

    shells = []
    for defect_count in sorted(grouped):
        checkpoint = (
            checkpoint_dir / f"target_a_n{n}_d{defect_count:02d}.json"
            if checkpoint_dir is not None
            else None
        )
        if resume and checkpoint is not None and checkpoint.exists():
            shell = json.loads(checkpoint.read_text(encoding="utf-8"))
        else:
            shell = analyze_shell(
                n,
                defect_count,
                grouped[defect_count],
                threshold_rho,
                threshold_upper,
            )
            if checkpoint is not None:
                _write_json(checkpoint, shell)
        shells.append(shell)

    atlas = [row for shell in shells for row in shell["atlas_rows"]]
    counterexamples = [item for shell in shells for item in shell["counterexamples"]]
    nonoptimizer_rows = [
        row for row in atlas if not (row["defect_count"] == 0 and row["alpha"] == -1)
    ]
    smallest_nonoptimizer = min(nonoptimizer_rows, key=lambda row: row["min_numeric_rho"])
    q_orbits = sum(shell["q_orbits"] for shell in shells)
    result = {
        "method": "(Q, alpha)/D_n + one dense eigh + exact rational Rayleigh certificates",
        "n": n,
        "max_defects": max_defects,
        "threshold_numeric_rho": threshold_rho,
        "threshold_squared_upper": str(threshold_upper),
        "q_orbits": q_orbits,
        "spectral_states": 2 * q_orbits,
        "represented_switching_classes": sum(
            shell["represented_switching_classes"] for shell in shells
        ),
        "rayleigh_certified_nonoptimizers": sum(
            shell["rayleigh_certified_nonoptimizers"] for shell in shells
        ),
        "exact_fallbacks": sum(shell["exact_fallbacks"] for shell in shells),
        "counterexamples": counterexamples,
        "smallest_nonoptimizer": smallest_nonoptimizer,
        "two_defect_profile": [
            item for shell in shells for item in shell.get("two_defect_profile", [])
        ],
        "atlas": atlas,
        "shell_summaries": [
            {
                key: shell[key]
                for key in (
                    "defect_count",
                    "q_orbits",
                    "spectral_states",
                    "represented_switching_classes",
                    "rayleigh_certified_nonoptimizers",
                    "exact_fallbacks",
                    "elapsed_seconds",
                )
            }
            for shell in shells
        ],
        "status": "PASS" if not counterexamples else "FAIL",
        "elapsed_seconds": time.time() - started,
    }
    return result


def validate_reference(result: dict[str, Any], reference_path: Path) -> dict[str, Any]:
    reference_payload = json.loads(reference_path.read_text(encoding="utf-8"))
    reference = reference_payload["results"][0]
    checks = {
        "same_n": result["n"] == reference["n"],
        "same_counterexample_count": len(result["counterexamples"])
        == len(reference["counterexamples"]),
        "same_smallest_nonoptimizer_rho": math.isclose(
            result["smallest_nonoptimizer"]["min_numeric_rho"],
            reference["smallest_nonoptimizer_numeric_rho"],
            rel_tol=0.0,
            abs_tol=1e-10,
        ),
        "optimizer_is_d0_alpha_minus1": any(
            row["defect_count"] == 0
            and row["alpha"] == -1
            and abs(row["gap_from_optimizer"]) <= 1e-10
            for row in result["atlas"]
        ),
        "covers_all_switching_classes": result["represented_switching_classes"]
        == reference["switching_classes"],
    }
    return {"checks": checks, "status": "PASS" if all(checks.values()) else "FAIL"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=20)
    parser.add_argument("--max-defects", type=int)
    parser.add_argument("--counts-only", action="store_true")
    parser.add_argument("--checkpoint-dir", type=Path)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--reference-log", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.n < 8 or args.n % 2:
        parser.error("n must be even and at least 8")
    if args.max_defects is not None and args.max_defects % 2:
        parser.error("max-defects must be even")

    if args.counts_only:
        payload = count_orbits(args.n, args.max_defects)
    else:
        payload = search_flux_orbits(
            args.n,
            args.max_defects,
            args.checkpoint_dir,
            args.resume,
        )
        if args.reference_log:
            payload["reference_validation"] = validate_reference(payload, args.reference_log)
            if payload["reference_validation"]["status"] != "PASS":
                payload["status"] = "FAIL"
    if args.output:
        _write_json(args.output, payload)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    raise SystemExit(0 if payload.get("status", "PASS") == "PASS" else 1)


if __name__ == "__main__":
    main()

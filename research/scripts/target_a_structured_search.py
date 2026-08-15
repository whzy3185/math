"""Structured numerical attacks on Target A beyond exhaustive orbit searches.

These scans are exploratory.  Finite candidates below the conjectured bound
are handed to the exact verifier; otherwise reported gaps remain Observed.
Periodic Q-patterns are evaluated on the infinite cover with a Floquet symbol.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path
from typing import Any, Iterator

import numpy as np

from target_a_flux_search import (
    dihedral_orbit,
    q_vector,
    signing_from_q,
)
from target_a_reproduce import numpy_matrix


def threshold_rho(n: int) -> float:
    return 2.0 * math.sqrt(math.cos(math.pi / n) ** 2 + math.cos(2 * math.pi / n) ** 2)


def code_from_positions(positions: list[int]) -> int:
    code = 0
    for position in positions:
        code |= 1 << position
    return code


def numeric_rho(code: int, n: int, alpha: int) -> float:
    matrix = numpy_matrix(signing_from_q(code, n, alpha))
    return float(np.max(np.abs(np.linalg.eigvalsh(matrix.astype(float)))))


def finite_record(code: int, n: int, alpha: int, family: str) -> dict[str, Any]:
    rho = numeric_rho(code, n, alpha)
    threshold = threshold_rho(n)
    record: dict[str, Any] = {
        "family": family,
        "n": n,
        "alpha": alpha,
        "q_code": code,
        "defect_positions": [i for i in range(n) if (code >> i) & 1],
        "numeric_rho": rho,
        "threshold_rho": threshold,
        "numeric_gap": rho - threshold,
        "evidence": "Observed",
    }
    if rho < threshold - 1e-10:
        record["numeric_candidate_below_threshold"] = True
    return record


def scan_two_defects(ns: list[int]) -> list[dict[str, Any]]:
    results = []
    for n in ns:
        records = [
            finite_record(code_from_positions([0, distance]), n, alpha, "two_defect")
            for distance in range(1, n // 2 + 1)
            for alpha in (-1, 1)
        ]
        best = min(records, key=lambda item: item["numeric_rho"])
        best["distance"] = best["defect_positions"][1]
        results.append(best)
    return results


def scan_local_four_defects(min_n: int, max_n: int) -> list[dict[str, Any]]:
    positions = [0, 4, 10, 14]
    results = []
    for n in range(min_n, max_n + 1, 2):
        records = [
            finite_record(code_from_positions(positions), n, alpha, "local_d4_0_4_10_14")
            for alpha in (-1, 1)
        ]
        results.append(min(records, key=lambda item: item["numeric_rho"]))
    return results


def scan_period10_defects(max_n: int) -> list[dict[str, Any]]:
    results = []
    for n in range(20, max_n + 1, 10):
        positions = [position for position in range(n) if position % 10 in (0, 4)]
        records = [
            finite_record(code_from_positions(positions), n, alpha, "period10_defects_0_4")
            for alpha in (-1, 1)
        ]
        results.append(min(records, key=lambda item: item["numeric_rho"]))
    return results


def enumerate_binary_bracelets(n: int) -> Iterator[int]:
    visited = bytearray(1 << n)
    for code in range(1 << n):
        if visited[code]:
            continue
        orbit = dihedral_orbit(code, n)
        if orbit[0] != code:
            raise AssertionError("bracelet enumeration lost canonicality")
        for member in orbit:
            visited[member] = 1
        yield code


def has_minimal_period(code: int, period: int) -> bool:
    bits = [(code >> i) & 1 for i in range(period)]
    for divisor in range(1, period):
        if period % divisor == 0 and all(bits[i] == bits[i % divisor] for i in range(period)):
            return False
    return True


def tau_period_from_q_base(code: int, period: int) -> tuple[int, ...]:
    q = q_vector(code, period)
    tau_period = period if math.prod(q) == 1 else 2 * period
    tau = [1]
    for i in range(tau_period - 1):
        tau.append(tau[-1] * q[i % period])
    if tau[-1] * q[(tau_period - 1) % period] != 1:
        raise AssertionError("triangle-flux period did not close")
    return tuple(tau)


def floquet_matrix(tau: tuple[int, ...], theta: float) -> np.ndarray:
    period = len(tau)
    matrix = np.zeros((period, period), dtype=np.complex128)
    for i in range(period):
        terms = (
            (-2, tau[(i - 2) % period]),
            (-1, 1),
            (1, 1),
            (2, tau[i]),
        )
        for delta, coefficient in terms:
            target = i + delta
            residue = target % period
            cell_shift = (target - residue) // period
            matrix[i, residue] += coefficient * np.exp(1j * theta * cell_shift)
    if not np.allclose(matrix, matrix.conj().T, atol=1e-12):
        raise AssertionError("Floquet symbol is not Hermitian")
    return matrix


def floquet_rho(tau: tuple[int, ...], theta_count: int) -> tuple[float, float]:
    best_rho = -1.0
    best_theta = 0.0
    for theta in np.linspace(0.0, 2.0 * math.pi, theta_count, endpoint=False):
        values = np.linalg.eigvalsh(floquet_matrix(tau, float(theta)))
        rho = float(np.max(np.abs(values)))
        if rho > best_rho:
            best_rho = rho
            best_theta = float(theta)
    return best_rho, best_theta


def scan_periodic_q(max_period: int, coarse_theta_count: int = 256) -> dict[str, Any]:
    patterns = []
    for period in range(1, max_period + 1):
        for code in enumerate_binary_bracelets(period):
            if not has_minimal_period(code, period):
                continue
            tau = tau_period_from_q_base(code, period)
            rho, theta = floquet_rho(tau, coarse_theta_count)
            patterns.append(
                {
                    "q_period": period,
                    "canonical_q_code": code,
                    "Q_base": list(q_vector(code, period)),
                    "tau_period": len(tau),
                    "coarse_band_rho": rho,
                    "coarse_maximizing_theta": theta,
                }
            )

    # Refine the most competitive non-alternating patterns on a much finer grid.
    nonoptimizer = [
        pattern
        for pattern in patterns
        if not (pattern["q_period"] == 1 and pattern["canonical_q_code"] == 0)
    ]
    candidates = sorted(nonoptimizer, key=lambda item: item["coarse_band_rho"])[:20]
    for pattern in candidates:
        tau = tau_period_from_q_base(pattern["canonical_q_code"], pattern["q_period"])
        rho, theta = floquet_rho(tau, 2048)
        pattern["refined_band_rho"] = rho
        pattern["refined_maximizing_theta"] = theta
        pattern["gap_from_2sqrt2"] = rho - 2.0 * math.sqrt(2.0)

    best = min(candidates, key=lambda item: item["refined_band_rho"])
    return {
        "max_q_period": max_period,
        "coarse_theta_count": coarse_theta_count,
        "patterns_scanned": len(patterns),
        "refined_theta_count": 2048,
        "smallest_nonoptimizer_periodic_pattern": best,
        "potential_asymptotic_counterexamples": [
            pattern for pattern in candidates if pattern["refined_band_rho"] < 2.0 * math.sqrt(2.0) - 1e-9
        ],
        "refined_candidates": sorted(candidates, key=lambda item: item["refined_band_rho"]),
        "evidence": "Observed (dense Floquet grid)",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=100)
    parser.add_argument("--max-period", type=int, default=12)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_n < 20 or args.max_n % 2:
        parser.error("max-n must be even and at least 20")

    started = time.time()
    two_defect_ns = sorted({24, 30, 40, 50, 60, 80, args.max_n})
    two_defect_ns = [n for n in two_defect_ns if n <= args.max_n and n % 2 == 0]
    payload = {
        "evidence": "Observed unless an exact_check field is present",
        "two_defect_best_by_n": scan_two_defects(two_defect_ns),
        "local_four_defect_best_by_n": scan_local_four_defects(16, args.max_n),
        "period10_family_best_by_n": scan_period10_defects(args.max_n),
        "periodic_floquet": scan_periodic_q(args.max_period),
        "elapsed_seconds": time.time() - started,
    }
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()

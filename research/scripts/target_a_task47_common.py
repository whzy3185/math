"""Shared deterministic utilities for Target A Task 47 experiments."""

from __future__ import annotations

import hashlib
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

import numpy as np
import sympy as sp

from target_a_general_period_moments import closed_walk_moments, tau_lift
from target_a_reproduce import integer_rayleigh_lower_bound, numpy_matrix
from target_a_flux_search import signing_from_q


ETA = 4 + math.sqrt(10 + 2 * math.sqrt(5))
TARGET_Q = (1, -1, -1, -1, 1, -1, -1, -1)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def repository_head(root: Path) -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=root, check=True, capture_output=True, text=True
    ).stdout.strip()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def q_bits(q: Iterable[int]) -> str:
    return "".join("1" if value == 1 else "0" for value in q)


def q_code(q: tuple[int, ...]) -> int:
    return sum((value == 1) << index for index, value in enumerate(q))


def primitive_period(word: tuple[int, ...]) -> int:
    n = len(word)
    for period in range(1, n + 1):
        if n % period == 0 and all(word[index] == word[index % period] for index in range(n)):
            return period
    raise AssertionError("word has no primitive period")


def reverse_word(word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(reversed(word))


def rotations(word: tuple[int, ...]) -> list[tuple[int, ...]]:
    return [word[shift:] + word[:shift] for shift in range(len(word))]


def canonical_q(q: tuple[int, ...]) -> tuple[int, ...]:
    images = rotations(q) + rotations(reverse_word(q))
    return min(images, key=q_bits)


def defect_gaps(q: tuple[int, ...]) -> list[int]:
    positions = [index for index, value in enumerate(q) if value == 1]
    if not positions:
        return []
    return sorted(
        (positions[(index + 1) % len(positions)] - positions[index]) % len(q)
        for index in range(len(positions))
    )


def floquet_matrix(tau: tuple[int, ...], theta: float) -> np.ndarray:
    p = len(tau)
    z = complex(math.cos(theta), math.sin(theta))
    matrix = np.zeros((p, p), dtype=np.complex128)
    for row in range(p):
        for source, coefficient in (
            (row - 1, 1),
            (row + 1, 1),
            (row - 2, tau[(row - 2) % p]),
            (row + 2, tau[row]),
        ):
            cell, column = divmod(source, p)
            matrix[row, column] += coefficient * z**cell
    if not np.allclose(matrix, matrix.conj().T, atol=1e-12):
        raise AssertionError("Floquet matrix is not Hermitian")
    return matrix


def radius_squared_at(tau: tuple[int, ...], theta: float) -> float:
    values = np.linalg.eigvalsh(floquet_matrix(tau, theta))
    return float(max(abs(values[0]), abs(values[-1])) ** 2)


def grid_radius_squared(q: tuple[int, ...], grid: int) -> dict[str, Any]:
    tau = tau_lift(q)
    best_value = -math.inf
    best_index = 0
    for index in range(grid):
        value = radius_squared_at(tau, 2 * math.pi * index / grid)
        if value > best_value:
            best_value = value
            best_index = index
    return {
        "value": best_value,
        "theta": 2 * math.pi * best_index / grid,
        "grid_index": best_index,
        "grid": grid,
        "status": "NUMERICAL_GRID_ESTIMATE",
    }


def _golden_maximum(tau: tuple[int, ...], left: float, right: float) -> tuple[float, float]:
    ratio = (math.sqrt(5) - 1) / 2
    x1 = right - ratio * (right - left)
    x2 = left + ratio * (right - left)
    f1 = radius_squared_at(tau, x1)
    f2 = radius_squared_at(tau, x2)
    for _ in range(64):
        if right - left < 1e-13:
            break
        if f1 < f2:
            left, x1, f1 = x1, x2, f2
            x2 = left + ratio * (right - left)
            f2 = radius_squared_at(tau, x2)
        else:
            right, x2, f2 = x2, x1, f1
            x1 = right - ratio * (right - left)
            f1 = radius_squared_at(tau, x1)
    return (f1, x1) if f1 >= f2 else (f2, x2)


def adaptive_radius_squared(q: tuple[int, ...], coarse_grid: int = 128) -> dict[str, Any]:
    tau = tau_lift(q)
    values = [radius_squared_at(tau, 2 * math.pi * index / coarse_grid) for index in range(coarse_grid)]
    candidate_indices = sorted(range(coarse_grid), key=values.__getitem__, reverse=True)[:8]
    step = 2 * math.pi / coarse_grid
    best_value = -math.inf
    best_theta = 0.0
    for index in candidate_indices:
        value, theta = _golden_maximum(tau, index * step - step, index * step + step)
        theta %= 2 * math.pi
        if value > best_value:
            best_value, best_theta = value, theta
    grid_best = max(values)
    return {
        "value": max(best_value, grid_best),
        "theta": best_theta if best_value >= grid_best else step * int(np.argmax(values)),
        "coarse_grid": coarse_grid,
        "local_intervals_refined": len(candidate_indices),
        "status": "ADAPTIVE_CONTINUOUS_BLOCH_NUMERICAL_ESTIMATE",
        "warning": "floating adaptive maximization is not a rigorous enclosure",
    }


def exact_endpoint_rayleigh(q: tuple[int, ...], minimum: Fraction = Fraction(1561, 200)) -> dict[str, Any] | None:
    """Try to prove R(Q)>eta using an exact rational endpoint Rayleigh quotient."""
    eta_exact = 4 + sp.sqrt(10 + 2 * sp.sqrt(5))
    if sp.simplify(sp.Rational(minimum.numerator, minimum.denominator) - eta_exact).is_positive is not True:
        raise AssertionError("the rational comparison point does not strictly exceed eta")
    code = q_code(q)
    best: tuple[Fraction, int] | None = None
    for alpha in (-1, 1):
        matrix = numpy_matrix(signing_from_q(code, len(q), alpha))
        values, vectors = np.linalg.eigh(matrix.astype(float))
        index = int(np.argmax(np.abs(values)))
        bound = integer_rayleigh_lower_bound(matrix, vectors[:, index])
        if best is None or bound > best[0]:
            best = (bound, alpha)
    assert best is not None
    bound, alpha = best
    if bound <= minimum:
        return None
    return {
        "status": "CERTIFIED_R_GT_ETA",
        "method": "exact integer Rayleigh quotient at Bloch endpoint alpha=+1 or -1",
        "alpha": alpha,
        "rayleigh_lower_bound": str(bound),
        "comparison_rational": str(minimum),
        "logic": f"R(Q)^2 >= Rayleigh > {minimum} > eta; the last sign is checked exactly in SymPy",
    }


def exact_moment_profile(q: tuple[int, ...], maximum_k: int) -> dict[str, Any]:
    moments = closed_walk_moments(q, maximum_k + 1)
    excesses = [moments[index] - 8 * moments[index - 1] for index in range(1, len(moments))]
    first = next((index + 1 for index, value in enumerate(excesses) if value > 0), None)
    return {"moments": moments, "excesses": excesses, "first_positive_k": first}

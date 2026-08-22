"""Shared deterministic numerical and exact utilities for Target A Task 48A."""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any

import numpy as np

from target_a_flux_search import canonical_q_code, signing_from_q
from target_a_reproduce import numpy_matrix


def q_from_gaps(n: int, gaps: list[int]) -> tuple[int, ...]:
    if sum(gaps) != n or len(gaps) % 2:
        raise ValueError("gap sequence must sum to n and have an even number of defects")
    if min(gaps) <= 0:
        raise ValueError("all cyclic gaps must be positive")
    positions = [0]
    for gap in gaps[:-1]:
        positions.append(positions[-1] + gap)
    position_set = set(positions)
    return tuple(1 if i in position_set else -1 for i in range(n))


def canonical_code(q: tuple[int, ...]) -> int:
    code = sum((value == 1) << i for i, value in enumerate(q))
    return canonical_q_code(code, len(q))


def signing_arrays(q: tuple[int, ...], alpha: int) -> tuple[np.ndarray, np.ndarray]:
    signing = signing_from_q(canonical_code(q), len(q), alpha)
    return np.asarray(signing.step1, dtype=float), np.asarray(signing.step2, dtype=float)


def apply_adjacency(step1: np.ndarray, step2: np.ndarray, vector: np.ndarray) -> np.ndarray:
    return (
        step1 * np.roll(vector, -1)
        + np.roll(step1, 1) * np.roll(vector, 1)
        + step2 * np.roll(vector, -2)
        + np.roll(step2, 2) * np.roll(vector, 2)
    )


def sparse_radius_squared(
    q: tuple[int, ...], alpha: int, tolerance: float = 2e-13, maximum_iterations: int = 6000
) -> dict[str, Any]:
    step1, step2 = signing_arrays(q, alpha)
    n = len(q)
    x = np.sin((np.arange(n) + 1) * 0.731) + 0.3 * np.cos((np.arange(n) + 1) * 1.117)
    x += 2.0 * np.exp(-((np.minimum(np.arange(n), n - np.arange(n))) / 7.0) ** 2)
    x /= np.linalg.norm(x)
    value = 0.0
    residual = math.inf
    for iteration in range(1, maximum_iterations + 1):
        ax = apply_adjacency(step1, step2, x)
        y = apply_adjacency(step1, step2, ax)
        norm = np.linalg.norm(y)
        if norm == 0:
            raise AssertionError("zero A^2 iterate")
        x = y / norm
        ax = apply_adjacency(step1, step2, x)
        a2x = apply_adjacency(step1, step2, ax)
        new_value = float(np.dot(x, a2x))
        residual = float(np.linalg.norm(a2x - new_value * x))
        if abs(new_value - value) < tolerance * max(1.0, abs(new_value)) and residual < 2e-10:
            value = new_value
            break
        value = new_value
    return {
        "rho_squared": value,
        "eigenvector_A2": x,
        "iterations": iteration,
        "residual_A2": residual,
        "solver": "deterministic sparse A^2 power iteration",
    }


def dense_spectrum(q: tuple[int, ...], alpha: int) -> tuple[np.ndarray, np.ndarray]:
    matrix = numpy_matrix(signing_from_q(canonical_code(q), len(q), alpha)).astype(float)
    return np.linalg.eigh(matrix)


def single_slip_gaps(n: int, gap: int) -> list[int]:
    if (n - gap) % 4:
        raise ValueError("order is incompatible with the requested single slip")
    defect_count = (n - gap) // 4 + 1
    gaps = [gap] + [4] * (defect_count - 1)
    if defect_count % 2:
        raise ValueError("single-slip family violates Q legality")
    return gaps


def two_slip_gaps(n: int, separation_index: int) -> list[int]:
    defect_count = (n - 4) // 4
    if defect_count < 2 or defect_count % 2:
        raise ValueError("order is incompatible with two gap-6 slips")
    if not 0 <= separation_index <= (defect_count - 2) // 2:
        raise ValueError("separation is outside the dihedral fundamental domain")
    return [6] + [4] * separation_index + [6] + [4] * (defect_count - 2 - separation_index)


def threshold_squared_float(n: int) -> float:
    return 4 * (math.cos(math.pi / n) ** 2 + math.cos(2 * math.pi / n) ** 2)


def fit_log_tail(distances: np.ndarray, values: np.ndarray) -> dict[str, float]:
    # The first twelve cells resolve the physical tail while staying above the
    # A^2 iteration noise floor on the 512- and 1024-site rings.
    mask = (distances >= 2) & (distances <= 12) & (values > 1e-14)
    x = distances[mask].astype(float)
    y = np.log(values[mask])
    if len(x) < 4:
        return {"slope": float("nan"), "multiplier": float("nan"), "r_squared": float("nan"), "points": len(x)}
    design = np.column_stack([np.ones(len(x)), x])
    coefficients = np.linalg.lstsq(design, y, rcond=None)[0]
    prediction = design @ coefficients
    rss = float(np.sum((y - prediction) ** 2))
    tss = float(np.sum((y - y.mean()) ** 2))
    return {
        "slope": float(coefficients[1]),
        "multiplier": float(math.exp(coefficients[1])),
        "r_squared": 1 - rss / tss if tss else 1.0,
        "points": len(x),
    }


def localization_profile(vector: np.ndarray, center: int) -> dict[str, Any]:
    n = len(vector)
    amplitudes = []
    half = n // 2
    for offset in range(-half, half + 1):
        index = (center + offset) % n
        amplitudes.append({"offset": offset, "amplitude": float(abs(vector[index]))})
    max_cells = max(3, n // 16 - 2)
    cells = []
    for cell in range(-max_cells, max_cells + 1):
        indices = [(center + 8 * cell + shift - 3) % n for shift in range(8)]
        cells.append({"cell": cell, "norm": float(np.linalg.norm(vector[indices]))})
    left = [row for row in cells if row["cell"] < 0]
    right = [row for row in cells if row["cell"] > 0]
    left_fit = fit_log_tail(
        np.asarray([-row["cell"] for row in left]), np.asarray([row["norm"] for row in left])
    )
    right_fit = fit_log_tail(
        np.asarray([row["cell"] for row in right]), np.asarray([row["norm"] for row in right])
    )
    return {"site_amplitudes": amplitudes, "cell_norms": cells, "left_fit": left_fit, "right_fit": right_fit}


def fit_models(rows: list[dict[str, Any]], floquet_multipliers: list[float]) -> dict[str, Any]:
    rows = sorted(rows, key=lambda row: row["m"])
    m = np.asarray([row["m"] for row in rows], dtype=float)
    n = np.asarray([row["n"] for row in rows], dtype=float)
    y = np.asarray([row["rho_squared"] for row in rows], dtype=float)

    def score(name: str, basis: np.ndarray, parameter: float | list[float], k: int) -> dict[str, Any]:
        design = np.column_stack([np.ones(len(y)), basis])
        coefficients = np.linalg.lstsq(design, y, rcond=None)[0]
        residuals = y - design @ coefficients
        rss = max(float(np.sum(residuals**2)), 1e-300)
        aic = len(y) * math.log(rss / len(y)) + 2 * k
        bic = len(y) * math.log(rss / len(y)) + k * math.log(len(y))
        split = max(5, int(0.8 * len(y)))
        train_coeff = np.linalg.lstsq(design[:split], y[:split], rcond=None)[0]
        holdout = float(np.sum((y[split:] - design[split:] @ train_coeff) ** 2))
        return {
            "model": name,
            "parameters": parameter,
            "limit_c": float(coefficients[0]),
            "linear_coefficients": [float(value) for value in coefficients[1:]],
            "rss": rss,
            "AIC": aic,
            "BIC": bic,
            "holdout_rss": holdout,
            "parameter_count": k,
        }

    power_candidates = []
    for exponent in np.linspace(0.25, 10.0, 391):
        power_candidates.append(score("P", n[:, None] ** (-exponent), float(exponent), 3))
    power = min(power_candidates, key=lambda row: row["rss"])
    exponential_candidates = []
    m0 = m.min()
    for multiplier in np.geomspace(0.03, 0.95, 600):
        exponential_candidates.append(score("E", (multiplier ** (m - m0))[:, None], float(multiplier), 3))
    exponential = min(exponential_candidates, key=lambda row: row["rss"])
    multipliers = sorted(floquet_multipliers, reverse=True)[:2]
    e2_basis = np.column_stack([value ** (m - m0) for value in multipliers])
    two_exponential = score("E2", e2_basis, multipliers, 5)
    models = sorted([power, exponential, two_exponential], key=lambda row: row["BIC"])
    return {"models": models, "best_model": models[0]["model"], "second_best": models[1]["model"]}


def sparse_exact_ldl_positive(matrix: np.ndarray) -> dict[str, Any]:
    """Exact sparse LDL positivity test using an interior-first cycle ordering."""
    n = matrix.shape[0]
    boundary = min(4, n // 2)
    order = list(range(boundary, n - boundary)) + list(range(boundary)) + list(range(n - boundary, n))
    permuted = matrix[np.ix_(order, order)]
    active: list[dict[int, Fraction]] = []
    for i in range(n):
        active.append({j: Fraction(int(permuted[i, j])) for j in range(n) if permuted[i, j] != 0})
    pivots: list[Fraction] = []
    for k in range(n):
        pivot = active[k].get(k, Fraction(0))
        pivots.append(pivot)
        if pivot <= 0:
            return {"positive": False, "pivots": pivots, "order": order}
        neighbors = [i for i in range(k + 1, n) if active[i].get(k, 0)]
        for a, i in enumerate(neighbors):
            aik = active[i][k]
            for j in neighbors[a:]:
                value = active[j].get(i, Fraction(0)) - active[j][k] * aik / pivot
                if value:
                    active[j][i] = value
                    active[i][j] = value
                else:
                    active[j].pop(i, None)
                    active[i].pop(j, None)
        for i in neighbors:
            active[i].pop(k, None)
        active[k] = {k: pivot}
    return {"positive": True, "pivots": pivots, "order": order}

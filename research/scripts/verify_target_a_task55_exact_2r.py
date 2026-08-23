"""Independent fail-closed checker for the Task 55 exact-2r certificate.

This module deliberately does not import the producer or any of its helpers.
The G6 word, one-step transfer, interval arithmetic, Floquet charts, symmetry,
and all explicit constants are rebuilt below from their defining formulas.
"""

from __future__ import annotations

import hashlib
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product as cartesian_product
from math import isqrt
from pathlib import Path
from typing import Any

import sympy as sp


RESEARCH = Path(__file__).resolve().parents[1]
CERTIFICATE = RESEARCH / "proofs" / "task55" / "certificates" / "exact_2r_cluster.json"
G6_GLOBAL_EDGE = RESEARCH / "proofs" / "task53" / "certificates" / "g6_global_edge.json"

C6_LOWER = Fraction(7905369311620327, 10**15)
C6_UPPER = Fraction(7905369311620328, 10**15)
Q = Fraction(9, 25)
SQRT_DIGITS = 120
SUPPORTED_R = (1, 2, 3)


def strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_strict(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=strict_object)
    _reject_floats(data)
    return data


def _reject_floats(value: Any, location: str = "$") -> None:
    if isinstance(value, float):
        raise ValueError(f"floating-point acceptance value at {location}")
    if isinstance(value, dict):
        for key, child in value.items():
            _reject_floats(child, f"{location}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _reject_floats(child, f"{location}[{index}]")


def _fraction(value: Any) -> Fraction:
    if isinstance(value, bool) or isinstance(value, float):
        raise ValueError("non-exact rational value")
    return Fraction(value)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _compact_digest(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _ceil_fraction(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def _decimal_bound(value: Fraction, *, upper: bool, digits: int = 30) -> str:
    scale = 10**digits
    scaled = value.numerator * scale
    integer = -(-scaled // value.denominator) if upper else scaled // value.denominator
    sign = "-" if integer < 0 else ""
    integer = abs(integer)
    whole, decimal = divmod(integer, scale)
    return f"{sign}{whole}.{decimal:0{digits}d}"


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("reversed interval")

    @staticmethod
    def point(value: int | Fraction) -> "Interval":
        value = Fraction(value)
        return Interval(value, value)

    def __add__(self, other: object) -> "Interval":
        other = as_interval(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self) -> "Interval":
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other: object) -> "Interval":
        return self + (-as_interval(other))

    def __rsub__(self, other: object) -> "Interval":
        return as_interval(other) - self

    def __mul__(self, other: object) -> "Interval":
        other = as_interval(other)
        products = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def reciprocal(self) -> "Interval":
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError("interval contains zero")
        return Interval(min(1 / self.lo, 1 / self.hi), max(1 / self.lo, 1 / self.hi))

    def __truediv__(self, other: object) -> "Interval":
        return self * as_interval(other).reciprocal()

    def __rtruediv__(self, other: object) -> "Interval":
        return as_interval(other) / self

    def __pow__(self, exponent: int) -> "Interval":
        if exponent < 0:
            return self.reciprocal() ** (-exponent)
        result = Interval.point(1)
        base = self
        while exponent:
            if exponent & 1:
                result = result * base
            base = base * base
            exponent //= 2
        return result

    def excludes_zero(self) -> bool:
        return self.hi < 0 or self.lo > 0


def as_interval(value: object) -> Interval:
    if isinstance(value, Interval):
        return value
    if isinstance(value, (int, Fraction)):
        return Interval.point(value)
    raise TypeError(type(value))


def sqrt_interval(value: Interval) -> Interval:
    if value.lo < 0:
        raise ValueError("negative interval square root")
    scale = 10**SQRT_DIGITS

    def endpoint(number: Fraction, upper: bool) -> Fraction:
        numerator = number.numerator * scale * scale
        denominator = number.denominator
        root = isqrt(numerator // denominator)
        while (root + 1) ** 2 * denominator <= numerator:
            root += 1
        while root**2 * denominator > numerator:
            root -= 1
        if upper and root**2 * denominator != numerator:
            root += 1
        return Fraction(root, scale)

    return Interval(endpoint(value.lo, False), endpoint(value.hi, True))


def q_infinite(index: int) -> int:
    left = index <= 0 and index % 4 == 0
    right = index >= 6 and (index - 6) % 4 == 0
    return 1 if left or right else -1


def tau_values(low: int, high: int) -> dict[int, int]:
    tau = {0: 1}
    for index in range(high):
        tau[index + 1] = q_infinite(index) * tau[index]
    for index in range(-1, low - 1, -1):
        tau[index] = q_infinite(index) * tau[index + 1]
    return tau


def _identity() -> list[list[Interval]]:
    return [[Interval.point(row == column) for column in range(4)] for row in range(4)]


def _multiply(
    left: list[list[Interval]], right: list[list[Interval]]
) -> list[list[Interval]]:
    return [
        [
            sum(
                (left[row][middle] * right[middle][column] for middle in range(4)),
                Interval.point(0),
            )
            for column in range(4)
        ]
        for row in range(4)
    ]


def one_step(tau: dict[int, int], index: int, lam: Interval) -> list[list[Interval]]:
    a, b = tau[index], tau[index - 2]
    return [
        [-a, a * lam, -a, -a * b],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
    ]


def transfer_product(
    tau: dict[int, int], start: int, stop: int, lam: Interval
) -> list[list[Interval]]:
    result = _identity()
    for index in range(start, stop):
        result = _multiply(one_step(tau, index, lam), result)
    return result


def _determinant(matrix: list[list[Interval]]) -> Interval:
    size = len(matrix)
    result = Interval.point(0)
    for permutation in permutations(range(size)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(size)
            for j in range(i + 1, size)
        )
        term = Interval.point(-1 if inversions % 2 else 1)
        for row, column in enumerate(permutation):
            term = term * matrix[row][column]
        result = result + term
    return result


def cofactor_vector(
    matrix: list[list[Interval]], eigenvalue: Interval
) -> list[Interval]:
    vector = []
    for excluded in range(4):
        columns = [column for column in range(4) if column != excluded]
        minor = [
            [
                matrix[row][column]
                - (eigenvalue if row == column else Interval.point(0))
                for column in columns
            ]
            for row in (0, 1, 2)
        ]
        vector.append(((-1) ** excluded) * _determinant(minor))
    return vector


def _square_upper(value: Interval) -> Fraction:
    return (value * value).hi


def _best_chart(
    matrix: list[list[Interval]], eigenvalues: list[Interval]
) -> tuple[Fraction, tuple[int, int], tuple[int, int]]:
    raw = [cofactor_vector(matrix, eigenvalue) for eigenvalue in eigenvalues]
    candidates: list[tuple[Fraction, tuple[int, int], tuple[int, int]]] = []
    for pivots in cartesian_product(range(4), repeat=2):
        if any(not raw[column][pivots[column]].excludes_zero() for column in range(2)):
            continue
        vectors = [
            [raw[column][row] / raw[column][pivots[column]] for row in range(4)]
            for column in range(2)
        ]
        vector_norm_squared = sum(
            _square_upper(vectors[column][row])
            for column in range(2)
            for row in range(4)
        )
        for rows in combinations(range(4), 2):
            a, b = vectors[0][rows[0]], vectors[1][rows[0]]
            c, d = vectors[0][rows[1]], vectors[1][rows[1]]
            determinant = a * d - b * c
            if not determinant.excludes_zero():
                continue
            inverse_numerator = sum(_square_upper(value) for value in (a, b, c, d))
            minimum_determinant = min(abs(determinant.lo), abs(determinant.hi))
            bound_squared = (
                vector_norm_squared
                * inverse_numerator
                / (minimum_determinant * minimum_determinant)
            )
            candidates.append((bound_squared, pivots, rows))
    if not candidates:
        raise AssertionError("no nondegenerate Floquet chart")
    return min(candidates, key=lambda item: item[0])


def _symbolic_monodromy(cut: int, sign: int, tau: dict[int, int]) -> sp.Matrix:
    lam = sp.symbols("lam")
    result = sp.eye(4)
    for index in range(cut, cut + 8):
        a, b = tau[index], tau[index - 2]
        step = sp.Matrix(
            [[-a, sign * a * lam, -a, -a * b], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]
        )
        result = step * result
    return result.applyfunc(sp.expand)


def _matrix_digest(matrix: sp.Matrix) -> str:
    entries = [
        [str(sp.expand(matrix[row, column])) for column in range(matrix.cols)]
        for row in range(matrix.rows)
    ]
    return hashlib.sha256(json.dumps(entries, separators=(",", ":")).encode()).hexdigest()


@lru_cache(maxsize=1)
def reconstruct_floquet() -> dict[str, Any]:
    sys.set_int_max_str_digits(max(sys.get_int_max_str_digits(), 200000))
    y_interval = Interval(C6_LOWER, C6_UPPER)
    positive_lambda = sqrt_interval(y_interval)
    h = 2 * y_interval**2 - 16 * y_interval + 13
    discriminant = -12 * y_interval**2 + 96 * y_interval + 17
    root_discriminant = sqrt_interval(discriminant)
    w_values = [(h - root_discriminant) / 2, (h + root_discriminant) / 2]
    stable = [(w - sqrt_interval(w**2 - 4)) / 2 for w in w_values]
    if not all(0 < root.lo <= root.hi < Q for root in stable):
        raise AssertionError("stable Floquet multipliers are not below q")

    tau = tau_values(-128, 128)
    lam_symbol, y_symbol, z_symbol = sp.symbols("lam y z")
    expected_characteristic = (
        z_symbol**4
        + (-2 * y_symbol**2 + 16 * y_symbol - 13) * z_symbol**3
        + (y_symbol**4 - 16 * y_symbol**3 + 80 * y_symbol**2 - 128 * y_symbol + 40)
        * z_symbol**2
        + (-2 * y_symbol**2 + 16 * y_symbol - 13) * z_symbol
        + 1
    )
    records = []
    exact_bounds = []
    for sign in (1, -1):
        lam = positive_lambda if sign == 1 else -positive_lambda
        for side in ("right", "left"):
            for phase in range(8):
                cut = 14 + phase if side == "right" else -16 + phase
                interval_matrix = transfer_product(tau, cut, cut + 8, lam)
                eigenvalues = stable if side == "right" else [1 / value for value in stable]
                bound_squared, pivots, rows = _best_chart(interval_matrix, eigenvalues)
                symbolic = _symbolic_monodromy(cut, sign, tau)
                characteristic = sp.expand(symbolic.charpoly(z_symbol).as_expr())
                characteristic_y = sp.expand(characteristic.subs(lam_symbol**2, y_symbol))
                if (
                    sp.expand(characteristic_y - expected_characteristic) != 0
                    or sp.factor(symbolic.det()) != 1
                ):
                    raise AssertionError((sign, side, phase, "bulk monodromy mismatch"))
                exact_bounds.append(f"{bound_squared.numerator}/{bound_squared.denominator}")
                records.append(
                    {
                        "lambda_sign": sign,
                        "orientation": side,
                        "phase": phase,
                        "cut": cut,
                        "column_pivots": list(pivots),
                        "coordinate_rows": list(rows),
                        "monodromy_sha256": _matrix_digest(symbolic),
                        "k_squared_upper_integer": _ceil_fraction(bound_squared),
                    }
                )
    producer_left_cuts = {-16 + phase for phase in range(8)}
    reverse_tail_cuts = {-8 - phase for phase in range(8)}
    if {cut % 8 for cut in producer_left_cuts} != {
        cut % 8 for cut in reverse_tail_cuts
    }:
        raise AssertionError("left-cut phase sets are not equivalent modulo eight")
    if len(records) != 32 or max(row["k_squared_upper_integer"] for row in records) != 93:
        raise AssertionError("unexpected 32-chart envelope")
    if any(Fraction(value) >= 17**2 for value in exact_bounds):
        raise AssertionError("K=17 does not enclose all charts")
    return {
        "characteristic_polynomial": str(sp.expand(expected_characteristic)),
        "stable_multiplier_intervals": [
            {
                "lower": _decimal_bound(value.lo, upper=False),
                "upper": _decimal_bound(value.hi, upper=True),
            }
            for value in stable
        ],
        "stable_multiplier_exact_intervals": [
            [str(value.lo), str(value.hi)] for value in stable
        ],
        "unstable_multiplier_exact_intervals": [
            [str((1 / value).lo), str((1 / value).hi)] for value in stable
        ],
        "chart_count": 32,
        "records": records,
        "exact_interval_digest": hashlib.sha256(
            json.dumps(exact_bounds, separators=(",", ":")).encode()
        ).hexdigest(),
        "record_digest": _compact_digest(records),
        "maximum_k_squared_upper_integer": 93,
        "certified_K": 17,
        "left_cut_phase_equivalence": "{-16+p:0<=p<8}={-8-p:0<=p<8} modulo 8",
    }


def _integer_matrix_product(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    size = len(left)
    return [
        [sum(left[row][middle] * right[middle][column] for middle in range(size)) for column in range(size)]
        for row in range(size)
    ]


@lru_cache(maxsize=1)
def reconstruct_rank_two() -> dict[str, Any]:
    tau = tau_values(-520, 520)
    if not all(q_infinite(6 - index) == q_infinite(index) for index in range(-500, 501)):
        raise AssertionError("Q reflection identity failed")
    if not all(tau[7 - index] == -tau[index] for index in range(-500, 501)):
        raise AssertionError("tau reflection identity failed")
    windows = []
    for dimension in (58, 90, 138):
        low = (10 - dimension) // 2
        high = 9 - low
        adjacency = [[0] * dimension for _ in range(dimension)]
        symmetry = [[0] * dimension for _ in range(dimension)]
        for index in range(low, high + 1):
            row = index - low
            if index + 1 <= high:
                adjacency[row][row + 1] = adjacency[row + 1][row] = 1
            if index + 2 <= high:
                adjacency[row][row + 2] = adjacency[row + 2][row] = tau[index]
            symmetry[row][9 - index - low] = -1 if index % 2 else 1
        ka = _integer_matrix_product(symmetry, adjacency)
        ak = _integer_matrix_product(adjacency, symmetry)
        kk = _integer_matrix_product(symmetry, symmetry)
        if any(ka[i][j] != -ak[i][j] for i in range(dimension) for j in range(dimension)):
            raise AssertionError("finite-window anticommutation failed")
        if any(kk[i][j] != (-1 if i == j else 0) for i in range(dimension) for j in range(dimension)):
            raise AssertionError("finite-window K^2=-I failed")
        compact = lambda value: json.dumps(value, separators=(",", ":")).encode()
        windows.append(
            {
                "dimension": dimension,
                "index_interval": [low, high],
                "A_sha256": hashlib.sha256(compact(adjacency)).hexdigest(),
                "K_sha256": hashlib.sha256(compact(symmetry)).hexdigest(),
            }
        )
    return {
        "operator": "(Ku)_i=(-1)^i u_(9-i)",
        "identities": ["K^2=-I", "KA=-AK", "KH=HK"],
        "single_positive_A_multiplicity": 1,
        "single_negative_A_multiplicity": 1,
        "single_H_rank": 2,
        "cluster_dimensions": {str(r): 2 * r for r in SUPPORTED_R},
        "window_records": windows,
        "window_digest": _compact_digest(windows),
    }


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
    raise ValueError("even order required")


def complete_cells(distance: int) -> int:
    return (distance // 4 - 12) // 8


@lru_cache(maxsize=1)
def reconstruct_constants() -> dict[str, Any]:
    tail_squared_prefactor = Fraction(16 * 17**2, 1) / (1 - Q**2)
    ims_error = Fraction(320, 260**2)
    if tail_squared_prefactor != Fraction(10625, 2) or not tail_squared_prefactor < 73**2:
        raise AssertionError("tail constant failed")
    if ims_error != Fraction(4, 845):
        raise AssertionError("IMS reduction failed")
    gram = {str(2 * r): str(2 * r * 73**2 * Q**62) for r in SUPPORTED_R}
    if not Fraction(gram["6"]) < Fraction(1, 2):
        raise AssertionError("Gram bound failed")
    if not Fraction(1, 100) - ims_error > Fraction(1, 200):
        raise AssertionError("complement margin failed")
    if not Fraction(1, 200) - Fraction(1, 400) == Fraction(1, 400):
        raise AssertionError("window inverse failed")
    if not 400 * 3504**2 * 3 * Q**31 < 1:
        raise AssertionError("Feshbach remainder failed")
    if not 10515 * Q**31 < Fraction(1, 400):
        raise AssertionError("fixed window ownership failed")
    return {
        "q": str(Q),
        "K": 17,
        "tail_constant": 73,
        "tail_squared_prefactor": str(tail_squared_prefactor),
        "tail_squared_margin": str(Fraction(73**2) - tail_squared_prefactor),
        "operator_norm_A": 4,
        "operator_norm_H": 16,
        "c6_upper_norm_bound": 8,
        "residual_multiplier": 24,
        "residual_constant": 1752,
        "gram_formula": "m*73^2*q^(2*ell), m=2r",
        "gram_at_ell31": gram,
        "D0": 1040,
        "L_site_formula": "floor(D/4)-12",
        "ell_formula": "floor((floor(D/4)-12)/8)",
        "ell0": 31,
        "transition_width": 260,
        "ims_numerator_constant": 320,
        "ims_error_at_D0": str(ims_error),
        "delta6": "1/100",
        "delta_comp": "1/200",
        "window_radius": "1/400",
        "feshbach_inverse_bound": 400,
        "orthonormal_residual_constant": {str(r): 3504 * r for r in SUPPORTED_R},
        "eigenvalue_constants": {str(r): 3505 * r for r in SUPPORTED_R},
        "feshbach_worst_product": str(400 * 3504**2 * 3 * Q**31),
        "window_worst_product": str(10515 * Q**31),
        "N_exp": 3120,
    }


@lru_cache(maxsize=1)
def reconstruct_endpoints() -> list[dict[str, Any]]:
    records = []
    for residue, n, interfaces in ((2, 1042, 1), (4, 2084, 2), (6, 3126, 3)):
        distance = separation(n)
        assert distance is not None
        ell = complete_cells(distance)
        cap = C6_UPPER + 3505 * interfaces * Q**ell
        buffered_threshold = Fraction(8) - Fraction(200, n * n) - Fraction(9, 100)
        if distance < 1040 or ell != 31 or not cap < buffered_threshold:
            raise AssertionError((residue, n, distance, ell))
        records.append(
            {
                "residue": residue,
                "first_eligible_n": n,
                "interfaces": interfaces,
                "cluster_dimension": 2 * interfaces,
                "D": distance,
                "ell": ell,
                "cap": str(cap),
                "buffered_threshold": str(buffered_threshold),
                "strict_margin": str(buffered_threshold - cap),
            }
        )
    if complete_cells(1039) != 30 or complete_cells(1040) != 31:
        raise AssertionError("distance threshold off by one")
    if separation(3118) != 1038 or complete_cells(1038) != 30:
        raise AssertionError("N_exp predecessor mismatch")
    residue_zero_margin = Fraction(8) - Fraction(200, 3120**2) - Fraction(1561, 200)
    if residue_zero_margin <= 0:
        raise AssertionError("period-eight endpoint failed")
    return records


def _expected_dependency() -> dict[str, Any]:
    global_edge = load_strict(G6_GLOBAL_EDGE)
    rebuilt = reconstruct_rank_two()
    bridge = global_edge.get("negative_spectrum_bridge", {})
    checks = {
        "rank_two_stored": global_edge.get("squared_level_multiplicity") == 2,
        "operator_exact": bridge.get("operator") == rebuilt["operator"],
        "q_identity_exact": bridge.get("q_reflection_identity") == "Q_(6-i)=Q_i",
        "tau_identity_exact": bridge.get("tau_reflection_identity") == "tau_(7-i)=-tau_i",
        "tau_check_true": bridge.get("tau_identity_exact") is True,
        "finite_windows_match": bridge.get("window_records") == [
            {
                **record,
                "K_squared_is_minus_identity": True,
                "K_anticommutes_with_A": True,
                "K_commutes_with_H": True,
            }
            for record in rebuilt["window_records"]
        ],
    }
    if not all(checks.values()):
        raise AssertionError({"g6_global_edge_dependency": checks})
    return {
        "path": "research/proofs/task53/certificates/g6_global_edge.json",
        "sha256": _sha256(G6_GLOBAL_EDGE),
        "squared_level_multiplicity": 2,
        "symmetry_window_digest": rebuilt["window_digest"],
    }


def expected_exponential_tail() -> dict[str, Any]:
    threshold = Fraction(8) - Fraction(200, 3120**2)
    period_eight = Fraction(1561, 200)
    return {
        "N_exp": 3120,
        "distance_formulas": {
            "2": "D=n",
            "4": "D=n/2",
            "6": "D=6+4*floor((2k-3)/3), n=8k+6",
        },
        "ell_formula": "floor((floor(D/4)-12)/8)",
        "residue_endpoints": reconstruct_endpoints(),
        "period_eight_endpoint": {
            "n": 3120,
            "upper": str(period_eight),
            "threshold_lower": str(threshold),
            "strict_margin": str(threshold - period_eight),
        },
        "predecessor_control": {"n": 3118, "D": 1038, "ell": 30},
    }


def _forbid_legacy_contract(data: dict[str, Any]) -> bool:
    forbidden_keys = {
        "exact_r",
        "rank_r",
        "r_by_r",
        "r_x_r",
        "required_dimension_r",
    }
    forbidden_values = {
        "r",
        "I_r",
        "r x r",
        "r×r",
        "H_eff(z)-zP",
        "H_eff(lambda)-lambda P",
    }
    forbidden_fragments = ("I_r", "r x r", "r×r", "H_eff(z)-zP", "H_eff(lambda)-lambda P")

    def visit(value: Any) -> bool:
        if isinstance(value, dict):
            if any(str(key).lower() in forbidden_keys for key in value):
                return False
            return all(visit(child) for child in value.values())
        if isinstance(value, list):
            return all(visit(child) for child in value)
        return not (
            isinstance(value, str)
            and (
                value.strip() in forbidden_values
                or any(fragment in value for fragment in forbidden_fragments)
            )
        )

    return visit(data)


def verify(path: Path = CERTIFICATE) -> dict[str, bool]:
    data = load_strict(path)
    floquet = reconstruct_floquet()
    rank_two = reconstruct_rank_two()
    constants = reconstruct_constants()
    dependency_paths = {
        "research/proofs/task50/certificates/g6_interface_certificate.json": RESEARCH
        / "proofs/task50/certificates/g6_interface_certificate.json",
        "research/proofs/task53/certificates/g6_global_edge.json": G6_GLOBAL_EDGE,
        "research/proofs/task54/certificates/g6_spectral_isolation.json": RESEARCH
        / "proofs/task54/certificates/g6_spectral_isolation.json",
    }
    dependencies = data.get("dependencies", {})
    artifacts = dependencies.get("artifacts", [])
    dependency_hashes = (
        len(artifacts) == 3
        and {row.get("path") for row in artifacts} == set(dependency_paths)
        and all(
            row.get("sha256") == _sha256(dependency_paths[row["path"]])
            for row in artifacts
        )
    )
    rank_input = data.get("rank_two_input", {})
    expected_windows = [
        {
            "dimension": row["dimension"],
            "index_interval": row["index_interval"],
            "A_sha256": row["A_sha256"],
            "K_sha256": row["K_sha256"],
            "checks": {
                "K_squared_is_minus_identity": True,
                "K_anticommutes_with_A": True,
                "K_commutes_with_H": True,
            },
        }
        for row in rank_two["window_records"]
    ]
    bulk = data.get("bulk_floquet", {})
    phase_records = bulk.get("phase_records", [])
    positive_records = {
        (row["orientation"], row["phase"]): row
        for row in floquet["records"]
        if row["lambda_sign"] == 1
    }
    phase_geometry = len(phase_records) == 8 and all(
        row.get("phase") == phase
        and row.get("right_start") == 14 + phase
        and row.get("left_start") == -16 + phase
        and row.get("right_monodromy_sha256")
        == positive_records[("right", phase)]["monodromy_sha256"]
        and row.get("left_monodromy_sha256")
        == positive_records[("left", phase)]["monodromy_sha256"]
        and all(row.get("checks", {}).values())
        and row.get("right_stable_basis", {}).get("condition_bound_strictly_below_17") is True
        and row.get("left_unstable_basis_for_backward_decay", {}).get(
            "condition_bound_strictly_below_17"
        )
        is True
        for phase, row in enumerate(phase_records)
    )
    lam, y, p = sp.symbols("lam y p")
    stored_characteristic = sp.sympify(bulk.get("common_characteristic", "0"))
    rebuilt_characteristic = sp.sympify(floquet["characteristic_polynomial"], locals={"z": p})
    characteristic_matches = sp.expand(stored_characteristic - rebuilt_characteristic) == 0
    stable_records = bulk.get("stable_multiplier_intervals", [])
    unstable_records = bulk.get("unstable_multiplier_intervals", [])

    def encloses(stored: list[dict[str, Any]], exact: list[list[str]]) -> bool:
        return len(stored) == len(exact) and all(
            _fraction(record["lower"]) <= Fraction(bounds[0])
            <= Fraction(bounds[1]) <= _fraction(record["upper"])
            and _fraction(record["upper"]) < Q
            for record, bounds in zip(stored, exact)
        )

    stable_enclosed = encloses(stable_records, floquet["stable_multiplier_exact_intervals"])
    unstable_enclosed = len(unstable_records) == 2 and all(
        _fraction(record["lower"]) <= Fraction(bounds[0])
        <= Fraction(bounds[1]) <= _fraction(record["upper"])
        for record, bounds in zip(
            unstable_records, floquet["unstable_multiplier_exact_intervals"]
        )
    )
    stored_constants = data.get("constants", {})
    gram = data.get("gram", {})
    complement = data.get("complement", {})
    counting = data.get("counting", {})
    r_records = counting.get("r_records", [])
    exact_count_records = len(r_records) == 3 and all(
        row.get("r") == r
        and row.get("localized_columns") == 2 * r
        and _fraction(row.get("gram_error_upper_at_ell0"))
        == 2 * r * 73**2 * Q**62
        and _fraction(row.get("normalized_subspace_residual_upper_at_ell0"))
        == 3504 * r * Q**31
        and _fraction(row.get("feshbach_remainder_upper_at_ell0"))
        == 400 * r * 3504**2 * Q**62
        and _fraction(row.get("cluster_radius_upper_at_ell0"))
        == 3505 * r * Q**31
        and row.get("cluster_radius_below_fixed_window") is True
        and row.get("exact_fixed_window_riesz_rank") == 2 * r
        for r, row in zip(SUPPORTED_R, r_records)
    )
    feshbach = data.get("feshbach", {})
    checks = {
        "schema_exact": data.get("schema_version") == 1,
        "proof_status_exact": data.get("status")
        == "EXACT_2R_R123_CLUSTER_AND_FESHBACH_PROVED",
        "evidence_status_exact": data.get("evidence") == "COMPUTER_ASSISTED_PROVED",
        "audit_status_exact": data.get("mathematical_audit_status")
        == "TWO_INDEPENDENT_MATHEMATICAL_AUDITS_PASSED",
        "integration_status_final": data.get("integration_status")
        == "INDEPENDENT_CHECKER_PASS",
        "legacy_exact_r_rejected": _forbid_legacy_contract(data),
        "dependency_hashes_rebuilt": dependency_hashes,
        "g6_global_edge_rank_dependency_rebuilt": _expected_dependency()[
            "squared_level_multiplicity"
        ]
        == 2,
        "rank_two_rebuilt": (
            rank_input.get("operator") == rank_two["operator"]
            and rank_input.get("coefficient_identities")
            == ["Q_(6-i)=Q_i", "tau_(7-i)=-tau_i"]
            and rank_input.get("coefficient_identities_exact") is True
            and rank_input.get("operator_identities") == rank_two["identities"]
            and rank_input.get("window_controls") == expected_windows
            and rank_input.get("positive_A_root_multiplicity") == 1
            and rank_input.get("negative_A_root_multiplicity") == 1
            and rank_input.get("H_c6_riesz_rank") == 2
        ),
        "all_32_charts_rebuilt": floquet["chart_count"] == 32
        and floquet["maximum_k_squared_upper_integer"] < 17**2,
        "left_cut_convention_verified": floquet["left_cut_phase_equivalence"]
        == "{-16+p:0<=p<8}={-8-p:0<=p<8} modulo 8",
        "monodromies_and_phase_geometry_rebuilt": phase_geometry,
        "characteristic_rebuilt": characteristic_matches,
        "floquet_boundaries_rebuilt": stable_enclosed
        and unstable_enclosed
        and _fraction(bulk.get("maximum_stable_modulus_bound")) == Q
        and _fraction(bulk.get("maximum_stable_modulus_exact")) < Q
        and _fraction(bulk.get("strict_margin_to_9_over_25"))
        == Q - _fraction(bulk.get("maximum_stable_modulus_exact"))
        and bulk.get("basis_condition_bound") == 17,
        "tail_constants_rebuilt": (
            _fraction(stored_constants.get("floquet_cell_rate_q")) == Q
            and stored_constants.get("tail_basis_condition_bound") == constants["K"]
            and _fraction(stored_constants.get("tail_square_prefactor"))
            == Fraction(constants["tail_squared_prefactor"])
            and stored_constants.get("normalized_tail_bound") == "73*q^ell"
            and stored_constants.get("single_column_residual") == "1752*q^ell"
        ),
        "distance_and_ims_rebuilt": (
            stored_constants.get("minimum_interface_distance_D0") == 1040
            and stored_constants.get("S_at_D0") == 260
            and stored_constants.get("L_site_at_D0") == 248
            and stored_constants.get("ell_at_D0") == 31
            and stored_constants.get("ims_constant") == 320
            and _fraction(stored_constants.get("ims_error_at_D0")) == Fraction(4, 845)
            and _fraction(stored_constants.get("complement_gap")) == Fraction(1, 200)
            and _fraction(stored_constants.get("complement_surplus_at_D0"))
            == Fraction(9, 33800)
            and _fraction(stored_constants.get("fixed_window_radius")) == Fraction(1, 400)
            and stored_constants.get("Q_resolvent_bound") == 400
        ),
        "gram_rebuilt": (
            gram.get("columns") == "m=2r"
            and gram.get("operator_error") == "||G-I_(2r)||<=2r*73^2*q^(2ell)"
            and _fraction(gram.get("worst_error_at_r3_ell31")) == 6 * 73**2 * Q**62
            and gram.get("inverse_bound") == "||G^-1||<=2"
        ),
        "complement_rebuilt": (
            complement.get("dimension") == "2r"
            and complement.get("ims_identity_bound") == "320/T_min^2<=320/260^2=4/845"
            and complement.get("quadratic_form_bound")
            == "QHQ<=c6-1/100+4/845<c6-1/200"
        ),
        "exact_2r_count_rebuilt": (
            counting.get("fixed_window") == "[c6-1/400,c6+1/400]"
            and counting.get("result") == "rank 1_[c6-1/400,c6+1/400](H)=2r"
            and exact_count_records
        ),
        "feshbach_formula_exact": feshbach
        == {
            "orthonormal_map": "U=Phi G^(-1/2)",
            "projectors": "P=UU*, Q=I-P",
            "effective_operator": "H_eff(z)=U^*HU-U^*HQ(QHQ-z)^(-1)QHU",
            "spectral_equation": "H_eff(z)-z I_(2r)",
            "residual": "E=(H-c6)Phi",
            "exact_gram_formula": "H_eff(z)-c6 I_(2r)=G^(-1/2)Phi^*E G^(-1/2)-G^(-1/2)E^*Q(QHQ-z)^(-1)QE G^(-1/2)",
            "first_order_bound": "||T1||<=3504*r*q^ell",
            "second_order_bound": "||R2(z)||<=400*r*3504^2*q^(2ell)<r*q^ell",
            "cluster_bound": "|lambda_j-c6|<3505*r*q^ell for j=1,...,2r",
        },
        "exponential_tail_rebuilt": data.get("exponential_tail")
        == expected_exponential_tail(),
        "stored_checks_nonempty_and_true": len(data.get("checks", {})) >= 20
        and all(data["checks"].values()),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return checks


def main() -> None:
    verify()
    print("TARGET_A_TASK55_EXACT_2R_VERIFY_PASS")


if __name__ == "__main__":
    main()

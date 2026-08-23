"""Independent verifier for the Task 55 exact small-order classification.

The checker deliberately does not import the producer.  Floating point is not
used anywhere on an accepting path: local-window decisions use rational
brackets for the algebraic threshold and fraction-free Sylvester tests, while
terminal states use exact integer Rayleigh quotients or an exact optimizer
factorization.
"""

from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable

import sympy as sp


RESEARCH = Path(__file__).resolve().parents[1]
CERTIFICATE = (
    RESEARCH
    / "proofs"
    / "task55"
    / "certificates"
    / "small_order_exact_classification.json"
)

ORDER_SUPPORT = {34: 12, 36: 13, 38: 14, 42: 14, 44: 14, 46: 14}
EXPECTED = {
    34: (124, 1, 1, 2),
    36: (128, 1, 1, 2),
    38: (184, 77, 3, 6),
    42: (232, 337, 7, 14),
    44: (240, 353, 10, 20),
    46: (240, 599, 10, 20),
}
EXPECTED_AUTOMATON_STATES = {34: 92, 36: 92, 38: 132, 42: 166, 44: 171, 46: 171}
EXPECTED_ROOTED_ODD = {34: 0, 36: 4, 38: 38, 42: 392, 44: 620, 46: 690}
EXPECTED_BRACELETS = {
    34: 126390032,
    36: 477353376,
    38: 1808676326,
    42: 26179922024,
    44: 99957747388,
    46: 382443112538,
}
X = sp.Symbol("x")
_WINDOW_TABLE_CACHE: dict[tuple[int, str], list[tuple[int, int]]] = {}


@dataclass(frozen=True)
class Threshold:
    n: int
    polynomial: tuple[int, ...]
    lower: Fraction
    upper: Fraction


@dataclass(frozen=True)
class Reconstruction:
    thresholds: dict[int, Threshold]
    allowed_windows: dict[int, tuple[int, ...]]
    rooted_walks: dict[int, tuple[int, ...]]
    canonical_classes: dict[int, tuple[int, ...]]
    unresolved_windows: dict[int, int]
    automaton_states: dict[int, int]
    rooted_odd_counts: dict[int, int]


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def _strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_float(value: str) -> None:
    raise ValueError(f"floating JSON number is forbidden: {value}")


def _parse_int(value: str) -> int:
    if len(value.lstrip("-")) > 200:
        raise ValueError("oversized JSON integer")
    return int(value)


def load_strict(path: Path = CERTIFICATE) -> dict[str, Any]:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raise ValueError("JSON BOM is forbidden")
    if b"\r" in raw:
        raise ValueError("JSON must use LF line endings")
    try:
        text = raw.decode("ascii")
    except UnicodeDecodeError as exc:
        raise ValueError("certificate JSON must be ASCII") from exc
    data = json.loads(
        text,
        object_pairs_hook=_strict_object,
        parse_float=_reject_float,
        parse_int=_parse_int,
        parse_constant=_reject_float,
    )
    if not isinstance(data, dict):
        raise ValueError("certificate root must be an object")
    return data


def _fraction(value: Any, label: str) -> Fraction:
    _require(type(value) is str, f"{label} must be a rational string")
    try:
        result = Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise AssertionError(f"invalid rational in {label}") from exc
    accepted_forms = {
        str(result),
        f"{result.numerator}/{result.denominator}",
    }
    _require(value in accepted_forms, f"{label} is not in canonical rational form")
    return result


def _int_list(value: Any, label: str, *, length: int | None = None) -> list[int]:
    _require(type(value) is list, f"{label} must be a list")
    _require(all(type(item) is int for item in value), f"{label} must contain integers")
    if length is not None:
        _require(len(value) == length, f"{label} has the wrong length")
    return value


def _stream_sha256(values: Iterable[Any]) -> str:
    digest = hashlib.sha256()
    for value in values:
        digest.update(
            (json.dumps(value, ensure_ascii=True, separators=(",", ":")) + "\n").encode(
                "ascii"
            )
        )
    return digest.hexdigest()


def _digest(value: Any) -> str:
    payload = (
        json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":"))
        + "\n"
    ).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def _threshold(n: int) -> Threshold:
    """Isolate rho_-(n)^2 as the largest real conjugate, exactly.

    Writing c=cos(2*pi*k/n), every conjugate has value 2+2c+4c^2.
    For the admissible cyclotomic conjugates, k=+/-1 gives the unique largest
    value: the quadratic is increasing on [-1/4,1], while its values on
    [-1,-1/4] are at most 4, far below the k=1 value for these six orders.
    Thus the rightmost real interval of the exact minimal polynomial identifies
    the required threshold without a numerical root-selection decision.
    """

    expression = 4 + 2 * sp.cos(2 * sp.pi / n) + 2 * sp.cos(4 * sp.pi / n)
    polynomial = sp.Poly(sp.minimal_polynomial(expression, X), X, domain=sp.QQ)
    _require(polynomial.LC() == 1, f"n={n}: threshold polynomial is not monic")
    coefficients = tuple(int(value) for value in polynomial.all_coeffs())
    _require(
        all(sp.Integer(value) == value for value in polynomial.all_coeffs()),
        f"n={n}: threshold polynomial is not integral",
    )
    intervals = polynomial.intervals(eps=sp.Rational(1, 10**10))
    _require(
        sum(multiplicity for _interval, multiplicity in intervals) == polynomial.degree(),
        f"n={n}: threshold polynomial is not totally real",
    )
    (left, right), multiplicity = intervals[-1]
    _require(multiplicity == 1, f"n={n}: rightmost threshold root is not simple")
    _require(
        polynomial.count_roots(left, right) == 1,
        f"n={n}: threshold interval does not isolate one root",
    )
    _require(polynomial.eval(left) * polynomial.eval(right) < 0, f"n={n}: bad endpoint signs")
    lower = Fraction(int(left.p), int(left.q))
    upper = Fraction(int(right.p), int(right.q))
    _require(Fraction(7) < lower < upper < Fraction(8), f"n={n}: bad threshold range")
    return Threshold(n, coefficients, lower, upper)


def _local_gram(code: int, support: int) -> list[list[int]]:
    """Build C_Q^T C_Q from the open-line four-term operator."""

    width = support + 1
    _require(0 <= code < 1 << width, "local-window code out of range")
    q = [1 if (code >> index) & 1 else -1 for index in range(width)]

    # q[index] represents Q_{index-2}; tau[index] represents tau_{index-2}.
    tau = [1]
    for sign in q:
        tau.append(tau[-1] * sign)

    # Inputs are 0,...,support-1 and Av can occupy -2,...,support+1.
    c_matrix = [[0] * support for _ in range(support + 4)]
    for output in range(-2, support + 2):
        for input_index in (output - 1, output + 1):
            if 0 <= input_index < support:
                c_matrix[output + 2][input_index] += 1
        input_index = output - 2
        if 0 <= input_index < support:
            c_matrix[output + 2][input_index] += tau[output]
        input_index = output + 2
        if 0 <= input_index < support:
            c_matrix[output + 2][input_index] += tau[output + 2]

    return [
        [
            sum(c_matrix[row][left] * c_matrix[row][right] for row in range(support + 4))
            for right in range(support)
        ]
        for left in range(support)
    ]


def _rational_shift_positive_definite(
    matrix: list[list[int]], endpoint: Fraction
) -> bool:
    """Apply fraction-free Sylvester to endpoint*I-matrix."""

    size = len(matrix)
    numerator, denominator = endpoint.numerator, endpoint.denominator
    active = [
        [
            (numerator if row == column else 0) - denominator * matrix[row][column]
            for column in range(size)
        ]
        for row in range(size)
    ]
    previous = 1
    for pivot_index in range(size):
        pivot = active[pivot_index][pivot_index]
        if pivot <= 0:
            return False
        for row in range(pivot_index + 1, size):
            row_entry = active[row][pivot_index]
            for column in range(row, size):
                value = (
                    pivot * active[row][column]
                    - row_entry * active[column][pivot_index]
                )
                quotient, remainder = divmod(value, previous)
                _require(remainder == 0, "fraction-free Sylvester division failed")
                active[row][column] = active[column][row] = quotient
        previous = pivot
    return True


def _classify_window(matrix: list[list[int]], threshold: Threshold) -> str:
    if _rational_shift_positive_definite(matrix, threshold.lower):
        return "ALLOWED"
    if not _rational_shift_positive_definite(matrix, threshold.upper):
        return "EXCLUDED"
    return "UNRESOLVED"


def _rooted_even_closed_walks(
    n: int, support: int, allowed_windows: tuple[int, ...]
) -> tuple[tuple[int, ...], int, int]:
    mask = (1 << support) - 1
    adjacency: dict[int, list[tuple[int, int]]] = {}
    states: set[int] = set()
    for window in allowed_windows:
        source = window & mask
        bit = (window >> support) & 1
        target = (source >> 1) | (bit << (support - 1))
        states.update((source, target))
        adjacency.setdefault(source, []).append((target, bit))
    for edges in adjacency.values():
        edges.sort()

    words: set[int] = set()
    odd_count = 0
    for start in sorted(states):
        def visit(state: int, depth: int, word: int, parity: int) -> None:
            nonlocal odd_count
            if depth == n:
                if state == start:
                    if parity == 0:
                        words.add(word)
                    else:
                        odd_count += 1
                return
            for target, bit in adjacency.get(state, ()):
                visit(target, depth + 1, word | (bit << depth), parity ^ bit)

        visit(start, 0, 0, 0)
    return tuple(sorted(words)), len(states), odd_count


def _canonical_q_code(code: int, n: int) -> int:
    mask = (1 << n) - 1
    reverse = sum(((code >> index) & 1) << (n - 1 - index) for index in range(n))
    candidates: list[int] = []
    for source in (code, reverse):
        for shift in range(n):
            rotated = source if shift == 0 else ((source >> shift) | (source << (n - shift))) & mask
            candidates.append(rotated)
    return min(candidates)


@lru_cache(maxsize=1)
def reconstruct() -> Reconstruction:
    thresholds = {n: _threshold(n) for n in ORDER_SUPPORT}
    allowed: dict[int, list[int]] = {n: [] for n in ORDER_SUPPORT}
    unresolved: dict[int, int] = {n: 0 for n in ORDER_SUPPORT}

    by_support: dict[int, list[int]] = {}
    for n, support in ORDER_SUPPORT.items():
        by_support.setdefault(support, []).append(n)
    for support, orders in sorted(by_support.items()):
        for code in range(1 << (support + 1)):
            matrix = _local_gram(code, support)
            for n in orders:
                decision = _classify_window(matrix, thresholds[n])
                if decision == "ALLOWED":
                    allowed[n].append(code)
                elif decision == "UNRESOLVED":
                    unresolved[n] += 1

    allowed_tuples = {n: tuple(codes) for n, codes in allowed.items()}
    walk_data = {
        n: _rooted_even_closed_walks(n, ORDER_SUPPORT[n], allowed_tuples[n])
        for n in ORDER_SUPPORT
    }
    walks = {n: walk_data[n][0] for n in ORDER_SUPPORT}
    state_counts = {n: walk_data[n][1] for n in ORDER_SUPPORT}
    odd_counts = {n: walk_data[n][2] for n in ORDER_SUPPORT}
    classes = {
        n: tuple(sorted({_canonical_q_code(code, n) for code in walks[n]}))
        for n in ORDER_SUPPORT
    }
    return Reconstruction(
        thresholds,
        allowed_tuples,
        walks,
        classes,
        unresolved,
        state_counts,
        odd_counts,
    )


def _even_binary_bracelets(length: int) -> int:
    rotation_fixed = 0
    for shift in range(length):
        cycles = math.gcd(length, shift)
        cycle_length = length // cycles
        rotation_fixed += 1 << cycles if cycle_length % 2 == 0 else 1 << (cycles - 1)
    reflection_fixed = length * (1 << (length // 2))
    quotient, remainder = divmod(rotation_fixed + reflection_fixed, 2 * length)
    _require(remainder == 0, "Burnside quotient is not integral")
    return quotient


def _verify_window_tables(data: dict[str, Any]) -> dict[int, list[tuple[int, int]]]:
    tables = data.get("window_tables")
    _require(type(tables) is list and len(tables) == 3, "window tables missing")
    _require(
        [table.get("support_length") for table in tables if type(table) is dict]
        == [12, 13, 14],
        "window tables are missing, duplicated, or out of order",
    )
    quotients: dict[int, list[tuple[int, int]]] = {}
    for table in tables:
        support = table["support_length"]
        _require(
            set(table)
            == {
                "support_length",
                "q_window_length",
                "row_schema",
                "all_window_count",
                "rows_sha256",
                "rows",
            },
            f"support={support}: unexpected window-table schema",
        )
        _require(table["q_window_length"] == support + 1, "Q-window length mismatch")
        _require(
            table["row_schema"]
            == ["window_code", "numerator", "denominator", "integer_vector"],
            "window row schema mismatch",
        )
        expected_count = 1 << (support + 1)
        _require(table["all_window_count"] == expected_count, "all-window count mismatch")
        rows = table["rows"]
        _require(type(rows) is list and len(rows) == expected_count, "window rows incomplete")
        actual_rows_sha256 = _stream_sha256(rows)
        _require(table["rows_sha256"] == actual_rows_sha256, "window row hash mismatch")
        cache_key = (support, actual_rows_sha256)
        if cache_key in _WINDOW_TABLE_CACHE:
            quotients[support] = _WINDOW_TABLE_CACHE[cache_key]
            continue

        table_quotients: list[tuple[int, int]] = []
        for expected_code, row in enumerate(rows):
            _require(type(row) is list and len(row) == 4, "malformed window row")
            code, numerator, denominator, raw_vector = row
            _require(code == expected_code, "window rows are missing, duplicated, or out of order")
            _require(type(numerator) is int and type(denominator) is int, "window quadratic is not integral")
            vector = _int_list(raw_vector, "window vector", length=support)
            _require(any(vector), "window vector is zero")
            _require(max(abs(value) for value in vector) <= 10**9, "window vector is oversized")
            _require(math.gcd(*(abs(value) for value in vector)) == 1, "window vector is not primitive")
            _require(next(value for value in vector if value) > 0, "window vector sign is not canonical")
            matrix = _local_gram(code, support)
            rebuilt_numerator = sum(
                vector[left] * matrix[left][right] * vector[right]
                for left in range(support)
                for right in range(support)
            )
            rebuilt_denominator = sum(value * value for value in vector)
            _require(numerator == rebuilt_numerator, "window numerator mismatch")
            _require(denominator == rebuilt_denominator, "window denominator mismatch")
            _require(denominator > 0, "window denominator is not positive")
            table_quotients.append((numerator, denominator))
        quotients[support] = table_quotients
        _WINDOW_TABLE_CACHE[cache_key] = table_quotients
    return quotients


def _verify_threshold_record(
    record: Any, threshold: Threshold
) -> tuple[Fraction, Fraction]:
    n = threshold.n
    _require(type(record) is dict, f"n={n}: threshold record missing")
    _require(
        record.get("definition") == "4*(cos(pi/n)^2+cos(2*pi/n)^2)",
        f"n={n}: threshold definition mismatch",
    )
    coefficients = record.get("minimal_polynomial_coefficients")
    _require(
        type(coefficients) is list
        and all(type(value) is str for value in coefficients)
        and coefficients == [str(value) for value in threshold.polynomial],
        f"n={n}: threshold polynomial mismatch",
    )
    lower = _fraction(record.get("strict_rational_lower"), f"n={n} threshold lower")
    upper = _fraction(record.get("strict_rational_upper"), f"n={n} threshold upper")
    _require(
        threshold.lower < lower < upper < threshold.upper,
        f"n={n}: stored threshold interval misses the independently isolated root",
    )
    polynomial = sp.Poly.from_list(list(threshold.polynomial), gens=X)
    sympy_lower = sp.Rational(lower.numerator, lower.denominator)
    sympy_upper = sp.Rational(upper.numerator, upper.denominator)
    _require(polynomial.count_roots(sympy_lower, sympy_upper) == 1, f"n={n}: stored threshold interval does not isolate a root")
    _require(polynomial.eval(sympy_lower) * polynomial.eval(sympy_upper) < 0, f"n={n}: stored threshold endpoint signs fail")
    _require(
        record.get("exact_endpoint_sign_checks")
        == {"theta_minus_lower": 1, "upper_minus_theta": 1},
        f"n={n}: stored endpoint checks mismatch",
    )
    return lower, upper


def _adjacency_image(q_code: int, n: int, alpha: int, vector: list[int]) -> list[int]:
    _require(alpha in (-1, 1), "alpha must be -1 or +1")
    _require(q_code.bit_count() % 2 == 0, "Q word has odd parity")
    q = [1 if (q_code >> index) & 1 else -1 for index in range(n)]
    tau = [1]
    for index in range(n - 1):
        tau.append(tau[-1] * q[index])
    _require(tau[-1] * q[-1] == 1, "Q word does not close")
    step_one = [1] * n
    step_one[-1] = alpha
    step_two = [
        tau[index] * step_one[index] * step_one[(index + 1) % n]
        for index in range(n)
    ]
    image = [0] * n
    for index in range(n):
        for distance, sign in ((1, step_one[index]), (2, step_two[index])):
            target = (index + distance) % n
            image[index] += sign * vector[target]
            image[target] += sign * vector[index]
    return image


@lru_cache(maxsize=None)
def _optimizer_check(n: int, threshold: Threshold) -> dict[str, Any]:
    q_code = 0
    alpha = -1
    basis_vectors = []
    for column in range(n):
        vector = [0] * n
        vector[column] = 1
        basis_vectors.append(_adjacency_image(q_code, n, alpha, vector))
    adjacency = sp.Matrix.hstack(*(sp.Matrix(column) for column in basis_vectors))
    square_polynomial = sp.Poly((adjacency * adjacency).charpoly(X).as_expr(), X)
    threshold_polynomial = sp.Poly.from_list(list(threshold.polynomial), gens=X)
    quotient = square_polynomial
    exponent = 0
    while True:
        divided, remainder = sp.div(quotient, threshold_polynomial)
        if remainder.as_expr() != 0:
            break
        quotient = divided
        exponent += 1
    _require(exponent >= 1, f"n={n}: optimizer misses the threshold factor")
    lower = sp.Rational(threshold.lower.numerator, threshold.lower.denominator)
    upper = sp.Rational(threshold.upper.numerator, threshold.upper.denominator)
    square_intervals = square_polynomial.intervals(eps=sp.Rational(1, 10**10))
    threshold_intervals = [
        (interval, multiplicity)
        for interval, multiplicity in square_intervals
        if interval[0] < upper and lower < interval[1]
    ]
    _require(
        len(threshold_intervals) == 1
        and threshold_intervals[0] == square_intervals[-1]
        and threshold_intervals[0][1] == exponent,
        f"n={n}: threshold is not the optimizer's largest squared eigenvalue",
    )
    charpoly_text = str(square_polynomial.as_expr())
    return {
        "threshold_factor_multiplicity": exponent,
        "largest_root_multiplicity": threshold_intervals[0][1],
        "charpoly_A2": charpoly_text,
        "charpoly_A2_sha256": hashlib.sha256((charpoly_text + "\n").encode("ascii")).hexdigest(),
    }


def _verify_terminal(
    record: dict[str, Any],
    n: int,
    q_code: int,
    alpha: int,
    threshold: Threshold,
    stored_threshold_upper: Fraction,
) -> dict[str, Any]:
    _require(type(record) is dict, "terminal record must be an object")
    _require(type(record.get("canonical_q_code")) is int, "terminal Q is not an integer")
    _require(record.get("canonical_q_code") == q_code, "terminal Q mismatch")
    _require(
        record.get("q_bits")
        == "".join("1" if (q_code >> index) & 1 else "0" for index in range(n)),
        "terminal Q bits mismatch",
    )
    _require(type(record.get("alpha")) is int, "terminal alpha is not an integer")
    _require(record.get("alpha") == alpha, "terminal alpha mismatch")
    unhashed = {key: value for key, value in record.items() if key != "record_sha256"}
    _require(record.get("record_sha256") == _digest(unhashed), "terminal record hash mismatch")
    if q_code == 0 and alpha == -1:
        _require(record.get("status") == "EXACT_THRESHOLD_EIGENVALUE", "optimizer status mismatch")
        check = _optimizer_check(n, threshold)
        _require(
            record.get("conclusion")
            == "rho(A)^2 is at least the conjectured threshold squared",
            "optimizer conclusion mismatch",
        )
        _require(
            record.get("threshold_minpoly_divides_charpoly_A2") is True,
            "optimizer divisibility flag mismatch",
        )
        _require(
            record.get("threshold_multiplicity_in_charpoly_A2")
            == check["threshold_factor_multiplicity"],
            "optimizer multiplicity mismatch",
        )
        _require(
            record.get("threshold_minpoly_coefficients")
            == [str(value) for value in threshold.polynomial],
            "optimizer threshold polynomial mismatch",
        )
        _require(record.get("charpoly_A2") == check["charpoly_A2"], "optimizer charpoly mismatch")
        _require(record.get("charpoly_A2_sha256") == check["charpoly_A2_sha256"], "optimizer charpoly hash mismatch")
        _require(record.get("threshold_upper_is_strictly_above_equality") is True, "optimizer upper-bound flag mismatch")
        _require(_fraction(record.get("threshold_upper"), "optimizer threshold upper") == stored_threshold_upper, "optimizer threshold upper mismatch")
        return {"method": "EXACT_THRESHOLD_EIGENVALUE", **check}

    vector = _int_list(record.get("integer_vector"), "terminal vector", length=n)
    _require(any(vector), "terminal vector is zero")
    _require(max(abs(value) for value in vector) <= 10**12, "terminal vector is oversized")
    _require(math.gcd(*(abs(value) for value in vector)) == 1, "terminal vector is not primitive")
    first = next(value for value in vector if value)
    _require(first > 0, "terminal vector has noncanonical sign")
    image = _adjacency_image(q_code, n, alpha, vector)
    numerator = sum(value * value for value in image)
    denominator = sum(value * value for value in vector)
    bound = Fraction(numerator, denominator)
    _require(bound > stored_threshold_upper, "terminal Rayleigh quotient does not clear certified threshold")
    _require(record.get("status") == "EXACT_INTEGER_RAYLEIGH_ABOVE_THRESHOLD_UPPER", "terminal status mismatch")
    _require(type(record.get("numerator")) is int, "terminal numerator is not an integer")
    _require(type(record.get("denominator")) is int, "terminal denominator is not an integer")
    _require(record.get("numerator") == numerator, "terminal numerator mismatch")
    _require(record.get("denominator") == denominator, "terminal denominator mismatch")
    _require(_fraction(record.get("quotient"), "terminal Rayleigh quotient") == bound, "terminal quotient mismatch")
    _require(
        _fraction(record.get("strict_margin_over_threshold_upper"), "terminal strict margin")
        == bound - stored_threshold_upper,
        "terminal strict margin mismatch",
    )
    return {"method": "INTEGER_RAYLEIGH", "numerator": numerator, "denominator": denominator}


def verify(path: Path = CERTIFICATE) -> dict[str, Any]:
    data = load_strict(path)
    rebuilt = reconstruct()
    _require(type(data.get("schema_version")) is int and data["schema_version"] == 1, "schema version mismatch")
    _require(
        data.get("status") == "TASK55_SMALL_ORDER_EXACT_CLASSIFICATION_PRODUCED",
        "producer status mismatch",
    )
    _require(
        data.get("evidence_status")
        == "EXACT_FINITE_PRODUCER; INDEPENDENT_CHECKER_REQUIRED_FOR_UPGRADE",
        "producer evidence boundary mismatch",
    )
    _require(
        type(data.get("arithmetic_boundary")) is str
        and "integer quadratic forms and exact Fraction comparisons" in data["arithmetic_boundary"],
        "arithmetic boundary mismatch",
    )
    producer_relative = "research/scripts/target_a_task55_small_order_exact.py"
    producer_path = RESEARCH.parent / producer_relative
    _require(data.get("producer_path") == producer_relative, "producer path mismatch")
    _require(
        data.get("producer_sha256") == hashlib.sha256(producer_path.read_bytes()).hexdigest(),
        "producer hash mismatch",
    )
    core = {key: value for key, value in data.items() if key != "payload_core_sha256"}
    _require(data.get("payload_core_sha256") == _digest(core), "payload core hash mismatch")

    window_quotients = _verify_window_tables(data)
    orders = data.get("orders")
    _require(type(orders) is list, "orders must be a list")
    _require([row.get("n") for row in orders if type(row) is dict] == list(ORDER_SUPPORT), "orders are missing, duplicated, or out of order")

    reports: list[dict[str, Any]] = []
    total_terminal_unresolved = 0
    for row in orders:
        n = row["n"]
        support = ORDER_SUPPORT[n]
        threshold = rebuilt.thresholds[n]
        allowed = list(rebuilt.allowed_windows[n])
        walks = list(rebuilt.rooted_walks[n])
        classes = list(rebuilt.canonical_classes[n])
        expected_allowed, expected_walks, expected_classes, expected_terminals = EXPECTED[n]

        _require(row.get("status") == "EXACT_NO_COUNTEREXAMPLE", f"n={n}: status mismatch")
        _require(row.get("support_length") == support, f"n={n}: support mismatch")
        _stored_lower, stored_upper = _verify_threshold_record(
            row.get("threshold_squared"), threshold
        )

        partition = row.get("local_window_partition")
        _require(type(partition) is dict, f"n={n}: local partition missing")
        stored_allowed = _int_list(
            partition.get("surviving_window_codes"), f"n={n} allowed windows"
        )
        stored_walks = _int_list(
            row.get("rooted_even_Q_codes"), f"n={n} rooted walks"
        )
        stored_classes = _int_list(
            row.get("canonical_terminal_Q_codes"), f"n={n} canonical classes"
        )
        _require(stored_allowed == allowed, f"n={n}: allowed windows mismatch")
        _require(stored_walks == walks, f"n={n}: rooted walks mismatch")
        _require(stored_classes == classes, f"n={n}: canonical classes mismatch")
        _require(rebuilt.unresolved_windows[n] == 0, f"n={n}: local window unresolved")

        decisions: list[list[Any]] = []
        witness_survivors: list[int] = []
        excluded_margins: list[Fraction] = []
        for code, (numerator, denominator) in enumerate(window_quotients[support]):
            quotient = Fraction(numerator, denominator)
            if quotient > stored_upper:
                decision = "EXCLUDED"
                excluded_margins.append(quotient - stored_upper)
            else:
                decision = "SURVIVOR"
                witness_survivors.append(code)
            decisions.append([code, decision])
        _require(witness_survivors == allowed, f"n={n}: stored exact witnesses give a different partition")
        _require(len(excluded_margins) + len(allowed) == 1 << (support + 1), f"n={n}: partition incomplete")
        _require(
            partition
            == {
                "all_window_count": 1 << (support + 1),
                "excluded_window_count": (1 << (support + 1)) - expected_allowed,
                "surviving_window_count": expected_allowed,
                "surviving_window_codes": allowed,
                "surviving_window_codes_sha256": _digest(allowed),
                "partition_sha256": _stream_sha256(decisions),
                "minimum_exact_exclusion_margin": str(min(excluded_margins)),
            },
            f"n={n}: local partition counts, hashes, or margin mismatch",
        )

        _require(
            row.get("overlap_automaton_state_count")
            == rebuilt.automaton_states[n]
            == EXPECTED_AUTOMATON_STATES[n],
            f"n={n}: automaton state count mismatch",
        )
        _require(row.get("rooted_even_closed_walk_count") == expected_walks, f"n={n}: even closed-walk count mismatch")
        _require(
            row.get("rooted_odd_closed_walk_count")
            == rebuilt.rooted_odd_counts[n]
            == EXPECTED_ROOTED_ODD[n],
            f"n={n}: odd closed-walk count mismatch",
        )
        _require(row.get("rooted_even_Q_codes_sha256") == _digest(walks), f"n={n}: rooted-walk hash mismatch")
        _require(row.get("canonical_terminal_Q_codes_sha256") == _digest(classes), f"n={n}: canonical-class hash mismatch")
        symmetry = row.get("symmetry_reduction")
        _require(type(symmetry) is dict, f"n={n}: symmetry record missing")
        bracelets = _even_binary_bracelets(n)
        _require(bracelets == EXPECTED_BRACELETS[n], f"n={n}: independent Burnside count mismatch")
        _require(
            symmetry
            == {
                "legal_even_Q_dihedral_orbits_before_pruning": bracelets,
                "spectral_states_before_pruning": 2 * bracelets,
                "canonicalization": "binary dihedral orbit; alpha remains an independent +/-1 sector",
            },
            f"n={n}: symmetry reduction mismatch",
        )

        terminals = row.get("terminal_records")
        _require(type(terminals) is list, f"n={n}: terminals missing")
        terminal_keys = [
            (record.get("canonical_q_code"), record.get("alpha"))
            for record in terminals
            if type(record) is dict
        ]
        expected_keys = [(code, alpha) for code in classes for alpha in (-1, 1)]
        _require(terminal_keys == expected_keys, f"n={n}: terminals missing, duplicated, or out of order")
        terminal_reports = [
            _verify_terminal(record, n, code, alpha, threshold, stored_upper)
            for record, (code, alpha) in zip(terminals, expected_keys, strict=True)
        ]
        _require(row.get("terminal_state_count") == expected_terminals, f"n={n}: terminal count mismatch")
        _require(row.get("terminal_unresolved") == 0, f"n={n}: unresolved terminal")
        _require(row.get("terminal_records_sha256") == _digest(terminals), f"n={n}: terminal stream hash mismatch")
        _require(
            row.get("conclusion")
            == "No signing has rho(A)^2 strictly below the conjectured threshold squared.",
            f"n={n}: conclusion mismatch",
        )
        total_terminal_unresolved += row["terminal_unresolved"]
        reports.append(
            {
                "n": n,
                "allowed_windows": len(allowed),
                "rooted_even_closed_walks": len(walks),
                "canonical_q_classes": len(classes),
                "terminal_states": len(terminal_reports),
                "terminal_unresolved": 0,
            }
        )

    _require(total_terminal_unresolved == 0, "terminal_unresolved is nonzero")
    _require(
        data.get("classification")
        == {
            "holds_at": list(ORDER_SUPPORT),
            "fails_at_in_task55_interval": [40],
            "combined_with_inherited_results": (
                "For even n>=8, the conjecture fails exactly at n=32, n=40, "
                "and every even n>=48."
            ),
        },
        "classification summary mismatch",
    )
    _require(
        data.get("global_checks")
        == {
            "all_six_orders_present": True,
            "all_six_exact_no_counterexample": True,
            "terminal_unresolved_total": 0,
            "all_window_tables_complete": True,
        },
        "global checks mismatch",
    )
    return {
        "status": "TARGET_A_TASK55_SMALL_ORDER_EXACT_VERIFY_PASS",
        "orders": reports,
        "terminal_unresolved": total_terminal_unresolved,
    }


def main() -> None:
    report = verify()
    print(report["status"])
    for row in report["orders"]:
        print(
            "n={n} allowed={allowed_windows} rooted_even={rooted_even_closed_walks} "
            "classes={canonical_q_classes} terminals={terminal_states}".format(**row)
        )


if __name__ == "__main__":
    main()

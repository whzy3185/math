"""Produce the exact Task 55 classification for the six open small orders.

Floating point is used only to propose integer Rayleigh vectors. Every
accepted exclusion is the exact rational comparison

    v^T M v / v^T v > U_n > rho_-(n)^2.

The certificate stores every local window, every surviving rooted cyclic
word, every dihedral terminal, and both holonomy sectors.
"""

from __future__ import annotations

import hashlib
import json
import math
import platform
import subprocess
import time
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np
import sympy as sp

from target_a_verifier import Signing, exact_sign, threshold_squared


REPO = Path(__file__).resolve().parents[2]
OUTPUT = (
    REPO
    / "research"
    / "proofs"
    / "task55"
    / "certificates"
    / "small_order_exact_classification.json"
)

ORDERS = (34, 36, 38, 42, 44, 46)
SUPPORT_BY_N = {34: 12, 36: 13, 38: 14, 42: 14, 44: 14, 46: 14}

# Exact isolating intervals previously obtained from the minimal polynomial of
# 4(cos(pi/n)^2+cos(2pi/n)^2). They are rechecked symbolically below.
THRESHOLD_INTERVALS = {
    34: (Fraction(6006814310587, 767066553830), Fraction(10861827659557, 1387048821607)),
    36: (Fraction(12030266208365, 1532713092434), Fraction(12379123219309, 1577159133677)),
    38: (Fraction(4331925327064, 550830192141), Fraction(27013554047573, 3434934825278)),
    42: (Fraction(9874089681459, 1251658121563), Fraction(8970253542190, 1137086157891)),
    44: (Fraction(7861741861835, 995329952838), Fraction(9658832935627, 1222849325155)),
    46: (Fraction(10819548274804, 1368314880897), Fraction(11594781349313, 1466356215440)),
}

EXPECTED = {
    34: {"allowed_windows": 124, "states": 92, "rooted_even": 1, "rooted_odd": 0, "canonical": 1},
    36: {"allowed_windows": 128, "states": 92, "rooted_even": 1, "rooted_odd": 4, "canonical": 1},
    38: {"allowed_windows": 184, "states": 132, "rooted_even": 77, "rooted_odd": 38, "canonical": 3},
    42: {"allowed_windows": 232, "states": 166, "rooted_even": 337, "rooted_odd": 392, "canonical": 7},
    44: {"allowed_windows": 240, "states": 171, "rooted_even": 353, "rooted_odd": 620, "canonical": 10},
    46: {"allowed_windows": 240, "states": 171, "rooted_even": 599, "rooted_odd": 690, "canonical": 10},
}

EXPECTED_BRACELETS = {
    34: 126390032,
    36: 477353376,
    38: 1808676326,
    42: 26179922024,
    44: 99957747388,
    46: 382443112538,
}


def compact(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(value: Any) -> str:
    return hashlib.sha256(compact(value)).hexdigest()


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def q_bits(code: int, length: int) -> str:
    return "".join("1" if (code >> index) & 1 else "0" for index in range(length))


def reverse_bits(code: int, length: int) -> int:
    result = 0
    for _ in range(length):
        result = (result << 1) | (code & 1)
        code >>= 1
    return result


def rotate_left(code: int, shift: int, length: int) -> int:
    mask = (1 << length) - 1
    shift %= length
    if not shift:
        return code & mask
    return ((code << shift) | (code >> (length - shift))) & mask


def dihedral_orbit(code: int, length: int) -> tuple[int, ...]:
    reflected = reverse_bits(code, length)
    return tuple(sorted(
        {rotate_left(code, shift, length) for shift in range(length)}
        | {rotate_left(reflected, shift, length) for shift in range(length)}
    ))


def canonical_code(code: int, length: int) -> int:
    return dihedral_orbit(code, length)[0]


def even_binary_bracelets(length: int) -> int:
    rotation_sum = 0
    for shift in range(length):
        cycles = math.gcd(length, shift)
        cycle_length = length // cycles
        rotation_sum += 1 << cycles if cycle_length % 2 == 0 else 1 << (cycles - 1)
    reflection_sum = length * (1 << (length // 2))
    quotient, remainder = divmod(rotation_sum + reflection_sum, 2 * length)
    if remainder:
        raise AssertionError("Burnside count is not integral")
    return quotient


def tau_from_window(code: int, q_length: int) -> tuple[int, ...]:
    tau = [1]
    for index in range(q_length):
        tau.append(tau[-1] * (1 if (code >> index) & 1 else -1))
    return tuple(tau)


def local_squared_matrix(code: int, support: int) -> np.ndarray:
    """Return P A^2 P on a support of `support` consecutive vertices."""
    tau_word = tau_from_window(code, support + 1)
    # tau_word is tau_-2,...,tau_(support-1).
    tau = {index - 2: value for index, value in enumerate(tau_word)}
    outputs = list(range(-2, support + 2))
    action = np.zeros((len(outputs), support), dtype=np.int64)
    for column in range(support):
        for row, output in enumerate(outputs):
            if abs(output - column) == 1:
                action[row, column] = 1
            elif output == column + 2:
                action[row, column] = tau[column]
            elif output == column - 2:
                action[row, column] = tau[column - 2]
    return action.T @ action


def normalize_integer_vector(vector: np.ndarray) -> tuple[int, ...]:
    values = [int(value) for value in vector]
    divisor = math.gcd(*map(abs, values))
    if divisor:
        values = [value // divisor for value in values]
    first = next((value for value in values if value), 0)
    if first < 0:
        values = [-value for value in values]
    if not any(values):
        raise AssertionError("integer proposal vanished")
    return tuple(values)


def integer_proposal(matrix: np.ndarray, scale: int) -> tuple[int, ...]:
    _values, vectors = np.linalg.eigh(matrix.astype(float))
    return normalize_integer_vector(np.rint(scale * vectors[:, -1]).astype(np.int64))


def quadratic(matrix: np.ndarray, vector: tuple[int, ...]) -> tuple[int, int]:
    denominator = sum(value * value for value in vector)
    numerator = sum(
        vector[row] * int(matrix[row, column]) * vector[column]
        for row in range(len(vector))
        for column in range(len(vector))
    )
    return numerator, denominator


def build_window_table(support: int) -> dict[str, Any]:
    q_length = support + 1
    rows = []
    stream = hashlib.sha256()
    for code in range(1 << q_length):
        matrix = local_squared_matrix(code, support)
        vector = integer_proposal(matrix, 4096)
        numerator, denominator = quadratic(matrix, vector)
        row = [code, numerator, denominator, list(vector)]
        rows.append(row)
        stream.update(compact(row))
    return {
        "support_length": support,
        "q_window_length": q_length,
        "row_schema": ["window_code", "numerator", "denominator", "integer_vector"],
        "all_window_count": 1 << q_length,
        "rows_sha256": stream.hexdigest(),
        "rows": rows,
    }


def classify_windows(table: dict[str, Any], upper: Fraction) -> tuple[list[int], dict[str, Any]]:
    survivors = []
    excluded = 0
    minimum_margin: Fraction | None = None
    partition = hashlib.sha256()
    for code, numerator, denominator, _vector in table["rows"]:
        quotient = Fraction(numerator, denominator)
        decision = "EXCLUDED" if quotient > upper else "SURVIVOR"
        partition.update(compact([code, decision]))
        if decision == "EXCLUDED":
            excluded += 1
            margin = quotient - upper
            minimum_margin = margin if minimum_margin is None or margin < minimum_margin else minimum_margin
        else:
            survivors.append(code)
    if excluded + len(survivors) != table["all_window_count"] or minimum_margin is None:
        raise AssertionError("window partition is incomplete")
    return survivors, {
        "all_window_count": table["all_window_count"],
        "excluded_window_count": excluded,
        "surviving_window_count": len(survivors),
        "surviving_window_codes": survivors,
        "surviving_window_codes_sha256": digest(survivors),
        "partition_sha256": partition.hexdigest(),
        "minimum_exact_exclusion_margin": fraction_text(minimum_margin),
    }


def closed_words(
    survivor_codes: list[int], q_window_length: int, length: int
) -> tuple[list[int], int, int]:
    state_mask = (1 << (q_window_length - 1)) - 1
    states = sorted(
        {code & state_mask for code in survivor_codes}
        | {code >> 1 for code in survivor_codes}
    )
    outgoing: dict[int, list[tuple[int, int]]] = {state: [] for state in states}
    for code in survivor_codes:
        outgoing[code & state_mask].append(
            (code >> 1, (code >> (q_window_length - 1)) & 1)
        )

    even_words: set[int] = set()
    trace_even = 0
    trace_odd = 0
    for root in states:
        stack = [(root, 0, 0, 0)]
        while stack:
            state, depth, parity, code = stack.pop()
            if depth == length:
                if state == root:
                    if parity == 0:
                        even_words.add(code)
                        trace_even += 1
                    else:
                        trace_odd += 1
                continue
            for target, bit in outgoing.get(state, ()):
                stack.append((target, depth + 1, parity ^ bit, code | (bit << depth)))

    words = sorted(even_words)
    if trace_even != len(words):
        raise AssertionError("closed-walk trace and rooted-word set disagree")
    return words, len(states), trace_odd


def signing_matrix(code: int, length: int, alpha: int) -> np.ndarray:
    q = tuple(1 if (code >> index) & 1 else -1 for index in range(length))
    tau = [1]
    for index in range(length - 1):
        tau.append(tau[-1] * q[index])
    if tau[-1] * q[-1] != 1:
        raise AssertionError("terminal Q word has odd parity")
    step1 = [1] * length
    step1[-1] = alpha
    step2 = [
        tau[index] * step1[index] * step1[(index + 1) % length]
        for index in range(length)
    ]
    matrix = np.zeros((length, length), dtype=np.int64)
    for index in range(length):
        for distance, sign in ((1, step1[index]), (2, step2[index])):
            target = (index + distance) % length
            matrix[index, target] = matrix[target, index] = sign
    return matrix


def terminal_rayleigh(code: int, length: int, alpha: int, upper: Fraction) -> dict[str, Any]:
    adjacency = signing_matrix(code, length, alpha)
    if code == 0 and alpha == 1:
        vector = tuple(index % 2 for index in range(length))
    else:
        square = adjacency @ adjacency
        vector = integer_proposal(square, 65536)
    image = adjacency @ np.asarray(vector, dtype=np.int64)
    numerator = sum(int(value) ** 2 for value in image)
    denominator = sum(value * value for value in vector)
    quotient = Fraction(numerator, denominator)
    if quotient <= upper:
        # This path remains proposal-only. Acceptance is still exact below.
        square = adjacency @ adjacency
        vector = integer_proposal(square, 1048576)
        image = adjacency @ np.asarray(vector, dtype=np.int64)
        numerator = sum(int(value) ** 2 for value in image)
        denominator = sum(value * value for value in vector)
        quotient = Fraction(numerator, denominator)
    if quotient <= upper:
        raise AssertionError(f"terminal Rayleigh witness unresolved: n={length}, code={code}, alpha={alpha}")
    record = {
        "canonical_q_code": code,
        "q_bits": q_bits(code, length),
        "alpha": alpha,
        "status": "EXACT_INTEGER_RAYLEIGH_ABOVE_THRESHOLD_UPPER",
        "integer_vector": list(vector),
        "numerator": numerator,
        "denominator": denominator,
        "quotient": fraction_text(quotient),
        "strict_margin_over_threshold_upper": fraction_text(quotient - upper),
    }
    record["record_sha256"] = digest(record)
    return record


def optimizer_record(
    length: int, upper: Fraction, threshold_minpoly: sp.Poly
) -> dict[str, Any]:
    signing = Signing(
        length,
        tuple([1] * (length - 1) + [-1]),
        tuple(signing_matrix(0, length, -1)[index, (index + 2) % length] for index in range(length)),
    )
    variable = threshold_minpoly.gens[0]
    adjacency = sp.zeros(length)
    for index, sign in enumerate(signing.step1):
        target = (index + 1) % length
        adjacency[index, target] = adjacency[target, index] = sign
    for index, sign in enumerate(signing.step2):
        target = (index + 2) % length
        adjacency[index, target] = adjacency[target, index] = sign
    characteristic = sp.Poly((adjacency * adjacency).charpoly(variable).as_expr(), variable, domain=sp.ZZ)
    quotient, remainder = sp.div(characteristic, threshold_minpoly, domain=sp.QQ)
    if not remainder.is_zero:
        raise AssertionError("optimizer does not contain the exact threshold eigenvalue")
    multiplicity = 1
    while True:
        next_quotient, next_remainder = sp.div(quotient, threshold_minpoly, domain=sp.QQ)
        if not next_remainder.is_zero:
            break
        quotient = next_quotient
        multiplicity += 1
    charpoly = str(characteristic.as_expr())
    record = {
        "canonical_q_code": 0,
        "q_bits": "0" * length,
        "alpha": -1,
        "status": "EXACT_THRESHOLD_EIGENVALUE",
        "conclusion": "rho(A)^2 is at least the conjectured threshold squared",
        "threshold_minpoly_divides_charpoly_A2": True,
        "threshold_multiplicity_in_charpoly_A2": multiplicity,
        "threshold_minpoly_coefficients": [str(value) for value in threshold_minpoly.all_coeffs()],
        "charpoly_A2": charpoly,
        "charpoly_A2_sha256": hashlib.sha256((charpoly + "\n").encode()).hexdigest(),
        "threshold_upper_is_strictly_above_equality": True,
        "threshold_upper": fraction_text(upper),
    }
    record["record_sha256"] = digest(record)
    return record


def threshold_record(length: int) -> tuple[Fraction, dict[str, Any], sp.Poly]:
    lower, upper = THRESHOLD_INTERVALS[length]
    value = threshold_squared(length)
    if exact_sign(value - sp.Rational(lower.numerator, lower.denominator)) != 1:
        raise AssertionError("threshold lower endpoint is not strict")
    if exact_sign(sp.Rational(upper.numerator, upper.denominator) - value) != 1:
        raise AssertionError("threshold upper endpoint is not strict")
    variable = sp.Symbol("x")
    polynomial = sp.Poly(sp.minimal_polynomial(value, variable), variable, domain=sp.QQ)
    return upper, {
        "definition": "4*(cos(pi/n)^2+cos(2*pi/n)^2)",
        "strict_rational_lower": fraction_text(lower),
        "strict_rational_upper": fraction_text(upper),
        "minimal_polynomial_coefficients": [str(value) for value in polynomial.all_coeffs()],
        "exact_endpoint_sign_checks": {"theta_minus_lower": 1, "upper_minus_theta": 1},
    }, polynomial


def order_record(length: int, table: dict[str, Any]) -> dict[str, Any]:
    upper, threshold, threshold_minpoly = threshold_record(length)
    survivor_windows, window_partition = classify_windows(table, upper)
    rooted, state_count, odd_count = closed_words(
        survivor_windows, table["q_window_length"], length
    )
    canonical = sorted({canonical_code(code, length) for code in rooted})
    covered = set()
    for code in canonical:
        covered.update(dihedral_orbit(code, length))
    if covered != set(rooted):
        raise AssertionError("canonical terminal orbits do not cover exactly the rooted words")

    terminals = []
    unresolved = 0
    for code in canonical:
        for alpha in (-1, 1):
            if code == 0 and alpha == -1:
                terminals.append(optimizer_record(length, upper, threshold_minpoly))
            else:
                terminals.append(terminal_rayleigh(code, length, alpha, upper))
    unresolved += sum(row["status"] not in {
        "EXACT_THRESHOLD_EIGENVALUE",
        "EXACT_INTEGER_RAYLEIGH_ABOVE_THRESHOLD_UPPER",
    } for row in terminals)

    bracelet_count = even_binary_bracelets(length)
    expected = EXPECTED[length]
    observed = {
        "allowed_windows": len(survivor_windows),
        "states": state_count,
        "rooted_even": len(rooted),
        "rooted_odd": odd_count,
        "canonical": len(canonical),
    }
    if observed != expected:
        raise AssertionError(f"unexpected exact state counts for n={length}: {observed}")
    if bracelet_count != EXPECTED_BRACELETS[length] or unresolved:
        raise AssertionError(f"global count or terminal closure failed for n={length}")

    return {
        "n": length,
        "status": "EXACT_NO_COUNTEREXAMPLE",
        "support_length": table["support_length"],
        "threshold_squared": threshold,
        "symmetry_reduction": {
            "legal_even_Q_dihedral_orbits_before_pruning": bracelet_count,
            "spectral_states_before_pruning": 2 * bracelet_count,
            "canonicalization": "binary dihedral orbit; alpha remains an independent +/-1 sector",
        },
        "local_window_partition": window_partition,
        "overlap_automaton_state_count": state_count,
        "rooted_even_closed_walk_count": len(rooted),
        "rooted_odd_closed_walk_count": odd_count,
        "rooted_even_Q_codes": rooted,
        "rooted_even_Q_codes_sha256": digest(rooted),
        "canonical_terminal_Q_codes": canonical,
        "canonical_terminal_Q_codes_sha256": digest(canonical),
        "terminal_state_count": len(terminals),
        "terminal_unresolved": unresolved,
        "terminal_records": terminals,
        "terminal_records_sha256": digest(terminals),
        "conclusion": "No signing has rho(A)^2 strictly below the conjectured threshold squared.",
    }


def repository_head() -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=REPO, check=True, capture_output=True, text=True
    ).stdout.strip()


def write_compact_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_bytes(compact(payload))
    temporary.replace(path)


def run() -> dict[str, Any]:
    started = time.perf_counter()
    tables = {support: build_window_table(support) for support in (12, 13, 14)}
    orders = [order_record(length, tables[SUPPORT_BY_N[length]]) for length in ORDERS]
    payload: dict[str, Any] = {
        "schema_version": 1,
        "status": "TASK55_SMALL_ORDER_EXACT_CLASSIFICATION_PRODUCED",
        "evidence_status": "EXACT_FINITE_PRODUCER; INDEPENDENT_CHECKER_REQUIRED_FOR_UPGRADE",
        "arithmetic_boundary": (
            "Floating eigensolvers propose integer vectors only. All accepted local and terminal "
            "exclusions use integer quadratic forms and exact Fraction comparisons against strict "
            "symbolically checked rational threshold upper endpoints."
        ),
        "repository_head": repository_head(),
        "producer_path": str(Path(__file__).resolve().relative_to(REPO)),
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "runtime": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "sympy": sp.__version__,
        },
        "window_tables": [tables[support] for support in (12, 13, 14)],
        "orders": orders,
        "classification": {
            "holds_at": list(ORDERS),
            "fails_at_in_task55_interval": [40],
            "combined_with_inherited_results": (
                "For even n>=8, the conjecture fails exactly at n=32, n=40, "
                "and every even n>=48."
            ),
        },
        "global_checks": {
            "all_six_orders_present": [row["n"] for row in orders] == list(ORDERS),
            "all_six_exact_no_counterexample": all(row["status"] == "EXACT_NO_COUNTEREXAMPLE" for row in orders),
            "terminal_unresolved_total": sum(row["terminal_unresolved"] for row in orders),
            "all_window_tables_complete": all(
                len(table["rows"]) == table["all_window_count"] for table in tables.values()
            ),
        },
    }
    core = dict(payload)
    payload["payload_core_sha256"] = digest(core)
    write_compact_json(OUTPUT, payload)
    elapsed = time.perf_counter() - started
    return {
        "status": payload["status"],
        "output": str(OUTPUT.relative_to(REPO)),
        "output_bytes": OUTPUT.stat().st_size,
        "output_sha256": hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),
        "payload_core_sha256": payload["payload_core_sha256"],
        "elapsed_seconds": elapsed,
        "orders": [
            {
                "n": row["n"],
                "allowed_windows": row["local_window_partition"]["surviving_window_count"],
                "rooted_even": row["rooted_even_closed_walk_count"],
                "canonical_Q": len(row["canonical_terminal_Q_codes"]),
                "terminal_states": row["terminal_state_count"],
                "terminal_unresolved": row["terminal_unresolved"],
            }
            for row in orders
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))

#!/usr/bin/env python3
"""Second-organization verifier for the Task 55 multi-gap certificate.

This file intentionally uses only the Python standard library.  In particular,
it does not import the producer or either of the repository's other verifiers.
"""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any, Callable


RESEARCH = Path(__file__).resolve().parents[1]
MANIFEST_PATH = RESEARCH / "proofs" / "task55" / "certificates" / "multigap_support18_manifest.json"
STREAM_PATH = RESEARCH / "proofs" / "task55" / "certificates" / "multigap_support18.jsonl"
C6_PATH = RESEARCH / "proofs" / "task51" / "certificates" / "c6_exact_evans_elimination.json"

TOTALS = (2, 6, 10, 14, 18)
THRESHOLD_NUMERATOR = 7_905_369_311_620_328
THRESHOLD_DENOMINATOR = 1_000_000_000_000_000
C6_LEFT = Fraction(7_905_369_311_620_327, THRESHOLD_DENOMINATOR)
C6_RIGHT = Fraction(THRESHOLD_NUMERATOR, THRESHOLD_DENOMINATOR)
C6_SHA256 = "3de93781004929852ebdbd31c7ecbfdf72d125e0eea2b1606b4e472237ecd225"
STREAM_SHA256 = "9c8ef135fc11ca7b8c1761c3d45fb89c65790d97c12f2081787814f046c038bf"
WORD_SHA256 = "1c635aa6c50d8dc2387508cf7ce63f67e6a2ced490a3ca6b4eacbe8b8c912bfb"
EXPECTED_COUNTS = {2: 1, 6: 16, 10: 186, 14: 2_275, 18: 28_530}

C6_POLYNOMIAL_DESCENDING = (
    16,
    -520,
    6_913,
    -48_448,
    191_768,
    -423_904,
    484_528,
    -270_464,
    137_856,
    -19_968,
    256,
)


class VerificationError(RuntimeError):
    """Raised when any exact certificate obligation fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def reject_float(token: str) -> Any:
    raise VerificationError(f"floating-point JSON scalar is forbidden: {token}")


def reject_constant(token: str) -> Any:
    raise VerificationError(f"non-finite JSON scalar is forbidden: {token}")


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise VerificationError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def decode_ascii_document(raw: bytes, label: str) -> str:
    require(not raw.startswith(b"\xef\xbb\xbf"), f"{label}: UTF-8 BOM is forbidden")
    require(b"\r" not in raw, f"{label}: CR/CRLF is forbidden")
    require(raw.endswith(b"\n"), f"{label}: terminal LF is required")
    try:
        return raw.decode("ascii")
    except UnicodeDecodeError as exc:
        raise VerificationError(f"{label}: non-ASCII byte is forbidden") from exc


def parse_json_object(raw: bytes, label: str) -> dict[str, Any]:
    text = decode_ascii_document(raw, label)
    try:
        payload = json.loads(
            text,
            object_pairs_hook=unique_object,
            parse_float=reject_float,
            parse_constant=reject_constant,
        )
    except json.JSONDecodeError as exc:
        raise VerificationError(f"{label}: invalid JSON: {exc}") from exc
    require(type(payload) is dict, f"{label}: top level must be an object")
    canonical = json.dumps(payload, ensure_ascii=True, indent=2) + "\n"
    require(text == canonical, f"{label}: document is not canonical two-space JSON")
    return payload


EXPECTED_MANIFEST: dict[str, Any] = {
    "schema_version": 1,
    "status": "TASK55_MULTIGAP_SUPPORT18_COMPUTER_ASSISTED_PROVED",
    "evidence": "COMPUTER_ASSISTED_PROVED",
    "scope": {
        "totals": [2, 6, 10, 14, 18],
        "minimum_gap_count": 2,
        "equivalence": "translation fixed by x_0=0; reflection canonical=min(g,reversed(g))",
        "primitive": "no nonempty contiguous subword has zero charge sum(g_i-4)",
        "counts_by_total": {"2": 1, "6": 16, "10": 186, "14": 2275, "18": 28530},
        "total_count": 31008,
    },
    "open_interface": {
        "defects": "(-4 Z_{>=0}) union {x_0,...,x_m} union (S+4 Z_{>=0})",
        "q": "Q_i=+1 at defects and -1 otherwise",
        "tau_anchor": "tau_0=1",
        "tau_recurrence": "tau_(i+1)=Q_i tau_i",
        "operator": "(Av)_k=v_(k-1)+v_(k+1)+tau_(k-2)v_(k-2)+tau_k v_(k+2)",
        "support": "I_g=[-2,S+2] intersect Z",
        "image_window": "J_g=[-4,S+4] intersect Z",
        "forbidden_truncation": "do not replace ||Av||^2 by ||P_I A P_I v||^2",
    },
    "witness_generation": {
        "rule": "round(20*u), divide coordinate gcd, make first nonzero coordinate positive",
        "top_vector": "FP64 top-branch location followed by 80- and 120-digit Rayleigh-quotient iteration; identical rounded vectors required",
        "acceptance": "integer recomputation of the full Av on J_g only",
    },
    "strict_threshold": {
        "numerator": THRESHOLD_NUMERATOR,
        "denominator": THRESHOLD_DENOMINATOR,
        "test": "N*1000000000000000 > 7905369311620328*D",
    },
    "stream": {
        "path": "research/proofs/task55/certificates/multigap_support18.jsonl",
        "format": "one compact ASCII JSON array [[g_1,...,g_m],[v_-2,...,v_(S+2)]] per LF-terminated line",
        "line_count": 31008,
        "word_sha256": WORD_SHA256,
        "sha256": STREAM_SHA256,
    },
    "statistics": {
        "maximum_absolute_vector_coordinate": 11,
        "maximum_numerator": 6226,
        "maximum_denominator": 442,
        "unique_weakest_word": [3, 3],
        "unique_weakest_vector": [3, 0, 5, 7, 6, 9, 7, 8, 6, 2, 4],
        "weakest_numerator": 2930,
        "weakest_denominator": 369,
    },
    "c6_dependency": {
        "path": "research/proofs/task51/certificates/c6_exact_evans_elimination.json",
        "sha256": C6_SHA256,
        "status": "C6_DEGREE10_EVANS_POLYNOMIAL_PROVED",
        "polynomial_coefficients_descending": list(C6_POLYNOMIAL_DESCENDING),
        "isolating_interval": [
            "7905369311620327/1000000000000000",
            "988171163952541/125000000000000",
        ],
    },
    "three_three_local_lemma": {
        "status": "ANALYTIC_PROVED_ARBITRARY_FINITE_CORE_LENGTH",
        "support_relative_to_first_motif_defect": [-2, 8],
        "tau_anchor": "tau_x=1",
        "cases": [
            {
                "predecessor_gap": "1",
                "vector": [1, 0, 3, 4, 3, 5, 4, 4, 3, 1, 2],
                "N_lower_bound": 874,
                "possible_N": [874, 902],
                "D": 106,
            },
            {
                "predecessor_gap": "2",
                "vector": [2, 0, 0, -3, -2, -2, -2, -2, -1, -1, -1],
                "N_lower_bound": 258,
                "possible_N": [258],
                "D": 32,
            },
            {
                "predecessor_gap": ">=3",
                "vector": [1, 0, 3, 4, 3, 5, 4, 4, 3, 1, 2],
                "N_lower_bound": 838,
                "possible_N": [838],
                "D": 106,
            },
        ],
        "finite_dependency_cases_checked": 32,
        "minimum_exact_margin_over_c6_upper": "1928310515327/6625000000000000",
        "opposite_tau_lift": "v_i -> (-1)^i v_i because A_(-tau)=-D A_tau D",
    },
    "proof_boundary": {
        "bounded_class": "PROVED only for the 31008 canonical primitive multi-gap cores with S<=18 in the listed residue class",
        "three_three_subclass": "PROVED for arbitrary finite core length when a consecutive (3,3) motif occurs",
        "universal_B0_to_B2": "OPEN",
        "reference_cell_insertion_removal": "REJECTED: it multiplies a non-scalar bulk monodromy and is not a spectral equivalence",
    },
}


def separator_composition(total: int, mask: int) -> tuple[int, ...]:
    parts: list[int] = []
    start = 0
    for position in range(1, total):
        if mask & (1 << (position - 1)):
            parts.append(position - start)
            start = position
    parts.append(total - start)
    return tuple(parts)


def is_primitive(word: tuple[int, ...]) -> bool:
    seen = {0}
    charge = 0
    for gap in word:
        charge += gap - 4
        if charge in seen:
            return False
        seen.add(charge)
    return True


def enumerate_words() -> list[tuple[int, ...]]:
    words: list[tuple[int, ...]] = []
    for total in TOTALS:
        layer: list[tuple[int, ...]] = []
        for mask in range(1, 1 << (total - 1)):
            word = separator_composition(total, mask)
            if word > tuple(reversed(word)):
                continue
            if is_primitive(word):
                layer.append(word)
        layer.sort()
        words.extend(layer)
    return words


def is_defect(index: int, positions: frozenset[int], total: int) -> bool:
    in_left_tail = index <= 0 and index % 4 == 0
    in_right_tail = index >= total and (index - total) % 4 == 0
    return in_left_tail or index in positions or in_right_tail


def tau_for_word(word: tuple[int, ...]) -> dict[int, int]:
    positions_list = [0]
    for gap in word:
        positions_list.append(positions_list[-1] + gap)
    total = positions_list[-1]
    positions = frozenset(positions_list)

    def q(index: int) -> int:
        return 1 if is_defect(index, positions, total) else -1

    tau = {0: 1}
    for index in range(0, total + 4):
        tau[index + 1] = q(index) * tau[index]
    for index in range(-1, -7, -1):
        tau[index] = q(index) * tau[index + 1]
    require(all(value in (-1, 1) for value in tau.values()), "tau reconstruction left {+1,-1}")
    return tau


def apply_open_operator(word: tuple[int, ...], vector: tuple[int, ...]) -> tuple[int, ...]:
    total = sum(word)
    require(len(vector) == total + 5, f"{word}: wrong support length")
    values = {index: vector[index + 2] for index in range(-2, total + 3)}
    tau = tau_for_word(word)

    def v(index: int) -> int:
        return values.get(index, 0)

    return tuple(
        v(index - 1)
        + v(index + 1)
        + tau[index - 2] * v(index - 2)
        + tau[index] * v(index + 2)
        for index in range(-4, total + 5)
    )


def parse_stream_record(raw_line: bytes, line_number: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    label = f"stream line {line_number}"
    require(raw_line, f"{label}: blank line is forbidden")
    try:
        text = raw_line.decode("ascii")
    except UnicodeDecodeError as exc:
        raise VerificationError(f"{label}: non-ASCII byte is forbidden") from exc
    try:
        record = json.loads(text, parse_float=reject_float, parse_constant=reject_constant)
    except json.JSONDecodeError as exc:
        raise VerificationError(f"{label}: invalid JSON: {exc}") from exc
    canonical = json.dumps(record, ensure_ascii=True, separators=(",", ":"))
    require(text == canonical, f"{label}: record is not compact canonical JSON")
    require(type(record) is list and len(record) == 2, f"{label}: expected [word,vector]")
    word_raw, vector_raw = record
    require(type(word_raw) is list and type(vector_raw) is list, f"{label}: fields must be arrays")
    require(all(type(value) is int for value in word_raw), f"{label}: gaps must be exact integers")
    require(all(type(value) is int for value in vector_raw), f"{label}: vector must contain exact integers")
    require(all(0 < value <= 1_000_000 for value in word_raw), f"{label}: invalid or oversized gap")
    require(all(abs(value) <= 1_000_000 for value in vector_raw), f"{label}: oversized vector integer")
    return tuple(word_raw), tuple(vector_raw)


def verify_stream(expected_words: list[tuple[int, ...]]) -> dict[str, Any]:
    raw = STREAM_PATH.read_bytes()
    decode_ascii_document(raw, "certificate stream")
    require(hashlib.sha256(raw).hexdigest() == STREAM_SHA256, "certificate stream SHA-256 mismatch")
    raw_lines = raw[:-1].split(b"\n")
    require(len(raw_lines) == len(expected_words), "certificate stream line count mismatch")

    word_hash = hashlib.sha256()
    counts: Counter[int] = Counter()
    max_abs = 0
    max_numerator = 0
    max_denominator = 0
    weakest_ratio: Fraction | None = None
    weakest_records: list[tuple[tuple[int, ...], tuple[int, ...], int, int]] = []

    for line_number, (raw_line, expected_word) in enumerate(zip(raw_lines, expected_words), start=1):
        word, vector = parse_stream_record(raw_line, line_number)
        require(word == expected_word, f"line {line_number}: missing, duplicate, or reordered word")
        require(len(word) >= 2, f"line {line_number}: single-gap word is forbidden")
        require(word <= tuple(reversed(word)), f"line {line_number}: reflection-noncanonical word")
        require(is_primitive(word), f"line {line_number}: nonprimitive word")
        require(vector and any(vector), f"line {line_number}: zero witness")
        first_nonzero = next(value for value in vector if value)
        require(first_nonzero > 0, f"line {line_number}: witness sign is not canonical")
        require(math.gcd(*(abs(value) for value in vector)) == 1, f"line {line_number}: witness is not primitive")

        image = apply_open_operator(word, vector)
        numerator = sum(value * value for value in image)
        denominator = sum(value * value for value in vector)
        require(
            numerator * THRESHOLD_DENOMINATOR > THRESHOLD_NUMERATOR * denominator,
            f"line {line_number}: exact Rayleigh inequality failed",
        )

        projection = json.dumps(list(word), ensure_ascii=True, separators=(",", ":")).encode("ascii") + b"\n"
        word_hash.update(projection)
        counts[sum(word)] += 1
        max_abs = max(max_abs, *(abs(value) for value in vector))
        max_numerator = max(max_numerator, numerator)
        max_denominator = max(max_denominator, denominator)
        ratio = Fraction(numerator, denominator)
        record = (word, vector, numerator, denominator)
        if weakest_ratio is None or ratio < weakest_ratio:
            weakest_ratio = ratio
            weakest_records = [record]
        elif ratio == weakest_ratio:
            weakest_records.append(record)

    require(dict(counts) == EXPECTED_COUNTS, f"layer counts mismatch: {dict(counts)}")
    require(word_hash.hexdigest() == WORD_SHA256, "word projection SHA-256 mismatch")
    require(max_abs == 11, f"maximum vector coordinate mismatch: {max_abs}")
    require(max_numerator == 6226, f"maximum numerator mismatch: {max_numerator}")
    require(max_denominator == 442, f"maximum denominator mismatch: {max_denominator}")
    require(len(weakest_records) == 1, "weakest Rayleigh certificate is not unique")
    weakest_word, weakest_vector, weakest_numerator, weakest_denominator = weakest_records[0]
    require(weakest_word == (3, 3), f"weakest word mismatch: {weakest_word}")
    require(weakest_vector == (3, 0, 5, 7, 6, 9, 7, 8, 6, 2, 4), "weakest vector mismatch")
    require((weakest_numerator, weakest_denominator) == (2930, 369), "weakest exact ratio mismatch")
    return {
        "line_count": len(raw_lines),
        "counts": dict(counts),
        "max_abs": max_abs,
        "max_numerator": max_numerator,
        "max_denominator": max_denominator,
        "weakest": [list(weakest_word), weakest_numerator, weakest_denominator],
    }


def trim_polynomial(coefficients: list[Fraction]) -> list[Fraction]:
    while coefficients and coefficients[-1] == 0:
        coefficients.pop()
    return coefficients


def polynomial_remainder(dividend: list[Fraction], divisor: list[Fraction]) -> list[Fraction]:
    remainder = trim_polynomial(dividend[:])
    divisor = trim_polynomial(divisor[:])
    require(bool(divisor), "polynomial division by zero")
    while remainder and len(remainder) >= len(divisor):
        shift = len(remainder) - len(divisor)
        factor = remainder[-1] / divisor[-1]
        for index, coefficient in enumerate(divisor):
            remainder[index + shift] -= factor * coefficient
        trim_polynomial(remainder)
    return remainder


def sturm_chain(coefficients_descending: tuple[int, ...]) -> list[list[Fraction]]:
    polynomial = [Fraction(value) for value in reversed(coefficients_descending)]
    derivative = [Fraction(index) * polynomial[index] for index in range(1, len(polynomial))]
    chain = [trim_polynomial(polynomial), trim_polynomial(derivative)]
    while chain[-1]:
        remainder = polynomial_remainder(chain[-2], chain[-1])
        if not remainder:
            break
        chain.append([-value for value in remainder])
    return chain


def polynomial_value(polynomial: list[Fraction], point: Fraction) -> Fraction:
    value = Fraction(0)
    for coefficient in reversed(polynomial):
        value = value * point + coefficient
    return value


def sign_variations(chain: list[list[Fraction]], point: Fraction) -> int:
    signs: list[int] = []
    for polynomial in chain:
        value = polynomial_value(polynomial, point)
        if value:
            signs.append(1 if value > 0 else -1)
    return sum(left != right for left, right in zip(signs, signs[1:]))


def verify_c6_dependency() -> dict[str, Any]:
    raw = C6_PATH.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == C6_SHA256, "Task 51 c6 certificate SHA-256 mismatch")
    payload = parse_json_object(raw, "Task 51 c6 certificate")
    c6 = payload.get("c6")
    require(type(c6) is dict, "Task 51 certificate has no c6 object")
    require(c6.get("status") == "C6_DEGREE10_EVANS_POLYNOMIAL_PROVED", "Task 51 c6 status mismatch")
    require(c6.get("unique_root_in_interval") is True, "Task 51 unique-root claim is absent")
    require(c6.get("irreducible_degree") == 10, "Task 51 c6 degree mismatch")
    require(
        c6.get("c6_interval")
        == ["7905369311620327/1000000000000000", "988171163952541/125000000000000"],
        "Task 51 c6 interval mismatch",
    )
    expected_polynomial = (
        "16*y**10 - 520*y**9 + 6913*y**8 - 48448*y**7 + 191768*y**6 - 423904*y**5 "
        "+ 484528*y**4 - 270464*y**3 + 137856*y**2 - 19968*y + 256"
    )
    require(c6.get("c6_polynomial") == expected_polynomial, "Task 51 c6 polynomial mismatch")

    chain = sturm_chain(C6_POLYNOMIAL_DESCENDING)
    require(polynomial_value(chain[0], C6_LEFT) != 0, "c6 left endpoint is a root")
    require(polynomial_value(chain[0], C6_RIGHT) != 0, "c6 right endpoint is a root")
    roots = sign_variations(chain, C6_LEFT) - sign_variations(chain, C6_RIGHT)
    require(roots == 1, f"independent Sturm count is {roots}, expected 1")
    return {"degree": 10, "sturm_chain_length": len(chain), "roots_in_interval": roots}


def tau_from_local_defects(defects: frozenset[int], anchor: int = 1) -> dict[int, int]:
    def q(index: int) -> int:
        return 1 if index in defects else -1

    tau = {0: anchor}
    for index in range(0, 11):
        tau[index + 1] = q(index) * tau[index]
    for index in range(-1, -7, -1):
        tau[index] = q(index) * tau[index + 1]
    return tau


def apply_with_tau(vector: tuple[int, ...], tau: dict[int, int]) -> tuple[int, ...]:
    values = {index: vector[index + 2] for index in range(-2, 9)}

    def v(index: int) -> int:
        return values.get(index, 0)

    return tuple(
        v(index - 1)
        + v(index + 1)
        + tau[index - 2] * v(index - 2)
        + tau[index] * v(index + 2)
        for index in range(-4, 11)
    )


def alternating_lift(vector: tuple[int, ...], start: int) -> tuple[int, ...]:
    return tuple((1 if index % 2 == 0 else -1) * value for index, value in enumerate(vector, start=start))


def verify_three_three_lemma() -> dict[str, Any]:
    vectors = {
        1: (1, 0, 3, 4, 3, 5, 4, 4, 3, 1, 2),
        2: (2, 0, 0, -3, -2, -2, -2, -2, -1, -1, -1),
        3: (1, 0, 3, 4, 3, 5, 4, 4, 3, 1, 2),
    }
    expected_min_abs = {
        1: (1, 1, 3, 8, 6, 11, 8, 15, 9, 11, 11, 1, 4, 3, 2),
        2: (2, 2, 0, 5, 7, 4, 3, 9, 3, 4, 6, 0, 2, 2, 1),
        3: (1, 1, 3, 0, 8, 11, 8, 15, 9, 11, 11, 1, 4, 3, 2),
    }
    expected_nd = {1: (874, 106), 2: (258, 32), 3: (838, 106)}
    checked = 0
    numerator_values: dict[int, set[int]] = {1: set(), 2: set(), 3: set()}
    # Only Q[-4,-1] and Q[0,7] can multiply nonzero vector entries.  For a
    # fixed nearest predecessor, every subset strictly to its left must still
    # be admitted; this is the quantifier missed by the first proof write-up.
    for predecessor in (1, 2, 3, 4, 5):
        category = min(predecessor, 3)
        vector = vectors[category]
        free_left = tuple(range(-4, -predecessor)) if predecessor <= 4 else ()
        for mask in range(1 << len(free_left)):
            left_defects = {-predecessor}
            left_defects.update(
                index for bit, index in enumerate(free_left) if mask & (1 << bit)
            )
            # b=1 means Q_7=+1; every b>=2 gives Q_7=-1 and is locally
            # identical.  Defects at 8 or farther cannot enter a nonzero term.
            for successor in (1, 2):
                defects = left_defects | {0, 3, 6, 6 + successor}
                tau = tau_from_local_defects(frozenset(defects))
                image = apply_with_tau(vector, tau)
                numerator = sum(value * value for value in image)
                denominator = sum(value * value for value in vector)
                expected_numerator, expected_denominator = expected_nd[category]
                require(denominator == expected_denominator, "(3,3) denominator mismatch")
                require(numerator >= expected_numerator, "(3,3) lower Rayleigh bound failed")
                numerator_values[category].add(numerator)

                if numerator == expected_numerator:
                    require(
                        tuple(abs(value) for value in image) == expected_min_abs[category],
                        "(3,3) minimizing image coordinates mismatch",
                    )

                opposite_tau = {index: -value for index, value in tau.items()}
                lifted_vector = alternating_lift(vector, -2)
                opposite_image = apply_with_tau(lifted_vector, opposite_tau)
                expected_opposite = tuple(
                    -(1 if index % 2 == 0 else -1) * value
                    for index, value in enumerate(image, start=-4)
                )
                require(opposite_image == expected_opposite, "opposite tau lift identity failed")
                checked += 1

    require(numerator_values == {1: {874, 902}, 2: {258}, 3: {838}}, "unexpected local numerator spectrum")

    minimum = Fraction(419, 53)
    require(minimum > C6_RIGHT, "(3,3) minimum does not exceed the c6 upper endpoint")
    margin = minimum - C6_RIGHT
    require(margin == Fraction(1_928_310_515_327, 6_625_000_000_000_000), "(3,3) margin mismatch")
    return {
        "finite_dependency_cases": checked,
        "numerators_by_predecessor_class": {
            "1": sorted(numerator_values[1]),
            "2": sorted(numerator_values[2]),
            ">=3": sorted(numerator_values[3]),
        },
        "minimum": "419/53",
        "margin": str(margin),
        "wording_correction_verified": "a=1 records possible N values 874 and 902 and uses the uniform lower bound N>=874",
    }


def expect_rejected(label: str, action: Callable[[], Any]) -> None:
    try:
        action()
    except (VerificationError, json.JSONDecodeError):
        return
    raise VerificationError(f"parser negative test was accepted: {label}")


def verify_parser_guards() -> list[str]:
    manifest_cases = {
        "duplicate-key": b'{"a":1,"a":2}\n',
        "CRLF": b'{"a":1}\r\n',
        "BOM": b'\xef\xbb\xbf{"a":1}\n',
        "trailing-json": b'{"a":1}{"b":2}\n',
        "float": b'{"a":1.0}\n',
    }
    for label, raw in manifest_cases.items():
        expect_rejected(label, lambda raw=raw: parse_json_object(raw, f"negative {label}"))

    stream_cases = {
        "stream-float": b"[[1,1],[1.0]]",
        "stream-bool": b"[[1,1],[true]]",
        "stream-oversized-int": b"[[1,1],[1000001]]",
        "stream-whitespace": b"[[1, 1],[1]]",
        "stream-trailing-json": b"[[1,1],[1]][]",
    }
    for label, raw in stream_cases.items():
        expect_rejected(label, lambda raw=raw: parse_stream_record(raw, 0))
    return [*manifest_cases, *stream_cases]


def verify_manifest() -> dict[str, Any]:
    raw = MANIFEST_PATH.read_bytes()
    payload = parse_json_object(raw, "multi-gap manifest")
    require(payload == EXPECTED_MANIFEST, "multi-gap manifest content mismatch")
    expected_raw = (json.dumps(EXPECTED_MANIFEST, ensure_ascii=True, indent=2) + "\n").encode("ascii")
    require(raw == expected_raw, "multi-gap manifest key order or byte format mismatch")
    return payload


def run() -> dict[str, Any]:
    verify_manifest()
    parser_guards = verify_parser_guards()
    c6 = verify_c6_dependency()
    words = enumerate_words()
    counts = Counter(map(sum, words))
    require(dict(counts) == EXPECTED_COUNTS, f"independent separator-mask counts mismatch: {dict(counts)}")
    require(len(words) == 31_008, f"independent word count mismatch: {len(words)}")
    stream = verify_stream(words)
    local_lemma = verify_three_three_lemma()
    result = {
        "status": "TARGET_A_TASK55_MULTIGAP_ALT_VERIFY_PASS",
        "independence": "stdlib only; no producer or existing checker import",
        "parser_negative_cases": parser_guards,
        "c6": c6,
        "stream": stream,
        "three_three_local_lemma": local_lemma,
    }
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))
    print("TARGET_A_TASK55_MULTIGAP_ALT_VERIFY_PASS")
    return result


if __name__ == "__main__":
    run()

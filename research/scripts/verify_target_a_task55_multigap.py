"""Independent fail-closed checker for Task 55 Lane D."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable


RESEARCH = Path(__file__).resolve().parents[1]
STREAM = RESEARCH / "proofs" / "task55" / "certificates" / "multigap_support18.jsonl"
MANIFEST = RESEARCH / "proofs" / "task55" / "certificates" / "multigap_support18_manifest.json"
C6_CERTIFICATE = RESEARCH / "proofs" / "task51" / "certificates" / "c6_exact_evans_elimination.json"

TOTALS = (2, 6, 10, 14, 18)
COUNTS = {2: 1, 6: 16, 10: 186, 14: 2275, 18: 28530}
THRESHOLD_NUMERATOR = 7905369311620328
THRESHOLD_DENOMINATOR = 10**15
WORD_SHA256 = "1c635aa6c50d8dc2387508cf7ce63f67e6a2ced490a3ca6b4eacbe8b8c912bfb"
STREAM_SHA256 = "9c8ef135fc11ca7b8c1761c3d45fb89c65790d97c12f2081787814f046c038bf"
POLYNOMIAL = (
    16, -520, 6913, -48448, 191768, -423904,
    484528, -270464, 137856, -19968, 256,
)


def strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_float(_: str) -> None:
    raise ValueError("floating-point JSON numbers are forbidden")


def load_json_bytes(raw: bytes) -> Any:
    if raw.startswith(b"\xef\xbb\xbf"):
        raise ValueError("BOM is forbidden")
    if b"\r" in raw:
        raise ValueError("CR/CRLF is forbidden")
    text = raw.decode("ascii")
    return json.loads(
        text,
        object_pairs_hook=strict_object,
        parse_float=reject_float,
        parse_constant=reject_float,
    )


def positive_compositions(total: int) -> Iterable[tuple[int, ...]]:
    """Recursive enumeration, intentionally unlike the producer's masks."""
    def visit(remaining: int, prefix: tuple[int, ...]) -> Iterable[tuple[int, ...]]:
        if remaining == 0:
            yield prefix
            return
        for part in range(1, remaining + 1):
            yield from visit(remaining - part, prefix + (part,))

    yield from visit(total, ())


def independently_primitive(word: tuple[int, ...]) -> bool:
    charges = [value - 4 for value in word]
    prefix = [0]
    for charge in charges:
        prefix.append(prefix[-1] + charge)
    return all(
        prefix[stop] != prefix[start]
        for start in range(len(word))
        for stop in range(start + 1, len(word) + 1)
    )


def expected_words() -> list[tuple[int, ...]]:
    return [
        word
        for total in TOTALS
        for word in positive_compositions(total)
        if len(word) >= 2
        and word <= word[::-1]
        and independently_primitive(word)
    ]


def independent_tau(word: tuple[int, ...], low: int, high: int) -> dict[int, int]:
    endpoint = sum(word)
    positions = {0}
    cursor = 0
    for gap in word:
        cursor += gap
        positions.add(cursor)

    def q(index: int) -> int:
        bulk_left = index <= 0 and index % 4 == 0
        bulk_right = index >= endpoint and (index - endpoint) % 4 == 0
        return 1 if index in positions or bulk_left or bulk_right else -1

    values = {0: 1}
    site = 0
    while site < high:
        values[site + 1] = q(site) * values[site]
        site += 1
    site = -1
    while site >= low:
        values[site] = q(site) * values[site + 1]
        site -= 1
    return values


def full_image(word: tuple[int, ...], vector: tuple[int, ...]) -> tuple[int, ...]:
    endpoint = sum(word)
    if len(vector) != endpoint + 5:
        raise ValueError("wrong support length")
    tau = independent_tau(word, -8, endpoint + 8)

    def v(index: int) -> int:
        return vector[index + 2] if -2 <= index <= endpoint + 2 else 0

    return tuple(
        v(index - 1) + v(index + 1)
        + tau[index - 2] * v(index - 2)
        + tau[index] * v(index + 2)
        for index in range(-4, endpoint + 5)
    )


def canonical_vector(vector: tuple[int, ...]) -> bool:
    nonzero = [value for value in vector if value]
    return bool(nonzero) and nonzero[0] > 0 and math.gcd(*map(abs, nonzero)) == 1


def parse_stream(path: Path) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf") or b"\r" in raw or not raw.endswith(b"\n"):
        raise ValueError("stream must be BOM-free ASCII with LF endings and a terminal LF")
    text = raw.decode("ascii")
    records = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line:
            raise ValueError(f"blank line {line_number}")
        value = json.loads(
            line,
            object_pairs_hook=strict_object,
            parse_float=reject_float,
            parse_constant=reject_float,
        )
        if json.dumps(value, separators=(",", ":"), ensure_ascii=True) != line:
            raise ValueError(f"line {line_number} is not canonical compact JSON")
        if not isinstance(value, list) or len(value) != 2:
            raise ValueError(f"line {line_number} has the wrong outer schema")
        word_raw, vector_raw = value
        if not isinstance(word_raw, list) or not isinstance(vector_raw, list):
            raise ValueError(f"line {line_number} has the wrong nested schema")
        flat = word_raw + vector_raw
        if any(type(item) is not int or abs(item) > 10**6 for item in flat):
            raise ValueError(f"line {line_number} contains a forbidden scalar")
        word = tuple(word_raw)
        vector = tuple(vector_raw)
        if not word or any(value <= 0 for value in word):
            raise ValueError(f"line {line_number} has an invalid gap word")
        records.append((word, vector))
    return records


def trim(polynomial: list[Fraction]) -> list[Fraction]:
    while polynomial and polynomial[0] == 0:
        polynomial.pop(0)
    return polynomial or [Fraction(0)]


def derivative(polynomial: list[Fraction]) -> list[Fraction]:
    degree = len(polynomial) - 1
    return trim([coefficient * (degree - index) for index, coefficient in enumerate(polynomial[:-1])])


def polynomial_remainder(dividend: list[Fraction], divisor: list[Fraction]) -> list[Fraction]:
    remainder = trim(dividend[:])
    divisor = trim(divisor[:])
    while remainder != [0] and len(remainder) >= len(divisor):
        factor = remainder[0] / divisor[0]
        for index, coefficient in enumerate(divisor):
            remainder[index] -= factor * coefficient
        remainder = trim(remainder)
    return remainder


def sturm_chain(coefficients: tuple[int, ...]) -> list[list[Fraction]]:
    chain = [[Fraction(value) for value in coefficients]]
    chain.append(derivative(chain[0]))
    while chain[-1] != [0]:
        remainder = polynomial_remainder(chain[-2], chain[-1])
        if remainder == [0]:
            break
        chain.append([-value for value in remainder])
    return chain


def evaluate(polynomial: list[Fraction], point: Fraction) -> Fraction:
    value = Fraction(0)
    for coefficient in polynomial:
        value = value * point + coefficient
    return value


def sign_variations(chain: list[list[Fraction]], point: Fraction) -> int:
    signs = []
    for polynomial in chain:
        value = evaluate(polynomial, point)
        if value:
            signs.append(1 if value > 0 else -1)
    return sum(left != right for left, right in zip(signs, signs[1:]))


def roots_in_c6_interval() -> int:
    left = Fraction(7905369311620327, 10**15)
    right = Fraction(7905369311620328, 10**15)
    chain = sturm_chain(POLYNOMIAL)
    if evaluate(chain[0], left) == 0 or evaluate(chain[0], right) == 0:
        raise AssertionError("c6 isolating endpoint is a root")
    return sign_variations(chain, left) - sign_variations(chain, right)


def local_image(
    left_defects: set[int], successor: int, vector: tuple[int, ...], tau_anchor: int = 1
) -> tuple[int, ...]:
    defects = left_defects | {0, 3, 6, 6 + successor}

    def q(index: int) -> int:
        return 1 if index in defects else -1

    tau = {0: tau_anchor}
    for index in range(0, 13):
        tau[index + 1] = q(index) * tau[index]
    for index in range(-1, -9, -1):
        tau[index] = q(index) * tau[index + 1]
    values = {index - 2: value for index, value in enumerate(vector)}
    return tuple(
        values.get(index - 1, 0) + values.get(index + 1, 0)
        + tau[index - 2] * values.get(index - 2, 0)
        + tau[index] * values.get(index + 2, 0)
        for index in range(-4, 11)
    )


def verify_local_lemma(manifest: dict[str, Any]) -> bool:
    first = (1, 0, 3, 4, 3, 5, 4, 4, 3, 1, 2)
    second = (2, 0, 0, -3, -2, -2, -2, -2, -1, -1, -1)
    expected = {1: (first, 874, 106), 2: (second, 258, 32), 3: (first, 838, 106)}
    numerator_values = {1: set(), 2: set(), 3: set()}
    checked = 0
    for predecessor in (1, 2, 3, 4, 5):
        category = min(predecessor, 3)
        vector, lower_numerator, denominator = expected[category]
        free_left = tuple(range(-4, -predecessor)) if predecessor <= 4 else ()
        for mask in range(1 << len(free_left)):
            left_defects = {-predecessor} | {
                index for bit, index in enumerate(free_left) if mask & (1 << bit)
            }
            for successor in (1, 2):
                image = local_image(left_defects, successor, vector)
                numerator = sum(value * value for value in image)
                if numerator < lower_numerator:
                    return False
                if sum(value * value for value in vector) != denominator:
                    return False
                numerator_values[category].add(numerator)
                lifted = tuple(
                    (1 if index % 2 == 0 else -1) * value
                    for index, value in enumerate(vector, start=-2)
                )
                opposite = local_image(left_defects, successor, lifted, tau_anchor=-1)
                expected_opposite = tuple(
                    -(1 if index % 2 == 0 else -1) * value
                    for index, value in enumerate(image, start=-4)
                )
                if opposite != expected_opposite:
                    return False
                checked += 1
    if numerator_values != {1: {874, 902}, 2: {258}, 3: {838}} or checked != 32:
        return False
    margin = Fraction(419, 53) - Fraction(THRESHOLD_NUMERATOR, THRESHOLD_DENOMINATOR)
    expected_block = {
        "status": "ANALYTIC_PROVED_ARBITRARY_FINITE_CORE_LENGTH",
        "support_relative_to_first_motif_defect": [-2, 8],
        "tau_anchor": "tau_x=1",
        "cases": [
            {"predecessor_gap": "1", "vector": list(first), "N_lower_bound": 874, "possible_N": [874, 902], "D": 106},
            {"predecessor_gap": "2", "vector": list(second), "N_lower_bound": 258, "possible_N": [258], "D": 32},
            {"predecessor_gap": ">=3", "vector": list(first), "N_lower_bound": 838, "possible_N": [838], "D": 106},
        ],
        "finite_dependency_cases_checked": 32,
        "minimum_exact_margin_over_c6_upper": str(margin),
        "opposite_tau_lift": "v_i -> (-1)^i v_i because A_(-tau)=-D A_tau D",
    }
    return manifest["three_three_local_lemma"] == expected_block


def exact_keys(value: dict[str, Any], expected: set[str], label: str) -> None:
    if set(value) != expected:
        raise AssertionError(f"{label} keys differ: {set(value) ^ expected}")


def verify(
    stream_path: Path = STREAM,
    manifest_path: Path = MANIFEST,
) -> dict[str, bool]:
    manifest = load_json_bytes(manifest_path.read_bytes())
    if not isinstance(manifest, dict):
        raise ValueError("manifest must be an object")
    exact_keys(manifest, {
        "schema_version", "status", "evidence", "scope", "open_interface",
        "witness_generation", "strict_threshold", "stream", "statistics",
        "c6_dependency", "three_three_local_lemma", "proof_boundary",
    }, "manifest")

    records = parse_stream(stream_path)
    words = expected_words()
    if len(words) != 31008:
        raise AssertionError("independent enumeration count changed")
    if [word for word, _ in records] != words:
        raise AssertionError("stream has a missing, duplicate, unordered, or noncanonical word")

    counts = {total: 0 for total in TOTALS}
    word_digest = hashlib.sha256()
    maximum_coordinate = maximum_numerator = maximum_denominator = 0
    ratios: list[tuple[Fraction, tuple[int, ...], tuple[int, ...], int, int]] = []
    for word, vector in records:
        endpoint = sum(word)
        counts[endpoint] += 1
        if word > word[::-1] or not independently_primitive(word):
            raise AssertionError("noncanonical or nonprimitive word survived")
        if not canonical_vector(vector):
            raise AssertionError("vector sign/gcd normalization failed")
        image = full_image(word, vector)
        numerator = sum(value * value for value in image)
        denominator = sum(value * value for value in vector)
        if numerator * THRESHOLD_DENOMINATOR <= THRESHOLD_NUMERATOR * denominator:
            raise AssertionError((word, numerator, denominator))
        word_digest.update((json.dumps(list(word), separators=(",", ":")) + "\n").encode("ascii"))
        maximum_coordinate = max(maximum_coordinate, *map(abs, vector))
        maximum_numerator = max(maximum_numerator, numerator)
        maximum_denominator = max(maximum_denominator, denominator)
        ratios.append((Fraction(numerator, denominator), word, vector, numerator, denominator))

    weakest_ratio = min(row[0] for row in ratios)
    weakest = [row for row in ratios if row[0] == weakest_ratio]
    stream_bytes = stream_path.read_bytes()
    c6_bytes = C6_CERTIFICATE.read_bytes()
    c6_data = load_json_bytes(c6_bytes)
    c6 = c6_data["c6"]

    exact_keys(manifest["scope"], {
        "totals", "minimum_gap_count", "equivalence", "primitive",
        "counts_by_total", "total_count",
    }, "scope")
    exact_keys(manifest["open_interface"], {
        "defects", "q", "tau_anchor", "tau_recurrence", "operator",
        "support", "image_window", "forbidden_truncation",
    }, "open_interface")
    exact_keys(manifest["witness_generation"], {"rule", "top_vector", "acceptance"}, "witness_generation")
    exact_keys(manifest["strict_threshold"], {"numerator", "denominator", "test"}, "strict_threshold")
    exact_keys(manifest["stream"], {"path", "format", "line_count", "word_sha256", "sha256"}, "stream")
    exact_keys(manifest["statistics"], {
        "maximum_absolute_vector_coordinate", "maximum_numerator", "maximum_denominator",
        "unique_weakest_word", "unique_weakest_vector", "weakest_numerator", "weakest_denominator",
    }, "statistics")
    exact_keys(manifest["c6_dependency"], {
        "path", "sha256", "status", "polynomial_coefficients_descending", "isolating_interval",
    }, "c6_dependency")
    exact_keys(manifest["proof_boundary"], {
        "bounded_class", "three_three_subclass", "universal_B0_to_B2",
        "reference_cell_insertion_removal",
    }, "proof_boundary")

    preflight = {
        "status": manifest["schema_version"] == 1
        and manifest["status"] == "TASK55_MULTIGAP_SUPPORT18_COMPUTER_ASSISTED_PROVED"
        and manifest["evidence"] == "COMPUTER_ASSISTED_PROVED",
        "scope": manifest["scope"] == {
            "totals": list(TOTALS),
            "minimum_gap_count": 2,
            "equivalence": "translation fixed by x_0=0; reflection canonical=min(g,reversed(g))",
            "primitive": "no nonempty contiguous subword has zero charge sum(g_i-4)",
            "counts_by_total": {str(total): COUNTS[total] for total in TOTALS},
            "total_count": 31008,
        } and counts == COUNTS,
        "open_interface": manifest["open_interface"] == {
            "defects": "(-4 Z_{>=0}) union {x_0,...,x_m} union (S+4 Z_{>=0})",
            "q": "Q_i=+1 at defects and -1 otherwise",
            "tau_anchor": "tau_0=1",
            "tau_recurrence": "tau_(i+1)=Q_i tau_i",
            "operator": "(Av)_k=v_(k-1)+v_(k+1)+tau_(k-2)v_(k-2)+tau_k v_(k+2)",
            "support": "I_g=[-2,S+2] intersect Z",
            "image_window": "J_g=[-4,S+4] intersect Z",
            "forbidden_truncation": "do not replace ||Av||^2 by ||P_I A P_I v||^2",
        },
        "witness_rule": manifest["witness_generation"]["rule"]
        == "round(20*u), divide coordinate gcd, make first nonzero coordinate positive"
        and manifest["witness_generation"]["top_vector"]
        == "FP64 top-branch location followed by 80- and 120-digit Rayleigh-quotient iteration; identical rounded vectors required"
        and manifest["witness_generation"]["acceptance"]
        == "integer recomputation of the full Av on J_g only",
        "threshold": manifest["strict_threshold"] == {
            "numerator": THRESHOLD_NUMERATOR,
            "denominator": THRESHOLD_DENOMINATOR,
            "test": "N*1000000000000000 > 7905369311620328*D",
        },
        "stream": manifest["stream"] == {
            "path": "research/proofs/task55/certificates/multigap_support18.jsonl",
            "format": "one compact ASCII JSON array [[g_1,...,g_m],[v_-2,...,v_(S+2)]] per LF-terminated line",
            "line_count": 31008,
            "word_sha256": WORD_SHA256,
            "sha256": STREAM_SHA256,
        }
        and word_digest.hexdigest() == WORD_SHA256
        and hashlib.sha256(stream_bytes).hexdigest() == STREAM_SHA256,
        "statistics": len(weakest) == 1
        and (maximum_coordinate, maximum_numerator, maximum_denominator) == (11, 6226, 442)
        and manifest["statistics"] == {
            "maximum_absolute_vector_coordinate": maximum_coordinate,
            "maximum_numerator": maximum_numerator,
            "maximum_denominator": maximum_denominator,
            "unique_weakest_word": list(weakest[0][1]),
            "unique_weakest_vector": list(weakest[0][2]),
            "weakest_numerator": weakest[0][3],
            "weakest_denominator": weakest[0][4],
        }
        and weakest[0][1:] == (
            (3, 3), (3, 0, 5, 7, 6, 9, 7, 8, 6, 2, 4), 2930, 369
        ),
        "c6_dependency": manifest["c6_dependency"] == {
            "path": "research/proofs/task51/certificates/c6_exact_evans_elimination.json",
            "sha256": hashlib.sha256(c6_bytes).hexdigest(),
            "status": "C6_DEGREE10_EVANS_POLYNOMIAL_PROVED",
            "polynomial_coefficients_descending": list(POLYNOMIAL),
            "isolating_interval": [
                "7905369311620327/1000000000000000",
                "988171163952541/125000000000000",
            ],
        }
        and c6["status"] == "C6_DEGREE10_EVANS_POLYNOMIAL_PROVED"
        and c6["c6_polynomial"]
        == "16*y**10 - 520*y**9 + 6913*y**8 - 48448*y**7 + 191768*y**6 - 423904*y**5 + 484528*y**4 - 270464*y**3 + 137856*y**2 - 19968*y + 256"
        and c6["c6_interval"] == [
            "7905369311620327/1000000000000000",
            "988171163952541/125000000000000",
        ]
        and roots_in_c6_interval() == 1,
        "local_lemma": verify_local_lemma(manifest),
        "proof_boundary": manifest["proof_boundary"] == {
            "bounded_class": "PROVED only for the 31008 canonical primitive multi-gap cores with S<=18 in the listed residue class",
            "three_three_subclass": "PROVED for arbitrary finite core length when a consecutive (3,3) motif occurs",
            "universal_B0_to_B2": "OPEN",
            "reference_cell_insertion_removal": "REJECTED: it multiplies a non-scalar bulk monodromy and is not a spectral equivalence",
        },
    }
    if not all(preflight.values()):
        raise AssertionError(preflight)
    print("TARGET_A_TASK55_MULTIGAP_VERIFY_PASS")
    return preflight


if __name__ == "__main__":
    verify()

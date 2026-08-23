"""Produce exact finite-support witnesses for Task 55 Lane D."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable

import mpmath as mp
import numpy as np


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "proofs" / "task55" / "certificates"
STREAM = OUTPUT / "multigap_support18.jsonl"
MANIFEST = OUTPUT / "multigap_support18_manifest.json"
C6_CERTIFICATE = RESEARCH / "proofs" / "task51" / "certificates" / "c6_exact_evans_elimination.json"

TOTALS = (2, 6, 10, 14, 18)
C6_LOWER = Fraction(7905369311620327, 10**15)
C6_UPPER = Fraction(7905369311620328, 10**15)
EXPECTED_COUNTS = {2: 1, 6: 16, 10: 186, 14: 2275, 18: 28530}
EXPECTED_WORD_SHA256 = "1c635aa6c50d8dc2387508cf7ce63f67e6a2ced490a3ca6b4eacbe8b8c912bfb"
EXPECTED_STREAM_SHA256 = "9c8ef135fc11ca7b8c1761c3d45fb89c65790d97c12f2081787814f046c038bf"


def compositions(total: int) -> Iterable[tuple[int, ...]]:
    """Generate positive compositions independently from separator masks."""
    for mask in range(1 << (total - 1)):
        word = []
        previous = 0
        for index in range(total - 1):
            if mask & (1 << index):
                word.append(index + 1 - previous)
                previous = index + 1
        word.append(total - previous)
        yield tuple(word)


def primitive(word: tuple[int, ...]) -> bool:
    charges = tuple(gap - 4 for gap in word)
    for start in range(len(charges)):
        subtotal = 0
        for stop in range(start, len(charges)):
            subtotal += charges[stop]
            if subtotal == 0:
                return False
    return True


def canonical_words() -> list[tuple[int, ...]]:
    words = [
        word
        for total in TOTALS
        for word in compositions(total)
        if len(word) >= 2 and word <= tuple(reversed(word)) and primitive(word)
    ]
    return sorted(words, key=lambda word: (sum(word), word))


def defect_positions(word: tuple[int, ...]) -> set[int]:
    positions = {0}
    endpoint = 0
    for gap in word:
        endpoint += gap
        positions.add(endpoint)
    return positions


def q_value(index: int, word: tuple[int, ...], positions: set[int]) -> int:
    endpoint = sum(word)
    left_bulk = index <= 0 and index % 4 == 0
    right_bulk = index >= endpoint and (index - endpoint) % 4 == 0
    return 1 if left_bulk or right_bulk or index in positions else -1


def tau_values(word: tuple[int, ...], low: int, high: int) -> dict[int, int]:
    positions = defect_positions(word)
    tau = {0: 1}
    for index in range(high):
        tau[index + 1] = q_value(index, word, positions) * tau[index]
    for index in range(-1, low - 1, -1):
        tau[index] = q_value(index, word, positions) * tau[index + 1]
    return tau


def open_operator(word: tuple[int, ...]) -> np.ndarray:
    endpoint = sum(word)
    support = tuple(range(-2, endpoint + 3))
    output = tuple(range(-4, endpoint + 5))
    column = {index: local for local, index in enumerate(support)}
    tau = tau_values(word, -8, endpoint + 8)
    matrix = np.zeros((len(output), len(support)), dtype=np.int64)
    for row, index in enumerate(output):
        for source, coefficient in (
            (index - 1, 1),
            (index + 1, 1),
            (index - 2, tau[index - 2]),
            (index + 2, tau[index]),
        ):
            if source in column:
                matrix[row, column[source]] += coefficient
    return matrix


def normalize_integer_vector(values: Iterable[int]) -> tuple[int, ...]:
    vector = tuple(int(value) for value in values)
    nonzero = [value for value in vector if value]
    if not nonzero:
        raise AssertionError("rounded top vector vanished")
    divisor = math.gcd(*map(abs, nonzero))
    vector = tuple(value // divisor for value in vector)
    if next(value for value in vector if value) < 0:
        vector = tuple(-value for value in vector)
    return vector


def rounded_vector(values: Iterable[mp.mpf | float]) -> tuple[int, ...]:
    return normalize_integer_vector(int(mp.nint(20 * value)) for value in values)


def high_precision_proposal(matrix: np.ndarray) -> tuple[int, ...]:
    """Locate in FP64, then require identical 80/120-digit RQI rounding."""
    gram = matrix.T @ matrix
    _, eigenvectors = np.linalg.eigh(gram.astype(np.float64))
    initial = [mp.mpf(float(value)) for value in eigenvectors[:, -1]]
    proposals = []
    current = initial
    for digits in (80, 120):
        with mp.workdps(digits):
            exact = mp.matrix([[int(value) for value in row] for row in gram.tolist()])
            vector = mp.matrix([mp.mpf(value) for value in current])
            vector /= mp.norm(vector)
            rayleigh = (vector.T * exact * vector)[0]
            vector = mp.lu_solve(exact - rayleigh * mp.eye(len(current)), vector)
            vector /= mp.norm(vector)
            current = [mp.mpf(value) for value in vector]
            proposals.append(rounded_vector(current))
    if proposals[0] != proposals[1]:
        raise AssertionError("80/120-digit witness proposals disagree")
    return proposals[1]


def fast_proposal(matrix: np.ndarray) -> tuple[int, ...]:
    """Development-only proposal path; exact acceptance below is unchanged."""
    _, eigenvectors = np.linalg.eigh((matrix.T @ matrix).astype(np.float64))
    return normalize_integer_vector(np.rint(20 * eigenvectors[:, -1]).astype(np.int64))


def exact_rayleigh(
    word: tuple[int, ...], vector: tuple[int, ...]
) -> tuple[int, int, tuple[int, ...]]:
    endpoint = sum(word)
    values = {index: vector[index + 2] for index in range(-2, endpoint + 3)}
    tau = tau_values(word, -8, endpoint + 8)
    image = tuple(
        values.get(index - 1, 0)
        + values.get(index + 1, 0)
        + tau[index - 2] * values.get(index - 2, 0)
        + tau[index] * values.get(index + 2, 0)
        for index in range(-4, endpoint + 5)
    )
    numerator = sum(value * value for value in image)
    denominator = sum(value * value for value in vector)
    return numerator, denominator, image


def compact_line(word: tuple[int, ...], vector: tuple[int, ...]) -> bytes:
    return (json.dumps([list(word), list(vector)], separators=(",", ":")) + "\n").encode("ascii")


def build_manifest(stream_bytes: bytes, records: list[dict[str, object]], proposal: str) -> dict[str, object]:
    counts = {total: sum(sum(row["word"]) == total for row in records) for total in TOTALS}
    weakest = min(records, key=lambda row: Fraction(row["numerator"], row["denominator"]))
    c6_bytes = C6_CERTIFICATE.read_bytes()
    c6_data = json.loads(c6_bytes)
    if c6_data["c6"]["status"] != "C6_DEGREE10_EVANS_POLYNOMIAL_PROVED":
        raise AssertionError("Task 51 c6 dependency has the wrong status")
    word_digest = hashlib.sha256()
    for row in records:
        word_digest.update((json.dumps(row["word"], separators=(",", ":")) + "\n").encode("ascii"))
    return {
        "schema_version": 1,
        "status": "TASK55_MULTIGAP_SUPPORT18_COMPUTER_ASSISTED_PROVED",
        "evidence": "COMPUTER_ASSISTED_PROVED",
        "scope": {
            "totals": list(TOTALS),
            "minimum_gap_count": 2,
            "equivalence": "translation fixed by x_0=0; reflection canonical=min(g,reversed(g))",
            "primitive": "no nonempty contiguous subword has zero charge sum(g_i-4)",
            "counts_by_total": {str(total): counts[total] for total in TOTALS},
            "total_count": len(records),
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
            "top_vector": proposal,
            "acceptance": "integer recomputation of the full Av on J_g only",
        },
        "strict_threshold": {
            "numerator": 7905369311620328,
            "denominator": 10**15,
            "test": "N*1000000000000000 > 7905369311620328*D",
        },
        "stream": {
            "path": "research/proofs/task55/certificates/multigap_support18.jsonl",
            "format": "one compact ASCII JSON array [[g_1,...,g_m],[v_-2,...,v_(S+2)]] per LF-terminated line",
            "line_count": len(records),
            "word_sha256": word_digest.hexdigest(),
            "sha256": hashlib.sha256(stream_bytes).hexdigest(),
        },
        "statistics": {
            "maximum_absolute_vector_coordinate": max(row["max_abs"] for row in records),
            "maximum_numerator": max(row["numerator"] for row in records),
            "maximum_denominator": max(row["denominator"] for row in records),
            "unique_weakest_word": weakest["word"],
            "unique_weakest_vector": weakest["vector"],
            "weakest_numerator": weakest["numerator"],
            "weakest_denominator": weakest["denominator"],
        },
        "c6_dependency": {
            "path": "research/proofs/task51/certificates/c6_exact_evans_elimination.json",
            "sha256": hashlib.sha256(c6_bytes).hexdigest(),
            "status": c6_data["c6"]["status"],
            "polynomial_coefficients_descending": [
                16, -520, 6913, -48448, 191768, -423904,
                484528, -270464, 137856, -19968, 256,
            ],
            "isolating_interval": [str(C6_LOWER), str(C6_UPPER)],
        },
        "three_three_local_lemma": {
            "status": "ANALYTIC_PROVED_ARBITRARY_FINITE_CORE_LENGTH",
            "support_relative_to_first_motif_defect": [-2, 8],
            "tau_anchor": "tau_x=1",
            "cases": [
                {"predecessor_gap": "1", "vector": [1, 0, 3, 4, 3, 5, 4, 4, 3, 1, 2], "N_lower_bound": 874, "possible_N": [874, 902], "D": 106},
                {"predecessor_gap": "2", "vector": [2, 0, 0, -3, -2, -2, -2, -2, -1, -1, -1], "N_lower_bound": 258, "possible_N": [258], "D": 32},
                {"predecessor_gap": ">=3", "vector": [1, 0, 3, 4, 3, 5, 4, 4, 3, 1, 2], "N_lower_bound": 838, "possible_N": [838], "D": 106},
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


def run(full_high_precision: bool = True) -> dict[str, object]:
    words = canonical_words()
    counts = {total: sum(sum(word) == total for word in words) for total in TOTALS}
    if counts != EXPECTED_COUNTS or len(words) != 31008:
        raise AssertionError((counts, len(words)))

    records = []
    chunks = []
    proposal = high_precision_proposal if full_high_precision else fast_proposal
    for index, word in enumerate(words, start=1):
        vector = proposal(open_operator(word))
        numerator, denominator, _ = exact_rayleigh(word, vector)
        if numerator * 10**15 <= 7905369311620328 * denominator:
            raise AssertionError((word, vector, numerator, denominator))
        chunks.append(compact_line(word, vector))
        records.append({
            "word": list(word),
            "vector": list(vector),
            "numerator": numerator,
            "denominator": denominator,
            "max_abs": max(map(abs, vector)),
        })
        if index % 5000 == 0:
            print(f"proposed and exactly accepted {index}/{len(words)} witnesses", flush=True)

    stream_bytes = b"".join(chunks)
    proposal_text = (
        "FP64 top-branch location followed by 80- and 120-digit Rayleigh-quotient iteration; identical rounded vectors required"
        if full_high_precision
        else "DEVELOPMENT_ONLY_FP64; exact integer acceptance unchanged"
    )
    manifest = build_manifest(stream_bytes, records, proposal_text)
    if manifest["stream"]["word_sha256"] != EXPECTED_WORD_SHA256:
        raise AssertionError("word stream digest changed")
    if manifest["stream"]["sha256"] != EXPECTED_STREAM_SHA256:
        raise AssertionError("witness stream digest changed")

    OUTPUT.mkdir(parents=True, exist_ok=True)
    STREAM.write_bytes(stream_bytes)
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="ascii")
    print(json.dumps({
        "status": manifest["status"],
        "records": len(records),
        "stream_sha256": manifest["stream"]["sha256"],
        "weakest": manifest["statistics"]["unique_weakest_word"],
    }, indent=2))
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--fast-proposals",
        action="store_true",
        help="development-only FP64 proposal path; exact acceptance and fixed digests still apply",
    )
    args = parser.parse_args()
    run(full_high_precision=not args.fast_proposals)


if __name__ == "__main__":
    main()

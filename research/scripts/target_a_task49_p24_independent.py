"""Independent Task 49 audit of the complete p=17..24 exact partition."""

from __future__ import annotations

import json
import math
import multiprocessing as mp
from fractions import Fraction
from pathlib import Path
from typing import Iterator

import numpy as np

from target_a_task47_common import write_json


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "reproducibility" / "task49" / "p24_independent"
TARGET = (1, 0, 0, 0, 1, 0, 0, 0)


def necklaces(n: int) -> Iterator[tuple[int, ...]]:
    word = [0] * (n + 1)

    def visit(position: int, period: int) -> Iterator[tuple[int, ...]]:
        if position > n:
            if n % period == 0:
                yield tuple(word[1:])
            return
        word[position] = word[position - period]
        yield from visit(position + 1, period)
        for value in range(word[position - period] + 1, 2):
            word[position] = value
            yield from visit(position + 1, position)

    yield from visit(1, 1)


def rotations(word: tuple[int, ...]) -> list[tuple[int, ...]]:
    return [word[shift:] + word[:shift] for shift in range(len(word))]


def bracelet_representatives(n: int) -> Iterator[tuple[tuple[int, ...], int]]:
    for word in necklaces(n):
        if sum(word) % 2 != n % 2:
            continue
        reflected_minimum = min(rotations(tuple(reversed(word))))
        if word > reflected_minimum:
            continue
        images = set(rotations(word)) | set(rotations(tuple(reversed(word))))
        yield word, len(images)


def canonical_code(word: tuple[int, ...]) -> int:
    images = rotations(word) + rotations(tuple(reversed(word)))
    return min(sum(bit << index for index, bit in enumerate(image)) for image in images)


def primitive_period(word: tuple[int, ...]) -> int:
    for period in range(1, len(word) + 1):
        if len(word) % period == 0 and all(word[i] == word[i % period] for i in range(len(word))):
            return period
    raise AssertionError


def tau_lift(bits: tuple[int, ...]) -> tuple[int, ...]:
    q = tuple(1 if bit else -1 for bit in bits)
    tau = [1]
    for value in q[:-1]:
        tau.append(tau[-1] * value)
    if tau[-1] * q[-1] != 1:
        raise AssertionError("illegal independent Q lift")
    return tuple(tau)


def first_positive(bits: tuple[int, ...], maximum: int = 16) -> int | None:
    tau = tau_lift(bits)
    n = len(bits)
    states = [{start: 1} for start in range(n)]
    previous = None
    for length in range(1, 2 * (maximum + 1) + 1):
        updated_states = []
        for state in states:
            updated = {}
            for position, amplitude in state.items():
                transitions = (
                    (position - 1, 1), (position + 1, 1),
                    (position - 2, tau[(position - 2) % n]), (position + 2, tau[position % n]),
                )
                for endpoint, coefficient in transitions:
                    updated[endpoint] = updated.get(endpoint, 0) + amplitude * coefficient
            updated_states.append(updated)
        states = updated_states
        if length % 2:
            continue
        moment = sum(states[start].get(start, 0) for start in range(n))
        if previous is not None:
            k = length // 2 - 1
            if moment - 8 * previous > 0:
                return k
        previous = moment
    return None


def independent_matrix(bits: tuple[int, ...], alpha: int) -> np.ndarray:
    n = len(bits)
    tau = tau_lift(bits)
    step1 = [1] * n
    step1[-1] = alpha
    step2 = [tau[i] * step1[i] * step1[(i + 1) % n] for i in range(n)]
    matrix = np.zeros((n, n), dtype=np.int64)
    for i in range(n):
        for step, sign in ((1, step1[i]), (2, step2[i])):
            j = (i + step) % n
            matrix[i, j] = matrix[j, i] = sign
    return matrix


def exact_endpoint(bits: tuple[int, ...]) -> dict:
    best = Fraction(0)
    best_alpha = 0
    for alpha in (-1, 1):
        matrix = independent_matrix(bits, alpha)
        values, vectors = np.linalg.eigh(matrix.astype(float))
        vector = vectors[:, int(np.argmax(np.abs(values)))]
        integer = np.rint(vector * 10**9).astype(np.int64)
        image = matrix @ integer
        quotient = Fraction(sum(int(x) ** 2 for x in image), sum(int(x) ** 2 for x in integer))
        if quotient > best:
            best, best_alpha = quotient, alpha
    return {"bound": str(best), "alpha": best_alpha, "passes_1561_over_200": best > Fraction(1561, 200)}


def target_repetition(bits: tuple[int, ...]) -> bool:
    if len(bits) % 8:
        return False
    repeated = TARGET * (len(bits) // 8)
    return min(rotations(bits) + rotations(tuple(reversed(bits)))) == min(rotations(repeated) + rotations(tuple(reversed(repeated))))


def audit_period(period: int) -> dict:
    orbit_count = 0
    multiplicity = 0
    moment = 0
    strict = 0
    equality = 0
    lower = 0
    unresolved = 0
    survivors = []
    codes = set()
    for bits, orbit_size in bracelet_representatives(period):
        orbit_count += 1
        multiplicity += orbit_size
        code = canonical_code(bits)
        if code in codes:
            raise AssertionError("independent duplicate bracelet")
        codes.add(code)
        first = first_positive(bits)
        if first is not None:
            moment += 1
            continue
        if target_repetition(bits):
            equality += 1
            survivors.append({"canonical_q_code": code, "classification": "EQUALITY", "primitive_q_period": primitive_period(bits), "primitive_tau_period": primitive_period(tau_lift(bits))})
            continue
        certificate = exact_endpoint(bits)
        if certificate["passes_1561_over_200"]:
            strict += 1
            classification = "STRICT"
        else:
            unresolved += 1
            classification = "UNRESOLVED"
        survivors.append({"canonical_q_code": code, "classification": classification, "certificate": certificate, "primitive_q_period": primitive_period(bits), "primitive_tau_period": primitive_period(tau_lift(bits))})
    if multiplicity != 1 << (period - 1):
        raise AssertionError("independent orbit multiplicity failed")
    return {
        "period": period,
        "legal_dihedral_orbits": orbit_count,
        "represented_legal_words": multiplicity,
        "moment": moment,
        "strict": strict,
        "equality": equality,
        "lower": lower,
        "unresolved": unresolved,
        "consumed": moment + strict + equality + lower + unresolved,
        "survivors": survivors,
    }


def run() -> dict:
    periods = list(range(17, 25))
    with mp.get_context("spawn").Pool(8) as pool:
        rows = pool.map(audit_period, periods)
    totals = {key: sum(row[key] for row in rows) for key in ("legal_dihedral_orbits", "moment", "strict", "equality", "lower", "unresolved", "consumed")}
    expected = {"legal_dihedral_orbits": 370100, "moment": 369916, "strict": 183, "equality": 1, "lower": 0, "unresolved": 0, "consumed": 370100}
    status = "P24_AUDIT_PASS" if totals == expected and all(row["consumed"] == row["legal_dihedral_orbits"] for row in rows) else "P24_AUDIT_FAIL"
    payload = {
        "status": status,
        "independence": "new necklace/bracelet generation, Q lift, moments, finite matrices, and integer Rayleigh recomputation; no canonical or moment helper imported",
        "totals": totals,
        "expected": expected,
        "periods": rows,
        "destructive_accounting_remaining": totals["legal_dihedral_orbits"] - totals["consumed"],
    }
    OUTPUT.mkdir(parents=True, exist_ok=True)
    write_json(OUTPUT / "summary.json", payload)
    print(json.dumps({"status": status, "totals": totals}, indent=2))
    return payload


if __name__ == "__main__":
    run()

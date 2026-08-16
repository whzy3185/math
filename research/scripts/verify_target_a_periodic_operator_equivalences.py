"""Independently verify periodic operator conjugacies and zone folding."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Iterable


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CERTIFICATE = RESEARCH_ROOT / "proofs" / "target_a_periodic_operator_equivalences.json"


class PeriodicEquivalenceError(RuntimeError):
    pass


def _check(condition: bool, message: str) -> None:
    if not condition:
        raise PeriodicEquivalenceError(message)


def legal_q_words(p: int) -> Iterable[tuple[int, ...]]:
    for code in range(1 << max(p - 1, 0)):
        prefix = tuple(1 if (code >> i) & 1 else -1 for i in range(p - 1))
        product = 1
        for value in prefix:
            product *= value
        yield prefix + (product,)


def lift(q_word: tuple[int, ...]) -> tuple[int, ...]:
    tau = [1]
    for value in q_word[:-1]:
        tau.append(tau[-1] * value)
    _check(tau[-1] * q_word[-1] == tau[0], "LIFT_CLOSURE_FAIL")
    return tuple(tau)


def flux(tau: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(tau[i] * tau[(i + 1) % len(tau)] for i in range(len(tau)))


def primitive_period(word: tuple[int, ...]) -> int:
    for period in range(1, len(word) + 1):
        if len(word) % period == 0 and all(word[i] == word[i % period] for i in range(len(word))):
            return period
    raise AssertionError("unreachable")


def coefficient(tau: tuple[int, ...], i: int, step: int) -> int:
    p = len(tau)
    if step in (-1, 1):
        return 1
    if step == 2:
        return tau[i % p]
    if step == -2:
        return tau[(i - 2) % p]
    raise ValueError(step)


def kernel(tau: tuple[int, ...], i: int) -> dict[int, int]:
    return {i + step: coefficient(tau, i, step) for step in (-2, -1, 1, 2)}


def verify_translation(tau: tuple[int, ...], shift: int) -> None:
    p = len(tau)
    moved = tuple(tau[(i - shift) % p] for i in range(p))
    for i in range(p):
        expected = {j + shift: value for j, value in kernel(tau, i - shift).items()}
        _check(kernel(moved, i) == expected, f"TRANSLATION_FAIL:p={p}:r={shift}:i={i}")
    expected_q = tuple(flux(tau)[(i - shift) % p] for i in range(p))
    _check(flux(moved) == expected_q, f"TRANSLATION_FLUX_FAIL:p={p}:r={shift}")


def verify_reflection(tau: tuple[int, ...]) -> None:
    p = len(tau)
    reflected = tuple(tau[(-i - 2) % p] for i in range(p))
    for i in range(p):
        expected = {-j: value for j, value in kernel(tau, -i).items()}
        _check(kernel(reflected, i) == expected, f"REFLECTION_FAIL:p={p}:i={i}")
    expected_q = tuple(flux(tau)[(-i - 3) % p] for i in range(p))
    _check(flux(reflected) == expected_q, f"REFLECTION_FLUX_FAIL:p={p}")


def verify_negation(tau: tuple[int, ...]) -> None:
    negative = tuple(-value for value in tau)
    for i in range(len(tau)):
        for j, value in kernel(tau, i).items():
            conjugated = -((-1) ** i) * value * ((-1) ** j)
            _check(kernel(negative, i)[j] == conjugated, f"NEGATION_FAIL:p={len(tau)}:i={i}:j={j}")


def verify_zone_folding(tau: tuple[int, ...], q: int) -> int:
    p = len(tau)
    _check(p % q == 0 and q < p, "ZONE_FOLD_DOMAIN_FAIL")
    primitive = tau[:q]
    _check(tau == primitive * (p // q), "ZONE_FOLD_REPETITION_FAIL")
    checks = 0
    for i in range(p):
        r = i % q
        k = (i - r) // q
        for step in (-2, -1, 1, 2):
            j = i + step
            target_r = j % q
            target_block = (j - target_r) // q
            primitive_j = r + step
            primitive_r = primitive_j % q
            primitive_block = (primitive_j - primitive_r) // q
            _check(target_r == primitive_r, f"ZONE_FOLD_RESIDUE_FAIL:p={p}:q={q}:i={i}:s={step}")
            _check(target_block - k == primitive_block, f"ZONE_FOLD_EXPONENT_FAIL:p={p}:q={q}:i={i}:s={step}")
            _check(coefficient(tau, i, step) == coefficient(primitive, r, step), f"ZONE_FOLD_COEFFICIENT_FAIL:p={p}:q={q}:i={i}:s={step}")
            checks += 1
    return checks


def build_audit() -> dict:
    words = 0
    translation_checks = 0
    reflection_checks = 0
    negation_checks = 0
    repeated_words = 0
    zone_fold_transition_checks = 0
    repeated_by_period: dict[str, int] = {}
    for p in range(1, 17):
        repeated_at_p = 0
        for q_word in legal_q_words(p):
            words += 1
            tau = lift(q_word)
            for shift in range(p):
                verify_translation(tau, shift)
                translation_checks += 1
            verify_reflection(tau)
            reflection_checks += 1
            verify_negation(tau)
            negation_checks += 1
            q = primitive_period(tau)
            if q < p:
                repeated_words += 1
                repeated_at_p += 1
                zone_fold_transition_checks += verify_zone_folding(tau, q)
        repeated_by_period[str(p)] = repeated_at_p
    return {
        "schema_version": "1.0.0",
        "status": "TARGET_A_PERIODIC_OPERATOR_EQUIVALENCES_PASS",
        "periods": [1, 16],
        "legal_q_words": words,
        "translation_word_checks": translation_checks,
        "reflection_word_checks": reflection_checks,
        "negation_word_checks": negation_checks,
        "repeated_words": repeated_words,
        "repeated_words_by_period": repeated_by_period,
        "zone_fold_transition_checks": zone_fold_transition_checks,
        "identities": {
            "translation": "T_r A_tau T_r^-1=A_(tau shifted by r)",
            "reflection": "J A_tau J=A_(tau'_i=tau_(-i-2))",
            "negation": "A_(-tau)=-D A_tau D",
            "zone_folding": "H_(mq)(z)~=direct_sum_(w^m=z) H_q(w)"
        },
        "finite_infinite_boundary": "zone folding concerns periodic infinite-volume fibers; finite sectors additionally require z^L=alpha"
    }


def verify_certificate(certificate: dict, actual: dict) -> None:
    _check(certificate == actual, "CERTIFICATE_MISMATCH")


def main() -> None:
    try:
        actual = build_audit()
        verify_certificate(json.loads(DEFAULT_CERTIFICATE.read_text(encoding="utf-8")), actual)
    except Exception as error:
        print(f"Periodic operator equivalence verification failed: {error}", file=sys.stderr)
        print("TARGET_A_PERIODIC_OPERATOR_EQUIVALENCES_FAIL")
        raise SystemExit(1)
    print("TARGET_A_PERIODIC_OPERATOR_EQUIVALENCES_PASS")


if __name__ == "__main__":
    main()

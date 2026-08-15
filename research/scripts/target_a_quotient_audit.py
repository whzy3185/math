"""Adversarial completeness audit for the Target A quotient generator."""

from __future__ import annotations

import argparse
import json
import math
import random
import time
from pathlib import Path
from typing import Any

import numpy as np

from target_a_flux_search import (
    canonical_q_code,
    dihedral_orbit,
    enumerate_q_orbits,
    q_code_from_signing,
    search_flux_orbits,
    signing_from_q,
)
from target_a_reproduce import numpy_matrix, reproduce_n, signing_from_class_code
from target_a_verifier import Signing


def negate_signing(signing: Signing) -> Signing:
    return Signing(
        signing.n,
        tuple(-value for value in signing.step1),
        tuple(-value for value in signing.step2),
    )


def edge_index(u: int, v: int, step: int, n: int) -> int:
    if (u + step) % n == v:
        return u
    if (v + step) % n == u:
        return v
    raise ValueError(f"edge {{{u},{v}}} is not a step-{step} edge")


def transform_signing(signing: Signing, orientation: int, shift: int) -> Signing:
    """Apply vertex automorphism i -> orientation*i+shift modulo n."""
    n = signing.n
    permutation = lambda vertex: (orientation * vertex + shift) % n
    step1 = [0] * n
    step2 = [0] * n
    for i, sign in enumerate(signing.step1):
        index = edge_index(permutation(i), permutation((i + 1) % n), 1, n)
        step1[index] = sign
    for i, sign in enumerate(signing.step2):
        index = edge_index(permutation(i), permutation((i + 2) % n), 2, n)
        step2[index] = sign
    if any(value == 0 for value in step1 + step2):
        raise AssertionError("dihedral automorphism did not map each edge family bijectively")
    return Signing(n, tuple(step1), tuple(step2))


def switching_vector(source: Signing, target: Signing) -> tuple[int, ...] | None:
    """Return d with target=D*source*D, or None if none exists."""
    if source.n != target.n:
        return None
    n = source.n
    diagonal = [1] * n
    for i in range(n - 1):
        diagonal[i + 1] = target.step1[i] * source.step1[i] * diagonal[i]
    for i in range(n):
        if diagonal[i] * source.step1[i] * diagonal[(i + 1) % n] != target.step1[i]:
            return None
        if diagonal[i] * source.step2[i] * diagonal[(i + 2) % n] != target.step2[i]:
            return None
    return tuple(diagonal)


def dihedral_switching_relation(reference: Signing, target: Signing) -> dict[str, Any] | None:
    n = reference.n
    for orientation in (1, -1):
        for shift in range(n):
            transformed = transform_signing(reference, orientation, shift)
            diagonal = switching_vector(transformed, target)
            if diagonal is not None:
                return {
                    "orientation": orientation,
                    "shift": shift,
                    "global_negation": False,
                    "switching_vector": diagonal,
                }
            diagonal = switching_vector(negate_signing(transformed), target)
            if diagonal is not None:
                return {
                    "orientation": orientation,
                    "shift": shift,
                    "global_negation": True,
                    "switching_vector": diagonal,
                }
    return None


def burnside_even_bracelets(n: int) -> int:
    rotation_fixed = 0
    for shift in range(n):
        cycles = math.gcd(n, shift)
        cycle_length = n // cycles
        rotation_fixed += 1 << (cycles if cycle_length % 2 == 0 else cycles - 1)
    reflection_fixed = n * (1 << (n // 2))
    numerator = rotation_fixed + reflection_fixed
    if numerator % (2 * n):
        raise AssertionError("Burnside numerator is not divisible by group order")
    return numerator // (2 * n)


def audit_n20() -> dict[str, Any]:
    started = time.time()
    raw = reproduce_n(20, True)
    quotient = search_flux_orbits(20)
    optimizer_row = next(
        row for row in quotient["atlas"] if row["defect_count"] == 0 and row["alpha"] == -1
    )
    quotient_optimizer_classes = sum(
        2 * detail["dihedral_orbit_size"] for detail in optimizer_row["minimizer_details"]
    )
    raw_smallest_states = sorted(
        {
            (
                canonical_q_code(q_code_from_signing(signing_from_class_code(20, code))[0], 20),
                q_code_from_signing(signing_from_class_code(20, code))[1],
            )
            for code in raw["smallest_nonoptimizer_codes"]
        }
    )
    quotient_smallest_state = (
        quotient["smallest_nonoptimizer"]["minimizer_details"][0]["canonical_q_code"],
        quotient["smallest_nonoptimizer"]["alpha"],
    )
    checks = {
        "raw_status_pass": raw["status"] == "PASS",
        "quotient_status_pass": quotient["status"] == "PASS",
        "same_global_minimum": abs(optimizer_row["gap_from_optimizer"]) <= 1e-10,
        "same_optimizer_class_count": len(raw["optimizer_class_codes"])
        == quotient_optimizer_classes,
        "same_smallest_nonoptimizer_rho": math.isclose(
            raw["smallest_nonoptimizer_numeric_rho"],
            quotient["smallest_nonoptimizer"]["min_numeric_rho"],
            rel_tol=0.0,
            abs_tol=1e-10,
        ),
        "same_smallest_nonoptimizer_state": raw_smallest_states == [quotient_smallest_state],
        "same_counterexample_count": len(raw["counterexamples"])
        == len(quotient["counterexamples"]),
        "quotient_orbit_sum_recovers_raw_space": quotient["represented_switching_classes"]
        == raw["switching_classes"],
        "burnside_q_orbit_count_matches": quotient["q_orbits"] == burnside_even_bracelets(20),
    }
    return {
        "n": 20,
        "checks": checks,
        "status": "PASS" if all(checks.values()) else "FAIL",
        "raw": {
            "switching_classes": raw["switching_classes"],
            "optimizer_classes": len(raw["optimizer_class_codes"]),
            "smallest_nonoptimizer_numeric_rho": raw["smallest_nonoptimizer_numeric_rho"],
            "smallest_nonoptimizer_codes_recorded": raw["smallest_nonoptimizer_codes"],
            "smallest_nonoptimizer_quotient_states": raw_smallest_states,
            "counterexamples": len(raw["counterexamples"]),
            "rayleigh_certified_nonoptimizers": raw["rayleigh_certified_nonoptimizers"],
            "exact_fallbacks": raw["exact_fallbacks"],
            "elapsed_seconds": raw["elapsed_seconds"],
        },
        "quotient": {
            "q_orbits": quotient["q_orbits"],
            "spectral_states": quotient["spectral_states"],
            "represented_switching_classes": quotient["represented_switching_classes"],
            "represented_optimizer_classes": quotient_optimizer_classes,
            "smallest_nonoptimizer_numeric_rho": quotient["smallest_nonoptimizer"][
                "min_numeric_rho"
            ],
            "smallest_nonoptimizer_state": quotient_smallest_state,
            "counterexamples": len(quotient["counterexamples"]),
            "rayleigh_certified_nonoptimizers": quotient[
                "rayleigh_certified_nonoptimizers"
            ],
            "exact_fallbacks": quotient["exact_fallbacks"],
            "elapsed_seconds": quotient["elapsed_seconds"],
        },
        "elapsed_seconds": time.time() - started,
    }


def spectral_radius(signing: Signing) -> float:
    return float(np.max(np.abs(np.linalg.eigvalsh(numpy_matrix(signing).astype(float)))))


def audit_n22_samples(sample_count: int, seed: int) -> dict[str, Any]:
    representatives = list(enumerate_q_orbits(22))
    states = [
        (code, orbit_size, alpha)
        for code, orbit_size in representatives
        for alpha in (-1, 1)
    ]
    rng = random.Random(seed)
    sampled = rng.sample(states, sample_count)
    sample_reports = []
    total_expanded_switching_classes = 0
    total_members_checked = 0
    maximum_numeric_rho_drift = 0.0
    all_relations_exact = True
    all_numeric_checks = True

    for code, expected_orbit_size, alpha in sampled:
        orbit = dihedral_orbit(code, 22)
        reference = signing_from_q(code, 22, alpha)
        reference_rho = spectral_radius(reference)
        direct_relations = 0
        negated_relations = 0
        sample_maximum_drift = 0.0
        relation_failures = []
        for member in orbit:
            target = signing_from_q(member, 22, alpha)
            relation = dihedral_switching_relation(reference, target)
            if relation is None:
                relation_failures.append(member)
                all_relations_exact = False
                continue
            if relation["global_negation"]:
                negated_relations += 1
            else:
                direct_relations += 1
            target_rho = spectral_radius(target)
            drift = abs(target_rho - reference_rho)
            sample_maximum_drift = max(sample_maximum_drift, drift)
            maximum_numeric_rho_drift = max(maximum_numeric_rho_drift, drift)
            if drift > 1e-11:
                all_numeric_checks = False

            negated = negate_signing(target)
            negated_q, negated_alpha = q_code_from_signing(negated)
            if negated_q != member or negated_alpha != alpha:
                relation_failures.append(member)
                all_relations_exact = False
            if not np.array_equal(numpy_matrix(negated), -numpy_matrix(target)):
                relation_failures.append(member)
                all_relations_exact = False

        orbit_size_matches = len(orbit) == expected_orbit_size
        all_relations_exact = all_relations_exact and orbit_size_matches
        expanded = 2 * len(orbit)
        total_expanded_switching_classes += expanded
        total_members_checked += len(orbit)
        sample_reports.append(
            {
                "canonical_q_code": code,
                "alpha": alpha,
                "dihedral_orbit_size": len(orbit),
                "expanded_switching_classes_with_global_sign": expanded,
                "orbit_size_matches_generator": orbit_size_matches,
                "direct_dihedral_switching_relations": direct_relations,
                "relations_requiring_global_negation": negated_relations,
                "relation_failures": relation_failures,
                "maximum_numeric_rho_drift": sample_maximum_drift,
            }
        )

    checks = {
        "sample_count_met": len(sampled) == sample_count,
        "all_dihedral_members_have_exact_relation": all_relations_exact,
        "all_global_negations_preserve_Q_alpha_and_negate_matrix": all_relations_exact,
        "all_numeric_rho_diagnostics_agree": all_numeric_checks,
        "generator_q_orbits_match_burnside": len(representatives)
        == burnside_even_bracelets(22),
        "generator_spectral_states_match_expected": 2 * len(representatives) == 97468,
    }
    return {
        "n": 22,
        "seed": seed,
        "sample_count": sample_count,
        "dihedral_members_checked": total_members_checked,
        "expanded_switching_classes_checked": total_expanded_switching_classes,
        "maximum_numeric_rho_drift": maximum_numeric_rho_drift,
        "checks": checks,
        "samples": sample_reports,
        "status": "PASS" if all(checks.values()) else "FAIL",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sample-count", type=int, default=32)
    parser.add_argument("--seed", type=int, default=20260815)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    started = time.time()
    n20 = audit_n20()
    n22 = audit_n22_samples(args.sample_count, args.seed)
    payload = {
        "method": "raw/quotient cross-check + exact dihedral/switching/global-sign relations",
        "n20": n20,
        "n22_samples": n22,
        "status": "PASS" if n20["status"] == n22["status"] == "PASS" else "FAIL",
        "elapsed_seconds": time.time() - started,
    }
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    raise SystemExit(0 if payload["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()

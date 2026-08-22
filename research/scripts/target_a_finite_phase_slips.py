"""Task 47 Experiment B: structured finite phase slips outside multiples of eight."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import multiprocessing as mp
import platform
import shutil
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np
import sympy as sp

from target_a_flux_search import canonical_q_code, q_vector, signing_from_q
from target_a_rational_certificate import bareiss_leading_minors
from target_a_reproduce import numpy_matrix
from target_a_task47_common import TARGET_Q, q_bits, repository_head, sha256, write_json
from target_a_verifier import serialize, signed_adjacency


RESEARCH = Path(__file__).resolve().parents[1]
REPO = RESEARCH.parent
DEFAULT_OUTPUT = RESEARCH / "experiments" / "finite_phase_slips"
TARGET_TAU = (1, 1, -1, 1, -1, -1, 1, -1)


def _q_from_tau(tau: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(tau[index] * tau[(index + 1) % len(tau)] for index in range(len(tau)))


def _q_from_gaps(n: int, gaps: list[int]) -> tuple[int, ...]:
    if sum(gaps) != n or len(gaps) % 2:
        raise ValueError("gap sequence must sum to n and contain an even number of defects")
    positions = [0]
    for gap in gaps[:-1]:
        positions.append(positions[-1] + gap)
    return tuple(1 if index in positions else -1 for index in range(n))


def _balanced_gaps(n: int, defect_count: int, clustered: bool) -> list[int]:
    base, extra = divmod(n, defect_count)
    gaps = [base + (index < extra) for index in range(defect_count)]
    if not clustered and extra:
        gaps = [base] * defect_count
        for index in range(extra):
            gaps[(index * defect_count) // extra] += 1
    return gaps


def structured_seeds(n: int) -> list[tuple[str, tuple[int, ...]]]:
    truncated_tau = tuple(TARGET_TAU[index % 8] for index in range(n))
    seeds: list[tuple[str, tuple[int, ...]]] = [("B1_TRUNCATE_LOCAL_REPAIR", _q_from_tau(truncated_tau))]
    defect_count = max(2, 2 * round(n / 8))
    if defect_count % 2:
        defect_count += 1
    defect_count = min(defect_count, n - (n % 2))
    delta = n - 4 * defect_count
    gaps = [4] * defect_count
    gaps[0] += delta
    if min(gaps) > 0:
        seeds.append(("B2_SINGLE_PHASE_SLIP", _q_from_gaps(n, gaps)))
    gaps = [4] * defect_count
    first = delta // 2
    gaps[0] += first
    gaps[defect_count // 2] += delta - first
    if min(gaps) > 0:
        seeds.append(("B3_TWO_PHASE_SLIPS", _q_from_gaps(n, gaps)))
    seeds.append(("B4_DISTRIBUTED_MISMATCH", _q_from_gaps(n, _balanced_gaps(n, defect_count, False))))
    seeds.append(("B5_LOCALIZED_MISMATCH_BLOCK", _q_from_gaps(n, _balanced_gaps(n, defect_count, True))))
    base = list(_q_from_tau(truncated_tau))
    for offsets in ((-2, 0), (-1, 1), (0, 2), (1, 3)):
        mutated = base[:]
        for offset in offsets:
            mutated[offset % n] *= -1
        seeds.append(("B6_LOCAL_DEFECT_MUTATION", tuple(mutated)))
    unique: dict[int, tuple[str, tuple[int, ...]]] = {}
    for family, q in seeds:
        if math.prod(q) != 1:
            raise AssertionError("structured seed violates Q legality")
        code = canonical_q_code(sum((value == 1) << index for index, value in enumerate(q)), n)
        unique.setdefault(code, (family, q_vector(code, n)))
    return list(unique.values())


def _numeric_record(q: tuple[int, ...], alpha: int, family: str, depth: int) -> dict[str, Any]:
    n = len(q)
    code = canonical_q_code(sum((value == 1) << index for index, value in enumerate(q)), n)
    signing = signing_from_q(code, n, alpha)
    matrix = numpy_matrix(signing)
    values = np.linalg.eigvalsh(matrix.astype(float))
    rho2 = float(max(abs(values[0]), abs(values[-1])) ** 2)
    threshold2 = 4 * (math.cos(math.pi / n) ** 2 + math.cos(2 * math.pi / n) ** 2)
    return {
        "n": n,
        "alpha": alpha,
        "family": family,
        "search_hamming_radius": depth,
        "canonical_q_code": code,
        "q_bits": q_bits(q_vector(code, n)),
        "defect_count": code.bit_count(),
        "rho_squared_numerical": rho2,
        "threshold_squared_numerical": threshold2,
        "delta_squared": rho2 - threshold2,
        "evidence_status": "NUMERICAL_EVIDENCE",
    }


def legal_pair_neighbors(code: int, n: int, limit: int) -> list[int]:
    defects = [index for index in range(n) if (code >> index) & 1]
    anchors = sorted(set(defects + [0, 1, n - 2, n - 1]))
    candidates: set[int] = set()
    for left in anchors:
        for distance in range(1, 9):
            right = (left + distance) % n
            candidates.add(canonical_q_code(code ^ (1 << left) ^ (1 << right), n))
            right = (left - distance) % n
            candidates.add(canonical_q_code(code ^ (1 << left) ^ (1 << right), n))
    candidates.discard(code)
    return sorted(candidates)[:limit]


def search_order(n: int, beam_size: int, neighbor_limit: int, maximum_radius: int) -> dict[str, Any]:
    initial = [
        _numeric_record(q, alpha, family, 0)
        for family, q in structured_seeds(n)
        for alpha in (-1, 1)
    ]
    evaluated: dict[tuple[int, int], dict[str, Any]] = {
        (row["canonical_q_code"], row["alpha"]): row for row in initial
    }
    beam = sorted(initial, key=lambda row: (row["rho_squared_numerical"], row["canonical_q_code"], row["alpha"]))[:beam_size]
    for depth in range(2, maximum_radius + 1, 2):
        proposals: list[dict[str, Any]] = []
        for parent in beam:
            for code in legal_pair_neighbors(parent["canonical_q_code"], n, neighbor_limit):
                key = (code, parent["alpha"])
                if key in evaluated:
                    continue
                row = _numeric_record(q_vector(code, n), parent["alpha"], parent["family"], depth)
                evaluated[key] = row
                proposals.append(row)
        if not proposals:
            break
        beam = sorted(beam + proposals, key=lambda row: (row["rho_squared_numerical"], row["canonical_q_code"], row["alpha"]))[:beam_size]
    best = min(evaluated.values(), key=lambda row: (row["rho_squared_numerical"], row["canonical_q_code"], row["alpha"]))
    return {
        "n": n,
        "residue_mod_8": n % 8,
        "structured_seed_count": len(initial),
        "states_evaluated": len(evaluated),
        "best": best,
    }


def _candidate_payload(row: dict[str, Any]) -> dict[str, Any]:
    signing = signing_from_q(row["canonical_q_code"], row["n"], row["alpha"])
    return {"n": signing.n, "step1": list(signing.step1), "step2": list(signing.step2)}


def _rational_above(value: float, denominator: int = 10000) -> Fraction:
    return Fraction(math.ceil((value + 1e-8) * denominator), denominator)


def _elementary_threshold_lower(n: int) -> tuple[Fraction, str]:
    if n == 32:
        return Fraction(1561, 200), "existing exact n=32 threshold lower bound"
    lower = Fraction(8) - Fraction(200, n * n)
    return lower, "cos(x)>1-x^2/2 and pi^2<10 give rho_-(n)^2>8-200/n^2"


def _verify_rational_finite_bound(candidate: dict[str, Any], bound: Fraction) -> dict[str, Any]:
    signing = signing_from_q(
        sum((value == 1) << index for index, value in enumerate(candidate["quadrilaterals"])),
        candidate["n"],
        candidate["alpha"],
    )
    adjacency = signed_adjacency(signing)
    square = adjacency * adjacency
    certificate_matrix = bound.numerator * sp.eye(signing.n) - bound.denominator * square
    rows = [[int(certificate_matrix[i, j]) for j in range(signing.n)] for i in range(signing.n)]
    minors = bareiss_leading_minors(rows)
    positive = len(minors) == signing.n and all(value > 0 for value in minors)
    threshold_lower, threshold_method = _elementary_threshold_lower(signing.n)
    result = positive and threshold_lower > bound
    matrix_bytes = (json.dumps(rows, separators=(",", ":")) + "\n").encode()
    return {
        "result": result,
        "decision": "COUNTEREXAMPLE_VERIFIED" if result else "CERTIFICATE_FAILED",
        "n": signing.n,
        "alpha": candidate["alpha"],
        "rational_bound_on_rho_squared": str(bound),
        "positive_definite_by_exact_bareiss_sylvester": positive,
        "leading_principal_minor_determinants": [str(value) for value in minors],
        "threshold_rational_lower": str(threshold_lower),
        "threshold_lower_method": threshold_method,
        "threshold_lower_exceeds_bound": threshold_lower > bound,
        "certificate_matrix_sha256": hashlib.sha256(matrix_bytes).hexdigest(),
    }


def certify_candidate(row: dict[str, Any], output: Path) -> dict[str, Any]:
    candidate = _candidate_payload(row)
    candidate_path = output / "candidates" / f"n{row['n']}_a{row['alpha']:+d}.json"
    write_json(candidate_path, candidate)
    bound = _rational_above(row["rho_squared_numerical"])
    report = _verify_rational_finite_bound(
        {
            "n": row["n"],
            "alpha": row["alpha"],
            "quadrilaterals": list(q_vector(row["canonical_q_code"], row["n"])),
        },
        bound,
    )
    certificate_path = output / "certificates" / f"n{row['n']}_a{row['alpha']:+d}.json"
    write_json(certificate_path, report)
    threshold_lower = Fraction(report["threshold_rational_lower"])
    return {
        "n": row["n"],
        "residue_mod_8": row["n"] % 8,
        "alpha": row["alpha"],
        "q_bits": row["q_bits"],
        "family": row["family"],
        "delta_squared_numerical": row["delta_squared"],
        "status": "CERTIFIED_FINITE_COUNTEREXAMPLE" if report["result"] else "NUMERICAL_CANDIDATE_ONLY",
        "rational_bound": str(bound),
        "threshold_rational_lower": str(threshold_lower),
        "certified_gap_margin_lower_bound": str(threshold_lower - bound),
        "candidate_path": str(candidate_path.relative_to(REPO)),
        "candidate_sha256": hashlib.sha256(serialize(signing_from_q(row["canonical_q_code"], row["n"], row["alpha"]))).hexdigest(),
        "certificate_path": str(certificate_path.relative_to(REPO)),
        "certificate_sha256": sha256(certificate_path),
    }


def _search_arguments(arguments: tuple[int, int, int, int]) -> dict[str, Any]:
    return search_order(*arguments)


def _certify_arguments(arguments: tuple[dict[str, Any], Path]) -> dict[str, Any]:
    return certify_candidate(*arguments)


def run(min_n: int, max_n: int, beam_size: int, neighbor_limit: int, maximum_radius: int, output: Path, jobs: int = 8) -> dict[str, Any]:
    output.mkdir(parents=True, exist_ok=True)
    for child in (output / "candidates", output / "certificates"):
        if child.exists():
            shutil.rmtree(child)
    orders = list(range(min_n, max_n + 1, 2))
    arguments = [(n, beam_size, neighbor_limit, maximum_radius) for n in orders]
    with mp.get_context("spawn").Pool(min(jobs, len(arguments))) as pool:
        results = pool.map(_search_arguments, arguments)
    results.sort(key=lambda row: row["n"])
    numerical = [row["best"] for row in results if row["best"]["delta_squared"] < -1e-7]
    if numerical:
        with mp.get_context("spawn").Pool(min(jobs, len(numerical))) as pool:
            certificates = pool.map(_certify_arguments, [(row, output) for row in numerical])
    else:
        certificates = []
    certificates.sort(key=lambda row: row["n"])
    certified = [row for row in certificates if row["status"] == "CERTIFIED_FINITE_COUNTEREXAMPLE"]
    payload = {
        "schema_version": 1,
        "status": "TARGET_A_FINITE_PHASE_SLIP_EXPERIMENT_COMPLETE",
        "scope": "EXPERIMENTAL_DISCOVERY_WITH_EXACT_FOLLOWUP; NO_THEOREM_EXTENSION",
        "order_range": [min_n, max_n],
        "orders": orders,
        "residues_tested": [0, 2, 4, 6],
        "families": ["B1_TRUNCATE_LOCAL_REPAIR", "B2_SINGLE_PHASE_SLIP", "B3_TWO_PHASE_SLIPS", "B4_DISTRIBUTED_MISMATCH", "B5_LOCALIZED_MISMATCH_BLOCK", "B6_LOCAL_DEFECT_MUTATION"],
        "search": {"beam_size": beam_size, "neighbor_limit_per_state": neighbor_limit, "maximum_hamming_radius": maximum_radius, "parallel_jobs": jobs, "random_restarts": 0, "deterministic_ordering": True},
        "software": {"python": platform.python_version(), "numpy": np.__version__, "sympy": sp.__version__},
        "repository_head": repository_head(REPO),
        "script_sha256": sha256(Path(__file__)),
        "results": results,
        "numerical_candidate_count": len(numerical),
        "certified_counterexample_count": len(certified),
        "certified_counterexamples": certificates,
    }
    write_json(output / "summary.json", payload)
    write_json(output / "certified_counterexamples.json", certified)
    write_json(output / "uncertified_candidates.json", [row for row in certificates if row not in certified])
    with (output / "best_by_n.csv").open("w", newline="", encoding="utf-8") as stream:
        fields = ["n", "residue_mod_8", "alpha", "family", "search_hamming_radius", "q_bits", "defect_count", "rho_squared_numerical", "threshold_squared_numerical", "delta_squared", "evidence_status"]
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for result in results:
            source = {"residue_mod_8": result["residue_mod_8"], **result["best"]}
            writer.writerow({field: source[field] for field in fields})
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-n", type=int, default=32)
    parser.add_argument("--max-n", type=int, default=128)
    parser.add_argument("--beam-size", type=int, default=6)
    parser.add_argument("--neighbor-limit", type=int, default=192)
    parser.add_argument("--maximum-radius", type=int, default=4)
    parser.add_argument("--jobs", type=int, default=8)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run(args.min_n, args.max_n, args.beam_size, args.neighbor_limit, args.maximum_radius, args.output, args.jobs)
    print(json.dumps({"numerical": payload["numerical_candidate_count"], "certified": payload["certified_counterexample_count"]}, indent=2))


if __name__ == "__main__":
    main()

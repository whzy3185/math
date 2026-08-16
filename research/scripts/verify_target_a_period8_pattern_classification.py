"""Independently verify the Target A period-8 pattern classification."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import sys
from pathlib import Path
from typing import Any, Iterable

import sympy as sp
from sympy.polys.numberfields import to_number_field


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULT = RESEARCH_ROOT / "proofs" / "target_a_period8_pattern_classification.json"
DEFAULT_AUDIT = RESEARCH_ROOT / "audit" / "period8_pattern_classification_audit.json"
DEFAULT_SHARP = RESEARCH_ROOT / "proofs" / "target_a_period8_sharp_constant.json"
DEFAULT_SOURCE = RESEARCH_ROOT / "scripts" / "target_a_period8_pattern_classification.py"
EXPECTED_SHARP_SHA256 = "f742f79d804f3c44da18dcb4b6562d4d7d1eb75e9f631133bc7314c475dbaa63"
N = 8
TARGET_Q = (1, -1, -1, -1, 1, -1, -1, -1)
ALL_NEGATIVE_Q = (-1,) * N


class ClassificationVerificationError(RuntimeError):
    pass


def _check(condition: bool, message: str) -> None:
    if not condition:
        raise ClassificationVerificationError(message)


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _json_hash(payload: Any) -> str:
    return _sha(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode())


def _positive(expression: sp.Expr) -> bool:
    root = to_number_field(sp.simplify(expression)).to_root()
    return root.is_positive is True or sp.simplify(root > 0) is sp.true


def _bits(signs: Iterable[int]) -> str:
    values = tuple(signs)
    _check(all(value in (-1, 1) for value in values), "VERIFY_SIGN_FAIL")
    return "".join("1" if value == 1 else "0" for value in values)


def _rotate(signs: tuple[int, ...], amount: int) -> tuple[int, ...]:
    amount %= len(signs)
    return signs[amount:] + signs[:amount]


def _images(signs: tuple[int, ...]) -> set[tuple[int, ...]]:
    reflected = tuple(reversed(signs))
    return {_rotate(base, amount) for base in (signs, reflected) for amount in range(N)}


def _canonical(signs: tuple[int, ...]) -> tuple[int, ...]:
    return min(_images(signs), key=_bits)


def _legal_q() -> list[tuple[int, ...]]:
    return [q for q in itertools.product((-1, 1), repeat=N) if math.prod(q) == 1]


def _q_from_tau(tau: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(tau[index] * tau[(index + 1) % N] for index in range(N))


def _tau_from_q(q: tuple[int, ...]) -> tuple[int, ...]:
    _check(len(q) == N and math.prod(q) == 1, "VERIFY_Q_LEGALITY_FAIL")
    tau = [1]
    for value in q[:-1]:
        tau.append(tau[-1] * value)
    _check(tau[-1] * q[-1] == tau[0], "VERIFY_TAU_CLOSURE_FAIL")
    result = tuple(tau)
    _check(_q_from_tau(result) == q, "VERIFY_TAU_RECONSTRUCTION_FAIL")
    return result


def _period(signs: tuple[int, ...]) -> int:
    for period in range(1, N + 1):
        if N % period == 0 and all(signs[index] == signs[index % period] for index in range(N)):
            return period
    raise ClassificationVerificationError("VERIFY_PERIOD_FAIL")


def _bloch(tau: tuple[int, ...], z: sp.Expr) -> sp.Matrix:
    matrix = sp.zeros(N)
    for output in range(N):
        for displacement, coefficient in (
            (-1, 1),
            (1, 1),
            (-2, tau[(output - 2) % N]),
            (2, tau[output]),
        ):
            source = output + displacement
            cell, residue = divmod(source, N)
            matrix[output, residue] += coefficient * z**cell
    return matrix


def _comparison(numerator: int, denominator: int) -> str:
    return ">" if numerator > 8 * denominator else ("=" if numerator == 8 * denominator else "<")


def _rayleigh(tau: tuple[int, ...], certificate: dict[str, Any]) -> tuple[int, int, str]:
    z_value = certificate.get("z")
    vector = certificate.get("vector")
    _check(z_value in (-1, 1), "VERIFY_RAYLEIGH_Z_FAIL")
    _check(
        isinstance(vector, list)
        and len(vector) == N
        and all(type(value) is int for value in vector)
        and any(vector),
        "VERIFY_RAYLEIGH_VECTOR_FAIL",
    )
    column = sp.Matrix(vector)
    matrix = _bloch(tau, sp.Integer(z_value))
    numerator = int((column.T * matrix**2 * column)[0])
    denominator = sum(value * value for value in vector)
    comparison = _comparison(numerator, denominator)
    _check(certificate.get("numerator") == numerator, "VERIFY_RAYLEIGH_NUMERATOR_FAIL")
    _check(certificate.get("denominator") == denominator, "VERIFY_RAYLEIGH_DENOMINATOR_FAIL")
    _check(
        certificate.get("difference_from_8_times_denominator") == numerator - 8 * denominator,
        "VERIFY_RAYLEIGH_DIFFERENCE_FAIL",
    )
    _check(certificate.get("comparison_to_8") == comparison, "VERIFY_RAYLEIGH_COMPARISON_FAIL")
    return numerator, denominator, comparison


def _term_rows(expression: sp.Expr, x: sp.Symbol, z: sp.Symbol, shift: int) -> list[dict[str, Any]]:
    polynomial = sp.Poly(sp.expand(expression * z**shift), x, z, domain=sp.QQ)
    return [
        {"x_degree": degree[0], "z_degree": degree[1] - shift, "coefficient": str(coefficient)}
        for degree, coefficient in polynomial.terms()
    ]


def _signatures(tau: tuple[int, ...]) -> dict[str, Any]:
    x, z = sp.symbols("x z", nonzero=True)
    characteristic = sp.expand((x * sp.eye(N) - _bloch(tau, z)).det(method="domain-ge"))
    full = _term_rows(characteristic, x, z, 2)
    reversed_full = _term_rows(characteristic.subs(x, -x), x, z, 2)
    canonical_full = min(full, reversed_full, key=lambda rows: json.dumps(rows, sort_keys=True))
    squared_x = _term_rows(sp.expand(characteristic * characteristic.subs(x, -x)), x, z, 4)
    _check(all(row["x_degree"] % 2 == 0 for row in squared_x), "VERIFY_SQUARED_EVENNESS_FAIL")
    squared = [
        {
            "y_degree": row["x_degree"] // 2,
            "z_degree": row["z_degree"],
            "coefficient": row["coefficient"],
        }
        for row in squared_x
    ]
    endpoints = []
    for endpoint in (1, -1):
        coefficients = [str(value) for value in sp.Poly(characteristic.subs(z, endpoint), x).all_coeffs()]
        reversed_coefficients = [
            str(value)
            for value in sp.Poly(characteristic.subs({z: endpoint, x: -x}), x).all_coeffs()
        ]
        endpoints.append(min(coefficients, reversed_coefficients))
    return {
        "full_charpoly_signature_sha256": _json_hash(canonical_full),
        "squared_charpoly_signature_sha256": _json_hash(squared),
        "endpoint_spectra_signature_sha256": _json_hash(endpoints),
        "full_charpoly_canonical_terms": canonical_full,
        "squared_charpoly_terms": squared,
    }


def _burnside_rows(legal: list[tuple[int, ...]]) -> tuple[list[dict[str, Any]], dict[str, int]]:
    rows = []
    shell_sums = {defects: 0 for defects in range(0, N + 1, 2)}
    for kind in ("rotation", "reflection"):
        for parameter in range(N):
            def transform(q: tuple[int, ...]) -> tuple[int, ...]:
                if kind == "rotation":
                    return tuple(q[(index + parameter) % N] for index in range(N))
                return tuple(q[(parameter - index) % N] for index in range(N))

            fixed = [q for q in legal if transform(q) == q]
            fixed_shells = {
                str(defects): sum(sum(value == 1 for value in q) == defects for q in fixed)
                for defects in shell_sums
            }
            for defects in shell_sums:
                shell_sums[defects] += fixed_shells[str(defects)]
            rows.append(
                {
                    "kind": kind,
                    "parameter": parameter,
                    "fixed_legal_q_count": len(fixed),
                    "fixed_by_shell": fixed_shells,
                }
            )
    return rows, {str(defects): shell_sums[defects] // 16 for defects in shell_sums}


def _verify_all_negative_identity(tau: tuple[int, ...]) -> None:
    z = sp.Symbol("z", nonzero=True)
    shift = sp.zeros(N)
    for output in range(N):
        source = output + 1
        cell, residue = divmod(source, N)
        shift[output, residue] = z**cell
    inverse = shift.inv()
    expected = 4 * sp.eye(N) + shift**2 + inverse**2 + shift**4 + inverse**4
    _check((_bloch(tau, z) ** 2 - expected).applyfunc(sp.expand) == sp.zeros(N), "VERIFY_RUNNER_UPPER_FAIL")


def verify_classification_data(
    result: dict[str, Any],
    audit: dict[str, Any],
    sharp: dict[str, Any],
    sharp_sha256: str,
    source_sha256: str,
) -> None:
    _check(sharp_sha256 == EXPECTED_SHARP_SHA256, "VERIFY_SHARP_FILE_SHA_FAIL")
    _check(sharp.get("status") == "PERIOD8_SHARP_SPECTRAL_CONSTANT_PROVED", "VERIFY_SHARP_STATUS_FAIL")
    _check(result.get("sharp_dependency", {}).get("sha256") == sharp_sha256, "VERIFY_SHARP_DEPENDENCY_FAIL")
    _check(audit.get("sharp_dependency_sha256") == sharp_sha256, "VERIFY_AUDIT_SHARP_DEPENDENCY_FAIL")
    _check(result.get("script_sha256") == source_sha256, "VERIFY_SOURCE_SHA_FAIL")
    _check(audit.get("source_script_sha256") == source_sha256, "VERIFY_AUDIT_SOURCE_SHA_FAIL")
    eta = sp.sympify(sharp["eta_squared"]["exact_radical"])
    rho_star = sp.sympify(sharp["rho_star"]["exact_radical"])
    _check(_positive(8 - eta), "VERIFY_ETA_LT_EIGHT_FAIL")
    _check(sp.simplify(rho_star**2 - eta) == 0, "VERIFY_RHO_STAR_FAIL")

    raw_tau = list(itertools.product((-1, 1), repeat=N))
    fibers: dict[tuple[int, ...], list[tuple[int, ...]]] = {}
    for tau in raw_tau:
        fibers.setdefault(_q_from_tau(tau), []).append(tau)
    legal = _legal_q()
    _check(len(raw_tau) == 256 and len(legal) == 128, "VERIFY_PHASE_COUNTS_FAIL")
    _check(set(fibers) == set(legal), "VERIFY_TAU_IMAGE_FAIL")
    _check(all(len(fiber) == 2 for fiber in fibers.values()), "VERIFY_TAU_FIBER_FAIL")
    representatives = sorted({_canonical(q) for q in legal}, key=_bits)
    expected_shells = {
        str(defects): sum(sum(value == 1 for value in q) == defects for q in representatives)
        for defects in range(0, N + 1, 2)
    }
    _check(len(representatives) == 18, "VERIFY_ORBIT_COUNT_FAIL")
    _check(expected_shells == {"0": 1, "2": 4, "4": 8, "6": 4, "8": 1}, "VERIFY_SHELL_COUNT_FAIL")
    phase = result.get("phase_space", {})
    _check(phase.get("raw_tau_count") == len(raw_tau), "VERIFY_RECORDED_TAU_COUNT_FAIL")
    _check(phase.get("legal_q_count") == len(legal), "VERIFY_RECORDED_Q_COUNT_FAIL")
    _check(phase.get("d8_orbit_count") == len(representatives), "VERIFY_RECORDED_ORBIT_COUNT_FAIL")
    _check(phase.get("shell_counts") == expected_shells, "VERIFY_RECORDED_SHELL_FAIL")

    orbit_rows = result.get("orbits")
    _check(isinstance(orbit_rows, list) and len(orbit_rows) == len(representatives), "VERIFY_ORBIT_TABLE_FAIL")
    _check(len({row.get("canonical_q_bits") for row in orbit_rows}) == 18, "VERIFY_DUPLICATE_ORBIT_FAIL")
    signature_rows = audit.get("spectral_equivalence", {}).get("signature_rows")
    _check(isinstance(signature_rows, list) and len(signature_rows) == 18, "VERIFY_SIGNATURE_TABLE_FAIL")
    signatures_by_orbit = {row.get("orbit_id"): row for row in signature_rows}
    covered: set[tuple[int, ...]] = set()
    target_rows = []
    runner_rows = []
    strict_count = 0
    ge_count = 0
    full_groups: dict[str, list[str]] = {}
    squared_groups: dict[str, list[str]] = {}
    endpoint_groups: dict[str, list[str]] = {}
    for index, (row, expected_q) in enumerate(zip(orbit_rows, representatives), start=1):
        orbit_id = f"P8-{index:02d}"
        members = _images(expected_q)
        _check(not (covered & members), "VERIFY_ORBIT_OVERLAP_FAIL")
        covered |= members
        _check(row.get("orbit_id") == orbit_id, "VERIFY_ORBIT_ID_FAIL")
        _check(row.get("canonical_q_bits") == _bits(expected_q), "VERIFY_CANONICALIZATION_FAIL")
        _check(row.get("canonical_q_signs") == list(expected_q), "VERIFY_Q_SIGNS_FAIL")
        _check(row.get("canonical_q_code") == int(_bits(expected_q), 2), "VERIFY_Q_CODE_FAIL")
        _check(row.get("defect_count") == sum(value == 1 for value in expected_q), "VERIFY_DEFECT_COUNT_FAIL")
        _check(row.get("orbit_size") == len(members), "VERIFY_ORBIT_SIZE_FAIL")
        _check(row.get("stabilizer_size") * len(members) == 16, "VERIFY_STABILIZER_FAIL")
        tau = _tau_from_q(expected_q)
        _check(row.get("tau_lift_tau0_plus") == list(tau), "VERIFY_RECORDED_TAU_FAIL")
        _check(row.get("primitive_q_period") == _period(expected_q), "VERIFY_Q_PERIOD_FAIL")
        _check(row.get("primitive_tau_period") == _period(tau), "VERIFY_TAU_PERIOD_FAIL")
        is_target = TARGET_Q in members
        is_runner = ALL_NEGATIVE_Q in members
        _check(row.get("target_phase") is is_target, "VERIFY_TARGET_MEMBERSHIP_FAIL")
        _check(row.get("all_unbalanced_phase") is is_runner, "VERIFY_RUNNER_MEMBERSHIP_FAIL")
        if is_target:
            target_rows.append(row)
            _check(row.get("exact_lower_certificate") is None, "VERIFY_TARGET_CERTIFICATE_FAIL")
            _check(sp.simplify(sp.sympify(row.get("exact_sharp_constant")) - eta) == 0, "VERIFY_TARGET_ETA_FAIL")
        else:
            certificate = row.get("exact_lower_certificate")
            _check(isinstance(certificate, dict), "VERIFY_MISSING_RAYLEIGH_FAIL")
            _, _, comparison = _rayleigh(tau, certificate)
            ge_count += comparison in ("=", ">")
            strict_count += comparison == ">"
            if is_runner:
                runner_rows.append(row)
                _check(comparison == "=", "VERIFY_RUNNER_ATTAINMENT_FAIL")
                _verify_all_negative_identity(tau)
                _check(row.get("exact_sharp_constant") == "8", "VERIFY_RUNNER_EXACT_FAIL")
            else:
                _check(comparison == ">", "VERIFY_COMPETITOR_STRICT_FAIL")
        z = sp.Symbol("z", nonzero=True)
        matrix = _bloch(tau, z)
        _check(matrix == matrix.T.subs(z, z**-1), "VERIFY_HERMITIAN_IDENTITY_FAIL")
        alternating = sp.diag(*((-1) ** position for position in range(N)))
        _check(
            _bloch(tuple(-value for value in tau), z) == -alternating * matrix * alternating,
            "VERIFY_TAU_NEGATION_FAIL",
        )
        exact_signatures = _signatures(tau)
        recorded = signatures_by_orbit.get(orbit_id)
        _check(recorded is not None, "VERIFY_SIGNATURE_ORBIT_FAIL")
        for key, value in exact_signatures.items():
            _check(recorded.get(key) == value, f"VERIFY_SIGNATURE_FAIL:{orbit_id}:{key}")
        _check(
            row.get("squared_charpoly_signature_sha256")
            == exact_signatures["squared_charpoly_signature_sha256"],
            "VERIFY_ORBIT_SPECTRAL_HASH_FAIL",
        )
        full_groups.setdefault(exact_signatures["full_charpoly_signature_sha256"], []).append(orbit_id)
        squared_groups.setdefault(exact_signatures["squared_charpoly_signature_sha256"], []).append(orbit_id)
        endpoint_groups.setdefault(exact_signatures["endpoint_spectra_signature_sha256"], []).append(orbit_id)
    _check(covered == set(legal), "VERIFY_ORBIT_COVERAGE_FAIL")
    _check(len(target_rows) == 1 and len(runner_rows) == 1, "VERIFY_DISTINGUISHED_ORBITS_FAIL")
    _check(sum(row["orbit_size"] for row in orbit_rows) == 128, "VERIFY_ORBIT_SIZE_SUM_FAIL")
    _check(ge_count == 17 and strict_count == 16, "VERIFY_CERTIFICATE_COUNTS_FAIL")
    _check(
        len(full_groups) == 18 and len(squared_groups) == 18 and len(endpoint_groups) == 18,
        "VERIFY_SPECTRAL_CLASS_COUNT_FAIL",
    )
    _check(
        phase.get("full_charpoly_equivalence_class_count") == len(full_groups),
        "VERIFY_RECORDED_FULL_CHARPOLY_COUNT_FAIL",
    )
    _check(phase.get("spectral_equivalence_class_count") == len(squared_groups), "VERIFY_RECORDED_SPECTRAL_COUNT_FAIL")

    spectral_audit = audit.get("spectral_equivalence", {})
    _check(spectral_audit.get("full_charpoly_class_count") == len(full_groups), "VERIFY_AUDIT_FULL_COUNT_FAIL")
    _check(spectral_audit.get("full_charpoly_groups") == list(full_groups.values()), "VERIFY_AUDIT_FULL_GROUPS_FAIL")
    preview_coincidences = spectral_audit.get("numeric_sharp_preview_coincidences", {})
    _check(preview_coincidences.get("status") == "OBSERVED", "VERIFY_PREVIEW_STATUS_FAIL")
    _check(
        preview_coincidences.get("exact_sharp_constant_coincidence_claimed") is False,
        "VERIFY_PREVIEW_OVERCLAIM_FAIL",
    )

    burnside_rows, burnside_shells = _burnside_rows(legal)
    route_b = audit.get("route_b", {})
    _check(route_b.get("group_elements") == burnside_rows, "VERIFY_BURNSIDE_ROWS_FAIL")
    fixed_sum = sum(row["fixed_legal_q_count"] for row in burnside_rows)
    _check(route_b.get("fixed_point_sum") == fixed_sum, "VERIFY_BURNSIDE_SUM_FAIL")
    _check(route_b.get("orbit_count") == fixed_sum // 16 == 18, "VERIFY_BURNSIDE_COUNT_FAIL")
    _check(route_b.get("shell_orbit_counts") == burnside_shells == expected_shells, "VERIFY_BURNSIDE_SHELL_FAIL")

    d2 = result.get("d2_shell", {})
    d2_rows = d2.get("rows", [])
    _check(len(d2_rows) == 4, "VERIFY_D2_COUNT_FAIL")
    _check({row.get("cyclic_plus_separation") for row in d2_rows} == {1, 2, 3, 4}, "VERIFY_D2_SEPARATIONS_FAIL")
    _check(sum(row.get("target_phase") is True for row in d2_rows) == 1, "VERIFY_D2_TARGET_FAIL")
    _check(next(row for row in d2_rows if row["target_phase"])["cyclic_plus_separation"] == 4, "VERIFY_D2_TARGET_SEPARATION_FAIL")

    runner_certificate = audit.get("all_unbalanced_exact_certificate", {})
    _check(runner_certificate.get("status") == "ALL_UNBALANCED_SHARP_CONSTANT_PROVED", "VERIFY_RUNNER_STATUS_FAIL")
    _check(runner_certificate.get("sharp_squared_constant") == "8", "VERIFY_RUNNER_CONSTANT_FAIL")
    _rayleigh(_tau_from_q(ALL_NEGATIVE_Q), runner_certificate.get("attainment", {}))
    decision = audit.get("decision", {})
    _check(decision.get("competitor_classes_certified_ge_8") == ge_count, "VERIFY_DECISION_GE_FAIL")
    _check(decision.get("non_runner_classes_certified_gt_8") == strict_count, "VERIFY_DECISION_GT_FAIL")
    _check(decision.get("runner_exactly_8") is True, "VERIFY_DECISION_RUNNER_FAIL")
    _check(result.get("status") == "PERIOD8_UNIQUE_OPTIMUM_AND_SECOND_BEST_PROVED", "VERIFY_FINAL_STATUS_FAIL")
    _check(audit.get("status") == "PERIOD8_PATTERN_CLASSIFICATION_INDEPENDENTLY_AUDITED", "VERIFY_AUDIT_STATUS_FAIL")
    ranking = result.get("ranking", {})
    _check(ranking.get("competitor_classes_certified_ge_8") == 17, "VERIFY_RANKING_GE_FAIL")
    _check(ranking.get("competitor_classes_certified_gt_8") == 16, "VERIFY_RANKING_GT_FAIL")
    _check(ranking.get("ties_with_target") == [], "VERIFY_FALSE_TIE_FAIL")
    _check(ranking.get("classes_better_than_target") == [], "VERIFY_BETTER_CLASS_FAIL")
    _check(result.get("target", {}).get("unique_period8_minimizer") is True, "VERIFY_UNIQUENESS_FAIL")
    runner = result.get("runner_up", {})
    _check(runner.get("unique") is True and runner.get("sharp_squared_constant") == "8", "VERIFY_RUNNER_RANK_FAIL")
    _check(sp.simplify(sp.sympify(runner["exact_squared_gap"]) - (8 - eta)) == 0, "VERIFY_SQUARED_GAP_FAIL")
    _check(
        sp.simplify(sp.sympify(runner["exact_radius_gap"]) - (2 * sp.sqrt(2) - rho_star)) == 0
        and _positive(sp.sympify(runner["exact_radius_gap"])),
        "VERIFY_RADIUS_GAP_FAIL",
    )
    expected_scope = {
        "period8_infinite_volume_optimality": "PROVED",
        "finite_size_global_optimality": "NOT_CLAIMED",
        "all_period_global_optimality": "NOT_CLAIMED",
        "all_signings_global_optimality": "NOT_CLAIMED",
    }
    _check(result.get("scope_boundary") == expected_scope, "VERIFY_SCOPE_OVERCLAIM_FAIL")
    _check(audit.get("scope_boundary") == expected_scope, "VERIFY_AUDIT_SCOPE_OVERCLAIM_FAIL")


def verify_files(
    result_path: Path = DEFAULT_RESULT,
    audit_path: Path = DEFAULT_AUDIT,
    sharp_path: Path = DEFAULT_SHARP,
    source_path: Path = DEFAULT_SOURCE,
) -> None:
    result = json.loads(result_path.read_text(encoding="utf-8"))
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    sharp_bytes = sharp_path.read_bytes()
    sharp = json.loads(sharp_bytes)
    verify_classification_data(result, audit, sharp, _sha(sharp_bytes), _sha(source_path.read_bytes()))


def main() -> None:
    try:
        verify_files()
    except Exception as error:
        print(f"Target A period-8 pattern classification verification failed: {error}", file=sys.stderr)
        print("TARGET_A_PERIOD8_PATTERN_CLASSIFICATION_FAIL")
        raise SystemExit(1)
    print("TARGET_A_PERIOD8_PATTERN_CLASSIFICATION_PASS")


if __name__ == "__main__":
    main()

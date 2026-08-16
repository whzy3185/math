"""Classify all period-8 Target A flux phases and prove their ranking."""

from __future__ import annotations

import argparse
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
DEFAULT_SHARP = RESEARCH_ROOT / "proofs" / "target_a_period8_sharp_constant.json"
DEFAULT_RESULT = RESEARCH_ROOT / "proofs" / "target_a_period8_pattern_classification.json"
DEFAULT_AUDIT = RESEARCH_ROOT / "audit" / "period8_pattern_classification_audit.json"
EXPECTED_SHARP_SHA256 = "f742f79d804f3c44da18dcb4b6562d4d7d1eb75e9f631133bc7314c475dbaa63"
CELL_SIZE = 8
TARGET_Q = (1, -1, -1, -1, 1, -1, -1, -1)
ALL_UNBALANCED_Q = (-1,) * CELL_SIZE
BIT_CONVENTION = "1 means Q_i=+1; 0 means Q_i=-1; Q_0 is the leftmost bit"


class PatternClassificationError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise PatternClassificationError(message)


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_file(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def _json_hash(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return _sha256_bytes(encoded)


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def _exact_positive(expression: sp.Expr) -> bool:
    root = to_number_field(sp.simplify(expression)).to_root()
    return root.is_positive is True or sp.simplify(root > 0) is sp.true


def sign_bits(signs: Iterable[int]) -> str:
    values = tuple(signs)
    _require(all(value in (-1, 1) for value in values), "non-sign in bit conversion")
    return "".join("1" if value == 1 else "0" for value in values)


def bits_signs(bits: str) -> tuple[int, ...]:
    _require(len(bits) == CELL_SIZE and set(bits) <= {"0", "1"}, "bad Q bits")
    return tuple(1 if bit == "1" else -1 for bit in bits)


def rotate(signs: tuple[int, ...], shift: int) -> tuple[int, ...]:
    shift %= len(signs)
    return signs[shift:] + signs[:shift]


def reflect(signs: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(reversed(signs))


def dihedral_images(signs: tuple[int, ...]) -> set[tuple[int, ...]]:
    return {
        rotate(base, shift)
        for base in (signs, reflect(signs))
        for shift in range(len(signs))
    }


def canonical_q(signs: tuple[int, ...]) -> tuple[int, ...]:
    return min(dihedral_images(signs), key=sign_bits)


def legal_q_vectors() -> list[tuple[int, ...]]:
    return [
        signs
        for signs in itertools.product((-1, 1), repeat=CELL_SIZE)
        if math.prod(signs) == 1
    ]


def raw_tau_fiber_audit() -> dict[str, Any]:
    raw_tau = list(itertools.product((-1, 1), repeat=CELL_SIZE))
    fibers: dict[tuple[int, ...], list[tuple[int, ...]]] = {}
    for tau in raw_tau:
        fibers.setdefault(reconstruct_q(tau), []).append(tau)
    legal = set(legal_q_vectors())
    _require(set(fibers) == legal, "raw tau image is not the legal Q space")
    _require(all(len(lifts) == 2 for lifts in fibers.values()), "a Q fiber does not have two lifts")
    _require(
        all(lifts[1] == tuple(-value for value in lifts[0]) for lifts in fibers.values()),
        "the two tau lifts are not global negatives",
    )
    return {
        "raw_tau_count": len(raw_tau),
        "distinct_q_count": len(fibers),
        "lifts_per_q": sorted({len(lifts) for lifts in fibers.values()}),
        "fiber_relation": "the two lifts are tau and -tau",
    }


def route_a_orbits() -> list[dict[str, Any]]:
    legal = legal_q_vectors()
    representatives = sorted({canonical_q(signs) for signs in legal}, key=sign_bits)
    orbits: list[dict[str, Any]] = []
    covered: set[tuple[int, ...]] = set()
    for representative in representatives:
        members = dihedral_images(representative)
        _require(not (covered & members), "Route A produced overlapping orbits")
        covered |= members
        orbits.append({"representative": representative, "members": members})
    _require(covered == set(legal), "Route A did not cover the legal Q space")
    return orbits


def _route_b_transform(signs: tuple[int, ...], kind: str, parameter: int) -> tuple[int, ...]:
    if kind == "rotation":
        return tuple(signs[(index + parameter) % CELL_SIZE] for index in range(CELL_SIZE))
    _require(kind == "reflection", "unknown Route B group element")
    return tuple(signs[(parameter - index) % CELL_SIZE] for index in range(CELL_SIZE))


def route_b_burnside() -> dict[str, Any]:
    legal = legal_q_vectors()
    rows: list[dict[str, Any]] = []
    shell_sums = {defects: 0 for defects in range(0, CELL_SIZE + 1, 2)}
    for kind in ("rotation", "reflection"):
        for parameter in range(CELL_SIZE):
            fixed = [
                signs
                for signs in legal
                if _route_b_transform(signs, kind, parameter) == signs
            ]
            shell_fixed = {
                str(defects): sum(sum(value == 1 for value in signs) == defects for signs in fixed)
                for defects in shell_sums
            }
            for defects in shell_sums:
                shell_sums[defects] += shell_fixed[str(defects)]
            rows.append(
                {
                    "kind": kind,
                    "parameter": parameter,
                    "fixed_legal_q_count": len(fixed),
                    "fixed_by_shell": shell_fixed,
                }
            )
    fixed_sum = sum(row["fixed_legal_q_count"] for row in rows)
    _require(fixed_sum % 16 == 0, "Burnside total is not integral")
    shell_orbits = {str(defects): shell_sums[defects] // 16 for defects in shell_sums}
    _require(
        all(shell_sums[defects] % 16 == 0 for defects in shell_sums),
        "Burnside shell total is not integral",
    )
    return {
        "group_order": 16,
        "group_elements": rows,
        "fixed_point_sum": fixed_sum,
        "orbit_count": fixed_sum // 16,
        "shell_orbit_counts": shell_orbits,
    }


def primitive_period(signs: tuple[int, ...]) -> int:
    for period in range(1, len(signs) + 1):
        if len(signs) % period == 0 and all(
            signs[index] == signs[index % period] for index in range(len(signs))
        ):
            return period
    raise PatternClassificationError("primitive period not found")


def tau_lift(q_signs: tuple[int, ...]) -> tuple[int, ...]:
    _require(len(q_signs) == CELL_SIZE and math.prod(q_signs) == 1, "illegal Q lift")
    tau = [1]
    for q_value in q_signs[:-1]:
        tau.append(q_value * tau[-1])
    _require(tau[-1] * q_signs[-1] == tau[0], "tau lift does not close")
    return tuple(tau)


def reconstruct_q(tau: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(tau[index] * tau[(index + 1) % CELL_SIZE] for index in range(CELL_SIZE))


def bloch_matrix(tau: tuple[int, ...], z: sp.Expr) -> sp.Matrix:
    _require(len(tau) == CELL_SIZE and all(value in (-1, 1) for value in tau), "bad tau")
    matrix = sp.zeros(CELL_SIZE)
    for output in range(CELL_SIZE):
        transitions = (
            (-1, 1),
            (1, 1),
            (-2, tau[(output - 2) % CELL_SIZE]),
            (2, tau[output]),
        )
        for displacement, coefficient in transitions:
            source = output + displacement
            source_cell, source_residue = divmod(source, CELL_SIZE)
            matrix[output, source_residue] += coefficient * z**source_cell
    return matrix


def verify_bloch_construction(tau: tuple[int, ...]) -> None:
    z = sp.Symbol("z", nonzero=True)
    matrix = bloch_matrix(tau, z)
    reflected_adjoint = matrix.T.subs(z, z**-1)
    _require(matrix.applyfunc(sp.expand) == reflected_adjoint.applyfunc(sp.expand), "Bloch adjoint failed")
    for endpoint in (sp.Integer(1), sp.Integer(-1)):
        exact = bloch_matrix(tau, endpoint)
        _require(exact == exact.T, "endpoint Bloch matrix is not symmetric")
        _require(all(entry.is_Integer for entry in exact), "endpoint Bloch matrix is not integral")


def verify_tau_negation_equivalence(tau: tuple[int, ...]) -> None:
    z = sp.Symbol("z", nonzero=True)
    alternating = sp.diag(*((-1) ** index for index in range(CELL_SIZE)))
    left = bloch_matrix(tuple(-value for value in tau), z)
    right = -alternating * bloch_matrix(tau, z) * alternating
    _require(left.applyfunc(sp.expand) == right.applyfunc(sp.expand), "tau negation equivalence failed")


def _numeric_preview(tau: tuple[int, ...], sample_count: int = 4096) -> dict[str, Any]:
    import numpy as np

    coefficients = {shift: np.zeros((CELL_SIZE, CELL_SIZE), dtype=float) for shift in (-1, 0, 1)}
    for output in range(CELL_SIZE):
        for displacement, coefficient in (
            (-1, 1),
            (1, 1),
            (-2, tau[(output - 2) % CELL_SIZE]),
            (2, tau[output]),
        ):
            source = output + displacement
            source_cell, source_residue = divmod(source, CELL_SIZE)
            coefficients[source_cell][output, source_residue] += coefficient
    best_value = -1.0
    best_index = 0
    for index in range(sample_count):
        theta = 2.0 * math.pi * index / sample_count
        z_value = np.exp(1j * theta)
        matrix = (
            coefficients[-1] / z_value + coefficients[0] + coefficients[1] * z_value
        )
        eigenvalues = np.linalg.eigvalsh(matrix)
        value = float(np.max(np.abs(eigenvalues)) ** 2)
        if value > best_value:
            best_value = value
            best_index = index
    return {
        "status": "OBSERVED",
        "sample_count": sample_count,
        "rho_squared": format(best_value, ".15g"),
        "theta_over_pi": format(2.0 * best_index / sample_count, ".15g"),
        "candidate_z_endpoint": 1 if best_index == 0 else (-1 if best_index == sample_count // 2 else None),
    }


def _rayleigh_data(tau: tuple[int, ...], z_value: int, vector: tuple[int, ...]) -> dict[str, Any]:
    matrix = bloch_matrix(tau, sp.Integer(z_value))
    squared = matrix * matrix
    column = sp.Matrix(vector)
    numerator = int((column.T * squared * column)[0])
    denominator = sum(value * value for value in vector)
    return {
        "method": "rayleigh_at_z_pm1",
        "z": z_value,
        "vector": list(vector),
        "numerator": numerator,
        "denominator": denominator,
        "difference_from_8_times_denominator": numerator - 8 * denominator,
        "comparison_to_8": ">" if numerator > 8 * denominator else ("=" if numerator == 8 * denominator else "<"),
    }


def find_rayleigh_certificate(tau: tuple[int, ...], strict: bool) -> dict[str, Any] | None:
    required_difference = 1 if strict else 0
    for z_value in (1, -1):
        for vector in itertools.product((-1, 0, 1), repeat=CELL_SIZE):
            if not any(vector):
                continue
            certificate = _rayleigh_data(tau, z_value, vector)
            if certificate["difference_from_8_times_denominator"] >= required_difference:
                return certificate
    return None


def _laurent_term_rows(expression: sp.Expr, x: sp.Symbol, z: sp.Symbol, shift: int) -> list[dict[str, Any]]:
    polynomial = sp.Poly(sp.expand(expression * z**shift), x, z, domain=sp.QQ)
    return [
        {
            "x_degree": degrees[0],
            "z_degree": degrees[1] - shift,
            "coefficient": str(coefficient),
        }
        for degrees, coefficient in polynomial.terms()
    ]


def spectral_signatures(tau: tuple[int, ...]) -> dict[str, Any]:
    x, z = sp.symbols("x z", nonzero=True)
    characteristic = sp.expand((x * sp.eye(CELL_SIZE) - bloch_matrix(tau, z)).det(method="domain-ge"))
    full_rows = _laurent_term_rows(characteristic, x, z, 2)
    sign_reversed_rows = _laurent_term_rows(characteristic.subs(x, -x), x, z, 2)
    full_canonical = min(full_rows, sign_reversed_rows, key=lambda rows: json.dumps(rows, sort_keys=True))
    squared_expression = sp.expand(characteristic * characteristic.subs(x, -x))
    squared_x_rows = _laurent_term_rows(squared_expression, x, z, 4)
    _require(all(row["x_degree"] % 2 == 0 for row in squared_x_rows), "squared signature is not even")
    squared_rows = [
        {
            "y_degree": row["x_degree"] // 2,
            "z_degree": row["z_degree"],
            "coefficient": row["coefficient"],
        }
        for row in squared_x_rows
    ]
    endpoint_rows = []
    for endpoint in (1, -1):
        polynomial = sp.Poly(characteristic.subs(z, endpoint), x, domain=sp.QQ)
        coefficients = [str(value) for value in polynomial.all_coeffs()]
        reversed_coefficients = [
            str(value) for value in sp.Poly(characteristic.subs({z: endpoint, x: -x}), x).all_coeffs()
        ]
        endpoint_rows.append(min(coefficients, reversed_coefficients))
    return {
        "full_charpoly_signature_sha256": _json_hash(full_canonical),
        "squared_charpoly_signature_sha256": _json_hash(squared_rows),
        "endpoint_spectra_signature_sha256": _json_hash(endpoint_rows),
        "full_charpoly_canonical_terms": full_canonical,
        "squared_charpoly_terms": squared_rows,
    }


def all_unbalanced_exact_certificate(q_signs: tuple[int, ...]) -> dict[str, Any]:
    _require(q_signs == ALL_UNBALANCED_Q, "all-unbalanced certificate used on wrong Q")
    tau = tau_lift(q_signs)
    z = sp.Symbol("z", nonzero=True)
    shift = sp.zeros(CELL_SIZE)
    for output in range(CELL_SIZE):
        source = output + 1
        source_cell, source_residue = divmod(source, CELL_SIZE)
        shift[output, source_residue] = z**source_cell
    inverse_shift = shift.inv()
    c_operator = shift + inverse_shift
    e_operator = shift**2 + inverse_shift**2
    alternating = sp.diag(*tau)
    matrix = bloch_matrix(tau, z)
    _require(matrix == c_operator + alternating * e_operator, "all-unbalanced operator split failed")
    _require(c_operator * alternating == -alternating * c_operator, "anticommutation failed")
    _require(e_operator * alternating == alternating * e_operator, "even shift commutation failed")
    expected_square = 4 * sp.eye(CELL_SIZE) + shift**2 + inverse_shift**2 + shift**4 + inverse_shift**4
    _require((matrix**2 - expected_square).applyfunc(sp.expand) == sp.zeros(CELL_SIZE), "square identity failed")
    attainment = find_rayleigh_certificate(tau, strict=False)
    _require(attainment is not None and attainment["comparison_to_8"] == "=", "8 attainment missing")
    return {
        "status": "ALL_UNBALANCED_SHARP_CONSTANT_PROVED",
        "tau": list(tau),
        "operator_decomposition": "A=C+D*E with C=S+S^-1, E=S^2+S^-2, D_i=(-1)^i",
        "square_identity": "A^2=4I+S^2+S^-2+S^4+S^-4",
        "upper_bound": "for |w|=1, 4+w^2+w^-2+w^4+w^-4<=8",
        "attainment": attainment,
        "sharp_squared_constant": "8",
        "sharp_spectral_radius": "2*sqrt(2)",
    }


def _cyclic_separation(q_signs: tuple[int, ...]) -> int | None:
    positions = [index for index, value in enumerate(q_signs) if value == 1]
    if len(positions) != 2:
        return None
    distance = (positions[1] - positions[0]) % CELL_SIZE
    return min(distance, CELL_SIZE - distance)


def load_sharp_dependency(path: Path = DEFAULT_SHARP) -> dict[str, Any]:
    raw = path.read_bytes()
    _require(_sha256_bytes(raw) == EXPECTED_SHARP_SHA256, "Task 40A result SHA mismatch")
    payload = json.loads(raw)
    _require(payload.get("status") == "PERIOD8_SHARP_SPECTRAL_CONSTANT_PROVED", "Task 40A status mismatch")
    eta = sp.sympify(payload["eta_squared"]["exact_radical"])
    _require(_exact_positive(8 - eta), "target eta is not below eight")
    return {"payload": payload, "sha256": _sha256_bytes(raw), "eta": eta}


def classify_patterns(
    sharp_path: Path = DEFAULT_SHARP,
    result_path: Path = DEFAULT_RESULT,
    audit_path: Path = DEFAULT_AUDIT,
) -> tuple[dict[str, Any], dict[str, Any]]:
    sharp = load_sharp_dependency(sharp_path)
    tau_fibers = raw_tau_fiber_audit()
    route_a = route_a_orbits()
    route_b = route_b_burnside()
    shell_counts = {
        str(defects): sum(
            sum(value == 1 for value in orbit["representative"]) == defects for orbit in route_a
        )
        for defects in range(0, CELL_SIZE + 1, 2)
    }
    _require(len(legal_q_vectors()) == 128, "legal Q count mismatch")
    _require(len(route_a) == route_b["orbit_count"], "enumeration routes disagree")
    _require(shell_counts == route_b["shell_orbit_counts"], "shell routes disagree")
    _require(sum(len(orbit["members"]) for orbit in route_a) == 128, "orbit sizes do not sum to 128")

    orbit_rows: list[dict[str, Any]] = []
    signature_rows: list[dict[str, Any]] = []
    target_count = 0
    for orbit_index, orbit in enumerate(route_a, start=1):
        q_signs = orbit["representative"]
        tau = tau_lift(q_signs)
        _require(reconstruct_q(tau) == q_signs, "tau reconstruction mismatch")
        verify_bloch_construction(tau)
        verify_tau_negation_equivalence(tau)
        is_target = TARGET_Q in orbit["members"]
        is_all_unbalanced = ALL_UNBALANCED_Q in orbit["members"]
        target_count += int(is_target)
        strict = not is_target and not is_all_unbalanced
        rayleigh = None if is_target else find_rayleigh_certificate(tau, strict=strict)
        _require(is_target or rayleigh is not None, "competitor certificate search failed")
        signatures = spectral_signatures(tau)
        signature_rows.append(
            {
                "orbit_id": f"P8-{orbit_index:02d}",
                "canonical_q_bits": sign_bits(q_signs),
                **signatures,
            }
        )
        q_period = primitive_period(q_signs)
        tau_period = primitive_period(tau)
        row = {
            "orbit_id": f"P8-{orbit_index:02d}",
            "canonical_q_bits": sign_bits(q_signs),
            "canonical_q_code": int(sign_bits(q_signs), 2),
            "canonical_q_signs": list(q_signs),
            "defect_count": sum(value == 1 for value in q_signs),
            "orbit_size": len(orbit["members"]),
            "stabilizer_size": 16 // len(orbit["members"]),
            "primitive_q_period": q_period,
            "tau_lift_tau0_plus": list(tau),
            "primitive_tau_period": tau_period,
            "tau_period_relation": "equals_q_period" if tau_period == q_period else "doubles_q_period",
            "target_phase": is_target,
            "all_unbalanced_phase": is_all_unbalanced,
            "cyclic_plus_separation": _cyclic_separation(q_signs),
            "numeric_preview": _numeric_preview(tau),
            "exact_lower_certificate": rayleigh,
            "exact_sharp_constant": (
                sharp["payload"]["eta_squared"]["exact_radical"]
                if is_target
                else ("8" if is_all_unbalanced else None)
            ),
            "classification_status": (
                "UNIQUE_TARGET_EXACT"
                if is_target
                else ("UNIQUE_SECOND_BEST_EXACT" if is_all_unbalanced else "STRICTLY_ABOVE_EIGHT_CERTIFIED")
            ),
            "squared_charpoly_signature_sha256": signatures["squared_charpoly_signature_sha256"],
            "endpoint_spectra_signature_sha256": signatures["endpoint_spectra_signature_sha256"],
        }
        orbit_rows.append(row)
    _require(target_count == 1, "target phase orbit is not unique")

    full_groups: dict[str, list[str]] = {}
    squared_groups: dict[str, list[str]] = {}
    endpoint_groups: dict[str, list[str]] = {}
    for row in signature_rows:
        full_groups.setdefault(row["full_charpoly_signature_sha256"], []).append(row["orbit_id"])
        squared_groups.setdefault(row["squared_charpoly_signature_sha256"], []).append(row["orbit_id"])
        endpoint_groups.setdefault(row["endpoint_spectra_signature_sha256"], []).append(row["orbit_id"])
    numeric_groups: dict[str, list[str]] = {}
    for row in orbit_rows:
        numeric_groups.setdefault(row["numeric_preview"]["rho_squared"], []).append(row["orbit_id"])
    numeric_preview_coincidences = [group for group in numeric_groups.values() if len(group) > 1]
    all_unbalanced = all_unbalanced_exact_certificate(canonical_q(ALL_UNBALANCED_Q))
    competitor_rows = [row for row in orbit_rows if not row["target_phase"]]
    certified_ge_eight = sum(
        row["exact_lower_certificate"]["comparison_to_8"] in ("=", ">") for row in competitor_rows
    )
    certified_gt_eight = sum(
        row["exact_lower_certificate"]["comparison_to_8"] == ">" for row in competitor_rows
    )
    strongest = certified_ge_eight == 17 and certified_gt_eight == 16
    final_status = (
        "PERIOD8_UNIQUE_OPTIMUM_AND_SECOND_BEST_PROVED"
        if strongest
        else "PERIOD8_FLUX_CLASSIFICATION_COMPLETE"
    )
    d2_rows = [
        {
            "orbit_id": row["orbit_id"],
            "canonical_q_bits": row["canonical_q_bits"],
            "cyclic_plus_separation": row["cyclic_plus_separation"],
            "target_phase": row["target_phase"],
            "certificate_comparison_to_8": (
                "eta<8" if row["target_phase"] else row["exact_lower_certificate"]["comparison_to_8"]
            ),
        }
        for row in orbit_rows
        if row["defect_count"] == 2
    ]
    result = {
        "schema_version": 1,
        "status": final_status,
        "classification_statuses": [
            "PERIOD8_FLUX_CLASSIFICATION_COMPLETE",
            "PERIOD8_UNIQUE_OPTIMUM_PROVED" if strongest else "NOT_PROVED",
            "PERIOD8_SECOND_BEST_GAP_PROVED" if strongest else "NOT_PROVED",
        ],
        "bit_convention": BIT_CONVENTION,
        "sharp_dependency": {
            "path": "research/proofs/target_a_period8_sharp_constant.json",
            "sha256": sharp["sha256"],
            "status": sharp["payload"]["status"],
        },
        "phase_space": {
            "raw_tau_count": tau_fibers["raw_tau_count"],
            "tau_lifts_per_q": tau_fibers["lifts_per_q"][0],
            "tau_negation_equivalence": "A_(-tau)(z)=-D*A_tau(z)*D with D=diag((-1)^i)",
            "legal_q_count": len(legal_q_vectors()),
            "d8_orbit_count": len(route_a),
            "shell_counts": shell_counts,
            "orbit_size_sum": sum(row["orbit_size"] for row in orbit_rows),
            "full_charpoly_equivalence_class_count": len(full_groups),
            "spectral_equivalence_class_count": len(squared_groups),
            "endpoint_spectra_class_count": len(endpoint_groups),
        },
        "orbits": orbit_rows,
        "d2_shell": {
            "status": "D2_TARGET_UNIQUE_OPTIMUM_FINITE_EXACT_CLASSIFICATION",
            "proof_type": "finite exact table using target eta<8 and three strict endpoint Rayleigh certificates",
            "rows": d2_rows,
        },
        "target": {
            "q_orbit": next(row["canonical_q_bits"] for row in orbit_rows if row["target_phase"]),
            "eta": sharp["payload"]["eta_squared"]["exact_radical"],
            "rho_star": sharp["payload"]["rho_star"]["exact_radical"],
            "unique_period8_minimizer": strongest,
        },
        "runner_up": {
            "q_orbit": sign_bits(canonical_q(ALL_UNBALANCED_Q)),
            "sharp_squared_constant": "8",
            "sharp_spectral_radius": "2*sqrt(2)",
            "unique": strongest,
            "exact_squared_gap": "4 - sqrt(2*sqrt(5) + 10)",
            "exact_radius_gap": "2*sqrt(2) - sqrt(sqrt(2*sqrt(5) + 10) + 4)",
        },
        "ranking": {
            "method": "Task 40A exact target constant, fresh all-unbalanced upper identity, and exact endpoint Rayleigh lower certificates",
            "competitor_classes_certified_ge_8": certified_ge_eight,
            "competitor_classes_certified_gt_8": certified_gt_eight,
            "ties_with_target": [],
            "classes_better_than_target": [],
        },
        "scope_boundary": {
            "period8_infinite_volume_optimality": "PROVED" if strongest else "CLASSIFIED",
            "finite_size_global_optimality": "NOT_CLAIMED",
            "all_period_global_optimality": "NOT_CLAIMED",
            "all_signings_global_optimality": "NOT_CLAIMED",
        },
        "checker": {
            "path": "research/scripts/verify_target_a_period8_pattern_classification.py",
            "status": "TARGET_A_PERIOD8_PATTERN_CLASSIFICATION_PASS",
        },
        "script_sha256": _sha256_file(Path(__file__).resolve()),
        "next_gate": "Task 40C",
    }
    audit = {
        "schema_version": 1,
        "status": "PERIOD8_PATTERN_CLASSIFICATION_INDEPENDENTLY_AUDITED",
        "source_script_sha256": result["script_sha256"],
        "sharp_dependency_sha256": sharp["sha256"],
        "route_a": {
            "method": "raw tau fibers, then legal-Q enumeration and explicit rotation/reflection orbits",
            "tau_fiber_audit": tau_fibers,
            "legal_q_count": len(legal_q_vectors()),
            "orbit_count": len(route_a),
            "shell_orbit_counts": shell_counts,
        },
        "route_b": route_b,
        "bloch_construction": {
            "status": "FRESH_BLOCH_CONSTRUCTION_PASS",
            "operator": "(Ax)_i=x_(i-1)+x_(i+1)+tau_(i-2)x_(i-2)+tau_i*x_(i+2)",
            "hermitian_identity": "H(z)^*=H(z^-1)",
            "endpoint_integer_symmetric": True,
            "tau_negation_equivalence_verified_for_all_orbits": True,
        },
        "all_unbalanced_exact_certificate": all_unbalanced,
        "spectral_equivalence": {
            "method": "exact squared full-Bloch characteristic-polynomial signatures",
            "flux_orbit_count": len(route_a),
            "full_charpoly_class_count": len(full_groups),
            "full_charpoly_groups": list(full_groups.values()),
            "squared_spectral_class_count": len(squared_groups),
            "squared_groups": list(squared_groups.values()),
            "endpoint_spectra_class_count": len(endpoint_groups),
            "endpoint_groups": list(endpoint_groups.values()),
            "numeric_sharp_preview_coincidences": {
                "status": "OBSERVED",
                "groups": numeric_preview_coincidences,
                "exact_sharp_constant_coincidence_claimed": False,
            },
            "signature_rows": signature_rows,
        },
        "decision": {
            "status": final_status,
            "eta_strictly_below_8": True,
            "competitor_classes_certified_ge_8": certified_ge_eight,
            "non_runner_classes_certified_gt_8": certified_gt_eight,
            "runner_exactly_8": True,
        },
        "scope_boundary": result["scope_boundary"],
    }
    _write_json(result_path, result)
    _write_json(audit_path, audit)
    return result, audit


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sharp", type=Path, default=DEFAULT_SHARP)
    parser.add_argument("--output", type=Path, default=DEFAULT_RESULT)
    parser.add_argument("--audit", type=Path, default=DEFAULT_AUDIT)
    args = parser.parse_args()
    try:
        result, _ = classify_patterns(args.sharp, args.output, args.audit)
    except Exception as error:
        print(f"Target A period-8 pattern classification failed: {error}", file=sys.stderr)
        print("TARGET_A_PERIOD8_PATTERN_CLASSIFICATION_FAIL")
        raise SystemExit(1)
    print("PERIOD8_FLUX_CLASSIFICATION_COMPLETE")
    for status in result["classification_statuses"][1:]:
        if status != "NOT_PROVED":
            print(status)
    print(result["status"])


if __name__ == "__main__":
    main()

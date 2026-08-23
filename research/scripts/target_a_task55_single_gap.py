"""Exact Task 55 quotient duality and gap-plus-eight recurrence certificate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import sympy as sp

from target_a_task47_common import write_json
from target_a_task51_algebra import symmetric_evans_core
from target_a_task52_exact import exterior_square, product_for_gap


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "proofs" / "task55" / "certificates"
LAM, Y, S, P, T = sp.symbols("lam y S P t")
C6_LEFT = sp.Rational(7905369311620327, 10**15)
C6_RIGHT = sp.Rational(7905369311620328, 10**15)
EXTERIOR_BASIS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))


def reciprocal_relation(variable: sp.Expr) -> sp.Expr:
    a = -2 * variable**4 + 16 * variable**2 - 13
    b = variable**8 - 16 * variable**6 + 80 * variable**4 - 128 * variable**2 + 40
    return sp.expand((P + 1) ** 2 * (P**2 + 1 - b * P) + a**2 * P**2)


def primitive_evans(gap: int) -> sp.Expr:
    core, _degrees = symmetric_evans_core(gap)
    a = -2 * LAM**4 + 16 * LAM**2 - 13
    substituted = sp.cancel(core.subs(S, -a * P / (P + 1)))
    numerator = sp.fraction(substituted)[0]
    return sp.expand(sp.primitive(sp.Poly(numerator, P))[1].as_expr())


def quotient_remainder(expression: sp.Expr, relation: sp.Expr) -> sp.Expr:
    return sp.expand(sp.rem(sp.Poly(expression, P), sp.Poly(relation, P)).as_expr())


def even_to_y(expression: sp.Expr) -> sp.Expr:
    result = 0
    for (power,), coefficient in sp.Poly(sp.expand(expression), LAM).terms():
        if power % 2:
            raise AssertionError("expected an even polynomial in lam")
        result += coefficient * Y ** (power // 2)
    return sp.expand(result)


def polynomial_text(expression: sp.Expr, *variables: sp.Symbol) -> str:
    return str(sp.Poly(sp.expand(expression), *variables).as_expr())


def expression_digest(expression: sp.Expr, *variables: sp.Symbol) -> str:
    return hashlib.sha256(polynomial_text(expression, *variables).encode()).hexdigest()


def matrix_entries(matrix: sp.Matrix) -> list[list[str]]:
    return [
        [str(sp.expand(matrix[row, column])) for column in range(matrix.cols)]
        for row in range(matrix.rows)
    ]


def matrix_digest(matrix: sp.Matrix) -> str:
    payload = json.dumps(matrix_entries(matrix), separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def recurrence_matrix(gap: int) -> sp.Matrix:
    right = product_for_gap(gap, gap, gap + 8, LAM)
    inserted = product_for_gap(gap + 8, gap, gap + 8, LAM)
    next_right = product_for_gap(gap + 8, gap + 8, gap + 16, LAM)
    return (next_right * inserted * right.inv()).applyfunc(sp.expand)


def matrix_class_record(label: str, gap: int, q4: sp.Expr, m5: sp.Expr) -> dict[str, Any]:
    matrix = recurrence_matrix(gap)
    wedge = exterior_square(matrix).applyfunc(sp.expand)
    annihilator = (wedge - sp.eye(6)) * (
        wedge**4
        + q4.coeff(T, 3).subs(Y, LAM**2) * wedge**3
        + q4.coeff(T, 2).subs(Y, LAM**2) * wedge**2
        + q4.coeff(T, 1).subs(Y, LAM**2) * wedge
        + sp.eye(6)
    )
    evaluated = wedge.subs(LAM, 3)
    seed = sp.eye(6)[:, 0]
    krylov = sp.Matrix.hstack(*[evaluated**power * seed for power in range(5)])
    krylov_minor = int(krylov.extract((0, 1, 2, 3, 5), range(5)).det())
    characteristic = even_to_y(matrix.charpoly(T).as_expr())
    exterior_characteristic = even_to_y(wedge.charpoly(T).as_expr())
    return {
        "class": label,
        "representative_gap": gap,
        "residues": [1, 3, 5, 7] if gap % 2 else [2, 4, 6, 8],
        "C_entries": matrix_entries(matrix),
        "C_sha256": matrix_digest(matrix),
        "W_entries": matrix_entries(wedge),
        "W_sha256": matrix_digest(wedge),
        "det_C": str(sp.factor(matrix.det())),
        "characteristic": polynomial_text(characteristic, T, Y),
        "exterior_characteristic": polynomial_text(exterior_characteristic, T, Y),
        "rank_W_minus_I_at_lam_3": int((evaluated - sp.eye(6)).rank()),
        "krylov_rows": [0, 1, 2, 3, 5],
        "krylov_minor_at_lam_3": krylov_minor,
        "annihilator": polynomial_text(m5, T, Y),
        "annihilator_zero": all(sp.expand(value) == 0 for value in annihilator),
    }


def build_certificate() -> dict[str, Any]:
    relation_lam = reciprocal_relation(LAM)
    relation_y = even_to_y(relation_lam)
    raw2 = primitive_evans(2)
    raw6 = primitive_evans(6)
    reduced2 = quotient_remainder(raw2, relation_lam)
    reduced6 = quotient_remainder(raw6, relation_lam)
    reversed_reduced2 = sp.expand(
        P**3 * reduced2.subs({LAM: -LAM, P: 1 / P}, simultaneous=True)
    )
    norm2_lam = sp.resultant(reduced2, relation_lam, P)
    norm6_lam = sp.resultant(reduced6, relation_lam, P)
    norm_y = sp.factor(even_to_y(norm2_lam))

    a_coefficient = -Y**4 + 16 * Y**3 - 88 * Y**2 + 200 * Y - 158
    b_coefficient = 2 * Y**4 - 16 * Y**3 + 36 * Y**2 - 8 * Y - 29
    q4 = T**4 + a_coefficient * T**3 + b_coefficient * T**2 + a_coefficient * T + 1
    u = (Y - 3) * (Y**3 - 13 * Y**2 + 49 * Y - 53)
    v = (Y - 3) * (3 * Y**3 - 23 * Y**2 + 55 * Y - 43)
    m5 = sp.expand((T - 1) * q4)
    recurrence = T**5 - u * T**4 + v * T**3 - v * T**2 + u * T - 1
    discriminant = sp.factor(a_coefficient**2 - 4 * (b_coefficient - 2))
    expected_characteristic = (
        T**4
        + (-2 * Y**2 + 12 * Y - 17) * T**3
        + (Y**4 - 16 * Y**3 + 88 * Y**2 - 200 * Y + 160) * T**2
        + (-2 * Y**2 + 12 * Y - 17) * T
        + 1
    )
    classes = [
        matrix_class_record("odd", 1, q4, m5),
        matrix_class_record("even", 2, q4, m5),
    ]
    residue_matrices = {gap: recurrence_matrix(gap) for gap in range(1, 9)}
    expected_minors = {
        "odd": -361233047485886499,
        "even": 1134653061164985747,
    }

    checks = {
        "free_symbol_contract": (
            raw2.free_symbols | raw6.free_symbols | relation_lam.free_symbols
        ) <= {LAM, P},
        "bulk_relation_degree_four": sp.degree(relation_lam, P) == 4,
        "bulk_relation_palindromic": sp.expand(
            P**4 * relation_y.subs(P, 1 / P) - relation_y
        ) == 0,
        "reduced_cores_have_degree_below_four": all(
            sp.degree(core, P) < 4 for core in (reduced2, reduced6)
        ),
        "unsquared_quotient_involution": sp.expand(reduced6 - reversed_reduced2) == 0,
        "reduced_norms_identical": sp.expand(norm2_lam - norm6_lam) == 0,
        "norm_is_even": sp.expand(norm2_lam - norm_y.subs(Y, LAM**2)) == 0,
        "two_matrix_classes_only": all(
            residue_matrices[gap] == residue_matrices[1 if gap % 2 else 2]
            for gap in range(1, 9)
        ),
        "all_characteristics_identical": all(
            sp.expand(
                even_to_y(residue_matrices[gap].charpoly(T).as_expr())
                - expected_characteristic
            ) == 0
            for gap in range(1, 9)
        ),
        "all_exterior_annihilators_zero": all(row["annihilator_zero"] for row in classes),
        "generic_minimal_degree_five": all(
            row["krylov_minor_at_lam_3"] == expected_minors[row["class"]]
            for row in classes
        ),
        "five_term_recurrence_expands": sp.expand(m5 - recurrence) == 0,
        "quadratic_discriminant_factorization": discriminant
        == (Y - 8) * (Y - 4) * (Y - 2) ** 2 * (Y**2 - 8 * Y + 14) ** 2,
        "c6_interval_lies_in_complex_mode_region": 4 < C6_LEFT < C6_RIGHT < 8,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    if not all(checks.values()):
        raise AssertionError(checks)

    return {
        "schema_version": 1,
        "status": "TASK55_SINGLE_GAP_ALGEBRA_PROVED_HIERARCHY_OPEN",
        "evidence": "COMPUTER_ASSISTED_PROVED",
        "symbol_contract": ["lam", "S", "P", "y", "t"],
        "transfer_convention": {
            "q": "Q_i=+1 on 4Z through 0 and on g+4Z from g onward; Q_i=-1 otherwise",
            "tau": "tau_0=1 and tau_(i+1)=Q_i tau_i",
            "state": "(u_(i+1),u_i,u_(i-1),u_(i-2))",
            "step": "[[-tau_i,tau_i*lam,-tau_i,-tau_i*tau_(i-2)],[1,0,0,0],[0,1,0,0],[0,0,1,0]]",
            "product_order": "left multiplication in increasing site index",
            "evans_cut": {"start": "-8", "stop": "g+8", "cofactor_rows": [0, 1, 2]},
            "gap_plus_eight_factors": ["R_g=[g,g+8)", "N_(g+8)=[g,g+8)", "R_(g+8)=[g+8,g+16)"],
            "exterior_basis": [list(pair) for pair in EXTERIOR_BASIS],
        },
        "unsquared_duality": {
            "quotient_ring": "Q(lam)[P,P^-1]/(R_lam)",
            "bulk_relation": polynomial_text(relation_y, P, Y),
            "reduced_e2": polynomial_text(reduced2, P, LAM),
            "reduced_e6": polynomial_text(reduced6, P, LAM),
            "identity": "e6(lam,P)=P^3 e2(-lam,P^-1)",
            "raw_e2_sha256": expression_digest(raw2, P, LAM),
            "raw_e6_sha256": expression_digest(raw6, P, LAM),
            "reduced_e2_sha256": expression_digest(reduced2, P, LAM),
            "reduced_e6_sha256": expression_digest(reduced6, P, LAM),
            "common_norm": polynomial_text(norm_y, Y),
            "common_norm_factorization": str(sp.factor(norm_y)),
            "common_norm_sha256": expression_digest(norm_y, Y),
        },
        "gap_plus_eight": {
            "residue_to_matrix_class": {
                "1": "odd", "2": "even", "3": "odd", "4": "even",
                "5": "odd", "6": "even", "7": "odd", "8": "even",
            },
            "characteristic": polynomial_text(expected_characteristic, T, Y),
            "exterior_characteristic": polynomial_text((T - 1) ** 2 * q4, T, Y),
            "generic_minimal_polynomial": polynomial_text(m5, T, Y),
            "order_five_recurrence": polynomial_text(recurrence, T, Y),
            "U": polynomial_text(u, Y),
            "V": polynomial_text(v, Y),
            "quadratic_discriminant": polynomial_text(discriminant, Y),
            "quadratic_discriminant_factorization": str(sp.factor(discriminant)),
            "matrix_classes": classes,
        },
        "supersedes": {
            "artifact": "research/proofs/task53/certificates/plus_minus_two_structure.json",
            "reason": "Task 53 mixed symbols named lambda and lam, so its negative unsquared-duality search was not probative.",
        },
        "proof_boundary": (
            "The quotient involution exchanges P with P^-1 and hence exchanges stable and "
            "unstable Floquet branches. The exact order-five recurrence has complex paired "
            "modes for 4<y<8; it does not prove physical-root ordering, eventual monotonicity, "
            "or a uniform all-single-gap lower theorem."
        ),
        "checks": checks,
    }


def run() -> dict[str, Any]:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    payload = build_certificate()
    write_json(OUTPUT / "single_gap_structure.json", payload)
    print(json.dumps({"status": payload["status"], "matrix_classes": 2}, indent=2))
    return payload


if __name__ == "__main__":
    run()

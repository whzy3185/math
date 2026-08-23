"""Independent exact checker for the Task 55 single-gap algebra certificate."""

from __future__ import annotations

import hashlib
import json
from functools import lru_cache
from pathlib import Path
from typing import Any

import sympy as sp


RESEARCH = Path(__file__).resolve().parents[1]
CERTIFICATE = RESEARCH / "proofs" / "task55" / "certificates" / "single_gap_structure.json"
LAM, Y, S, P, T = sp.symbols("lam y S P t")
C6_LEFT = sp.Rational(7905369311620327, 10**15)
C6_RIGHT = sp.Rational(7905369311620328, 10**15)
EXTERIOR_BASIS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))


def strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_strict(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=strict_object)


def q_value(index: int, gap: int) -> int:
    in_left_bulk = index <= 0 and index % 4 == 0
    in_right_bulk = index >= gap and (index - gap) % 4 == 0
    return 1 if in_left_bulk or in_right_bulk else -1


def tau_values(gap: int, low: int, high: int) -> dict[int, int]:
    tau = {0: 1}
    for index in range(high):
        tau[index + 1] = q_value(index, gap) * tau[index]
    for index in range(-1, low - 1, -1):
        tau[index] = q_value(index, gap) * tau[index + 1]
    return tau


def transfer_product(gap: int, start: int, stop: int) -> sp.Matrix:
    tau = tau_values(gap, min(-32, start - 4), max(48, stop + 4))
    product = sp.eye(4)
    for index in range(start, stop):
        a, b = tau[index], tau[index - 2]
        step = sp.Matrix([
            [-a, a * LAM, -a, -a * b],
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
        ])
        product = step * product
    return product.applyfunc(sp.expand)


def cofactor_vector(matrix: sp.Matrix, eigenvalue: sp.Expr) -> sp.Matrix:
    shifted = matrix - eigenvalue * sp.eye(4)
    rows = (0, 1, 2)
    return sp.Matrix([
        (-1) ** excluded
        * shifted.extract(rows, [column for column in range(4) if column != excluded]).det(
            method="domain-ge"
        )
        for excluded in range(4)
    ])


def symmetric_evans(gap: int) -> sp.Expr:
    z1, z2 = sp.symbols("z1 z2")
    start, stop = -8, gap + 8
    left = transfer_product(gap, start - 8, start)
    right = transfer_product(gap, stop, stop + 8)
    defect = transfer_product(gap, start, stop)
    left_vectors = [
        (z**3 * cofactor_vector(left, 1 / z)).applyfunc(sp.cancel)
        for z in (z1, z2)
    ]
    right_vectors = [cofactor_vector(right, z) for z in (z1, z2)]
    determinant = sp.factor(
        sp.Matrix.hstack(
            defect * left_vectors[0],
            defect * left_vectors[1],
            right_vectors[0],
            right_vectors[1],
        ).det(method="domain-ge")
    )
    symmetric, remainder, mapping = sp.symmetrize(
        sp.cancel(determinant / (z1 - z2) ** 2), [z1, z2], formal=True
    )
    if remainder != 0:
        raise AssertionError("matching determinant is not symmetric")
    return sp.expand(
        symmetric.subs({mapping[0][0]: S, mapping[1][0]: P})
    )


def primitive_evans(gap: int) -> sp.Expr:
    a = -2 * LAM**4 + 16 * LAM**2 - 13
    substituted = sp.cancel(symmetric_evans(gap).subs(S, -a * P / (P + 1)))
    numerator = sp.fraction(substituted)[0]
    return sp.expand(sp.primitive(sp.Poly(numerator, P))[1].as_expr())


def reciprocal_relation() -> sp.Expr:
    a = -2 * LAM**4 + 16 * LAM**2 - 13
    b = LAM**8 - 16 * LAM**6 + 80 * LAM**4 - 128 * LAM**2 + 40
    return sp.expand((P + 1) ** 2 * (P**2 + 1 - b * P) + a**2 * P**2)


def reduced(expression: sp.Expr, relation: sp.Expr) -> sp.Expr:
    return sp.expand(sp.rem(sp.Poly(expression, P), sp.Poly(relation, P)).as_expr())


def even_to_y(expression: sp.Expr) -> sp.Expr:
    result = 0
    for (power,), coefficient in sp.Poly(sp.expand(expression), LAM).terms():
        if power % 2:
            raise AssertionError("expected even polynomial")
        result += coefficient * Y ** (power // 2)
    return sp.expand(result)


def exterior_square(matrix: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([
        [matrix.extract(rows, columns).det(method="domain-ge") for columns in EXTERIOR_BASIS]
        for rows in EXTERIOR_BASIS
    ]).applyfunc(sp.expand)


def recurrence_matrix(gap: int) -> sp.Matrix:
    right = transfer_product(gap, gap, gap + 8)
    inserted = transfer_product(gap + 8, gap, gap + 8)
    next_right = transfer_product(gap + 8, gap + 8, gap + 16)
    return (next_right * inserted * right.inv()).applyfunc(sp.expand)


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
    encoded = json.dumps(matrix_entries(matrix), separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def class_record(label: str, gap: int, q4: sp.Expr, m5: sp.Expr) -> dict[str, Any]:
    matrix = recurrence_matrix(gap)
    wedge = exterior_square(matrix)
    a_lam = q4.coeff(T, 3).subs(Y, LAM**2)
    b_lam = q4.coeff(T, 2).subs(Y, LAM**2)
    annihilator = (wedge - sp.eye(6)) * (
        wedge**4 + a_lam * wedge**3 + b_lam * wedge**2 + a_lam * wedge + sp.eye(6)
    )
    evaluated = wedge.subs(LAM, 3)
    seed = sp.eye(6)[:, 0]
    krylov = sp.Matrix.hstack(*[evaluated**power * seed for power in range(5)])
    return {
        "class": label,
        "representative_gap": gap,
        "residues": [1, 3, 5, 7] if gap % 2 else [2, 4, 6, 8],
        "C_entries": matrix_entries(matrix),
        "C_sha256": matrix_digest(matrix),
        "W_entries": matrix_entries(wedge),
        "W_sha256": matrix_digest(wedge),
        "det_C": str(sp.factor(matrix.det())),
        "characteristic": polynomial_text(even_to_y(matrix.charpoly(T).as_expr()), T, Y),
        "exterior_characteristic": polynomial_text(
            even_to_y(wedge.charpoly(T).as_expr()), T, Y
        ),
        "rank_W_minus_I_at_lam_3": int((evaluated - sp.eye(6)).rank()),
        "krylov_rows": [0, 1, 2, 3, 5],
        "krylov_minor_at_lam_3": int(
            krylov.extract((0, 1, 2, 3, 5), range(5)).det()
        ),
        "annihilator": polynomial_text(m5, T, Y),
        "annihilator_zero": all(sp.expand(value) == 0 for value in annihilator),
    }


@lru_cache(maxsize=1)
def reconstructed_certificate() -> dict[str, Any]:
    relation_lam = reciprocal_relation()
    relation_y = even_to_y(relation_lam)
    raw2, raw6 = primitive_evans(2), primitive_evans(6)
    reduced2, reduced6 = reduced(raw2, relation_lam), reduced(raw6, relation_lam)
    reversed_reduced2 = sp.expand(
        P**3 * reduced2.subs({LAM: -LAM, P: 1 / P}, simultaneous=True)
    )
    norm2_lam = sp.resultant(reduced2, relation_lam, P)
    norm6_lam = sp.resultant(reduced6, relation_lam, P)
    norm_y = sp.factor(even_to_y(norm2_lam))

    a = -Y**4 + 16 * Y**3 - 88 * Y**2 + 200 * Y - 158
    b = 2 * Y**4 - 16 * Y**3 + 36 * Y**2 - 8 * Y - 29
    q4 = T**4 + a * T**3 + b * T**2 + a * T + 1
    u = (Y - 3) * (Y**3 - 13 * Y**2 + 49 * Y - 53)
    v = (Y - 3) * (3 * Y**3 - 23 * Y**2 + 55 * Y - 43)
    m5 = sp.expand((T - 1) * q4)
    recurrence = T**5 - u * T**4 + v * T**3 - v * T**2 + u * T - 1
    discriminant = sp.factor(a**2 - 4 * (b - 2))
    characteristic = (
        T**4
        + (-2 * Y**2 + 12 * Y - 17) * T**3
        + (Y**4 - 16 * Y**3 + 88 * Y**2 - 200 * Y + 160) * T**2
        + (-2 * Y**2 + 12 * Y - 17) * T
        + 1
    )
    classes = [class_record("odd", 1, q4, m5), class_record("even", 2, q4, m5)]
    matrices = {gap: recurrence_matrix(gap) for gap in range(1, 9)}
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
            matrices[gap] == matrices[1 if gap % 2 else 2] for gap in range(1, 9)
        ),
        "all_characteristics_identical": all(
            sp.expand(even_to_y(matrices[gap].charpoly(T).as_expr()) - characteristic) == 0
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
            "characteristic": polynomial_text(characteristic, T, Y),
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


def verify(path: Path = CERTIFICATE) -> dict[str, bool]:
    stored = load_strict(path)
    expected = reconstructed_certificate()
    checks = {
        "exact_schema_and_values": stored == expected,
        "all_stored_checks_true": bool(stored.get("checks"))
        and all(stored["checks"].values()),
        "theorem_boundary_open": stored.get("status")
        == "TASK55_SINGLE_GAP_ALGEBRA_PROVED_HIERARCHY_OPEN",
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return checks


def main() -> None:
    verify()
    print("TARGET_A_TASK55_SINGLE_GAP_VERIFY_PASS")


if __name__ == "__main__":
    main()

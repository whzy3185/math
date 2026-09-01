"""Symbolic bulk/boundary templates for the residue-two fixed-cap proof."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


REPO = Path(__file__).resolve().parents[2]
OUTPUT = REPO / "research/proof_closure/r2_block_riccati_template.json"


def matrix_payload(matrix: sp.Matrix) -> list[list[str]]:
    return [[str(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]


def build() -> dict[str, object]:
    # Block sites are {2+4j,...,5+4j}; this is M=198 I-25 A^2.
    diagonal = sp.Matrix([
        [98, 0, -25, 0],
        [0, 98, 0, -25],
        [-25, 0, 98, 0],
        [0, -25, 0, 98],
    ])
    coupling_plus = sp.Matrix([
        [-25, 0, 0, 0],
        [0, 25, 0, 0],
        [-25, 50, 25, 0],
        [50, -25, 0, -25],
    ])
    coupling_minus = sp.Matrix([
        [-25, 0, 0, 0],
        [0, 25, 0, 0],
        [-25, -50, 25, 0],
        [-50, -25, 0, -25],
    ])
    involution = sp.diag(1, -1, 1, -1)
    left_core = sp.diag(98, 98)
    left_first = sp.Matrix([
        [-25, -50, 25, 0],
        [-50, -25, 0, -25],
    ])
    left_last = sp.Matrix([
        [-25, 0, -25, 0],
        [0, -25, 0, -25],
    ])
    first_last = sp.Matrix([
        [0, 0, -25, 0],
        [0, 0, 0, 25],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ])

    x11, x12, x13, x14, x22, x23, x24, x33, x34, x44 = sp.symbols(
        "x11 x12 x13 x14 x22 x23 x24 x33 x34 x44"
    )
    state = sp.Matrix([
        [x11, x12, x13, x14],
        [x12, x22, x23, x24],
        [x13, x23, x33, x34],
        [x14, x24, x34, x44],
    ])
    determinant = sp.factor(state.det())
    adjugate = state.adjugate()

    def update(coupling: sp.Matrix) -> list[list[str]]:
        numerator = diagonal * determinant - coupling.T * adjugate * coupling
        return [[str(sp.factor(numerator[i, j])) for j in range(4)] for i in range(4)]

    return {
        "status": "R2_BLOCK_RICCATI_TEMPLATE_DERIVED",
        "state_dimension": 10,
        "state_coordinates": [str(symbol) for symbol in (x11, x12, x13, x14, x22, x23, x24, x33, x34, x44)],
        "diagonal_block": matrix_payload(diagonal),
        "coupling_plus": matrix_payload(coupling_plus),
        "coupling_minus": matrix_payload(coupling_minus),
        "alternation_identity": matrix_payload(coupling_minus - involution * coupling_plus * involution),
        "determinant": str(determinant),
        "coupling_determinants": {
            "plus": str(coupling_plus.det()),
            "minus": str(coupling_minus.det()),
        },
        "differential": "D F_E(X)[H]=E^T X^(-1) H X^(-1) E",
        "generic_dimension_decision": "10; the differential is an automorphism of Sym_4 because det(E_plus)=det(E_minus)=25^4 is nonzero",
        "update_rule": "F_E(X)=(det(X) D-E^T adj(X) E)/det(X)",
        "plus_numerators": update(coupling_plus),
        "minus_numerators": update(coupling_minus),
        "bulk_map": "Phi=F_minus o F_plus",
        "boundary_core": {
            "left_block_size": 2,
            "right_block_size": 4,
            "left_core": matrix_payload(left_core),
            "left_first": matrix_payload(left_first),
            "left_last": matrix_payload(left_last),
            "first_last": matrix_payload(first_last),
            "wraparound_couplings": "these three matrices are independent of k",
        },
    }


def run() -> dict[str, object]:
    payload = build()
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": payload["status"], "state_dimension": payload["state_dimension"]}))
    return payload


if __name__ == "__main__":
    run()

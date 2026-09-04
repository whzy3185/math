#!/usr/bin/env python3
"""Independent exact audit of the invariance and half-cell chiral identities.

This script is not the proof.  It checks the displayed fiber conventions,
lift/dihedral conjugacies, the square of the monomial half-cell operator, the
chiral iff for every sign word through period 12, and the flux reformulation.
"""

from itertools import product

import sympy as sp


def fiber(tau, z):
    p = len(tau)
    matrix = sp.zeros(p)
    for r in range(p):
        transitions = (
            (-1, 1),
            (1, 1),
            (-2, tau[(r - 2) % p]),
            (2, tau[r]),
        )
        for displacement, coefficient in transitions:
            cell_shift, residue = divmod(r + displacement, p)
            matrix[r, residue] += coefficient * z**cell_shift
    return matrix


def coordinate_map(p, index_map, z):
    """Matrix of x_i -> x_{index_map(i)} on the z-Bloch fiber."""
    matrix = sp.zeros(p)
    for r in range(p):
        cell_shift, residue = divmod(index_map(r), p)
        matrix[r, residue] = z**cell_shift
    return matrix


def rotate(tau, k):
    p = len(tau)
    return tuple(tau[(i + k) % p] for i in range(p))


def reflect(tau):
    p = len(tau)
    return tuple(tau[(-i - 2) % p] for i in range(p))


def flux(tau):
    p = len(tau)
    return tuple(tau[i] * tau[(i + 1) % p] for i in range(p))


def main():
    z = sp.symbols("z", nonzero=True)

    # Lift invariance.  D maps the z-fiber to the ((-1)^p z)-fiber.
    for p in range(1, 9):
        tau = tuple(-1 if i % 3 == 0 else 1 for i in range(p))
        diagonal = sp.diag(*((-1) ** i for i in range(p)))
        lifted = tuple(-value for value in tau)
        identity = diagonal * fiber(tau, z) * diagonal + fiber(
            lifted, ((-1) ** p) * z
        )
        assert sp.simplify(identity) == sp.zeros(p)

    # Cyclic translation and reflection conjugacies.
    for p in range(3, 9):
        tau = tuple(-1 if i in (0, p - 1) else 1 for i in range(p))
        for k in range(p):
            shift = coordinate_map(p, lambda i, k=k: i + k, z)
            assert sp.simplify(
                fiber(rotate(tau, k), z) * shift - shift * fiber(tau, z)
            ) == sp.zeros(p)

        reflection = coordinate_map(p, lambda i: -i, z)
        assert sp.simplify(
            fiber(reflect(tau), z**-1) * reflection
            - reflection * fiber(tau, z)
        ) == sp.zeros(p)

    # Exact half-cell square and anticommutation iff for all words p <= 12.
    for m in range(1, 7):
        p = 2 * m
        diagonal = sp.diag(*((-1) ** i for i in range(p)))
        half_shift = coordinate_map(p, lambda i, m=m: i + m, z)
        monomial = diagonal * half_shift
        assert sp.simplify(
            monomial * monomial - ((-1) ** m) * z * sp.eye(p)
        ) == sp.zeros(p)

        for tau in product((-1, 1), repeat=p):
            anticommutes = sp.simplify(
                monomial * fiber(tau, z) + fiber(tau, z) * monomial
            ) == sp.zeros(p)
            antiperiodic = all(tau[i + m] == -tau[i] for i in range(m))
            assert anticommutes == antiperiodic

            q = flux(tau)
            flux_criterion = (
                all(q[i + m] == q[i] for i in range(m))
                and sp.prod(q[:m]) == -1
            )
            assert antiperiodic == flux_criterion

    target = (1, 1, -1, 1, -1, -1, 1, -1)
    target_flux = flux(target)
    assert target[4:] == tuple(-value for value in target[:4])
    assert target_flux == (1, -1, -1, -1, 1, -1, -1, -1)
    assert sp.prod(target_flux[:4]) == -1

    print("SYMMETRY_AND_HALF_CELL_CHIRAL_EXACT_AUDIT_PASS")


if __name__ == "__main__":
    main()

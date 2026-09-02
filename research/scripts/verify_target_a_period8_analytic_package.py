"""Independent symbolic audit of the analytic period-eight theorem package."""

from __future__ import annotations

import sympy as sp


TAU = (1, 1, -1, 1, -1, -1, 1, -1)
TWO_DEFECT_MOMENTS = {
    1: (32, 192, 1376, 10976, 93312),
    2: (32, 192, 1328, 9888, 76832, 612624, 4965328),
    3: (32, 192, 1280, 9056, 66592, 503088, 3877920, 30363808, 240761792, 1928966432),
}


def floquet(tau, z):
    matrix = sp.zeros(8)
    for output in range(8):
        for delta, coefficient in ((-2, tau[(output - 2) % 8]), (-1, 1), (1, 1), (2, tau[output])):
            source = output + delta
            cell, residue = divmod(source, 8)
            matrix[output, residue] += coefficient * z**cell
    return matrix


def tau_from_q(q):
    tau = [1]
    for sign in q[:-1]:
        tau.append(tau[-1] * sign)
    if tau[-1] * q[-1] != 1:
        raise AssertionError("illegal Q")
    return tuple(tau)


def moments(q, maximum):
    tau = tau_from_q(q)
    states = [{start: 1} for start in range(8)]
    output = []
    for length in range(1, 2 * maximum + 1):
        next_states = []
        for state in states:
            updated = {}
            for position, amplitude in state.items():
                for target, coefficient in (
                    (position - 1, 1),
                    (position + 1, 1),
                    (position - 2, tau[(position - 2) % 8]),
                    (position + 2, tau[position % 8]),
                ):
                    updated[target] = updated.get(target, 0) + amplitude * coefficient
            next_states.append(updated)
        states = next_states
        if length % 2 == 0:
            output.append(sum(states[start].get(start, 0) for start in range(8)))
    return output


def verify():
    x, y, z, xi, c = sp.symbols("x y z xi c", nonzero=True)
    h = floquet(TAU, z)
    translation = sp.zeros(8)
    for output in range(8):
        source = output + 4
        cell, residue = divmod(source, 8)
        translation[output, residue] = z**cell
    involution = xi**-1 * sp.diag(*((-1) ** index for index in range(8))) * translation
    h_xi = h.subs(z, xi**2)
    involution_xi = involution.subs(z, xi**2)
    determinant = sp.expand((x * sp.eye(8) - h).det())
    expected = y**4 - 16*y**3 + (80 - 2*c)*y**2 + (-128 + 16*c)*y + c**2 - 13*c + 38
    determinant_expected = expected.subs({y: x**2, c: z + z**-1})
    eta = 4 + sp.sqrt(10 + 2 * sp.sqrt(5))
    boundary_factorization = (y**2 - 8 * y + 6 - 2 * sp.sqrt(5)) * (
        y**2 - 8 * y + 6 + 2 * sp.sqrt(5)
    )
    taylor_lower_bound = (
        4
        + 2
        * (
            1
            - sp.Rational(10, 2 * 16**2)
            + sp.Rational(81, 24 * 16**4)
            - sp.Rational(1000, 720 * 16**6)
        )
        + 2
        * (
            1
            - sp.Rational(10, 2 * 8**2)
            + sp.Rational(81, 24 * 8**4)
            - sp.Rational(1000, 720 * 8**6)
        )
    )
    checks = {
        "chiral_square": (involution_xi**2 - sp.eye(8)).applyfunc(sp.expand) == sp.zeros(8),
        "chiral_anticommutation": (involution_xi * h_xi + h_xi * involution_xi).applyfunc(sp.expand) == sp.zeros(8),
        "floquet_determinant": sp.expand(determinant - determinant_expected) == 0,
        "boundary_factorization": sp.expand(expected.subs(c, 2) - boundary_factorization) == 0
        and sp.simplify(expected.subs({y: eta, c: 2})) == 0,
        "cosine_threshold_arithmetic": taylor_lower_bound == sp.Rational(1178731111, 150994944)
        and taylor_lower_bound > sp.Rational(1561, 200),
    }
    for separation, index, value in ((1, 4, 5504), (2, 6, 64336), (3, 9, 2872096)):
        q = [-1] * 8
        q[0] = q[separation] = 1
        values = moments(q, 10)
        checks[f"moment_table_{separation}"] = values[: len(TWO_DEFECT_MOMENTS[separation])] == list(
            TWO_DEFECT_MOMENTS[separation]
        )
        checks[f"moment_separation_{separation}"] = values[index] - 8 * values[index - 1] == value
    if not all(checks.values()):
        raise AssertionError(checks)
    return {"status": "PERIOD8_ANALYTIC_PACKAGE_AUDIT_PASS", "checks": checks}


if __name__ == "__main__":
    print(verify())

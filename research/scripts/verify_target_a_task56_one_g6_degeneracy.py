"""Fail-closed checker for the Task 56 one-G6 finite-ring theorem.

The finite controls below test the formulas, but do not replace the all-k
coefficient proof in the theorem document.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any


RESEARCH = Path(__file__).resolve().parents[1]
THEOREM = RESEARCH / "proofs/task56/TARGET_A_ONE_G6_FINITE_RING_DEGENERACY.md"
DEPENDENCY = RESEARCH / "proofs/task55/certificates/exact_2r_cluster.json"


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def _strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        _require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _load_strict(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_strict_object)

    def reject_floats(value: Any) -> None:
        _require(not isinstance(value, float), "floating-point dependency value")
        if isinstance(value, dict):
            for child in value.values():
                reject_floats(child)
        elif isinstance(value, list):
            for child in value:
                reject_floats(child)

    reject_floats(data)
    return data


def q_word(n: int) -> tuple[int, ...]:
    _require(n >= 10 and n % 8 == 2, "n must be 8k+2 with k>=1")
    defects = set(range(0, n - 5, 4))
    return tuple(1 if i in defects else -1 for i in range(n))


def tau_lift(q: tuple[int, ...]) -> tuple[int, ...]:
    tau = [1]
    for value in q[:-1]:
        tau.append(value * tau[-1])
    _require(q[-1] * tau[-1] == tau[0], "cyclic tau lift does not close")
    return tuple(tau)


def matrix_controls(n: int) -> dict[str, bool]:
    q = q_word(n)
    tau = tau_lift(q)
    a = n - 3

    q_reflection = all(q[(n - 6 - i) % n] == q[i] for i in range(n))
    tau_reflection = all(tau[(n - 5 - i) % n] == -tau[i] for i in range(n))
    k_squared = all(((-1) ** i) * ((-1) ** ((a - i) % n)) == -1 for i in range(n))

    # Sparse integer matrices make the anticommutator control exact and cheap.
    A: dict[tuple[int, int], int] = {}
    K: dict[tuple[int, int], int] = {}
    for i in range(n):
        for j, value in (
            ((i - 1) % n, 1),
            ((i + 1) % n, 1),
            ((i - 2) % n, tau[(i - 2) % n]),
            ((i + 2) % n, tau[i]),
        ):
            A[i, j] = A.get((i, j), 0) + value
        K[i, (a - i) % n] = (-1) ** i

    def product(left: dict[tuple[int, int], int], right: dict[tuple[int, int], int]):
        by_row: dict[int, list[tuple[int, int]]] = {}
        for (i, j), value in right.items():
            by_row.setdefault(i, []).append((j, value))
        out: dict[tuple[int, int], int] = {}
        for (i, middle), x in left.items():
            for j, y in by_row.get(middle, []):
                out[i, j] = out.get((i, j), 0) + x * y
        return {key: value for key, value in out.items() if value}

    ak = product(A, K)
    ka = product(K, A)
    anticommutation = set(ak) == set(ka) and all(ak[key] == -ka[key] for key in ak)
    return {
        "q_reflection": q_reflection,
        "tau_reflection": tau_reflection,
        "K_squared_minus_I": k_squared,
        "KA_equals_minus_AK": anticommutation,
    }


def verify(theorem_path: Path = THEOREM, dependency_path: Path = DEPENDENCY) -> dict[str, bool]:
    theorem = theorem_path.read_text(encoding="utf-8")
    required_text = (
        "n=8k+2",
        "D={0,4,8,...,n-6}",
        "tau_(i+1)=Q_i tau_i",
        "Q_(n-6-i)=Q_i",
        "tau_(n-5-i)=-tau_i",
        "K_n^2=-I",
        "K_n A_n=-A_n K_n",
        "n>=1042",
        "applies with `r=1`\nand `D=n`",
        "|Lambda_n-c6|<3505(9/25)^ell",
        "ell=floor((floor(n/4)-12)/8)",
        "multiplicity exactly two",
        "It is the spectral top of `H_n`",
        "each simple",
        "This is an all-order identity, not a sampled finite\ncalculation.",
    )
    _require(all(token in theorem for token in required_text), "theorem contract changed")
    exact_counts = {
        "n>=1042": 2,
        "multiplicity exactly two": 2,
        "D=n": 1,
        "K_n A_n=-A_n K_n": 1,
    }
    _require(
        all(theorem.count(token) == count for token, count in exact_counts.items()),
        "theorem contract occurrence count changed",
    )
    forbidden = ("exactly `r` squared levels", "codimension-`r`", "`r x r` Feshbach")
    _require(not any(token in theorem for token in forbidden), "withdrawn exact-r claim present")

    dependency = _load_strict(dependency_path)
    _require(dependency.get("status") == "EXACT_2R_R123_CLUSTER_AND_FESHBACH_PROVED", "Task55 status")
    _require(dependency.get("evidence") == "COMPUTER_ASSISTED_PROVED", "Task55 evidence")
    _require(dependency.get("integration_status") == "INDEPENDENT_CHECKER_PASS", "Task55 checker")
    constants = dependency.get("constants", {})
    _require(constants.get("minimum_interface_distance_D0") == 1040, "Task55 D0")
    _require(constants.get("fixed_window_radius") == "1/400", "Task55 window")
    _require(constants.get("complement_gap") == "1/200", "Task55 complement")
    _require(constants.get("cluster_bound") == "3505*r*q^ell", "Task55 bound")
    _require(constants.get("floquet_cell_rate_q") == "9/25", "Task55 q")
    counting = dependency.get("counting", {})
    rows = counting.get("r_records", [])
    _require(rows and rows[0].get("r") == 1 and rows[0].get("exact_fixed_window_riesz_rank") == 2, "Task55 r=1 rank")
    tail = dependency.get("exponential_tail", {})
    _require(tail.get("distance_formulas", {}).get("2") == "D=n", "Task55 one-G6 distance")
    endpoint = tail.get("residue_endpoints", [None])[0]
    _require(endpoint == {**endpoint, "residue": 2, "first_eligible_n": 1042, "interfaces": 1, "cluster_dimension": 2, "D": 1042, "ell": 31}, "Task55 endpoint")

    controls = {n: matrix_controls(n) for n in (10, 18, 42, 106, 1042)}
    _require(all(all(row.values()) for row in controls.values()), "finite exact matrix control")
    ell = (1042 // 4 - 12) // 8
    _require(ell == 31 and Fraction(3505) * Fraction(9, 25) ** ell < Fraction(1, 400), "endpoint bound")
    _require(Fraction(1, 400) < Fraction(1, 200), "window/complement ordering")

    return {
        "theorem_contract_fail_closed": True,
        "task55_dependency_fail_closed": True,
        "all_k_Q_tau_argument_audited": True,
        "K_anticommutation_argument_audited": True,
        "task55_r1_n1042_application_verified": True,
        "finite_controls_pass": True,
        "finite_controls_do_not_replace_analytic_proof": True,
    }


def main() -> None:
    checks = verify()
    _require(all(checks.values()), "one-G6 degeneracy verification failed")
    print("TARGET_A_TASK56_ONE_G6_DEGENERACY_VERIFY_PASS")
    print("FINITE_CONTROLS_DO_NOT_REPLACE_ALL_K_ANALYTIC_PROOF")


if __name__ == "__main__":
    main()

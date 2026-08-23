"""Independent chart checker for the Task 53 single-G6 global edge."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp
import numpy as np

from target_a_task50_g6_certificate import evans, tau_window
from target_a_task50_interval import Interval
from target_a_task52_exact import elimination_resultant


RESEARCH = Path(__file__).resolve().parents[1]
CERTIFICATE = RESEARCH / "proofs" / "task53" / "certificates" / "g6_global_edge.json"
LOWER = sp.Rational(7905369311620328, 10**15)
INTERVALS = (
    Interval(Fraction(8080985802104273, 10**15), Fraction(8080985802104274, 10**15)),
    Interval(Fraction(813985656333926, 10**14), Fraction(813985656333928, 10**14)),
)


def _strict_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_strict_object)


def rebuild_symmetry() -> dict[str, object]:
    records = []
    for dimension in (58, 90, 138):
        low = (10 - dimension) // 2
        high = 9 - low
        tau = tau_window(6, low=low - 4, high=high + 4)
        adjacency = np.zeros((dimension, dimension), dtype=np.int64)
        symmetry = np.zeros((dimension, dimension), dtype=np.int64)
        for index in range(low, high + 1):
            row = index - low
            if index + 1 <= high:
                adjacency[row, row + 1] = adjacency[row + 1, row] = 1
            if index + 2 <= high:
                adjacency[row, row + 2] = adjacency[row + 2, row] = tau[index]
            symmetry[row, 9 - index - low] = -1 if index % 2 else 1
        square = adjacency @ adjacency
        compact = lambda matrix: json.dumps(matrix.tolist(), separators=(",", ":")).encode()
        records.append({
            "dimension": dimension,
            "index_interval": [low, high],
            "A_sha256": hashlib.sha256(compact(adjacency)).hexdigest(),
            "K_sha256": hashlib.sha256(compact(symmetry)).hexdigest(),
            "K_squared_is_minus_identity": bool(np.array_equal(
                symmetry @ symmetry, -np.eye(dimension, dtype=np.int64)
            )),
            "K_anticommutes_with_A": bool(np.array_equal(
                symmetry @ adjacency, -(adjacency @ symmetry)
            )),
            "K_commutes_with_H": bool(np.array_equal(symmetry @ square, square @ symmetry)),
        })
    def q_infinite(index: int) -> int:
        left = index <= 0 and index % 4 == 0
        right = index >= 6 and (index - 6) % 4 == 0
        return 1 if left or right else -1

    q_representatives = list(range(-4, 10))
    q_checks = [q_infinite(6 - index) == q_infinite(index) for index in q_representatives]
    tau = tau_window(6, low=-8, high=16)
    tau_anchor = tau[7] == -tau[0]
    return {
        "operator": "(Ku)_i=(-1)^i u_(9-i)",
        "q_reflection_identity": "Q_(6-i)=Q_i",
        "tau_reflection_identity": "tau_(7-i)=-tau_i",
        "q_identity_domain_partition": "i<=0 and i>=6 are period-4 tails; 1<=i<=5 is checked individually",
        "q_identity_representatives": q_representatives,
        "q_identity_representative_checks": q_checks,
        "tau_identity_anchor": {"index": 0, "tau_7": tau[7], "minus_tau_0": -tau[0]},
        "tau_identity_proof": "Q_(6-i)=Q_i plus tau_7=-tau_0 propagates tau_(7-i)=-tau_i by induction in both directions",
        "tau_identity_exact": all(q_checks) and tau_anchor,
        "window_records": records,
        "spectral_consequence": (
            "K maps every A-eigenvector at lambda to one at -lambda. The simple positive "
            "G6 Evans root therefore has a simple negative partner, and the corresponding "
            "H=A^2 eigenspace at c6 has rank exactly 2."
        ),
    }


def verify_symmetry(path: Path = CERTIFICATE) -> dict[str, bool]:
    data = _load(path)
    checks = {
        "negative_spectrum_bridge_rebuilt": data.get("negative_spectrum_bridge")
        == rebuild_symmetry(),
        "squared_multiplicity_corrected": data.get("squared_level_multiplicity") == 2,
        "operator_norm_corrected": "||A6||<=4" in data.get("global_argument", "")
        and "||H6||<=4" not in data.get("global_argument", ""),
        "stored_symmetry_check_true": data.get("checks", {}).get(
            "negative_spectrum_bridge"
        ) is True,
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return checks


def verify(path: Path = CERTIFICATE) -> dict[str, bool]:
    data = _load(path)
    y = sp.symbols("y")
    _resultant, record = elimination_resultant(6)
    global_count = sum(
        int(sp.Poly(sp.sympify(row["polynomial"]), y).count_roots(LOWER, 16))
        for row in record["factors"]
    )
    alternative_chart = []
    for interval in INTERVALS:
        matching, _defect, metadata = evans(interval, gap=6, cofactor_rows=(0, 2, 3))
        alternative_chart.append(
            matching.value.excludes_zero()
            and all(row["nonzero_components"] for row in metadata["cofactor_pivots"])
        )
    local = _load(
        RESEARCH / "proofs" / "task50" / "certificates" / "g6_interface_certificate.json"
    )
    symmetry = rebuild_symmetry()
    checks = {
        "resultant_count_rebuilt": global_count == 2,
        "alternative_rows_023_exclude_both": all(alternative_chart),
        "producer_used_different_chart": all(row["cofactor_rows"] == [0, 1, 3] for row in data["candidate_records"]),
        "local_unique_root_rechecked": local["checks"]["derivative_positive"] and local["checks"]["left_sign_negative"] and local["checks"]["right_sign_positive"],
        "two_nonphysical_records": len(data["candidate_records"]) == 2 and all(
            row["classification"] == "NONPHYSICAL_FOR_G6" and row["matching_excludes_zero"]
            for row in data["candidate_records"]
        ),
        "theorem_not_status_only": "sup sigma(H6)=c6" in data["theorem"],
        "negative_spectrum_bridge_rebuilt": data["negative_spectrum_bridge"] == symmetry,
        "squared_multiplicity_corrected": data["squared_level_multiplicity"] == 2,
        "operator_norm_corrected": "||A6||<=4" in data["global_argument"]
        and "||H6||<=4" not in data["global_argument"],
        "artifact_checks_true": all(data["checks"].values()),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    verify_symmetry(path)
    return checks


def main() -> None:
    verify()
    print("TARGET_A_TASK53_A3_VERIFY_PASS")


if __name__ == "__main__":
    main()

"""Small deterministic verifier for strengthened Target A computational evidence."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import sympy as sp
from sympy.polys.numberfields import to_number_field


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = (
    REPO_ROOT
    / "research"
    / "reproducibility"
    / "target_a_computational_evidence_manifest.json"
)
ORDERS = (24, 26, 28, 30)


class ComputationalEvidenceError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ComputationalEvidenceError(message)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _exact_sign(value: sp.Expr) -> int:
    value = sp.simplify(value)
    if value == 0:
        return 0
    root = sp.simplify(to_number_field(value).to_root())
    if root.is_positive is True:
        return 1
    if root.is_negative is True:
        return -1
    raise ComputationalEvidenceError("COMPUTE_EXACT_SIGN_FAIL")


def _verify_optimizer_is_spectral_edge(n: int) -> None:
    step_one = [1] * n
    step_one[-1] = -1
    tau = [1 if index % 2 == 0 else -1 for index in range(n)]
    step_two = [
        tau[index] * step_one[index] * step_one[(index + 1) % n]
        for index in range(n)
    ]
    matrix = sp.zeros(n)
    for index in range(n):
        for offset, sign in ((1, step_one[index]), (2, step_two[index])):
            target = (index + offset) % n
            _require(matrix[index, target] == 0, f"COMPUTE_OPTIMIZER_EDGE_COLLISION:N{n}")
            matrix[index, target] = matrix[target, index] = sign
    variable = sp.Symbol("Y")
    characteristic = sp.Poly((matrix * matrix).charpoly(variable).as_expr(), variable)
    threshold = sp.simplify(
        4 * (sp.cos(sp.pi / n) ** 2 + sp.cos(2 * sp.pi / n) ** 2)
    )
    minimal = sp.Poly(sp.minimal_polynomial(threshold, variable), variable)
    _quotient, remainder = sp.div(characteristic, minimal)
    _require(remainder.is_zero, f"COMPUTE_OPTIMIZER_FACTOR_FAIL:N{n}")
    intervals = characteristic.intervals(eps=sp.Rational(1, 10**24))
    containing = []
    for (left, right), multiplicity in intervals:
        if _exact_sign(threshold - left) >= 0 and _exact_sign(right - threshold) >= 0:
            containing.append((left, right, multiplicity))
        else:
            _require(
                _exact_sign(threshold - right) > 0,
                f"COMPUTE_OPTIMIZER_LARGER_ROOT:N{n}",
            )
    _require(len(containing) == 1, f"COMPUTE_OPTIMIZER_ROOT_ISOLATION_FAIL:N{n}")


def verify(manifest_path: Path = DEFAULT_MANIFEST) -> dict[str, Any]:
    manifest = _load(manifest_path)
    _require(manifest.get("schema_version") == 1, "COMPUTE_MANIFEST_SCHEMA_FAIL")
    _require(
        manifest.get("status") == "TARGET_A_COMPUTATIONAL_EVIDENCE_COMPLETE",
        "COMPUTE_MANIFEST_STATUS_FAIL",
    )
    _require(manifest.get("orders") == list(ORDERS), "COMPUTE_ORDER_LIST_FAIL")
    files = manifest.get("files")
    _require(isinstance(files, list) and len(files) == 22, "COMPUTE_FILE_COUNT_FAIL")
    _require(len({row.get("path") for row in files}) == len(files), "COMPUTE_DUPLICATE_PATH_FAIL")
    for row in files:
        path = (REPO_ROOT / row["path"]).resolve()
        _require(path.is_relative_to(REPO_ROOT) and path.is_file(), f"COMPUTE_FILE_MISSING:{row['path']}")
        _require(_sha256(path) == row.get("sha256"), f"COMPUTE_HASH_FAIL:{row['path']}")

    set_root = REPO_ROOT / "research/reproducibility/target_a_large_order_completeness"
    spectral_root = REPO_ROOT / "research/reproducibility/target_a_independent_spectral_audit"
    set_summary = _load(set_root / "summary.json")
    spectral_summary = _load(spectral_root / "summary.json")
    _require(set_summary.get("status") == "PASS", "COMPUTE_SET_SUMMARY_FAIL")
    _require(spectral_summary.get("status") == "PASS", "COMPUTE_SPECTRAL_SUMMARY_FAIL")
    _require(set_summary.get("orders") == list(ORDERS), "COMPUTE_SET_ORDERS_FAIL")
    _require(spectral_summary.get("orders") == list(ORDERS), "COMPUTE_SPECTRAL_ORDERS_FAIL")

    reports = []
    for n, set_row, spectral_row in zip(
        ORDERS, set_summary["results"], spectral_summary["results"]
    ):
        _require(set_row["order"] == spectral_row["order"] == n, f"COMPUTE_ORDER_ALIGNMENT_FAIL:N{n}")
        set_path = set_root / set_row["file"]
        spectral_path = spectral_root / spectral_row["file"]
        _require(_sha256(set_path) == set_row["file_sha256"], f"COMPUTE_SET_DETAIL_HASH_FAIL:N{n}")
        _require(_sha256(spectral_path) == spectral_row["file_sha256"], f"COMPUTE_SPECTRAL_DETAIL_HASH_FAIL:N{n}")
        set_detail = _load(set_path)
        spectral_detail = _load(spectral_path)
        _require(set_detail.get("status") == "PASS", f"COMPUTE_SET_DETAIL_FAIL:N{n}")
        _require(all(set_detail.get("checks", {}).values()), f"COMPUTE_SET_CHECK_FAIL:N{n}")
        _require(spectral_detail.get("status") == "PASS", f"COMPUTE_SPECTRAL_DETAIL_FAIL:N{n}")
        _require(all(spectral_detail.get("checks", {}).values()), f"COMPUTE_SPECTRAL_CHECK_FAIL:N{n}")
        representatives = set_detail["number_of_canonical_dihedral_representatives"]
        states = 2 * representatives
        _require(spectral_detail["canonical_representatives"] == representatives, f"COMPUTE_REPRESENTATIVE_MISMATCH:N{n}")
        _require(spectral_detail["spectral_states"] == states, f"COMPUTE_STATE_MISMATCH:N{n}")
        _require(spectral_detail["rayleigh_certified_nonoptimizers"] == states - 1, f"COMPUTE_DECISION_COUNT_FAIL:N{n}")
        _require(spectral_detail["uncertified_states"] == [], f"COMPUTE_UNCERTIFIED_STATE:N{n}")
        _require(set_detail["sum_of_represented_switching_classes"] == 1 << (n + 1), f"COMPUTE_CLASS_TOTAL_FAIL:N{n}")
        _require(spectral_detail["represented_switching_classes"] == 1 << (n + 1), f"COMPUTE_SPECTRAL_CLASS_TOTAL_FAIL:N{n}")
        _require(spectral_detail["holonomies"] == [-1, 1], f"COMPUTE_HOLONOMY_FAIL:N{n}")
        _require(spectral_detail["optimizer"]["status"] == "EXACT_THRESHOLD_FACTOR_PASS", f"COMPUTE_OPTIMIZER_FAIL:N{n}")
        _verify_optimizer_is_spectral_edge(n)
        reports.append(
            {
                "n": n,
                "canonical_representatives": representatives,
                "spectral_states": states,
                "switching_classes": 1 << (n + 1),
                "status": "PASS",
            }
        )
    return {"status": "PASS", "reports": reports}


def main() -> None:
    report = verify()
    print("TARGET_A_COMPUTATIONAL_EVIDENCE_PASS")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

"""Verify Task 47 experiment artifacts without expanding theorem scope."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[2]
RESEARCH = REPO / "research"
BASELINE = "9d75ce04fd4509034ef65db50177d236f13479ab"


class Task47VerificationError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise Task47VerificationError(message)


def _load(path: Path) -> dict[str, Any]:
    _require(path.is_file(), f"TASK47_FILE_MISSING:{path.relative_to(REPO)}")
    return json.loads(path.read_text(encoding="utf-8"))


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _verify_script_hash(payload: dict[str, Any], name: str) -> None:
    path = RESEARCH / "scripts" / name
    _require(payload.get("script_sha256") == _sha(path), f"TASK47_SCRIPT_HASH_FAIL:{name}")


def verify() -> dict[str, Any]:
    changed = subprocess.run(
        ["git", "diff", "--name-only", BASELINE, "--", "research/paper/manuscript_tex_pub", "research/paper/manuscript_tex_pub_zh"],
        cwd=REPO,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    _require(not changed, "TASK47_MANUSCRIPT_CHANGED")

    a = _load(RESEARCH / "experiments/two_defect_geometry/summary.json")
    _verify_script_hash(a, "target_a_two_defect_geometry.py")
    _require(a.get("case_count") == 522, "TASK47_A_CASE_COUNT_FAIL")
    _require(a["summary"]["numerical_candidates_below_eta"] == 0, "TASK47_A_BELOW_ETA_FAIL")
    _require(a["summary"]["period_not_equal_8_numerical_candidates_below_8"] == 4, "TASK47_A_SUB8_COUNT_FAIL")
    target_rows = [row for row in a["records"] if row["repeated_target"]]
    _require(len(target_rows) == 1 and target_rows[0]["period"] == 8 and target_rows[0]["separation"] == 4, "TASK47_A_TARGET_FAIL")
    _require(target_rows[0]["rigorous_certificate"]["status"] == "CERTIFIED_R_EQ_ETA", "TASK47_A_TARGET_CERT_FAIL")

    b = _load(RESEARCH / "experiments/finite_phase_slips/summary.json")
    _verify_script_hash(b, "target_a_finite_phase_slips.py")
    _require(b.get("order_range") == [32, 128], "TASK47_B_RANGE_FAIL")
    _require(b.get("residues_tested") == [0, 2, 4, 6], "TASK47_B_RESIDUES_FAIL")
    _require(len(b.get("results", [])) == 49, "TASK47_B_ORDER_COUNT_FAIL")
    _require(b["certified_counterexample_count"] <= b["numerical_candidate_count"], "TASK47_B_CERT_COUNT_FAIL")
    for row in b["certified_counterexamples"]:
        candidate = REPO / row["candidate_path"]
        certificate = REPO / row["certificate_path"]
        _require(candidate.is_file() and certificate.is_file(), "TASK47_B_CERT_FILE_FAIL")
        _require(_sha(certificate) == row["certificate_sha256"], "TASK47_B_CERT_HASH_FAIL")
        detail = _load(certificate)
        if row["status"] == "CERTIFIED_FINITE_COUNTEREXAMPLE":
            _require(detail.get("result") is True, "TASK47_B_EXACT_STATUS_FAIL")

    c = _load(RESEARCH / "experiments/high_period_moments/summary.json")
    _verify_script_hash(c, "target_a_high_period_moments_task47.py")
    _require(c.get("periods") == list(range(17, 25)) and c.get("maximum_k") == 16, "TASK47_C_SCOPE_FAIL")
    _require(c["checks"]["all_period_checks_pass"], "TASK47_C_CHECK_FAIL")
    for row in c["results"]:
        _require(all(row["checks"].values()), f"TASK47_C_PERIOD_FAIL:{row['period']}")
        histogram = sum(row["first_positive_histogram"].values())
        _require(histogram + row["residual_count"] == row["dihedral_orbits"], f"TASK47_C_PARTITION_FAIL:{row['period']}")

    d = _load(RESEARCH / "experiments/high_period_certified/candidates.json")
    _verify_script_hash(d, "target_a_high_period_certified_task47.py")
    counts = d["classification_counts"]
    _require(counts["CERTIFIED_R_LT_ETA"] == 0, "TASK47_D_LT_ETA_FOUND")
    _require(counts["UNRESOLVED"] == counts["NUMERICAL_ONLY"] == 0, "TASK47_D_UNRESOLVED_FAIL")
    for row in d["candidates"]:
        path = REPO / row["certificate_file"]
        _require(_sha(path) == row["certificate_file_sha256"], "TASK47_D_CERT_HASH_FAIL")

    record = _load(RESEARCH / "reproducibility/target_a_n22_independent_record_audit/n22.json")
    spectral = _load(RESEARCH / "reproducibility/target_a_n22_independent_spectral_audit/n22.json")
    _require(record.get("status") == "PASS" and all(record["checks"].values()), "TASK47_E_RECORD_FAIL")
    _require(record["number_of_canonical_dihedral_representatives"] == 48734, "TASK47_E_REP_COUNT_FAIL")
    _require(spectral.get("status") == "PASS" and all(spectral["checks"].values()), "TASK47_E_SPECTRAL_FAIL")
    _require(spectral["spectral_states"] == 97468 and not spectral["uncertified_states"], "TASK47_E_STATE_FAIL")

    return {
        "status": "TARGET_A_TASK47_VERIFICATION_PASS",
        "manuscript_changed": False,
        "two_defect_cases": a["case_count"],
        "finite_orders": len(b["results"]),
        "moment_orbits": sum(row["dihedral_orbits"] for row in c["results"]),
        "moment_survivors_F16": sum(row["residual_count"] for row in c["results"]),
        "high_period_candidates_certified": counts["CERTIFIED_R_GT_ETA"] + counts["CERTIFIED_R_EQ_ETA"],
        "n22_spectral_states": spectral["spectral_states"],
    }


def main() -> None:
    print(json.dumps(verify(), indent=2))


if __name__ == "__main__":
    main()

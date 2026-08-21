"""Verify the immutable Target A submission artifact manifest."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = RESEARCH_ROOT.parent
DEFAULT_MANIFEST = RESEARCH_ROOT / "reproducibility" / "target_a_submission_artifact_manifest.json"


class SubmissionManifestError(RuntimeError):
    pass


def _check(condition: bool, message: str) -> None:
    if not condition:
        raise SubmissionManifestError(message)


def verify_manifest(data: dict) -> None:
    _check(data.get("schema_version") == "1.0.0", "VERIFY_SUBMISSION_MANIFEST_SCHEMA_FAIL")
    _check(data.get("status") == "TARGET_A_SUBMISSION_ARTIFACT_MANIFEST_COMPLETE", "VERIFY_SUBMISSION_MANIFEST_STATUS_FAIL")
    commit = data.get("artifact_snapshot", {}).get("commit")
    _check(commit == "bb3c8aca39a27c76e8b76bbe733b84d0fd1fafc6", "VERIFY_ARTIFACT_COMMIT_FAIL")
    resolved = subprocess.run(
        ["git", "rev-parse", commit], cwd=REPO_ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()
    _check(resolved == commit, "VERIFY_ARTIFACT_COMMIT_RESOLUTION_FAIL")
    files = data.get("files", [])
    _check(len(files) == 35, "VERIFY_ARTIFACT_FILE_COUNT_FAIL")
    _check(len({row["path"] for row in files}) == len(files), "VERIFY_ARTIFACT_DUPLICATE_PATH_FAIL")
    for row in files:
        content = subprocess.run(
            ["git", "show", f"{commit}:{row['path']}"],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
        ).stdout
        digest = hashlib.sha256(content).hexdigest()
        _check(digest == row["sha256"], f"VERIFY_ARTIFACT_SHA_FAIL:{row['path']}")
    theorem_a = data.get("theorem_a", {})
    _check(theorem_a.get("orders") == list(range(8, 33, 2)), "VERIFY_THEOREM_A_ORDER_COVERAGE_FAIL")
    _check(theorem_a.get("mathematical_mismatch_count") == 0, "VERIFY_THEOREM_A_MISMATCH_FAIL")
    _check(
        theorem_a.get("recordwise_independent_generator_orders") == [24, 26, 28, 30],
        "VERIFY_THEOREM_A_RECORDWISE_COVERAGE_FAIL",
    )
    _check(
        theorem_a.get("independent_full_spectral_decision_orders") == [24, 26, 28, 30],
        "VERIFY_THEOREM_A_INDEPENDENT_DECISION_COVERAGE_FAIL",
    )
    _check(
        "recordwise_independent_generator_limit" not in theorem_a,
        "VERIFY_THEOREM_A_OBSOLETE_RECORDWISE_LIMIT_FAIL",
    )
    theorem_f = data.get("theorem_f", {})
    _check(theorem_f.get("canonical_orbit_rows") == 2626, "VERIFY_THEOREM_F_ORBIT_COUNT_FAIL")
    _check(theorem_f.get("canonical_set_equality_checked") is True, "VERIFY_THEOREM_F_SET_BINDING_FAIL")
    _check(sum(theorem_f.get("partition", {}).values()) == 2626, "VERIFY_THEOREM_F_PARTITION_FAIL")
    _check(len(data.get("limitations", [])) == 3, "VERIFY_SUBMISSION_LIMITATIONS_FAIL")
    print("TARGET_A_SUBMISSION_ARTIFACT_HASHES_PASS")
    print("TARGET_A_THEOREM_A_ARTIFACT_COVERAGE_PASS")
    print("TARGET_A_THEOREM_F_ARTIFACT_COVERAGE_PASS")
    print("TARGET_A_SUBMISSION_ARTIFACT_MANIFEST_PASS")


def main() -> None:
    try:
        verify_manifest(json.loads(DEFAULT_MANIFEST.read_text(encoding="utf-8")))
    except Exception as error:
        print(f"Target A submission manifest verification failed: {error}", file=sys.stderr)
        print("TARGET_A_SUBMISSION_ARTIFACT_MANIFEST_FAIL")
        raise SystemExit(1)


if __name__ == "__main__":
    main()

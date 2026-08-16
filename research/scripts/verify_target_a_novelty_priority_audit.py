"""Verify the imported Target A novelty, priority, and provenance audit."""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
LITERATURE = RESEARCH_ROOT / "literature"
DEFAULT_AUDIT = LITERATURE / "target_a_novelty_priority_audit.json"
DEFAULT_LEDGER = LITERATURE / "target_a_search_query_ledger.json"
DEFAULT_SNAPSHOT = LITERATURE / "target_a_public_source_snapshot.json"
DEFAULT_NARRATIVE = LITERATURE / "TARGET_A_NOVELTY_PRIORITY_AUDIT.md"
DEFAULT_TIMELINE = LITERATURE / "TARGET_A_PROVENANCE_TIMELINE.md"
EXPECTED_HASHES = {
    "audit": "68cc3aa7c1a65877c3d7488518faf7defc0400306b59128dc9212d42dca573b4",
    "ledger": "72719ff69a5b1f0c0149d2734de253c3207d22dd854a69cf32e68ef1ca2c0235",
    "snapshot": "df3776cbeed1863bef256858d07b8100658c863fb4f79ba3af22387ac7993b79",
    "narrative": "e4711c2e6251dda1422fa0348b7dfcc054a6f40ae0cac6d1569756096b504e63",
    "timeline": "9f221c2a0deaf5ab9533fc24d5f104752cce4e25c471cbbc5c424d452cd6c39d",
}
EXPECTED_ASSESSMENTS = {
    "N1": "NO_DIRECT_PUBLIC_PRIOR_FOUND",
    "N2": "NO_DIRECT_PUBLIC_PRIOR_FOUND",
    "N3": "NO_DIRECT_PUBLIC_PRIOR_FOUND",
    "N4": "NO_DIRECT_PUBLIC_PRIOR_FOUND",
    "N5": "NO_DIRECT_PUBLIC_PRIOR_FOUND",
    "N6": "CLOSE_PRIOR_FOUND",
    "N7": "NO_DIRECT_PUBLIC_PRIOR_FOUND",
    "N8": "RELATED_METHOD_ONLY",
    "N9": "RELATED_METHOD_ONLY",
    "N10": "RELATED_METHOD_ONLY",
    "N11": "NO_DIRECT_PUBLIC_PRIOR_FOUND",
}
ALLOWED_ASSESSMENTS = {
    "DIRECT_PRIOR_FOUND",
    "CLOSE_PRIOR_FOUND",
    "RELATED_METHOD_ONLY",
    "NO_DIRECT_PUBLIC_PRIOR_FOUND",
    "UNRESOLVED",
}
FORBIDDEN_PRIORITY_WORDING = ("world first", "definitely first", "nobody has ever found")
SAFE_SENTENCE = "As of 16 August 2026, no direct public prior was found in the sources and queries recorded in this audit."


class NoveltyAuditVerificationError(RuntimeError):
    pass


def _check(condition: bool, message: str) -> None:
    if not condition:
        raise NoveltyAuditVerificationError(message)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _verify_fingerprints(snapshot: dict[str, Any]) -> None:
    for category in ("baseline_file_fingerprints", "synchronization_source_fingerprints"):
        rows = snapshot.get(category, [])
        _check(rows, f"VERIFY_{category.upper()}_EMPTY")
        for row in rows:
            path = RESEARCH_ROOT.parent / row["path"]
            _check(path.is_file(), f"VERIFY_FINGERPRINT_PATH_MISSING:{row['path']}")
            _check(_sha256(path.read_bytes()) == row["sha256"], f"VERIFY_FINGERPRINT_SHA_FAIL:{row['path']}")


def verify_audit_data(
    audit: dict[str, Any],
    ledger: dict[str, Any],
    snapshot: dict[str, Any],
    narrative: str,
    timeline: str,
) -> None:
    _check(audit.get("schema_version") == "1.1.0", "VERIFY_AUDIT_SCHEMA_FAIL")
    metadata = audit.get("audit", {})
    _check(metadata.get("target") == "Target A" and metadata.get("task") == 41, "VERIFY_AUDIT_IDENTITY_FAIL")
    _check(metadata.get("cutoff_date") == "2026-08-16", "VERIFY_AUDIT_CUTOFF_FAIL")
    _check(metadata.get("baseline_commit") == "c5cadf3ec7e160fc994453907fe83c579dc89646", "VERIFY_AUDIT_BASELINE_FAIL")
    _check(metadata.get("baseline_verified_clean") is True, "VERIFY_BASELINE_CLEAN_FAIL")
    _check(metadata.get("summary") == SAFE_SENTENCE, "VERIFY_SAFE_SUMMARY_FAIL")
    addendum = metadata.get("synchronization_addendum", {})
    _check(addendum.get("added_claims") == ["N10", "N11"], "VERIFY_ADDENDUM_CLAIMS_FAIL")
    _check(
        addendum.get("source_commits")
        == ["637de46394592f918f8e719c88648a46077f1214", "d43046f86d6b9f9ddf9a38b9d63dae0d11a7178d"],
        "VERIFY_ADDENDUM_COMMITS_FAIL",
    )

    policy = audit.get("classification_policy", {})
    _check(set(policy.get("allowed_values", [])) == ALLOWED_ASSESSMENTS, "VERIFY_ALLOWED_ASSESSMENTS_FAIL")
    claims = audit.get("claims", [])
    _check(len(claims) == 11, "VERIFY_CLAIM_COUNT_FAIL")
    assessments = {row.get("id"): row.get("assessment") for row in claims}
    _check(assessments == EXPECTED_ASSESSMENTS, "VERIFY_CLAIM_ASSESSMENTS_FAIL")
    source_ids = {row.get("id") for row in snapshot.get("sources", [])}
    _check(source_ids == {f"S{index:02d}" for index in range(1, 20)}, "VERIFY_SOURCE_ID_SET_FAIL")
    for row in claims:
        _check(row.get("assessment") in ALLOWED_ASSESSMENTS, "VERIFY_CLAIM_LABEL_FAIL")
        _check(row.get("claim") and row.get("basis") and row.get("limitations"), "VERIFY_CLAIM_EVIDENCE_FIELDS_FAIL")
        _check(set(row.get("evidence_source_ids", [])) <= source_ids, "VERIFY_CLAIM_SOURCE_REFERENCE_FAIL")
    counts = Counter(assessments.values())
    expected_counts = {label: counts.get(label, 0) for label in ALLOWED_ASSESSMENTS}
    _check(audit.get("assessment_counts") == expected_counts, "VERIFY_ASSESSMENT_COUNTS_FAIL")
    _check(expected_counts["DIRECT_PRIOR_FOUND"] == 0, "VERIFY_DIRECT_PRIOR_CONFLICT")

    disclosure = audit.get("project_origin_public_disclosure", {})
    _check(disclosure.get("repository_observed_public") is True, "VERIFY_PUBLIC_DISCLOSURE_FAIL")
    _check(disclosure.get("observed_branch") == "agent/target-a-discovery-snapshot", "VERIFY_DISCLOSURE_BRANCH_FAIL")
    synchronized = {row.get("claim"): row for row in disclosure.get("synchronization_disclosures", [])}
    _check(set(synchronized) == {"N10", "N11"}, "VERIFY_DISCLOSURE_ADDENDUM_FAIL")
    _check(all(row.get("anonymous_raw_http_status") == 200 for row in synchronized.values()), "VERIFY_DISCLOSURE_HTTP_FAIL")

    _check(ledger.get("schema_version") == "1.1.0", "VERIFY_LEDGER_SCHEMA_FAIL")
    _check(ledger.get("audit_cutoff_date") == "2026-08-16", "VERIFY_LEDGER_CUTOFF_FAIL")
    queries = ledger.get("queries", [])
    _check(len(queries) == 135, "VERIFY_QUERY_COUNT_FAIL")
    _check([row.get("id") for row in queries] == [f"Q{index:03d}" for index in range(1, 136)], "VERIFY_QUERY_SEQUENCE_FAIL")
    _check(all(row.get("service") and row.get("status") and row.get("accessed_at_utc") for row in queries), "VERIFY_QUERY_FIELDS_FAIL")
    coverage = ledger.get("coverage_summary", {})
    _check(coverage.get("query_count") == 135, "VERIFY_COVERAGE_COUNT_FAIL")
    _check(coverage.get("synchronization_addendum_query_ids") == {"start": "Q076", "end": "Q135", "claims": ["N10", "N11"]}, "VERIFY_ADDENDUM_QUERY_RANGE_FAIL")
    required_channels = {"arXiv", "Crossref", "Semantic Scholar", "Google Scholar attempted", "general web", "GitHub", "author pages", "citations and follow-ups"}
    _check(set(coverage.get("required_channels_covered", [])) == required_channels, "VERIFY_CHANNEL_COVERAGE_FAIL")
    _check("Google Scholar" in coverage.get("inaccessible_services", []), "VERIFY_GOOGLE_SCHOLAR_LIMITATION_FAIL")
    services = {row.get("service"): row for row in ledger.get("service_status", [])}
    _check(services.get("Google Scholar", {}).get("status") == "inaccessible", "VERIFY_SERVICE_STATUS_FAIL")
    _check(services.get("Semantic Scholar", {}).get("status") == "partially_accessible_rate_limited", "VERIFY_SEMANTIC_STATUS_FAIL")

    _check(snapshot.get("schema_version") == "1.1.0", "VERIFY_SNAPSHOT_SCHEMA_FAIL")
    _check(snapshot.get("snapshot_cutoff_date") == "2026-08-16", "VERIFY_SNAPSHOT_CUTOFF_FAIL")
    primary = {row["id"]: row for row in snapshot["sources"]}
    _check(primary["S01"].get("latest_version_at_cutoff") == "v1", "VERIFY_PRIMARY_VERSION_FAIL")
    _check(primary["S02"].get("latest_version_at_cutoff") == "v1", "VERIFY_COMPANION_VERSION_FAIL")
    _check(primary["S03"].get("latest_commit", {}).get("sha") == "312f0e2f0b4cdc588b3c06c4754f1df231d4da6a", "VERIFY_AUTHOR_REPO_COMMIT_FAIL")
    _verify_fingerprints(snapshot)

    combined_text = narrative + "\n" + timeline + "\n" + json.dumps(audit) + json.dumps(ledger) + json.dumps(snapshot)
    lowered = combined_text.lower()
    _check(all(phrase not in lowered for phrase in FORBIDDEN_PRIORITY_WORDING), "VERIFY_FORBIDDEN_PRIORITY_WORDING_FAIL")
    _check(SAFE_SENTENCE in narrative, "VERIFY_SAFE_NARRATIVE_SENTENCE_FAIL")
    _check("Google Scholar was inaccessible" in narrative, "VERIFY_ACCESS_LIMITATION_NARRATIVE_FAIL")
    _check("Project-origin public disclosure" in narrative or "project-origin public disclosure" in narrative, "VERIFY_PROJECT_ORIGIN_NARRATIVE_FAIL")
    _check("N10" in timeline and "N11" in timeline, "VERIFY_TIMELINE_ADDENDUM_FAIL")


def verify_files(
    audit_path: Path = DEFAULT_AUDIT,
    ledger_path: Path = DEFAULT_LEDGER,
    snapshot_path: Path = DEFAULT_SNAPSHOT,
    narrative_path: Path = DEFAULT_NARRATIVE,
    timeline_path: Path = DEFAULT_TIMELINE,
) -> None:
    paths = {
        "audit": audit_path,
        "ledger": ledger_path,
        "snapshot": snapshot_path,
        "narrative": narrative_path,
        "timeline": timeline_path,
    }
    raw = {name: path.read_bytes() for name, path in paths.items()}
    for name, content in raw.items():
        _check(_sha256(content) == EXPECTED_HASHES[name], f"VERIFY_IMPORTED_{name.upper()}_SHA_FAIL")
    verify_audit_data(
        json.loads(raw["audit"]),
        json.loads(raw["ledger"]),
        json.loads(raw["snapshot"]),
        raw["narrative"].decode(),
        raw["timeline"].decode(),
    )


def main() -> None:
    try:
        verify_files()
    except Exception as error:
        print(f"Target A novelty audit verification failed: {error}", file=sys.stderr)
        print("TARGET_A_NOVELTY_PRIORITY_AUDIT_FAIL")
        raise SystemExit(1)
    print("TARGET_A_NOVELTY_PRIORITY_AUDIT_PASS")


if __name__ == "__main__":
    main()

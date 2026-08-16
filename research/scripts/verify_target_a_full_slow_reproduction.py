"""Verify the compact Target A full slow-reproduction import."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = RESEARCH_ROOT.parent
REPRO_ROOT = RESEARCH_ROOT / "reproducibility"
DEFAULT_SUMMARY = REPRO_ROOT / "target_a_full_slow_reproduction_summary.json"
DEFAULT_NARRATIVE = REPRO_ROOT / "TARGET_A_FULL_SLOW_REPRODUCTION.md"
EXPECTED_SUMMARY_SHA256 = "6ab911dfee4f69e41b4afcfd8964bf24417944c2524c9ab2802366bf6f3f0f66"
EXPECTED_NARRATIVE_SHA256 = "ae58e24dba756d71c41e9353d26e641388ca0b682ba3d466a251fa0c876b6b06"
EXPECTED_BASELINE = "c5cadf3ec7e160fc994453907fe83c579dc89646"
EXPECTED_TREE = "dc08b21bbb5d641e8f525c844b208fe9e1d9d93b"
EXPECTED_SOURCE_HASHES = {
    "search_script_sha256": "5653c6d6b086ba00d70a3ab7d6692445334f4f0009d4400274959f74a53fd6fc",
    "generator_source_sha256": "2a972d97c1c72e2f12140336c3328362de531507b5931c0f4b442beb7ac1f5d7",
}
EXPECTED_ROWS = {
    24: (176906, 353812, 8388608, 33554432, 28, "2dde869aea5da4f040e67a4fef3e93b5f35f5fb42d75f6d48820439f418c83c1"),
    26: (649532, 1299064, 33554432, 134217728, 76, "c515350b8bea840c04448086fbc98523615364c05ca837553c93efb933bc0c4e"),
    28: (2405236, 4810472, 134217728, 536870912, 250, "7ba200b05590b2a9c0ea1121f25f89ddf1d294d0c043417e69f78f764f6e8ee1"),
    30: (8964800, 17929600, 536870912, 2147483648, 908, "b7fd264eece645eead187424152ae810a9ff940e37ffc5649b5ddf65aa31d59d"),
}
REQUIRED_STATUS_CODES = {
    "FULL_FINITE_SEARCH_REGENERATION_PASS",
    "FULL_CERTIFICATE_REPLAY_PASS",
    "FULL_SLOW_REGRESSION_PASS",
}
HEX64 = re.compile(r"[0-9a-f]{64}")


class SlowReproductionVerificationError(RuntimeError):
    pass


def _check(condition: bool, message: str) -> None:
    if not condition:
        raise SlowReproductionVerificationError(message)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _result_chain(result: dict[str, Any]) -> str:
    return result.get("final_checkpoint_chain_sha256") or result.get("checkpoint_final_chain_sha256", "")


def verify_summary_data(summary: dict[str, Any], narrative: str) -> None:
    _check(summary.get("schema_version") == "1.0.0", "VERIFY_SCHEMA_FAIL")
    _check(summary.get("status") == "TARGET_A_FULL_SLOW_REPRODUCTION_PASS", "VERIFY_STATUS_FAIL")
    baseline = summary.get("baseline", {})
    _check(baseline.get("git_commit") == EXPECTED_BASELINE, "VERIFY_BASELINE_FAIL")
    _check(baseline.get("git_tree") == EXPECTED_TREE, "VERIFY_TREE_FAIL")
    _check(baseline.get("active_repository_used_as_output") is False, "VERIFY_OUTPUT_ISOLATION_FAIL")
    _check(set(summary.get("status_codes", [])) == REQUIRED_STATUS_CODES, "VERIFY_COMPONENT_STATUS_FAIL")

    rows = summary.get("fresh_regeneration", [])
    _check([row.get("n") for row in rows] == [24, 26, 28, 30], "VERIFY_ORDER_COVERAGE_FAIL")
    for row in rows:
        n = row["n"]
        bracelets, states, q_vectors, switching, chunks, chain = EXPECTED_ROWS[n]
        _check(row.get("status") == f"VERIFIED_NO_COUNTEREXAMPLE_AT_N{n}", f"VERIFY_RESULT_STATUS_FAIL:N{n}")
        _check(row.get("q_bracelets") == bracelets, f"VERIFY_BRACELETS_FAIL:N{n}")
        _check(row.get("spectral_states") == states, f"VERIFY_STATES_FAIL:N{n}")
        _check(row.get("represented_q_vectors") == q_vectors, f"VERIFY_Q_COVERAGE_FAIL:N{n}")
        _check(row.get("represented_switching_classes") == switching, f"VERIFY_SWITCHING_COVERAGE_FAIL:N{n}")
        _check(row.get("checkpoint_chunks") == chunks, f"VERIFY_CHUNKS_FAIL:N{n}")
        _check(row.get("exact_fallbacks") == 0 and row.get("counterexamples") == [], f"VERIFY_OUTCOME_FAIL:N{n}")
        _check(all(row.get("completion_checks", {}).values()), f"VERIFY_COMPLETION_CHECKS_FAIL:N{n}")
        hashes = row.get("hashes", {})
        _check(hashes.get("final_checkpoint_chain_sha256") == chain, f"VERIFY_CHAIN_FAIL:N{n}")
        _check(all(HEX64.fullmatch(value or "") for value in hashes.values()), f"VERIFY_HASH_FORMAT_FAIL:N{n}")

    replay = summary.get("committed_certificate_replay", {})
    _check(replay.get("status") == "PASS", "VERIFY_REPLAY_STATUS_FAIL")
    _check(replay.get("orders") == [24, 26, 28, 30], "VERIFY_REPLAY_ORDERS_FAIL")
    _check(replay.get("checks_per_order") == 12 and replay.get("all_checks_true") is True, "VERIFY_REPLAY_CHECKS_FAIL")
    slow = summary.get("slow_generator_regression", {})
    _check(slow.get("status") == "PASS", "VERIFY_SLOW_STATUS_FAIL")
    _check((slow.get("passed"), slow.get("failed")) == (3, 0), "VERIFY_SLOW_COUNTS_FAIL")
    _check(all("DirectBraceletTests::" in test for test in slow.get("tests", [])), "VERIFY_SLOW_SELECTORS_FAIL")

    incidents = summary.get("operational_incidents", [])
    _check({row.get("kind") for row in incidents} == {"manager_restart", "pytest_selector_error"}, "VERIFY_INCIDENT_SET_FAIL")
    _check(all(row.get("mathematical_mismatch") is False for row in incidents), "VERIFY_INCIDENT_MISMATCH_FAIL")
    comparison = summary.get("comparison", {})
    _check(comparison.get("fresh_and_committed_core_results_match") is True, "VERIFY_CORE_COMPARISON_FAIL")
    _check(comparison.get("fresh_and_committed_final_checkpoint_chains_match") is True, "VERIFY_CHAIN_COMPARISON_FAIL")
    _check(comparison.get("fresh_and_committed_manifest_file_hashes_match") is False, "VERIFY_MANIFEST_EQUALITY_CLAIM_FAIL")
    _check(comparison.get("manifest_hash_difference_expected") is True, "VERIFY_MANIFEST_EXPLANATION_FAIL")
    _check(comparison.get("mismatch_count") == 0, "VERIFY_MISMATCH_COUNT_FAIL")

    imported = summary.get("repository_import", {})
    _check(imported == {"large_chunk_files_committed": False, "full_logs_committed": False, "compact_summary_only": True}, "VERIFY_COMPACT_IMPORT_FAIL")
    gate = summary.get("paper_gate", {})
    _check(gate.get("status") == "PAPER_PACKAGE_READY", "VERIFY_PAPER_GATE_FAIL")
    _check(all(gate.get(key) == "PASS" for key in ("novelty_priority_audit", "stable_new_theorem", "default_tests", "slow_evidence_without_mismatch", "claim_scope_frozen")), "VERIFY_PAPER_GATE_COMPONENT_FAIL")
    _check("before manuscript drafting" in gate.get("next_stage", ""), "VERIFY_PRE_MANUSCRIPT_STAGE_FAIL")

    for token in (
        "TARGET_A_FULL_SLOW_REPRODUCTION_PASS",
        "FULL_FINITE_SEARCH_REGENERATION_PASS",
        "FULL_CERTIFICATE_REPLAY_PASS",
        "FULL_SLOW_REGRESSION_PASS",
        "PAPER_PACKAGE_READY",
        "No manuscript drafting is started",
    ):
        _check(token in narrative, f"VERIFY_NARRATIVE_TOKEN_FAIL:{token}")
    _check("all-period optimality" in narrative and "does not claim" in narrative, "VERIFY_SCOPE_CAVEAT_FAIL")


def verify_committed_evidence(summary: dict[str, Any]) -> None:
    evidence = summary["evidence_file_hashes"]
    source_paths = {
        "search_script_sha256": RESEARCH_ROOT / "scripts" / "target_a_minimality_search.py",
        "generator_source_sha256": RESEARCH_ROOT / "scripts" / "target_a_bracelets.py",
    }
    for key, path in source_paths.items():
        _check(evidence.get(key) == EXPECTED_SOURCE_HASHES[key], f"VERIFY_SOURCE_DECLARATION_FAIL:{key}")
        _check(_sha256(path.read_bytes()) == EXPECTED_SOURCE_HASHES[key], f"VERIFY_SOURCE_FILE_FAIL:{key}")

    for row in summary["fresh_regeneration"]:
        n = row["n"]
        hashes = row["hashes"]
        result_path = RESEARCH_ROOT / "logs" / f"target_a_search_n{n}.json"
        manifest_path = RESEARCH_ROOT / "logs" / "checkpoints" / f"n{n}" / "manifest.json"
        _check(_sha256(result_path.read_bytes()) == hashes["committed_result_file_sha256"], f"VERIFY_COMMITTED_RESULT_SHA_FAIL:N{n}")
        _check(_sha256(manifest_path.read_bytes()) == hashes["committed_checkpoint_manifest_sha256"], f"VERIFY_COMMITTED_MANIFEST_SHA_FAIL:N{n}")
        result = _load(result_path)
        _check(result.get("completed_q_bracelets") == row["q_bracelets"], f"VERIFY_COMMITTED_BRACELETS_FAIL:N{n}")
        _check(result.get("completed_spectral_states") == row["spectral_states"], f"VERIFY_COMMITTED_STATES_FAIL:N{n}")
        _check(result.get("ordered_input_sha256") == hashes["ordered_input_sha256"], f"VERIFY_COMMITTED_INPUT_HASH_FAIL:N{n}")
        _check(result.get("ordered_certificate_sha256") == hashes["ordered_certificate_sha256"], f"VERIFY_COMMITTED_CERT_HASH_FAIL:N{n}")
        _check(_result_chain(result) == hashes["final_checkpoint_chain_sha256"], f"VERIFY_COMMITTED_CHAIN_FAIL:N{n}")

    replay_path = RESEARCH_ROOT / "audit" / "target_a_minimality_checkpoint_replay.json"
    replay = _load(replay_path)
    _check(_sha256(replay_path.read_bytes()) == summary["committed_certificate_replay"]["result_file_sha256"], "VERIFY_REPLAY_FILE_SHA_FAIL")
    _check(replay.get("status") == "PASS", "VERIFY_REPLAY_FILE_STATUS_FAIL")
    _check(all(report.get("status") == "PASS" and all(report.get("checks", {}).values()) for report in replay.get("reports", [])), "VERIFY_REPLAY_FILE_CHECKS_FAIL")


def verify_external_evidence(summary: dict[str, Any], external_root: Path) -> None:
    evidence_paths = {
        "manager_state_sha256": external_root / "manager-state.json",
        "events_sha256": external_root / "events.jsonl",
        "slow_test_inventory_sha256": external_root / "SLOW_TEST_INVENTORY.md",
        "manager_script_sha256": external_root / "lane_r_manager.py",
    }
    for key, path in evidence_paths.items():
        _check(path.is_file(), f"VERIFY_EXTERNAL_FILE_MISSING:{path}")
        _check(_sha256(path.read_bytes()) == summary["evidence_file_hashes"][key], f"VERIFY_EXTERNAL_SHA_FAIL:{key}")

    slow_log = external_root / "logs" / "slow-generator-tests.log"
    _check(_sha256(slow_log.read_bytes()) == summary["slow_generator_regression"]["log_sha256"], "VERIFY_EXTERNAL_SLOW_LOG_SHA_FAIL")
    _check("3 passed in 154.54s" in slow_log.read_text(encoding="utf-8"), "VERIFY_EXTERNAL_SLOW_LOG_RESULT_FAIL")
    replay_path = external_root / "manifests" / "committed_certificate_replay.json"
    _check(_sha256(replay_path.read_bytes()) == summary["committed_certificate_replay"]["result_file_sha256"], "VERIFY_EXTERNAL_REPLAY_SHA_FAIL")

    for row in summary["fresh_regeneration"]:
        n = row["n"]
        hashes = row["hashes"]
        result_path = external_root / "manifests" / f"target_a_search_n{n}.json"
        manifest_path = external_root / "checkpoints" / f"n{n}" / "manifest.json"
        _check(_sha256(result_path.read_bytes()) == hashes["fresh_result_file_sha256"], f"VERIFY_FRESH_RESULT_SHA_FAIL:N{n}")
        _check(_sha256(manifest_path.read_bytes()) == hashes["fresh_checkpoint_manifest_sha256"], f"VERIFY_FRESH_MANIFEST_SHA_FAIL:N{n}")
        result = _load(result_path)
        _check(result.get("git_commit") == EXPECTED_BASELINE, f"VERIFY_FRESH_BASELINE_FAIL:N{n}")
        _check(result.get("completed_q_bracelets") == row["q_bracelets"], f"VERIFY_FRESH_BRACELETS_FAIL:N{n}")
        _check(result.get("completed_spectral_states") == row["spectral_states"], f"VERIFY_FRESH_STATES_FAIL:N{n}")
        _check(result.get("represented_q_vectors") == row["represented_q_vectors"], f"VERIFY_FRESH_Q_COVERAGE_FAIL:N{n}")
        _check(result.get("represented_switching_classes") == row["represented_switching_classes"], f"VERIFY_FRESH_SWITCHING_COVERAGE_FAIL:N{n}")
        _check(_result_chain(result) == hashes["final_checkpoint_chain_sha256"], f"VERIFY_FRESH_CHAIN_FAIL:N{n}")
        _check(result.get("ordered_input_sha256") == hashes["ordered_input_sha256"], f"VERIFY_FRESH_INPUT_HASH_FAIL:N{n}")
        _check(result.get("ordered_certificate_sha256") == hashes["ordered_certificate_sha256"], f"VERIFY_FRESH_CERT_HASH_FAIL:N{n}")
        _check(result.get("exact_fallbacks") == 0 and result.get("counterexamples") == [], f"VERIFY_FRESH_OUTCOME_FAIL:N{n}")


def verify_files(external_root: Path | None = None) -> None:
    summary_raw = DEFAULT_SUMMARY.read_bytes()
    narrative_raw = DEFAULT_NARRATIVE.read_bytes()
    _check(_sha256(summary_raw) == EXPECTED_SUMMARY_SHA256, "VERIFY_IMPORTED_SUMMARY_SHA_FAIL")
    _check(_sha256(narrative_raw) == EXPECTED_NARRATIVE_SHA256, "VERIFY_IMPORTED_NARRATIVE_SHA_FAIL")
    summary = json.loads(summary_raw)
    verify_summary_data(summary, narrative_raw.decode())
    verify_committed_evidence(summary)
    _check(not list(REPRO_ROOT.rglob("chunk_*.json")), "VERIFY_LARGE_CHUNK_IMPORT_FAIL")
    if external_root is not None:
        verify_external_evidence(summary, external_root)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--external-root", type=Path)
    args = parser.parse_args()
    try:
        verify_files(args.external_root)
    except Exception as error:
        print(f"Target A slow reproduction verification failed: {error}", file=sys.stderr)
        print("TARGET_A_FULL_SLOW_REPRODUCTION_FAIL")
        raise SystemExit(1)
    print("TARGET_A_FULL_SLOW_REPRODUCTION_PASS")


if __name__ == "__main__":
    main()

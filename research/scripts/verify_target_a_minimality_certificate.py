"""Independently derive and verify the Target A smallest-order conclusion."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

from target_a_checkpoint_replay import replay_saved_search
from verify_target_a_n32_certificate import verify_n32_certificate


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CERTIFICATE = (
    RESEARCH_ROOT / "counterexamples" / "target_a_minimality_certificate.json"
)
PRODUCTION_ORDERS = (24, 26, 28, 30)
TRUSTED_EVIDENCE_SHA256 = {
    "research/logs/target_a_reproduction_n8_18.json": "141d0253159acde39473cf4f825f65d438cd56e8433e407c3302fe048ad3715e",
    "research/logs/target_a_search_n20.json": "20a0d812a268d51c4c52188c63827732216815f20901ef83ad680816d82fbcc4",
    "research/logs/target_a_flux_search_n22.json": "588c5998a83d01c0db9cbc81d0551cbd04d66823c58ce7f506b259e8125264be",
    "research/logs/target_a_search_n24.json": "3fea700914b3c2d8a08a26bbaf490432123ed1a877c231f0d53ddbdf8f394a51",
    "research/logs/target_a_search_n26.json": "9cb022a9bc7ba5e2ad7d8d1d0427ec3073a64aae60a09ef032f0a2286875f815",
    "research/logs/target_a_search_n28.json": "07644fbae5bbb93da64bc9d532a1a4a41bc38d013dd96ab2b19524f0fe524269",
    "research/logs/target_a_search_n30.json": "34bbeba4b07723eff94eb8cc7b19f640ea2c07674e72cb5b91b3c74ba1a0b449",
    "research/logs/checkpoints/n24/manifest.json": "978b38db75ccf8d05bd7bae76b28373d5a0b56655299ea2a65cc25722514a98b",
    "research/logs/checkpoints/n26/manifest.json": "59d106f91ff5bd457e25c1676233970ee46382e4ace7c8e41b7769b85d5b140d",
    "research/logs/checkpoints/n28/manifest.json": "e1d1411f0563915c282651d12858c77671b5a8153ac2b47357373d7963b2fc91",
    "research/logs/checkpoints/n30/manifest.json": "56b0cc2c8d12da9d99ca49d66d136d7b40a517cb4211f8fed5eb7b69c83ec7d4",
    "research/counterexamples/target_a_n32_period8.json": "c5ecd532da469092ef98fe2385dfb69b8da542595f942cd88b881d985b72bc10",
    "research/counterexamples/target_a_n32_period8_certificate.json": "db1378c6a7e5ab8526890be41c929a60ee17675d920a5ca0c501f49d888e46b4",
}


class MinimalityCertificateError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise MinimalityCertificateError(message)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _require_trusted(relative_path: str, actual_sha256: str) -> None:
    expected = TRUSTED_EVIDENCE_SHA256.get(relative_path)
    _require(expected is not None, f"no committed provenance anchor for {relative_path}")
    _require(
        actual_sha256 == expected,
        f"EVIDENCE_HASH_MISMATCH: committed provenance for {relative_path}",
    )


def _resolve(research_root: Path, relative_path: str) -> Path:
    _require(isinstance(relative_path, str), "dependency path is not a string")
    path = (research_root.parent / relative_path).resolve()
    _require(path.is_relative_to(research_root.resolve()), f"path escapes research root: {relative_path}")
    _require(path.is_file(), f"missing dependency: {relative_path}")
    return path


def _parse_domain(spec_path: Path) -> tuple[int, str]:
    text = spec_path.read_text(encoding="utf-8")
    domain_match = re.search(
        r"## Domain\s+.*?`n` is an even integer with `n(?:≥|>=)(\d+)`",
        text,
        flags=re.DOTALL,
    )
    if not domain_match:
        raise MinimalityCertificateError("DOMAIN_AUDIT_FAIL: domain rule not found")
    minimum = int(domain_match.group(1))
    _require(minimum == 8, "DOMAIN_AUDIT_FAIL: lower bound is not 8")
    _require(
        "`n` odd is outside the conjecture" in text,
        "DOMAIN_AUDIT_FAIL: odd-order exclusion is absent",
    )
    _require(
        "spectral radius of either twisted class with alternating triangle flux and step-1 Hamilton-cycle holonomy `α=−1`"
        in text,
        "DOMAIN_AUDIT_FAIL: distinguished optimizer equality is absent",
    )
    return minimum, "even n >= 8"


def _entry_by_n(payload: dict[str, Any], n: int) -> dict[str, Any]:
    matches = [item for item in payload.get("results", []) if item.get("n") == n]
    _require(len(matches) == 1, f"finite source has {len(matches)} records for n={n}")
    return matches[0]


def _audit_raw(entry: dict[str, Any], source: dict[str, Any]) -> None:
    n = entry["n"]
    result = _entry_by_n(source, n)
    expected = 2 ** (n + 1)
    _require(source.get("overall") == "PASS", f"n={n} source overall is not PASS")
    _require(result.get("status") == "PASS" and result.get("exhaustive") is True, f"n={n} is not exhaustive PASS")
    _require(result.get("switching_classes") == expected, f"n={n} switching-class count mismatch")
    checks = result.get("optimizer_exact_checks")
    _require(isinstance(checks, list) and len(checks) == 2, f"n={n} optimizer exact records missing")
    _require(all(item.get("multiplicity") == 4 for item in checks), f"n={n} optimizer multiplicity mismatch")
    rayleigh = result.get("rayleigh_certified_nonoptimizers")
    fallbacks = result.get("exact_fallbacks")
    _require(rayleigh + fallbacks == expected - 2, f"n={n} nonoptimizer certificate count mismatch")
    _require(fallbacks == 0 and result.get("counterexamples") == [], f"n={n} has fallback or counterexample")
    _require(entry.get("expected_search_space") == {"switching_classes": expected}, f"n={n} certificate expected count changed")
    _require(entry.get("completed_search_space") == {"switching_classes": expected}, f"n={n} certificate completed count changed")
    _require(entry.get("completion_fraction") == 1, f"n={n} completion fraction changed")
    _require(entry.get("rayleigh_certified") == rayleigh, f"n={n} Rayleigh count changed")
    _require(entry.get("exact_fallbacks") == fallbacks, f"n={n} fallback count changed")
    _require(entry.get("counterexamples") == 0, f"n={n} certificate counterexample count is nonzero")
    _require(entry.get("optimizer_exact_check", {}).get("status") == "PASS", f"n={n} certificate optimizer status changed")


def _audit_n22(entry: dict[str, Any], result: dict[str, Any]) -> None:
    _require(result.get("n") == 22 and result.get("status") == "PASS", "n=22 source is not PASS")
    _require(result.get("max_defects") is None, "n=22 source is a truncated defect search")
    expected = {"q_orbits": 48734, "spectral_states": 97468, "represented_switching_classes": 2**23}
    completed = {key: result.get(key) for key in expected}
    _require(completed == expected, "n=22 top-level completion mismatch")
    shells = result.get("shell_summaries")
    _require(isinstance(shells, list) and {item["defect_count"] for item in shells} == set(range(0, 23, 2)), "n=22 shell coverage mismatch")
    for key in ("q_orbits", "spectral_states", "represented_switching_classes"):
        _require(sum(item[key] for item in shells) == expected[key], f"n=22 shell {key} mismatch")
    rayleigh = result.get("rayleigh_certified_nonoptimizers")
    fallbacks = result.get("exact_fallbacks")
    _require(rayleigh + fallbacks == expected["spectral_states"] - 1, "n=22 certificate count mismatch")
    _require(fallbacks == 0 and result.get("counterexamples") == [], "n=22 has fallback or counterexample")
    optimizer_rows = [
        row for row in result.get("atlas", [])
        if row.get("defect_count") == 0 and row.get("alpha") == -1
    ]
    _require(len(optimizer_rows) == 1, "n=22 distinguished optimizer state missing")
    _require(entry.get("expected_search_space") == expected, "n=22 certificate expected count changed")
    _require(entry.get("completed_search_space") == expected, "n=22 certificate completed count changed")
    _require(entry.get("completion_fraction") == 1, "n=22 completion fraction changed")
    _require(entry.get("rayleigh_certified") == rayleigh, "n=22 Rayleigh count changed")
    _require(entry.get("exact_fallbacks") == 0 and entry.get("counterexamples") == 0, "n=22 certificate decision changed")
    optimizer = entry.get("optimizer_exact_check", {})
    _require(
        optimizer.get("status") == "ESTABLISHED_BY_DISTINGUISHED_THRESHOLD_DEFINITION"
        and optimizer.get("serialized_in_historical_schema") is False
        and optimizer.get("optimizer_state") == {"defect_count": 0, "alpha": -1},
        "n=22 historical optimizer compatibility changed",
    )


def _audit_production(
    entry: dict[str, Any], result: dict[str, Any], research_root: Path
) -> None:
    n = entry["n"]
    _require(result.get("n") == n, f"n={n} result order mismatch")
    _require(result.get("status") == f"VERIFIED_NO_COUNTEREXAMPLE_AT_N{n}", f"n={n} result status mismatch")
    _require(result.get("completion_fraction") == 1, f"n={n} incomplete result")
    _require(result.get("expected_q_bracelets") == result.get("completed_q_bracelets"), f"n={n} bracelet completion mismatch")
    _require(result.get("expected_spectral_states") == result.get("completed_spectral_states"), f"n={n} state completion mismatch")
    _require(result.get("represented_switching_classes") == 2 ** (n + 1), f"n={n} represented class count mismatch")
    _require(result.get("optimizer") == {"defect_count": 0, "canonical_q_code": 0, "alpha": -1}, f"n={n} optimizer mismatch")
    optimizer_check = result.get("optimizer_exact_check")
    _require(
        isinstance(optimizer_check, dict)
        and optimizer_check.get("multiplicity") == 4
        and isinstance(optimizer_check.get("charpoly_A2"), str)
        and len(optimizer_check.get("threshold_root_interval", [])) == 2,
        f"n={n} optimizer exact check missing",
    )
    rayleigh = result.get("rayleigh_certified")
    fallbacks = result.get("exact_fallbacks")
    _require(rayleigh + fallbacks == result["completed_spectral_states"] - 1, f"n={n} certificate count mismatch")
    _require(fallbacks == 0 and result.get("counterexamples") == [], f"n={n} has fallback or counterexample")
    expected = {
        "q_bracelets": result["expected_q_bracelets"],
        "spectral_states": result["expected_spectral_states"],
        "represented_switching_classes": 2 ** (n + 1),
    }
    completed = {
        "q_bracelets": result["completed_q_bracelets"],
        "spectral_states": result["completed_spectral_states"],
        "represented_switching_classes": result["represented_switching_classes"],
    }
    _require(entry.get("expected_search_space") == expected, f"n={n} certificate expected count changed")
    _require(entry.get("completed_search_space") == completed, f"n={n} certificate completed count changed")
    _require(entry.get("completion_fraction") == 1, f"n={n} certificate completion changed")
    _require(entry.get("rayleigh_certified") == rayleigh, f"n={n} certificate Rayleigh count changed")
    _require(entry.get("exact_fallbacks") == 0 and entry.get("counterexamples") == 0, f"n={n} certificate decision changed")
    _require(entry.get("optimizer_exact_check", {}).get("status") == "PASS", f"n={n} certificate optimizer status changed")
    manifest_path = _resolve(research_root, entry.get("checkpoint_manifest"))
    manifest_hash = _sha256(manifest_path)
    _require_trusted(entry["checkpoint_manifest"], manifest_hash)
    _require(manifest_hash == entry.get("checkpoint_manifest_sha256"), f"n={n} EVIDENCE_HASH_MISMATCH: manifest")
    _require(manifest_hash == result.get("checkpoint_manifest_sha256"), f"n={n} result/manifest provenance mismatch")


def verify_minimality_certificate(
    certificate_path: Path = DEFAULT_CERTIFICATE,
    research_root: Path = RESEARCH_ROOT,
    run_replays: bool = True,
) -> dict[str, Any]:
    certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
    _require(certificate.get("schema_version") == 1, "unsupported certificate schema")
    conjecture = certificate.get("conjecture", {})
    _require(conjecture.get("id") == "C029", "wrong conjecture id")
    spec_path = _resolve(research_root, conjecture.get("domain_spec_file"))
    _require(_sha256(spec_path) == conjecture.get("domain_spec_sha256"), "EVIDENCE_HASH_MISMATCH: domain spec")
    minimum, domain = _parse_domain(spec_path)
    _require(conjecture.get("domain") == domain, "certificate domain text mismatch")
    _require(conjecture.get("failure_condition") == "rho(A_sigma) < rho_-(n)", "failure condition mismatch")

    claimed_order = certificate.get("claim", {}).get("smallest_counterexample_order")
    _require(type(claimed_order) is int and claimed_order == 32, "claimed first order is not 32")
    required_orders = list(range(minimum, claimed_order, 2))
    _require(required_orders == list(range(8, 32, 2)), "generated admissible order sequence mismatch")
    _require(certificate.get("required_orders_below_32") == required_orders, "required-order list mismatch")
    entries = certificate.get("finite_no_counterexample_orders")
    _require(isinstance(entries, list), "finite evidence list missing")
    orders = [entry.get("n") for entry in entries]
    _require(orders == required_orders and len(set(orders)) == len(orders), "missing, duplicate, or unordered finite evidence")

    for entry in entries:
        n = entry["n"]
        source_path = _resolve(research_root, entry.get("source_file"))
        source_hash = _sha256(source_path)
        _require_trusted(entry["source_file"], source_hash)
        _require(source_hash == entry.get("source_sha256"), f"n={n} EVIDENCE_HASH_MISMATCH: result")
        source = json.loads(source_path.read_text(encoding="utf-8"))
        if n <= 20:
            _audit_raw(entry, source)
        elif n == 22:
            _audit_n22(entry, source)
        else:
            _audit_production(entry, source, research_root)
        _require(entry.get("status") == "VERIFIED_NO_COUNTEREXAMPLE", f"n={n} certificate status changed")
    _require(certificate.get("domain_coverage_complete") is True, "certificate domain coverage flag is false")

    if run_replays:
        replay_reports = [replay_saved_search(n, research_root) for n in PRODUCTION_ORDERS]
        _require(all(report["status"] == "PASS" for report in replay_reports), "checkpoint replay failed")
    else:
        replay_reports = []
    saved_replay = certificate.get("checkpoint_replays", {})
    saved_replay_path = _resolve(research_root, saved_replay.get("source_file"))
    _require(_sha256(saved_replay_path) == saved_replay.get("source_sha256"), "EVIDENCE_HASH_MISMATCH: replay audit")
    replay_payload = json.loads(saved_replay_path.read_text(encoding="utf-8"))
    _require(replay_payload.get("status") == "PASS", "saved checkpoint replay is not PASS")
    _require([report["n"] for report in replay_payload.get("reports", [])] == list(PRODUCTION_ORDERS), "saved checkpoint replay order mismatch")
    if run_replays:
        _require(replay_payload["reports"] == replay_reports, "fresh checkpoint replay differs from saved audit")

    n32 = certificate.get("n32_counterexample", {})
    _require(n32.get("n") == claimed_order, "n=32 counterexample order mismatch")
    witness_path = _resolve(research_root, n32.get("witness_file"))
    exact_certificate_path = _resolve(research_root, n32.get("exact_certificate_file"))
    witness_hash = _sha256(witness_path)
    exact_certificate_hash = _sha256(exact_certificate_path)
    _require_trusted(n32["witness_file"], witness_hash)
    _require_trusted(n32["exact_certificate_file"], exact_certificate_hash)
    _require(witness_hash == n32.get("witness_sha256"), "EVIDENCE_HASH_MISMATCH: n32 witness")
    _require(exact_certificate_hash == n32.get("exact_certificate_sha256"), "EVIDENCE_HASH_MISMATCH: n32 exact certificate")
    n32_report = verify_n32_certificate(witness_path, exact_certificate_path)
    _require(n32_report["status"] == "N32_COUNTEREXAMPLE_EXACT_PASS", "n=32 exact verifier failed")
    _require(max(required_orders) + 2 == claimed_order, "32 is not the next admissible order")

    dependency = certificate.get("dependencies", {})
    dependency_path = _resolve(research_root, dependency.get("manifest_file"))
    _require(_sha256(dependency_path) == dependency.get("manifest_sha256"), "EVIDENCE_HASH_MISMATCH: dependency manifest")
    manifest = json.loads(dependency_path.read_text(encoding="utf-8"))
    paths = [item.get("path") for item in manifest.get("dependencies", [])]
    _require(len(paths) == len(set(paths)), "duplicate dependency manifest path")
    for item in manifest.get("dependencies", []):
        path = _resolve(research_root, item.get("path"))
        _require(_sha256(path) == item.get("sha256"), f"EVIDENCE_HASH_MISMATCH: {item.get('path')}")

    for checker_key in ("certificate_checker", "n32_certificate_checker"):
        checker = certificate.get(checker_key, {})
        checker_path = _resolve(research_root, checker.get("source_file"))
        _require(_sha256(checker_path) == checker.get("source_sha256"), f"EVIDENCE_HASH_MISMATCH: {checker_key}")

    return {
        "status": "SMALLEST_COUNTEREXAMPLE_VERIFIED",
        "domain": domain,
        "required_orders_below_32": required_orders,
        "finite_evidence_count": len(entries),
        "first_counterexample_order": claimed_order,
        "n32_status": n32_report["status"],
        "checkpoint_replays": replay_reports if run_replays else "not requested",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    args = parser.parse_args()
    try:
        verify_minimality_certificate(args.certificate)
    except Exception as error:
        print(f"Target A minimality certificate failed: {error}", file=sys.stderr)
        print("TARGET_A_MINIMALITY_CERTIFICATE_FAIL")
        raise SystemExit(1)
    print("TARGET_A_MINIMALITY_CERTIFICATE_PASS")


if __name__ == "__main__":
    main()

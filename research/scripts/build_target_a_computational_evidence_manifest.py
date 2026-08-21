"""Build the authenticated manifest for strengthened Target A computation."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUT = (
    REPO_ROOT
    / "research"
    / "reproducibility"
    / "target_a_computational_evidence_manifest.json"
)
PATHS = [
    "research/scripts/target_a_independent_orbit_scan.c",
    "research/scripts/target_a_record_set_audit.py",
    "research/scripts/target_a_independent_spectral_audit.py",
    "research/scripts/target_a_bracelets.py",
    "research/scripts/verify_target_a_computational_evidence.py",
    "research/scripts/test_target_a_computational_evidence.py",
    "research/scripts/build_target_a_computational_evidence_manifest.py",
    "research/reproducibility/target_a_large_order_completeness/summary.json",
    "research/reproducibility/target_a_large_order_completeness/n24.json",
    "research/reproducibility/target_a_large_order_completeness/n26.json",
    "research/reproducibility/target_a_large_order_completeness/n28.json",
    "research/reproducibility/target_a_large_order_completeness/n30.json",
    "research/reproducibility/target_a_independent_spectral_audit/summary.json",
    "research/reproducibility/target_a_independent_spectral_audit/n24.json",
    "research/reproducibility/target_a_independent_spectral_audit/n26.json",
    "research/reproducibility/target_a_independent_spectral_audit/n28.json",
    "research/reproducibility/target_a_independent_spectral_audit/n30.json",
    "research/review/TARGET_A_FINITE_MINIMALITY_TRUST_MAP.md",
    "research/logs/checkpoints/n24/manifest.json",
    "research/logs/checkpoints/n26/manifest.json",
    "research/logs/checkpoints/n28/manifest.json",
    "research/logs/checkpoints/n30/manifest.json",
]


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    files = []
    for relative in PATHS:
        path = REPO_ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(relative)
        files.append({"path": relative, "sha256": _sha256(path)})
    head = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    return {
        "schema_version": 1,
        "status": "TARGET_A_COMPUTATIONAL_EVIDENCE_COMPLETE",
        "repository_head_at_manifest_build": head,
        "orders": [24, 26, 28, 30],
        "coverage_claim": "exact record-level dihedral representative equality at every listed order",
        "decision_claim": "independent reconstruction and exact Rayleigh exclusion of every nonoptimizer spectral state at every listed order",
        "checkpoint_claim": "production checkpoint chains bind the original ordered decisions; they are separate from the independent decision rerun",
        "files": files,
        "trust_boundary": [
            "both routes implement the proved Q/holonomy quotient specification",
            "floating eigensolvers propose integer vectors but do not decide inequalities",
            "full per-state vectors are regenerated rather than archived individually",
        ],
    }


def main() -> None:
    payload = build()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    temporary = OUTPUT.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    temporary.replace(OUTPUT)
    print("TARGET_A_COMPUTATIONAL_EVIDENCE_MANIFEST_BUILT")


if __name__ == "__main__":
    main()

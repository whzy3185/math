"""Fail-closed audit entry point for the Target A proof-closure package."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader


REPO = Path(__file__).resolve().parents[2]
CLOSURE = REPO / "research" / "proof_closure"
SUVAGIYA = (
    REPO
    / "research"
    / "related_work"
    / "papers"
    / "core"
    / "2026_Suvagiya_SignedCirculants_PREPRINT.pdf"
)

REQUIRED_DOCUMENTS = (
    "BASELINE_FREEZE.md",
    "SUVAGIYA_CLAIM_SOURCE_MAP.md",
    "PROOF_PROVENANCE_MAP.md",
    "PROOF_OBLIGATION_MATRIX.md",
    "TWISTED_SIGNING_SPECTRUM.md",
    "PHASE_SLIP_AND_G6_CLOSURE.md",
    "ANALYTIC_THRESHOLD_LEDGER.md",
    "FINITE_CERTIFICATE_SEMANTICS.md",
    "ORDER_COVERAGE_LEDGER.md",
    "FINAL_MATHEMATICAL_PROOF_STATUS.md",
    "STRUCTURE_REFERENCE_AUDIT.md",
    "THEOREM_DEPENDENCY_DAG.md",
    "MANUSCRIPT_ARCHITECTURE_PLAN.md",
    "CITATION_PLACEMENT_PLAN.md",
    "SUPPLEMENT_BOUNDARY_PLAN.md",
    "ANALYTIC_PROOF_PROGRAM.md",
    "EQUALITY_ANALYTIC_SEARCH.md",
    "FINITE_TAIL_ANALYTIC_SEARCH.md",
    "G6_ANALYTIC_REDUCTION.md",
    "FINAL_THEOREM_PROOF_MAP.md",
    "ANALYTIC_PROOF_RED_TEAM.md",
    "LEAN_THEOREM_MAP.md",
    "LEAN_BUILD_STATUS.md",
    "UNIFORM_RESIDUE_CAP_PROGRAM.md",
    "PERIODIC_COUNTEREXAMPLE_COVERAGE.md",
    "R2_SCHUR_RICCATI_REDUCTION.md",
)

EXACT_VERIFIERS = (
    "research/scripts/verify_target_a_task50_interface.py",
    "research/scripts/verify_target_a_task51.py",
    "research/scripts/verify_target_a_task53_a2.py",
    "research/scripts/verify_target_a_task53_a3.py",
    "research/scripts/verify_target_a_task55_exact_2r.py",
    "research/scripts/verify_target_a_task55_single_gap.py",
    "research/scripts/verify_target_a_task56_single_gap.py",
    "research/scripts/verify_target_a_task57_uniform_single_gap.py",
    "research/scripts/verify_target_a_minimality_certificate.py",
    "research/scripts/verify_target_a_n32_certificate.py",
    "research/scripts/verify_target_a_task55_small_order_exact.py",
    "research/scripts/verify_target_a_task55_orders_34_46.py",
    "research/scripts/verify_target_a_task54_threshold.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def verify(full: bool = False) -> dict[str, int]:
    for name in REQUIRED_DOCUMENTS:
        require((CLOSURE / name).is_file(), f"missing closure document: {name}")

    source_map = (CLOSURE / "SUVAGIYA_CLAIM_SOURCE_MAP.md").read_text(
        encoding="utf-8"
    )
    for phrase in (
        "Conjecture 3",
        "{8,10,12,14,16,18}",
        "`32`",
        "every even `n>=48`",
    ):
        require(phrase in source_map, f"Suvagiya source map omits: {phrase}")

    source_text = "\n".join(page.extract_text() or "" for page in PdfReader(SUVAGIYA).pages)
    require("Conjecture 3" in source_text, "source PDF lacks Conjecture 3")
    require("{8,10,12,14,16,18}" in source_text.replace(" ", ""),
            "source PDF check-range mismatch")

    matrix = (CLOSURE / "PROOF_OBLIGATION_MATRIX.md").read_text(encoding="utf-8")
    require("| CLASS |" in matrix, "classification row missing")
    require("CLOSED_EXACT_COMPUTER_ASSISTED" in matrix, "closed status absent")
    require("B0 -> B2" in matrix and "| OPEN |" in matrix,
            "open interface boundary omitted")

    coverage = (CLOSURE / "ORDER_COVERAGE_LEDGER.md").read_text(encoding="utf-8")
    for phrase in ("8,10,12,14,16,18,20,22,24,26,28,30", "`32`", "`40`", "48<=n<240", "n>=240"):
        require(phrase in coverage, f"coverage gap in ledger: {phrase}")

    dag = (CLOSURE / "THEOREM_DEPENDENCY_DAG.md").read_text(encoding="utf-8")
    require("complete classification theorem" in dag, "classification DAG sink absent")
    require("This graph is acyclic." in dag, "DAG cycle audit absent")

    architecture = (CLOSURE / "MANUSCRIPT_ARCHITECTURE_PLAN.md").read_text(
        encoding="utf-8"
    )
    require("does not modify any manuscript source" in architecture,
            "architecture plan crosses the manuscript freeze")
    require("Exact finite failures and universal optimality" in architecture,
            "finite proof section lacks a proof role")

    analytic = (CLOSURE / "ANALYTIC_PROOF_PROGRAM.md").read_text(encoding="utf-8")
    require("T10 failures 32/40" in analytic and "ANALYTIC_PROVED" in analytic,
            "period-eight analytic replacement is absent")
    finite_tail = (CLOSURE / "FINITE_TAIL_ANALYTIC_SEARCH.md").read_text(
        encoding="utf-8"
    )
    require("remaining finite rows are" in finite_tail and "45" in finite_tail,
            "finite-tail compression is absent")
    equality = (CLOSURE / "EQUALITY_ANALYTIC_SEARCH.md").read_text(
        encoding="utf-8"
    )
    require("not yet an analytic proof" in equality,
            "finite-language boundary is overstated")
    g6 = (CLOSURE / "G6_ANALYTIC_REDUCTION.md").read_text(encoding="utf-8")
    require("does not imply" in g6, "G6 physical-branch boundary is absent")
    residue_caps = (CLOSURE / "UNIFORM_RESIDUE_CAP_PROGRAM.md").read_text(
        encoding="utf-8"
    )
    require("T2 = 198/25" in residue_caps and "Riccati" in residue_caps,
            "uniform residue-cap reduction is absent")
    periodic = (CLOSURE / "PERIODIC_COUNTEREXAMPLE_COVERAGE.md").read_text(
        encoding="utf-8"
    )
    require(
        all(f"| {period} |" in periodic for period in (10, 12, 14, 18, 22)),
        "auxiliary periodic-family record is absent",
    )
    require("stop rule" in periodic and "25" in periodic,
            "periodic-family boundary or accounting is absent")
    r2_schur = (CLOSURE / "R2_SCHUR_RICCATI_REDUCTION.md").read_text(
        encoding="utf-8"
    )
    require("12 x 12" in r2_schur and "8 x 8" in r2_schur,
            "residue-two fixed-width Schur reduction is absent")

    if full:
        for verifier in EXACT_VERIFIERS:
            subprocess.run([sys.executable, verifier], cwd=REPO, check=True)

    return {"documents": len(REQUIRED_DOCUMENTS), "verifiers": len(EXACT_VERIFIERS) if full else 0}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--full", action="store_true")
    args = parser.parse_args()
    report = verify(full=args.full)
    print("TARGET_A_PROOF_CLOSURE_PASS", report)

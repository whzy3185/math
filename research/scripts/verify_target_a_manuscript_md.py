"""Validate the Target A Markdown manuscript gate."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANUSCRIPT = RESEARCH_ROOT / "paper" / "manuscript_md" / "TARGET_A_MANUSCRIPT_V2.md"
ARTIFACT_COMMIT = "c81be34a3b12a7ac47adbb4499c475df7bf4fc04"
REQUIRED_HEADINGS = [
    "# Counterexamples and Flux-Phase Structure for Signed Circulant Graphs",
    "# 1. Introduction",
    "# 2. Signed Circulants and Flux Coordinates",
    "# 3. The Smallest Counterexample",
    "# 4. Periodic Construction and Floquet Reduction",
    "# 5. The Exact Period-Eight Spectral Edge",
    "# 6. The Eight-Barrier and Structural Optimum",
    "# 7. General-Period Closed-Walk Obstructions",
    "# 8. The Low-Period Spectral Frontier",
    "# 9. Computer-Assisted Verification",
    "# 10. Discussion and Open Problems",
    "# Appendix A. Quotient and Orbit Completeness",
    "# Appendix B. Exact Classification and Residual Certificates",
    "# Appendix C. Computational Protocol",
    "# References",
]


class ManuscriptVerificationError(RuntimeError):
    pass


def _check(condition: bool, message: str) -> None:
    if not condition:
        raise ManuscriptVerificationError(message)


def verify_manuscript(text: str) -> None:
    _check(all(heading in text for heading in REQUIRED_HEADINGS), "VERIFY_MANUSCRIPT_HEADING_FAIL")
    positions = [text.index(heading) for heading in REQUIRED_HEADINGS]
    _check(positions == sorted(positions), "VERIFY_MANUSCRIPT_HEADING_ORDER_FAIL")
    for letter in "ABCDEF":
        _check(f"**Theorem {letter} (" in text, f"VERIFY_THEOREM_{letter}_FAIL")

    _check("R(Q)=sup_(|z|=1) rho(H_tau(z))^2" in text, "VERIFY_R_SQUARED_DEFINITION_FAIL")
    _check(text.count("eta=4+sqrt(10+2sqrt(5))") >= 4, "VERIFY_ETA_CONSISTENCY_FAIL")
    _check("F_k(Q)>0  ==>  R(Q)>8" in text, "VERIFY_MOMENT_DIRECTION_FAIL")
    _check("does not prove `R(Q)<=8`" in text, "VERIFY_MOMENT_WARNING_FAIL")
    _check("r>4" in text and "positive square-root branch" in text, "VERIFY_RADICAL_BRANCH_FAIL")
    _check("finite computer-assisted" in text.lower(), "VERIFY_COMPUTER_ASSISTED_DISCLOSURE_FAIL")
    _check("2,147,483,648" in text and "17,929,600" in text, "VERIFY_QUOTIENT_TRUST_BOUNDARY_FAIL")
    _check("20 August 2026" in text and re.search(r"bounded\s+search statement", text), "VERIFY_CURRENT_STATUS_CITATION_FAIL")
    _check(ARTIFACT_COMMIT in text, "VERIFY_IMMUTABLE_ARTIFACT_CITATION_FAIL")

    lower = text.lower()
    for forbidden in ("todo", "proof omitted", "left to the author", "author must add", "world-first"):
        _check(forbidden not in lower, f"VERIFY_FORBIDDEN_TEXT:{forbidden}")
    _check(not re.search(r"F_?k\s*(?:<=|≤)\s*0\s*(?:==>|=>|implies)\s*R\(Q\)\s*(?:<=|≤)\s*8", text), "VERIFY_REVERSE_MOMENT_FAIL")

    body = text.split("# Appendix A.", 1)[0]
    _check(not re.search(r"\bTask\s+[0-9]", body), "VERIFY_BODY_TASK_LANGUAGE_FAIL")
    body_hashes = set(re.findall(r"\b[0-9a-f]{40}\b", body))
    _check(body_hashes == {ARTIFACT_COMMIT}, "VERIFY_BODY_COMMIT_HASH_FAIL")
    _check("all-period theorem" not in lower or "not an all-period theorem" in lower, "VERIFY_ALL_PERIOD_SCOPE_FAIL")
    _check("all-signings global optimality" not in lower, "VERIFY_ALL_SIGNINGS_OVERCLAIM_FAIL")
    print("TARGET_A_MANUSCRIPT_STRUCTURE_PASS")
    print("TARGET_A_MANUSCRIPT_THEOREMS_PASS")
    print("TARGET_A_MANUSCRIPT_NOTATION_PASS")
    print("TARGET_A_MANUSCRIPT_SCOPE_PASS")
    print("TARGET_A_MANUSCRIPT_COMPUTATION_BOUNDARY_PASS")
    print("TARGET_A_MANUSCRIPT_MD_GATE_PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manuscript", type=Path, default=DEFAULT_MANUSCRIPT)
    args = parser.parse_args()
    try:
        verify_manuscript(args.manuscript.read_text(encoding="utf-8"))
    except Exception as error:
        print(f"Target A manuscript verification failed: {error}", file=sys.stderr)
        print("TARGET_A_MANUSCRIPT_MD_GATE_FAIL")
        raise SystemExit(1)


if __name__ == "__main__":
    main()

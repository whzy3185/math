"""Fail-closed verifier for the Target A Task 52 artifact package."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


RESEARCH = Path(__file__).resolve().parents[1]
ROOT = RESEARCH.parent
CERT = RESEARCH / "proofs" / "task52" / "certificates"
EXP = RESEARCH / "experiments" / "task52"
PROOF = RESEARCH / "proofs" / "task52"
ENTRY = "ac4c69b796c9dc14d1307a092d1e0faa093081f2"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    algebra = load(CERT / "plus_minus_two_algebra.json")
    sectors = load(CERT / "translation_charge.json")
    comparisons = load(CERT / "single_gap_exact_comparisons.json")
    recurrence = load(CERT / "charge_recurrence.json")
    primitive = load(EXP / "primitive_interface_search.json")
    fixed = load(EXP / "fixed_r_full_spectrum_scan.json")
    high_precision = load(EXP / "fixed_r_high_precision_evans.json")
    grammar = load(EXP / "c6_low_energy_grammar.json")
    p24 = load(EXP / "p24_c6_audit.json")
    synthesis = (PROOF / "TARGET_A_TASK52_SYNTHESIS.md").read_text(encoding="utf-8")
    checks = {
        "entry_is_ancestor": subprocess.run(["git", "merge-base", "--is-ancestor", ENTRY, "HEAD"], cwd=ROOT).returncode == 0,
        "manuscript_freeze": subprocess.run([
            "git", "diff", "--quiet", ENTRY, "--",
            "research/paper/manuscript_tex_pub", "research/paper/manuscript_tex_pub_zh",
        ], cwd=ROOT).returncode == 0,
        "translation_charge": sectors["status"] == "TRANSLATION_CHARGE_PROVED_CORRECTED_RULE" and sectors["composition_checks"]["all_pass"],
        "candidate_rule_falsified": sectors["candidate_rule_q_over_2_mod_4"] == "FALSIFIED",
        "plus_minus_two": algebra["status"] == "PLUS_MINUS_TWO_COMMON_POLYNOMIAL_PROVED" and all(algebra["checks"].values()),
        "single_gap_comparisons": comparisons["status"] == "COMPETITIVE_SINGLE_GAP_COMPARISONS_CERTIFIED" and all(comparisons["proved_comparisons"].values()),
        "gap_recurrence": recurrence["status"] == "GAP_PLUS_EIGHT_EXACT_EXTERIOR_RECURRENCE_PROVED" and all(all(row["checks"].values()) for row in recurrence["records"]),
        "primitive_boundary": not primitive["completeness_achieved"] and not primitive["non_G6_candidates_below_c6"],
        "fixed_r_numerical": fixed["large_separation_all_have_r_cluster_levels"] and fixed["large_separation_hidden_branch_cases"] == 0,
        "high_precision_ladders": all([row["digits"] for row in case["precision_ladder"]] == [80, 120, 160] for case in high_precision["cases"]),
        "grammar_boundary": grammar["classification"] == "WEAK" and grammar["primitive_cycles_through_period_16"] > 1,
        "period10": p24["period10_exact"]["status"] == "PERIOD10_BAND_EDGE_GT_C6_PROVED" and all(p24["period10_exact"]["checks"].values()),
        "no_limsup_overclaim": "no LIMSUP theorem claimed" in synthesis,
        "final_status": "TARGET_A_TASK52_PARTIAL_PROGRESS" in synthesis,
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    output = {"status": "TARGET_A_TASK52_VERIFY_PASS", "checks": checks}
    target = RESEARCH / "reproducibility" / "task52"
    target.mkdir(parents=True, exist_ok=True)
    (target / "verification.json").write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(output["status"])


if __name__ == "__main__":
    main()

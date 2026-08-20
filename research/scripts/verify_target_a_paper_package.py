"""Validate Target A's pre-manuscript theorem package."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = RESEARCH_ROOT.parent
PAPER_ROOT = RESEARCH_ROOT / "paper"
DEFAULT_INVENTORY = PAPER_ROOT / "target_a_claim_inventory.json"
DEFAULT_GRAPH = PAPER_ROOT / "target_a_theorem_dependency_graph.json"
DEFAULT_GATE = PAPER_ROOT / "target_a_manuscript_gate.json"
DEFAULT_ROUND2 = RESEARCH_ROOT / "audit" / "target_a_reviewer_zero_round2_findings.json"
DEFAULT_ARCHITECTURE = PAPER_ROOT / "TARGET_A_MANUSCRIPT_ARCHITECTURE.md"
EXPECTED_IDS = [f"C{index}" for index in range(1, 26)]
EXPECTED_THEOREMS = [f"THEOREM_{letter}" for letter in "ABCDEF"]
REQUIRED_FIELDS = {
    "id", "title", "exact_statement", "status", "scope", "proof_type",
    "dependencies", "main_proof_artifact", "machine_certificate",
    "independent_checker", "test", "sha256", "novelty_audit_item",
    "manuscript_role",
}


class PaperPackageVerificationError(RuntimeError):
    pass


def _check(condition: bool, message: str) -> None:
    if not condition:
        raise PaperPackageVerificationError(message)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _assert_acyclic(claims: dict[str, dict[str, Any]]) -> None:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(claim_id: str) -> None:
        _check(claim_id not in visiting, f"VERIFY_DEPENDENCY_CYCLE:{claim_id}")
        if claim_id in visited:
            return
        visiting.add(claim_id)
        for dependency in claims[claim_id]["dependencies"]:
            visit(dependency)
        visiting.remove(claim_id)
        visited.add(claim_id)

    for claim_id in claims:
        visit(claim_id)


def verify_claim_inventory(inventory: dict[str, Any]) -> None:
    _check(inventory.get("schema_version") == "1.0.0", "VERIFY_INVENTORY_SCHEMA_FAIL")
    _check(inventory.get("status") == "TARGET_A_CLAIM_INVENTORY_COMPLETE", "VERIFY_INVENTORY_STATUS_FAIL")
    _check(inventory.get("exploration_status") == "EXPLORATORY_EXTENSION_PAUSED", "VERIFY_EXPLORATION_FREEZE_FAIL")
    _check(inventory.get("frozen_head") == "dfb9c9846fa95545fdb1a5153ceabe1767c9ee0a", "VERIFY_FROZEN_HEAD_FAIL")
    _check(inventory.get("frozen_tree") == "7a15c4498b1ac9f52f13c17dff5355fa30c4db7c", "VERIFY_FROZEN_TREE_FAIL")
    claims_list = inventory.get("claims", [])
    _check([row.get("id") for row in claims_list] == EXPECTED_IDS, "VERIFY_CLAIM_ID_SEQUENCE_FAIL")
    claims = {row["id"]: row for row in claims_list}
    allowed_types = set(inventory.get("allowed_proof_types", []))
    allowed_roles = set(inventory.get("allowed_manuscript_roles", []))
    _check(allowed_types == {"PURE_ANALYTIC", "FINITE_COMPUTER_ASSISTED", "HYBRID", "INDEPENDENTLY_REPRODUCED"}, "VERIFY_PROOF_TYPES_FAIL")
    _check(allowed_roles == {"MAIN_THEOREM", "THEOREM", "LEMMA", "COROLLARY", "SUPPLEMENT_ONLY"}, "VERIFY_ROLES_FAIL")

    novelty = _load(RESEARCH_ROOT / "literature" / "target_a_novelty_priority_audit.json")
    novelty_ids = {row["id"] for row in novelty["claims"]}
    for claim_id, row in claims.items():
        _check(set(row) == REQUIRED_FIELDS, f"VERIFY_CLAIM_FIELDS_FAIL:{claim_id}")
        _check(row["proof_type"] in allowed_types, f"VERIFY_PROOF_TYPE_FAIL:{claim_id}")
        _check(row["manuscript_role"] in allowed_roles, f"VERIFY_ROLE_FAIL:{claim_id}")
        _check(row["novelty_audit_item"] in novelty_ids, f"VERIFY_NOVELTY_LINK_FAIL:{claim_id}")
        _check(set(row["dependencies"]) <= set(claims), f"VERIFY_UNKNOWN_DEPENDENCY:{claim_id}")
        paths = {
            "main": row["main_proof_artifact"],
            "certificate": row["machine_certificate"],
            "checker": row["independent_checker"],
            "test": row["test"],
        }
        _check(set(row["sha256"]) == set(paths), f"VERIFY_SHA_KEYS_FAIL:{claim_id}")
        for key, relative in paths.items():
            path = REPO_ROOT / relative
            _check(path.is_file(), f"VERIFY_ARTIFACT_MISSING:{claim_id}:{relative}")
            _check(_sha256(path) == row["sha256"][key], f"VERIFY_ARTIFACT_SHA_FAIL:{claim_id}:{key}")
        joined = (row["exact_statement"] + " " + row["scope"]).lower()
        _check("all-period optimum" not in joined and "all signings optimum" not in joined, f"VERIFY_SCOPE_OVERCLAIM:{claim_id}")
    _assert_acyclic(claims)
    _check(inventory.get("scope_exclusions") == ["ALL_PERIOD_OPTIMUM", "ALL_SIGNINGS_OPTIMUM", "FINITE_N_GLOBAL_OPTIMUM_FOR_ALL_N"], "VERIFY_SCOPE_EXCLUSIONS_FAIL")
    deferred = inventory.get("deferred_claims", [])
    _check(len(deferred) == 1 and deferred[0].get("title") == "Period-10 counterexample family", "VERIFY_DEFERRED_CLAIM_FAIL")
    _check(deferred[0].get("status") == "DEFERRED_FROM_MANUSCRIPT", "VERIFY_DEFERRED_STATUS_FAIL")


def verify_dependency_graph(graph: dict[str, Any], inventory: dict[str, Any]) -> None:
    _check(graph.get("schema_version") == "1.0.0", "VERIFY_GRAPH_SCHEMA_FAIL")
    _check(graph.get("status") == "TARGET_A_THEOREM_DEPENDENCY_GRAPH_COMPLETE", "VERIFY_GRAPH_STATUS_FAIL")
    rows = graph.get("theorems", [])
    _check([row.get("id") for row in rows] == EXPECTED_THEOREMS, "VERIFY_THEOREM_ID_SEQUENCE_FAIL")
    claim_ids = {row["id"] for row in inventory["claims"]}
    for theorem in rows:
        deps = theorem.get("dependencies", [])
        _check(deps and set(deps) <= claim_ids, f"VERIFY_THEOREM_DEPENDENCIES_FAIL:{theorem['id']}")
        _check(set(theorem.get("deletion_tests", {})) == set(deps), f"VERIFY_DELETION_TEST_COVERAGE_FAIL:{theorem['id']}")
        _check(all(theorem["deletion_tests"].values()), f"VERIFY_EMPTY_DELETION_EFFECT_FAIL:{theorem['id']}")
    expected_edges = {
        (row["id"], dependency)
        for row in inventory["claims"]
        for dependency in row["dependencies"]
    }
    actual_edges = {tuple(edge) for edge in graph.get("claim_edges", [])}
    _check(actual_edges == expected_edges, "VERIFY_CLAIM_EDGE_SET_FAIL")
    _check(graph.get("independent_verification_is_logical_dependency") is False, "VERIFY_INDEPENDENCE_BOUNDARY_FAIL")
    classes = graph.get("edge_classes", {})
    _check(classes.get("mathematical_implication") == "claim_edges", "VERIFY_EDGE_CLASS_FAIL")
    _check(classes.get("primary_proof_dependencies") == "theorems[].dependencies", "VERIFY_PRIMARY_DEPENDENCY_CLASS_FAIL")
    _check(len(classes.get("optional_cross_checks", [])) == 2, "VERIFY_OPTIONAL_CROSSCHECK_CLASS_FAIL")


def verify_graph_markdown(graph: dict[str, Any], markdown: str) -> None:
    rendered: dict[str, list[str]] = {}
    for line in markdown.splitlines():
        if not line.startswith("| THEOREM_"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        _check(len(cells) == 3, f"VERIFY_GRAPH_MARKDOWN_COLUMNS_FAIL:{line}")
        rendered[cells[0]] = [item.strip() for item in cells[2].split(",")]
    expected = {row["id"]: row["dependencies"] for row in graph["theorems"]}
    _check(rendered == expected, "VERIFY_GRAPH_MARKDOWN_SEMANTIC_MISMATCH")


def verify_initial_files() -> None:
    inventory = _load(DEFAULT_INVENTORY)
    graph = _load(DEFAULT_GRAPH)
    verify_claim_inventory(inventory)
    verify_dependency_graph(graph, inventory)
    inventory_md = (PAPER_ROOT / "TARGET_A_CLAIM_INVENTORY.md").read_text(encoding="utf-8")
    graph_md = (PAPER_ROOT / "TARGET_A_THEOREM_DEPENDENCY_GRAPH.md").read_text(encoding="utf-8")
    classification = (PAPER_ROOT / "TARGET_A_PROOF_CLASSIFICATION.md").read_text(encoding="utf-8")
    _check("squared" in inventory_md and "necessary, never sufficient" in inventory_md, "VERIFY_INVENTORY_SCOPE_TEXT_FAIL")
    _check("Deletion Audit" in graph_md, "VERIFY_GRAPH_DELETION_TEXT_FAIL")
    verify_graph_markdown(graph, graph_md)
    _check("2,147,483,648" in classification and "17,929,600" in classification, "VERIFY_TRUST_BOUNDARY_TEXT_FAIL")
    _check("classified **HYBRID**, not pure analytic" in classification, "VERIFY_HYBRID_MOMENT_CLASSIFICATION_FAIL")
    print("TARGET_A_CLAIM_INVENTORY_PASS")
    print("TARGET_A_THEOREM_DEPENDENCY_GRAPH_PASS")
    print("TARGET_A_PROOF_CLASSIFICATION_PASS")


def verify_notation_and_compression() -> None:
    notation = (PAPER_ROOT / "TARGET_A_NOTATION.md").read_text(encoding="utf-8")
    required_notation = (
        "G_n=C_n(1,2)", "sigma:E(G_n)->{+-1}", "A_sigma", "tau_i",
        "Q_i=tau_i tau_{i+1}", "D(Q)", "H_Q(z)", "R(Q)", "eta",
        "rho_*", "M_k(Q)", "F_k(Q)", "alpha", "L", "p",
    )
    for token in required_notation:
        _check(token in notation, f"VERIFY_NOTATION_TOKEN_FAIL:{token}")
    _check("R(Q)` | **Always**" in notation, "VERIFY_R_SQUARED_DEFINITION_FAIL")
    _check("F_k(Q)>0  =>  R(Q)>8" in notation, "VERIFY_MOMENT_DIRECTION_FAIL")
    _check("Neither `F_k<=0 => R(Q)<=8`" in notation, "VERIFY_MOMENT_WARNING_FAIL")
    _check("Finite statements must write `rho(A_sigma)^2`" in notation, "VERIFY_FINITE_INFINITE_BOUNDARY_FAIL")

    compression = (PAPER_ROOT / "TARGET_A_PROOF_COMPRESSION.md").read_text(encoding="utf-8")
    for theorem in EXPECTED_THEOREMS:
        label = theorem.replace("THEOREM_", "Theorem ")
        _check(label in compression, f"VERIFY_COMPRESSION_THEOREM_FAIL:{theorem}")
    for phrase in ("does not list 2624 witnesses", "Fresh `n=24,26,28,30` regeneration", "No theorem asserts all-period optimality"):
        _check(phrase in compression, f"VERIFY_COMPRESSION_BOUNDARY_FAIL:{phrase}")
    print("TARGET_A_NOTATION_PASS")
    print("TARGET_A_PROOF_COMPRESSION_PASS")


def verify_claim_evidence_and_reproducibility() -> None:
    matrix = (PAPER_ROOT / "TARGET_A_CLAIM_EVIDENCE_MATRIX.md").read_text(encoding="utf-8")
    matrix_ids = []
    for line in matrix.splitlines():
        if line.startswith("| C") and line.split("|", 2)[1].strip() in EXPECTED_IDS:
            matrix_ids.append(line.split("|", 2)[1].strip())
            _check(line.count("|") == 9, f"VERIFY_MATRIX_COLUMN_COUNT_FAIL:{matrix_ids[-1]}")
    _check(matrix_ids == EXPECTED_IDS, "VERIFY_MATRIX_CLAIM_COVERAGE_FAIL")

    reproducibility = (PAPER_ROOT / "TARGET_A_REPRODUCIBILITY_STATEMENT.md").read_text(encoding="utf-8")
    for token in (
        "353,812", "1,299,064", "4,810,472", "17,929,600", "1,262",
        "2,147,483,648", "mismatch count is zero",
        "FULL_FINITE_SEARCH_REGENERATION_PASS", "FULL_CERTIFICATE_REPLAY_PASS",
        "FULL_SLOW_REGRESSION_PASS", "FULL_CHECKPOINT_INTEGRITY_REPLAY_PASS",
    ):
        _check(token in reproducibility, f"VERIFY_REPRODUCIBILITY_TOKEN_FAIL:{token}")
    _check("does not mean that 2.147 billion" in reproducibility and "independent pytest cases" in reproducibility, "VERIFY_REPRODUCIBILITY_TRUST_BOUNDARY_FAIL")
    _check("original production checkpoint chunks are committed" in reproducibility, "VERIFY_COMMITTED_CHUNK_WORDING_FAIL")

    trust = (PAPER_ROOT / "TARGET_A_FINITE_COMPUTATION_TRUST_MODEL.md").read_text(encoding="utf-8")
    trust_lower = trust.lower()
    for token in ("executable", "exhaustive", "computer-assisted proof", "integrity replay", "not an independent", "regeneration-based"):
        _check(token in trust_lower, f"VERIFY_TRUST_MODEL_TOKEN_FAIL:{token}")

    n24 = _load(RESEARCH_ROOT / "audit" / "target_a_n24_dual_generator_audit.json")
    _check(n24.get("status") == "TARGET_A_N24_DUAL_GENERATOR_PASS", "VERIFY_N24_DUAL_STATUS_FAIL")
    _check(n24.get("reference_sha256") == n24.get("production_sha256"), "VERIFY_N24_DUAL_DIGEST_FAIL")
    _check(all(n24.get("checks", {}).values()), "VERIFY_N24_DUAL_CHECKS_FAIL")

    novelty = (PAPER_ROOT / "TARGET_A_PRE_SUBMISSION_NOVELTY_REFRESH_PLAN.md").read_text(encoding="utf-8")
    safe = "As of 16 August 2026, no direct public prior was found in the sources and"
    _check(safe in novelty, "VERIFY_NOVELTY_SAFE_SENTENCE_FAIL")
    _check("Do not repeat the entire 135-query" in novelty, "VERIFY_NOVELTY_REFRESH_SCOPE_FAIL")
    _check("must not use “world-first”" in novelty, "VERIFY_NOVELTY_PRIORITY_BOUNDARY_FAIL")
    print("TARGET_A_CLAIM_EVIDENCE_MATRIX_PASS")
    print("TARGET_A_REPRODUCIBILITY_STATEMENT_PASS")
    print("TARGET_A_NOVELTY_REFRESH_PLAN_PASS")
    print("TARGET_A_FINITE_COMPUTATION_TRUST_MODEL_PASS")
    print("TARGET_A_PAPER_PACKAGE_LINT_PASS")


def verify_reviewer_zero_round2_and_gate(
    round2: dict[str, Any] | None = None,
    gate: dict[str, Any] | None = None,
    architecture: str | None = None,
) -> None:
    round2 = _load(DEFAULT_ROUND2) if round2 is None else round2
    gate = _load(DEFAULT_GATE) if gate is None else gate
    architecture = DEFAULT_ARCHITECTURE.read_text(encoding="utf-8") if architecture is None else architecture

    expected_counts = {"CRITICAL": 0, "MAJOR": 0, "MODERATE": 5, "MINOR": 1}
    _check(round2.get("schema_version") == "1.0.0", "VERIFY_RZ2_SCHEMA_FAIL")
    _check(round2.get("reviewed_head") == "b9e00bd34222d40e9ac954d3d5c4817644650be0", "VERIFY_RZ2_HEAD_FAIL")
    _check(round2.get("counts") == expected_counts, "VERIFY_RZ2_COUNTS_FAIL")
    calculated_gate = round2["counts"]["CRITICAL"] == 0 and round2["counts"]["MAJOR"] == 0
    _check(round2.get("gate_pass") is calculated_gate and calculated_gate, "VERIFY_RZ2_GATE_FAIL")
    findings = round2.get("findings", [])
    _check([row.get("id") for row in findings] == [f"RZ2-{index:03d}" for index in range(1, 7)], "VERIFY_RZ2_FINDING_IDS_FAIL")
    _check(all(row.get("severity") in expected_counts for row in findings), "VERIFY_RZ2_SEVERITY_FAIL")
    _check(all(row.get("disposition") in {"OPEN", "ACCEPTED_RISK"} for row in findings), "VERIFY_RZ2_DISPOSITION_FAIL")

    _check(gate.get("schema_version") == "1.0.0", "VERIFY_GATE_SCHEMA_FAIL")
    _check(gate.get("status") == "TARGET_A_MANUSCRIPT_READY", "VERIFY_GATE_STATUS_FAIL")
    _check(gate.get("drafting_gate_pass") is True, "VERIFY_DRAFTING_GATE_FAIL")
    _check(gate.get("submission_status") == "MODERATE_REPAIRS_REMAIN", "VERIFY_SUBMISSION_BOUNDARY_FAIL")
    reviewed = gate.get("reviewed_package", {})
    _check(reviewed.get("head") == round2["reviewed_head"], "VERIFY_GATE_REVIEWED_HEAD_FAIL")
    _check(reviewed.get("tree") == "3873fb1c948a85443a2b55a642dbf1dba9359bdb", "VERIFY_GATE_REVIEWED_TREE_FAIL")
    _check(reviewed.get("claim_bearing_package_frozen") is True, "VERIFY_CLAIM_PACKAGE_FREEZE_FAIL")
    _check(reviewed.get("round2_report_sha256") == _sha256(RESEARCH_ROOT / "audit" / "TARGET_A_REVIEWER_ZERO_ROUND2.md"), "VERIFY_RZ2_REPORT_SHA_FAIL")
    _check(reviewed.get("round2_json_sha256") == _sha256(DEFAULT_ROUND2), "VERIFY_RZ2_JSON_SHA_FAIL")
    _check(gate.get("reviewer_zero", {}).get("round2", {}).get("counts") == expected_counts, "VERIFY_GATE_RZ2_COUNTS_FAIL")
    _check(gate["reviewer_zero"]["round2"].get("gate_pass") is True, "VERIFY_GATE_RZ2_PASS_FAIL")
    open_ids = {row["id"] for row in findings if row["disposition"] == "OPEN"}
    risk_ids = {row["id"] for row in findings if row["disposition"] == "ACCEPTED_RISK"}
    _check(set(gate["reviewer_zero"]["round2"].get("open_nonblocking", [])) == open_ids, "VERIFY_GATE_OPEN_FINDINGS_FAIL")
    _check(set(gate["reviewer_zero"]["round2"].get("accepted_risks", [])) == risk_ids, "VERIFY_GATE_ACCEPTED_RISKS_FAIL")
    _check(all(gate.get("conditions", {}).values()), "VERIFY_GATE_CONDITION_FAIL")
    _check(gate.get("auto_start_next_task") is False, "VERIFY_TASK44_AUTOSTART_FAIL")

    expected_sections = (
        "## 1. Introduction",
        "## 2. Signed Circulants and Flux Coordinates",
        "## 3. The Smallest Counterexample",
        "## 4. Periodic Construction and Floquet Reduction",
        "## 5. Exact Period-8 Spectral Edge",
        "## 6. The Eight-Barrier and Structural Optimum",
        "## 7. General-Period Closed-Walk Obstructions",
        "## 8. The Low-Period Spectral Frontier",
        "## 9. Computer-Assisted Verification",
        "## 10. Discussion and Open Problems",
        "## Appendices",
        "## Supplement",
        "## Submission Preflight",
    )
    _check(all(section in architecture for section in expected_sections), "VERIFY_ARCHITECTURE_SECTION_FAIL")
    _check(all(f"**O{index}.**" in architecture for index in range(1, 6)), "VERIFY_OPEN_PROBLEM_COVERAGE_FAIL")
    _check("not manuscript prose" in architecture and "Task 44" in architecture, "VERIFY_ARCHITECTURE_BOUNDARY_FAIL")
    _check("world-first" not in architecture.lower(), "VERIFY_ARCHITECTURE_NOVELTY_OVERCLAIM_FAIL")
    print("TARGET_A_REVIEWER_ZERO_ROUND2_PASS")
    print("TARGET_A_MANUSCRIPT_ARCHITECTURE_PASS")
    print("TARGET_A_MANUSCRIPT_GATE_PASS")


def main() -> None:
    try:
        verify_initial_files()
        verify_notation_and_compression()
        verify_claim_evidence_and_reproducibility()
        verify_reviewer_zero_round2_and_gate()
    except Exception as error:
        print(f"Target A paper package verification failed: {error}", file=sys.stderr)
        print("TARGET_A_PAPER_PACKAGE_FAIL")
        raise SystemExit(1)


if __name__ == "__main__":
    main()

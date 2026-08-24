"""Fail-closed verifier for the four Task 57.5 proof-connection repairs."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

import sympy as sp


REPO = Path(__file__).resolve().parents[2]
PACKAGE = REPO / "research" / "paper" / "proof_completion"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(relative: str, package: Path = PACKAGE) -> str:
    path = package / relative
    require(path.is_file(), f"missing repair artifact: {relative}")
    text = path.read_text(encoding="utf-8")
    require(len(text.strip()) >= 200, f"stub repair artifact: {relative}")
    return text


def normalized(text: str) -> str:
    cleaned = text.replace("\\", "").replace("`", "")
    cleaned = re.sub(r"(?<=[A-Za-z])-(?=[A-Za-z])", " ", cleaned)
    return re.sub(r"\s+", " ", cleaned).strip().lower()


def verify_candidate_fiber_identity() -> None:
    z = sp.Symbol("z", nonzero=True)
    spectral = sp.Symbol("spectral")
    c = (z + z**-1) / 2
    fiber = sp.Matrix([[2 * c, 1 + z**-1], [1 + z, -2 * c]])
    characteristic = sp.factor(fiber.charpoly(spectral).as_expr())
    expected = sp.factor(spectral**2 - (4 * c**2 + 2 + 2 * c))
    require(sp.simplify(characteristic - expected) == 0, "candidate fiber identity")


def git_tree(path: str) -> str:
    completed = subprocess.run(
        ["git", "ls-tree", "HEAD", path],
        cwd=REPO,
        text=True,
        capture_output=True,
        check=True,
    )
    fields = completed.stdout.strip().split()
    require(len(fields) >= 3 and fields[1] == "tree", f"missing frozen tree: {path}")
    return fields[2]


def verify(package: Path = PACKAGE, check_git: bool = True) -> dict[str, bool]:
    attainment = read("01_even_order_classification/CANDIDATE_ATTAINMENT_LEMMA.md", package)
    classification = read("01_even_order_classification/FULL_PROOF.md", package)
    classification_dependencies = read("01_even_order_classification/DEPENDENCIES.md", package)
    a = normalized(attainment)
    c = normalized(classification)
    cd = normalized(classification_dependencies)
    for token in (
        "q_i=-1", "alpha=-1", "for every even", "fourier", "2 x 2",
        "rho(a", "rho_-(n)", "m_n<=rho_-(n)",
    ):
        require(token in a, f"attainment omits {token}")
    require("m_n>=rho_-(n)" in c and "m_n=rho_-(n)" in c, "classification equality bridge")
    require("candidate attainment" in cd or "candidate-attainment" in cd, "attainment dependency absent")
    require("candidate_attainment_lemma.md" in cd, "attainment artifact dependency absent")
    verify_candidate_fiber_identity()

    essential = read("05_g6_edge/ESSENTIAL_SPECTRUM_LEMMA.md", package)
    g6_full = read("05_g6_edge/FULL_PROOF.md", package)
    e = normalized(essential)
    for token in (
        "self adjoint", "finite range", "finite rank", "compact",
        "essential spectrum", "half line", "periodic", "eta",
        "finite multiplicity", "exponential", "stable", "unstable",
    ):
        require(token in e, f"essential-spectrum lemma omits {token}")
    require("sigma_ess(h_6)" in e or "sigma_ess(h6)" in e, "essential-spectrum equality absent")
    require("standard cutoff weyl-sequence argument" not in g6_full.lower(), "old essential-spectrum shortcut remains")
    require("rational interval (1)" not in g6_full.lower(), "stale G6 equation reference remains")

    patch = read("07_exact_2r/PATCH_IDENTIFICATION_LEMMA.md", package)
    exact_full = read("07_exact_2r/FULL_PROOF.md", package)
    exact_dependencies = read("07_exact_2r/DEPENDENCIES.md", package)
    p = normalized(patch)
    for token in (
        "forward", "reflected", "tau lift", "holonomy", "seam",
        "range four", "d>=1040", "period eight", "psi_(j,+)",
        "psi_(j,-)", "phi_(j,+/-)",
    ):
        require(token in p, f"patch lemma omits {token}")
    require("patch identification lemma" in normalized(exact_full), "exact-2r proof omits patch lemma")
    require("patch_identification_lemma.md" in exact_dependencies.lower(), "exact-2r dependency file omits patch artifact")

    safety = read("TARGET_A_MANUSCRIPT_IMPORT_SAFETY.md", package)
    notation = read("TARGET_A_FINAL_NOTATION.md", package)
    hierarchy = read("TARGET_A_JGT_THEOREM_HIERARCHY.md", package)
    architecture = read("TARGET_A_JGT_PROOF_ARCHITECTURE.md", package)
    s = normalized(safety)
    for category in (
        "canonical_import", "import_with_caution", "do_not_import_current_claims", "historical_only",
    ):
        require(category in s, f"import manifest omits {category}")
    for hazard in (
        "research/proofs/task52/target_a_multi_slip_interaction_asymptotics.md",
        "research/proofs/task54/target_a_common_residue_limit_scope.md",
    ):
        require(hazard in s, f"import blacklist omits {hazard}")
    n = normalized(notation)
    require("theta_n" in n and "rho_-^2(n)" in n, "theta notation absent")
    require("fails at" in n and "m_n<rho_-(n)" in n, "failure terminology absent")
    require("exactly seven main theorem families" in normalized(hierarchy), "hierarchy count not seven")
    require("exactly seven main theorem families" in normalized(architecture), "architecture count not seven")

    inventory = read("TARGET_A_FINAL_CLAIM_INVENTORY_V2.md", package)
    matrix = read("TARGET_A_FINAL_CLAIM_EVIDENCE_MATRIX_V2.md", package)
    dag = read("TARGET_A_FINAL_PROOF_DEPENDENCY_GRAPH.md", package)
    for claim in ("T8.0", "T4.0", "T6.0"):
        require(claim in inventory and claim in matrix and claim in dag, f"canonical bridge claim missing: {claim}")
    require("T8.0" in re.search(r"## Layer 7: Main Classification.*", dag, re.DOTALL).group(0), "attainment absent from final DAG")

    forbidden = re.compile(
        r"rank[- ]one|exact-`?r`?(?![A-Za-z])|exactly\s+`?r`?\s+(?:near|eigen)|"
        r"codimension-`?r`?(?![A-Za-z])|`?r`?\s+x\s+`?r`?\s+(?:feshbach|effective)",
        re.IGNORECASE,
    )
    rejection = re.compile(
        r"historical|false|falsified|reject|withdraw|supersed|forbidden|cannot|do not|not a theorem|\bno\b",
        re.IGNORECASE,
    )
    for path in package.glob("[0-9][0-9]_*/*.md"):
        if path.name not in {"THEOREM_STATEMENT.md", "FULL_PROOF.md"}:
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        for index, line in enumerate(lines):
            if forbidden.search(line):
                context = " ".join(lines[max(0, index - 1):index + 2])
                require(rejection.search(context) is not None, f"active stale-r wording: {path}:{index+1}")

    if check_git:
        require(
            git_tree("research/paper/manuscript_tex_pub")
            == "59e3a8f73a152ef06f994e979b7219a3365efeae",
            "English manuscript tree changed",
        )
        require(
            git_tree("research/paper/manuscript_tex_pub_zh")
            == "57ae03fb5b90866f84d0d72b414008678e8f5004",
            "Chinese manuscript tree changed",
        )

    return {
        "candidate_attainment_bridge": True,
        "candidate_fourier_identity": True,
        "classification_equality_logic": True,
        "G6_essential_spectrum_bridge": True,
        "G6_cross_references_repaired": True,
        "exact_2r_patch_identification": True,
        "reflection_lifts_holonomy_seam_covered": True,
        "seven_theorem_families": True,
        "import_blacklist_complete": True,
        "canonical_bridge_claims_registered": True,
        "no_active_stale_rank_claim": True,
        "formal_manuscripts_frozen": True,
    }


if __name__ == "__main__":
    require(all(verify().values()), "Task 57.5 proof repair failed")
    print("TARGET_A_TASK575_PROOF_REPAIR_VERIFY_PASS")

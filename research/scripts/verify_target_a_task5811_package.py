"""Fail-closed audit for Task 58.11, appendices and submission artifacts."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from pypdf import PdfReader


REPO = Path(__file__).resolve().parents[2]
MAIN = REPO / "research/paper/manuscript_tex_task58"
SUPP = REPO / "research/paper/manuscript_tex_task58_supplement"
CONTROL = REPO / "research/paper/task58"
ENGLISH_TREE = "59e3a8f73a152ef06f994e979b7219a3365efeae"
CHINESE_TREE = "57ae03fb5b90866f84d0d72b414008678e8f5004"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def git_tree(path: str) -> str:
    output = subprocess.check_output(
        ["git", "ls-tree", "HEAD", path], cwd=REPO, text=True
    ).strip()
    require(output, f"missing frozen tree: {path}")
    return output.split()[2]


def verify() -> dict[str, int | bool | str]:
    required_main = (
        "main.tex", "main.pdf", "main_anonymous.tex", "main_anonymous.pdf",
        "appendices/appendix_a_g6_certification.tex",
        "appendices/appendix_b_finite_classification.tex",
        "sections/08_concluding.tex", "sections/09_data_code_availability.tex",
    )
    required_supp = (
        "main.tex", "main.pdf", "README.md",
        "sections/01_exact_2r.tex", "sections/02_single_gap.tex",
        "sections/03_reproducibility.tex",
    )
    require(all((MAIN / path).is_file() for path in required_main),
            "main-paper package incomplete")
    require(all((SUPP / path).is_file() for path in required_supp),
            "supplement package incomplete")

    main_tex = "\n".join(path.read_text(encoding="ascii") for path in MAIN.rglob("*.tex"))
    supp_tex = "\n".join(path.read_text(encoding="ascii") for path in SUPP.rglob("*.tex"))
    for marker in ("TASK58_DRAFT_STUB", "TODO", "TBD", "FIXME", "PLACEHOLDER"):
        require(marker not in main_tex and marker not in supp_tex,
                f"draft marker remains: {marker}")
    require(r"\footnote" not in main_tex + supp_tex, "author footnote remains")

    figure_inputs = re.findall(r"\\input\{figures/([^}]+)\}", main_tex)
    require(sorted(figure_inputs) == [
        "figure_cycle_switching", "figure_patch_localization", "figure_reference_slips"
    ], "main-text figure inventory changed")
    for label in (
        "fig:switching-coordinates", "fig:reference-slips", "fig:patch-localization"
    ):
        require(f"\\ref{{{label}}}" in main_tex and f"\\label{{{label}}}" in main_tex,
                f"figure not explicitly cited: {label}")
    for figure_path in (MAIN / "figures").glob("*.tex"):
        figure = figure_path.read_text(encoding="ascii")
        require("rounded corners" not in figure and "color=" not in figure,
                f"nonessential figure decoration: {figure_path.name}")

    conclusion = (MAIN / "sections/08_concluding.tex").read_text(encoding="ascii")
    require(conclusion.count("?") == 3, "Conclusion must contain exactly three questions")
    for lead in ("First,", "Second,", "Third,"):
        require(lead in conclusion, f"Conclusion question absent: {lead}")
    require("proves only the corresponding upper\nlimit bound" in conclusion,
            "limsup-only boundary absent")
    require("restricted to\nsingle-gap interfaces" in conclusion,
            "single-gap scope boundary absent")
    require("do not\nclassify the minimizing switching classes" in conclusion,
            "minimizer-structure nonclaim absent")

    availability = (MAIN / "sections/09_data_code_availability.tex").read_text(
        encoding="ascii"
    )
    availability_compact = "".join(availability.split())
    require("https://github.com/whzy3185/math" in availability,
            "development repository absent")
    require("e365e1553ad73a8a534f" in availability and
            "b67f5ee76562521609ce" in availability,
            "source checkpoint absent")
    require("hasnotyetbeenassigned" in availability_compact and
            "willaccompanythefinalsubmittedversion" in availability_compact,
            "archive-pending statement absent")
    require("DOI" not in availability, "invented or provisional DOI present")
    for phrase in ("certificate manifest", "source commit",
                   "reproducibility supplement", "dependency information"):
        require(phrase in availability, f"archive content absent: {phrase}")

    app_a = (MAIN / "appendices/appendix_a_g6_certification.tex").read_text(
        encoding="ascii"
    )
    app_b = (MAIN / "appendices/appendix_b_finite_classification.tex").read_text(
        encoding="ascii"
    )
    require(len(app_a.splitlines()) >= 450, "Appendix A is incomplete")
    require(len(app_b.splitlines()) >= 400, "Appendix B is incomplete")
    for phrase in (
        "reference Floquet calculation", "Exact transfer through the G6 core",
        "Physical realization and algebraic identification",
        "complete Grassmann atlas", "genuine unsquared exclusion",
        "squared multiplicity",
    ):
        require(phrase.lower() in app_a.lower(), f"Appendix A topic absent: {phrase}")
    for token in (
        "p_6(y)^2", "Sturm", "I_1", "I_2",
        r"\dim\ker(H_6-c_6)=2", "continuous orientation",
        "cross-chart necessity argument",
    ):
        require(token in app_a, f"Appendix A certificate fact absent: {token}")
    for phrase in (
        "finite quotient and its spectral certificates",
        "Complete decisions through order thirty",
        "exact counterexamples at orders thirty-two and forty",
        "Local exclusion at the six recovery orders",
        "Parity-lifted overlap closure",
        "exact bridge from forty-eight to two hundred thirty-eight",
    ):
        require(phrase.lower() in app_b.lower(), f"Appendix B topic absent: {phrase}")
    for token in ("64", "96", "none remains unresolved",
                  r"15541I_{40}-2000A_{40}^2"):
        require(token in app_b, f"Appendix B finite fact absent: {token}")
    require("strictly positive fraction-free leading principal" in app_b and
            "two choices \\(\\tau_0=\\pm1\\)" in app_b,
            "Appendix B exact positivity or lift-count boundary absent")
    main_without_availability = main_tex.replace(availability, "")
    for pattern in (r"research/", r"scripts/", r"certificates/", r"target_a_task"):
        require(re.search(pattern, main_without_availability, re.IGNORECASE) is None,
                f"internal path leaked into main paper: {pattern}")
    for word in ("JSON", "schema", "hash", "tamper"):
        require(word not in app_a and word not in app_b,
                f"engineering prose leaked into appendix: {word}")

    exact2r = (SUPP / "sections/01_exact_2r.tex").read_text(encoding="ascii")
    witnesses = (SUPP / "sections/02_single_gap.tex").read_text(encoding="ascii")
    manifest = (SUPP / "sections/03_reproducibility.tex").read_text(encoding="ascii")
    for token in (
        r"D\geq1040", r"=2r", r"\cSix-\frac1{200}",
        r"H_{\mathrm{eff}}(z)", "3505", r"\frac9{25}", "3120",
    ):
        require(token in exact2r, f"supplement exact-2r fact absent: {token}")
    for gap in ("Gap \\(g=1\\)", "Gap \\(g=2\\)", "Gap \\(g=3\\)",
                "Gap \\(g=5\\)", "Gap \\(g=7\\)", "Gap \\(g=8\\)"):
        require(gap in witnesses, f"single-gap witness absent: {gap}")
    require("e365e1553ad73a8a534fb67f5ee76562521609ce" in manifest,
            "supplement checkpoint absent")
    require("pending" in manifest.lower() and "DOI" in manifest,
            "supplement archive boundary absent")
    path_matches = sorted(set(re.findall(r"research/[A-Za-z0-9_./-]+", supp_tex)))
    for raw_path in path_matches:
        path = raw_path.rstrip(".,;:)")
        require((REPO / path).exists(), f"supplement path missing: {path}")
    for required_path in (
        "research/proofs/task50/certificates/g6_interface_certificate.json",
        "research/proofs/task51/certificates/c6_exact_evans_elimination.json",
        "research/scripts/verify_target_a_task56_single_gap.py",
        "research/counterexamples/target_a_minimality_certificate.json",
        "research/counterexamples/target_a_n32_period8_certificate.json",
        "research/proofs/task55/certificates/small_order_exact_classification.json",
        "research/proofs/task55/TARGET_A_ORDERS_34_46_CERTIFICATES.json",
        "research/proofs/task54/TARGET_A_TASK54_EVENTUAL_THRESHOLD_CERTIFICATE.json",
    ):
        require(required_path in supp_tex, f"core artifact missing from manifest: {required_path}")
    require(re.search(r"(?m)^python3 research/scripts/test_", manifest) is None,
            "pytest module is invoked as an inert plain script")
    require(re.search(r"(?<!\\)qquad", supp_tex) is None,
            "literal qquad remains in supplement formulas")

    main_reader = PdfReader(MAIN / "main.pdf")
    anonymous_reader = PdfReader(MAIN / "main_anonymous.pdf")
    supp_reader = PdfReader(SUPP / "main.pdf")
    main_pages = len(main_reader.pages)
    anonymous_pages = len(anonymous_reader.pages)
    supplement_pages = len(supp_reader.pages)
    require(main_pages <= 45 and anonymous_pages <= 45, "essential paper exceeds page gate")
    require(supplement_pages > 0, "supplement PDF is empty")
    anonymous_text = "\n".join(page.extract_text() or "" for page in anonymous_reader.pages)
    require("github.com/whzy3185" not in anonymous_text and
            "e365e1553ad73a8a534f" not in anonymous_text,
            "anonymous PDF leaks repository identity")
    require(main_reader.metadata.title ==
            "Spectral Radius Minimization for Signed Squares of Cycles",
            "main PDF title metadata absent")
    require(anonymous_reader.metadata.author == "Anonymous",
            "anonymous PDF author metadata absent")
    app_a_page = app_b_page = refs_page = None
    for page_number, page in enumerate(main_reader.pages, 1):
        text = page.extract_text() or ""
        if app_a_page is None and "Exact Spectral Certi" in text:
            app_a_page = page_number
        if app_b_page is None and "Exact Finite Classi" in text:
            app_b_page = page_number
        if refs_page is None and text.lstrip().startswith("References"):
            refs_page = page_number
    require(app_a_page == 24 and app_b_page > app_a_page and refs_page == main_pages,
            "main narrative/appendix/bibliography page boundary changed")

    layout = (CONTROL / "TASK58_LAYOUT_AND_LENGTH_AUDIT.md").read_text(encoding="ascii")
    for phrase in (
        "TASK58_11_VISUAL_AND_LENGTH_PASS", "Main-text figures: 3",
        "Author footnotes: 0", "TASK58_DRAFT_STUB: 0",
        "Immutable archive: PENDING",
    ):
        require(phrase in layout, f"layout audit fact absent: {phrase}")
    require(git_tree("research/paper/manuscript_tex_pub") == ENGLISH_TREE,
            "historical English manuscript changed")
    require(git_tree("research/paper/manuscript_tex_pub_zh") == CHINESE_TREE,
            "historical Chinese manuscript changed")

    return {
        "main_pages": main_pages,
        "anonymous_pages": anonymous_pages,
        "supplement_pages": supplement_pages,
        "main_figures": 3,
        "draft_stubs": 0,
        "author_footnotes": 0,
        "archive_status": "IMMUTABLE_ARCHIVE_PENDING",
        "author_metadata_status": "PENDING_USER_METADATA",
        "historical_trees_frozen": True,
    }


if __name__ == "__main__":
    result = verify()
    print(
        "TARGET_A_TASK5811_PACKAGE_VERIFY_PASS "
        f"main={result['main_pages']} anonymous={result['anonymous_pages']} "
        f"supplement={result['supplement_pages']} figures={result['main_figures']} "
        f"stubs={result['draft_stubs']} footnotes={result['author_footnotes']} "
        f"archive={result['archive_status']}"
    )

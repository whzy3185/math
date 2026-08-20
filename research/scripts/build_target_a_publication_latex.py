"""Build publication LaTeX from the frozen Target A manuscript sources."""

from __future__ import annotations

import hashlib
import re
import shutil
from dataclasses import dataclass
from pathlib import Path

from build_target_a_manuscript_md import build_manuscript


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
MD_DIR = RESEARCH_ROOT / "paper" / "manuscript_md"
PUB_DIR = RESEARCH_ROOT / "paper" / "manuscript_tex_pub"
CANONICAL = MD_DIR / "TARGET_A_MANUSCRIPT_V2.md"
FROZEN_SHA256 = "d7b9e35acd57b2ab9916bf82bf8d52359ee30ab13cda09efebf0f93f8e76ce6b"

SECTIONS = [
    "02_INTRODUCTION",
    "03_PRELIMINARIES",
    "04_SMALLEST_COUNTEREXAMPLE",
    "05_PERIODIC_FLOQUET",
    "06_PERIOD8_SPECTRAL_EDGE",
    "07_EIGHT_BARRIER",
    "08_GENERAL_PERIOD",
    "09_LOW_PERIOD_FRONTIER",
    "10_COMPUTATIONAL_VERIFICATION",
    "11_DISCUSSION",
]
APPENDICES = [
    "12_APPENDIX_ORBIT_COMPLETENESS",
    "13_APPENDIX_EXACT_CERTIFICATES",
    "14_APPENDIX_COMPUTATION",
]

CITATIONS = {
    "1": "BiluLinial2006",
    "2": "Lieb1994",
    "3": "MarcusSpielmanSrivastava2015",
    "4": "Suvagiya2026Parity",
    "5": "Suvagiya2026Signed",
    "6": "XuZhang2026",
}

SECTION_LABELS = {
    "1": "sec:introduction",
    "2": "sec:preliminaries",
    "3": "sec:smallest-counterexample",
    "4": "sec:periodic-construction",
    "5": "sec:period-eight-edge",
    "6": "sec:eight-barrier",
    "7": "sec:general-period",
    "8": "sec:low-period-frontier",
    "9": "sec:computational-verification",
    "10": "sec:discussion",
}

APPENDIX_LABELS = {
    "A": "app:orbit-completeness",
    "B": "app:exact-certificates",
    "C": "app:computational-protocol",
}

SUBSECTION_LABELS = {
    "2.3": "subsec:floquet-matrices",
    "6.2": "subsec:all-negative-baseline",
    "6.4": "subsec:four-or-more-defects",
    "6.5": "subsec:two-defects",
}

EQUATION_LABELS = {
    "2.1": "eq:periodic-operator",
    "2.2": "eq:quadrilateral-flux",
    "2.3": "eq:local-defect-statistics",
    "2.4": "eq:fiber-transpose",
    "2.5": "eq:squared-periodic-radius",
    "2.6": "eq:finite-bloch-grid",
    "2.7": "eq:finite-floquet-decomposition",
    "2.8": "eq:zone-folding",
    "2.9": "eq:moment-and-excess",
    "2.10": "eq:moment-integral",
    "2.11": "eq:moment-barrier",
    "2.12": "eq:conjectured-threshold",
    "2.13": "eq:target-edge",
    "3.1": "eq:order-thirty-two-triangle-word",
    "3.2": "eq:order-thirty-two-flux-word",
    "3.3": "eq:order-thirty-two-certificate",
    "3.4": "eq:order-thirty-two-threshold",
    "3.5": "eq:order-thirty-two-polynomial",
    "3.6": "eq:excluded-orders",
    "3.7": "eq:finite-exclusion-bound",
    "3.8": "eq:rayleigh-certificate",
    "4.1": "eq:target-triangle-word",
    "4.2": "eq:target-floquet-matrix",
    "4.3": "eq:target-finite-decomposition",
    "4.4": "eq:target-characteristic-polynomial",
    "4.5": "eq:floquet-polynomial",
    "4.6": "eq:rational-positive-expansion",
    "4.7": "eq:uniform-fiber-bound",
    "4.8": "eq:finite-family-upper-bound",
    "4.9": "eq:threshold-at-thirty-two",
    "4.10": "eq:monotone-threshold-bound",
    "5.1": "eq:edge-polynomial",
    "5.2": "eq:edge-depressed-quartic",
    "5.3": "eq:edge-four-roots",
    "5.4": "eq:eta-definition",
    "5.5": "eq:eta-positive-expansion",
    "5.6": "eq:exact-infinite-edge",
    "5.7": "eq:eta-minimal-polynomial",
    "5.8": "eq:minus-one-fiber-factorization",
    "5.9": "eq:minus-one-fiber-comparison",
    "5.10": "eq:floquet-c-derivative",
    "5.11": "eq:positive-holonomy-edge",
    "5.12": "eq:negative-holonomy-edge",
    "6.1": "eq:all-negative-square",
    "6.2": "eq:all-negative-dispersion",
    "6.3": "eq:period-eight-first-moment",
    "6.4": "eq:period-eight-second-moment",
    "6.5": "eq:period-eight-third-moment",
    "6.6": "eq:period-eight-second-excess",
    "6.7": "eq:target-antiperiodicity",
    "6.8": "eq:chiral-symmetry",
    "6.9": "eq:off-diagonal-square",
    "7.1": "eq:tau-product-from-flux",
    "7.2": "eq:walk-recurrence",
    "7.3": "eq:walk-moment",
    "7.4": "eq:general-flux-moments",
    "7.5": "eq:general-defect-moments",
    "7.6": "eq:general-excesses",
    "7.7": "eq:general-necessary-conditions",
    "8.1": "eq:legal-periodic-flux",
    "8.2": "eq:low-period-orbit-counts",
    "8.3": "eq:frontier-moment-exclusion",
    "8.4": "eq:target-zone-folding-rows",
    "8.5": "eq:residual-rayleigh-quotient",
    "8.6": "eq:residual-radical-comparison",
    "8.7": "eq:frontier-partition",
    "A.1": "eq:cycle-coordinate-space",
    "A.2": "eq:orbit-weight-identity",
    "A.3": "eq:permutation-cycle-sign",
    "A.4": "eq:burnside-orbit-count",
}

THEOREM_LABELS = {
    "A": "thm:smallest-counterexample",
    "B": "thm:infinite-counterexample-family",
    "C": "thm:exact-period-eight-edge",
    "D": "thm:eight-barrier-trichotomy",
    "E": "thm:general-period-moment-obstruction",
    "F": "thm:low-period-frontier",
}

NUMBERED_STATEMENT_LABELS = {
    ("Lemma", "2.1"): "lem:operator-equivalences",
    ("Lemma", "2.2"): "lem:zone-folding",
    ("Lemma", "2.3"): "lem:moment-barrier",
    ("Proposition", "3.1"): "prop:order-thirty-two-witness",
    ("Proposition", "3.2"): "prop:finite-exclusion",
    ("Proposition", "4.1"): "prop:finite-floquet-decomposition",
}

TABLE_METADATA = {
    ("04_SMALLEST_COUNTEREXAMPLE", 1): (
        "Finite minimality enumeration and exact nonoptimizer certificates.",
        "tab:minimality-counts",
    ),
    ("07_EIGHT_BARRIER", 1): (
        "Coefficients of the squared operator by displacement.",
        "tab:squared-operator-coefficients",
    ),
    ("07_EIGHT_BARRIER", 2): (
        "First positive moment excess for two nonantipodal defects.",
        "tab:two-defect-excesses",
    ),
    ("08_GENERAL_PERIOD", 1): (
        "Closed-walk contributions from one starting residue.",
        "tab:closed-walk-contributions",
    ),
    ("09_LOW_PERIOD_FRONTIER", 1): (
        "Residual low-period competitors requiring endpoint certificates.",
        "tab:residual-competitors",
    ),
    ("10_COMPUTATIONAL_VERIFICATION", 1): (
        "Canonical spectral states and checkpoint chunks in the large-order enumeration.",
        "tab:checkpoint-counts",
    ),
    ("12_APPENDIX_ORBIT_COMPLETENESS", 1): (
        "Legal flux words and dihedral orbit counts through period sixteen.",
        "tab:low-period-orbit-counts",
    ),
    ("13_APPENDIX_EXACT_CERTIFICATES", 1): (
        "Exact classification of legal period-eight flux orbits.",
        "tab:period-eight-classification",
    ),
    ("13_APPENDIX_EXACT_CERTIFICATES", 2): (
        "Exact Rayleigh data for the five residual competitors.",
        "tab:residual-rayleigh-data",
    ),
    ("13_APPENDIX_EXACT_CERTIFICATES", 3): (
        "Exact radical-comparison data for the residual competitors.",
        "tab:residual-radical-data",
    ),
    ("13_APPENDIX_EXACT_CERTIFICATES", 4): (
        "Moment and excess sequences for separated period-eight defect pairs.",
        "tab:separated-defect-moments",
    ),
    ("14_APPENDIX_COMPUTATION", 1): (
        "Recorded regeneration resources and terminal checkpoint hashes.",
        "tab:regeneration-resources",
    ),
}


def verify_frozen_source() -> None:
    canonical_bytes = CANONICAL.read_bytes()
    digest = hashlib.sha256(canonical_bytes).hexdigest()
    if digest != FROZEN_SHA256:
        raise RuntimeError(f"FROZEN_SOURCE_HASH_MISMATCH:{digest}")
    if build_manuscript() != canonical_bytes.decode("utf-8"):
        raise RuntimeError("FROZEN_COMPONENT_MERGE_MISMATCH")


def escape_text(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
    }
    return "".join(replacements.get(char, char) for char in text)


def _balanced_function(value: str, name: str, command: str) -> str:
    needle = name + "("
    while needle in value:
        start = value.rfind(needle)
        depth = 1
        end = start + len(needle)
        while end < len(value) and depth:
            depth += (value[end] == "(") - (value[end] == ")")
            end += 1
        if depth:
            break
        inside = value[start + len(needle) : end - 1]
        value = value[:start] + command + "{" + inside + "}" + value[end:]
    return value


def latex_math(text: str) -> str:
    value = text.strip()
    if "product_(ell=1)^s product_(h=r_(2ell-1))^(r_(2ell)-1) Q_h" in value:
        return value.replace(
            "product_(ell=1)^s product_(h=r_(2ell-1))^(r_(2ell)-1) Q_h",
            r"\prod_{\ell=1}^{s}\prod_{h=r_{2\ell-1}}^{r_{2\ell}-1}Q_h",
        ).replace("=", "=", 1)
    value = re.sub(r"\s+\(([A-Z]?\d+\.\d+)\)\s*$", "", value)
    value = value.replace("{", r"\{").replace("}", r"\}")
    value = value.replace("Z/nZ", r"\mathbb{Z}/n\mathbb{Z}")
    value = value.replace("emptyset", r"\varnothing")
    value = value.replace("==>", r"\Longrightarrow")
    value = value.replace("~=", r"\cong")
    value = value.replace("<=", r"\leq ").replace(">=", r"\geq ")
    value = value.replace("->", r"\to ")
    value = value.replace("direct_sum", r"\bigoplus")
    value = value.replace("sum_orbits", r"\sum_{\mathrm{orbits}}")
    value = re.sub(r"\^\(([^()]*)\)", r"^{\1}", value)
    value = re.sub(r"_\(([^()]*)\)", r"_{\1}", value)
    value = re.sub(r"\^(-?\d+)", r"^{\1}", value)
    value = re.sub(r"_(\d+)", r"_{\1}", value)
    for name, command in (("sqrt", r"\sqrt"),):
        value = _balanced_function(value, name, command)
    value = re.sub(r"(?<![A-Za-z])2pi(?![A-Za-z])", r"2\\pi", value)
    token_map = {
        "alpha": r"\alpha",
        "eta": r"\eta",
        "epsilon": r"\varepsilon",
        "lambda": r"\lambda",
        "pi": r"\pi",
        "rho": r"\rho",
        "sigma": r"\sigma",
        "tau": r"\tau",
        "theta": r"\theta",
        "delta": r"\delta",
        "ell": r"\ell",
    }
    for token, replacement in token_map.items():
        value = re.sub(
            rf"(?<![A-Za-z\\]){token}(?![A-Za-z])",
            lambda _match, replacement=replacement: replacement,
            value,
        )
    for operator in ("det", "diag", "spec", "tr"):
        value = re.sub(
            rf"(?<![A-Za-z\\]){operator}(?![A-Za-z])",
            lambda _match, operator=operator: rf"\operatorname{{{operator}}}",
            value,
        )
    value = re.sub(r"(?<![A-Za-z])CT_z", lambda _m: r"\operatorname{CT}_{z}", value)
    value = re.sub(r"(?<![A-Za-z])product", lambda _m: r"\prod", value)
    value = re.sub(r"(?<![A-Za-z])integral", lambda _m: r"\int", value)
    value = re.sub(r"(?<![A-Za-z])sum", lambda _m: r"\sum", value)
    for operator in ("cos", "max", "min", "sup"):
        value = re.sub(
            rf"(?<![A-Za-z\\]){operator}(?![A-Za-z])",
            lambda _match, operator=operator: rf"\{operator}",
            value,
        )
    value = re.sub(r"(?<![A-Za-z])in(?![A-Za-z])", lambda _m: r"\in", value)
    value = re.sub(r"(?<![A-Za-z])if(?![A-Za-z])", lambda _m: r"\text{if}", value)
    value = re.sub(r"(?<![A-Za-z])and(?![A-Za-z])", lambda _m: r"\text{and}", value)
    value = re.sub(
        r"(?<![A-Za-z])otherwise(?![A-Za-z])", lambda _m: r"\text{otherwise}", value
    )
    value = value.replace("#", r"\#")
    value = value.replace("translated \\tau", r"\text{translated }\tau")
    value = value.replace("reflected \\tau", r"\text{reflected }\tau")
    value = value.replace("^can", r"^{\mathrm{can}}")
    value = value.replace("...", r"\ldots")
    value = re.sub(r"(?<=\d)\*(?=\d)", r"\\cdot ", value)
    value = re.sub(r"(?<=\w) x (?=\w)", r"\\times ", value)
    value = value.replace("dtheta", r"\,d\theta")
    # Simple arithmetic fractions occurring in the source.
    value = re.sub(
        r"(?<![\w}])(\d+[A-Za-z]?)/(\d+)(?![\w{])",
        lambda match: rf"\frac{{{match.group(1)}}}{{{match.group(2)}}}",
        value,
    )
    value = re.sub(
        r"(?<![\w}])(\\pi)/(n)(?![\w{])",
        lambda match: rf"\frac{{{match.group(1)}}}{{{match.group(2)}}}",
        value,
    )
    value = value.replace("1/(2\\pi)", r"\frac{1}{2\pi}")
    value = re.sub(
        r"(?<![\w}])(\d*\\pi)/(n|L)(?![\w{])",
        lambda match: rf"\frac{{{match.group(1)}}}{{{match.group(2)}}}",
        value,
    )
    value = re.sub(
        r"\|\|([^|]+)\|\|", lambda match: rf"\lVert {match.group(1)}\rVert", value
    )
    value = re.sub(r"\|([^|]+)\|", lambda match: rf"\lvert {match.group(1)}\rvert", value)
    return value


def code_token(text: str) -> str:
    if text == "research/reproducibility/target_a_submission_artifact_manifest.json":
        return (
            r"\path{research/reproducibility/}\allowbreak"
            r"\path{target_a_submission_}\allowbreak"
            r"\path{artifact_manifest.json}"
        )
    if (
        text.endswith((".json", ".py", ".txt", ".md"))
        or text.startswith(("TARGET_A_", ".venv", "research/", "python"))
        or re.fullmatch(r"[0-9a-f]{40,64}", text)
    ):
        if "/" in text or text.endswith((".json", ".py", ".txt", ".md")):
            return r"\path{" + text + "}"
        return r"\texttt{\detokenize{" + text + "}}"
    if text in {"strictly_below", "threshold_lower_bound", "certified_above_threshold"}:
        return r"\texttt{" + text.replace("_", r"\_") + "}"
    if text == "square":
        return ""
    return r"\(" + latex_math(text) + r"\)"


INLINE_PATTERN = re.compile(
    r"`([^`]+)`|\*\*([^*]+)\*\*|\[([^\]]+)\]\((https?://[^)]+)\)|\[([1-6])\]"
)


def _plain_text(text: str) -> str:
    placeholders: dict[str, str] = {}

    def hold(value: str) -> str:
        key = f"ZZREF{len(placeholders)}ZZ"
        placeholders[key] = value
        return key

    for number, label in EQUATION_LABELS.items():
        text = re.sub(
            rf"\b[Ee]quation\s*\({re.escape(number)}\)",
            lambda _m, label=label: hold(rf"Equation~\eqref{{{label}}}"),
            text,
        )
        text = text.replace(f"({number})", hold(rf"\eqref{{{label}}}"))
    section_pairs = {
        "Sections 4 and 5": (
            r"Sections~\ref{sec:periodic-construction} and~\ref{sec:period-eight-edge}"
        ),
        "Sections 2 and 4": (
            r"Sections~\ref{sec:preliminaries} and~\ref{sec:periodic-construction}"
        ),
    }
    for phrase, replacement in section_pairs.items():
        text = text.replace(phrase, hold(replacement))
    for number, label in SUBSECTION_LABELS.items():
        text = re.sub(
            rf"\bSection {re.escape(number)}(?!\d|\.\d)",
            lambda _m, label=label: hold(rf"Section~\ref{{{label}}}"),
            text,
        )
    for number, label in SECTION_LABELS.items():
        text = re.sub(
            rf"\bSection {number}(?!\d|\.\d)",
            lambda _m, label=label: hold(rf"Section~\ref{{{label}}}"),
            text,
        )
    for letter, label in APPENDIX_LABELS.items():
        text = re.sub(
            rf"\bAppendix {letter}\b",
            lambda _m, label=label: hold(rf"Appendix~\ref{{{label}}}"),
            text,
        )
    for letter, label in THEOREM_LABELS.items():
        text = re.sub(
            rf"\bTheorem {letter}\b",
            lambda _m, label=label: hold(rf"Theorem~\ref{{{label}}}"),
            text,
        )
    text = text.replace(
        "Theorems A and F",
        hold(r"Theorems~\ref{thm:smallest-counterexample} and~\ref{thm:low-period-frontier}"),
    )
    for (kind, number), label in NUMBERED_STATEMENT_LABELS.items():
        text = re.sub(
            rf"\b{kind} {re.escape(number)}\b",
            lambda _m, kind=kind, label=label: hold(rf"{kind}~\ref{{{label}}}"),
            text,
        )
    text = text.replace("Table 3.1", hold(r"Table~\ref{tab:minimality-counts}"))
    value = escape_text(text)
    for key, replacement in placeholders.items():
        value = value.replace(key, replacement)
    return value


def render_inline(text: str) -> str:
    pieces: list[str] = []
    cursor = 0
    for match in INLINE_PATTERN.finditer(text):
        pieces.append(_plain_text(text[cursor : match.start()]))
        code, bold, link_text, url, citation = match.groups()
        if code is not None:
            pieces.append(code_token(code))
        elif bold is not None:
            pieces.append(r"\textbf{" + render_inline(bold) + "}")
        elif link_text is not None:
            pieces.append(r"\href{" + url + "}{" + escape_text(link_text) + "}")
        else:
            pieces.append(r"\cite{" + CITATIONS[citation] + "}")
        cursor = match.end()
    pieces.append(_plain_text(text[cursor:]))
    return "".join(pieces).rstrip()


def _equation_label(block: list[str]) -> str | None:
    joined = " ".join(block)
    match = re.search(r"\(((?:[A-Z]|\d+)\.\d+)\)\s*$", joined)
    return EQUATION_LABELS.get(match.group(1)) if match else None


def _align_line(line: str, continuation: bool = False) -> str:
    value = latex_math(line)
    if continuation:
        return r"&\quad " + value
    match = re.search(r"(?<![<>])(?:=|<|>|\\leq|\\geq|\\cong)", value)
    if match:
        return value[: match.start()] + "&" + value[match.start() :]
    return "&" + value


def render_math_block(block: list[str]) -> list[str]:
    label = _equation_label(block)
    cleaned = [
        re.sub(r"\s+\((?:[A-Z]|\d+)\.\d+\)\s*$", "", line.rstrip())
        for line in block
    ]
    raw = "\n".join(cleaned).strip()

    if raw.startswith("https://github.com/"):
        url = "".join(line.strip() for line in cleaned)
        return [r"\begin{center}", rf"\url{{{url}}}", r"\end{center}"]
    if raw.startswith("Python 3.12.13"):
        rows = [line.split(maxsplit=1) for line in cleaned]
        output = [
            r"\begin{center}",
            r"\begin{tabular}{ll}",
            r"\toprule",
            r"Component & Version \\",
            r"\midrule",
        ]
        output.extend(
            f"{escape_text(name)} & {escape_text(version)} \\\\" for name, version in rows
        )
        output.extend([r"\bottomrule", r"\end{tabular}", r"\end{center}"])
        return output
    if raw.startswith("H(z)=\n["):
        rows = []
        for line in cleaned[1:]:
            row = line.strip().strip("[].")
            rows.append(" & ".join(latex_math(cell) for cell in row.split()))
        math = "H(z)=\\begin{pmatrix}\n" + " \\\\\n".join(rows) + "\n\\end{pmatrix}."
    elif raw.startswith("D(Q)=emptyset"):
        math = (
            r"\begin{cases}"
            "\nR(Q)=8, & D(Q)=\\varnothing; \\\\\n"
            "R(Q)=\\eta<8, & D(Q)=\\{j,j+4\\}; \\\\\n"
            "R(Q)>8, & \\text{for every other legal period-eight }Q.\n"
            r"\end{cases}"
        )
    elif raw.startswith("N_p=(1/(2p))"):
        math = (
            r"N_p=\frac{1}{2p}\sum_{g\in D_p}\begin{cases}"
            "2^{c(g)-1}, & \\text{if }g\\text{ has an odd cycle}, \\\\\n"
            "2^{c(g)}, & \\text{if all cycles of }g\\text{ are even}."
            r"\end{cases}"
        )
    elif raw.startswith("M_k(Q)=(1/(2pi))"):
        math = (
            r"M_k(Q)=\frac{1}{2\pi}\int_{0}^{2\pi}"
            r"\sum_j\lambda_j(e^{i\theta})^{2k}\,d\theta."
        )
    elif raw.startswith("W_0^(r)(j)=1 if j=r"):
        math = (
            r"\begin{aligned}"
            "W_0^{(r)}(j)&=\\begin{cases}1,&j=r,\\\\0,&j\\ne r,\\end{cases}\\\\\n"
            "W_{\\ell+1}^{(r)}(j)&=\\sum_{\\delta\\in\\{-2,-1,1,2\\}}"
            "W_{\\ell}^{(r)}(j-\\delta)w(j-\\delta,\\delta).\n"
            r"\end{aligned}"
        )
    elif raw.startswith("H(z)=[0 B; C 0]"):
        math = (
            r"H(z)=\begin{pmatrix}0&B\\C&0\end{pmatrix},\qquad "
            r"H(z)^2=\begin{pmatrix}BC&0\\0&CB\end{pmatrix}."
        )
    elif raw.startswith("2611  moment-detected"):
        math = (
            r"\begin{aligned}"
            r"2611&\quad\text{moment-detected representatives},\\" "\n"
            r"8&\quad\text{repeated all-negative representatives},\\" "\n"
            r"5&\quad\text{endpoint-certified residual competitors},\\" "\n"
            r"2&\quad\text{displayed target representations},\\" "\n"
            r"2626&\quad\text{total representatives}." "\n"
            r"\end{aligned}"
        )
    else:
        if len(cleaned) == 1:
            math = latex_math(cleaned[0])
        else:
            rendered = []
            for index, line in enumerate(cleaned):
                continuation = bool(index and re.match(r"^\s*[+\-]", line))
                rendered.append(_align_line(line, continuation))
            math = "\\begin{aligned}\n" + " \\\\\n".join(rendered) + "\n\\end{aligned}"

    output = [r"\begin{equation}"]
    if label:
        output.append(rf"\label{{{label}}}")
    output.extend(math.splitlines())
    output.append(r"\end{equation}")
    return output


def render_table(lines: list[str], stem: str, index: int) -> list[str]:
    rows = [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in lines]
    rows.pop(1)
    columns = len(rows[0])
    caption, label = TABLE_METADATA[(stem, index)]
    wide = columns >= 5 or max(sum(len(cell) for cell in row) for row in rows) > 90
    spec = "".join("r" if re.fullmatch(r"[\d,.-]+", cell.replace("`", "")) else "l" for cell in rows[0])
    placement = (
        "H"
        if stem == "13_APPENDIX_EXACT_CERTIFICATES" and index in {3, 4}
        else "tbp"
    )
    array_stretch = "1.35" if (stem, index) == ("13_APPENDIX_EXACT_CERTIFICATES", 3) else "1.12"
    output = [
        rf"\begin{{table}}[{placement}]",
        r"\centering",
        rf"\caption{{{caption}}}",
        rf"\label{{{label}}}",
        r"\begingroup",
        rf"\renewcommand{{\arraystretch}}{{{array_stretch}}}",
    ]
    if wide:
        output.extend([r"\scriptsize", r"\resizebox{\textwidth}{!}{%"])
    output.extend([rf"\begin{{tabular}}{{{spec}}}", r"\toprule"])
    for row_index, row in enumerate(rows):
        output.append(" & ".join(render_inline(cell) for cell in row) + r" \\")
        if row_index == 0:
            output.append(r"\midrule")
    output.extend([r"\bottomrule", r"\end{tabular}"])
    if wide:
        output.append("}")
    output.extend([r"\endgroup", r"\end{table}"])
    return output


@dataclass
class ConverterState:
    theorem: str | None = None
    main_theorem_letter: str | None = None
    proof: bool = False
    list_kind: str | None = None
    table_index: int = 0


INTRO_THEOREM_ENDS = {
    "A": "The exclusion through 30",
    "B": "The Floquet analysis is sharp",
    "C": "The local mechanism is described",
    "D": "The same squared-operator calculation",
    "E": "Finally we classify",
    "F": "This theorem is also computer-assisted",
}


def convert_markdown(text: str, stem: str) -> str:
    lines = text.splitlines()
    output: list[str] = []
    state = ConverterState()
    index = 0

    def close_list() -> None:
        if state.list_kind:
            output.append(rf"\end{{{state.list_kind}}}")
            state.list_kind = None

    def close_statement() -> None:
        if state.proof:
            close_list()
            output.append(r"\end{proof}")
            state.proof = False
        if state.theorem:
            close_list()
            output.append(rf"\end{{{state.theorem}}}")
            state.theorem = None
            state.main_theorem_letter = None

    while index < len(lines):
        line = lines[index].rstrip()

        if stem == "02_INTRODUCTION" and state.main_theorem_letter:
            letter = state.main_theorem_letter
            if line.startswith(INTRO_THEOREM_ENDS[letter]):
                close_statement()

        if state.proof and (
            line.startswith("#")
            or re.match(r"^\*\*(?:Lemma|Proposition|Theorem)", line)
            or line.startswith("We emphasize that")
        ):
            close_statement()

        if line.startswith("```"):
            close_list()
            language = line[3:].strip()
            block: list[str] = []
            index += 1
            while index < len(lines) and not lines[index].startswith("```"):
                block.append(lines[index])
                index += 1
            if language == "bash":
                output.append(r"\begin{lstlisting}[language=bash]")
                for shell_line in block:
                    shell_line = shell_line.replace(
                        'export OUT=/absolute/path/to/target-a-regeneration',
                        'export OUT="${TARGET_A_OUTPUT:?set TARGET_A_OUTPUT}"',
                    )
                    shell_line = shell_line.replace(
                        '--output /tmp/target_a_checkpoint_replay.json',
                        '--output "$OUT/target_a_checkpoint_replay.json"',
                    )
                    output.append(shell_line)
                output.append(r"\end{lstlisting}")
            else:
                output.extend(render_math_block(block))
        elif line.startswith("| ") and index + 1 < len(lines) and re.match(r"^\|[-: |]+\|$", lines[index + 1]):
            close_list()
            table = [line, lines[index + 1]]
            index += 2
            while index < len(lines) and lines[index].startswith("|"):
                table.append(lines[index])
                index += 1
            state.table_index += 1
            output.extend(render_table(table, stem, state.table_index))
            continue
        elif line.startswith("# "):
            close_statement()
            match = re.match(r"# (\d+)\.\s*(.*)", line)
            app_match = re.match(r"# Appendix ([A-C])\.\s*(.*)", line)
            if match:
                number, title = match.groups()
                output.append(rf"\section{{{render_inline(title)}}}\label{{{SECTION_LABELS[number]}}}")
            elif app_match:
                letter, title = app_match.groups()
                output.append(rf"\section{{{render_inline(title)}}}\label{{{APPENDIX_LABELS[letter]}}}")
        elif line.startswith("## "):
            close_list()
            number_match = re.match(r"^## (\d+\.\d+)\s*(.*)", line)
            title = re.sub(r"^## (?:\d+\.\d+\s*|[A-C]\.\d+\s*)", "", line)
            subsection = rf"\subsection{{{render_inline(title)}}}"
            if number_match and number_match.group(1) in SUBSECTION_LABELS:
                subsection += rf"\label{{{SUBSECTION_LABELS[number_match.group(1)]}}}"
            output.append(subsection)
        elif line.startswith("### "):
            close_list()
            output.append(rf"\subsubsection{{{render_inline(line[4:])}}}")
        elif re.match(r"^\*\*Theorem [A-F] ", line):
            close_statement()
            match = re.match(r"^\*\*Theorem ([A-F]) \(([^)]+)\)\.\*\*\s*(.*)", line)
            if not match:
                raise RuntimeError(f"THEOREM_PARSE_FAIL:{line}")
            letter, title, body = match.groups()
            state.theorem = "theorem"
            state.main_theorem_letter = letter
            output.extend(
                [
                    rf"\begin{{theorem}}[{render_inline(title.title())}]",
                    rf"\label{{{THEOREM_LABELS[letter]}}}",
                    render_inline(body),
                ]
            )
        elif re.match(r"^\*\*(Lemma|Proposition) ", line):
            close_statement()
            match = re.match(r"^\*\*(Lemma|Proposition) ([0-9.]+)(?: \(([^)]+)\))?\.\*\*\s*(.*)", line)
            if not match:
                raise RuntimeError(f"STATEMENT_PARSE_FAIL:{line}")
            kind, number, title, body = match.groups()
            env = kind.lower()
            state.theorem = env
            opening = rf"\begin{{{env}}}" + (rf"[{render_inline(title)}]" if title else "")
            output.extend(
                [opening, rf"\label{{{NUMBERED_STATEMENT_LABELS[(kind, number)]}}}", render_inline(body)]
            )
        elif line.startswith("**Proof.**"):
            if state.theorem:
                output.append(rf"\end{{{state.theorem}}}")
                state.theorem = None
            state.proof = True
            output.extend([r"\begin{proof}", render_inline(line[len("**Proof.**") :].strip())])
        elif re.match(r"^\d+\. ", line):
            if state.list_kind != "enumerate":
                close_list()
                state.list_kind = "enumerate"
                output.append(r"\begin{enumerate}")
            output.append(r"\item " + render_inline(re.sub(r"^\d+\. ", "", line)))
        elif line.startswith("- "):
            if state.list_kind != "itemize":
                close_list()
                state.list_kind = "itemize"
                output.append(r"\begin{itemize}")
            output.append(r"\item " + render_inline(line[2:]))
        elif not line.strip():
            close_list()
            output.append("")
        else:
            if state.list_kind and re.match(r"^\s{2,}\S", line):
                output[-1] += " " + render_inline(line.strip())
            else:
                close_list()
                rendered = render_inline(line)
                if stem == "02_INTRODUCTION":
                    rendered = rendered.replace(
                        "As of 20 August 2026, we found no direct public resolution",
                        "To the best of our knowledge, there is no direct public resolution",
                    )
                    rendered = rendered.replace(
                        "This is a dated and bounded search statement, not an absolute priority claim.",
                        "This is a bounded literature statement, not an absolute priority claim; the search date and scope are recorded in the reproducibility note.",
                    )
                output.append(rendered)
        index += 1

    close_statement()
    close_list()
    return "\n".join(output).rstrip() + "\n"


def abstract_tex() -> str:
    source = (MD_DIR / "01_TITLE_AND_ABSTRACT.md").read_text(encoding="utf-8")
    abstract = source.split("## Abstract", 1)[1].strip()
    return "\n".join(render_inline(line) for line in abstract.splitlines())


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


PREAMBLE = r"""\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{microtype}
\usepackage{mathtools,amssymb,amsthm}
\usepackage{booktabs,array,tabularx,graphicx}
\usepackage{float}
\usepackage{xcolor}
\usepackage{listings}
\usepackage[hidelinks]{hyperref}
\usepackage[nameinlink,noabbrev]{cleveref}
\usepackage{geometry}
\geometry{margin=1in}
\emergencystretch=3em
\raggedbottom

\DeclareMathOperator{\spec}{spec}
\DeclareMathOperator{\diag}{diag}
\DeclareMathOperator{\CT}{CT}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}

\lstset{
  basicstyle=\ttfamily\footnotesize,
  breaklines=true,
  columns=fullflexible,
  keepspaces=true,
  frame=single,
  rulecolor=\color{black!25},
  xleftmargin=0.5em,
  xrightmargin=0.5em
}
"""

FRONTMATTER = r"""\title{Counterexamples and Flux-Phase Structure for Signed Circulant Graphs}
\ifdefined\TargetAAnonymous
  \author{Anonymous}
\else
  \author{[AUTHOR NAME]}
\fi
\date{}
\maketitle

\ifdefined\TargetAAnonymous\else
\begin{center}
\small
\mbox{[AFFILIATION]}\\
\mbox{[DEPARTMENT]}, \mbox{[INSTITUTION]}\\
\mbox{[CITY]}, \mbox{[COUNTRY]}\\[3pt]
Corresponding author: [CORRESPONDING AUTHOR]\\
Email: [EMAIL]\quad ORCID: [ORCID]
\end{center}
\fi

\begin{abstract}
__ABSTRACT__
\end{abstract}

\noindent\textbf{Keywords:} [KEYWORDS TO CONFIRM]\par
\noindent\textbf{MSC 2020:} [MSC CODES TO CONFIRM]
"""

DATA_AVAILABILITY = r"""\section*{Data and Code Availability}
\addcontentsline{toc}{section}{Data and Code Availability}
The source code, exact certificates, canonical tables, and reproducibility
manifests supporting the computer-assisted statements are available in the
public immutable GitHub snapshot
\url{https://github.com/whzy3185/math/tree/c81be34a3b12a7ac47adbb4499c475df7bf4fc04}.
The public-status search was last run on 20 August 2026 and had the bounded
scope described in the repository's novelty-audit record.  A preservation
record should be added before submission: [ARCHIVAL DOI TO ADD BEFORE
SUBMISSION].

\section*{Funding}
[FUNDING INFORMATION]

\section*{Acknowledgments}
[ACKNOWLEDGMENTS]

\section*{Supplementary Material}
The computational protocol and exact certificate tables are included in the
appendices of this build.  External preservation identifiers remain to be
assigned: [SUPPLEMENT ARCHIVE DOI], [CODE ARCHIVE DOI], and [DATA ARCHIVE DOI].
"""

BIBLIOGRAPHY = r"""@article{BiluLinial2006,
  author = {Bilu, Yonatan and Linial, Nathan},
  title = {Lifts, discrepancy and nearly optimal spectral gap},
  journal = {Combinatorica},
  volume = {26},
  number = {5},
  pages = {495--519},
  year = {2006},
  doi = {10.1007/s00493-006-0029-7}
}

@article{Lieb1994,
  author = {Lieb, Elliott H.},
  title = {Flux phase of the half-filled band},
  journal = {Physical Review Letters},
  volume = {73},
  number = {16},
  pages = {2158--2161},
  year = {1994},
  doi = {10.1103/PhysRevLett.73.2158}
}

@article{MarcusSpielmanSrivastava2015,
  author = {Marcus, Adam W. and Spielman, Daniel A. and Srivastava, Nikhil},
  title = {Interlacing families {I}: Bipartite {Ramanujan} graphs of all degrees},
  journal = {Annals of Mathematics},
  volume = {182},
  number = {1},
  pages = {307--325},
  year = {2015},
  doi = {10.4007/annals.2015.182.1.7}
}

@misc{Suvagiya2026Parity,
  author = {Suvagiya, Vaibhav},
  title = {Parity families and a kernel-averaged {L}-function for near-{Ramanujan} signings},
  year = {2026},
  eprint = {2607.17343},
  archiveprefix = {arXiv},
  primaryclass = {math.CO},
  howpublished = {arXiv preprint arXiv:2607.17343v1}
}

@misc{Suvagiya2026Signed,
  author = {Suvagiya, Vaibhav},
  title = {Signed circulants at the {Ramanujan} bound},
  year = {2026},
  eprint = {2607.18334},
  archiveprefix = {arXiv},
  primaryclass = {math.CO},
  howpublished = {arXiv preprint arXiv:2607.18334v1}
}

@misc{XuZhang2026,
  author = {Xu, Zhiqiang and Zhang, Xinyue},
  title = {An improved upper bound for the {Bilu--Linial} conjecture via interlacing families},
  year = {2026},
  eprint = {2606.28797},
  archiveprefix = {arXiv},
  primaryclass = {math.CO},
  howpublished = {arXiv preprint arXiv:2606.28797v2},
  note = {Withdrawn}
}

@article{Zaslavsky1982,
  author = {Zaslavsky, Thomas},
  title = {Signed graphs},
  journal = {Discrete Applied Mathematics},
  volume = {4},
  number = {1},
  pages = {47--74},
  year = {1982},
  doi = {10.1016/0166-218X(82)90033-6}
}

@book{Davis1979,
  author = {Davis, Philip J.},
  title = {Circulant Matrices},
  publisher = {John Wiley \& Sons},
  address = {New York},
  year = {1979}
}

@book{Kuchment1993,
  author = {Kuchment, Peter A.},
  title = {Floquet Theory for Partial Differential Equations},
  series = {Operator Theory: Advances and Applications},
  volume = {60},
  publisher = {Birkh{\"a}user},
  address = {Basel},
  year = {1993}
}
"""


def wrapper(*, anonymous: bool = False, variant: str = "generic") -> str:
    class_options = "11pt"
    variant_note = ""
    if variant == "sidma":
        class_options = "11pt,fleqn"
        variant_note = r"\newcommand{\TargetAJournalVariant}{SIDMA pre-adaptation}"
    elif variant == "jgt":
        variant_note = r"\newcommand{\TargetAJournalVariant}{JGT pre-adaptation}"
    anonymous_line = r"\newcommand{\TargetAAnonymous}{1}" if anonymous else ""
    return rf"""\documentclass[{class_options}]{{article}}
{anonymous_line}
{variant_note}
\input{{publication-preamble}}
\begin{{document}}
\input{{frontmatter}}
\input{{body}}
\bibliographystyle{{plain}}
\bibliography{{references}}
\end{{document}}
"""


def build() -> None:
    verify_frozen_source()
    if PUB_DIR.exists():
        for child in PUB_DIR.iterdir():
            if child.name == "build":
                continue
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()

    for stem in SECTIONS:
        source = (MD_DIR / f"{stem}.md").read_text(encoding="utf-8")
        write(PUB_DIR / "sections" / f"{stem.lower()}.tex", convert_markdown(source, stem))
    for stem in APPENDICES:
        source = (MD_DIR / f"{stem}.md").read_text(encoding="utf-8")
        write(PUB_DIR / "appendices" / f"{stem.lower()}.tex", convert_markdown(source, stem))

    related_work = (
        "\nThe switching viewpoint belongs to the classical theory of signed graphs~"
        "\\cite{Zaslavsky1982}; circulant spectra and Floquet reduction provide the "
        "finite and periodic operator context~\\cite{Davis1979,Kuchment1993}. "
        "The broader spectral-signing problem was formulated by Bilu and Linial~"
        "\\cite{BiluLinial2006}, and its bipartite case was resolved by Marcus, "
        "Spielman, and Srivastava~\\cite{MarcusSpielmanSrivastava2015}.  Lieb's "
        "flux-phase theorem supplies the physical terminology~\\cite{Lieb1994}. "
        "These sources supply background rather than the counterexample or the "
        "classification results proved here.\n"
    )
    intro_path = PUB_DIR / "sections" / "02_introduction.tex"
    intro = intro_path.read_text(encoding="utf-8")
    marker = "The inherited ingredients"
    intro = intro.replace(marker, related_work + "\n" + marker, 1)
    intro = re.sub(
        r"This theorem is also computer-assisted\..*?zone folding\.\n",
        lambda _match: (
            "This theorem is computer-assisted: a complete exact finite classification "
            "combines closed-walk compression with exact certificates for the residual "
            "competitors.  The full partition and certificate accounting appear in "
            "Section~\\ref{sec:low-period-frontier}.\n"
        ),
        intro,
        flags=re.DOTALL,
    )
    intro = intro.replace(
        "This is a dated and bounded\nsearch statement, not an absolute priority claim.",
        "This is a bounded literature statement, not an absolute priority claim; "
        "the search date and scope are recorded in the reproducibility note.",
    )
    intro_path.write_text(intro, encoding="utf-8")

    body_inputs = "\n".join(rf"\input{{sections/{stem.lower()}}}" for stem in SECTIONS)
    appendix_inputs = "\n".join(rf"\input{{appendices/{stem.lower()}}}" for stem in APPENDICES)
    body = f"{body_inputs}\n\n\\input{{sections/12_data_code_availability}}\n\n\\appendix\n{appendix_inputs}\n"
    write(PUB_DIR / "body.tex", body)
    write(PUB_DIR / "sections" / "12_data_code_availability.tex", DATA_AVAILABILITY)
    write(PUB_DIR / "publication-preamble.tex", PREAMBLE)
    write(PUB_DIR / "frontmatter.tex", FRONTMATTER.replace("__ABSTRACT__", abstract_tex()))
    write(PUB_DIR / "references.bib", BIBLIOGRAPHY)
    write(PUB_DIR / "main.tex", wrapper())
    write(PUB_DIR / "main_anonymous.tex", wrapper(anonymous=True))
    write(PUB_DIR / "main_jgt.tex", wrapper(variant="jgt"))
    write(PUB_DIR / "main_sidma.tex", wrapper(variant="sidma"))
    write(
        PUB_DIR / "README.md",
        """# Target A publication LaTeX

`main.tex` is the generic publication build. `main_anonymous.tex` is the
double-blind build. `main_jgt.tex` and `main_sidma.tex` are lightweight
journal-style wrappers sharing `body.tex`; final official class migration
awaits journal selection and does not duplicate the mathematical body.
Generated section files come from the frozen V2 Markdown source.
""",
    )
    (PUB_DIR / "figures").mkdir(parents=True, exist_ok=True)
    write(PUB_DIR / "figures" / ".gitkeep", "")
    print("TARGET_A_PUBLICATION_LATEX_BUILD_PASS")


if __name__ == "__main__":
    build()

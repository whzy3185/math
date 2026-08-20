"""Convert the frozen Target A Markdown section sources to compilable LaTeX."""

from __future__ import annotations

import re
from pathlib import Path


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
MD_DIR = RESEARCH_ROOT / "paper" / "manuscript_md"
TEX_DIR = RESEARCH_ROOT / "paper" / "manuscript_tex"

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


def _escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in text)


def _mathify(text: str) -> str:
    value = text.strip()
    value = re.sub(r"\^\(([^()]*)\)", r"^{\1}", value)
    value = re.sub(r"_\(([^()]*)\)", r"_{\1}", value)
    value = value.replace("==>", r"\Longrightarrow")
    value = value.replace("<=", r"\le ").replace(">=", r"\ge ")
    value = value.replace("~=", r"\cong ").replace("+-", r"\pm ")
    value = re.sub(r"(?<=\d)\|(?=[A-Za-z])", r"\\mid ", value)
    token_map = {
        "alpha": r"\alpha",
        "eta": r"\eta",
        "lambda": r"\lambda",
        "pi": r"\pi",
        "rho": r"\rho",
        "sigma": r"\sigma",
        "tau": r"\tau",
        "theta": r"\theta",
        "emptyset": r"\varnothing",
        "in": r"\in",
    }
    for token, replacement in token_map.items():
        value = re.sub(
            rf"(?<![A-Za-z]){token}(?![A-Za-z])",
            lambda _match, replacement=replacement: replacement,
            value,
        )
    while "sqrt(" in value:
        start = value.rfind("sqrt(")
        depth = 1
        end = start + len("sqrt(")
        while end < len(value) and depth:
            depth += (value[end] == "(") - (value[end] == ")")
            end += 1
        if depth:
            break
        value = value[:start] + r"\sqrt{" + value[start + len("sqrt(") : end - 1] + "}" + value[end:]
    for operator in ("cos", "det", "diag", "max", "min", "spec", "sup", "tr"):
        value = re.sub(
            rf"(?<![A-Za-z]){operator}(?![A-Za-z])",
            lambda _match, operator=operator: rf"\operatorname{{{operator}}}",
            value,
        )
    value = re.sub(r"(?<![A-Za-z])CT(?![A-Za-z])", lambda _match: r"\operatorname{CT}", value)
    value = re.sub(r"(?<![A-Za-z])product(?![A-Za-z])", lambda _match: r"\prod", value)
    value = re.sub(r"(?<![A-Za-z])sum(?![A-Za-z])", lambda _match: r"\sum", value)
    value = value.replace("direct_sum", r"\bigoplus")
    value = value.replace("#", r"\#")
    return value


def _code_token(text: str) -> str:
    if (
        text.endswith((".json", ".py", ".txt", ".md"))
        or text.startswith(("TARGET_A_", "http", ".venv"))
    ):
        return r"\path{" + text + "}"
    if re.fullmatch(r"[0-9a-f]{32,64}", text):
        return r"\texttt{\detokenize{" + text + "}}"
    if text == "square":
        return r"\(\square\)"
    return r"\(" + _mathify(text) + r"\)"


INLINE_PATTERN = re.compile(
    r"`([^`]+)`|\*\*([^*]+)\*\*|\[([^\]]+)\]\((https?://[^)]+)\)|\[([1-6])\]"
)


def render_inline(text: str) -> str:
    pieces: list[str] = []
    cursor = 0
    for match in INLINE_PATTERN.finditer(text):
        pieces.append(_escape(text[cursor : match.start()]))
        code, bold, label, url, citation = match.groups()
        if code is not None:
            pieces.append(_code_token(code))
        elif bold is not None:
            pieces.append(r"\textbf{" + render_inline(bold) + "}")
        elif label is not None:
            pieces.append(r"\href{" + url + "}{" + _escape(label) + "}")
        else:
            pieces.append(r"\cite{" + CITATIONS[citation] + "}")
        cursor = match.end()
    pieces.append(_escape(text[cursor:]))
    return "".join(pieces)


def _render_table(lines: list[str]) -> list[str]:
    rows = [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in lines]
    rows.pop(1)
    columns = len(rows[0])
    width_score = sum(max(len(row[column]) for row in rows) for column in range(columns))
    resize = columns >= 5 or width_score > 80
    output = [r"\begin{center}"]
    if resize:
        output.append(r"\resizebox{\textwidth}{!}{%")
    output.extend([r"\begin{tabular}{" + "l" * columns + "}", r"\toprule"])
    for index, row in enumerate(rows):
        output.append(" & ".join(render_inline(cell) for cell in row) + r" \\")
        if index == 0:
            output.append(r"\midrule")
    output.extend([r"\bottomrule", r"\end{tabular}%"])
    if resize:
        output.append("}")
    output.append(r"\end{center}")
    return output


def convert_markdown(text: str, appendix: bool = False) -> str:
    lines = text.splitlines()
    output: list[str] = []
    index = 0
    list_kind: str | None = None

    def close_list() -> None:
        nonlocal list_kind
        if list_kind:
            output.append(r"\end{" + list_kind + "}")
            list_kind = None

    while index < len(lines):
        line = lines[index]
        if line.startswith("```"):
            close_list()
            language = line[3:].strip()
            block: list[str] = []
            index += 1
            while index < len(lines) and not lines[index].startswith("```"):
                block.append(lines[index])
                index += 1
            output.append(r"\begin{lstlisting}[language={" + ("bash" if language == "bash" else "") + "}]")
            output.extend(block)
            output.append(r"\end{lstlisting}")
        elif line.startswith("| ") and index + 1 < len(lines) and re.match(r"^\|[-: |]+\|$", lines[index + 1]):
            close_list()
            table = [line, lines[index + 1]]
            index += 2
            while index < len(lines) and lines[index].startswith("|"):
                table.append(lines[index])
                index += 1
            output.extend(_render_table(table))
            continue
        elif line.startswith("# "):
            close_list()
            title = re.sub(r"^# (?:\d+\.\s*|Appendix [A-C]\.\s*)", "", line)
            output.append(r"\section{" + render_inline(title) + "}")
        elif line.startswith("## "):
            close_list()
            title = re.sub(r"^## (?:\d+\.\d+\s*|[A-C]\.\d+\s*)", "", line)
            output.append(r"\subsection{" + render_inline(title) + "}")
        elif line.startswith("### "):
            close_list()
            output.append(r"\subsubsection{" + render_inline(line[4:]) + "}")
        elif re.match(r"^\d+\. ", line):
            if list_kind != "enumerate":
                close_list()
                list_kind = "enumerate"
                output.append(r"\begin{enumerate}")
            output.append(r"\item " + render_inline(re.sub(r"^\d+\. ", "", line)))
        elif line.startswith("- "):
            if list_kind != "itemize":
                close_list()
                list_kind = "itemize"
                output.append(r"\begin{itemize}")
            output.append(r"\item " + render_inline(line[2:]))
        elif not line.strip():
            close_list()
            output.append("")
        else:
            if list_kind and line.startswith("   "):
                output[-1] += " " + render_inline(line.strip())
            else:
                close_list()
                output.append(render_inline(line))
        index += 1
    close_list()
    return "\n".join(output).rstrip() + "\n"


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build() -> None:
    for stem in SECTIONS:
        source = (MD_DIR / f"{stem}.md").read_text(encoding="utf-8")
        _write(TEX_DIR / "sections" / f"{stem.lower()}.tex", convert_markdown(source))
    for stem in APPENDICES:
        source = (MD_DIR / f"{stem}.md").read_text(encoding="utf-8")
        _write(TEX_DIR / "appendices" / f"{stem.lower()}.tex", convert_markdown(source, appendix=True))

    title_source = (MD_DIR / "01_TITLE_AND_ABSTRACT.md").read_text(encoding="utf-8")
    abstract = title_source.split("## Abstract", 1)[1].strip()
    abstract_tex = convert_markdown(abstract).strip()
    section_inputs = "\n".join(rf"\input{{sections/{stem.lower()}}}" for stem in SECTIONS)
    appendix_inputs = "\n".join(rf"\input{{appendices/{stem.lower()}}}" for stem in APPENDICES)
    main = rf"""\documentclass[11pt]{{article}}
\usepackage[margin=1in]{{geometry}}
\usepackage{{amsmath,amssymb,amsthm}}
\usepackage{{booktabs,graphicx}}
\usepackage[hidelinks]{{hyperref}}
\usepackage{{listings}}
\lstset{{basicstyle=\ttfamily\small,breaklines=true,columns=fullflexible,keepspaces=true}}
\emergencystretch=2em
\raggedbottom
\sloppy
\title{{Counterexamples and Flux-Phase Structure for Signed Circulant Graphs}}
\author{{Anonymous manuscript}}
\date{{}}
\begin{{document}}
\maketitle
\begin{{abstract}}
{abstract_tex}
\end{{abstract}}
\tableofcontents

{section_inputs}

\appendix
{appendix_inputs}

\begin{{thebibliography}}{{99}}
\bibitem{{BiluLinial2006}} Y. Bilu and N. Linial, Lifts, discrepancy and nearly optimal spectral gap, \emph{{Combinatorica}} 26 (2006), 495--519.
\bibitem{{Lieb1994}} E. H. Lieb, Flux phase of the half-filled band, \emph{{Physical Review Letters}} 73 (1994), 2158--2161.
\bibitem{{MarcusSpielmanSrivastava2015}} A. W. Marcus, D. A. Spielman, and N. Srivastava, Interlacing families I: Bipartite Ramanujan graphs of all degrees, \emph{{Annals of Mathematics}} 182 (2015), 307--325.
\bibitem{{Suvagiya2026Parity}} V. Suvagiya, Parity families and a kernel-averaged L-function for near-Ramanujan signings, arXiv:2607.17343v1 (2026).
\bibitem{{Suvagiya2026Signed}} V. Suvagiya, Signed circulants at the Ramanujan bound, arXiv:2607.18334v1 (2026).
\bibitem{{XuZhang2026}} Z. Xu and X. Zhang, An improved upper bound for the Bilu--Linial conjecture, arXiv:2606.28797 (2026).
\end{{thebibliography}}
\end{{document}}
"""
    _write(TEX_DIR / "main.tex", main)

    bib = """@article{BiluLinial2006, author={Bilu, Yonatan and Linial, Nathan}, title={Lifts, discrepancy and nearly optimal spectral gap}, journal={Combinatorica}, volume={26}, year={2006}, pages={495--519}}
@article{Lieb1994, author={Lieb, Elliott H.}, title={Flux phase of the half-filled band}, journal={Physical Review Letters}, volume={73}, year={1994}, pages={2158--2161}}
@article{MarcusSpielmanSrivastava2015, author={Marcus, Adam W. and Spielman, Daniel A. and Srivastava, Nikhil}, title={Interlacing families I: Bipartite Ramanujan graphs of all degrees}, journal={Annals of Mathematics}, volume={182}, year={2015}, pages={307--325}}
@misc{Suvagiya2026Parity, author={Suvagiya, Vaibhav}, title={Parity families and a kernel-averaged L-function for near-Ramanujan signings}, eprint={2607.17343}, archivePrefix={arXiv}, year={2026}}
@misc{Suvagiya2026Signed, author={Suvagiya, Vaibhav}, title={Signed circulants at the Ramanujan bound}, eprint={2607.18334}, archivePrefix={arXiv}, year={2026}}
@misc{XuZhang2026, author={Xu, Z. and Zhang, X.}, title={An improved upper bound for the Bilu--Linial conjecture}, eprint={2606.28797}, archivePrefix={arXiv}, year={2026}}
"""
    _write(TEX_DIR / "references.bib", bib)
    print("TARGET_A_LATEX_BUILD_PASS")


if __name__ == "__main__":
    build()

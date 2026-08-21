"""Verify the Chinese manuscript against the frozen English publication source."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
ENGLISH_DIR = RESEARCH_ROOT / "paper" / "manuscript_tex_pub"
CHINESE_DIR = RESEARCH_ROOT / "paper" / "manuscript_tex_pub_zh"
BODY_PARTS = ("sections", "appendices")
ENVIRONMENTS = (
    "equation",
    "theorem",
    "proposition",
    "lemma",
    "proof",
    "table",
    "lstlisting",
)
FORBIDDEN_CHINESE_PHRASES = (
    "带符号循环图",
    "带符号邻接矩阵",
    "带符号图",
    "闭步",
    "极小元",
    "非极小元",
    "记账",
    "生产阶数",
    "生产检查点",
    "躲过这些",
    "惩罚局部",
    "谱平方半径",
    "谱半径平方",
    "谱带值平方",
    "锐正性",
    "独立生成器审计",
    "逻辑指纹",
    "系统拒绝",
    "本原相位认同",
)
EXPECTED_THEOREM_TITLES = (
    "最小反例定理",
    "无限反例族定理",
    "周期八精确谱边定理",
    "周期八相位三分定理",
    "一般周期必要条件定理",
    "低周期谱极值分类定理",
)


class ChineseLatexVerificationError(RuntimeError):
    pass


def check(condition: bool, message: str) -> None:
    if not condition:
        raise ChineseLatexVerificationError(message)


def source_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.tex")
        if not any(part in {"build", "tmp"} for part in path.parts)
    )


def body_text(root: Path) -> str:
    files = [path for path in source_files(root) if path.parent.name in BODY_PARTS]
    return "\n".join(path.read_text(encoding="utf-8") for path in files)


def environment_bodies(text: str, environment: str) -> list[str]:
    return re.findall(
        rf"\\begin\{{{environment}\}}(?:\[[^]]*\])?(.*?)\\end\{{{environment}\}}",
        text,
        flags=re.DOTALL,
    )


def normalized_equation(equation: str) -> str:
    equation = re.sub(r"\\text\{[，。]\}", "", equation)
    equation = re.sub(
        r"[.,;，。](?=\s*\\end\{(?:aligned|cases)\}\s*$)", "", equation
    )
    equation = re.sub(r"\\text\{[^{}]*\}", r"\\text{TEXT}", equation)
    equation = equation.replace(r"\\sum", r"\sum")
    equation = re.sub(r"[.,;，。]\s*$", "", equation.strip())
    return re.sub(r"\s+", "", equation)


def citation_keys(text: str) -> set[str]:
    keys: set[str] = set()
    for group in re.findall(r"\\cite\{([^}]+)\}", text):
        keys.update(item.strip() for item in group.split(","))
    return keys


def table_numeric_tokens(table: str) -> list[str]:
    return re.findall(r"(?<![A-Za-z])\d[\d,]*(?:\.\d+)?", table)


def table_inline_math(table: str) -> list[str]:
    return [
        re.sub(r"\s+", "", item)
        for item in re.findall(r"\\\((.*?)\\\)", table, flags=re.DOTALL)
    ]


def verify_target_a_chinese_latex() -> None:
    check(ENGLISH_DIR.is_dir(), "ENGLISH_PUBLICATION_TREE_MISSING")
    check(CHINESE_DIR.is_dir(), "CHINESE_PUBLICATION_TREE_MISSING")
    english_body = body_text(ENGLISH_DIR)
    chinese_body = body_text(CHINESE_DIR)
    chinese_source_files = source_files(CHINESE_DIR)
    chinese_sources = "\n".join(
        path.read_text(encoding="utf-8") for path in chinese_source_files
    )
    frontmatter = (CHINESE_DIR / "frontmatter.tex").read_text(encoding="utf-8")
    preamble = (CHINESE_DIR / "publication-preamble.tex").read_text(encoding="utf-8")

    check(re.search(r"[\u4e00-\u9fff]", chinese_body) is not None, "CHINESE_TEXT_MISSING")
    check(r"\usepackage{xeCJK}" in chinese_sources, "XECJK_MISSING")
    check("Songti SC" in chinese_sources and "STHeiti" in chinese_sources, "CHINESE_FONTS")
    check("a4paper" in chinese_sources, "A4_LAYOUT_MISSING")
    check(r"\raggedright\sffamily\bfseries" in preamble, "SECTION_NOT_LEFT_ALIGNED")
    check(r"\centering\sffamily\bfseries" not in preamble, "CENTERED_SECTION_HEADING")
    check(r"\sloppy" not in chinese_sources, "SLOPPY_FORBIDDEN")
    check(
        not re.search(r"(?:^|\s)(?:/Users/|/absolute/|/tmp/|file://)", chinese_sources),
        "LOCAL_ABSOLUTE_PATH",
    )
    check("符号循环图的周期八谱结构与反例" in frontmatter, "CHINESE_TITLE")
    check("[作者姓名]" in frontmatter and "[单位]" in frontmatter, "AUTHOR_PLACEHOLDERS")
    check("[院系]" in frontmatter and "[城市]" in frontmatter, "AFFILIATION_PLACEHOLDERS")
    check("[邮编]" in frontmatter and "[通讯作者]" in frontmatter, "CONTACT_PLACEHOLDERS")
    check("[电子邮箱]" in frontmatter and "[ORCID]" in frontmatter, "EMAIL_ORCID_PLACEHOLDERS")
    check("MR(2020)分类号" in frontmatter and "TargetAMRClass" in frontmatter, "MR_INTERFACE")
    check("中图分类号" in frontmatter and "TargetAChineseLibraryClass" in frontmatter, "CLC_INTERFACE")
    check("TargetAFunding" in frontmatter, "FUNDING_INTERFACE")
    check("IncludeEnglishAbstract" in frontmatter, "ENGLISH_ABSTRACT_SWITCH")
    check((CHINESE_DIR / "english-abstract-interface.tex").is_file(), "ENGLISH_ABSTRACT_INTERFACE")
    check("TargetARunningTitle" in preamble, "RUNNING_TITLE_INTERFACE")

    abstract_match = re.search(
        r"\\noindent\\textbf\{摘要：\}(.*?)\\par", frontmatter, flags=re.DOTALL
    )
    check(abstract_match is not None, "CHINESE_ABSTRACT_MISSING")
    abstract_han_length = len(re.findall(r"[\u4e00-\u9fff]", abstract_match.group(1)))
    check(250 <= abstract_han_length <= 350, f"ABSTRACT_LENGTH:{abstract_han_length}")
    check(
        "符号循环图；谱半径；切换等价；通量相；Floquet 理论；闭游走矩；计算机辅助证明"
        in frontmatter,
        "SEVEN_KEYWORDS",
    )

    for phrase in FORBIDDEN_CHINESE_PHRASES:
        check(phrase not in chinese_body and phrase not in frontmatter, f"FORBIDDEN_TERM:{phrase}")
    check("我们" not in chinese_body and "我们" not in frontmatter, "UNNECESSARY_WE")

    for environment in ENVIRONMENTS:
        english_items = environment_bodies(english_body, environment)
        chinese_items = environment_bodies(chinese_body, environment)
        check(
            len(english_items) == len(chinese_items),
            f"ENVIRONMENT_COUNT:{environment}:{len(english_items)}:{len(chinese_items)}",
        )

    english_equations = [
        normalized_equation(item) for item in environment_bodies(english_body, "equation")
    ]
    chinese_equations = [
        normalized_equation(item) for item in environment_bodies(chinese_body, "equation")
    ]
    check(english_equations == chinese_equations, "EQUATION_SEQUENCE_CHANGED")
    check(
        environment_bodies(english_body, "lstlisting")
        == environment_bodies(chinese_body, "lstlisting"),
        "CODE_LISTINGS_CHANGED",
    )

    english_tables = environment_bodies(english_body, "table")
    chinese_tables = environment_bodies(chinese_body, "table")
    for index, (english_table, chinese_table) in enumerate(
        zip(english_tables, chinese_tables), start=1
    ):
        check(
            table_numeric_tokens(english_table) == table_numeric_tokens(chinese_table),
            f"TABLE_NUMERIC_DATA_CHANGED:{index}",
        )
        check(
            table_inline_math(english_table) == table_inline_math(chinese_table),
            f"TABLE_MATH_CHANGED:{index}",
        )

    theorem_titles = tuple(
        re.findall(r"\\begin\{theorem\}\[([^]]+)\]", chinese_body)
    )
    check(theorem_titles == EXPECTED_THEOREM_TITLES, "THEOREM_TITLES")
    critical_fragments = (
        r"8\leq n\leq 30",
        r"n=32",
        r"8\mid n",
        r"n\geq 32",
        r"\frac{1561}{200}",
        r"p\leq16",
        "2,626",
        "2,611",
    )
    for fragment in critical_fragments:
        check(fragment in chinese_body or fragment in frontmatter, f"CRITICAL_SCOPE:{fragment}")
    partition = next(
        equation
        for equation in environment_bodies(chinese_body, "equation")
        if "2611" in equation and "2626" in equation
    )
    for count in ("2611", "8", "5", "2", "2626"):
        check(count in partition, f"PARTITION_COUNT:{count}")

    english_labels = set(re.findall(r"\\label\{([^}]+)\}", english_body))
    chinese_labels = set(re.findall(r"\\label\{([^}]+)\}", chinese_body))
    check(english_labels == chinese_labels, "LABEL_SET_CHANGED")
    check(citation_keys(english_body) == citation_keys(chinese_body), "CITATION_SET_CHANGED")
    check(
        (ENGLISH_DIR / "references.bib").read_bytes()
        == (CHINESE_DIR / "references.bib").read_bytes(),
        "BIBLIOGRAPHY_METADATA_CHANGED",
    )

    labels = set(re.findall(r"\\label\{([^}]+)\}", chinese_sources))
    refs = set(re.findall(r"\\(?:ref|eqref|cref|Cref)\{([^}]+)\}", chinese_sources))
    check(refs <= labels, f"UNRESOLVED_SOURCE_REFS:{sorted(refs - labels)}")
    bib_keys = set(
        re.findall(
            r"@[A-Za-z]+\{([^,]+),",
            (CHINESE_DIR / "references.bib").read_text(encoding="utf-8"),
        )
    )
    check(
        citation_keys(chinese_sources) <= bib_keys,
        "UNRESOLVED_SOURCE_CITATIONS",
    )

    audit_path = CHINESE_DIR / "build_audit.json"
    check(audit_path.is_file(), "BUILD_AUDIT_MISSING")
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    check(
        audit.get("status") == "TARGET_A_CHINESE_PUBLICATION_BUILD_PASS",
        "BUILD_AUDIT_STATUS",
    )
    pdf = CHINESE_DIR / str(audit.get("pdf"))
    check(pdf.is_file() and pdf.read_bytes().startswith(b"%PDF-"), "PDF_MISSING")
    check(hashlib.sha256(pdf.read_bytes()).hexdigest() == audit.get("pdf_sha256"), "PDF_HASH")
    check(audit.get("page_format") == "A4", "PDF_PAGE_FORMAT")
    check(audit.get("exit_code") == 0, "BUILD_EXIT")
    check(audit.get("overfull_boxes") == 0, "OVERFULL_BOX")
    check(audit.get("undefined_references") == 0, "UNDEFINED_REFERENCE")
    check(audit.get("undefined_citations") == 0, "UNDEFINED_CITATION")
    check(audit.get("fatal_errors") == 0, "FATAL_LATEX")

    english_pdf_hash = hashlib.sha256((ENGLISH_DIR / "main.pdf").read_bytes()).hexdigest()
    check(audit.get("english_source_pdf_sha256") == english_pdf_hash, "ENGLISH_PDF_CHANGED")

    print("TARGET_A_CHINESE_MATH_STRUCTURE_PASS")
    print(f"TARGET_A_CHINESE_ABSTRACT_LENGTH_PASS:{abstract_han_length}")
    print("TARGET_A_CHINESE_TERMINOLOGY_PASS")
    print("TARGET_A_CHINESE_FRONTMATTER_PASS")
    print("TARGET_A_CHINESE_TABLE_NUMERIC_PASS")
    print("TARGET_A_CHINESE_LABEL_CITATION_PASS")
    print("TARGET_A_CHINESE_LISTING_BIBLIOGRAPHY_PASS")
    print("TARGET_A_CHINESE_BUILD_ARTIFACT_PASS")
    print("TARGET_A_CHINESE_LATEX_GATE_PASS")


def main() -> None:
    try:
        verify_target_a_chinese_latex()
    except Exception as error:
        print(f"Target A Chinese LaTeX verification failed: {error}", file=sys.stderr)
        print("TARGET_A_CHINESE_LATEX_GATE_FAIL")
        raise SystemExit(1)


if __name__ == "__main__":
    main()

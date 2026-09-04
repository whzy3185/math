#!/usr/bin/env python3
"""Deterministic structural checks for the bilingual manuscript."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent


def joined(language):
    return "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted((ROOT / f"sections_{language}").glob("*.tex"))
    )


def groups(pattern, text):
    return set(re.findall(pattern, text))


english = joined("en")
chinese = joined("zh")

english_labels = groups(r"\\label\{([^}]+)\}", english)
chinese_labels = groups(r"\\label\{([^}]+)\}", chinese)
assert english_labels == chinese_labels

for language, text in (("en", english), ("zh", chinese)):
    references = groups(r"\\(?:ref|eqref|cref)\{([^}]+)\}", text)
    assert not references - groups(r"\\label\{([^}]+)\}", text)
    assert len(re.findall(r"\\section\{", text)) == 6
    assert "PLACEHOLDER" not in text
    assert "TODO" not in text

bib_text = (ROOT / "references.bib").read_text(encoding="utf-8")
bib_keys = set(re.findall(r"^@\w+\{([^,]+),", bib_text, re.M))
assert len(bib_keys) == 14

for text in (english, chinese):
    citation_keys = set()
    for citation_group in re.findall(r"\\cite\{([^}]+)\}", text):
        citation_keys.update(key.strip() for key in citation_group.split(","))
    assert citation_keys == bib_keys

frontmatter = (ROOT / "frontmatter_en.tex").read_text(encoding="utf-8")
abstract = re.search(
    r"\\begin\{abstract\}(.*?)\\end\{abstract\}", frontmatter, re.S
).group(1)
plain_abstract = re.sub(r"\\[A-Za-z]+(?:\{[^{}]*\})?", " ", abstract)
plain_abstract = re.sub(r"[^A-Za-z0-9-]+", " ", plain_abstract)
assert len(plain_abstract.split()) <= 250

required_phrases = (
    r"\tau_{i+m}=-\tau_i",
    r"\gamma_m(z)^2=(-1)^m z^{-1}",
    r"4+\sqrt{10+2\sqrt5}",
    r"(k,E_k)=(4,5504)",
    r"M_3=118p+168d+96a+48b",
)
all_sources = "\n".join(
    path.read_text(encoding="utf-8")
    for path in ROOT.rglob("*.tex")
)
for phrase in required_phrases:
    assert phrase in all_sources

print("BILINGUAL_MANUSCRIPT_STRUCTURE_CHECK_PASS")

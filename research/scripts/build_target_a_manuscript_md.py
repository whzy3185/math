"""Build the merged Target A Markdown manuscript from section sources."""

from __future__ import annotations

import argparse
from pathlib import Path


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = RESEARCH_ROOT / "paper" / "manuscript_md"
DEFAULT_OUTPUT = SOURCE_DIR / "TARGET_A_MANUSCRIPT_V2.md"
SECTION_STEMS = [
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
    "12_APPENDIX_ORBIT_COMPLETENESS",
    "13_APPENDIX_EXACT_CERTIFICATES",
    "14_APPENDIX_COMPUTATION",
    "15_REFERENCES",
]


def build_manuscript() -> str:
    title_source = (SOURCE_DIR / "01_TITLE_AND_ABSTRACT.md").read_text(encoding="utf-8")
    abstract = title_source.split("## Abstract", 1)[1].strip()
    front_matter = (
        "# Counterexamples and Flux-Phase Structure for Signed Circulant Graphs\n\n\n"
        + abstract
    )
    sections = [front_matter] + [
        (SOURCE_DIR / f"{stem}.md").read_text(encoding="utf-8").rstrip()
        for stem in SECTION_STEMS
    ]
    return "\n\n".join(sections) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    args.output.write_text(build_manuscript(), encoding="utf-8")
    print(f"TARGET_A_MANUSCRIPT_BUILD_PASS:{args.output}")


if __name__ == "__main__":
    main()

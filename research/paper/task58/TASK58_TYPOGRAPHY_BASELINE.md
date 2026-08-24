# Task 58 Typography Baseline

Status: `TASK58_3_CLEAN_BUILD_PASS`.

## Submission-template decision

The Journal of Graph Theory author guidance was rechecked on 2026-08-24. It
accepts a LaTeX main document, requires a compiled PDF for peer review, and
strongly recommends Wiley's current LaTeX authoring template. Wiley's current
template page also says that production converts accepted files to the
journal's final specifications and advises standard LaTeX coding without
custom fonts or elaborate layout. The downloadable Wiley class was not
vendored into the approved repository checkpoint. Task 58.3 therefore uses a
traditional, stable mathematics `article` setup and records this choice rather
than guessing class options or imitating publisher typography.

Sources checked:

- <https://onlinelibrary.wiley.com/page/journal/10970118/homepage/forauthors.html>
- <https://authors.wiley.com/author-resources/Journal-Authors/Prepare/new-journal-design.html>

Migration to an official class, if required at submission, is an
infrastructure-only operation and may not change mathematical prose.

## Baseline specification

| Item | Task 58.3 baseline |
|---|---|
| Document class | Standard `article`, 11 pt, one column |
| Template provenance | Stable mathematics fallback; Wiley/JGT guidance checked as above |
| Body font | Latin Modern through `lmodern` with T1 encoding |
| Mathematics font | Latin Modern/AMS through `amsmath`, `amssymb`, and `mathtools` |
| Geometry | `geometry`, one-inch margins on US Letter |
| Text block | 6.5 by 9 inches |
| Theorem package | `amsthm`; plain theorem/proposition/lemma/corollary styles |
| Caption package | None at scaffold stage |
| Figure packages | `graphicx` and monochrome `tikz` |
| Bibliography | BibTeX with `plain`; local `references.bib` |
| Hyperlinks | `hyperref` with hidden link decoration; `cleveref` |
| Compiler | Tectonic 0.17.0 (XeTeX-based) |
| Build command | `tectonic main.tex` and `tectonic main_anonymous.tex` |
| Build warnings | None in the final Task 58.3 builds |

## Render review

Both entry points compile to four US-Letter pages at the scaffold stage. The
identified-author PDF was rendered to PNG at 110 dpi and pages 1, 2, and 4 were
inspected. The title, abstract measure, serif text/math baseline, section and
subsection hierarchy, margins, and page numbers are coherent. The theorem and
equation spacing will be inspected again once those environments first contain
mathematical content. The initial empty-body render exposed a forced stack of
headings; invisible draft paragraphs now permit normal page breaks without
adding visible placeholder prose. No overlap, clipped heading, blank interior
page, decorative theorem box, or publisher-font imitation remains.

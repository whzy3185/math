# Task 58 manuscript

This directory contains the first-submission manuscript source for
`Spectral Radius Minimization for Signed Squares of Cycles`.

Build the identified-author and anonymous versions from this directory with:

```sh
tectonic main.tex
tectonic main_anonymous.tex
```

A conventional full TeX installation may instead use:

```sh
latexmk -pdf main.tex
latexmk -pdf main_anonymous.tex
```

Both entry points share `publication-preamble.tex`, `frontmatter.tex`, and
`body.tex`. The bibliography is `references.bib`. The compiled Task 58.11
checkpoint is 38 pages for `main.pdf` and 38 pages for
`main_anonymous.pdf`; both builds are warning-free under Tectonic 0.17.0.

The separate reproducibility supplement is in the sibling directory
`../manuscript_tex_task58_supplement/`. It contains the full exact-`2r`
proof, complete single-gap integer witnesses, and the repository artifact
manifest.

The historical English and Chinese manuscript trees are separate frozen
artifacts and are not imported into this manuscript's mathematical prose.

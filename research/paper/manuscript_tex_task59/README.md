# Task 59 submission revision

This directory contains the submission-stage editorial revision of
`When Is the Twisted Signing of an Even Cycle Square Spectrally Optimal?`.
The frozen Task 58 source remains in
`research/paper/manuscript_tex_task58/`.

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
`body.tex`. The bibliography is `references.bib`. The compiled Task 59
checkpoint is 37 pages for `main.pdf` and 37 pages for
`main_anonymous.pdf`; both builds are warning-free under Tectonic 0.17.0.

The separate reproducibility supplement is in the sibling directory
`../manuscript_tex_task59_supplement/`. It contains the full exact-`2r`
proof, complete single-gap integer witnesses, and the repository artifact
manifest.

The historical English and Chinese manuscript trees are separate frozen
artifacts and are not imported into this manuscript's mathematical prose.

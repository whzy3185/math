# Task 58 manuscript scaffold

This directory is the clean first-submission LaTeX tree for Task 58. It does
not import mathematical prose from an earlier manuscript.

Build the identified-author version from this directory with the preferred
full TeX installation:

```sh
latexmk -pdf main.tex
```

The Task 58.3 baseline was built with the locally available Tectonic engine:

```sh
tectonic --keep-logs --keep-intermediates main.tex
```

Build the anonymous version with:

```sh
latexmk -pdf main_anonymous.tex
```

Both entry points share `publication-preamble.tex`, `frontmatter.tex`, and
`body.tex`. `references.bib` is a mechanical copy of the bibliography database
from the frozen English publication tree; no old mathematical prose is
imported. Draft bodies are
identified by the exact marker `% TASK58_DRAFT_STUB`; the final manuscript
audit must find no remaining markers.

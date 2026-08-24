# Task 59 supplementary material

This directory is an independent LaTeX source tree for the supplementary
material accompanying `When Is the Twisted Signing of an Even Cycle Square
Spectrally Optimal?`.

## Contents

- `sections/01_exact_2r.tex`: the full separated-interface exact-`2r`
  theorem, including patch identification, Gram control, the codimension-`2r`
  complement, exact counting, and the `2r`-dimensional Feshbach equation.
- `sections/02_single_gap.tex`: every integer witness vector, its exact
  `A_g v` image, squared norms, rational quotient, and strict margin used in
  the abnormal single-gap hierarchy.
- `sections/03_g6_rational_enclosures.tex`: raw outward rational enclosures
  used by the human-readable Appendix A sign arguments.
- `sections/03_reproducibility.tex`: source states, certificate families,
  one-command verification, evidence boundaries, and archive status.

The evidence checkpoint is `e365e1553ad73a8a534fb67f5ee76562521609ce`;
the submission source is tagged `target-a-task59-submission-v1`. An immutable
external archive and persistent identifier are pending.

## Build

With a standard TeX Live installation:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main_anonymous.tex
```

The compiled identified and anonymous supplements are both 12 pages and
warning-free under Tectonic 0.17.0.

Alternatively, run `pdflatex` twice:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

No bibliography processor is required. The Task 58.11 checkpoint was built
successfully with Tectonic 0.17.0:

```sh
tectonic main.tex
```

The compiled `main.pdf` is included in this tree.

# Research note and Chinese abstract

The six-page note presents the general neighborhood-union compression theorem, the exact Hall ratio rho(M6)=10/3, and the complete classification of its equality subsets into 199 ambient-automorphism orbits. The proofs are explicitly computer-assisted where they use finite certificates and exact enumeration. No publication-priority, proof-assistant, or global asymptotic claim is made.

Deliverables:

- `mycielski_hall_note.tex`: editable manuscript source
- `output/pdf/mycielski_hall_note.pdf`: compiled and visually verified six-page PDF, including a Chinese abstract
- `chinese_abstract.md`: standalone Chinese abstract with the layer counts and scope distinction

The independently audited mathematical programs and certificates remain in the sibling `mycielski_pilot` and `mycielski_strengthening` packages. They are not duplicated here.

## Build

Requires XeLaTeX, standard LaTeX mathematical packages, Latin Modern fonts, and Noto Serif CJK SC for Chinese text.

```
bash build.sh
```

On a standard TeX installation, two XeLaTeX passes suffice. The build helper includes a workspace-local fallback for an incomplete TeX format database using an already installed TeX Live tree. It does not install packages or alter system configuration.

Generated format files, caches, auxiliary files, logs, and rendered page images are excluded from the publication manifest. The PDF has been compiled, its text extracted, and all six rendered pages visually inspected. See `VALIDATION.md`.

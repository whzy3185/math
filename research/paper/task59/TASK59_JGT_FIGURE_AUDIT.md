# Task 59 JGT Figure Audit

Baseline: `80e3d948f462c5dadaa0a4d1d0552b5a37aca0d9`.

## Figure inventory

| Figure | File | Section | Mathematical purpose | Old weakness | Revision | JGT precedent type | 100% readability | Grayscale safety | Caption words | Supported result | PDF page identified / anonymous |
|---:|---|---|---|---|---|---|---|---:|---|---|
| 1 | `figures/figure_cycle_switching.tex` | 2 | Display `C_8^2` and its seam-free Hamilton-gauge coordinates | The old linear path did not reveal the cyclic graph | Full eight-vertex cycle square with solid step-one edges, dashed step-two edges, and a separate local flux panel | Structural graph and coordinate figure | PASS | PASS | 6 | Hamilton gauge, candidate setup, local `Q_i` coordinate | 6 / 6 |
| 2 | `figures/figure_reference_g6.tex` | 4 | Compare the period-eight positive-`Q` lattice with the bilateral `B_0`-to-`B_2` six-gap interface | Reference, defect, residue closure, charge, and sector data were crowded into one figure | Separate bulk/defect figure with the true `4,4,6,4,4` gap sequence and only `q=2`, `B_0 -> B_2` | Signed building block and local replacement figure | PASS | PASS | 10 | Reference edge and G6 essential-spectrum/matching setup | 9 / 9 |
| 3 | `figures/figure_residue_rings.tex` | 6 | Show one, two, and three separated G6 cores closing residues `2,4,6 mod 8` | Three rings shared space with the reference and sector diagrams | Three equal rings with thick defect arcs; charge is stated once and sector compatibility remains in prose | Extremal configuration family | PASS | PASS | 7 | Admissible residue constructions | 15 / 15 |
| 4 | `figures/figure_patch_localization.tex` | 6 | Identify `W_R^+` on a finite ring with a bilateral G6 patch while keeping `e_alpha` outside | The old figure contained several prose labels and could float into the proposition proof | Proof-local configuration using only `W_R`, `W_R^+`, `G6`, `e_alpha`, `B_0`, and `B_2`; figure source precedes Proposition 6.1 | Proof-local configuration diagram | PASS | PASS | 11 | Finite-ring patch identification | 15 / 15 |

## Rendered checks

- Builds inspected: identified and anonymous main manuscripts.
- Regression builds: identified and anonymous supplements.
- Main page inventory: `37 / 37`; supplement inventory: `12 / 12`.
- Inspection mode: full-page grayscale PNG at 180 dpi, corresponding to a
  stricter view than ordinary 100% PDF display.
- Minimum figure text: `\footnotesize`; no `\tiny` text is used.
- Overlap, clipping, text beyond margins, broken panels, and unreadable line
  encodings: none.
- Figure 3 and Figure 4 share page 15 after the final prose pass, retain
  distinct visual hierarchy, and remain before Proposition 6.1 without
  interrupting its proof.

## Deliberate exclusions

No proof-architecture flowchart was added because it would visualize the
paper's narrative rather than a mathematical object. No numerical spectral
plot was added because the paper's spectral decisions are algebraic and such
a plot would not support a proof step. No software or certificate diagram was
added because reproducibility belongs to the supplement and machine-readable
manifest, not the mathematical figure sequence.

## Mathematical boundary

The figure pass changes no theorem statement, classification order, constant,
inequality, quantifier, certificate, or proof dependency. Captions identify
objects only; all mathematical explanations remain in the surrounding prose.

# Integrity report: JGT authorial rewrite

## Verdict

**PASS**, subject only to the author-owned submission metadata listed in
`AUTHOR_AND_SUBMISSION_QUESTIONS.md`.

## Mathematical scope

- exact positive-holonomy radius: `L>=1`;
- strict twisted comparison: `L>=4`;
- negative holonomy: exact analytic formula, not a Lean claim;
- chiral iff: restricted to the natural monomial half-cell class;
- minimal period: primitive periodic words;
- rigidity: dihedral orbits of legal period-eight `Q`-words;
- two `tau` lifts: stated separately from the `Q` orbit;
- global minimum: only an upper bound, never an equality claim.

All frozen mathematical statements are unchanged.

## Proof transparency repairs

- printed `UV`, `tr(UV)`, and `det(UV)` before the quartic;
- renamed dispersion indices to `epsilon,delta`, block scalar to `h`, and
  twisted phase to `theta`;
- proved band separation by explicit positive inequalities;
- displayed the local nine-displacement row of `A_tau^2`;
- derived `M3` from four closed-step support classes;
- justified the short-period survivor table by parity and cyclic gaps;
- packaged the three period-eight integer excesses in a lemma;
- retained every exact Rayleigh vector in the body.

## Narrative and style

- Introduction rebuilt from the fixed-graph question rather than definitions;
- threshold 8 established before “sub-eight” is used;
- general chiral theorem followed by flux interpretation and period-two limit;
- minimal period and rigidity presented as two successive questions;
- repeated Section 6 merged into Section 5;
- theorem/proposition/lemma/proof optional bracket titles removed;
- section-by-section roadmap and repository-management prose removed;
- Hu--Liu cameo citation removed; bibliography now has 14 functional entries;
- equation-only half-cell figure removed; Figure 1 half-cell orientation and
  triangle-flux chord styles corrected.

## Verification population

| check | result |
|---|---|
| bilingual section/label/citation structure | PASS |
| canonical reference library | PASS: 30 rows, 14 cited, 10 JGT corpus, 6 reserve |
| exact finite edge and full dispersion | PASS |
| minimal-period certificates | PASS |
| symmetry and chiral criterion | PASS |
| general-period moments | PASS |
| period-eight structural mechanism | PASS |
| English and Chinese LaTeX builds | PASS |
| unresolved references / layout overflow | none after final build |

The Lean tree remains frozen and was not modified.

# Reserve and excluded references

## Verified reserve

These are real and potentially useful, but they are not currently cited.

| ID | work | reason not in the 14-entry core |
|---|---|---|
| `V001` | Belardo--Brunetti (2024), limit points for signed spectral radii | duplicates the broad signed-radius programme role already covered; no direct period-eight or fixed-support theorem |
| `V002` | Brunetti--Trevisan (2026), unbalanced signed-radius limit points | current but outside the exact fixed-graph mechanism; recency alone is not a reason to cite |
| `V003` | Kuchment--Vainberg (2006), locally perturbed periodic graph operators | relevant to abandoned interface/G6 work, not to the present purely periodic article |
| `V004` | Lin--Ning (2021), complete Cvetković--Rowlinson solution | valuable JGT architecture precedent but not topical evidence for a claim in the paper |
| `V005` | Goedgebeur--Schaudt (2018), exhaustive generation | older computation-architecture precedent superseded by the recent JGT corpus; the present proof is not an exhaustive graph generator |

## Excluded from the current bibliography by scope

- R2/R4/R6/G6 and phase-slip/operator-interface literature;
- all-even classification references assembled for superseded manuscripts;
- generic numerical linear algebra references not used by the analytic proof;
- generic AI, Lean, or computer-assisted-proof literature;
- JGT articles used only to imitate section count or prose structure;
- repeated signed-graph surveys with no distinct role;
- papers whose only connection is the word “Floquet” or “chiral.”

## Promotion rule

A reserve item may enter the manuscript only if a new sentence creates a
specific citation need that the existing core does not cover.  Promotion
requires:

1. exact metadata revalidation;
2. a new row in `CLAIM_REFERENCE_MAP.md`;
3. synchronized BibTeX files;
4. a rerun of `verify_reference_library.py` and the manuscript integrity gate.

Referee requests should be assessed by mathematical relevance, not accepted as
automatic bibliography expansion.

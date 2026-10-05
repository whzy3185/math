# R2 terminal Schur reduction: verified partial formalization

**PASS**, 5 October 2026. This is an eight-theorem increment on the frozen 246-theorem checkpoint. It formalizes the terminal block reduction, not the full R2 analytic family theorem.

## Exact dimensions and definitions

All matrices are over the reals. The pivot X, responses W and E, and terminal H are 4-by-4. The head G is 2-by-2; C and R are 2-by-4. The retained boundary B is 6-by-6 and the coupling T is 6-by-4:

```text
B = [[G,C],[C^T,H]],       T = [R;(W+E)^T].
M_terminal = [[X,T^T],[T,B]],     S = B - T X^-1 T^T.
```

The source uses actual `Fin 2`, `Fin 4`, `Fin 6` and `Fin 10` types. Explicit finite equivalences put the retained head pair before the retained terminal four sites, and put the eliminated pivot first in the 10-by-10 matrix.

`r2_terminal_posDef_iff` proves, from `X.PosDef` alone,

```text
M_terminal.PosDef iff S.PosDef.
```

Strict positivity is derived from Mathlib's Schur semidefinite criterion, its block invertibility equivalence, and the characterization of a positive definite matrix as positive semidefinite and invertible. There is no new positivity axiom.

## Terminal corrections proved

The complete core is expanded as

```text
G' = G - R X^-1 R^T,
C' = C - R X^-1 (W+E),
H' = H - (W+E)^T X^-1 (W+E).
```

The lower-left block is proved to be `(C')^T` under the positive-pivot hypothesis. Separate equalities verify

```text
C' = (C - R X^-1 W) - R X^-1 E,
H' = H - W^T X^-1 W - W^T X^-1 E
       - E^T X^-1 W - E^T X^-1 E.
```

Thus the off-diagonal linear correction, both H cross terms, and the fixed terminal quadratic term are explicit. `r2_terminal_EPlus_posDef_iff` specializes the result to the actual R2 matrix

```text
E_plus = [[-1,0,0,0],[0,1,0,0],[-1,2,1,0],[2,-1,0,-1]].
```

## Verification

- `lake build TargetA.R2TerminalSchur`: exit 0 at 09:32:17 UTC, 8,706 jobs
- `lake env lean R2TerminalAxiomAudit.lean`: exit 0 at 09:36:13 UTC
- The audit covers all 254 theorem declarations, including the unchanged period-eight work
- Axiom union: `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx` or project-specific axiom
- Source scan: no `sorry`, `admit`, axiom declaration, `unsafe`, `native_decide`, or kernel-skipping directive

Use official Lean 4.33.1 and Mathlib `0df444a360eaa60ab8c11dca51a86af692955474`, with the configuration from the preceding 246 checkpoint. Copy the two files in `formal/` into that checkpoint or apply the incremental patch, then run the two commands above. This package is incremental: it does not repeat the preceding checkpoint's unchanged source files. Logs and SHA-256 manifests are included.

## Remaining obligations

The hypothesis `X.PosDef` is an explicit local pivot premise. This module does not prove positivity of the full pivot orbit, the graph-to-block identification, the rational n=106 seed certificate, local contraction, response decay, infinite Schur tails, or all-length R2 positivity. The existing R2/R4/R6 family results remain analytic/certificate-assisted results until those additional dependencies are formalized. The reviewed manuscript need not be revised for this isolated addendum.

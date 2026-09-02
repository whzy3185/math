# Line audit of the residue-two tail draft

## Scope

This audit examines only the proposed analytic tail from the exact response
entrance to the cyclic boundary core.  It does not certify the all-even
classification or any nonzero residue other than two.

## Findings

| Check | Verdict | Evidence / required repair |
|---|---|---|
| Exact response recurrence | PASS | The terminal rule `W_final = W_propagated + E_terminal` is reconstructed and agrees with direct rational Schur elimination at six orders. |
| Orientation of response metric | REPAIRED | Row responses require `L Q L^T`, not only `L^T P L`. The dual rational matrix `Q` is now checked and the local perturbation statement records the Q-norm as well. |
| Bulk entrance into local ball | PASS | `X_12=Phi^12(D)` is exact; the local self-map proof applies from that point. |
| Response entrance | PASS | Exact bounds after 24 block eliminations are checked with Fraction-LDL. |
| Seed positivity | PASS | `S_410-9I/20` is positive definite by exact fixed-core LDL. |
| Tail indexing | PASS | The open-chain sequences are length-independent; the terminal is at `j=m-1`, and `m=2k` makes its coupling parity fixed. At `m=102` this leaves 38 complete two-cell transfers after the 24-step entrance. The exact index verifier checks this arithmetic. |
| Tail constants | OPEN | The draft separates the linear terminal cross term, quadratic Schur series, and pivot error, but it does not yet provide an explicit term-by-term majorant for the pivot-inverse differences. |
| Limit parity | PASS | The proof records that `m=2k` is even and therefore one fixed terminal parity defines the limiting core. |
| Two-cell Loewner monotonicity | REJECTED | Numerical diagnostic of `S_{m+2}-S_m` has both positive and negative eigenvalues from the first tested order onward. A one-sided monotone-core proof is unavailable; retain the response/pivot majorant route. |

## Promotion rule

No numerical comparison of `S_250`, `S_410`, or larger cores can discharge
the tail proof.  The current internal derivation is analytic, but manuscript
promotion still requires an independent human line audit of the recurrence
reindexing and all displayed norm constants.

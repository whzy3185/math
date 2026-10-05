# R2 normalized n=106 seed datum: verified finite certificate

**PASS**, 5 October 2026 at 09:49:29 UTC.

This ten-theorem increment verifies the finite positive-definiteness certificate for the explicitly recorded six-by-six rational seed datum. It does not yet identify that datum with the result of graph elimination or the R2 recurrence inside Lean. The earlier 254-theorem terminal-Schur checkpoint is unchanged.

## Exact certified statement

```lean
TargetA.r2_seed106_margin_posDef :
  (TargetA.r2Seed106Core - (1/50 : ℝ) • (1 : Matrix (Fin 6) (Fin 6) ℝ)).PosDef
```

There are no numerical hypotheses in this theorem. `r2Seed106Core` is the explicit rational matrix recorded in `certificates.seed_106_core`, cast entrywise to the reals. It uses the normalized six-dimensional n=106 datum and margin `1/50`, not the older, differently normalized eight-dimensional seed.

## Certificate checked in Lean

For the rational core S, an explicit unit-lower-triangular matrix L and diagonal D are embedded in the source. Lean verifies:

1. `S - (1/50)I = L diagonal(D) L^T` exactly over the rationals
2. All six entries of D are strictly positive
3. L is lower triangular and every diagonal entry is one
4. After rational-to-real transport, `det(L)=1`, so L is invertible
5. Positive diagonal congruence gives the stated strict positive-definite margin

The large rational identity and pivot inequalities use kernel-checked exact arithmetic. Finite triangularity and unit-diagonal facts use ordinary decidable proofs. There is no floating-point eigenvalue, solver tolerance, native-computation oracle, or externally assumed LDL equality.

The independently reconstructed rational factors match all six recorded `seed_106_pivots`. The exact matrix, factors and pivots are in `data/seed106_ldl.json`. `data/source_provenance.json` records the source-file SHA-256, selected fields and canonical core hash. The source-data match and the formal positive-definiteness proof are distinct checks.

## Fresh execution

- `lake build TargetA.R2Seed106Certificate`: exit 0 at 09:48:03 UTC, 8,707 dependency/build jobs
- `lake env lean R2Seed106AxiomAudit.lean`: exit 0 at 09:49:29 UTC
- Full audit: 264 theorem declarations, including all unchanged period-eight and R2 terminal work
- Exact axiom union: `propext`, `Classical.choice`, `Quot.sound`
- No `sorryAx`, project-specific axiom or extra computation axiom appears
- Source scan: no `sorry`, `admit`, axiom declaration, `unsafe`, `native_decide`, or kernel-skipping directive

The proof source is approximately 15 KB; compiled objects are not needed in this source package. Non-fatal style diagnostics remain in the logs.

## Reproduction

This is an incremental package on the 254-theorem R2 terminal checkpoint. Keep the preceding sources unchanged, copy the two files under `formal/` or apply `r2_seed106_increment.patch`, and run the two commands above. Use official Lean 4.33.1 and Mathlib `0df444a360eaa60ab8c11dca51a86af692955474` with the previously verified pinned configuration. The patch is dry-run checked, and SHA-256 manifests cover the new files and the complete source state.

## Remaining R2 obligations

The formal statement proves positivity of the recorded datum itself. It does not prove that the R2 recurrence produces this datum as S26, or that the recurrence is the raw signed graph's normalized Schur reduction. The pivot entrance, local Riccati contraction, response decay, infinite tails and their two-error seed transfer, remaining finite base cases, and all-length R2 positivity are still separate obligations. The full R2/R4/R6 family results remain analytic/certificate-assisted rather than fully formalized. This isolated addendum does not require changing the reviewed manuscript's accurately labeled checkpoint.

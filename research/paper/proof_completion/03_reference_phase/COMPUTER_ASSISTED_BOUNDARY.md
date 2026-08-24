# Computer-Assisted Boundary

## Logical status

**NONE REQUIRED FOR THIS THEOREM.**

The theorem is proved by displaying the fiber, its determinant, and the exact
positive identity (3) in `FULL_PROOF.md`. Every implication from those
expressions is elementary algebra and spectral theory.

## Optional verification

Computer algebra was used historically to discover and audit the determinant
and the expansion, but a reader may verify both by direct symbolic
multiplication and substitution. The independent artifact

```text
research/audit/period8_floquet_independent_audit.json
```

is reproducibility evidence, not a logical premise.

## Exact finite object

The only finite object is the explicitly printed `8 x 8` Laurent matrix.
The finite verification consists of the polynomial identity
`det(xI-A_ref(z))` and the substitution identity for
`P(eta+u,2-t)`. Neither uses floating-point arithmetic, interval claims, or
unpublished data.

## What is not claimed

- No arbitrary-period minimization theorem follows from this computation.
- The finite negative-holonomy ring need not attain `eta`.
- The proof concerns the squared band edge; it does not choose a sign of the
  unsquared extremal eigenvalue.

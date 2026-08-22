# Target A Multi-Slip Effective Theory

Widely separated `r=2,3,4` G6 configurations produce clusters of `r` positive
interface-derived levels.  Projecting defect delta seeds into each positive
cluster and orthonormalizing gives an effective squared matrix whose spectrum
reconstructs the full selected cluster to at worst `9e-15`.

At defect count 64 (`n=262` for residue six):

```text
three G6: 7.905374884723909
single G10: 7.977104370400552
difference: -0.071729485676643.
```

The Task 49 `n=510` record independently gives `7.905369311653343` for three
G6.  Thus three separated `+2` slips robustly beat G10 in the tested large
rings.  G10 should no longer be treated as the fundamental residue-six
excitation.

The two-slip shift at the Task 51 spacing is below `1e-12` and is classified
`BELOW_DOUBLE_RESOLUTION`.  Consequently neither pairwise sufficiency nor a
genuine three-/four-body remainder is inferred from the FP64 residuals.
High-precision multi-interface Evans arithmetic is required.  The two-path
formula `T(L)+alpha T(M-L)` remains a promising explanation of mod16, but its
orientation matrices and signs have not been derived.

Status: `THREE_G6_REFRAME_STRONG`; pairwise and many-body status `UNRESOLVED`.

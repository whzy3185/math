# Fixed-r Global Spectral Cap

Let a legal ring contain `r=1,2,3` G6 interfaces and otherwise period-eight
bulk, with minimum interface separation `D>=26`. Set
`R=floor((D-9)/4)`.

For a normalized vector `x`, apply the cyclic IMS partition. Each localized
vector `chi_j x`, after the explicit equivalence from the patch
classification, is compactly supported in either the period-eight bulk or a
single forward/reflected G6 operator. Their spectral upper edges are
`eta<c6` and `c6`, respectively. Consequently

```text
sum_j <chi_j x,H chi_j x> <= c6 sum_j ||chi_j x||^2=c6.
```

The exact IMS lemma supplies the only error. Taking the supremum over unit
vectors gives, for both holonomies,

```text
rho(A_ring)^2 <= c6+576/R^2.
```

For `D>=26`, `R>=D/8`, so the convenient separation form is

```text
rho(A_ring)^2 <= c6+36864/D^2.
```

This is a genuine spectral-radius bound: every finite-ring eigenvalue is
controlled, not merely the cluster produced by truncated interface states.
The proof is uniform in orientations and in the locations of the holonomy
cut.

Status: `GATE_B3_PASS` / PROVED.

# Qualitative Exponential Fixed-r Global Cap

> **Proof superseded.** The cap is expected to survive with two localized
> modes per interface, but this proof depends on the invalid exact-`r`
> complement theorem. Task 55 has since integrated the corrected exact-`2r`
> certificate; this historical proof must not be used in its place.

For each `r in {1,2,3}`, the corrected complement theorem places every
noncluster eigenvalue below `c6-1/200`. The exact-`r` theorem puts precisely
`r` eigenvalues in the fixed near-`c6` window and gives, with

```text
L_site=floor(D/4)-12,
ell=floor(L_site/8),
q=9/25,
```

the existential cluster estimate `|lambda_j-c6|<=C_r q^ell`. For sufficiently
large `D`, the spectral top therefore belongs to this cluster and

```text
rho(A_ring)^2 <=c6+C_r(9/25)^ell.
```

This is uniform over the finitely many orientations and holonomies for fixed
`r`. The constants `C_r` and the onset are not explicit in the current
certificate package.

Historical Task 54 status: `OPEN_PENDING_2R_REPAIR`. Current project status:
the explicit cap `3505r(9/25)^ell` is `COMPUTER_ASSISTED_PROVED` in Task 55.
Any use must cite that independently checked certificate rather than this
withdrawn proof.

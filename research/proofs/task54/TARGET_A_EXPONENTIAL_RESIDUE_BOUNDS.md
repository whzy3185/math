# Qualitative Exponential Residue Bounds

> **Superseded.** This Task 54 derivation used the invalid exact-`r` cluster
> ownership. The residue geometry remains correct, but the spectral bound
> must be re-established from a codimension-`2r` theorem. Task 55 has now
> supplied that theorem, the explicit `3505r` bound, and `N_exp=3120`.

Insert the exact site separations of the explicit constructions:

```text
D_2(n)=n,
D_4(n)=n/2,
D_6(n)=6+4 floor((2k-3)/3),  n=8k+6.
```

For `r=2,4,6`, define

```text
ell_r(n)=floor((floor(D_r(n)/4)-12)/8).
```

Then for each residue there is an existential constant `C_(r/2)` such that
the explicit construction satisfies, for sufficiently large `n`,

```text
m_n^2 <=c6+C_(r/2)(9/25)^ell_r(n).
```

This is an upper construction, not a minimizer characterization. Because the
constants are not explicit, the statement does not supply a numerical
eventual threshold.

Historical Task 54 status: `OPEN_PENDING_2R_REPAIR`. Current project status:
the corrected residue bounds and explicit constants are
`COMPUTER_ASSISTED_PROVED` in Task 55.

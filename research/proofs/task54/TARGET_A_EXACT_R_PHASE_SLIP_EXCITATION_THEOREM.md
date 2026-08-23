# Exact-r Phase-Slip Excitation Theorem

> **Falsified as stated.** The local squared level has rank two, so this
> theorem's exact-`r` count and one-mode-per-interface proof are invalid. The
> expected replacement is exact `2r`, but it requires a new proof.

For each fixed `r in {1,2,3}` there are constants `L_r` and `C_r` such that
every legal ring containing `r` G6 interfaces with minimum cyclic site
separation `D`, where

```text
L_site=floor(D/4)-12,
ell=floor(L_site/8) >=L_r,
```

has exactly `r` squared eigenvalues, counted with multiplicity, in

```text
[c6-1/400,c6+1/400].
```

Each level obeys

```text
|lambda_j-c6| <=C_r(9/25)^ell.
```

Both interface orientations and holonomies are allowed. The constants are
uniform over those finite choices but remain existential.

The `r=1` complement proof uses the separate interface/bulk two-cutoff
partition; `r=2,3` use the cyclic interface-arc partition.

Historical status withdrawn. Current status: `FALSIFIED_AS_STATED`;
corrected exact-`2r` theorem `OPEN`.

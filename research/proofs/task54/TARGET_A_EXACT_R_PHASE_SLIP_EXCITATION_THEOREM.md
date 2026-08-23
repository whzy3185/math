# Exact-r Phase-Slip Excitation Theorem

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

Status: `EXACT_R_R123_PHASE_SLIP_EXCITATION_PROVED` /
COMPUTER_ASSISTED_PROVED. The counting argument is analytic conditional on
the computer-assisted single-G6 isolation input.

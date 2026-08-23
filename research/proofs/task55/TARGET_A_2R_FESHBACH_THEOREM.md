# The 2r-Dimensional G6 Feshbach Theorem

Status: `EXACT_2R_R123_FESHBACH_PROVED` / `COMPUTER_ASSISTED_PROVED`.

Mathematical audit status: `TWO_INDEPENDENT_MATHEMATICAL_AUDITS_PASSED`
(`PASS`, then `PASS_WITH_SHARPENING`). Integration status:
`INDEPENDENT_CHECKER_PASS`. The independent exact-`2r` checker and 29 tamper
tests pass.

Assume the hypotheses and notation of the exact-`2r` cluster theorem. Put

```text
G=Phi^*Phi,
U=Phi G^(-1/2),
P=UU^*,
Q=I-P,
E=(H-c6)Phi.
```

Then `U:C^(2r)->ell^2(Z/nZ)` is an isometry and `P` has rank `2r`. The
codimension-`2r` complement theorem gives

```text
QHQ <=c6-1/200.                                       (1)
```

Hence, for real or complex `z` in the closed fixed-window neighborhood
`|z-c6|<=1/400` with the usual distance interpretation off the real axis,

```text
||(QHQ-z)^(-1)|| <=400.                               (2)
```

## Exact Schur complement

Define the coordinate-space effective operator

```text
H_eff(z)=U^*HU-U^*HQ(QHQ-z)^(-1)QHU.                  (3)
```

Block Gaussian elimination of `H-z` with respect to `P+Q=I` shows that the
finite-ring eigenvalue equation is

```text
det(H_eff(z)-z I_(2r))=0.                             (4)
```

The identity matrix in (4) is essential. The old expression `-zP` mixed the
physical Hilbert space and the `2r`-dimensional coordinate space.

Since `U=Phi G^(-1/2)` and `QHU=QE G^(-1/2)`, equations (2)--(3) give the exact
Gram-coordinate formula

```text
H_eff(z)-c6 I_(2r)
 =G^(-1/2) Phi^* E G^(-1/2)
  -G^(-1/2) E^* Q(QHQ-z)^(-1)Q E G^(-1/2).            (5)
```

No orthogonality of the uncorrected truncated columns is assumed in (5).

## Explicit bounds

Each column of `E` has norm at most `1752q^ell`, and there are `2r` columns.
The Gram estimate gives `||G^(-1)||<=2`. Consequently

```text
||E G^(-1/2)||^2
 <=2*(2r)*1752^2 q^(2ell)
 =r*3504^2 q^(2ell).                                  (6)
```

Writing (5) as

```text
H_eff(z)=c6 I_(2r)+T1+R2(z),                          (7)
```

one obtains

```text
||T1|| <=3504 r q^ell,                                (8)
||R2(z)|| <=400 r*3504^2 q^(2ell).                    (9)
```

The exact integer inequality

```text
400*3504^2*(9/25)^31 <1                              (10)
```

implies, for every `ell>=31`,

```text
||R2(z)|| <r q^ell.                                   (11)
```

Every one of the exactly `2r` fixed-window eigenvalues therefore satisfies

```text
|lambda_j-c6| <3505 r q^ell.                          (12)
```

The entries of `T1` retain same-interface `+/-` truncation effects, both ring
paths, orientation, and holonomy. The theorem makes no universal sign,
nonvanishing, simplicity, or leading-coefficient assertion about those
entries.

The computer-assisted inputs are limited to the certified G6 spectral
isolation and the exact-rational Floquet tail constants. Equations (1)--(12)
are analytic deductions from those inputs and the finite-range cutoff
construction.

Certificate: `certificates/exact_2r_cluster.json`.
Producer: `../../scripts/target_a_task55_exact_2r.py`.

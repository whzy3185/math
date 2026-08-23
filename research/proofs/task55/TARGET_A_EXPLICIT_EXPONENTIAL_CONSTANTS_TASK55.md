# Explicit Exponential Constants for the Exact-2r Cluster

Status: `EXPLICIT_EXPONENTIAL_CONSTANTS_R123_PROVED` /
`COMPUTER_ASSISTED_PROVED`.

Mathematical audit status: `TWO_INDEPENDENT_MATHEMATICAL_AUDITS_PASSED`.
Integration status: `INDEPENDENT_CHECKER_PASS`. The independent exact-`2r`
checker and 29 tamper tests pass.

This document extracts explicit constants from the Task 55 exact-`2r`
construction. It replaces the open-constant status recorded in Task 54.

## Floquet input

Let

```text
q=9/25.
```

Exact rational interval arithmetic on all eight period-eight monodromy cuts
shows that both stable multipliers have modulus strictly below `q`. For each
right stable space and each left unstable space used in backward propagation,
the certified two-column Floquet basis has condition number below

```text
K=17.                                                     (1)
```

These monodromy and interval bounds are computer-assisted inputs. The
remaining estimates below are exact analytic consequences.

## Normalized tails

There are eight site residues and two tails. Summing the geometric series for
a normalized G6 mode gives

```text
||psi_tail||^2
 <=16 K^2/(1-q^2) q^(2ell)
 =10625/2 q^(2ell)
 <73^2 q^(2ell).                                         (2)
```

The negative mode `psi_-=K_G6 psi_+` is obtained by a unitary symmetry, so the
same estimate holds for both modes and both reflected orientations.

Since `||H||<=16` and `c6<8`, a cutoff mode satisfies

```text
||(H-c6)phi_(j,+/-)||
 <=(16+8)*73 q^ell
 =1752 q^ell.                                            (3)
```

## Gram and Feshbach constants

For `r in {1,2,3}` there are `m=2r` cutoff columns. Their Gram matrix obeys

```text
||G-I_m|| <=m*73^2 q^(2ell).                             (4)
```

With

```text
D>=1040,
L_site=floor(D/4)-12,
ell=floor(L_site/8)>=31,
```

the worst case `m=6` in (4) is below `1/2`; hence `||G^(-1)||<=2`.
Gram orthonormalization and (3) give

```text
||T1|| <=3504 r q^ell.                                   (5)
```

The codimension-`2r` complement has resolvent norm at most 400 in the fixed
window. Consequently

```text
||R2(z)|| <=400 r*3504^2 q^(2ell).                       (6)
```

The exact inequality

```text
400*3504^2*(9/25)^31 <1                                 (7)
```

turns (6) into `||R2(z)||<r q^ell`. Therefore every one of the exactly `2r`
cluster eigenvalues satisfies

```text
|lambda_j-c6| <C_r q^ell,                               (8)
```

with the explicit constants

| interfaces `r` | cluster dimension | `C_r` |
|---:|---:|---:|
| 1 | 2 | 3505 |
| 2 | 4 | 7010 |
| 3 | 6 | 10515 |

No fitted decimal coefficient enters (1)--(8). The values are conservative
and are not claimed optimal.

Certificate: `certificates/exact_2r_cluster.json`, blocks `bulk_floquet`,
`constants`, `gram`, `counting`, and `feshbach`.

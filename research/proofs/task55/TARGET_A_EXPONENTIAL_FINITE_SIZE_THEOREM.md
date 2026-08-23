# Exponential Finite-Size Counterexample Theorem

Status: `N_EXP_3120_SUFFICIENT_PROVED` / `COMPUTER_ASSISTED_PROVED`.

Mathematical audit status: `TWO_INDEPENDENT_MATHEMATICAL_AUDITS_PASSED`.
Integration status: `INDEPENDENT_CHECKER_PASS`. The independent exact-`2r`
checker and 29 tamper tests pass.

## Theorem

For every even order

```text
n>=3120,                                                 (1)
```

one of the explicit period-eight or separated-G6 families satisfies

```text
rho(A_n)^2 <rho_-(n)^2.                                  (2)
```

Thus

```text
N_exp=3120                                               (3)
```

is a continuous sufficient onset for the exponential construction. It is not
claimed to be optimal or minimal. The independently proved finite-plus-IMS
threshold `N_star=48` remains stronger.

## Threshold lower bound

For every even `n`, the elementary trigonometric estimate gives

```text
rho_-(n)^2 >8-200/n^2.                                   (4)
```

For the three nonzero residues we use the stronger intermediate target

```text
B(n)=8-200/n^2-9/100.                                    (5)
```

The exact-`2r` theorem and its explicit constants give

```text
rho(A_n)^2 <=c6_upper+3505 r(9/25)^ell.                 (6)
```

## First distance-eligible endpoints

The explicit constructions have interface separations

```text
D_2(n)=n,
D_4(n)=n/2,
D_6(n)=6+4 floor((2k-3)/3),   n=8k+6,                  (7)
```

and

```text
ell=floor((floor(D/4)-12)/8).                           (8)
```

The first orders in each nonzero residue with `D>=1040` are:

| `n mod 8` | first `n` | interfaces `r` | cluster dimension | `D` | `ell` | certified comparison |
|---:|---:|---:|---:|---:|---:|---|
| 2 | 1042 | 1 | 2 | 1042 | 31 | `B(n)-[c6_upper+3505q^31] >1/250` |
| 4 | 2084 | 2 | 4 | 1042 | 31 | `B(n)-[c6_upper+7010q^31] >1/250` |
| 6 | 3126 | 3 | 6 | 1042 | 31 | `B(n)-[c6_upper+10515q^31] >1/250` |

The certificate stores each cap, threshold, and strict margin as a complete
exact rational number. The immediately preceding same-residue orders are
`1034`, `2076`, and `3118`; their separations are respectively `1034`, `1038`,
and `1038`, so none meets `D>=1040`. In particular,

```text
ell(1039)=30,   ell(1040)=31,
n=3118: D=1038, ell=30.                                 (9)
```

This verifies the endpoint and off-by-one claims without numerical fitting.

## Residue zero

When `8` divides `n`, use the exact period-eight family. Its squared spectral
top is bounded by

```text
eta <=1561/200.                                         (10)
```

At `n=3120`,

```text
8-200/3120^2 =389375/48672,
(389375/48672)-(1561/200)=237251/1216800>0.             (11)
```

The right side of (4) increases with `n`, so (10)--(11) cover every later
order divisible by eight.

## Continuous onset

Within each fixed residue modulo eight, the distance in (7) is nondecreasing.
Hence `ell` is nondecreasing, the cap in (6) is nonincreasing, and `B(n)` is
strictly increasing. It is therefore enough to check the first eligible
endpoint in each residue.

Starting at 3120, the first four even orders are

```text
3120 (mod 8 =0),
3122 (mod 8 =2),
3124 (mod 8 =4),
3126 (mod 8 =6).                                       (12)
```

The residue-two and residue-four families were already eligible from 1042 and
2084, while the residue-six family becomes eligible at 3126. Equations
(5)--(12) therefore cover every even `n>=3120` and prove (1)--(3).

The `n=100/102` controls are not inputs. No minimality claim for `N_exp` is
made.

Certificate: `certificates/exact_2r_cluster.json`, block `exponential_tail`.

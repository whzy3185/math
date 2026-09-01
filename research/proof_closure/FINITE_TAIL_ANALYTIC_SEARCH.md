# Finite-Tail Analytic Search

## Confirmed compression: the residue-zero family

For `n=8L`, choose the period-eight reference signing with the periodic finite
holonomy. The period-eight Floquet theorem gives, for every `L>=1`,

```text
rho(A_(8L,+1))^2=eta=4+sqrt(10+2sqrt(5))<1561/200.
```

For the twisted benchmark, the elementary bound already used in the analytic
tail is

```text
rho_-(n)^2 > 8-200/n^2.
```

In fact the family begins at `n=32`. The elementary bounds

```text
cos x > 1-x^2/2,    pi^2 < 987/100
```

give

```text
rho_-(32)^2
 > 8-5pi^2/256
 > 39973/5120
 > 1561/200.
```

The benchmark is increasing with even `n`, since both cosine arguments
decrease on the relevant interval. Thus `eta<rho_-(n)^2` for every multiple
of eight with `n>=32`. The coarser bound used for the old global tail also
gives, for `n>=48`,

```text
1561/200 < 2279/288.
```

Thus, without any LDL row,

```text
n=0 mod 8 and n>=32  =>  m_n^2<=eta<rho_-(n)^2.
```

This is an `ANALYTIC_PROVED` residue-family theorem. It removes all 24
residue-zero rows from the former `48<=n<240` bridge and structurally supplies
the failures at `n=32,40`; their LDL records remain backup evidence.

## Existing IMS information used at its sharper residue scope

The exact Task 54 tent ledger proves monotonic residue-specific inequalities
after the following last failed endpoints:

| residue | last endpoint where its IMS inequality fails | analytic range certified by the same proof |
|---:|---:|---|
| 2 | 90 | `n=8k+2, n>=92` |
| 4 | 164 | `n=8k+4, n>=166` |
| 6 | 238 | `n=8k+6, n>=240` |

These are not new asymptotic estimates. They are the per-residue monotonic
consequences already encoded in the exact certificate, separated here rather
than hidden behind the coarser global threshold 240.

## Quantified effect

The old bridge has 96 rows, 24 per even residue. After the residue-zero
theorem and the residue-specific IMS ranges, the remaining finite rows are:

| residue | retained finite orders | rows |
|---:|---|---:|
| 0 | none | 0 |
| 2 | `50,58,66,74,82,90` | 6 |
| 4 | `52,60,...,164` | 15 |
| 6 | `54,62,...,238` | 24 |
| total | | 45 |

The first reduction left 45 rows. The additional exact period-10, 12, 14, 18,
and 22 Floquet families now cover 20 more rows; see
`PERIODIC_COUNTEREXAMPLE_COVERAGE.md`. The remaining 25 rows are still
`FINITE_FORMAL_PROVED` backup evidence.

## Attempted F1--F4 routes and current obstruction

The one-interface finite closure is exactly

```text
det(M_n(lambda)-alpha I)=0,
```

and its squared determinant obeys a universal order-nine exterior-power
recurrence. After `y=8+u`, the recurrence coefficients alternate in sign.
The first nine terms have a one-sign property, but that fact is not preserved
by the recurrence's naive coefficient cone. Therefore no valid monotonicity
or global spectral-exclusion theorem follows at present. The missing argument
is an invariant cone, a Riccati/Schur complement estimate, or an equivalent
finite-rank defect bound. It would be mathematically incorrect to extrapolate
the initial symbolic rows.

## Next analytic target

The priority is a one-G6 transfer theorem for `n=8k+2` that treats both
holonomies and proves its relevant finite-ring edge is below the benchmark for
all `k>=6`. A proof would remove the remaining six residue-two rows and
provide the first genuine F1/F4 family replacement.

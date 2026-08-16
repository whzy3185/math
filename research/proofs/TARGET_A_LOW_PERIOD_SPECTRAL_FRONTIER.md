# Target A Low-Period Spectral Frontier

Date: 2026-08-16

Status: **PERIOD_LE16_UNIQUE_PRIMITIVE_OPTIMUM_PROVED**

Component statuses:

```text
LOW_PERIOD_PHASE_SPACE_COMPLETE
LOW_PERIOD_SPECTRAL_FRONTIER_TABLE_PROVED
PERIOD_LE16_UNIQUE_PRIMITIVE_OPTIMUM_PROVED
```

## Theorem

Among all periodic Hamilton-gauge signings whose primitive `tau` period is at
most 16, the Target A period-8 phase is the unique minimizer of the
infinite-volume squared spectral radius, up to translation, reflection,
global `tau` negation, and repetition of the unit cell.

Its exact value is

```text
eta=4+sqrt(10+2sqrt(5)).
```

Every genuinely different phase in this bounded domain has `R(Q)>eta`.

This is a theorem only through primitive period 16. It is not an all-period,
finite-size, or all-signings global optimality statement.

## 1. Phase Space

For each cell length `1<=p<=16`, enumerate

```text
Q in {-1,+1}^p,
product_i Q_i=1,
```

and quotient by the dihedral action `D_p`. Route A explicitly partitions the
`2^(p-1)` legal words into rotation/reflection orbits.

Route B is independent of sign-word enumeration. For each rotation or
reflection, decompose its permutation of the `p` positions into cycles. A
fixed word is constant on each cycle. If at least one cycle has odd length,
exactly half of the cycle-sign assignments have product `+1`; if every cycle
has even length, every assignment has product `+1`. Burnside averaging then
gives the orbit count.

The two routes agree period by period:

| `p` | legal `Q` | `D_p` orbits | primitive tau period `p` orbits |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 2 | 2 | 2 | 1 |
| 3 | 4 | 2 | 1 |
| 4 | 8 | 4 | 2 |
| 5 | 16 | 4 | 3 |
| 6 | 32 | 8 | 5 |
| 7 | 64 | 9 | 8 |
| 8 | 128 | 18 | 14 |
| 9 | 256 | 23 | 21 |
| 10 | 512 | 44 | 39 |
| 11 | 1024 | 63 | 62 |
| 12 | 2048 | 122 | 112 |
| 13 | 4096 | 190 | 189 |
| 14 | 8192 | 362 | 352 |
| 15 | 16384 | 612 | 607 |
| 16 | 32768 | 1162 | 1144 |

The orbit total is exactly

```text
1+2+2+4+4+8+9+18+23+44+63+122+190+362+612+1162=2626.
```

Any periodic signing of primitive `tau` period at most 16 occurs in this
list using its primitive cell. Thus the enumeration covers the theorem's
entire domain.

## 2. General Bloch Constructor

For a periodic lift `tau`, the infinite operator is

```text
(A_tau x)_i=x_(i-1)+x_(i+1)
              +tau_(i-2)x_(i-2)+tau_i x_(i+2).
```

For each transition from residue `i` to an absolute source `j`, write

```text
j=mp+r, 0<=r<p,
```

and add its coefficient times `z^m` to entry `(i,r)`. This handles the
short cells `p=1,2,3` without special collision assumptions.

The resulting exact Laurent matrices satisfy, for every one of the 2626
orbits,

```text
H_tau(z)^T=H_tau(z^-1).
```

Hence they are Hermitian on `|z|=1`. If

```text
D=diag(1,-1,1,-1,...),
```

then the correct general negation identity is

```text
H_(-tau)(z)=-D H_tau((-1)^p z) D.
```

For even `p` this preserves each fiber. For odd `p` it shifts `z` to `-z`;
the supremum over the unit circle is still unchanged. Recording this phase
shift avoids silently applying the period-8 same-fiber identity to odd cells.

The program also compares, for every orbit, all `Q` rotations/reflections
with the `Q` words reconstructed from all translations/reflections/global
negations of its `tau` lift. The sets agree exactly. Primitive `Q` and `tau`
periods are recomputed from the words rather than inferred from the cell size.

## 3. Discovery Scan

Every orbit receives a dense-grid Bloch preview containing

```text
p,
canonical Q,
tau lift,
primitive Q period,
primitive tau period,
observed R(Q),
observed maximizing phase,
observed gap from eta.
```

The base grid has 256 phases. The five best classes at each period are
refined to 4096 phases. These values locate candidates and certificate
points; they are explicitly marked `OBSERVED_DENSE_BLOCH_GRID` and are not
used as proof.

No preview lies below `eta` outside the target representations. The closest
competitor is

```text
p=10,
Q=0000010001,
R_numeric^2=7.91638155174...,
R_numeric^2-eta=0.11215548656....
```

It is independently certified by both exact endpoint Rayleigh arithmetic and
Sturm root isolation.

## 4. Exact Competitor Certificates

The 2624 non-target orbit representatives split as follows.

| exact route | orbit count |
|---|---:|
| Task 42A positive `F_1` or `F_2` | 1787 |
| `z=+1` or `-1`, ternary Rayleigh vector | 824 |
| `z=+1` or `-1`, small integer Rayleigh vector | 13 |
| uncertified | 0 |

For a moment certificate, Task 42A gives

```text
F_k>0 ==> R(Q)>8>eta.
```

For an endpoint certificate, let `H=H_Q(+1)` or `H_Q(-1)` and let `v` be the
stored nonzero integer vector. Exact integer arithmetic computes

```text
r=(v^T H^2 v)/(v^T v).
```

The stored certificate verifies `r>eta` without floating point. Put

```text
u=((r-4)^2-10)/2.
```

The exact rational inequalities `u>0` and `u^2>5` imply
`r>4+sqrt(10+2sqrt(5))=eta`. Rayleigh's principle then gives

```text
R(Q)>=lambda_max(H^2)>=r>eta.
```

The 24 numerically closest endpoint-certified classes receive a second exact
route. The checker reconstructs the integer polynomial

```text
det(yI-H^2)
```

and repeats Sturm isolation of its largest real root. In each case the
rational lower endpoint of the isolating interval is itself proved greater
than `eta`. All 13 classes with observed gap below `0.25` are included in
this double-check set.

## 5. Target Repetition

The target has primitive flux word

```text
Q_primitive=0001
```

with primitive `tau` period 8. It appears in the table as

```text
P08-0006: Q=00010001,
P16-0512: Q=0001000100010001.
```

The second row is a repeated unit cell, not a second infinite periodic phase.
Both receive their exact value `R=eta` from the frozen Task 40A theorem. The
program assigns them the same infinite-phase key `tau8:Q0001`.

No other orbit lacks a strict `R>eta` certificate. This proves uniqueness in
the stated primitive-period domain.

## 6. Low-Period Frontier Table

For periods without a target representation, the displayed minimum is a
numerical ranking, while the strict relation of every orbit to `eta` is
proved exactly. At periods 8 and 16 the minimum itself is exactly `eta`.

| `p` | observed minimum `R^2` | minimizing canonical `Q` | exact relation to `eta` |
|---:|---:|---|---|
| 1 | 16.0000000000 | `1` | every orbit `>eta` |
| 2 | 8.0000000000 | `00` | every orbit `>eta` |
| 3 | 8.1162737607 | `001` | every orbit `>eta` |
| 4 | 8.0000000000 | `0000` | every orbit `>eta` |
| 5 | 9.0000000000 | `00001` | every orbit `>eta` |
| 6 | 8.0000000000 | `000000` | every orbit `>eta` |
| 7 | 8.5282531776 | `0000001` | every orbit `>eta` |
| 8 | `eta` | `00010001` | exact target |
| 9 | 8.1162738603 | `001001001` | every orbit `>eta` |
| 10 | 7.9163815517 | `0000010001` | every competitor `>eta` |
| 11 | 8.0945968174 | `00010001001` | every orbit `>eta` |
| 12 | 7.9355448971 | `000000010001` | every orbit `>eta` |
| 13 | 8.1004636721 | `0000010001001` | every orbit `>eta` |
| 14 | 7.9634702195 | `00000000010001` | every orbit `>eta` |
| 15 | 8.1162738621 | `001001001001001` | every orbit `>eta` |
| 16 | `eta` | `0001000100010001` | repeated target cell |

The numerical ordering within a non-target period is not promoted to an
exact within-period minimizer theorem. What is exact, and sufficient for the
main theorem, is that every listed competitor is strictly above `eta`.

## 7. Independent Verification and Scope

The checker does not import the classifier. It independently:

- recomputes explicit orbit counts and Burnside counts;
- reconstructs all `Q`, `tau`, primitive periods, orbit sizes, and geometric
  equivalence images;
- rebuilds the general Laurent Bloch matrices;
- verifies all 1787 moment and 837 endpoint Rayleigh certificates;
- recomputes all 24 Sturm characteristic polynomials and root intervals;
- confirms that the two target rows are one primitive period-8 phase.

Proved:

```text
unique optimum among primitive tau periods <=16,
complete legal-Q/D_p phase space through p=16,
exact strict separation of every bounded-domain competitor from eta.
```

Not claimed:

```text
anything for primitive period >=17,
all-period global optimality,
finite-size global optimality,
global optimality among arbitrary nonperiodic signings.
```

Run:

```bash
python research/scripts/target_a_low_period_spectral_frontier.py
python research/scripts/verify_target_a_low_period_spectral_frontier.py
python -m pytest -q research/scripts/test_target_a_low_period_spectral_frontier.py
```

Expected checker status:

```text
TARGET_A_LOW_PERIOD_SPECTRAL_FRONTIER_PASS
```

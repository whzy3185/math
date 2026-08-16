# Target A: Classification of Period-8 Flux Phases

Date: 2026-08-16

Status: **PERIOD8_UNIQUE_OPTIMUM_AND_SECOND_BEST_PROVED**

## Theorem

For an 8-periodic Hamilton-gauge signing, put

```text
(A_tau x)_i = x_(i-1) + x_(i+1)
              + tau_(i-2) x_(i-2) + tau_i x_(i+2),
Q_i = tau_i tau_(i+1),
R(Q) = sup_(|z|=1) rho(H_Q(z))^2.
```

Modulo switching, cyclic translation, reflection, and the two lifts `tau`
and `-tau`, the unique minimizer among all 8-periodic flux phases is

```text
Q_* = (+,-,-,-,+,-,-,-) = (+---)^2.
```

Its exact squared spectral radius is

```text
eta = 4 + sqrt(10 + 2*sqrt(5)).
```

The unique second-best orbit is the all-unbalanced phase `Q_0=(-)^8`, with

```text
R(Q_0) = 8,       rho(Q_0) = 2*sqrt(2).
```

Every other period-8 flux orbit satisfies `R(Q)>8`.  Consequently the exact
squared and unsquared gaps between first and second place are

```text
8 - eta = 4 - sqrt(10 + 2*sqrt(5)) > 0,
2*sqrt(2) - sqrt(eta) > 0.
```

This is an infinite-volume theorem restricted to 8-periodic phases.  It does
not claim finite-size global optimality, optimality among arbitrary periods,
or optimality among all signings.

## Definitions and Equivalences

The bit convention in every machine artifact is

```text
1 <=> Q_i=+1,   0 <=> Q_i=-1,   Q_0 is the leftmost bit.
```

Since

```text
product_(i=0)^7 Q_i = product_i tau_i tau_(i+1) = 1,
```

there are `2^7=128` legal `Q` vectors.  Conversely, fixing `tau_0=+1` and
recursing by `tau_(i+1)=Q_i tau_i` closes exactly when `product Q_i=1`.
Every legal `Q` has precisely two lifts, `tau` and `-tau`.

Let `D=diag((-1)^i)`.  Directly from the step-1 and step-2 terms,

```text
H_(-tau)(z) = -D H_tau(z) D.
```

Thus the two lifts have negated spectra and identical spectral radii.  The
remaining translation and reflection actions are the usual `D_8` action on
the cyclic `Q` word.

## Completeness

Two independent counts were performed.

Route A enumerates all 256 `tau` words, verifies their fibers over the 128
legal `Q` words, explicitly forms every rotation and reflected rotation, and
takes the lexicographically least bit word in each orbit.  It gives 18
disjoint orbits whose sizes sum to 128.

Route B acts on the legal parity set directly.  The rotation fixed-point
counts are

```text
128, 2, 4, 2, 16, 2, 4, 2,
```

and each of the eight reflected actions fixes 16 legal words.  Their sum is
288, so Burnside's lemma gives `288/16=18`.  Applying Burnside separately in
each shell gives

```text
d(Q)=0: 1,   d(Q)=2: 4,   d(Q)=4: 8,
d(Q)=6: 4,   d(Q)=8: 1.
```

Here `d(Q)` is the number of entries with `Q_i=+1`.

## Fresh Bloch Construction

For each canonical `Q`, the classifier reconstructs the lift with
`tau_0=+1`.  It then generates the `8 x 8` Bloch matrix directly from the four
infinite-graph transitions at each output residue.  If a source crosses a
cell boundary by `m`, its entry receives `z^m`.  No pre-existing period-8
constructor is imported.

The implementation symbolically checks

```text
H_tau(z)^T = H_tau(z^-1),
```

and checks that `H_tau(+1)` and `H_tau(-1)` are integral symmetric matrices.
It also verifies the `tau -> -tau` identity above for every orbit.

## Orbit and Certificate Table

The numeric column is a 4096-point discovery scan and is only **OBSERVED**.
Every comparison in the final column is independently recomputed with exact
integer arithmetic from `v^T H(z)^2 v / v^T v`.

| Orbit | canonical Q | d | orbit | stab. | per(Q) | per(tau) | numeric R(Q) | exact certificate |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| P8-01 | `00000000` | 0 | 1 | 16 | 1 | 2 | 8.00000000000001 | `z=1`, `v=(-1)^8`, `64/8=8` |
| P8-02 | `00000011` | 2 | 8 | 2 | 8 | 8 | 9.90631707599469 | `z=1`, `v=(-1,-1,-1,-1,-1,-1,-1,-1)`, `72/8>8` |
| P8-03 | `00000101` | 2 | 8 | 2 | 8 | 8 | 8.74180853217889 | `z=-1`, `v=(-1,-1,-1,0,-1,-1,-1,1)`, `60/7>8` |
| P8-04 | `00001001` | 2 | 8 | 2 | 8 | 8 | 8.67888773155075 | `z=1`, `v=(-1,-1,-1,0,-1,-1,-1,-1)`, `60/7>8` |
| P8-05 | `00001111` | 4 | 8 | 2 | 8 | 8 | 12.2826722313107 | `z=1`, `v=(-1)^8`, `88/8>8` |
| P8-06 | `00010001` | 2 | 4 | 4 | 4 | 8 | 7.80422606518062 | Task 40A exact `R=eta<8` |
| P8-07 | `00010111` | 4 | 16 | 1 | 8 | 8 | 10.8382901411622 | `z=1`, `v=(-1,-1,-1,-1,0,-1,-1,-1)`, `60/7>8` |
| P8-08 | `00011011` | 4 | 8 | 2 | 8 | 8 | 9.95763413943552 | `z=1`, `v=(-1,-1,-1,0,0,0,-1,-1)`, `42/5>8` |
| P8-09 | `00100111` | 4 | 8 | 2 | 8 | 8 | 10.6404654218786 | `z=1`, `v=(-1)^8`, `80/8>8` |
| P8-10 | `00101011` | 4 | 16 | 1 | 8 | 8 | 10.3623044650767 | `z=1`, `v=(-1,-1,-1,0,0,0,-1,-1)`, `42/5>8` |
| P8-11 | `00101101` | 4 | 8 | 2 | 8 | 8 | 10.4721359549996 | `z=1`, `v=(-1,-1,0,-1,-1,0,-1,1)`, `52/6>8` |
| P8-12 | `00110011` | 4 | 4 | 4 | 4 | 4 | 10.4721359549996 | `z=1`, `v=(-1)^8`, `80/8>8` |
| P8-13 | `00111111` | 6 | 8 | 2 | 8 | 8 | 13.3745298794648 | `z=1`, `v=(-1)^8`, `104/8>8` |
| P8-14 | `01010101` | 4 | 2 | 8 | 2 | 4 | 10 | `z=1`, `v=(-1,-1,-1,0,1,0,1,-1)`, `50/6>8` |
| P8-15 | `01011111` | 6 | 8 | 2 | 8 | 8 | 13.4381783232217 | `z=1`, `v=(-1)^8`, `80/8>8` |
| P8-16 | `01101111` | 6 | 8 | 2 | 8 | 8 | 12.2725813107434 | `z=1`, `v=(-1,-1,-1,-1,0,-1,-1,-1)`, `60/7>8` |
| P8-17 | `01110111` | 6 | 4 | 4 | 4 | 8 | 11.1038667445264 | `z=1`, `v=(-1,-1,-1,-1,1,-1,-1,-1)`, `72/8>8` |
| P8-18 | `11111111` | 8 | 1 | 16 | 1 | 1 | 16 | `z=1`, `v=(-1)^8`, `128/8>8` |

## Target Phase

The requested word `10001000` belongs to orbit `P8-06`, whose canonical word
is `00010001`.  Its orbit has size 4.  Its primitive `Q` period is 4, while
the lift

```text
tau=(+,-,+,-,-,+,-,+)
```

has primitive period 8.  The frozen Task 40A theorem proves

```text
R(P8-06)=eta=4+sqrt(10+2*sqrt(5))<8.
```

## Exact Competitor Lower Bounds

For every non-target orbit, the classifier searches `z in {+1,-1}` and
`v in {-1,0,1}^8` in deterministic order.  The table stores the first vector
meeting the required exact threshold.  Since

```text
R(Q) >= rho(H_Q(z))^2
     >= v^T H_Q(z)^2 v / v^T v,
```

the 17 certificates prove `R(Q)>=8` for every competitor.  The 16
non-runner certificates are strict.

The independent checker does not trust the stored numerator, denominator,
or comparison sign.  It reconstructs `Q -> tau -> H(z) -> H(z)^2`, then
recomputes every quotient.

## Exact Runner-Up Constant

For `Q_0=(-)^8`, the lift is `tau_i=(-1)^i`.  Let `S` be the unitary lattice
shift, `C=S+S^-1`, `E=S^2+S^-2`, and `D=diag((-1)^i)`.  Then

```text
A=C+DE,       CD=-DC,       ED=DE.
```

Therefore

```text
A^2=C^2+E^2
   =4I+S^2+S^-2+S^4+S^-4.
```

On a unit-circle shift eigenvalue `w`, this has scalar value

```text
4+w^2+w^-2+w^4+w^-4
=4+2*cos(2 theta)+2*cos(4 theta) <= 8.
```

The `z=1`, `v=(-1)^8` certificate attains 8, so `R(Q_0)=8` exactly.  It is
the unique second-best orbit because all other non-target classes have a
strict lower certificate above 8.

## The d=2 Shell

The four `d=2` orbits correspond exactly to cyclic separations 1, 2, 3, and
4 between the two `Q_i=+1` positions:

| separation | canonical Q | conclusion |
|---:|---:|---|
| 1 | `00000011` | exact Rayleigh lower bound `>8` |
| 2 | `00000101` | exact Rayleigh lower bound `>8` |
| 3 | `00001001` | exact Rayleigh lower bound `>8` |
| 4 | `00010001` | target, exact `R=eta<8` |

Thus equal spacing is the unique minimizer in this shell.  This is a finite
exact classification, not a claimed general separation-monotonicity theorem.

## Spectral Coincidences

For every orbit, the audit independently computes the full Laurent Bloch
characteristic polynomial, canonicalizes the harmless `x -> -x` lift change,
and computes the exact squared characteristic signature

```text
det(xI-H(z)) det(-xI-H(z)).
```

All 18 squared signatures are distinct.  The unordered exact endpoint
spectra at `z=+1,-1` also form 18 distinct classes.  Hence this classification
has 18 flux orbits and 18 exact squared-Bloch spectral equivalence classes.
The coincident numeric previews for `P8-11` and `P8-12` do not represent full
Bloch spectral equivalence.

## Scope

The proved statement is

```text
period8_infinite_volume_optimality: PROVED
finite_size_global_optimality: NOT_CLAIMED
all_period_global_optimality: NOT_CLAIMED
all_signings_global_optimality: NOT_CLAIMED
```

Task 40A's finite-holonomy conclusions for the target remain valid, but this
task does not compare all competitors on every finite allowed Bloch grid.

## Machine Verification

Run

```bash
python research/scripts/verify_target_a_period8_pattern_classification.py
```

Expected terminal status:

```text
TARGET_A_PERIOD8_PATTERN_CLASSIFICATION_PASS
```

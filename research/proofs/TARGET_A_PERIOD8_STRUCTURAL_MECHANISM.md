# Structural Mechanism for the Period-8 Optimum

Date: 2026-08-16

Status: **PERIOD8_STRUCTURAL_MECHANISM_PROVED**

Component statuses:

```text
PERIOD8_EIGHT_BARRIER_TRICHOTOMY_PROVED
PERIOD8_CLOSED_WALK_MECHANISM_PROVED
PERIOD8_TARGET_CHIRAL_MECHANISM_PROVED
```

## Theorem

For a legal 8-periodic flux phase `Q`, define

```text
D(Q)={i:Q_i=+1},
R(Q)=sup_(|z|=1) rho(H_Q(z))^2,
eta=4+sqrt(10+2*sqrt(5)).
```

Then exactly one of the following cases occurs:

1. `D(Q)` is empty.  Then `Q=(-)^8` and `R(Q)=8`.
2. `D(Q)={j,j+4}` for some `j`.  Then `R(Q)=eta<8`.
3. In every other case, `R(Q)>8`.

Equivalently,

```text
R(Q)<8  iff the two positive-flux positions are antipodal,
R(Q)=8  iff Q=(-)^8,
R(Q)>8  otherwise.
```

This theorem concerns infinite-volume 8-periodic phases only.  It does not
claim finite-size global optimality, arbitrary-period optimality, or
optimality among all signings.

## 1. Squaring the Signed Operator

In Hamilton gauge,

```text
(A_tau x)_i=x_(i-1)+x_(i+1)
              +tau_(i-2)x_(i-2)+tau_i x_(i+2),
Q_i=tau_i tau_(i+1).
```

Expanding the two-step transitions from residue `i` gives the following
complete row of `A_tau^2` on the infinite lattice:

| displacement | coefficient |
|---:|---|
| `-4` | `Q_(i-4)Q_(i-3)` |
| `-3` | `tau_(i-3)(1+Q_(i-3))` |
| `-2` | `1` |
| `-1` | `tau_(i-2)(1+Q_(i-2))` |
| `0` | `4` |
| `+1` | `tau_(i-1)(1+Q_(i-1))` |
| `+2` | `1` |
| `+3` | `tau_i(1+Q_i)` |
| `+4` | `Q_iQ_(i+1)` |

The machine proof obtains the left side by multiplying the four signed
transitions twice.  It independently obtains the right side from `Q`, then
checks all eight indices for all 256 sign words `tau`.  This performs 4096
checks with `Q=-1` and 4096 with `Q=+1`.

The mechanism is immediate from the odd displacements.  A negative flux
entry makes `1+Q_i=0` and cancels its associated odd-distance coupling.  A
positive flux entry makes `1+Q_i=2` and activates a coupling of amplitude
`+2` or `-2`.  We call the positive-flux positions the defect set `D(Q)`.

## 2. The Cancellation Baseline

For `D(Q)=emptyset`, the lift is `tau_i=(-1)^i`.  Put

```text
C=S+S^-1,       E=S^2+S^-2,       D=diag((-1)^i).
```

Then `A=C+DE`, while `CD=-DC` and `ED=DE`.  Hence

```text
A^2=C^2+E^2
   =4I+S^2+S^-2+S^4+S^-4.
```

On a unitary shift eigenvalue `exp(i theta)`, the scalar symbol is

```text
4+2*cos(2 theta)+2*cos(4 theta)<=8.
```

Equality occurs at `theta=0`, so this phase has `R(Q)=8`.  It is the
cancellation baseline for the trichotomy.

## 3. Closed-Walk Moment Barrier

Define the exact even moments

```text
M_k(Q)=CT_z tr(H_Q(z)^(2k)).
```

Constant-term extraction is equivalent to averaging over the Bloch phase:

```text
M_k=(1/(2*pi))*integral_0^(2*pi)
        tr(H_Q(exp(i theta))^(2k)) dtheta.
```

It is also the signed length-`2k` closed-walk sum per eight-site cell.  The
implementation computes it by integer dynamic programming on absolute
lattice positions, so no numerical quadrature enters the proof.

If `R(Q)<=8`, every `y_j(theta)=lambda_j(theta)^2` lies in `[0,8]`.  Thus

```text
y_j(theta)^(k+1)<=8*y_j(theta)^k.
```

Summing and integrating proves

```text
M_(k+1)<=8*M_k.
```

Therefore the only logical direction used below is

```text
F_k(Q):=M_(k+1)-8*M_k>0  ==>  R(Q)>8.
```

A negative `F_k` does not prove `R(Q)<=8`, and finitely many negative moments
do not prove the target upper bound.  The target's `R(Q)=eta<8` remains a
dependency on the exact Task 40A Floquet theorem.

## 4. Low Moments as Local Flux Statistics

Put

```text
d=#{i:Q_i=+1},
a=#{i:Q_i=Q_(i+1)=+1},
b=#{i:Q_i=Q_(i+2)=+1}.
```

The diagonal of `A^2` immediately gives

```text
M_1=8*4=32.
```

Since `A^2` is Hermitian,

```text
M_2=tr(A^4)=sum_(i,j) |(A^2)_(i,j)|^2.
```

The diagonal, even-distance, and distance-four terms contribute the baseline
160.  Every `Q_i=+1` opens four oriented odd-distance entries of squared
amplitude four, contributing 16.  Hence

```text
M_2=160+16d.
```

For `M_3=tr((A^2)^3)`, exact collection of the local closed products gives

```text
M_3=944+168d+96a+48b.
```

The four coefficients are not supplied to the program.  They are solved from
the exact closed-walk expansion in the basis `1,d,a,b`, then checked on all
128 legal `Q`.  The terms respectively represent the cancellation baseline,
single activated positions, adjacent activated pairs, and distance-two
activated pairs.  No higher interaction occurs at length six.

Consequently,

```text
F_2=M_3-8*M_2=-336+40d+96a+48b.
```

## 5. High-Defect Phases Cross the Barrier

Suppose first that `d=4`.  Write the four cyclic gaps between positive
positions as positive integers summing to eight.  Let `n1` count gaps equal
to one.

If `n1>=2`, then `2a>=4`.  If `n1=0`, every gap is two, so `b=4`.  If
`n1=1`, the other three gaps must be `2,2,3`, so again `2a+b=4`.  Therefore

```text
2a+b>=4,
F_2=-176+48(2a+b)>=16>0.
```

For `d=6`, the two negative positions destroy at most four of the eight
adjacent positive-positive edges, so `a>=4`.  Hence

```text
F_2=-96+96a+48b>=288>0.
```

For `d=8`, the second moment already gives

```text
F_1=M_2-8*M_1=288-256=32>0.
```

The moment barrier lemma now proves `R(Q)>8` for every phase with `d>=4`.
The exhaustive checks over the 70, 28, and 1 vectors in these shells are
retained only as machine cross-checks of the combinatorial arguments.

## 6. Two-Defect Phases

For `d=2`, let `s` be the smaller cyclic distance between the positive-flux
positions.  Then `s` is one of `1,2,3,4`.  The exact moments through `M_10`
and excesses through `F_9` are:

### Separation 1

```text
M = 32, 192, 1376, 10976, 93312, 823920, 7447136,
    68348832, 633982976, 5926419872
F = -64, -160, -32, 5504, 77424, 855776, 8771744,
    87192320, 854556064
```

The first positive excess is `F_4=5504`, so `R(Q)>8`.

### Separation 2

```text
M = 32, 192, 1328, 9888, 76832, 612624, 4965328,
    40683296, 335872832, 2788389472
F = -64, -208, -736, -2272, -2032, 64336, 960672,
    10406464, 101406816
```

The first positive excess is `F_6=64336`, so `R(Q)>8`.

### Separation 3

```text
M = 32, 192, 1280, 9056, 66592, 503088, 3877920,
    30363808, 240761792, 1928966432
F = -64, -256, -1184, -5856, -29648, -146784, -659552,
    -2148672, 2872096
```

The first positive excess is `F_9=2872096`, so `R(Q)>8`.

### Separation 4

```text
M = 32, 192, 1280, 8928, 63872, 464496, 3417152,
    25354656, 189356672, 1421345952
F = -64, -256, -1312, -7552, -46480, -298816, -1982560,
    -13480576, -93507424
```

No `F_1,...,F_9` is positive.  This finite observation is not the upper-bound
proof.  Separation four is the antipodal target phase, and Task 40A proves
exactly that `R(Q)=eta<8`.

The exact first-detection hierarchy `4<6<9` shows that the closed-walk excess
above the barrier appears at progressively longer even-walk scales as the two
defects separate.  Only the antipodal pair is sub-eight.  This conclusion is
restricted to the four period-8 two-defect phases; no general separation
monotonicity theorem is claimed.

## 7. Anti-Periodicity and Chiral Symmetry

The canonical target word is `Q=00010001`.  Reconstructing from `tau_0=+1`
gives

```text
tau=(+,-,+,-,-,+,-,+),
tau_(i+4)=-tau_i.
```

Let `T_4(z)` be translation by four sites on the Bloch fiber and let
`D=diag((-1)^i)`.  There is a small normalization point that matters:

```text
(D*T_4(z))^2=zI,
```

not `I`, on a general fiber.  Choose `xi` with `xi^2=z` and define

```text
J_z=xi^-1 D T_4(z).
```

Direct symbolic multiplication gives

```text
J_z^2=I,
J_z H(z) J_z^-1=-H(z).
```

The `+1` and `-1` eigenspaces of `J_z` both have dimension four.  The two
diagonal compressions of `H(z)` vanish, so in a chiral basis

```text
H(z) = [ 0   B  ],
       [ C   0  ]

H(z)^2 = [ BC   0  ].
         [ 0    CB ]
```

On the unit circle the blocks are adjoint forms `BB*` and `B*B`.  This
explains structurally why the target characteristic polynomial is even and
why the squared problem reduces to four dimensions.

For a legal period-8 word,

```text
tau_(i+4)=-tau_i
```

holds if and only if

```text
Q_(i+4)=Q_i,
product_(i=0)^3 Q_i=-1.
```

There are eight such `Q` vectors and exactly two `D_8` orbits:

| canonical Q | d | spectral classification |
|---:|---:|---|
| `00010001` | 2 | target, `R=eta<8` |
| `01110111` | 6 | `R>8` by the high-defect moment proof |

Thus chiral symmetry explains the even spectral reduction, but chiral
symmetry alone does not imply optimality.  Defect density and geometry remain
essential.

## 8. The Eight-Barrier Trichotomy

Every legal period-8 `Q` has even `d`.

- `d=0` is exactly the cancellation baseline, with `R=8`.
- `d>=4` crosses the barrier by the structural moment inequalities.
- `d=2` has separations `1,2,3,4`; the first three cross the barrier by exact
  moments, while separation four is the Task 40A target with `R=eta<8`.

These cases are disjoint and exhaustive, proving the theorem.

## 9. Independent Relation to Task 40B

Task 40B used 18 `D_8` orbits and 17 endpoint Rayleigh certificates.  The
present route instead uses the local square formula, defect geometry,
closed-walk moments, and the one Task 40A target theorem.  The machine
cross-check expands both routes back to all 128 legal `Q` vectors and finds
zero mismatches:

```text
below eight: 4 vectors,
equal eight: 1 vector,
above eight: 123 vectors.
```

This is a structural second proof of the same period-8 classification, not an
extension to a larger optimization domain.

## 10. Scope and Verification

The result records:

```text
period8_infinite_volume_structural_theorem: PROVED
finite_size_global_optimality: NOT_CLAIMED
all_period_global_optimality: NOT_CLAIMED
all_signings_global_optimality: NOT_CLAIMED
novelty_audit_started: false
paper_manuscript_started: false
```

Run:

```bash
python research/scripts/verify_target_a_period8_structural_mechanism.py
```

Expected status:

```text
TARGET_A_PERIOD8_STRUCTURAL_MECHANISM_PASS
```

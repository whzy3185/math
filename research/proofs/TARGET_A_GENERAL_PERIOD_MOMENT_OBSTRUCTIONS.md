# General-Period Closed-Walk Obstructions

Date: 2026-08-16

Status: **GENERAL_PERIOD_CLOSED_WALK_OBSTRUCTIONS_PROVED**

Component statuses:

```text
GENERAL_PERIOD_CLOSED_WALK_IDENTITIES_PROVED
GENERAL_PERIOD_DEFECT_DENSITY_OBSTRUCTION_PROVED
GENERAL_PERIOD_LOCAL_CLUSTER_OBSTRUCTION_PROVED
```

## Theorem

Let `p>=1`, let `tau_(i+p)=tau_i` take values in `{-1,+1}`, and put

```text
Q_i=tau_i*tau_(i+1).
```

Equivalently, a `p`-periodic flux word has a periodic Hamilton-gauge lift if
and only if

```text
product_(i=0)^(p-1) Q_i=1.
```

Define the cyclic statistics

```text
d=#{i:Q_i=+1},
a=#{i:Q_i=Q_(i+1)=+1},
b=#{i:Q_i=Q_(i+2)=+1},
```

and the exact Bloch moments

```text
M_k(Q)=CT_z tr(H_(p,Q)(z)^(2k)).
```

Then, for every legal period and flux word,

```text
M_1 = 4p,
M_2 = 20p+16d,
M_3 = 118p+168d+96a+48b.
```

If

```text
R(Q)=sup_(|z|=1) rho(H_(p,Q)(z))^2 <= 8,
```

then necessarily

```text
d <= 3p/4,
40d+96a+48b <= 42p.
```

Equivalently, either strict reverse inequality proves `R(Q)>8`.

These conditions are necessary, not sufficient. The theorem does not claim
that the known period-8 target is optimal among all periods or all signings.

## 1. Period-Independent Square Formula

On the infinite lattice the Hamilton-gauge operator is

```text
(A_tau x)_i=x_(i-1)+x_(i+1)
              +tau_(i-2)x_(i-2)+tau_i x_(i+2).
```

Multiplying the four transitions twice gives the complete row of `A_tau^2`:

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

No step in this calculation refers to the cell length. Thus the formula is
an infinite-lattice local identity and remains valid after imposing any
period `p`. The proof script directly multiplies both sides for all 510 sign
words of periods `1,...,8`, checking 3586 rows, including short-cell residue
collisions.

As in the period-8 theorem, `Q_i=-1` cancels its associated odd-distance
couplings, while `Q_i=+1` activates amplitudes of absolute value two.

## 2. Symbolic Closed-Walk Expansion

The four allowed steps are `-2,-1,+1,+2`. A step of length one has weight
one. A `+2` step from `j` has weight `tau_j`, and a `-2` step from `j` has
weight `tau_(j-2)`.

For a closed step word, reduce repeated `tau` factors modulo two. The
remaining number of endpoints is even. If they are

```text
r_1<r_2<...<r_(2s),
```

then

```text
product_j tau_(r_j)
 = product_(ell=1)^s product_(h=r_(2ell-1))^(r_(2ell)-1) Q_h.
```

This converts every signed closed walk into a `Q` monomial without choosing
a period. Exhaustively enumerating the closed words and collecting monomials
up to translation gives:

| walk length | closed words | translation-class coefficients |
|---:|---:|---|
| 2 | 4 | `4` |
| 4 | 36 | `28 + 8Q_i` |
| 6 | 430 | `238 + 156Q_i + 24Q_iQ_(i+1) + 12Q_iQ_(i+2)` |

Summing over the `p` possible starting residues therefore proves

```text
M_1=4p,
M_2=28p+8 sum_i Q_i,
M_3=238p+156 sum_i Q_i
          +24 sum_i Q_iQ_(i+1)
          +12 sum_i Q_iQ_(i+2).
```

Put `I_i=(1+Q_i)/2`. Then

```text
d=sum_i I_i,
a=sum_i I_i I_(i+1),
b=sum_i I_i I_(i+2).
```

Substitution and exact collection yield

```text
M_1=4p,
M_2=20p+16d,
M_3=118p+168d+96a+48b.
```

This derivation explains why no motif beyond single positive fluxes and
pairs at cyclic offsets one and two occurs through length six. It also works
when the offsets coincide modulo a short period: the cyclic products and
indicator identities automatically reduce correctly.

## 3. Moment Barrier

Constant-term extraction equals normalized Bloch-phase averaging. Since each
fiber is Hermitian,

```text
M_k=(1/(2*pi))*integral tr(H(e^(i theta))^(2k)) dtheta
   =(1/(2*pi))*integral sum_j lambda_j(theta)^(2k) dtheta.
```

If `R(Q)<=8`, then `y_j(theta)=lambda_j(theta)^2` lies in `[0,8]`, so

```text
y_j^(k+1)<=8y_j^k.
```

Summing and integrating proves `M_(k+1)<=8M_k`. For the first two excesses,

```text
F_1=M_2-8M_1=16d-12p,
F_2=M_3-8M_2=-42p+40d+96a+48b.
```

Consequently,

```text
R(Q)<=8  ==>  d<=3p/4,
R(Q)<=8  ==>  40d+96a+48b<=42p.
```

The first inequality is a defect-density obstruction. The second detects
both density and clustering: adjacent positive-flux pairs carry coefficient
96, and distance-two pairs carry coefficient 48.

Only the strict contrapositive is used. A nonpositive `F_k` does not prove an
upper bound, and satisfying both displayed inequalities does not prove
`R(Q)<=8`.

## 4. Exact Machine Checks

The theorem generator performs the following checks:

- all 4095 legal `Q` words for periods `1,...,12`;
- 320 deterministic samples at periods `13,17,24,31,48`;
- translation, reflection, and `tau -> -tau` invariance;
- an independent integer Laurent-polynomial computation of
  `CT_z tr(H(z)^(2k))` for all 63 legal words of periods `1,...,6`;
- direct infinite-lattice `A^2` multiplication through period 8.

The checker does not import the theorem generator. It independently
re-enumerates closed words by recursive traversal, rechecks all legal words
through period 10, and uses a separate random seed at larger periods. No
floating-point quadrature is used.

## 5. Scope

Proved:

```text
arbitrary-period first three moment identities,
arbitrary-period necessary density obstruction,
arbitrary-period necessary local-cluster obstruction.
```

Not claimed:

```text
sufficiency of either obstruction,
global optimality among all periodic phases,
finite-size global optimality,
global optimality among all signings,
an M_4 local-motif theorem.
```

The optional `M_4` exploration was left outside this theorem package because
the first three moments already produce two concise structural obstructions;
Task 42B is the next controlled extension.

Run:

```bash
python research/scripts/target_a_general_period_moments.py
python research/scripts/verify_target_a_general_period_moments.py
python -m pytest -q research/scripts/test_target_a_general_period_moments.py
```

Expected final checker status:

```text
TARGET_A_GENERAL_PERIOD_MOMENTS_PASS
```

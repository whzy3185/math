# Task 56 Lane C: Finite Obstructions For `B0 -> B2` Cores

## Status And Baseline

This report records analytic progress on the universal finite-core question

```text
every B0 -> B2 core has sup sigma(A^2) >= c6.                 (U)
```

Statement (U) remains `OPEN`.  No experiment below is promoted to a theorem.
The baseline used here is the corrected one: one G6 interface has rank two,
`r` separated interfaces have exactly `2r` levels, their proved displacement
bound is `3505r(9/25)^ell`, and `N_exp=3120`.  The complete even-order
classification is failure exactly at `n=32`, `n=40`, and every even
`n>=48`.  None of those facts is changed below.

Write a core as consecutive positive gaps `g=(g_1,...,g_m)`.  Defects have
`Q_i=1`, other sites have `Q_i=-1`, and

```text
tau_(i+1)=Q_i tau_i,
(Av)_k=v_(k-1)+v_(k+1)+tau_(k-2)v_(k-2)+tau_k v_(k+2).       (1)
```

We use the certified strict upper endpoint

```text
c6 < u6 := 7905369311620328/10^15.                          (2)
```

For the other `tau` lift, with `(Dv)_i=(-1)^i v_i`, direct substitution in
(1) gives

```text
A_(-tau)D=-DA_tau.                                          (3)
```

Thus every finite-support calculation below applies to both lifts.

## Lemma 1: A Unit Gap Is A Uniform Local Obstruction

Suppose two consecutive defects occur at `x,x+1`.  Then, independently of
all other defects,

```text
sup sigma(A^2) >= 44/5 > c6.                                (4)
```

### Proof

Translate `x` to zero, choose `tau_0=1`, and put `v_i=1` for
`0<=i<=4`, with all other coordinates zero.  Only

```text
Q_-2,Q_-1,Q_2,Q_3
```

are not fixed by the two consecutive defects and can enter `Av`; each is an
arbitrary sign.  Substitution in (1) over the full image interval `[-2,6]`
gives

```text
||v||^2=5,             ||Av||^2 in {44,48,52}.
```

For example, the minimizing absolute-coordinate pattern is

```text
(1,0,2,3,4,3,2,0,1),
```

whose squared norm is `44`.  The four arbitrary signs give only sixteen
cases; changing either left sign can only replace a boundary cancellation by
a contribution of absolute value two, and changing either right sign has the
same effect.  Hence the displayed set is exhaustive.  Finally,

```text
44/5-u6 = 111828836047459/125000000000000 > 0.
```

Equation (3) proves the claim for the other lift, and the variational
principle proves (4).  In particular, a core with spectral top at most `c6`
contains no gap `1`.  QED.

## Lemma 2: Five Small-Gap Pair Obstructions

Suppose three consecutive defects have gaps `(a,b)`, where, up to reflection,

```text
(a,b) in {(2,2),(2,3),(2,5),(3,5),(5,5)}.                   (5)
```

Then `sup sigma(A^2)>c6` independently of the rest of the core.  The already
proved arbitrary-length `(3,3)` lemma supplies the sixth unordered pair in
the alphabet `{2,3,5}` and gives the stronger bound `419/53>c6`.

### Proof

Put the three defects at `0,a,S`, where `S=a+b`, and fix `tau_0=1`.
Coordinates in the following table are ordered on `[-2,S+2]`.  Direct use of
(1) on the full interval `[-4,S+4]` gives the stated denominator and the
complete set of possible numerators.

| `(a,b)` | integer vector `v` | `D=||v||^2` | possible `N=||Av||^2` | `min N/D` |
|---|---|---:|---|---:|
| `(2,2)` | `(0,0,0,1,1,0,0,-1,-1)` | 4 | `{32}` | `8` |
| `(2,3)` | `(2,-1,6,2,1,8,-6,2,-4,4)` | 182 | `{1472,1476,1480,1484,1488,1492}` | `736/91` |
| `(2,5)` | `(0,0,1,-1,-2,3,-3,3,-1,2,-2,2)` | 46 | `{370,374}` | `185/23` |
| `(3,5)` | `(2,-1,5,7,5,11,8,10,9,1,6,6,6)` | 579 | `{4640,4648,4708,4716,4752,4760,4820,4828}` | `4640/579` |
| `(5,5)` | `(1,0,3,3,3,4,0,4,4,4,4,0,2,2,2)` | 120 | `{986,1010,1034,1058}` | `493/60` |

Here is the finite closure behind the table.  Consecutiveness fixes `Q` at
every site from `0` through `S`.  For a vector on `[-2,S+2]`, all remaining
dependence consists exactly of

```text
(Q_-4,Q_-3,Q_-2,Q_-1,Q_(S+1)) in {-1,1}^5.                 (6)
```

More distant defects cannot occur in a coefficient multiplying a nonzero
coordinate in (1).  Expanding the five displayed integer vectors for the 32
sign choices in (6), collecting equal squared norms, gives exactly the five
numerator sets in the table.  This is an exhaustive algebraic substitution,
not a spectral computation.  The smallest quotient in the table is `8`, and
by (2)

```text
8-u6 = 11828836047459/125000000000000 > 0.                 (7)
```

All other rows are larger.  Reflection handles the reversed pairs, (3)
handles the other lift, and the variational principle completes the proof.
QED.

## Lemma 3: A Gap Of Length At Least 45 Is A Uniform Obstruction

If two consecutive defects are separated by a gap `g>=45`, then

```text
sup sigma(A^2) >= 18061/2283 > c6.                          (8)
```

### Proof

Translate the left defect to zero.  On the 43 sites `3,...,45`, take the
vector whose coordinates, in order, are

```text
(-5,0,-8,0,-12,0,-15,0,-18,0,-21,0,-23,0,-25,0,-26,0,
 -27,0,-28,0,-28,0,-27,0,-26,0,-25,0,-23,0,-21,0,-18,0,
 -15,0,-12,0,-8,0,-5).
```

Because the two defects are consecutive and `g>=45`, all sites `1,...,44`
are nondefects.  Hence every `tau` coefficient that multiplies this vector
alternates in sign; the endpoint defect at `45` is not used in forming
`tau_45`.  Substitution in (1), including the two outgoing coordinates on
each side, gives exactly

```text
||v||^2=9132,             ||Av||^2=72244,
72244/9132=18061/2283.
```

The opposite alternating phase has the same quotient by (3) (indeed this
vector is supported on one parity).  The exact strict margin is

```text
18061/2283-u6
 = 1630232696348897/285375000000000000 > 0.                (9)
```

The variational principle proves (8).  QED.

## Corollary: A Finite-Alphabet Obstruction For The Open Class

Let `g` be a primitive multi-gap `B0 -> B2` core with at least two gaps and
suppose `sup sigma(A_g^2)<=c6`.  Then all of the following are necessary:

1. `sum g_i>=22`.  The `B0 -> B2` congruence gives
   `sum g_i=2 mod 4`, while the support-18 certificate proves strict
   inequality above `c6` for every primitive core with total support
   `2,6,10,14,18`.
2. Every gap lies in `{2,3,5,6,...,44}`.  Gap `4` contradicts primitivity,
   gap `1` is excluded by Lemma 1, and gaps at least `45` are excluded by
   Lemma 3.
3. The word has no adjacent pair whose two letters both lie in `{2,3,5}`.
   Lemma 2, reflection, and the inherited `(3,3)` lemma exclude all six
   unordered pairs.
4. Consequently the word contains at least one letter in `{6,...,44}`.

This is a genuine finite obstruction: the unresolved universal problem is
reduced from an unbounded gap alphabet to a 42-letter alphabet, with a
nontrivial forbidden sublanguage.  It is not a finite enumeration, because
the word length is still unbounded.

## Blocker And Honest Boundary

The support-18 certificate cannot simply be applied to a contiguous subword:
its witness uses the period-four completions at both endpoints, while an
embedded subword receives different boundary `Q` data.  Likewise, deleting
or inserting a reference cell multiplies boundary data by a non-scalar bulk
monodromy and is not a spectral equivalence.  These are exact blockers to the
naive terminating-replacement argument.

The lemmas above do not exclude arbitrarily long primitive words over

```text
{2,3,5,6,...,44}
```

that obey the forbidden-pair rule and have total support `2 mod 4`.  No
monotone local replacement for those words is proved here, and no universal
`B0 -> B2` lower theorem is claimed.  The next logically valid target is a
boundary-robust motif certificate for pairs involving `{6,...,44}`, followed
by a terminating finite-state argument; until both pieces are independently
checked, (U) remains `OPEN`.

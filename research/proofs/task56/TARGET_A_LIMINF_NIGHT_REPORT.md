# Certified-Local Subclasses of the Common-Liminf Problem

Status: certified-local liminf theorem `PROVED`; restricted tight,
dichotomy, and normalized-vanishing subclasses `CLOSED`; unrestricted
common-residue liminf `OPEN`.

## 1. Purpose and corrected baseline

This report asks whether the complete finite-order classification and the
Task 55 support-18 and `(3,3)` interface theorems close a nontrivial part of
the common-liminf problem.  The answer is yes, but only after the covered
class is stated as a local occurrence condition.  The resulting theorem does
not require spectral decoupling or deletion of reference cells.

The structural baseline used here is the corrected one:

```text
one G6 interface has H=A^2 eigenspace rank 2;
r separated interfaces have exactly 2r levels in the certified cluster;
|lambda-c6| < 3505 r (9/25)^ell;
N_exp=3120.
```

The exact finite-order classification is

```text
failure exactly at n=32, n=40, and every even n>=48.       (1)
```

Neither the rank count nor the exponential estimate is needed below.

## 2. Certified local classes

Use the Target A tree gauge

```text
(A v)_k=v_(k-1)+v_(k+1)+tau_(k-2)v_(k-2)+tau_k v_(k+2),  (2)
```

and call the sites with `Q_k=+1` defects.  Their cyclic successive distances
are the defect gaps.

Define `C_33(n)` to be the legal order-`n` signings whose cyclic gap word
contains two consecutive gaps `(3,3)`.  Thus, after translation, three
consecutive defects occur at `0,3,6`.  For `n>14`, the support and image
windows used below embed injectively in the ring.

Let `G_18` be the 31,008 reflection-canonical primitive words

```text
g=(g_1,...,g_m),  m>=2,
sum g_i in {2,6,10,14,18},
```

certified in Task 55.  Define `C_18^loc(n)` as follows.  A signing belongs to
this class if, for some `g in G_18`, translation, orientation, and one of the
two `tau` lifts identify an injective ring interval with the exact
open-interface coefficient window used by the Task 55 certificate:

```text
I_g=[-2,S+2],       J_g=[-4,S+4],       S=sum g_i,          (3)
```

and the map from vectors supported on `I_g` to their full images on `J_g`
is the certified integer matrix `C_g`.  This is a local-copy condition, not a
claim that period-four reference cells may be inserted or deleted.  In gap
language it says that the actual core and the finite amount of adjacent bulk
seen by (3) agree with the open-interface completion, without contracting
any zero-charge subword.

Finally set

```text
C_cert(n)=C_33(n) union C_18^loc(n).                       (4)
```

## 3. Certified-local liminf theorem

### Theorem

Let `A_j` be legal signed adjacency matrices on rings of orders `n_j` tending
to infinity.  If `A_j in C_cert(n_j)` for every sufficiently large `j`, then

```text
liminf_j rho(A_j)^2 >= 419/53 > c6.                        (5)
```

If the stronger hypothesis `A_j in C_18^loc(n_j)` holds eventually, then

```text
liminf_j rho(A_j)^2 >= 2930/369 > 419/53 > c6.             (6)
```

Both conclusions remain true if the certified occurrence drifts around the
ring or if its distance from a fixed external root tends to infinity.

### Proof

First suppose `A_j in C_33(n_j)`.  Root at an occurrence with defects at
`0,3,6`.  Task 55 gives one of three explicit integer vectors supported on
`[-2,8]`, selected only by whether the preceding gap is `1`, `2`, or at
least `3`.  Its complete image under (2) is supported on `[-4,10]`.  The
finite dependency audit covers all five locally distinct predecessor cases,
all relevant earlier defects, both successor cases, and both `tau` lifts.
Consequently, for every sufficiently large `j`, the vector embeds without
wrap-around and satisfies

```text
||A_j v_j||^2 / ||v_j||^2 >= 419/53.                       (7)
```

Since `A_j` is self-adjoint,

```text
rho(A_j)^2=||A_j^2||
            >= <v_j,A_j^2 v_j>/<v_j,v_j>
            = ||A_j v_j||^2/||v_j||^2.
```

This proves (5) in the `(3,3)` case.

Now suppose `A_j in C_18^loc(n_j)`.  By definition the relevant local map is
exactly `C_g`, up to a translation, reflection, or the alternating unitary
which exchanges the two `tau` lifts.  The stored integer witness therefore
has exactly the same numerator and denominator on the finite ring as on the
bilateral open interface.  The complete enumeration found the unique weakest
quotient

```text
min_(g in G_18) ||C_g v_g||^2/||v_g||^2 =2930/369.         (8)
```

The same variational argument proves (6).  Finally,

```text
2930/369 - 419/53 = 679/19557 >0,
419/53 - 7905369311620328/10^15
  =1928310515327/6625000000000000 >0,
```

and the certified upper endpoint in the second line is strictly above `c6`.
Thus both bounds are strict above `c6`, completing the proof.

The proof is deliberately local.  It neither passes through a limiting
operator nor assumes that distant components decouple.

## 4. Consequences for the concentration-compactness branches

The theorem closes the following genuine subclasses.

### Tight certified cores

Suppose the unnormalized compactness masses are uniformly bounded, the
sequence is tight, and its actual finite `B0 -> B2` core, with no spectral
deletion of reference cells, eventually belongs to `G_18`.  Tightness places
the whole core in a bounded interval and the complementary ring arc tends to
infinite length.  Hence the finite coefficient window (3) eventually agrees
with its open-interface completion.  Equation (6) follows.  This closes the
support-18 part of `TIGHT_CLUSTER_BLOCKER`.

The same conclusion holds without bounded total mass whenever a tight core
contains `(3,3)`, by (7).  It does not classify tight motif-free cores of
support greater than 18, nor tight infinite or semi-infinite excursions.

### Dichotomy with one certified component

Suppose a dichotomy sequence has a component whose distance from every other
component tends to infinity and whose actual local core is in `G_18`.  The
growing period-four buffer realizes (3), so that one component alone supplies
the witness in (6).  No estimate on the interaction between the two
components is required.  More generally, any dichotomy sequence containing
`(3,3)` in either component obeys (5), even without using the separation.

This closes the certified-component part of `DICHOTOMY_BLOCKER`.  It does not
show that every charged component contains a certified core.

### Motif-bearing normalized vanishing

Normalized vanishing does not remove local integer mass; it says only that
the mass in each fixed ball is negligible after division by the total mass.
If every sufficiently large ring nevertheless contains one `(3,3)` motif,
root at that motif and apply (7).  Therefore every motif-bearing normalized-
vanishing sequence satisfies the strict bound (5).  The same argument covers
a vanishing sequence containing any local copy from `C_18^loc`.

This is a nontrivial closed part of `VANISHING_BLOCKER`: the witness may drift
to infinity and its normalized mass may tend to zero, but its unnormalized
Rayleigh quotient remains fixed.  Motif-free vanishing remains uncontrolled.

## 5. Exclusion from eventual minimizing sequences

For `r in {2,4,6}`, let `A_k` be an exact minimizer at order `8k+r`, so that

```text
rho(A_k)^2=m_(8k+r)^2.
```

The already proved explicit G6 constructions give

```text
limsup_(k->infinity) m_(8k+r)^2 <=c6.                     (9)
```

Combining (5) with the strict gap `c6<419/53` yields the following structural
corollary:

```text
for every r in {2,4,6}, every exact minimizing signing is eventually
outside C_cert(8k+r).                                    (10)
```

Indeed, (9) implies `m_(8k+r)^2<419/53` for all sufficiently large `k`,
whereas membership in `C_cert` would imply the opposite inequality.  Thus
the new local theorems rigorously prune all three concentration-compactness
branches, but they also show that an asymptotic minimizer must live in the
remaining motif-free, non-certified class.

## 6. Blocker proposition: why the unrestricted liminf does not follow

### Proposition

The finite-order classification (1), the complete support-18 theorem, and
the arbitrary-length `(3,3)` lemma do not compose to prove

```text
liminf_(k->infinity) m_(8k+r)^2 >=c6,
r in {2,4,6}.                                             (11)
```

After adding the known upper bound (9), their strongest universal consequence
for minimizers is the exclusion statement (10), not (11).

### Proof

There are two independent missing implications.

First, (1) decides only whether

```text
m_n^2 < rho_-(n)^2,
```

and does not give a lower bound for `m_n^2` or classify a minimizing signing.
Moreover `rho_-(n)^2` tends to `8`, which is strictly above `c6`.  Therefore
the truth value of this comparison supplies no inequality in the direction
required by (11).  A finite number of exceptional orders is irrelevant to a
liminf, while the all-orders tail in (1) is an existence/upper-bound result.

Second, the local theorems have hypotheses.  They cover exactly the presence
of a certified support-18 open-interface window or a `(3,3)` occurrence.
No accepted result proves that every legal signing, every near-minimizer, or
one component in every tight/dichotomy/vanishing decomposition has either
property.  In particular, motif-free primitive cores with support greater
than 18, non-isolated concatenations, infinite tight excursions, and
aperiodic words remain outside (4).  Insertion or deletion of a period-eight
reference cell cannot bridge this gap because its bulk monodromy is
non-scalar and the operation is not a spectral equivalence.

Finally, (9) and the strict local gap prove that large exact minimizers avoid
rather than satisfy the local hypotheses, as shown in (10).  Thus applying
the support-18 or `(3,3)` theorem to an arbitrary contradiction sequence
would be circular: the required occurrence is precisely what has not been
proved and is eventually forbidden for actual minimizers.  This establishes
the claimed dependency blocker.

## 7. Exact remaining target

The unrestricted common liminf remains `OPEN`.  After this report, its hard
class can be stated more sharply: an asymptotic minimizing sequence may be
assumed eventually to have

```text
no cyclic `(3,3)` motif;
no local open-interface copy of any of the 31,008 certified cores;
and no justified reference-cell contraction reducing it to such a core.
```

A next theorem must act on that complement.  Sufficient routes include a
uniform local witness for every motif-free primitive core beyond support 18,
a transfer-monodromy replacement lemma that retains reference propagation,
or a coercive spectral estimate for motif-free vanishing/aperiodic words.
Until one of these supplies coverage rather than bounded enumeration, (11)
cannot be promoted.

## 8. Dependencies and evidence level

- Task 54 pointed compactness and charge concentration-compactness.
- Task 55 `TARGET_A_MULTIGAP_SUPPORT18_THEOREM.md` and its independent
  certificate checker.
- Task 55 `TARGET_A_THREE_THREE_LOCAL_LEMMA.md`, including the 32-case local
  dependency closure and both `tau` lifts.
- The proved nonzero-residue upper bound (9).
- The complete even-order classification is used only in the blocker audit;
  it contributes no lower-bound step.

No formal manuscript is modified, and no claim here depends on the
falsified exact-`r`, codimension-`r`, rank-one G6, or `r x r` Feshbach
statements.

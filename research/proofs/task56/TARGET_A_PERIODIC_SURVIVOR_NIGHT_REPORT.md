# Target A Periodic Survivor Night Report

Status: `EXACT_FINITE_READ_ONLY`; structural tail lemma `OPEN`.

## 1. Scope and baseline

This lane analyzes only the existing bounded period-25/26 moment-survivor
computation.  It does not enumerate period 27 or higher and does not modify a
formal manuscript.

The active baseline is the corrected Task 55 baseline: one `G6` block has
rank two; `r` interfaces give exactly `2r` localized levels; the quantitative
bound is

```text
3505 r (9/25)^ell,
```

with `N_exp=3120`.  The complete even-order classification is failure exactly
at `n=32`, `n=40`, and every even `n>=48`.  None of those results depends on
the present periodic-survivor observation.

## 2. Bounded exact recovery

At repository head `c26c18f9077f184b8a62684baf2feb1e099edccc`, the inherited
function

```text
target_a_high_period_moments_task47.analyze_period((p,16))
```

was run in memory for `p=25,26`.  No output artifact was written and no
unbounded enumeration was launched.  Two complete executions returned the
same summary:

| `p` | canonical dihedral orbits | represented legal words | expected legal words | `F_1,...,F_16` survivors |
|---:|---:|---:|---:|---:|
| 25 | 337,594 | 16,777,216 | 16,777,216 | 58 |
| 26 | 649,532 | 33,554,432 | 33,554,432 | 95 |

For both periods the implementation reported all three exact internal checks
as true: orbit multiplicity is complete, the first-positive/survivor
partition is complete, and the survival curve is nonincreasing.  These counts
are therefore reproducible from the checked-in deterministic source, but they
remain `EXACT_FINITE_READ_ONLY`: this lane did not supply a second independent
orbit generator, a serialized partition, or an independent checker.

The exact survivor defect-count distribution was

| `p` | number `d` of `+` entries | survivor count |
|---:|---:|---:|
| 25 | 1, 3, 5, 7 | 1, 8, 37, 12 |
| 26 | 0, 2, 4, 6, 8 | 1, 4, 30, 51, 9 |

Thus every period-25 survivor has `d<=7`, and every period-26 survivor has
`d<=8`.

## 3. Common local motif

Write `-` for `Q_i=-1` and read words cyclically.  Direct intersection of the
cyclic window sets of all 153 recovered survivors gives

```text
length 1:  -
length 2:  --
length 3:  ---
length 4 through 12: no common literal window.
```

In particular, the longest common literal local motif is

```text
---,  equivalently  Q_i=Q_(i+1)=Q_(i+2)=-1.             (H1)
```

In the lifted signing this is the alternating four-site segment

```text
(tau_i,tau_(i+1),tau_(i+2),tau_(i+3))=(s,-s,s,-s).
```

The finite observation (H1) also has a short combinatorial proof once the
recovered defect-count bounds are accepted.  If a cyclic word with `d>0`
contained no `---`, every run of minus signs would have length at most two.
There are `d` such cyclic runs, so `p-d<=2d`, hence `p<=3d`.  This contradicts
`25>3*7` at period 25 and `26>3*8` at period 26.  The all-minus period-26
survivor contains (H1) trivially.

The length-three conclusion is sharp for this data.  The all-minus survivor
forces any common length-four word to be `----`, while, for example, the
period-25 survivor with canonical code `2236965` has cyclic word
`1010010001000100010001000` and longest minus run three.  Hence no literal
length-four word occurs in every survivor.

## 4. What this does not prove

The motif (H1) is not yet a spectral tail lemma.  The period-eight equality
word `+---+---` itself contains (H1), so the mere presence of `---` cannot
imply a strict Rayleigh bound above `c6`.  It also cannot distinguish one
copy of the equality phase from a nonperiodic concatenation.  Consequently
this report proves neither a uniform gap above `c6` nor closure of the
periodic frontier beyond `p<=24`.

The strongest reusable proved statement from this lane is the elementary
conditional lemma:

```text
If a cyclic sign word of length p has d<p/3 plus entries, then it contains
the local tau motif (s,-s,s,-s).
```

Its application to all 153 rows still depends on the read-only finite
classification above.

## 5. Blocker and next structural target

A useful tail argument must retain context around (H1).  The next bounded
question is to classify the two symbols immediately outside each maximal
minus run and derive a finite family of contextual motifs, then construct an
exact local Rayleigh numerator for each family.  Any proposed family must
separate the equality context `+---+---` from a strict-improvement context.

Until that contextual classification and its exact local quadratic-form
proof exist, the structural periodic-tail statement remains `OPEN`.  Extending
the period enumeration alone would not close this blocker.

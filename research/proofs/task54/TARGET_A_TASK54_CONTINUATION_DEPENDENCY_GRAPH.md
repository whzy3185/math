# Target A Task 54 Continuation Dependency Graph

## Superseded Cluster Chain

```text
Task 53 global single-G6 edge c6
        +
Task 54 exact G6 isolation delta6=1/100, rank(c6)=2
        +
old one-mode-per-interface complement partition
        v
codimension-r complement cap [NOT PROVED]
        +
localized G6 quasimodes
        v
exact-r count and rank-r Riesz cluster [FALSIFIED]
        +
problem-specific r x r Feshbach reduction [OPEN]
        v
qualitative exponential global cap [OPEN PENDING 2r REPAIR]
```

The abstract Schur identity and the cutoff arithmetic survive. A corrected
chain must use two modes per interface, a codimension-`2r` complement, and a
`2r x 2r` effective matrix.

Independently,

```text
Task 53 IMS identity and local patch classification
        +
exact tent translation sums and residue separations
        v
global IMS error (240R-342)/(R(2R^2+1)) <= 120/R^2
        v
N_IMS=240
```

and

```text
structured witnesses for every even 48<=n<240
        +
exact full-matrix positive-definiteness certificates
        +
independent natural-order LDL checker
        v
N_finite=48
```

give the integrated result

```text
N_Task53=2500, N_IMS=240, N_finite=48
        v
N_star=48.
```

Here `N_star` is the start of a rigorously covered explicit-witness tail, not
a proof of globally minimal onset.

## Interaction chain

```text
exact-2r + codimension-2r complement + Feshbach [OPEN]
        v
T1=O((9/25)^ell), R2=O((9/25)^(2ell)).
```

Explicit leading coefficients, global simplicity, and a complete splitting
law remain `OPEN`.

## Lower-bound chain

```text
pointed compactness + finite-support form transfer
        v
||H_infinity|| <= liminf ||H_j||
        +
charge concentration-compactness
        v
TIGHT / DICHOTOMY / NORMALIZED_VANISHING analysis
        +
multi-gap interfaces + reference excursions + single-gap hierarchy
        v
common-residue liminf.
```

The final arrow is not established.  Tight non-G6 clusters, dichotomy into
non-G6 components, normalized vanishing, sparse escaped charge, and aperiodic
limits are explicit blockers.

## Bounded evidence

Task 53's complete primitive periodic frontier remains `p<=24`.  Any extension
past 24 is a separate exact-finite classification problem and is not a
dependency of the accepted Task 54 threshold theorem.

# Full Proof Of Registry Validity

This document proves the registry contract in
[THEOREM_STATEMENT.md](THEOREM_STATEMENT.md). It is a proof of canonical-layer
consistency relative to the accepted corpus, not a replacement for the full
mathematical proofs cited by the evidence matrix.

## 1. Stable And Disjoint Namespace

The namespace is divided by mathematical role:

- `T1`-`T8`: setup and theorem spine;
- `A`: supporting appendix theorems;
- `C`: explicit finite computer-assisted lemmas;
- `O`: open statements;
- `R`: exact but non-promoted finite evidence;
- `X`: falsified statements.

These prefixes are disjoint. Within each prefix every identifier occurs once
in the [inventory](../TARGET_A_FINAL_CLAIM_INVENTORY_V2.md). Therefore no
accepted statement has two competing canonical IDs, and no open or falsified
statement shares an accepted ID.

## 2. Evidence Assignment

Every accepted `T`, `A`, or `C` row has exactly one label from the registered
evidence vocabulary. The evidence matrix supplies:

- a human proof path;
- the machine component, if any;
- producer, checker, and certificate fields;
- mathematical dependencies;
- quantified scope;
- paper placement.

For `PURE_ANALYTIC_PROVED`, the machine fields are `N/A` or explicitly
corroborative. For `COMPUTER_ASSISTED_PROVED`, the finite object and an
independent checker are named. For an analytic consequence of a certified
premise, the label is `ANALYTIC_COROLLARY_OF_CERTIFIED_INPUTS`; this prevents
the deduction from being misrepresented as computation-free while preserving
the human nature of the final implication.

Thus the evidence label and the logical role of computation agree.

## 3. Mathematical Closure

The dependency graph is acyclic by its displayed layers.

1. `T1` contains analytic leaves.
2. `T2` and `T3` depend only on `T1` and the explicit Bloch-polynomial lemma.
3. `T4` depends on the reference phase, the algebraic `c6` isolation, and the
   finite physical-matching lemma `C.6`.
4. `T5` depends on `T4` and exact finite witness lemma `C.8`.
5. `T6` depends on earlier layers, the analytic IMS identity, and `C.7`.
6. `T7` depends on charge closure, localization, and finite bridge `C.5`.
7. `T8` depends on `C.1`-`C.5` and the tail `T7.3`.

No edge returns to an earlier layer. Every main theorem therefore terminates
at an analytic identity or an explicit finite exact lemma.

## 4. Exhaustiveness Of The Main Classification Node

The domain is the even integers `n>=8`. Partition it into

```text
8<=n<=30,
n=32,
n in {34,36,38,40,42,44,46},
48<=n<240,
n>=240.
```

The first region is closed by `C.1`; `n=32` by `C.2`; the six true orders in
the third region by `C.3`; `n=40` by `C.4`; the fourth region by `C.5`; and
the final region by the analytic IMS tail using the certified bulk and G6
edges. The regions are disjoint and exhaustive. Their truth values yield

```text
failure exactly at n=32, n=40, and every even n>=48.
```

This proves that `T8.4` is registered with the correct scope and dependency
set.

## 5. Rank-Two Consistency

`T4.3` records `dim ker(H_6-c6)=2`. Every downstream cluster statement uses
two localized columns per interface. The exact-count node is `T6.3` and says
`2r`; the Feshbach node is `T6.4` and says `2r x 2r`. The incompatible
rank-`r` statements are placed in `X.1` and `X.2`, not in the accepted set.

Therefore the accepted namespace contains no internal rank-one/rank-two
contradiction.

## 6. Quantifier Safety

The single-gap theorem `T5.1` quantifies over one positive abnormal gap, both
lifts, and both orientations. It does not quantify over arbitrary finite-core
words. The residue theorem `T7.2` is a `limsup` upper statement and has no
lower-bound edge. The periodic theorem `A.3` stops at primitive period 24.
The finite-alphabet reduction `A.6` is necessary, not sufficient.

Accordingly, universal interface optimality, common limits, and all-period
classification remain in `O.1`-`O.4` or `R.1`-`R.2` and cannot be inferred
from an accepted row.

## 7. Editorial Closure

Every accepted theorem family is assigned to `MAIN_TEXT`, `APPENDIX`, or
`REPRODUCIBILITY`, and the
[architecture](../TARGET_A_JGT_PROOF_ARCHITECTURE.md) maps each family to a
section. The [theorem hierarchy](../TARGET_A_JGT_THEOREM_HIERARCHY.md) gives
human-readable theorem names and removes chronological labels from the paper
story.

The registry contract follows.

# Reference-Relative Cost: Finite Graph Evidence

Status: `EXACT_FINITE_READ_ONLY`; no spectral lower-bound theorem is claimed.

## 1. Statement

The raw `c6`-weighted moment/coboundary architecture from Task 53 is
falsified: the period-eight reference cycle itself has the wrong strict sign.
Task 55 therefore studies only a reference-calibrated finite graph in which a
full reference traversal has cost zero.

The read-only computation uses the inherited finite-memory grammar with

```text
base graph:       105 states, 164 directed edges,
four-phase lift:  420 states, 656 directed edges.     (1)
```

For each of the calibrated forms `F4` and `F5`, the read-only exact graph
calculation found

```text
no negative directed cycle,
only the reference cycle orbit at zero cost.           (2)
```

Here "reference cycle orbit" includes the phase copies of the same
period-eight traversal. Statement (2) is finite relative-cost evidence. It is
not an operator inequality and is not integrated as a computer-assisted
theorem because no producer artifact or independent checker is present.

## 2. Evidence

The state and edge counts in (1) agree with the established overlap grammar
and its four-phase lift. The read-only search used exact edge arithmetic for
cycle comparison, rather than accepting a floating negative-cycle tolerance.
It exhausted the stated finite graph and reported no nonreference zero cycle
for either `F4` or `F5`.

The admissible evidence label is therefore exactly
`EXACT_FINITE_READ_ONLY`. It records a reproducible research target and may
guide a future certificate design, but it does not change the integrated
Task 53 conclusion `CURRENT_LOCAL_GRAMMAR_INSUFFICIENT`.

## 3. Exact limitation

No implication of the form

```text
relative graph cost >=0  =>  sup sigma(H)>=c6          (3)
```

has been proved. In particular:

- `F4` and `F5` are finite-memory moment functionals, not the spectral top;
- nonnegative total cost need not provide a localized Rayleigh witness;
- a positive cost for one excursion can be diluted by arbitrarily long
  reference runs;
- the finite graph does not classify arbitrary transfer-matrix boundary data;
  and
- no additivity or coercivity theorem connects the cost to concatenated
  interface cores.

The reference-cell insertion/removal spectral-equivalence claim is
`REJECTED`. A period-eight reference cell multiplies the boundary transfer
data by a non-scalar bulk monodromy. Deleting or inserting that cell can
change matching and spectrum even though its calibrated additive graph cost
is zero. Cost contraction is therefore not spectral contraction.

## 4. Dependencies

- The 105-state/164-edge grammar and the chosen four-phase lift.
- Exact definitions and normalization of the calibrated `F4` and `F5` edge
  weights.
- The period-eight reference orbit used to fix zero cost.
- No dependency on the withdrawn exact-`r` interaction theory.

Because the read-only run did not emit a committed manifest, edge table,
potentials, digests, or checker transcript, those items remain missing proof
dependencies rather than implicit facts.

## 5. Next lemma

First produce a strict finite graph certificate: serialize all lifted states
and edges, exact `F4/F5` weights, a shortest-path potential proving reduced
weights nonnegative, and an exact classification of all zero cycles as the
reference orbit. An independent checker must rebuild the graph and reject
missing or duplicate edges.

The mathematical next lemma must then bridge graph cost to spectrum. A useful
form would assign every primitive nonreference excursion a finitely supported
vector `v` and prove, with a uniform function `Phi`,

```text
||Av||^2-c6_upper ||v||^2 >=Phi(relative cost)>0.       (4)
```

Without such a bridge, (2) remains finite combinatorial evidence only.

# Reference Excursion Rigidity: Exact Finite Scope

Status: finite graph conclusion `EXACT_FINITE_READ_ONLY`; universal excursion
rigidity and every spectral consequence are `OPEN`.

## 1. Statement

Fix the Task 55 four-phase lifted reference-relative graph. A closed walk is
called reference if every cycle in its directed-cycle decomposition belongs
to the period-eight reference orbit. A primitive excursion is a closed walk
that leaves the reference orbit and contains no smaller closed
nonreference subwalk after its reference portions are removed
combinatorially.

The read-only finite computation supports the following bounded statement for
each calibrated weight `F in {F4,F5}`:

```text
every nonreference directed cycle has Cost_F>0;         (1)
every directed cycle has Cost_F>=0.                     (2)
```

Consequently every closed walk whose cycle decomposition includes a
nonreference cycle has strictly positive total `F`-cost. This conclusion is
about the finite lifted graph only.

## 2. Proof of the finite graph implication

Assume the reported exact cycle classification: there is no negative cycle,
and every zero cycle lies in the reference orbit. Any closed directed walk in
a finite graph decomposes into directed simple cycles, with additive total
weight. Every summand is nonnegative. If the walk contains a nonreference
cycle, at least one summand is positive, proving (1)--(2) for the walk.

This deduction is exact once the edge table and cycle classification are
accepted. The present evidence remains `READ_ONLY`, however, because the
underlying table and an implementation-independent checker have not been
integrated.

## 3. What rigidity does and does not mean

Within the finite grammar, (1) excludes a zero-cost nonreference periodic
excursion. It also suggests a finite positive gap between zero and the cost
of a nonreference simple cycle after a common rational normalization.

It does not show any of the following:

1. a uniform positive cost per site for walks containing long reference runs;
2. positivity for an aperiodic bi-infinite word;
3. a lower bound on `sup sigma(H)`;
4. a complete classification of finite-core `B0 -> B2` interfaces;
5. that an excursion can be deleted without changing spectrum; or
6. that costs compose monotonically under transfer matching.

In particular, inserting or removing a reference cell is not a spectral
equivalence. The cell carries a non-scalar bulk monodromy. Only the additive
bookkeeping cost of its complete graph traversal is zero.

## 4. Dependencies

- Read-only counts: 105 base states and 164 base edges; 420 lifted states and
  656 lifted edges.
- Read-only cycle result: no negative `F4` or `F5` cycle and only the
  reference zero-cycle orbit.
- Reference-relative calibration; the falsified raw Task 53 sign convention
  is not used.
- No producer/checker currently binds these data.

## 5. Exact limitation

The word "rigidity" in this report refers only to zero-cycle rigidity in a
fixed finite automaton. It must not be cited as a spectral rigidity theorem,
a universal interface theorem, or an unrestricted common-liminf theorem.
The classification has not been extended beyond the grammar's memory or to
limits with positive symbolic complexity.

## 6. Next lemma

After certifying the finite graph, prove a composition lemma for primitive
excursions. The required statement should either:

```text
Cost(E1 compose E2) >=Cost(E1)+Cost(E2)-C_boundary,
```

with a boundary term controlled uniformly by the phase state, or construct a
local Rayleigh witness from every positive-cost excursion. A coercive version
that remains effective under sparse concatenation would directly address the
vanishing blocker in the common-liminf problem.

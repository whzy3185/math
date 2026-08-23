# Common Nonzero-Residue Limit: Current Scope

Status: common limsup upper bound `PROVED`; full limits `OPEN`.

## 1. Statement

For each nonzero even residue `r in {2,4,6}`, the explicit separated-G6
constructions give

```text
limsup_(k->infinity) m_(8k+r)^2 <=c6.                 (1)
```

If the unrestricted lower bound

```text
liminf_(k->infinity) m_(8k+r)^2 >=c6                 (2)
```

were proved for the same three residues, then (1)--(2) would imply

```text
lim_(k->infinity) m_(8k+2)^2
=lim_(k->infinity) m_(8k+4)^2
=lim_(k->infinity) m_(8k+6)^2
=c6.                                                  (3)
```

At present (2) is open, so none of the three equalities in (3) is a theorem.
The phrase "common limit" is therefore a target, not an established result.

## 2. Evidence

The upper bound (1) is rigorous. It comes from legal residue constructions
with one, two, or three increasingly separated G6 interfaces and the global
finite-range localization estimate. The restricted lower theorem is also
rigorous for any sequence that visibly retains a G6 interface with pure-bulk
radius tending to infinity. For those explicit dilute families, the upper
and local lower estimates identify `c6` as their limiting squared spectral
top.

This agreement is strong structural evidence for (3), but the minimization in
`m_n` ranges over all legal signings. A good explicit family cannot supply a
lower bound for an unrelated minimizing sequence.

The exact periodic frontier through `p<=24`, the read-only period-25/26
frontier, finite multi-gap support searches, and high-precision interaction
tables all point in the same direction. Each controls only a bounded or
restricted class and therefore remains secondary evidence for the full
limit.

## 3. Exact limitation

The missing implication is not an estimate on the known G6 construction. It
is a compactness/classification theorem for every possible near-minimizer.
Current arguments do not exclude:

- an unclassified tight core with edge below `c6`;
- a dichotomy of interacting charged components;
- a vanishing sequence whose pointed limits are all reference bulk; or
- an aperiodic limit outside every finite periodic frontier.

The period-eight residue-zero family has edge
`eta=4+sqrt(10+2sqrt(5))<c6`; it is a different residue sector and must not be
used as evidence for or against the common nonzero-residue limit (3).

The accepted exact-`2r` theorem sharpens convergence for the explicit fixed-`r`
constructions, but it still does not prove (2). Likewise,
reference-cell insertion/removal is not a spectral equivalence and cannot be
used to reduce arbitrary near-minimizers to a finite list.

## 4. Dependencies

- Proven residue constructions and their `limsup<=c6` bounds.
- The single-G6 global edge for the restricted matching lower bound.
- The pointed limit-operator inequality for every candidate lower-bound
  argument.
- The unrestricted liminf theorem is a missing dependency, not an inherited
  result.

## 5. Next lemma

Prove a near-minimizer compactness alternative with spectral content: every
sequence satisfying

```text
limsup rho(A_j)^2 <=c6
```

must, after rooting and subsequence extraction, either contain a dilute G6
limit or produce a certified finite/aperiodic interface whose spectral top is
at least `c6`. Such a theorem must explicitly close tightness, dichotomy,
vanishing, and aperiodicity. Once that lemma yields (2), equation (3) follows
immediately from the already proved upper bounds.

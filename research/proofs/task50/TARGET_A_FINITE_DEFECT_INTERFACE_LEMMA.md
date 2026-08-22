# Localized Finite-Defect Matching Lemma

## Statement

Let a real fourth-order recurrence agree outside a finite set with periodic
left and right recurrences.  Suppose that at `y=c` both period monodromies are
hyperbolic with two-dimensional stable and unstable subspaces.  Propagate a
basis of the left unstable subspace through the defect and compare it with a
basis of the right stable subspace.  If the resulting matching determinant has
a simple zero at `c`, then the infinite recurrence has a one-dimensional
space of solutions that decay exponentially at both ends.

If all stable multipliers have modulus at most `q<1`, then for some finite
constant `C`, measured in whole bulk cells,

\[
\|X_j\|\le Cq^{|j|}.
\]

The stable and unstable planes vary continuously on every compact
hyperbolicity interval on which their multiplier groups remain separated.

## Proof

Hyperbolicity gives direct sums

\[
\mathbb C^4=E_-^s\oplus E_-^u
=E_+^s\oplus E_+^u.
\]

A solution decaying at the left end must have its state in `E_-^u` at a left
cut, because backward iteration contracts precisely that subspace.  A solution
decaying at the right end must lie in `E_+^s` at a right cut.  Propagation
through the finite defect is invertible.  The matching determinant vanishes
exactly when the propagated left plane intersects the right plane.  If its
zero is simple, the intersection has dimension one after restricting to the
one-parameter spectral curve; otherwise the determinant would vanish to
higher order or the two planes would have a persistent higher-dimensional
intersection.

Writing the matched states in the stable eigenbases gives geometric decay by
the maximum stable multiplier modulus.  Changes of basis alter the determinant
by a nonzero factor and do not alter its zero set or the matched solution.
Continuity of the spectral projectors follows from separation of the two
multiplier groups, for example by the Riesz projector on a fixed separating
contour.

## Scope

This lemma proves the infinite localized state.  It does not, by itself,
identify the spectral radius of every finite twisted closure.  That additional
global exclusion is the open part of Task 50 Gate 4.

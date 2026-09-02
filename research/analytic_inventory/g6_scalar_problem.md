# G6 scalarization problem

## Evidence boundary

The existing local files establish a candidate degree-ten polynomial and an
interval-Evans certificate for a positive G6 eigenvalue.  They also show why
the polynomial alone is insufficient: it contains roots belonging to another
defect and algebraic elimination branches.  This note does not promote the
present certificate to an analytic proof.

## Fixed spectral problem

Let \(A_6\) be the bilateral period-eight signed operator with one G6 phase
slip, and put \(H_6=A_6^2\).  The bulk dispersion is governed by the
palindromic relation

\[
w^2+a(y)w+b(y)-2=0,
\qquad w=z+z^{-1},
\]

where

\[
a(y)=-2y^2+16y-13,
\qquad
b(y)=y^4-16y^3+80y^2-128y+40.
\]

The target is a human-checkable theorem of the form:

> There is exactly one physical G6 eigenvalue \(y\) in the relevant gap
> above the period-eight bulk edge, and no physical G6 eigenvalue lies above
> it.

The present degree-ten resultant may be used as an algebraic consequence,
but not as the definition of a physical branch.

## Desired Weyl formulation

Choose a block cut on the two sides of the defect for which the bulk
recurrence is block Jacobi.  For every energy \(y\) outside the bulk
spectrum, construct the decaying half-line solutions and their boundary
Dirichlet-to-Neumann matrices

\[
M_-(y),\qquad M_+(y).
\]

The interface condition should become one basis-free equation

\[
F_6(y)=\det\bigl(M_-(y)-M_+(y)+V_6(y)\bigr)=0,
\]

where \(V_6(y)\) is the finite defect coupling.  The exact sign convention
and block size remain to be fixed from the recurrence; this displayed form is
the research target, not an asserted identity.

## Required analytic lemmas

1. **Bulk gap lemma.**  Identify an interval \(I\) above the reference bulk
   edge on which the stable and unstable subspaces are separated and are
   graphs over the selected boundary coordinates.

2. **Weyl symmetry lemma.**  Prove the chosen \(M_\pm(y)\) are real symmetric
   on \(I\), and derive their derivative identity from the half-line
   resolvent or a discrete Green formula.

3. **Monotonic matching lemma.**  Establish a sign-definite derivative for
   the relevant eigenvalue of \(M_-(y)-M_+(y)+V_6(y)\), or an equivalent
   crossing form.  This replaces cofactor-chart derivative intervals.

4. **Endpoint lemma.**  Give exact, small algebraic endpoint signs.  One
   Sturm isolation of the resulting scalar equation is acceptable; decimal
   root selection is not.

5. **Global-edge lemma.**  Show every point above the selected zero is in the
   same Weyl domain or is excluded by a separate elementary bulk bound.  This
   replaces the current resultant candidate list and chart atlas.

## Rejection criteria

The Weyl route must be abandoned rather than patched if any of these occurs:

- the stable subspace fails to be a global graph over the chosen boundary
  coordinates on the required interval;
- the matching determinant has unavoidable poles or changes chart in the
  interval;
- its crossing form has no fixed sign;
- a second physical crossing appears in the same gap.

In that event the best honest result remains an exact computer-assisted G6
lemma, and the article route must not depend on calling it analytic.

## Relation to the article

The G6 scalar theorem is not needed to write the period-eight infinite
counterexample-family paper.  It becomes essential only for an analytic
all-residue tail and hence for Route A, the stronger all-even classification.

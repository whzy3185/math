# Width-seven arbitrary-exterior half-line reduction

This note strengthens `N7S_WIDTH7_HALF_LINE_RIGIDITY.md`.  The earlier lemma assumed three complement transitions before the defect.  Here the transition immediately before the defect is completely arbitrary.

Write the transition masks of an open width-seven strip in `Z/128Z`, with mask `127` denoting a complement transition.  The simultaneous dihedral action `D_7` on the seven row labels acts on every mask and preserves the spectrum.

## Theorem 1

Assume

\[
\rho(M)^2<8
\]

for an open width-seven strip whose transition word begins

\[
\boxed{(x,d,127^{14})},
\qquad x\in\{0,\ldots,127\},\quad d\ne127.
\tag{1}
\]

Then, up to the simultaneous `D_7` action, the ordered pair `(x,d)` is one of exactly the following 25 canonical pairs:

\[
\boxed{
\begin{aligned}
&(23,125),\\
&(31,117),(31,119),\\
&(43,87),(43,94),(43,95),(43,125),\\
&(47,87),(47,95),(47,117),(47,119),(47,123),\\
&(55,94),(55,95),(55,122),(55,123),(55,125),\\
&(63,87),(63,94),(63,95),(63,107),(63,111),(63,119),\\
&(127,47),(127,63).
\end{aligned}}
\tag{2}
\]

In particular, the arbitrary exterior transition does not create an uncontrolled half-line state space: after fourteen complement transitions only 25 `D_7`-orbits remain.

### Exact proof

There are

\[
128\cdot127=16256
\]

labelled pairs `(x,d)`.  Quotienting by the simultaneous dihedral action on seven edge positions leaves exactly

\[
\boxed{1282}
\tag{3}
\]

orbits.

For each orbit representative construct the corresponding open strip with transition word (1), form

\[
Q=M^2-8I,
\]

and attempt to find an integer vector `w` such that

\[
w^TQw\ge0,
\qquad w\ne0.
\tag{4}
\]

A candidate is rejected only after (4) is evaluated in exact integer arithmetic.  A floating eigensolver is used only to propose directions from which integer vectors are rounded.  Therefore floating error can retain an unnecessary orbit but cannot falsely remove one.

Exactly

\[
\boxed{1257}
\]

orbits are rejected by exact witnesses, leaving precisely 25 survivors.  Their canonical representatives are exactly the pairs displayed in (2).  Hence every sub-threshold word of the form (1) belongs to one of those 25 orbits. `square`

The complete reconstruction is `verify_n7s_width7_arbitrary_exterior_half_line.py`.

---

## Relation to the three-complement half-line lemma

If the arbitrary transition in (1) is itself followed by the special three-complement normalization used in `N7S_WIDTH7_HALF_LINE_RIGIDITY.md`, the 25-state list collapses further to the two critical defect classes `47` and `63`.  Thus the present theorem is the correct one-sided state-space reduction for long-gap arguments in which the exterior side cannot be assumed to be complement.

The next target is to apply this 25-state boundary set from both ends of a long complement gap and derive a uniform transfer obstruction, paralleling the width-five long-even-gap theorem.
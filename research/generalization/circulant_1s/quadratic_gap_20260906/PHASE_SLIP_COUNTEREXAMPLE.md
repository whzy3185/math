# Exact counterexample to the phase-zero conjecture

Date: 2026-09-06.

This note addresses Q7 from
`../extension_20260905/QUANTITATIVE_QUESTIONS.md`.

Q7 proposed that, for every even jump `s`, the global squared Bloch radius
of the explicit antipodal word is attained at phase zero:

\[
 R_s=\rho(H_s(1))^2.
\]

That statement is false.

## Exact certificate at `s=10`

Take `s=10`, hence `r=5`.  Recall the exact squared characteristic
polynomial `q_r(y,h)` from
`../extension_20260905/EVEN_JUMP_THEOREM_AND_PROOF.md`, with

\[
 h=\xi+\xi^{-1}\in[-2,2].
\]

At phase zero, `xi=1` and therefore `h=2`.

Choose the rational interior phase parameter

\[
 h_* = \frac{19997}{10000}=1.9997.
\]

Because `h_*` lies in `(-2,2)`, there exists a unit complex number `xi_*`
with `xi_*+xi_*^{-1}=h_*`.

Set the rational separator

\[
 y_* = \frac{317}{40}=7.925.
\]

Exact Sturm root counting over `QQ` gives

\[
 \#\{y>y_*:q_5(y,2)=0\}=0,
\]

but

\[
 \#\{y>y_*:q_5(y,h_*)=0\}=1.
\]

The roots of `q_5` are exactly the squared eigenvalues of the reduced
Bloch problem.  Therefore

\[
 \rho(H_{10}(1))^2 < \frac{317}{40}
 < \rho(H_{10}(\xi_*^2))^2.
\]

Hence

\[
 \boxed{R_{10}>\rho(H_{10}(1))^2,}
\]

which disproves Q7.

The accompanying script `verify_quadratic_gap_upgrade.py` reconstructs the
continuant polynomial with exact rational arithmetic and asks SymPy's Sturm
root counter to verify the two displayed counts.  No floating-point
comparison is used in the certificate.

## Numerical size of the slip

Floating-point minimization of the threshold matrix is useful only for
scale intuition.  It suggests, for `s=10`,

\[
 g_{10}(0)\approx0.0750899751,
\]

whereas the true Bloch minimum is about

\[
 g_{10}\approx0.0749467654.
\]

The maximizing square-root phase is small, about `1.8e-2` radians.
For larger even `s`, exploratory computations indicate that the phase
itself shrinks roughly like `s^{-2}` and the improvement over the endpoint
is of still higher order than the leading `s^{-2}` gap.

These last scaling statements are numerical observations, not theorems in
this note.

## Implication for the sharp asymptotic problem

The failure of Q7 does not contradict the conjecture

\[
 s^2(8-R_s)\to\pi^2.
\]

It only shows that proving that conjecture by analyzing the endpoint
`h=2` alone is insufficient at finite `s`.  A correct sharp proof must
control a boundary layer in the Bloch parameter and show that its phase
slip changes only lower-order terms.

A natural next target is therefore:

1. obtain an asymptotic expansion of the largest root of `q_r(y,h)` with
   `8-y=Theta(r^{-2})` and `4-h^2=O(r^{-4})`;
2. derive the limiting Robin condition for the soft Chebyshev channel;
3. prove that the optimizing phase satisfies `4-h^2=O(r^{-4})`;
4. extract the leading constant `pi^2` and, if possible, the first phase
   correction.

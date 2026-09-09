# Exact rigidity at `N=14`

Let `beta` be the largest real root of `x^3-7x+7`.

## Theorem

For `s in {3,4,5}`,

\[
 m(14,s)^2=4+\beta.
\]

Moreover, for each of the three steps there are exactly two labelled switching classes of minimizers. In Hamilton gauge they are the two choices of the global alternating chord sign `epsilon=+-1`; one-step rotation exchanges them.

The required Hamilton holonomy is

\[
\alpha=-1\quad(s=3,4),\qquad \alpha=+1\quad(s=5).
\]

For `s=2`, no signing has squared spectral radius below `6`.

## Proof

Put `B=A^2-4I` and `M=lambda_max(B)`. If a signing has squared radius below `6`, then `M<2`, and the parity-defect reduction forces `B` to be a signing of two copies of `C_7(1,t)cong overline(C_7)`. The order-seven lemma in `SUB_SQRT6_CLASSIFICATION.md` shows that a component can have largest eigenvalue below `2` only in one switching class, whose characteristic polynomial is

\[
x(x^3-7x+7)^2.
\]

Hence any sub-`6` signing must have `M>=beta`, with equality only when both parity components are in that class.

For each `s=2,3,4,5`, at least one of the mixed two-walk displacements `s-1,s+1` is outside the forced parity support. Since an off-support entry of `B` is even and `M<2`, that entire channel must vanish. In signed-shift Hamilton gauge this gives

\[
DT=-TD.
\]

Thus

\[
D=epsilon\,diag(1,-1,1,-1,\ldots),\qquad epsilon in {+-1},
\]

and

\[
B=T^2+T^{-2}+(-1)^s(T^{2s}+T^{-2s}),\qquad T^{14}=alpha I.
\]

So every possible sub-`6` signing is already reduced to the four finite cases `(s,alpha)` for each `s` and the irrelevant global choice `epsilon`.

Finite Fourier diagonalization of the signed shift gives, for `z^14=alpha`,

\[
mu(z)=z^2+z^{-2}+(-1)^s(z^{2s}+z^{-2s}).
\]

The exact characteristic polynomials are:

\[
\begin{array}{c|c|c}
s&alpha&chi_B(x)\\ \hline
2&-1&x^2(x^3-7x-7)^4\\
2&+1&(x-4)^2(x^3+2x^2-x-1)^4\\
3&-1&x^2(x^3-7x+7)^4\\
3&+1&x^2(x^3-7x-7)^4\\
4&-1&x^2(x^3-7x+7)^4\\
4&+1&(x-4)^2(x^3+2x^2-x-1)^4\\
5&-1&x^2(x^3-7x-7)^4\\
5&+1&x^2(x^3-7x+7)^4.
\end{array}
\]

The polynomial `x^3-7x+7` has largest root `beta<2`; the other displayed cases have largest root at least `2` (indeed `3.048917...` or `4`). Therefore the only sub-`6` holonomies are exactly

\[
(s,alpha)=(3,-1),(4,-1),(5,+1).
\]

For each allowed pair, anticommutation leaves precisely `epsilon=+-1`, so there are exactly two Hamilton-gauge representatives and hence exactly two labelled switching classes. A one-step rotation reverses the alternating diagonal and exchanges the two. This proves both exactness and rigidity.

## Independent finite audit

A full Hamilton-gauge enumeration over `2^(14+1)` representatives was also run as a hostile audit. It finds exactly two minimizers for each of `s=3,4,5`, and none below `6` for `s=2`. This enumeration is not needed for the analytic proof; it only checks the switching-class count independently.
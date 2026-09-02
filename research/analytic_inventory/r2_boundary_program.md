# Residue-two boundary-closure programme

## Target theorem

For the standard one-G6 signing at \(n=8k+2\), \(k\ge6\), prove

\[
198I-25A_{8k+2}^2\succ0.
\]

Together with the elementary benchmark comparison, this is an analytic
counterexample-family theorem for the residue-two class.  The theorem is not
currently claimed here.

## What is already reduced

After a fixed block ordering, the interior consists of alternating four by
four pivots

\[
F_\pm(X)=D-E_\pm^{\mathsf T}X^{-1}E_\pm,
\]

with

\[
D=\begin{pmatrix}
98/25&0&-1&0\\
0&98/25&0&-1\\
-1&0&98/25&0\\
0&-1&0&98/25
\end{pmatrix},
\]

\[
E_+=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\-1&2&1&0\\2&-1&0&-1\end{pmatrix},
\qquad
E_-=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\-1&-2&1&0\\-2&-1&0&-1\end{pmatrix}.
\]

The local rational box proof establishes that, after a fixed entrance
segment, all bulk pivots lie in alternating positive Loewner boxes
\(B_0,B_1\).  This is a useful finite matrix inequality, not a numerical
observation.

The full cyclic problem retains only the fixed response state

\[
(G_j,X_j,H_j,R_j,W_j,C_j),
\]

where \(G_j\) is two by two, \(X_j,H_j,W_j\) are four by four, and
\(R_j,C_j\) are two by four.  The final obstruction is the six by six
matrix

\[
S_k=\begin{pmatrix}G_k&C_k\\C_k^{\mathsf T}&H_k\end{pmatrix}.
\]

## Required proof, not heuristic

The existing stable-multiplier estimate does **not** itself show
\(S_k\succ0\).  A valid proof must supply all of the following.

1. **Response contraction.**  On the two invariant boxes, derive an explicit
   operator-norm or Loewner estimate for the maps carrying \(R_j,W_j,C_j\)
   through one full bulk cell.  The estimate must be uniform on the boxes and
   strictly contractive.

2. **Limit response.**  Construct the period-two limiting response state
   \(S_\infty^{(0)},S_\infty^{(1)}\) as a fixed point of the complete
   response recurrence, not merely as a floating-point limit.

3. **Positive limiting core.**  Exhibit a rational lower bound
   \(S_\infty^{(i)}\succeq\delta I\) with \(\delta>0\), or an equivalent
   exact Schur/LDL certificate.

4. **Finite-length error.**  Prove
   \(\|S_k-S_\infty^{(k\bmod2)}\|<\delta\) after an explicit index \(k_0\).
   Only then can a finite verification of \(6\le k<k_0\) close the theorem.

## Candidate route

The preferred route is a block-Woodbury calculation.  The bulk box confines
the inverse pivots; the left/right propagated responses should be products
of the same alternating transfer factors.  The final wrap-around interaction
is then a finite-rank perturbation of two decoupled half-chain responses.

The proof must bound the actual response products.  It may not infer a norm
bound solely from the reciprocal multiplier roots, because a transfer
eigenvalue bound need not control the chosen finite coordinate chart.

## First rejected shortcut

The direct Euclidean operator-norm estimate on the existing Loewner boxes is
not contractive.  The elementary bound

\[
\|DF_E(X)\|\leq\|X^{-1}E\|_2^2
\]

gives approximately \(1.01990\) for each alternating step, and approximately
\(1.04020\) for their product when evaluated at the rational lower-box
corners.  These figures are diagnostics, not proof data, but they rule out
using this unweighted estimate as a contraction argument.

The next legitimate options are a weighted Lyapunov/cone metric for the
linearized two-cycle, or a direct Woodbury estimate on the boundary response.

## Stop rule

Abandon this route if the response map fails to be contractive on every
reasonable rational box, or if its limiting six by six core is not positive.
In that case residue two stays as a finite exact module; it must not be
advertised as an analytic family.

## Article consequence

Closing this theorem would combine with the period-eight theorem to give two
analytic residue classes.  It is more valuable to the intended mathematical
story than reducing another collection of finite LDL certificates.

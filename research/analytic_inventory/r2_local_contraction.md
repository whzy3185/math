# Residue-two local contraction lemma

## Local contraction lemma (draft)

Let \(\Phi=F_-\circ F_+\) be the two-step residue-two Riccati map on the
ten-dimensional space of symmetric four-by-four matrices.  Let
\(X_{12}=\Phi^{12}(D)\), and use the rational Gram matrix \(W\) in
`r2_lyapunov_certificate.md`.  In the coordinate norm induced by \(W\), the
closed ball

\[
\mathcal B=\{X:\|X-X_{12}\|_W\le10^{-10}\}
\]

is intended to be mapped into itself with \(\Phi\) a strict contraction.
If the neighbourhood estimate below survives independent line audit, Banach's
theorem gives a unique fixed point \(X_*\) and geometric convergence of the
even bulk Riccati iterates.

## Exact finite premises

The companion verifier checks, using Fraction arithmetic and LDL positivity,

\[
X_{12}\succeq\tfrac12I,\qquad F_+(X_{12})\succeq\tfrac12I,\qquad
\tfrac9{10}I\preceq W\preceq2I,
\]

\[
D\Phi(X_{12})^{\mathsf T}W D\Phi(X_{12})\prec\frac6{25}W,
\qquad
\|\Phi(X_{12})-X_{12}\|_F<\frac1{40}\,10^{-10}.
\]

Run:

```text
python research/scripts/verify_target_a_r2_local_lyapunov.py
```

## Neighbourhood estimate

Write a symmetric perturbation as upper-triangular coordinates.  Its matrix
Frobenius norm is at most \(\sqrt2\) times the coordinate Euclidean norm.
For \(X\in\mathcal B\), the preceding lower bounds and
\(\sqrt2<3/2\) give

\[
\|X^{-1}\|_2,\ \|F_+(X)^{-1}\|_2\le3.
\]

Both coupling matrices have Frobenius norm below \(4\).  From

\[
DF_E(X)[H]=E^{\mathsf T}X^{-1}HX^{-1}E
\]

and differentiation once more, the deliberately coarse coordinate bounds
are

\[
\|DF_E(X)\|\le216,
\qquad
\|D^2F_E(X)\|\le2000.
\]

The chain rule for \(\Phi=F_-\circ F_+\) then yields

\[
\|D\Phi(X)-D\Phi(X_{12})\|_W
<\frac1{60}
\qquad(X\in\mathcal B).
\]

Here the conversion between the coordinate Euclidean norm and the \(W\)-norm
uses \(9I/10\preceq W\preceq2I\): one may use the conservative factors
\(10/9\) and \(3/2\).  Combining this with the exact centre
inequality gives

\[
\|D\Phi(X)\|_W<\frac12+\frac1{60}=\frac{31}{60}.
\]

Finally the centre residual has \(W\)-norm below \(3\cdot10^{-10}/80\).
Thus

\[
\|\Phi(X)-X_{12}\|_W
\le \frac3{80}10^{-10}+\frac{31}{60}10^{-10}<10^{-10},
\]

so \(\Phi(\mathcal B)\subset\mathcal B\).  Banach's theorem proves the
claim.

## Conditional consequence for the actual bulk orbit

No separate entrance theorem is needed for the standard bulk initial state:
by definition \(X_{12}=\Phi^{12}(D)\).  The first twelve two-step iterates
are finite rational matrices, and the companion exact data checks show that
the centre and intervening one-step pivot have a uniform lower bound.  From
the twelfth two-step iterate onwards the contraction argument applies.

Together with the already direct finite entrance calculation, the audited
lemma would give an all-length analytic proof that every repeated residue-two
bulk pivot is positive.  The statement concerns the open bulk chain only. It
does not settle the cyclic wrap-around boundary core.

## Boundary

Even after audit, this lemma proves only the bulk two-cycle.  It does not yet bound the
propagated cyclic response variables or establish positivity of the final
six-by-six boundary core.  It is therefore a rigorously isolated analytic
target, not the complete residue-two family theorem.

## Status

`LOCAL_CONTRACTION_DRAFT_PENDING_LINE_AUDIT`.  The centre Lyapunov and
residual premises are exactly verified; the neighbourhood derivative bound is
the remaining proof text to audit.

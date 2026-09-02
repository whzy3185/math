# Residue-two local Lyapunov route

## Diagnostic result

Let \(\Phi=F_-\circ F_+\) be the two-step four-by-four Riccati map at the
fixed cap \(198/25\).  Iterating from the exact entrance state and then
linearizing on the ten-dimensional symmetric-matrix space gives the following
floating-point diagnostics:

\[
\rho(D\Phi(X_*))\approx0.10683390,
\qquad
\|D\Phi(X_*)\|_2\approx0.54200374,
\]

where \(X_*\) is the observed fixed point and
\(\lambda_{\min}(X_*)\approx0.57904561\).  These values are not proof
data.  They show that the rejected coarse-box estimate is an artifact of the
box, not evidence against a local contraction theorem.

## Analytic theorem target

Construct rational symmetric matrices \(X_*^-\preceq X_*\preceq X_*^+\)
and a rational \(0<q<1\) such that:

1. \(\Phi\) maps the small box
   \(\mathcal B_*=[X_*^-,X_*^+]\) strictly into itself;
2. in a chosen weighted norm on symmetric matrices,
   \(\|D\Phi(X)[H]\|_W\le q\|H\|_W\) for every
   \(X\in\mathcal B_*\);
3. the original exact large boxes enter \(\mathcal B_*\) after a stated
   finite number of two-cycles.

The Banach fixed-point theorem then gives a unique rationally enclosed
period-two bulk response and an explicit geometric error bound.

## Why a weighted norm is legitimate

The derivative acts on the ten-dimensional real vector space of symmetric
four-by-four matrices.  A positive definite rational Gram matrix \(W\) gives
the norm \(\|H\|_W^2=\operatorname{vec}(H)^\mathsf TW\operatorname{vec}(H)\).
It is enough to verify the finite matrix inequality

\[
(D\Phi(X))^\mathsf TW D\Phi(X)\preceq q^2W
\]

throughout the small rational box.  This is a finite rational LMI/interval
certificate, not an order-by-order spectral computation.

## Remaining bridge to the cyclic boundary

Local bulk contraction alone is insufficient.  The same weighted estimate
must control the propagated response variables \(R_j,W_j,C_j\), or a
separate finite-rank Woodbury calculation must do so.  The resulting limiting
six-by-six core then needs an exact positive margin large enough to absorb the
geometric tail.

## Immediate work sequence

1. obtain high-precision fixed-point coordinates only as a guide;
2. rationalize a small enclosing box;
3. search for a rational Lyapunov Gram matrix at the fixed derivative;
4. turn the local inequality into an interval proof on the box;
5. propagate the response recurrence and certify the final core.

Failure of step 3 or 4 is decisive evidence to return to the direct Woodbury
route rather than widening the old Loewner boxes.

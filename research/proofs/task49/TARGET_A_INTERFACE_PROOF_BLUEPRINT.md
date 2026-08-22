# Target A Interface Proof Blueprint

## 1. Exact Bulk Transfer

After switching all step-one edges to `+1`, write the triangle fluxes as
`tau_i in {+1,-1}`.  The eigenvalue recurrence for the state

\[
 X_i=(v_{i+1},v_i,v_{i-1},v_{i-2})^T
\]

is `X_{i+1}=T_i(lambda)X_i`, where

\[
T_i(\lambda)=
\begin{pmatrix}
-\tau_i&\tau_i\lambda&-\tau_i&-\tau_i\tau_{i-2}\\
1&0&0&0\\
0&1&0&0\\
0&0&1&0
\end{pmatrix}.
\]

For the target bulk word, one convenient triangle-flux cell is
`(1,1,-1,1,-1,-1,1,-1)`.  Put

\[
M_8(\lambda)=T_7(\lambda)\cdots T_0(\lambda),\qquad y=\lambda^2.
\]

Direct exact multiplication gives the reciprocal characteristic polynomial

\[
\begin{aligned}
\chi(z;y)={}&z^4+(-2y^2+16y-13)z^3\\
&+(y^4-16y^3+80y^2-128y+40)z^2\\
&+(-2y^2+16y-13)z+1.
\end{aligned}
\]

Thus multipliers occur in reciprocal pairs.  The proof interval of interest is
`eta < y < 8`, containing `c6` and `c10`.  The first exact subtask is to isolate
two roots inside and two outside the unit circle uniformly on compact
subintervals containing the two interface levels.

## 2. Local Defect Matching

For a finite defect word `P`, multiply the finitely many altered one-step
matrices to obtain an exact `4x4` defect transfer `P(lambda)`.  Let
`U_-(lambda)` span the left bulk unstable subspace propagated toward the
defect and let `S_+(lambda)` span the right stable subspace.  The infinite-line
matching function is

\[
D_P(\lambda)=\det\bigl(P(\lambda)U_-(\lambda),S_+(\lambda)\bigr).
\]

Its zeros are the candidate localized states.  For a finite ring in the tree
gauge, the holonomy enters only through the twisted closure

\[
E_{n,\alpha}(\lambda)=\det(M_n(\lambda)-\alpha I_4),
\qquad \alpha\in\{-1,+1\}.
\]

Task 49 evaluates this determinant directly at 80, 120, and 160 digits.  The
one-step matrices, finite products, reciprocal polynomial, numerical root
intervals, and raw precision ladders are available.  The stable-subspace basis
and zero isolation are still numerical dependencies.

## 3. Ranked Exact-Root Routes

1. **Interval Evans certification.** Isolate the stable projector using
   interval arithmetic on a rational `y` interval, enclose `D_P`, and prove a
   unique simple zero by an interval Newton or argument-principle calculation.
   Complexity is moderate, rigor is complete, and it uses the strongest
   existing numerical conditioning.  This is the recommended first route.
2. **Algebraic stable subspace.** Reduce the palindromic quartic with
   `w=z+z^{-1}`, construct exact spectral projectors in the resulting algebraic
   extension, and eliminate the matching coefficients.  Complexity is
   moderate to high; it offers the cleanest exact structural theorem if the
   expressions remain manageable.
3. **Resultant elimination.** Combine `chi(z;y)` with the defect matching
   equations and eliminate the multipliers and matching amplitudes.  Rigor is
   direct, but expression swell and extraneous factors are high risk.  Use
   only after the algebraic-projector reduction.
4. **Cone or transfer contraction.** Prove a graph-transform contraction for
   stable two-planes over a rational `y` interval.  Complexity is high but it
   naturally supplies uniform finite-size bounds and avoids a large minimal
   polynomial.
5. **Finite-matrix comparison.** Use exact finite matrices plus explicit tail
   bracketing.  This is robust as a cross-check but inefficient as the primary
   infinite-interface proof and should not replace dimension reduction.

The G6 PSLQ degree-ten relation remains a candidate only.  It must not select
the proof route unless independently derived by elimination.

## 4. Uniform Finite-Ring Targets

The Task 49 data select

\[
|R_n-c_e|\le C_e q_e^{k},\qquad e\in\{6,10\},
\]

where `k` is the explicitly recorded closure distance in period-eight cells
and `q_e` may initially be any rational number strictly above the slow stable
multiplier modulus.  A resolvent/graph-transform proof can absorb the faster
stable mode into the same bound.

For two G6 defects separated by arcs of `L` and `M-L` bulk cells, target

\[
|R_{L,M}-c_6|\le
C\left(q_6^L+q_6^{M-L}\right).
\]

The leading two-defect expansion should retain the signs induced by the two
matching paths and by `alpha`; dropping them would lose the observed mod16
selection.  The theorem only needs the absolute two-tail estimate, while a
sharper asymptotic expansion can explain branch preference.

## 5. Eventual Threshold Comparison

The exact threshold is

\[
T_n=4\left(\cos^2\frac{\pi}{n}+\cos^2\frac{2\pi}{n}\right).
\]

Since `sin x <= x` for `x>=0` and `pi^2<10`,

\[
T_n\ge 8-\frac{20\pi^2}{n^2}>8-\frac{200}{n^2}.
\]

For each family choose a rational `delta_e>0` with
`c_e <= 8-delta_e`, a rational `q_e<1`, and a proved constant `C_e`.  It is
then enough to solve explicitly

\[
C_e q_e^{k(n)}+\frac{200}{n^2}<\delta_e.
\]

For two defects replace the first term by
`C(q_6^L+q_6^{M-L})`.  Taking the maximum of the four residue-class onset
bounds produces an explicit even-order `N`.

## 6. Proof Completion Checklist

1. Certify a simple G6 Evans zero in a rational interval below 8.
2. Certify the G10 zero analogously; do not rely on PSLQ.
3. Prove stable/unstable splitting and projector bounds on both intervals.
4. Derive single-defect finite-ring errors with explicit rational constants.
5. Derive the two-defect two-tail bound with twisted holonomy.
6. Instantiate all four nonzero even residue classes and combine with the
   proved period-eight family.
7. Run an independent exact/interval checker and expose its certificates.

The exact interface zero and the uniform estimates are the remaining
mathematical blockers.  All other Task 49 mechanism requirements are ready as
inputs to these proofs.

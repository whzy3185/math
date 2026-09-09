# RESEARCH_STATE — AML boundedness-to-stabilization project

Date: 2026-09-09
Target journal: Applied Mathematics Letters
Branch: `research/aml-production-consumption-stabilization`

## Seed

Qin–Zheng, *Applied Mathematics Letters* 180 (2026), 109995, studies
\[
\begin{cases}
 u_t=\Delta(\varphi(v)u),\\
 v_t=\Delta v+u-\alpha uv,
\end{cases}
\]
with Neumann/no-flux boundary conditions and proves global classical boundedness under an explicit motility condition for positive decreasing \(\varphi\).

## Current strongest theorem

Consider the more general system
\[
 u_t=\Delta(\varphi(v)u),
 \qquad
 v_t=\Delta v+uF(v)
\]
on a smooth bounded connected domain. Assume:

- \(m=\int_\Omega u_0>0\);
- the global nonnegative classical solution satisfies \(\sup_t\|u(t)\|_\infty<\infty\);
- the signal remains in a compact interval \(I\);
- \(\varphi\in C^1(I)\) and \(\min_I\varphi>0\);
- for some \(v_*\in I\), \(\beta>0\),
  \[
  F(v_*)=0,
  \qquad
  (s-v_*)F(s)\le-\beta(s-v_*)^2
  \quad(s\in I).
  \]

Then there exist \(C,\lambda>0\) such that
\[
\boxed{
\|u(t)-\bar u_0\|_{L^\infty}
+\|v(t)-v_*\|_{W^{1,\infty}}
\le Ce^{-\lambda t}
}
\qquad (t\ge2),
\]
where \(\bar u_0=m/|\Omega|\).

Evidence status: **Proved** in the repository campaign sense. Novelty status remains **Observed**, not certified.

## Proof architecture

1. Mass conservation + a mass-weighted Poincare/coercivity inequality.
2. Dissipative signal kinetics give exponential \(L^2\)-decay of \(v-v_*\).
3. Neumann heat-semigroup smoothing upgrades the signal to \(W^{1,\infty}\)-exponential decay.
4. Energy + Poincare give \(L^2\)-exponential decay of \(u-\bar u_0\).
5. Direct uniform upgrade: write
   \[
   q_t-\nabla\cdot(\varphi(v)\nabla q)=\nabla\cdot\big(u\varphi'(v)\nabla v\big).
   \]
   The forcing flux decays exponentially in \(L^\infty\). Choi 2016, Theorem 1.1, gives a local \(L^2\to L^\infty\) estimate up to the Neumann boundary for exactly this inhomogeneous divergence-form structure. A finite covering closes the global \(L^\infty\)-rate.

Reference for Step 5:
J. Choi, *Note on local estimates for weak solution of boundary value problem for second order parabolic equation*, Bull. Korean Math. Soc. 53 (2016), 1123–1148, DOI 10.4134/BKMS.b150567.

## Qin–Zheng corollary

For
\[
F(s)=1-\alpha s,
\qquad v_*=1/\alpha,
\]
we have
\[
(s-v_*)F(s)=-\alpha(s-v_*)^2.
\]
Therefore every uniformly bounded solution of the exact Qin–Zheng model satisfies
\[
\|u(t)-\bar u_0\|_\infty
+\left\|v(t)-\frac1\alpha\right\|_{W^{1,\infty}}
\le Ce^{-\lambda t}.
\]
The stabilization implication itself does **not** use \(\varphi'<0\).

## Novelty posture

Deep audit dated 2026-09-09 found material predecessors:

- Li–Zhao 2021: direct pure-consumption signal-dependent motility with exponential large-time behavior;
- Tao–Winkler 2025: simultaneous production–consumption with classical chemotactic sensitivity;
- 2026 indirect-signal/global-dynamics papers.

No exact-model exponential-stabilization collision or identical abstract dissipativity theorem was located, but this is not an open-status certificate.

Safe contribution architecture:

1. general boundedness-to-uniform-stabilization principle;
2. mass-weighted coercivity mechanism;
3. no monotonicity requirement on motility in the stabilization stage;
4. timely Qin–Zheng 2026 corollary.

## Current priority

The proof DAG is closed. Next priority is **adversarial novelty/referee audit and manuscript compression to AML's six-page format**, unless a further theorem strengthening is attempted first.

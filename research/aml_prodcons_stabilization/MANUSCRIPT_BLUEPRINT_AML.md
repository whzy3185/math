# MANUSCRIPT_BLUEPRINT_AML

Target: *Applied Mathematics Letters*  
Updated: 2026-09-11

## Preferred title

**Mass-weighted damping and a rate dichotomy for chemotaxis with signal-dependent motility**

Strong alternatives:
1. **Exponential and algebraic stabilization in chemotaxis with signal-dependent motility**
2. **A mass-weighted stabilization principle for dissipative signal kinetics**

The previous title, “A boundedness-to-stabilization principle…”, is now too narrow: the current mathematics includes arbitrary damping order, a quadratic/superquadratic rate dichotomy, eventual finite-`L^p` hypotheses, an explicit algebraic threshold, and sharp homogeneous profiles.

## Core message

For
\[
u_t=\Delta(\varphi(v)u),\qquad v_t=\Delta v+uF(v),
\]
the positive conserved mass of `u` turns the weighted reaction dissipation into an unweighted coercive mechanism. If
\[
F(v_*)=0,\qquad (s-v_*)F(s)\le-\beta|s-v_*|^q,
\]
then `q=2` yields exponential damping, while `q>2` yields algebraic signal decay of order `t^{-1/(q-2)}`. Under eventual finite `L^p` control with `p>max{n,2}`, these rates propagate to uniform cell/signal stabilization. The stabilization stage requires positivity, but not monotonicity, of the motility on the attained signal range.

## Manuscript hierarchy

The paper should be organized around four results, in this order.

### Result 1 — nonlinear mass-weighted coercivity

For `q>=2`, `rho>=0`, `int rho=m>0`, `||rho||_2<=K`,
\[
\|f\|_2^2
\le
A\|\nabla f\|_2^2
+B_q\left(\int_\Omega\rho|f|^q\right)^{2/q},
\]
with
\[
A=C_P^2\left(1+\frac{2|\Omega|K^2}{m^2}\right),
\qquad
B_q=2|\Omega|m^{-2/q}.
\]

Do not claim the inequality itself is new. Its importance is that it converts weighted damping into a closed energy inequality without eventual pointwise positivity of the cell density.

### Result 2 — abstract weighted-damping rate dichotomy

For
\[
z_t=\Delta z+\rho(x,t)F(z),\qquad \partial_\nu z=0,
\]
with fixed positive mass and a uniform `L^2` bound on `rho`, prove:

- `q=2`: exponential `L^2` signal decay;
- `q>2`: algebraic decay
\[
\|z(t)-z_*\|_2
\lesssim (1+t)^{-1/(q-2)}.
\]

Stress that no evolution law for `rho` is used.

### Result 3 — full stabilization from eventual finite `L^p`

Assume for some finite
\[
p>\max\{n,2\},\qquad
\sup_{t\ge T}\|u(t)\|_p\le U_p.
\]
Then:

- for quadratic damping,
\[
\|u(t)-\bar u_0\|_\infty
+\|v(t)-v_*\|_{W^{1,\infty}}
\le Ce^{-\lambda(t-T)};
\]
- for superquadratic damping `q>2`, for every
\[
0<\mu<\frac1{q-2}
\min\left\{1,\frac{2(p-n)}{pn}\right\},
\]
\[
\|u(t)-\bar u_0\|_\infty
+\|v(t)-v_*\|_{W^{1,\infty}}
=O((1+t-T)^{-\mu}).
\]

This finite-`L^p` formulation replaces the old uniform-`L^\infty` hypothesis in the main theorem. The theorem retains the natural scope `n>=1`: use Choi 2016 directly for the final local-boundedness step when `n>=2`, and in `n=1` replace Choi's mixed-norm Sobolev lemma by the one-dimensional Gagliardo--Nirenberg estimate before running the same lower-order-free De Giorgi iteration.

### Result 4 — applications and sharpness

1. **Qin–Zheng 2026:** `F(s)=1-alpha s`, `v_*=1/alpha`, quadratic branch, hence full exponential stabilization of their bounded classical solutions for every `n>=1`.
2. **Superlinear consumption:** `F(s)=-s^m`, `m>1`, so `q=m+1`; obtain signal rate `t^{-1/(m-1)}` and the corresponding uniform rate threshold.
3. **Sharp homogeneous profile:** for
\[
F(s)=-\kappa(s-v_*)|s-v_*|^\theta,
\]
spatially homogeneous solutions satisfy
\[
|v(t)-v_*|
=
\left(|w_0|^{-\theta}+\theta\kappa\bar u_0 t\right)^{-1/\theta}.
\]
Use this to justify sharpness of the signal exponent, not a blanket sharpness claim for every strong norm.

## Recommended AML-length architecture

### Page 1 — motivation, positioning, main statements

Use four compact paragraphs:

1. signal-dependent motility and the 2026 Qin–Zheng production–consumption model;
2. nearest predecessors: Li–Zhao 2021 (direct consumption), Li–Wang–Pan 2021 (logistic consumption), Tao–Winkler 2025 (same production–consumption reaction with classical chemotactic flux);
3. precise contribution: mass-weighted damping mechanism, arbitrary damping order, finite-`L^p` stabilization criterion;
4. applications: Qin–Zheng exponential branch and superlinear-consumption algebraic branch.

State the abstract rate dichotomy and the full stabilization theorem on page 1 or early page 2.

### Pages 2–3 — coercivity and signal decay

- prove the mass-weighted coercivity lemma explicitly;
- derive the signal energy inequality;
- close `q=2` by a spectral gap;
- close `q>2` by the differential inequality for `E^{-(q-2)/2}`;
- record the exact `L^2` algebraic exponent.

### Pages 3–4 — strong signal and cell stabilization

- eventual finite `L^p` gives the `L^2` weight bound;
- write the unit-interval Duhamel formula and use Neumann heat-semigroup smoothing for `W^{1,infinity}` signal decay;
- show the exponent transfer through `1/r=1/p+1/s`;
- recover the signal `L^infinity` norm from its mean and gradient;
- test the cell equation by `u-ubar`;
- write the exact conormal identity for `q=u-ubar`;
- use Choi's Neumann local boundedness theorem for the final `L^infinity` upgrade when `n>=2`;
- retain a compact two-sentence explanation of the `n=1` Gagliardo--Nirenberg/De Giorgi replacement. Do not drop this during compression.

### Page 5 — applications, sharpness, comparison

- Qin–Zheng in one paragraph, including the invariant signal interval and the fact that their uniform boundedness supplies every finite `L^p` hypothesis;
- superlinear consumption in one paragraph, explicitly inheriting the remaining hypotheses of the full theorem;
- homogeneous profile in one displayed formula;
- one short paragraph explaining that direct-consumption stabilization is known and that the contribution is the structural rate-dichotomy framework, not “the first stabilization result”.

### Page 6 — references

Aim for 10–16 references. Avoid a broad historical survey.

## Referee-facing positioning

Safe central sentence:

> The contribution is a mass-weighted damping mechanism which yields a quadratic/superquadratic rate dichotomy and converts an eventual finite-`L^p` bound into strong stabilization for the signal-dependent-motility class; the exact production–consumption model of Qin and Zheng and superlinear consumption laws arise as distinct special cases.

Useful secondary sentence:

> The stabilization implication uses positivity of the motility on the attained signal range, but no sign condition on its derivative; assumptions such as `phi'<0` may still be essential in separate boundedness theorems used to generate the hypothesis.

Do not use without further evidence:

- “first stabilization result for signal-dependent motility”;
- “the problem was open”;
- “new Poincare inequality”;
- “we remove the Qin–Zheng motility assumptions” without restricting the statement to the conditional stabilization stage;
- “sharp full stabilization rate” when only the signal exponent is explicitly attained by the homogeneous example.

## Current literature comparison to preserve

- Qin–Zheng, *Applied Mathematics Letters* 180 (2026), 109995: exact production–consumption signal-dependent-motility model; boundedness theorem and `n>=1` scope.
- Tao–Winkler, *European Journal of Applied Mathematics* 36 (2025), 570–583: same production–consumption reaction with classical Keller–Segel flux; stabilization.
- D. Li–J. Zhao, *ZAMP* 72 (2021), Art. 57: direct consumption with signal-dependent motility; boundedness and exponential large-time behavior.
- X. Li–L. Wang–X. Pan, *ZAMP* 72 (2021), Art. 170: direct consumption plus logistic cell source; boundedness and exponential stabilization.
- G. Li–M. Winkler, *Commun. Math. Sci.* 21 (2023), 299–322: relaxation in a direct-consumption signal-dependent-motility setting.
- Z. Zhang–Y. Li, *JMAA* 541 (2025), 128711: superlinear consumption with singular density-suppressed motility; global-solution theory.
- J. Choi, *Bull. Korean Math. Soc.* 53 (2016), 1123–1148: boundary local boundedness estimate used for the cell `L^infinity` upgrade in `n>=2`; its proof structure is also used for the manuscript's explicit `n=1` adaptation.

Novelty remains **observed/promising, not certified exhaustive**. Run a final forward-citation and same-author search immediately before submission freeze.

## Current writing state

- Full English draft: `MANUSCRIPT_DRAFT_AML.md`.
- Submission LaTeX: `research/paper/aml_mass_weighted_stabilization/main.tex`.
- Main theorem package: mathematically aligned with `STRENGTHENED_RATE_DICHOTOMY.md`.
- Abstract and title: synchronized to the rate-dichotomy version.
- Proof body: theorem-by-theorem hardening pass completed on 2026-09-11; the `n=1` endpoint and exact conormal boundary mapping are now explicit.
- Remaining editorial tasks: fresh novelty audit, bibliography/source normalization, actual Elsevier compile/page-count compression, and author/submission metadata.

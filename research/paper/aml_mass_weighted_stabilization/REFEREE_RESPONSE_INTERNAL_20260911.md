# Internal response to AML-style referee audit (2026-09-11)

This file records how the manuscript was revised after an adversarial referee report. It is an internal ledger, not a submission document.

## 1. State-of-the-art comparison

**Referee concern:** the five-reference bibliography underrepresented exact signal-dependent-motility consumption literature, weakening the originality claim.

**Action:** expanded the introduction and bibliography to include Li--Winkler 2023, Laurencot 2023, Li--Winkler 2024, Li--Wang--Pan 2021 and Zhang--Li 2025, while retaining Li--Zhao 2021, Qin--Zheng 2026 and Tao--Winkler 2025.

**Position now used:** neither stabilization for signal-dependent motility nor the pure-consumption case is claimed new. The claimed increment is the general dissipative-kinetics framework, nonzero equilibria, explicit quadratic/superquadratic rate dichotomy, degenerate algebraic signal rate, and the eventual finite-Lp transfer to strong norms.

## 2. Coercivity lemma novelty

**Referee concern:** Lemma 1 is elementary and should not be sold as an independent new weighted Poincare inequality.

**Action:** the manuscript now says explicitly: "The estimate is elementary; its role is to recover unweighted coercivity from positive mass without pointwise positivity of rho."

## 3. Choi boundary local-boundedness interface

**Referee concern:** the three-page version cited Choi too tersely and left hypotheses to the reader.

**Action:** isolated a new lemma `Boundary L2--Linfinity upgrade`. For n>=2 the proof now explicitly identifies:

- `A_ij = a delta_ij`;
- all lower-order coefficients and scalar source zero;
- forcing vector `F=H`;
- smooth bounded domain -> Sobolev extension domain;
- unused exponents chosen large so that Choi's `p_min=p`, `q_min=Q`;
- Choi's condition becomes exactly `n/p+2/Q<1`;
- lower-order norm `D=0`, hence fixed radius and constants are independent of the terminal time.

The application to the cell equation then verifies uniform ellipticity, the conormal condition, mixed-norm decay of the forcing, fixed-cylinder L2 decay, and the final finite covering.

## 4. One-dimensional endpoint

**Referee concern:** "the same De Giorgi proof applies" was too compressed because Choi states his theorem for d>=2.

**Action:** the local-upgrade lemma now includes a one-dimensional proof ingredient. For an interval and

`1/P + 2/Q = 1/2`, `2<=P<infinity`,

the manuscript proves

`||h||_{L_t^Q L_x^P} <= C(sup_t ||h(t)||_2 + ||h_x||_{L^2_{x,t}})`

from the one-dimensional Gagliardo--Nirenberg inequality. It then identifies this as the exact replacement for Choi Lemma 2.3 in Section 2.2 and notes that the remaining Caccioppoli estimate and De Giorgi iteration require only this embedding plus the local measure lower bound, which is automatic on an interval.

## 5. Sharpness

**Referee concern:** homogeneous solutions only prove sharpness of the signal exponent, not of the full strong-norm threshold.

**Action:** the proposition and concluding sentence now say explicitly that only the signal exponent `1/theta` is claimed optimal and that no sharpness claim is made for the full-system exponent.

## 6. Applications

**Referee concern:** the two corollaries should be illustrations, not presented as independent major results.

**Action:** Section 3 now opens by saying exactly that. The Qin--Zheng corollary explicitly preserves their upstream structural motility assumptions. The superlinear-consumption corollary is framed as a conditional decay-scale result complementing global-solution work such as Zhang--Li 2025.

## 7. Compression details

**Referee concern:** `s0=2p/(p-2)` became unnecessary once `grad v` was already known in Linfinity.

**Action:** removed `s0`. The cell energy estimate now uses the eventual Lp bound only to obtain a uniform L2 bound on u, then estimates the cross term directly by `||u||_2 ||grad q||_2 ||grad v||_infinity`.

## 8. Boundary condition

The manuscript now uses the natural no-flux formulation

`partial_nu(phi(v)u)=0`, `partial_nu v=0`.

This is exactly the conormal condition needed in the final scalar parabolic equation. Qin--Zheng impose `partial_nu u=partial_nu v=0`, which implies this no-flux condition for classical solutions.

## 9. Length

A local `elsarticle` compilation in `final,5p,times,twocolumn` format with a 10-item inline reference list still occupies three journal-format pages. Thus none of the proof-hardening material had to be removed to stay within the AML page limit.

## Current assessment

After this revision, the referee's two principal objections -- incomplete exact-model literature positioning and an under-verified final Linfinity bootstrap -- have been directly addressed. The main remaining external risk is novelty collision with very recent 2026 work not yet found in the current search, rather than a known proof gap in the present theorem chain.

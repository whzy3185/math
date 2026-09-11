# AML manuscript submission notes

Working title: **Mass-weighted damping and a rate dichotomy for chemotaxis with signal-dependent motility**

Target: *Applied Mathematics Letters*

## Current paper spine

1. nonlinear mass-weighted coercivity for every `q >= 2`;
2. an abstract weighted-damping rate dichotomy with positive mass and a uniform `L^2` bound on the weight;
3. full stabilization from eventual finite `L^p` control with `p > max{n,2}`;
4. quadratic damping -> exponential stabilization;
5. order `2+theta` damping -> signal rate `t^{-1/theta}` and full-system rates
   `mu < (1/theta) min{1, 2(p-n)/(pn)}`;
6. production--consumption and regular-motility superlinear-consumption illustrations;
7. homogeneous sharpness only for the signal exponent.

## Referee-strengthened status (2026-09-11)

The current `main.tex` has gone through three adversarial AML-style referee passes. The manuscript now has no known theorem-level gap in the main proof chain for `n>=1`; this is a proof-audit statement, not a novelty certificate.

### Novelty positioning

The introduction explicitly compares against:

- Li--Zhao 2021: boundedness and exponential large-time behavior for direct consumption;
- Li--Winkler 2023: relaxation for the exact local-sensing consumption model;
- Laurencot 2023: spatial homogenization in arbitrary dimension;
- Li--Winkler 2024: refined regularity and smooth stabilization;
- Li--Wang--Pan 2021: a logistic-source stabilization variant;
- Zhang--Li 2015: quantitative convergence rates for classical chemotactic-flux consumption;
- Zhang--Li 2025: global-solution theory for superlinear consumption with singular motility;
- Qin--Zheng 2026 and Tao--Winkler 2025 for the production--consumption comparison.

The manuscript explicitly says that neither signal-dependent motility nor stabilization for `F(s)=-s` is new. The claimed increment is the unified mechanism for general dissipative `F`, nonzero equilibria, degenerate damping, an explicit exponential/algebraic rate dichotomy, and eventual finite-`L^p` transfer to strong norms.

### Proof hardening

- The natural boundary condition is
  `partial_nu(phi(v)u)=0`, `partial_nu v=0`.
- Lemma 1 is explicitly called elementary; novelty is attached to its role in closing weighted damping, not to the inequality itself.
- The abstract damping theorem now explicitly requires a sufficiently regular solution (e.g. classical) so that testing by `z-z_*` is legitimate.
- The abstract and conclusion say that positive mass **together with finite/uniform `L^2` control** supplies the coercive closure.
- The `q>2` step records `X <= X^(2/q)` when `X <= 1`.
- The strong-signal step contains the unit-interval Duhamel formula and the integrability condition `1/2+n/(2r)<1`.
- The cell `L^2` estimate uses the eventual finite-`L^p` hypothesis only to obtain a uniform `L^2` bound on `u`, then pairs directly with `||grad v||_infinity`.
- The final `L^infinity` bootstrap is isolated as a boundary local-boundedness lemma with the weak-energy solution class and the mixed norm `L^{p,Q}=L_t^Q L_x^p` explicitly defined.
- The local-upgrade lemma assumes `p>max{n,2}`. For `n>=2`, the mapping to Choi Theorem 1.1 is explicit (`p_1=p`, `q_1=Q`, lower-order coefficients and scalar source zero, forcing vector `H`).
- For `n=1`, the manuscript does not merely say that the De Giorgi proof is unchanged. It supplies the one-dimensional Gagliardo--Nirenberg mixed-norm replacement, estimates the forcing term on level sets, and records a nonlinear recurrence
  `Y_{j+1} <= C b^j Y_j^(1 + 2 delta/(1+2 delta))`
  with `delta>0`, which closes the iteration.
- The Qin--Zheng application states that their structural motility assumptions remain upstream boundedness assumptions and are not removed by the stabilization theorem.
- The superlinear-consumption illustration uses `F(s)=-s^gamma`, `gamma>1`, to avoid conflict with the conserved mass `m`.
- The Zhang--Li 2025 comparison is qualified explicitly: that paper treats a singular-motility regime near `v=0`, which is **not covered** by Theorem 3's regular-motility assumptions.
- Sharpness is restricted to the signal exponent `1/theta`; no sharpness claim is made for the full-system threshold.

## Safe novelty language

Use:

> Positive conserved mass together with finite `L^2` control supplies an elementary but effective coercive closure that turns quadratic or degenerate signal dissipation into explicit rates for general dissipative kinetics; eventual finite-`L^p` control is enough to propagate these rates to the full signal-dependent-motility system.

Avoid:

- "first stabilization result for signal-dependent motility";
- "new weighted Poincare inequality";
- "we remove the Qin--Zheng assumptions" without restricting this to the stabilization stage;
- "the full algebraic rate is sharp";
- wording that suggests Theorem 3 applies directly to Zhang--Li 2025's singular motility setting.

## Length status

The terminal referee-hardened version compiles locally in `elsarticle` `final,5p,times,twocolumn` format in **4 journal-format pages** with an 11-item reference list in the preview. The rendered pages were inspected: there is no clipping, overlap, undefined citation, or overfull box.

## Final pre-submission items

1. Do one short final 2026 forward-citation / same-model collision search immediately before submission.
2. Decide whether to replace the secondary Neumann heat-semigroup source by an original semigroup source; this is a citation-quality preference, not a proof issue.
3. Insert author metadata, ORCID, funding/acknowledgements and any journal-required declarations.
4. Recompile with the final BibTeX toolchain used for submission and visually inspect the resulting PDF.
5. Recheck `T+1`, `T+2`, and fixed-cylinder time shifts after any final copy edit.
6. Do not add further theorems/applications unless a concrete error or direct novelty collision is found.

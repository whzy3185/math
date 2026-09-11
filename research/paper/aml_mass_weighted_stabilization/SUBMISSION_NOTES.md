# AML manuscript submission notes

Working title: **Mass-weighted damping and a rate dichotomy for chemotaxis with signal-dependent motility**

Target: *Applied Mathematics Letters*

## Current paper spine

1. nonlinear mass-weighted coercivity for every `q >= 2`;
2. an abstract weighted-damping rate dichotomy with only positive mass and a uniform `L^2` bound on the weight;
3. full stabilization from eventual finite `L^p` control with `p > max{n,2}`;
4. quadratic damping -> exponential stabilization;
5. order `2+theta` damping -> signal rate `t^{-1/theta}` and full-system rates
   `mu < (1/theta) min{1, 2(p-n)/(pn)}`;
6. production--consumption and superlinear-consumption illustrations;
7. homogeneous sharpness only for the signal exponent.

## Referee-strengthened status (2026-09-11)

The current `main.tex` now addresses the main objections raised by an adversarial AML-style referee audit.

### Novelty positioning

The introduction no longer lets Li--Zhao 2021 stand in for the full pure-consumption literature. It now explicitly compares against:

- Li--Zhao 2021: boundedness and exponential large-time behavior for direct consumption;
- Li--Winkler 2023: relaxation for the exact local-sensing consumption model;
- Laurencot 2023: spatial homogenization in arbitrary space dimension;
- Li--Winkler 2024: refined regularity and smooth stabilization;
- Li--Wang--Pan 2021: a logistic-source stabilization variant;
- Zhang--Li 2025: global-solution theory for superlinear consumption;
- Qin--Zheng 2026 and Tao--Winkler 2025 for the production--consumption comparison.

The manuscript explicitly says that neither signal-dependent motility nor stabilization for `F(s)=-s` is new. The claimed increment is the unified mechanism for general dissipative `F`, nonzero equilibria, degenerate damping, explicit rate dichotomy, and eventual finite-`L^p` transfer to strong norms.

### Proof hardening

- The natural boundary condition is written as
  `partial_nu(phi(v)u)=0`, `partial_nu v=0`.
- Lemma 1 is explicitly called elementary; novelty is attached to its role in closing weighted damping, not to the inequality itself.
- The `q>2` step records `X <= X^(2/q)` when `X <= 1`.
- The strong-signal step contains the unit-interval Duhamel formula and the integrability condition `1/2+n/(2r)<1`.
- The cell `L^2` estimate no longer introduces the unnecessary exponent `s0`; the eventual `L^p` hypothesis first gives an `L^2` bound on `u`, which is then paired directly with `||grad v||_infinity`.
- The final `L^infinity` bootstrap is now isolated as a separate boundary local-boundedness lemma.
- For `n>=2`, the mapping to Choi Theorem 1.1 is explicit: leading matrix `a I`, lower-order coefficients and scalar source zero, forcing vector `H`, smooth bounded domain as Sobolev extension domain, unused mixed exponents chosen large, and the fixed radius is time-independent because Choi's lower-order norm `D` vanishes.
- For `n=1`, the manuscript proves the missing mixed-norm embedding from the one-dimensional Gagliardo--Nirenberg inequality and explains exactly how it replaces Choi Lemma 2.3 in the De Giorgi proof. The interval measure-density bound is automatic.
- The Qin--Zheng application states that their structural motility assumptions remain upstream boundedness assumptions and are not removed by the stabilization theorem.
- The superlinear-consumption corollary is explicitly framed as an illustration/conditional decay result, not a new global-existence theorem.
- Sharpness is explicitly restricted to the signal exponent `1/theta`; no sharpness claim is made for the full-system threshold.

Current manuscript proof status: **no known theorem-level gap for `n>=1` after the referee-strengthening pass**. This is not a novelty certificate.

## Safe novelty language

Use:

> Positive conserved mass supplies an elementary but effective coercive closure that turns quadratic or degenerate signal dissipation into explicit rates for general dissipative kinetics; eventual finite-`L^p` control is enough to propagate these rates to the full signal-dependent-motility system.

Avoid:

- "first stabilization result for signal-dependent motility";
- "new weighted Poincare inequality";
- "we remove the Qin--Zheng assumptions" without restricting this to the stabilization stage;
- "the full algebraic rate is sharp".

## Length status

The referee-strengthened version still compiles in the `elsarticle` `final,5p,times,twocolumn` format in **3 journal-format pages** with a 10-item reference list in the local preview. Thus there is no need to delete the Choi mapping, the one-dimensional endpoint argument, or the expanded prior-art comparison merely to meet AML's page cap.

## Remaining pre-submission items

1. Run one final forward-citation search for Qin--Zheng 2026 and same-model papers appearing after the current literature pass.
2. Decide whether to replace the secondary Neumann heat-semigroup source by an original source.
3. Insert author metadata, funding/acknowledgements and any journal-required declarations.
4. Recompile with the final BibTeX toolchain used for submission and visually inspect the resulting PDF.
5. Recheck `T+1`, `T+2`, and fixed-cylinder time shifts after any final copy edit.

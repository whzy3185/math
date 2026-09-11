# AML manuscript submission notes

Working title: **Mass-weighted damping and a rate dichotomy for chemotaxis with signal-dependent motility**

Target: *Applied Mathematics Letters*

## Current paper spine

The paper is organized around one structural chain rather than a model-specific follow-up:

1. nonlinear mass-weighted coercivity for every `q >= 2`;
2. a weighted-damping rate dichotomy for `z_t = Delta z + rho F(z)` with only fixed positive mass and a uniform `L^2` bound on `rho`;
3. full stabilization of the signal-dependent-motility system from eventual finite `L^p` control with `p > max{n,2}`;
4. quadratic dissipation -> exponential stabilization;
5. degenerate order `2+theta` -> algebraic signal decay and the explicit full-rate threshold
   `mu < (1/theta) min{1, 2(p-n)/(pn)}`;
6. two applications: Qin--Zheng production--consumption and superlinear signal consumption;
7. homogeneous-profile sharpness for the signal exponent `1/theta`.

This is stronger than the older manuscript blueprint based only on uniform `L^infinity` boundedness and finite-`p` convergence of `u`.

## Proof-hardening status (2026-09-11)

The current `main.tex` has been line-checked through the main proof chain.

- The nonlinear mass-weighted coercivity constants were recomputed.
- The `q>2` closure now explicitly records the step `X <= X^(2/q)` for `X <= 1`.
- The strong-signal step now writes the unit-interval Duhamel formula, the integrable semigroup singularity, and the mean-to-`L^infinity` recovery explicitly.
- The cell energy step records the finite-measure passage from `||grad v||_{s0}` to `||grad v||_infinity`.
- The boundary conditions are stated as `partial_nu u = partial_nu v = 0`, and the final cell equation records the exact conormal identity.
- Choi Theorem 1.1 is used directly for `n >= 2` with all lower-order coefficients zero and forcing vector `B = u phi'(v) grad v`.
- The theorem still covers `n = 1`: Choi states his Neumann result for `d >= 2`, so the manuscript supplies the missing one-dimensional mixed-norm embedding from Gagliardo--Nirenberg and observes that the same lower-order-free De Giorgi iteration then gives the identical fixed-radius estimate.
- The Qin--Zheng corollary now records both the invariant signal interval and the passage from their uniform boundedness theorem to the finite-`L^p` hypothesis.
- The superlinear-consumption corollary explicitly inherits the remaining hypotheses of the full stabilization theorem.

Current proof status: no known theorem-level gap in the manuscript proof chain for `n >= 1`. This is a manuscript audit statement, not a novelty certificate.

## Safe novelty language

Use formulations such as:

> We isolate a mass-weighted damping mechanism that converts positive conserved mass and dissipative signal kinetics into quantitative stabilization rates for signal-dependent motility systems.

> The conditional stabilization theorem requires positivity, but not monotonicity, of the motility on the invariant signal range.

> The boundedness theorem of Qin and Zheng supplies the upstream hypothesis in the production--consumption model; the present argument identifies the asymptotic state and exponential rate.

Avoid:

- "first stabilization result for signal-dependent motility";
- "the production--consumption problem was open";
- "new weighted Poincare inequality";
- "we remove the Qin--Zheng assumptions" without saying "from the stabilization stage";
- calling the full algebraic threshold sharp. Only the signal exponent `1/theta` is currently supported by the homogeneous profile.

## Six-to-eight page AML compression plan

If the compiled draft is too long, compress in this order:

1. Keep Lemma 1 (coercivity), Theorem 2 (rate dichotomy), and Theorem 3 (full stabilization) in full.
2. Keep the proof of Lemma 1 and the scalar ODE integration in Theorem 2; these are short and expose the mechanism.
3. Compress the proof of Theorem 3 into three paragraphs: strong signal norm, cell `L^2`, boundary local-boundedness upgrade. Preserve the two-sentence `n=1` endpoint explanation even if other details are shortened.
4. Move the explicit definition of `Gamma_q` to a sentence in the proof if space is tight.
5. State the Qin--Zheng application as a corollary of two or three lines.
6. Keep superlinear consumption because it demonstrates genuinely degenerate kinetics and gives a concrete algebraic rate.
7. Keep the homogeneous sharpness proposition only if space permits; otherwise mention the exact profile in a final remark.
8. Do not add a preliminaries section, numerical examples, or a separate formal-verification section.

## Referee-facing comparisons to retain in the introduction

- **Qin--Zheng 2026:** same signal-dependent-motility production--consumption model; their displayed main result is global boundedness under an explicit motility condition. Present paper starts from an eventual finite-`L^p` bound and derives the asymptotic dynamics.
- **Tao--Winkler 2025:** same simultaneous production/consumption reaction but classical chemotactic sensitivity, not `Delta(phi(v)u)`.
- **Li--Zhao 2021:** same signal-dependent motility with pure consumption; exponential stabilization is already known there and must be acknowledged as a direct predecessor.
- **Choi 2016:** boundary local boundedness theorem used only for the final `L^infinity` cell upgrade in dimensions `n >= 2`; the one-dimensional endpoint is supplied in the manuscript by the corresponding Gagliardo--Nirenberg/De Giorgi adaptation.

## Before submission freeze

1. Run a fresh theorem-to-theorem novelty search, especially forward citations of Qin--Zheng 2026 and papers citing Li--Zhao 2021.
2. Keep the current explicit mapping to Choi's notation when compressing the proof; do not collapse the conormal condition or the `n=1` endpoint into an unsupported citation.
3. Check the chosen Neumann heat-semigroup reference and replace the secondary chapter citation by an original source if preferred by the journal style.
4. Insert author metadata, funding, data/code statement if required, and acknowledgements.
5. Compile with the current Elsevier class and reduce displayed equations if the page count exceeds the Letter format.
6. Check all constants and time shifts (`T+1`, `T+2`, fixed backward cylinders) for one consistent convention throughout the final compiled version.

## Current recommended abstract emphasis

Lead with the rate dichotomy and eventual finite-`L^p` hypothesis. Do not lead with "boundedness implies stabilization" because that slogan is too broad in the literature.

Recommended one-sentence contribution summary:

> Positive conserved mass induces a nonlinear weighted coercivity that turns quadratic or degenerate signal dissipation into explicit exponential or algebraic stabilization rates, and eventual finite-`L^p` control of the cell density is enough to propagate these rates to the full signal-dependent-motility system.

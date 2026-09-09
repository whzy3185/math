# Two-paper split: strict self-contained version

Date: 2026-09-09

This file fixes the final editorial and mathematical boundary between the two signed-circulant papers.

## Non-negotiable independence rule

The two papers are to be **fully independent manuscripts**.

- Paper I must not cite Paper II, even as a preprint or companion paper.
- Paper II must not cite Paper I, even as a preprint or companion paper.
- No theorem from one manuscript may be used as a black box in the other.
- Any elementary switching/flux/Fourier lemma needed by both papers must be stated and proved separately in each manuscript (or cited only to an external standard source when genuinely standard).
- The two papers may use the same underlying graph family and compatible notation, but their theorem statements and proof chains must close internally.
- No result should be advertised as "proved in the companion paper".

The split is therefore by **quantifier and mathematical question**, not by historical branch.

---

## Paper I — explicit periodic phases and sharp spectral gaps

Working branch:

`paper/circulant-periodic-gap-20260909`

Working title:

**Periodic flux phases in signed circulants: sharp spectral gaps and an exactly solvable base model**

Central question:

> For a structurally explicit periodic signing of the step-`(1,s)` operator, how far below the spectral edge can the continuous Bloch spectral radius be pushed, and what is the sharp large-`s` asymptotic mechanism?

Central object: the continuous squared Bloch/Floquet radius `Rhat_s` of an explicit parity-dependent periodic family, with

\[
\widehat g_s=8-\widehat R_s.
\]

### Results owned by Paper I

1. A self-contained switching/flux and Bloch reduction sufficient for the explicit periodic phases.
2. The half-cell/chiral criterion required for those phases.
3. Explicit parity-dependent phases for every `s>=2`:
   - odd `s`: period-two alternating-flux phase;
   - even `s`: primitive period-`4s` antipodal-defect phase.
4. Strict sub-edge theorem
   \[
   \widehat R_s<8.
   \]
5. Quantitative two-sided gap bounds.
6. Sharp leading asymptotic
   \[
   s^2\widehat g_s\to\pi^2.
   \]
7. Even-jump optimizing phase-slip asymptotics, including the audited second-order constants.
8. The `s=2` period-eight phase as an exactly solvable **single explicit phase**: exact fiber dispersion, holonomy dependence, and the direct comparison that originally produced a counterexample to the twisted optimizer conjecture.

### Results forbidden in Paper I

Paper I must not contain any theorem whose main quantifier is over **all finite signings** of `C_N(1,s)`. In particular it excludes:

- the global finite minimum `m(N,s)` as a main object;
- `m(N,s)=2 iff N=2s+2`;
- the universal `sqrt(5)` finite lower bound;
- the complete `N=3s` threshold classification;
- odd-`s` global finite obstruction certificates;
- minimal-period results obtained by comparing all competing signing patterns;
- uniqueness/rigidity statements obtained by classifying all finite signings or all switching classes.

In the `s=2` section, Paper I may solve the spectral fibers of the chosen period-eight word, but it must not claim that the word is globally unique or has globally minimal primitive period among all signings.

### Self-contained proof closure

Every upper bound, Bloch identity, phase-slip lemma, and asymptotic statement used in Paper I must be proved inside Paper I. Paper I cannot invoke finite extremal results from Paper II.

---

## Paper II — finite extrema, threshold transitions, and rigidity

Working branch:

`paper/circulant-finite-threshold-20260909`

Working title:

**Finite spectral extrema in signed step circulants: flat minima, threshold transitions, and rigidity**

Central object:

\[
m(N,s)=\min_\sigma \rho(A_\sigma),
\qquad 2\le s<N/2.
\]

Central question:

> What can be proved exactly about the minimum spectral radius over all finite signings, including equality cases, threshold transitions, exceptional arithmetic cases, and rigidity?

### Results owned by Paper II

1. Exact flat-minimum classification
   \[
   m(N,s)=2\iff N=2s+2.
   \]
2. Universal finite lower bound outside the flat case, currently
   \[
   m(N,s)\ge\sqrt5.
   \]
3. Complete threshold classification on `N=3s`:
   \[
   m(3s,s)<\sqrt8
   \iff
   s\text{ is even or }s\in\{3,5\}.
   \]
4. Direct, self-contained construction and Fourier proof for the even-`s` sub-`sqrt8` witness on `N=3s`:
   \[
   m(3s,s)^2\le 6+2\cos\frac{2\pi}{3s}<8.
   \]
   This proof must be included in Paper II itself; it must not cite Paper I's periodic-family theorem.
5. Exact exceptional cases `s=3,5`, including exact certificates converted into a publication-quality proof/certificate presentation.
6. Uniform odd obstruction for all odd `s>=7`, currently
   \[
   m(3s,s)^2\ge 8+\frac1{70}.
   \]
7. Finite rigidity/minimal-period/unique-orbit results for `s=2` **only when they quantify over competing finite signings or switching classes**.
8. Any later generalization from `N=3s` to broader resonance families belongs exclusively to Paper II.

### Results forbidden in Paper II

Paper II must not use or state as a main theorem:

- the all-`s` explicit continuous Bloch family from Paper I;
- the sharp periodic-gap asymptotic `s^2(8-Rhat_s)->pi^2`;
- the even phase-slip asymptotics of the period-`4s` family;
- the full exact period-eight dispersion analysis except for the minimal finite facts needed to prove a rigidity theorem, in which case those facts must be rederived locally.

Paper II may use switching, flux, traces, Fourier diagonalization, and finite certificates, but all such ingredients required for its proofs must be presented independently.

---

## No-overlap rule for the base case `s=2`

The historical period-eight project is split as follows.

Paper I owns:

- one explicit period-eight word;
- its exact Bloch/Floquet dispersion;
- its holonomy dependence;
- its direct spectral comparison with the twisted signing;
- its role as a model for the general periodic mechanism.

Paper II owns:

- statements that quantify over all candidate signings/switching classes;
- first possible primitive period below a threshold;
- uniqueness of a sub-threshold orbit when genuinely proved globally;
- finite extremal or rigidity classification.

The same theorem must not appear in both papers.

---

## Publication strategy under strict independence

Paper I is an analytic/spectral construction paper. Its strength comes from the all-jump explicit mechanism, the parity-free sharp constant `pi^2`, and the second-order phase-slip analysis. Its weakness is that it does not solve the global finite minimization problem.

Paper II is a finite extremal/classification paper. Its strength comes from exact equality and threshold classification over all signings. Its weakness is that the current broad threshold theorem is concentrated on one resonance line `N=3s`; extending the resonance theory would materially raise its ceiling.

Neither manuscript should describe the other manuscript or depend on its existence.

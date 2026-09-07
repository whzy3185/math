# Manuscript architecture: sharp Bloch gaps and an arithmetic resonance transition

Current status date: 2026-09-07
Branch: `research/quadratic-gap-upgrade`

## Working title

**Sharp Bloch Gaps and an Arithmetic Phase Transition in Signed Circulants**

Alternative:

**Parity, Phase Slip, and Finite Resonance in Signed `C_N(1,s)`**

## Central contribution package

The paper can now be organized around two complementary theorems, neither of
which depends on an open conjecture.

### Main periodic theorem

For an explicit parity-dependent periodic signing for every integer jump
`s>=2`, with squared Bloch radius `Rhat_s`,

\[
 Rhat_s<8,
 \qquad
 s^2(8-Rhat_s)\to\pi^2.
\]

Odd and even jumps use different sign patterns but have the same sharp
leading constant.

For even `s=2r`, the endpoint is not exactly phase-maximizing.  The phase
slip is proved to satisfy

\[
 r^2\phi_r\to\frac\pi{4\sqrt2},
 \qquad
 r^4(e_r-g_{2r})\to\frac{\pi^2}{32}.
\]

This turns the exact `s=10` phase-zero counterexample into a quantitative
avoided-crossing theorem.

### Main finite theorem

Let `m(N,s)` minimize spectral radius over all edge signings of `C_N(1,s)`.
On the full resonance line `N=3s`,

\[
 \boxed{
 m(3s,s)<\sqrt8
 \iff s\text{ is even, or }s\in\{3,5\}.}
\]

For every odd `s>=7`, the stronger uniform all-signing obstruction is

\[
 m(3s,s)^2\ge8+\frac1{70}.
\]

The short odd cases `s=3,5` have exact positive-definiteness certificates,
and even `s` has an explicit antiperiodic alternating signing below the
threshold.  Hence odd `s=7` is a genuine threshold transition, not a proof
artifact.

The universal flat theorem can be stated alongside this:

\[
 m(N,s)=2\iff N=2s+2,
 \qquad
 N\ne2s+2\Rightarrow m(N,s)\ge\sqrt5.
\]

## Proposed theorem hierarchy

### Theorem A — all-jump explicit periodic family

Define the parity-dependent construction:

- odd `s`: period-two alternating-flux word;
- even `s`: primitive period-`4s` antipodal word.

Prove `Rhat_s<8` and the common quadratic envelope.

### Theorem B — odd-jump exact model

Prove the exact Fourier dispersion, unique maximizing phase, Chebyshev
critical equation, and `s^2(8-M_s)->pi^2`.

### Theorem C — even antipodal determinant and quadratic gap

Develop chirality, the reduced threshold matrix, continuants, positive
generating functions and the inverse-trace quadratic lower bound.

### Proposition D — exact phase-zero failure

Give the `s=10` rational/Sturm certificate showing an interior phase beats
zero phase.

### Theorem E — even global sharp leading constant

Use phase localization and the limiting Robin equation to prove

` s^2(8-R_s)->pi^2 ` through even jumps.

### Theorem F — even second-order phase slip

Prove

`r^2 phi_r -> pi/(4sqrt2)`

and

`r^4(e_r-g_(2r)) -> pi^2/32`,

with the local effective parabola

`z^2-(pi/(2sqrt2))z`.

### Corollary G — parity-free sharp Bloch theorem

Combine odd and even subsequences:

` s^2(8-Rhat_s)->pi^2 `.

### Theorem H — universal flat finite minimum

State and prove

`m(N,s)=2 iff N=2s+2`, otherwise `m(N,s)>=sqrt5`.

### Theorem I — exact `N=3s` threshold phase transition

Prove

`m(3s,s)<sqrt8 iff s even or s in {3,5}`.

Proof pieces:

- even `s`: exact antiperiodic Fourier bound
  `rho^2<=8-4 sin^2(pi/(3s))`;
- `s=3,5`: exact Sylvester certificates;
- odd `s>=7`: uniform all-signing obstruction `8+1/70`.

### Lemma J — nine-column signed-triangle rule

For an open nine-column width-three strip, either a local integer Rayleigh
certificate gives squared norm at least `8+1/70`, or the six middle
transitions alternate exactly.  Sliding this rule around an odd helical cycle
forces a signed triangle to be orthogonally similar to its negative, which is
impossible because `tr(B^3)=+/-6` changes sign.

## Suggested section plan

1. **Introduction** — fixed-graph signing minimization; statement of both main
   phenomena.
2. **Switching, Hamilton gauge and finite/Bloch models**.
3. **Odd jumps: exact Fourier theory**.
4. **Even jumps: antipodal chirality and continuant determinant**.
5. **Quadratic gap and sharp `pi^2` leading asymptotics**.
6. **Phase slip and the second-order avoided-crossing law**.
7. **Finite minima: the exact flat line**.
8. **Width-three resonance model on `N=3s`**.
9. **Exact nine-column forbidden-word lemma**.
10. **Short cases and complete `N=3s` threshold classification**.
11. **Reproducibility and formalization boundary**.
12. **Literature positioning and open problems**.

## Evidence/reproducibility presentation

The manuscript must distinguish:

- analytic proofs;
- exact finite computer-assisted lemmas/theorems;
- numerical experiments used only for discovery/audit;
- uncompiled Lean source.

The finite `N=3s` proof is computer-assisted only through bounded exact
integer certificates.  The final accepted inequalities are not floating
claims.  On 2026-09-07 the key local rule and both exhaustive base cases were
independently rerun in the current analysis environment.

## Higher-order phase-slip refinement

`EVEN_THIRD_ORDER_PHASE_SLIP_REFINEMENT.md` derives candidate/provisional
`r^-3` phase and `r^-5` gain corrections.  These are **not required** for the
paper's main claims and should remain in an appendix or future-work section
until the uniform `o(r^-1)` remainder is audited at the same level as the
second-order theorem.

## Publication boundary

Do not claim:

- an exact formula for `m(N,s)` for every pair;
- global optimality of the periodic parity-dependent family on arbitrary
  finite rings;
- novelty of switching, Floquet theory, block-Jacobi methods, or flux-phase
  ideas themselves;
- a complete finite classification beyond the explicitly proved `N=3s`
  threshold and flat line;
- final priority before the broader magnetic/flux-phase audit is complete.

Closest direct 2026 comparison remains Suvagiya's `C_n(1,2)` work, together
with the companion parity-family framework.  The current safe distinct
package is arbitrary-jump sharp Bloch asymptotics, even phase-slip constants,
and the exact all-signing arithmetic transition on `N=3s`.

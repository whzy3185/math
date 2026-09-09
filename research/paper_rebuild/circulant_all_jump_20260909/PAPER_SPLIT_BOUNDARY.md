# Two-paper split for the signed-circulant project

Date: 2026-09-09

This file fixes the editorial and mathematical boundary between two papers emerging from the repository-wide signed-circulant program.

## Paper I — periodic phases and sharp spectral gaps

Working branch:

`paper/circulant-periodic-gap-20260909`

Working title:

**Periodic flux phases in signed circulants: sharp spectral gaps and an exactly solvable base model**

Central object: the continuous Bloch/Floquet spectral radius of explicit periodic signings of `C_N(1,s)`, not the global finite minimization problem over all signings.

### Results assigned to Paper I

1. Switching/flux coordinates and the periodic Bloch reduction needed for explicit phases.
2. The all-phase half-cell/chiral criterion
   \[
   D T_m=-T_mD
   \quad\Longleftrightarrow\quad
   \tau_{i+m}=(-1)^{s+1}\tau_i.
   \]
3. Explicit parity-dependent periodic phases for every `s>=2`:
   - odd `s`: period-2 alternating-flux phase;
   - even `s`: primitive period-`4s` antipodal double-defect phase.
4. Strict sub-edge bound for the explicit family:
   \[
   \widehat R_s<8.
   \]
5. Quantitative gap bounds for
   \[
   \widehat g_s:=8-\widehat R_s.
   \]
6. Sharp leading asymptotic
   \[
   s^2\widehat g_s\to\pi^2.
   \]
7. Even-jump phase-slip asymptotics, including
   \[
   r^2\phi_r\to \frac{\pi}{4\sqrt2},
   \qquad
   r^4(e_r-g_{2r})\to \frac{\pi^2}{32},
   \]
   subject to the final proof audit of the exact notation used in the integrated manuscript.
8. The `s=2` period-8 phase as an exactly solvable model: exact fiber dispersion, holonomy dependence, and the original counterexample mechanism. This material is explanatory/base-model material here, not a finite global extremal classification.
9. The original `C_N(1,2)` twisted-optimizer conjecture and its explicit period-8 counterexample family may be stated in the introduction as historical motivation, with the precise finite counterexample theorem included if it does not interrupt the general-flow narrative.

### Results explicitly excluded from Paper I

The following are not main theorems of Paper I and should be cited to Paper II or deferred:

- exact global finite minimum `m(N,s)`;
- `m(N,s)=2 iff N=2s+2`;
- universal finite lower bound away from the flat case;
- exact `N=3s` threshold classification;
- finite obstruction certificates for odd `s>=7`;
- global minimal-period / unique-orbit statements whose proof quantifies over all finite signings rather than the explicit periodic family.

### Narrative test

Every main theorem in Paper I should answer one question:

> How far below the unsigned/twisted spectral edge can an explicit, structurally natural periodic flux phase push the Bloch spectral radius, and what is the sharp large-jump asymptotic mechanism?

If a result instead asks for the minimum over **all** finite signings, it belongs to Paper II.

---

## Paper II — finite extrema, thresholds, and rigidity

Recommended branch for the second conversation:

`paper/circulant-finite-threshold-20260909`

Working title:

**Finite spectral extrema in signed step circulants: flat minima, threshold transitions, and rigidity**

Central object:

\[
 m(N,s)=\min_{\sigma}\rho(A_\sigma).
\]

### Results assigned to Paper II

1. Exact flat minimum:
   \[
   m(N,s)=2\iff N=2s+2.
   \]
2. The corresponding universal finite lower bound outside the flat case (currently `m(N,s)>=sqrt(5)` in the audited package).
3. Complete threshold classification on the resonance line `N=3s`:
   \[
   m(3s,s)<\sqrt8
   \iff
   s\text{ is even or }s\in\{3,5\}.
   \]
4. Exact exceptional cases `s=3,5` and all required finite certificates.
5. Uniform obstruction for odd `s>=7`, including the audited bound
   \[
   m(3s,s)^2\ge 8+\frac1{70}.
   \]
6. Finite rigidity/minimal-period classification for the `s=2` model when the result concerns all signings rather than only the explicit period-8 fiber.
7. Computational/exact-enumeration evidence only when clearly labeled and used to support a fully stated proof or to formulate open problems.

### Results Paper II may cite but should not re-prove at full length

- the general Bloch machinery from Paper I;
- the explicit even/odd periodic witness families from Paper I;
- the sharp `pi^2/s^2` periodic-gap asymptotic, unless directly needed in a finite comparison.

Paper II may restate the minimal lemmas required for self-contained finite arguments, but it should not become a second exposition of the periodic-gap paper.

---

## Shared notation and interface contract

Both manuscripts should use the same base notation for:

- `C_N(1,s)`;
- signed adjacency matrices `A_\sigma`;
- switching equivalence / flux variables;
- `m(N,s)` for the global finite minimum;
- `\widehat R_s` for the continuous Bloch radius of the explicit periodic family;
- `\widehat g_s=8-\widehat R_s` for its spectral gap.

The distinction

\[
\widehat R_s\quad\text{versus}\quad m(N,s)^2
\]

must never be blurred. Paper I supplies explicit witnesses; Paper II studies the global finite extremum.

## Publication strategy

Paper I should be completed first. Its strongest unifying headline is the all-jump periodic construction plus

\[
s^2(8-\widehat R_s)\to\pi^2.
\]

Paper II should continue theorem strengthening if possible before final submission, especially beyond the single resonance line `N=3s`.

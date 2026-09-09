# Two-paper split: strict self-contained version

Date: 2026-09-09

The two signed-circulant papers are fully independent manuscripts.

## Absolute independence rules

- Paper I and Paper II do not cite each other.
- No theorem from one paper may be used as a black box in the other.
- Any switching/flux/Fourier lemma needed in both must be stated and proved independently in each paper, unless it is cited to an external standard source.
- No sentence of the form "by the companion paper" or "proved elsewhere in this project" is permitted.
- The same theorem must not be duplicated as a headline theorem in both papers.

## Paper I: explicit periodic phases and sharp Bloch gaps

Branch: `paper/circulant-periodic-gap-20260909`

Paper I owns only the explicit periodic-family problem: the continuous Bloch radius `Rhat_s`, strict sub-eight periodic phases for every `s`, sharp gap asymptotics `s^2(8-Rhat_s)->pi^2`, even phase-slip asymptotics, and the exact dispersion of one explicit `s=2` period-eight phase.

Paper I does **not** contain global statements quantified over all finite signings. In particular it excludes `m(N,s)=2 iff N=2s+2`, the `sqrt(5)` lower bound, the `N=3s` global threshold classification, odd global obstruction certificates, and global minimal-period/uniqueness results.

## Paper II: finite extrema, thresholds, and rigidity

Branch: `paper/circulant-finite-threshold-20260909`

Paper II owns the finite global minimization problem

\[
m(N,s)=\min_\sigma\rho(A_\sigma).
\]

Its current core theorem package is:

\[
m(N,s)=2\iff N=2s+2,
\]

with the off-flat lower bound `m(N,s)>=sqrt(5)`, and

\[
m(3s,s)<\sqrt8\iff s\text{ is even or }s\in\{3,5\},
\]

including exact treatment of `s=3,5` and the uniform odd obstruction

\[
m(3s,s)^2\ge 8+\frac1{70}\qquad(s\ge7\text{ odd}).
\]

For even `s` on `N=3s`, Paper II must prove its own witness directly, for example by the self-contained Fourier computation

\[
m(3s,s)^2\le 6+2\cos\frac{2\pi}{3s}<8,
\]

rather than invoking Paper I.

Paper II must not use the all-jump Bloch theorem, the `pi^2/s^2` periodic-gap asymptotic, or the phase-slip theorem from Paper I.

## `s=2` ownership rule

Paper I: exact spectral analysis of one explicit period-eight phase.

Paper II: statements that classify or compare all finite signings/switching classes, including genuine minimal-period or uniqueness/rigidity claims.

This quantifier-based split is final unless a theorem is later strengthened enough to force a redesign.

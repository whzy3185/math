# Literature boundary update for the final theorem package

Date checked: 2026-09-07.

This is a targeted positioning audit, not a priority certificate.  It
supersedes numerical constants in `LITERATURE_UPDATE_20260906.md` where the
finite `N=3s` margin was still recorded in an older form.

## 1. Closest direct signed-circulant work

Vaibhav Suvagiya, **Signed circulants at the Ramanujan bound**,
arXiv:2607.18334 (July 2026), treats `C_n(1,2)`.

Primary record: https://arxiv.org/abs/2607.18334

The paper proves the exact Fourier spectrum of the alternating/twisted
`C_n(1,2)` parity family, identifies four switching classes for the all-
unbalanced-quadrilateral system when `n` is even, and gives the twisted value

`2 sqrt(cos^2(pi/n)+cos^2(2pi/n)) < 2 sqrt(2)`.

It exhaustively verifies global optimality only for a finite list of even
orders and states the general even-order optimality as a conjecture.  For odd
orders its quadrilateral parity system is inconsistent.

The current project must not claim the `s=2` twisted formula as new.  Its
distinct scope is arbitrary jump `s`, the even-jump antipodal defect family,
sharp all-`s` `pi^2/s^2` Bloch gaps, phase-slip asymptotics, and the all-signing
finite resonance classification on `N=3s`.

## 2. Companion parity-family framework

Suvagiya, **Parity families and a kernel-averaged L-function for
near-Ramanujan signings**, arXiv:2607.17343 (July 2026), develops affine
`F_2` families that make short even cycles unbalanced and studies averaged
trace / Ihara-L-function bounds for near-Ramanujan signings.

Primary record: https://arxiv.org/abs/2607.17343

This is important conceptual prior art for parity constraints and Bilu--Linial
signing methods.  It does not, from the inspected abstract/metadata, supply
the current exact all-jump circulant Bloch asymptotics or the `N=3s`
all-signing threshold theorem.

## 3. Flux-phase / magnetic operator boundary

Lieb, **Flux Phase of the Half-Filled Band**, Phys. Rev. Lett. 73 (1994),
proves an optimum magnetic-flux theorem for a half-filled fermionic model on
planar bipartite graphs with periodicity.  It is relevant conceptual prior art
for flux optimization, but its objective and hypotheses are not the present
fixed signed-adjacency spectral-radius minimization problem.

Higuchi--Shirai, **The Spectrum of Magnetic Schrodinger Operators on a Graph
with Periodic Structure**, J. Funct. Anal. 169 (1999), studies spectra of
discrete magnetic operators on covering graphs and dependence on magnetic
flow.

Korotyaev--Saburova, **Magnetic Schrodinger operators on periodic discrete
graphs**, J. Funct. Anal. 272 (2017), develops Floquet fiber representations,
band spectra and flux-dependent estimates on periodic graphs.

These sources confirm that Bloch/Floquet and magnetic-flux language is mature
framework and should be cited as such.  The current contribution should be
phrased in terms of its explicit signed-circulant constructions, sharp gap
constants and finite all-signing obstruction, not as a novelty claim about
Floquet theory itself.

## 4. Finite resonance theorem after the 2026-09-07 audit

The currently proved finite result is

`m(3s,s)^2 >= 8 + 1/70` for every odd `s>=7`,

and the full threshold classification is

`m(3s,s) < sqrt(8)` iff `s` is even or `s in {3,5}`.

The `1/70` margin has exact finite-state/integer certificates and was
independently rerun on 2026-09-07.  Any older occurrence of `1/1038` in the
2026-09-06 literature note is superseded.

A targeted search on 2026-09-07 did not locate a theorem stated directly as
this all-signing `C_(3s)(1,s)` threshold classification.  This absence is only
a bounded-search observation and must not be upgraded to a priority claim.

## 5. Safe novelty wording

A conservative introduction can say:

> We study spectral-radius minimization over signatures of the fixed
> four-regular circulants `C_N(1,s)`.  Using standard switching and
> Floquet/block-Jacobi reductions, we construct explicit periodic signings for
> every jump with sharp `pi^2/s^2` Bloch gap, identify an algebraic phase slip
> for even jumps, and prove a finite arithmetic phase transition on the line
> `N=3s`: sub-`sqrt(8)` signings exist exactly for even `s` and for `s=3,5`,
> while every signing is uniformly super-`sqrt(8)` for odd `s>=7`.

Avoid `first`, `complete classification` without the qualifier `on N=3s`, or
claims that the magnetic/flux mechanism has no prior analogue.

# Literature boundary update for the all-`s` and finite-resonance results

Date: 2026-09-06.

This note updates the bounded comparison in
`../extension_20260905/LITERATURE_BOUNDARY_20260905.md` after the new sharp
all-jump Bloch theory and the `N=3s` all-signing obstruction.  It is a
positioning audit, not a priority certificate.

## 1. Closest signed-circulant paper

Vaibhav Suvagiya, **Signed circulants at the Ramanujan bound**,
arXiv:2607.18334 (July 2026), studies `C_n(1,2)` for even `n`.

Primary record:

- https://arxiv.org/abs/2607.18334

The abstract states, among other things:

- for even `n`, the quadrilateral-unbalanced parity system has exactly four
  switching classes;
- the alternating step-two family has an exact Fourier spectrum;
- the twisted classes have radius
  `2 sqrt(cos^2(pi/n)+cos^2(2pi/n)) < 2 sqrt(2)`;
- exhaustive enumeration for `n=8,10,12,14,16,18` supports a conjecture that
  this twisted value is the global minimum;
- for odd `n` the quadrilateral parity system is inconsistent.

### Boundary relative to the current project

This paper is the closest direct fixed-circulant comparison and must be cited
prominently.  The current work should not present the `s=2` twisted formula as
new.

The new results have a different scope:

1. the jump parameter is arbitrary `s>=2`, with parity-dependent mechanisms;
2. even large jumps require the period-`4s` antipodal defect family rather
   than the `s=2` parity word;
3. the all-`s` continuous Bloch gap has sharp asymptotic `pi^2/s^2`;
4. the even family has a nonzero optimizing phase with explicit avoided-
   crossing asymptotics;
5. the finite theorem `m(3s,s)^2>8` for odd `s>=7` is an all-signing
   obstruction on a different arithmetic line.

Suvagiya's odd-order incompatibility statement concerns the specific
quadrilateral parity system for `C_n(1,2)`; it should not be conflated with
our theorem that **every** signing fails on the resonance family
`C_(3s)(1,s)`.

## 2. General periodic block-Jacobi framework

Golinskii and Kutsenko, **On Direct Integral Expansion for Periodic
Block-Operator Jacobi Matrices and Applications**, SIGMA 15 (2019), 050,
arXiv:1809.07136, develop direct-integral models for periodic block Jacobi and
Jacobi-block-Jacobi operators, including band decompositions for periodic
difference operators.

Primary records:

- https://arxiv.org/abs/1809.07136
- https://doi.org/10.3842/SIGMA.2019.050

This is relevant prior framework for the Bloch/fiber viewpoint.  The final
paper should cite such block-Jacobi literature when introducing direct
integrals and band edges, rather than presenting Bloch decomposition itself
as a novelty.

What is not supplied by that general framework is the current problem's
specific signed-circulant content: the antipodal sign construction, exact
continuant determinant, quadratic inverse-trace bound, phase-slip constants,
or optimization over finite signatures.

Sahbani's **Spectral theory of a class of block Jacobi matrices and
applications**, J. Math. Anal. Appl. 438 (2016), 93--118,
arXiv:1504.05822, is another general block-Jacobi reference.  Its goals are
spectral type and Mourre analysis rather than fixed-graph signing
minimization.

## 3. General signed-graph spectral literature

The signed-graph literature contains broad extremal and classification
results that establish the mature context but do not by themselves identify
our fixed circulant minima.

Examples to retain in the audit include:

- Belardo, Cioaba, Koolen, Wang, **Open problems in the spectral theory of
  signed graphs** — explicitly discusses how spectra vary when the
  underlying graph is fixed and signatures are changed;
- McKee and Smyth, **Integer symmetric matrices having all their eigenvalues
  in the interval [-2,2]**, J. Algebra 317 (2007), 260--290 — important
  prior boundary for spectral-radius-two signed graphs;
- work on limit points and extremal spectral radii of signed graphs, which is
  broader than the fixed `C_N(1,s)` optimization problem.

The final paper should distinguish three questions:

1. spectral classification over broad classes of signed graphs;
2. periodic operator band theory for a fixed coefficient pattern;
3. minimization over signatures of one fixed underlying circulant.

The present project lies primarily in the intersection of 2 and 3.

## 4. New finite strip result and possible operator-theory overlap

The theorem

`m(3s,s)^2 >= 8+1/1038` for odd `s>=7`

can be rewritten as a width-three block-Jacobi strip with eight signed
triangle column states and a helical boundary matching.  This makes periodic
and finite block-operator literature relevant in method, but a bounded search
has not located a theorem directly giving this all-signing obstruction.

Before a priority claim, the literature audit should still be extended toward:

- magnetic/discrete Schrödinger operators on cyclic strips;
- flux-phase theorems and frustration on odd-width cylinders;
- transfer-matrix and forbidden-word descriptions of matrix-valued Jacobi
  operators;
- signed ladder/strip graphs and signed toral tessellations.

The current finite-state proof should therefore be described as a concrete
exact theorem for this circulant family, without claiming that its mechanism
has no equivalent formulation elsewhere.

## 5. Recommended novelty wording

Safe wording for a draft introduction:

> We study a fixed family of four-regular circulants under optimization of
> edge signatures.  Using standard switching and Bloch/block-Jacobi
> reductions, we derive explicit sign patterns whose band edge has a sharp
> quadratic gap for every jump parameter.  For even jumps the edge exhibits
> a nonzero phase slip with an explicit avoided-crossing expansion.  In the
> finite problem we identify an infinite arithmetic resonance family
> `C_(3s)(1,s)`, `s` odd, on which every signing stays uniformly above the
> threshold.

Avoid wording such as "first", "new in all periodic operators", or "complete
classification" until a broader literature comparison is finished.

## 6. Current disposition

- **Known framework:** switching, Fourier/Bloch decomposition, periodic block
  Jacobi direct integrals, continuants/Chebyshev methods.
- **Direct signed-circulant overlap:** `C_n(1,2)` parity/twisted family in
  Suvagiya (2026).
- **Current distinct mathematical package:** all-jump sharp `pi^2/s^2` Bloch
  gap, even avoided-crossing phase asymptotics, and the all-signing
  `N=3s` odd resonance obstruction.
- **Still unresolved:** full priority relative to magnetic strip and
  flux-phase formulations; general finite formula for `m(N,s)`.

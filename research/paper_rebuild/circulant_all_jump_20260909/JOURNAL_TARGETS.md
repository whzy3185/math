# Journal strategy for the rebuilt signed-circulant paper

Date: 2026-09-09

This ranking is based on mathematical fit, not on an asserted acceptance probability or a claimed current quartile.  Journal classifications change and must be checked against the authors' institutional list at submission time.

## 1. Primary target: Journal of Graph Theory

**Recommendation: first submission if the rebuilt manuscript passes the proof and novelty audits.**

Why it fits:

- the problem is intrinsically graph-theoretic: minimize adjacency spectral radius over signings of a fixed circulant support;
- the strongest results combine signed-graph switching, graph spectra, exact extremal statements, and structural classification;
- the current package is no longer one special matrix calculation: it has an all-jump theorem, a sharp asymptotic law, an exact finite minimum line, and a complete resonance threshold transition;
- the old period-8 manuscript was already written in a JGT-compatible style, so the exposition infrastructure can be reused without forcing the mathematics into a different vocabulary.

What must be fixed before submission:

- the new manuscript must not claim a complete formula for `m(N,s)`;
- the proof of the all-jump `pi^2/s^2` law and the even phase-slip theorem must be presented self-containedly;
- the finite exact computations in the `N=3s` theorem must follow a proved completeness reduction;
- the direct literature comparison with the July-2026 signed-circulant preprint and nearby periodic signed/magnetic graph work must be up to date.

## 2. Second target: European Journal of Combinatorics

**Recommendation: strong fallback, or a co-equal first choice if the final paper emphasizes Cayley/circulant structure and the interaction of combinatorics with spectral analysis.**

Why it fits:

- the paper studies a highly structured combinatorial family rather than general matrix theory;
- the parity-dependent constructions, flux coordinates, and resonance classification connect graph combinatorics to Fourier/spectral methods;
- recent EJC work includes signed-graph spectral questions and Cayley-type graphs, so the thematic neighborhood is credible.

A submission here should emphasize:

- switching-invariant cycle data;
- the combinatorial meaning of the parity split;
- the exact finite threshold transition;
- the period-8 rigidity theorem as a combinatorial classification, not merely a dispersion calculation.

## 3. Third target: Linear Algebra and its Applications

**Recommendation: robust fallback if graph-theory editors regard the family as too specialized, or if the final rewrite emphasizes exact matrix/Floquet/Chebyshev mechanisms.**

Why it fits:

- the technical core includes structured Hermitian matrices, spectral-radius inequalities, exact characteristic reductions, and asymptotic eigenvalue analysis;
- LAA regularly publishes graph spectral and signed-graph matrix papers.

Why it is not the first choice:

- the strongest story is about a graph-signing optimization problem and a finite combinatorial phase transition, not a new general matrix theorem;
- moving to LAA too early would risk weakening the graph-theoretic motivation that distinguishes the work from a special structured-matrix calculation.

## 4. Stretch target: Journal of Combinatorial Theory, Series B

**Recommendation: do not submit the current package there first.  Reconsider only after a further conceptual strengthening.**

JCTB explicitly sets very high standards and expects an important step on an open problem, a new proof technique, or another substantial advance in graph/hypergraph/matroid theory.

A realistic upgrade that could justify trying JCTB would be one of:

- an exact formula/classification for `m(N,s)` on a substantially larger two-parameter region;
- a general fixed-support signing theorem that explains the periodic flux construction beyond circulants;
- a new minimization principle comparable in generality to a discrete flux-phase theorem;
- a classification of minimal sub-eight periods/equality classes for all jumps with a uniform structural proof.

The fact that the current work disproves a recent conjecture is valuable, but the conjecture is specialized and recent; by itself that does not make JCTB the natural first venue.

## 5. Additional alternatives

### Electronic Journal of Combinatorics

A credible open-access option if the authors prefer a fully free journal and the manuscript remains strongly combinatorial.  It is especially suitable if the exact finite classification and structural rigidity are foregrounded.

### SIAM Journal on Discrete Mathematics

Possible only if the paper is reframed around a general discrete optimization/signing principle.  The present theorem package is within its broad combinatorics/graph-theory scope, but the exact circulant spectral analysis is a more immediate fit for JGT/EJC.

### Journal of Spectral Theory

Possible if the paper is substantially rewritten as a periodic-operator/spectral-asymptotics paper.  This would underuse the graph-theoretic counterexample and finite classification, so it is not currently recommended.

## 6. Proposed submission order

Current recommendation:

1. **Journal of Graph Theory**
2. **European Journal of Combinatorics**
3. **Linear Algebra and its Applications**
4. **Electronic Journal of Combinatorics**

Treat **JCTB** as a stretch venue only after another conceptual upgrade.

## 7. Editorial positioning sentence

A suitable cover-letter positioning, after all audits are complete, is:

> The paper begins with a counterexample to the recently proposed twisted-signing optimizer for `C_n(1,2)`, but its main contribution is a general periodic mechanism for signed step circulants: explicit sub-threshold phases for every jump, a sharp `pi^2/s^2` Bloch-gap law, and a complete finite threshold transition on the resonance line `N=3s`.

Do not claim that the paper solves the full minimum-signing problem on all `C_N(1,s)`.

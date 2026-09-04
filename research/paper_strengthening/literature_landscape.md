# Literature landscape for the period-eight paper

## Audit policy

This document separates three kinds of statement.

1. **Established background** is attached to a primary source or a standard reference.
2. **Connection to the present paper** is our mathematical interpretation, not a claim that the cited paper proves our result.
3. **Recent context** is not allowed to determine the problem, title, or theorem order.

The present problem is therefore formulated independently of the 2026 Suvagiya preprint.  That preprint is relevant only when the paper discusses the particular twisted benchmark and the conjecture it was used to support.

## A. Signed graphs, switching, and cycle invariants

### Long-term line

Harary's balance theory and Zaslavsky's systematic development make switching a structural operation rather than a change of notation.  If (D) is a diagonal matrix with diagonal entries in \(\{\pm1\}\), switching replaces a signed adjacency matrix (A_\sigma) by (D A_\sigma D).  Consequently the spectrum is switching invariant, while products of edge signs around cycles survive as gauge-invariant data.

For gain graphs, Reff's unit-gain formulation extends the same principle from signs to unit complex gains.  It supplies an established language for the quasi-periodic phases that occur after the Hamilton cycle is cut open.

### Connection to this paper

The variables 

\[
\tau_j=s_j s_{j+1} t_j
\]

are not ad hoc signs.  They are the signs of the local triangles in (C_n(1,2)), hence local cycle invariants.  The product of the step-one signs around the Hamilton cycle is a global holonomy 

\[
\alpha=\prod_j s_j\in\{\pm1\}.
\]

The clean formulation is therefore:

- switching fixes the local step-one couplings on the cut-open lift;
- the global cycle product reappears as the boundary condition (u_{j+n}=\alpha u_j);
- the signing is represented by the gauge coordinates ((\tau,\alpha)).

This language resolves the apparent contradiction between “all local step-one signs are (+1)” and an allowed negative Hamilton holonomy.

### Core sources

- F. Harary, *On the notion of balance of a signed graph*, Michigan Math. J. 2 (1953/54), 143–146.
- T. Zaslavsky, *Signed graphs*, Discrete Appl. Math. 4 (1982), 47–74, DOI [10.1016/0166-218X(82)90033-6](https://doi.org/10.1016/0166-218X(82)90033-6).
- N. Reff, *Spectral properties of complex unit gain graphs*, Linear Algebra Appl. 436 (2012), 3165–3176, DOI [10.1016/j.laa.2011.10.021](https://doi.org/10.1016/j.laa.2011.10.021).
- F. Belardo et al., *Signed graphs: a survey*, [arXiv:1907.04349](https://arxiv.org/abs/1907.04349).

## B. Spectral optimization over signings

### Long-term line

The two-lift literature asks whether signs can be chosen so that newly created eigenvalues remain controlled.  Bilu and Linial connected signings to lifts and discrepancy; Marcus, Spielman, and Srivastava proved the existence of signings with one-sided spectral control via interlacing polynomials.  These results are existence theorems over all signings of a fixed graph, usually benchmarked by the universal-cover radius.

The present problem is finer and different.  For a fixed finite graph (G), define

\[
m(G)=\min_{\sigma:E(G)\to\{\pm1\}}\rho(A_\sigma).
\]

We do not merely ask for a universal bound or an existence theorem.  We compare explicit switching classes on a fixed circulant family and seek exact finite spectral radii.

### Connection to this paper

The durable question is:

> How can local cycle fluxes lower the spectral radius of a signed adjacency matrix when the underlying graph is fixed?

The period-eight result gives a complete answer for one explicit mechanism, not a complete solution for (m(C_n(1,2))).  Its significance is the combination of:

1. an exact finite family;
2. a minimal-period explanation;
3. a structural separation between local flux geometry and a translation-compatible twisted benchmark.

This is the problem statement that survives even if the recent conjecture is deleted.

### Core sources

- Y. Bilu and N. Linial, *Lifts, discrepancy and nearly optimal spectral gap*, Combinatorica 26 (2006), 495–519, [arXiv:math/0312022](https://arxiv.org/abs/math/0312022), DOI [10.1007/s00493-006-0029-7](https://doi.org/10.1007/s00493-006-0029-7).
- A. Marcus, D. Spielman, and N. Srivastava, *Interlacing families I: bipartite Ramanujan graphs of all degrees*, Ann. of Math. 182 (2015), 307–325, DOI [10.4007/annals.2015.182.1.7](https://doi.org/10.4007/annals.2015.182.1.7).
- M. K. Kannan and S. Pragada, *Signed spectral Turán type theorems*, Linear Algebra Appl. 663 (2023), 62–79, DOI [10.1016/j.laa.2023.01.002](https://doi.org/10.1016/j.laa.2023.01.002).

## C. Circulants, periodic graphs, and finite Floquet decomposition

### Long-term line

Ordinary circulant matrices are diagonalized by the discrete Fourier transform.  A periodic signing need not preserve one-site translation, but it preserves translation by its cell length.  The correct replacement is a finite Bloch decomposition: an (8L\times8L) matrix becomes a direct sum of (8\times8) Hermitian fibers over phases satisfying the finite boundary condition.

For the present cell length eight,

\[
A_{8L,\alpha}\simeq\bigoplus_{z^L=\alpha}H(z).
\]

This is simultaneously a finite-dimensional matrix identity and the finite-quotient version of periodic Floquet theory.

### Connection to this paper

The direct sum is the bridge that was missing in the earlier narrative.  It explains the research path:

1. the fixed graph suggests Fourier analysis;
2. a nonconstant signing destroys one-site diagonalization;
3. a period-eight flux word restores cell translation;
4. holonomy quantizes the Bloch phase;
5. (z=1) belongs to every positive-holonomy finite grid, so the infinite spectral edge is attained exactly on every finite ring.

The last point upgrades a uniform estimate to the exact identity

\[
\rho(A_{8L,+})^2=4+\sqrt{10+2\sqrt5}.
\]

### Core sources

- E. Korotyaev and N. Saburova, *Schrödinger operators on periodic discrete graphs*, J. Math. Anal. Appl. 420 (2014), 576–611.
- E. Korotyaev and N. Saburova, *Trace formulas for magnetic Schrödinger operators on periodic graphs*, Linear Algebra Appl. 676 (2023), 395–440, [arXiv:2206.09663](https://arxiv.org/abs/2206.09663), DOI [10.1016/j.laa.2023.07.025](https://doi.org/10.1016/j.laa.2023.07.025).
- E. Korotyaev and N. Saburova, *Magnetic Schrödinger operators on periodic discrete graphs*, J. Funct. Anal. 272 (2017), 1625–1660, DOI [10.1016/j.jfa.2016.12.015](https://doi.org/10.1016/j.jfa.2016.12.015).

## D. Magnetic graph operators and flux coordinates

### Long-term line

Magnetic graph operators encode edge phases up to vertex gauge transformations.  Their spectral data depend on fluxes through cycles, not on a particular gauge.  On periodic graphs, magnetic flux and Bloch quasi-momentum interact but play different roles: the former belongs to the operator, the latter labels a representation of the translation group.

### Connection to this paper

Our notation should preserve this separation.

- (\tau) is the local triangle-flux word.
- (\alpha) is the finite Hamilton holonomy.
- (z) is the Bloch phase of the eight-site cell.
- (c=z+z^{-1}=2\cos\theta) is the real parameter in the characteristic polynomial.

This prevents three common errors: treating switching representatives as different operators, confusing holonomy with cell quasi-momentum, and passing from the infinite band edge to a finite quotient without checking the allowed phase grid.

### What is new here

The gauge language itself is standard.  The new content is that one special 8-periodic flux word combines with a chiral half-period symmetry to yield an exactly solvable edge and an infinite finite-ring consequence.

## E. Chiral symmetry and moment methods

### Chiral line

If a Hermitian matrix (H) anticommutes with an involution (J), its spectrum is symmetric about zero.  In a basis adapted to the (\pm1) eigenspaces of (J),

\[
H=\begin{pmatrix}0&B^*\\B&0\end{pmatrix},
\qquad
H^2=\begin{pmatrix}B^*B&0\\0&BB^*\end{pmatrix}.
\]

For the target period-eight word, a signed half-cell translation supplies (J_z).  The ordinary (8\times8) fiber problem therefore becomes a (4\times4) singular-value problem, and the remaining symmetry reduces its determinant to a (2\times2) calculation.  This produces

\[
P(y,c),\qquad y=\lambda^2,\qquad c=z+z^{-1}.
\]

The final strengthening round proves more than the period-eight instance.  For
a `2m`-periodic Hamilton-gauge word, the natural alternating-diagonal
half-cell translation yields a chiral involution exactly when
`tau_(i+m)=-tau_i`; equivalently, the local `Q` word is half-periodic with
negative half-cell flux.  This is a general classification inside that
specified monomial symmetry class, not a classification of arbitrary unitary
chiral involutions.

The closest literature found in the focused post-proof audit concerns three
adjacent but distinct traditions:

- spectral symmetry mechanisms for signed graph Laplacians: Atay and Hua,
  *On the symmetry of the Laplacian spectra of signed graphs*, Linear Algebra
  Appl. 495 (2016), 24–37, DOI
  [10.1016/j.laa.2016.01.027](https://doi.org/10.1016/j.laa.2016.01.027);
- chiral index theory for quantum walks: C. Bourne, *Index Theory of Chiral
  Unitaries and Split-Step Quantum Walks*, SIGMA 19 (2023), 053,
  [journal page](https://sigma-journal.com/2023/053/);
- half-period structure in periodically driven chiral systems: Cedzich et al.,
  *Chiral Floquet systems and quantum walks at half period*,
  [arXiv:2006.04634](https://arxiv.org/abs/2006.04634).

These sources justify the general vocabulary of spectral symmetry,
off-diagonal reduction, and half-period operators.  They should not be cited
as proving the present signed-coefficient criterion.  The focused search did
not locate the same equivalence between negative half-cell graph flux and the
specific monomial involution, but that search result is a novelty lead rather
than proof of bibliographic exhaustiveness.

### Moment line

For a periodic word of length (p), the phase-averaged moments count closed walks.  The identities already proved are

\[
M_1=4p,
\qquad
M_2=20p+16d,
\qquad
M_3=118p+168d+96a+48b.
\]

Here (d) is defect count and (a,b) record specified local clustering statistics.  If the squared Bloch edge is at most eight, then positivity of the spectral measure gives

\[
M_2\le 8M_1,\qquad M_3\le 8M_2,
\]

hence

\[
d\le\frac{3p}{4},
\qquad
40d+96a+48b\le42p.
\]

These are necessary obstructions, not a classification.  In the final paper they should appear after the exact period-eight theorem and be used to explain why low-edge phases require sparse, weakly clustered defects.

### Methodological relation

The two tools work at different scales:

| tool | input | output | role |
|---|---|---|---|
| chiral reduction | half-periodic negative-flux words; then the rigid period-eight word | general dimension-halving criterion; then exact fiber polynomial and edge | explains and solves the witness |
| trace moments | arbitrary periodic word | local necessary inequalities | explains structural scarcity |

This complementarity is the conceptual link that should organize the article.

## Position of the Suvagiya preprint

The paper does not need the preprint to define its graph, its optimization problem, its period-eight witness, or its exact theorem.  The preprint should therefore be absent from the title, abstract, and opening motivation.

Its legitimate role is one short related-work paragraph:

- state exactly which twisted signing and optimality conjecture appeared there;
- state that the present family disproves that conjecture for every (n=8L\), (L\ge4);
- do not use the preprint as evidence for the general importance of signed spectral minimization;
- do not inherit its terminology or unverified claims.

Source: [arXiv:2607.18334](https://arxiv.org/abs/2607.18334).

## Literature-derived research story

The defensible story is not “a recent conjecture was false.”  It is:

> Fixed-graph signing optimization is governed by switching-invariant cycle data.  On the circulant (C_n(1,2)), a period-eight local flux phase produces a hidden chiral symmetry.  Finite Floquet decomposition converts that symmetry into an exact spectral radius on every positive-holonomy ring, while short closed-walk moments show that such low-edge periodic phases are locally constrained.  The resulting phase is the first possible period whose squared Bloch edge falls below eight and it systematically beats the natural twisted benchmark.

That story is independent, mathematically ordered, and compatible with either a graph-theoretic (JGT) or a matrix-spectral (LAA) presentation.

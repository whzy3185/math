# Writing-style audit for the finite-global signed-circulant paper

This note records how the manuscript should be written after comparing the current theorem package with representative signed-graph spectral papers.  It is a writing/positioning document, not evidence for any mathematical theorem.

## 1. The correct high-level problem statement

The broad problem should be stated before any recent circulant motivation:

> Given a fixed simple graph `G`, how small can the spectral radius of a signed adjacency matrix of `G` be?

Belardo--Cioaba--Koolen--Wang, *Open problems in the spectral theory of signed graphs*, Art Discrete Appl. Math. 1 (2018), Problem 3.18, explicitly asks for signatures of a fixed graph minimizing the spectral radius.  Our quantity

\[
m(N,s)=\min_\sigma\rho(A_\sigma)
\]

is a structured family instance of exactly that problem.

This is much better than opening with a particular periodic signing or with the 2026 `C_n(1,2)` preprint.

## 2. Define spectral radius before index

Recent signed-graph spectral papers repeatedly warn that Perron--Frobenius does not identify the signed spectral radius with the largest eigenvalue.  On page 1 write

\[
\rho(A_\sigma)=\max\{ |\lambda|:\lambda\in\operatorname{spec}(A_\sigma)\}.
\]

When `B=A_sigma^2-4I` is introduced later, explicitly note

\[
\rho(A_\sigma)^2=4+\lambda_{\max}(B),
\]

so that all subsequent `lambda_max(B)` arguments are unambiguous.

Good models for this distinction include:

- D. Wang, W. Dong, Y. Hou, D. Li, *Discrete Math.* 346 (2023), 113358;
- G. Sun, F. Liu, K. Lan, *Linear Algebra Appl.* 652 (2022), 125--131;
- D. Wang, Y. Hou, D. Li, *Linear Algebra Appl.* 681 (2024), 47--65.

## 3. Put the main finite extremal quantity and theorem package on page 1

The manuscript should not spend several pages on switching preliminaries before stating results.  After one paragraph of motivation, define `C_N(1,s)` and `m(N,s)`, then state two theorem blocks.

### Theorem A: low-end hierarchy and exact `k=4` resonance

A strong compact form is

\[
\boxed{
\begin{aligned}
m(N,s)&=2 &&\Longleftrightarrow N=2s+2,\\
m(N,s)&=\sqrt5 &&\Longleftrightarrow (N,s)\in\{(5,2),(10,3)\},\\
m(N,s)&=\sqrt{4+\sqrt2} &&\Longleftrightarrow (N,s)=(8,2),
\end{aligned}}
\]

and all remaining parameter pairs satisfy

\[
m(N,s)>\sqrt{4+\sqrt2}.
\]

Then immediately add the exact infinite refinement

\[
\boxed{m(4s,s)^2=4+2\cos\frac{\pi}{2s}\qquad(s\ge2),}
\]

with the two minimizing labelled switching classes described in the theorem statement.

This is now a more structural first theorem than the original standalone `sqrt(5)` lower bound.

### Theorem B: the `sqrt(8)` threshold

State separately

\[
N\text{ even}\Longrightarrow
m(N,s)^2\le6+2\cos\frac{2\pi}{N}<8,
\]

and

\[
m(3s,s)<\sqrt8
\Longleftrightarrow
s\text{ is even or }s\in\{3,5\},
\]

with the quantitative odd obstruction

\[
m(3s,s)^2\ge8+\frac2{139}\qquad(s\ge7\text{ odd}).
\]

This separation keeps the low-end exact theory distinct from the Ramanujan-scale transition.

## 4. Elevate the parity-defect mechanism

The algebra

\[
B=A_\sigma^2-4I,
\qquad
B\equiv A_0^2\pmod2
\]

should appear as an organizing idea, not a technical observation buried in an equality proof.

In `F_2[Z_N]`,

\[
(x+x^{-1}+x^s+x^{-s})^2
=x^2+x^{-2}+x^{2s}+x^{-2s}.
\]

This gives the trichotomy

\[
\operatorname{supp}(B\bmod2)=
\begin{cases}
\varnothing,&N=2s+2,\\
\operatorname{Cay}(\mathbb Z_N,\{\pm2\}),&N=4s,\\
\operatorname{Cay}(\mathbb Z_N,\{\pm2,\pm2s\}),&\text{otherwise}.
\end{cases}
\]

This single lemma explains:

- why the trace lower bound can be flat exactly on `N=2s+2`;
- why `N=4s` becomes exactly solvable through two forced cycles;
- why generic parameters carry a four-direction integral defect;
- why the `sqrt(5)` equality problem reduces to negative clique support.

A referee should encounter this lemma before the separate case analyses.

## 5. How to discuss established two-eigenvalue theory

Do **not** write:

> We discover a family of 4-regular signed graphs with spectrum `{+-2}`.

That ambient phenomenon is established.  Relevant sources include:

- J. McKee and C. Smyth, *J. Algebra* 317 (2007), 260--290: cyclotomic signed graphs / spectrum in `[-2,2]`;
- Y. Hou, Z. Tang, D. Wang, *Discrete Math.* 342 (2019), 111615: connected signed graphs of maximum degree at most 4 with two adjacency eigenvalues;
- Z. Stanic, *Discrete Math. Lett.* 17 (2026), 70--74: toral tessellations and extensions with two symmetric eigenvalues.

Write instead:

> The equation `A_sigma^2=4I` belongs to the established theory of symmetric weighing matrices and two-eigenvalue signed graphs.  Our result determines exactly when this equality can occur inside the fixed two-step circulant family and determines the corresponding labelled switching classes.

This makes the novelty boundary both accurate and stronger.

## 6. Weighing-matrix language

Gregory's trace/average-degree result, as recorded in the Belardo--Cioaba--Koolen--Wang survey, says that a signed graph of average degree `d` has spectral radius at least `sqrt(d)`, with equality exactly when the underlying graph is `d`-regular and the signed adjacency matrix is a symmetric weighing matrix of weight `d`.

Therefore in the flat section use the established term once:

> Since our graphs are 4-regular, equality in the trace bound is precisely the symmetric weighing-matrix condition `A_sigma^2=4I`.

Then give the direct trace proof anyway because it is one line and keeps the paper self-contained.

## 7. Switching language must be exact

Use three distinct notions:

- **signature/signing**: a map `sigma:E(G)->{+-1}`;
- **switching equivalence**: conjugation by a diagonal `{+-1}` matrix;
- **switching isomorphism**: switching followed by a graph isomorphism / permutation.

This distinction matters at `(8,3)=K_{4,4}`:

- six labelled switching classes;
- one orbit after graph automorphisms.

Do not use “unique switching class” for that case.

## 8. Finite Fourier wording

For the `N=4s` exact theorem and the all-even upper theorem, use phrases such as

> finite anti-periodic shift,

> the `N` roots of `z^N=-1`,

> finite Fourier diagonalization of the signed shift.

Avoid the language

- Bloch Hamiltonian;
- Brillouin zone;
- quasi-momentum maximization over a continuum;
- band functions;
- phase-slip asymptotics.

The relevant calculation is finite and should look finite on the page.

## 9. How to position signed Cayley literature

Godsil--Zhang (arXiv:2405.14140) studies signed Cayley graphs in which the sign is itself part of the Cayley connection-set data, so the signed adjacency matrix is translation invariant.  That is a substantially smaller class than the signatures considered here.

The manuscript should explicitly say:

> The underlying graph `C_N(1,s)` is a Cayley graph, but the minimization defining `m(N,s)` ranges over all edge signatures and imposes no translation invariance on the signing.

This prevents a common scope misunderstanding.

## 10. How to discuss the 2026 `C_n(1,2)` preprint

V. Suvagiya, *Signed circulants at the Ramanujan bound*, arXiv:2607.18334 (2026), considers `C_n(1,2)` for even `n`, identifies a four-class quadrilateral-flux family, derives its spectra, and reports exhaustive global minimization for `n=8,10,12,14,16,18`, followed by a conjecture for all even `n`.

Use it as recent motivation only.  Safe wording:

> Recent work on `C_n(1,2)` shows that flux constraints can isolate spectrally effective switching classes and motivates asking for genuine all-signing finite extrema on broader step-circulant families.

Do not write that the present paper is a counterexample note, and do not infer a contradiction or resolution of its global conjecture unless the exact quantifiers are checked case by case.

Our new exact `N=4s` theorem intersects the `s=2` preprint only at `(N,s)=(8,2)`; its content is otherwise a different varying-step resonance family.

## 11. How to present the computer-assisted `N=3s` obstruction

The global theorem should be stated normally.  The computational content should be isolated as one finite lemma.

Recommended structure:

1. define the eight signed triangle states and the open nine-column strip;
2. state the complete finite state space;
3. state the exact acceptance inequality
   `139 w^T(M^2-8I)w >= 2 w^T w`;
4. give survivor counts as an audit checksum;
5. prove that every survivor obeys the six middle alternations;
6. after the lemma, return to a purely analytic sliding-window/seam argument.

Do not place Python code or floating eigenvalue output in the proof.  Say explicitly that floating eigensolvers are used only to propose integer witnesses; every accepted certificate is checked in exact integer arithmetic.

## 12. Abstract style

Avoid a catalogue of every lemma.  A strong abstract should have four moves:

1. fixed-graph optimization problem;
2. exact low-end hierarchy;
3. exact `N=4s` family and even-order construction;
4. `N=3s` threshold transition and method.

Draft wording:

> For the two-step circulant `C_N(1,s)` we minimize the spectral radius over all edge signatures.  Writing `m(N,s)` for this minimum, we first determine the bottom of the finite extremal problem.  The trace bound `m(N,s)>=2` is attained exactly when `N=2s+2`; the next value `sqrt(5)` occurs only at `(5,2)` and `(10,3)`; and the next possible value is `sqrt(4+sqrt(2))`, attained only at `(8,2)`.  The organizing object is the integral two-step defect `A_sigma^2-4I`, whose support modulo two is fixed by `(N,s)`.  This parity defect also yields the exact resonance formula `m(4s,s)^2=4+2 cos(pi/(2s))`.  At the larger threshold `sqrt(8)`, every even order admits an explicit finite signing below threshold, while on `N=3s` we prove the exact transition `m(3s,s)<sqrt(8)` iff `s` is even or `s in {3,5}`; for odd `s>=7` a local exact certificate and a signed-triangle rigidity argument give `m(3s,s)^2>=8+2/139`.

Do not put priority words such as “first” or “sharpest known” in the abstract before a final literature-priority audit.

## 13. Introduction architecture

Recommended introduction sequence:

1. fixed-underlying-graph signature optimization and `m(N,s)`;
2. signed spectral radius versus largest eigenvalue;
3. one paragraph on switching and why all signatures are allowed;
4. Theorem A (low-end hierarchy + exact `N=4s` family);
5. the parity-defect interpretation;
6. Theorem B (`sqrt(8)` threshold);
7. relation to weighing matrices/two-eigenvalue signed graphs;
8. relation to Bilu--Linial/MSS and recent signed circulants;
9. proof-method paragraph, including exact computer-assisted trust boundary;
10. paper organization.

This is closer to current JGT/EJC/LAA theorem-first practice than a long preliminaries-first introduction.

## 14. Current journal positioning

The strengthened theorem package now contains more than a single resonance line:

- exact flat line with switching rigidity;
- complete first and second low-end equality levels;
- exact infinite `N=4s` resonance family with minimizer rigidity;
- all-even-order sub-`sqrt(8)` theorem;
- complete `N=3s` threshold classification and quantitative odd obstruction.

This materially strengthens the case for **Journal of Graph Theory** or **European Journal of Combinatorics**.  **Linear Algebra and its Applications** remains a natural fit because the defect-matrix and exact spectral arguments are central.  **Electronic Journal of Combinatorics** is also realistic.

A JCTB-level assessment should still wait for either a genuinely broader odd-`k` structural theorem or a conceptual replacement of most of the nine-column finite certificate.

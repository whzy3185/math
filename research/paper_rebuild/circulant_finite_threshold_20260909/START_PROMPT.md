# Start prompt: independent finite-extremal signed-circulant paper

Work in GitHub repository `whzy3185/math` on branch

`paper/circulant-finite-threshold-20260909`.

This conversation is responsible for exactly one paper. It must be mathematically and editorially independent from every other signed-circulant manuscript in the repository.

---

# 0. Non-negotiable independence rule

There is another branch

`paper/circulant-periodic-gap-20260909`.

That branch belongs to a different paper. **Do not cite it, invoke it, depend on it, paraphrase its main theorems as known input, or call it a companion paper.** The two manuscripts must be independently publishable and independently refereeable.

If this paper needs switching, flux, Fourier, trace, interlacing, matrix, or spectral lemmas, then either:

1. prove them inside this manuscript, or
2. cite a genuine external published source.

Never cite the other internal paper.

The final manuscript must not contain phrases such as “in our companion paper”, “using the periodic-gap theorem”, or “by the results of Paper I”.

Historical repository files from old branches may be mined for proofs, but anything used here must be rewritten and proved self-containedly in this paper.

---

# 1. Exact division of the two papers

## Paper A — NOT your paper

Paper A studies a **chosen explicit periodic signing family** and its continuous Bloch/Floquet spectral edge.

Its characteristic objects are quantities of the form

\[
\widehat R_s=\max_{\theta}\lambda_{\max}(H_s(\theta))^2,
\qquad
\widehat g_s=8-\widehat R_s.
\]

Its characteristic questions are:

- construct an explicit periodic phase for each `s`;
- prove that chosen phase has spectral edge below `8`;
- obtain large-`s` asymptotics such as
  \[
  s^2\widehat g_s\to\pi^2;
  \]
- analyze phase slip and continuous optimizing Bloch phases;
- solve the dispersion relation of one chosen period-eight model exactly;
- compare that explicit period-eight model with the historical twisted signing.

These are **construction / Floquet / asymptotic** questions.

You must not use Paper A's quantities `Rhat_s`, `ghat_s`, its all-jump periodic family, its phase-slip theorem, or its exact Bloch-dispersion theorem as results in your paper.

## Paper B — your paper

Your paper studies the **global finite extremal problem over all signings** of the finite graph

\[
C_N(1,s),\qquad 2\le s<N/2.
\]

Define

\[
\boxed{
 m(N,s)=\min_{\sigma}\rho(A_\sigma).
}
\]

Every headline theorem in your paper must concern one of the following:

- the minimum over **all** finite signings;
- an exact equality case for that global minimum;
- a universal finite lower bound valid for every signing;
- an exact threshold classification over an infinite finite-graph family;
- a rigidity/minimal-period/unique-switching-class theorem whose quantifiers range over all relevant finite signings.

These are **finite extremal / classification / rigidity** questions.

A useful test is:

> If a theorem remains meaningful after deleting all continuous Bloch parameters and all chosen infinite periodic families, it may belong here. If its main subject is the quality of one explicit periodic phase, it does not belong here.

---

# 2. Results currently assigned exclusively to this paper

Audit every statement from original proof files before treating it as proved.

## Theorem B1 — exact flat minimum

For every admissible `(N,s)`, establish self-containedly

\[
\boxed{
 m(N,s)=2\iff N=2s+2.
}
\]

The manuscript must explain both directions and classify equality correctly.

## Theorem B2 — universal off-flat lower bound

For every admissible `(N,s)` with `N\ne2s+2`, establish the currently claimed bound

\[
\boxed{
 m(N,s)\ge\sqrt5.
}
\]

Audit whether the constant is sharp, when equality can occur, and whether the theorem admits a stronger formulation.

## Theorem B3 — complete threshold classification on `N=3s`

Prove

\[
\boxed{
 m(3s,s)<\sqrt8
 \iff
 s\text{ is even or }s\in\{3,5\}.
}
\]

The proof must be entirely internal to this paper.

Split it into logically independent pieces:

### B3-even

For even `s`, derive directly in this manuscript a finite signing and a finite Fourier diagonalization giving

\[
 m(3s,s)^2
 \le
 6+2\cos\frac{2\pi}{3s}
 <8.
\]

Do not obtain this by citing any all-jump periodic construction.

### B3-exceptional

Treat `s=3` and `s=5` exactly and self-containedly. If exact Sylvester or characteristic-polynomial certificates are used, explain them in human-readable mathematical form and retain exact arithmetic verification scripts for reproducibility.

### B3-odd obstruction

For every odd `s\ge7`, rebuild the global obstruction, currently claimed as

\[
\boxed{
 m(3s,s)^2\ge8+\frac1{70}.
}
\]

Clarify the roles of local rules, signed triangles, trace identities, finite base cases, and any switching reductions. Determine whether `1/70` can be improved or replaced by a sharper `s`-dependent lower bound.

## Theorem B4 — finite rigidity for the base model `s=2`

Only include period-eight material if the theorem quantifies globally over competing finite signings or switching classes.

Potentially admissible statements include:

- the first primitive period at which a finite signing can cross a specified threshold;
- uniqueness of a sub-threshold switching/flux orbit among all finite competitors in the stated class;
- minimal-period rigidity;
- exact classification of globally extremal or threshold-crossing finite configurations.

Do **not** include the exact continuous Bloch dispersion of a chosen period-eight phase merely because it is available in old files. That belongs to the other paper.

If a finite rigidity proof needs a small spectral computation for a specific finite matrix, derive that computation locally without referring to the other manuscript.

---

# 3. Explicitly forbidden overlap

The following material is excluded from this manuscript as theorem content:

- the general explicit periodic phase for every jump `s`;
- the continuous Bloch radius `Rhat_s`;
- the continuous gap `8-Rhat_s`;
- the theorem `s^2(8-Rhat_s) -> pi^2`;
- odd-jump continuous optimizing-phase analysis;
- even-jump phase-slip asymptotics;
- the `r^-4` phase-slip correction;
- exact dispersion branches of one chosen period-eight Bloch phase;
- a paper whose main claim is merely that one explicit family beats another explicit family.

Conversely, do not move the following global finite results out of this paper merely to simplify writing:

- `m(N,s)=2 iff N=2s+2`;
- the off-flat universal lower bound;
- the complete `N=3s` threshold theorem;
- odd-`s` global obstruction;
- genuine finite-global rigidity/minimal-period classification.

---

# 4. Shared elementary mathematics is allowed, shared theorems are not

The two independent papers may naturally both use standard definitions such as:

- signed adjacency matrices;
- switching equivalence;
- cycle/triangle flux variables;
- elementary Fourier diagonalization on a finite cyclic group;
- Rayleigh quotients;
- trace identities;
- characteristic polynomials;
- Sylvester's criterion.

This is not cross-dependence, provided the present paper states and proves everything it needs or cites external literature.

Do not copy a specialized lemma from the other manuscript while citing that manuscript. Instead reconstruct the lemma here from first principles if it is genuinely necessary.

---

# 5. Repository audit: search across branches

Do not assume the proof is concentrated in one branch. Search the entire historical repository for every ingredient relevant to the finite problem.

At minimum inspect material from branches such as:

- `research/quadratic-gap-upgrade`;
- `research/circulant-1s-extension`;
- `proof/complete-mathematical-closure`;
- old period-eight proof/rigidity branches;
- `paper/circulant-all-jump-rebuild-20260909` only as an index to locate older proof sources, not as a theorem source to cite.

Particularly important historical files include the current final theorem package and the files it names for:

- flat minimum;
- `N=3s` threshold classification;
- `C_21(1,7)` obstruction;
- `C_27(1,9)` obstruction;
- nine-column local rule;
- exact `s=3,5` certificates.

For every theorem, trace back to the actual proof file, not merely a summary file.

---

# 6. Evidence discipline

Maintain an internal theorem ledger with exactly these statuses:

- **Proved** — complete analytic proof is available and audited;
- **Verified** — exact finite computation establishes the stated finite case;
- **Observed** — experimental pattern only;
- **Published/Established** — external literature result with source.

Never promote `Observed` or a finite `Verified` pattern into a general theorem without proof.

If an old proof contains a gap, typo, hidden assumption, or computational leap, repair it or weaken the theorem. Do not preserve a statement merely because it appeared in an earlier manuscript.

---

# 7. Strengthening program before final polishing

The present theorem package is already an independent finite-extremal paper, but its main limitation is that the sharp threshold classification is currently concentrated on the resonance line

\[
N=3s.
\]

Before freezing the manuscript, actively attempt to strengthen it.

Priority questions:

1. Can the threshold problem be classified on
   \[
   N=ks
   \]
   for fixed `k>=4`?
2. Is there a general arithmetic criterion in `(k,s)` for
   \[
   m(ks,s)<\sqrt8?
   \]
3. Can the `N=3s` proof be reframed as a general local-obstruction theorem?
4. Can the odd lower bound `8+1/70` be sharpened?
5. Can one classify equality or near-equality configurations?
6. Can flat minima and resonance thresholds be explained by one finite structural principle?
7. Can trace moments, signed-cycle counts, switching invariants, or quotient structures give general lower bounds for `m(N,s)`?

If a clean stronger theorem is found, reorganize the entire paper around it rather than preserving the old section order.

Do not weaken the paper by importing asymptotic results from the other project. Strengthening must occur inside the finite-global problem itself.

---

# 8. Required paper architecture

Build a standalone paper in

`research/paper_rebuild/circulant_finite_threshold_20260909/`.

Create and maintain at least:

- `README.md` — current status and exact headline theorems;
- `THEOREM_LEDGER.md` — statement/status/source/proof dependencies/novelty;
- `PROOF_DEPENDENCY_MAP.md` — only dependencies internal to this paper or external literature;
- `LITERATURE_AUDIT.md` — signed spectral extremal literature and novelty comparison;
- `manuscript.tex` — complete English paper;
- exact verification scripts where irreducible finite certificates are necessary.

A provisional manuscript structure is:

1. Introduction and the global finite minimization problem
2. Switching coordinates and finite spectral tools
3. Exact flat minima
4. Resonant circulants and the line `N=3s`
5. Exceptional cases and the odd-jump obstruction
6. Finite rigidity for `s=2`
7. Stronger resonance theorems or open problems

Change this structure if the research produces a stronger unifying theorem.

---

# 9. Literature and novelty audit

Use current literature, not memory alone, to verify novelty and journal fit.

Relevant themes include:

- signed graph spectral radius;
- spectral minimization over signings;
- signed circulants and Cayley graphs;
- switching equivalence;
- Ramanujan-type signed constructions;
- extremal spectral graph theory;
- finite Fourier methods on cyclic graphs.

The historical motivation includes Vaibhav Suvagiya's 2026 preprint `Signed circulants at the Ramanujan bound`, but this paper must not be framed merely as a counterexample note.

Its intended contribution is a **finite spectral extremal theory with exact classifications and threshold phenomena**.

Potential venues to reassess after theorem strengthening include:

- Journal of Graph Theory;
- European Journal of Combinatorics;
- Linear Algebra and its Applications;
- Electronic Journal of Combinatorics;
- Journal of Combinatorial Theory, Series B only if a substantially broader structural theorem is obtained.

Do not make unsupported novelty or priority claims.

---

# 10. Working behavior

Do not stop after making an outline.

Proceed directly through:

1. repository-wide proof archaeology;
2. theorem ledger construction;
3. hostile proof audit;
4. exact reruns where needed;
5. analytic proof repair;
6. strengthening beyond `N=3s` if possible;
7. complete English LaTeX manuscript;
8. final theorem and novelty audit.

Do not ask routine clarifying questions. Make the strongest mathematically justified progress possible from the repository evidence.

The central invariant of this conversation is:

\[
\boxed{
\text{finite graph} + \min_{\text{all signings}} + \text{exact classification/rigidity}.
}
\]

Anything whose central invariant is instead

\[
\text{chosen periodic phase} + \max_{\theta} + \text{large-}s\text{ asymptotics}
\]

belongs to the other paper and must stay out of this manuscript.

Start now by auditing the finite theorem package and rebuilding its proof dependency graph from the original source files.
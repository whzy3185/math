# Start prompt for the independent finite-extremal paper

Work in GitHub repository `whzy3185/math` on branch `paper/circulant-finite-threshold-20260909`.

This is an independent paper on the global finite minimization problem for signed step circulants

\[
m(N,s)=\min_\sigma \rho(A_\sigma),\qquad 2\le s<N/2.
\]

## Absolute independence rule

There is another project branch `paper/circulant-periodic-gap-20260909`, but **do not cite it, invoke it, depend on it, or treat any of its results as a black box**. The two papers must be publishable independently. If a switching, flux, Fourier, or spectral lemma is needed here, prove it inside this paper (or cite an external standard source). Do not write "companion paper" anywhere in the manuscript.

Read `research/paper_rebuild/circulant_all_jump_20260909/PAPER_SPLIT_BOUNDARY.md` first.

## Results currently assigned to this paper

Audit and rebuild complete proofs for:

1. Exact flat minimum
   \[
   m(N,s)=2\iff N=2s+2.
   \]
2. Off-flat lower bound
   \[
   m(N,s)\ge\sqrt5.
   \]
3. Complete resonance-line threshold theorem
   \[
   m(3s,s)<\sqrt8\iff s\text{ is even or }s\in\{3,5\}.
   \]
4. For even `s`, give a direct self-contained Fourier construction proving
   \[
   m(3s,s)^2\le 6+2\cos\frac{2\pi}{3s}<8.
   \]
5. Give exact self-contained treatment of the exceptional cases `s=3,5`.
6. Rebuild the odd obstruction for every odd `s>=7`, currently
   \[
   m(3s,s)^2\ge 8+\frac1{70}.
   \]
7. Include `s=2` results only when they are genuinely finite-global rigidity/minimal-period/unique-orbit statements quantifying over competing signings or switching classes.

## Forbidden material

Do not use as results of this paper:

- the all-jump continuous Bloch periodic family;
- `s^2(8-Rhat_s)->pi^2`;
- even phase-slip asymptotics;
- the exact dispersion theory of a chosen period-eight Bloch phase, except for any elementary finite fact rederived locally because it is strictly necessary for a global rigidity proof.

## Repository audit

Search the whole repository across historical branches, not just main. Important sources include `research/quadratic-gap-upgrade`, `research/circulant-1s-extension`, old period-eight proof branches, and `proof/complete-mathematical-closure`.

Build in this branch:

- `THEOREM_LEDGER.md`
- `PROOF_DEPENDENCY_MAP.md`
- `LITERATURE_AUDIT.md`
- `manuscript.tex`
- exact verification scripts only where necessary.

Every result must be labeled internally as Proved / Verified / Observed / Published-Established. Do not convert finite computation into a general theorem without proof.

## Strengthening priority

Before polishing, try to raise the theorem beyond the single line `N=3s`. Investigate resonance families such as `N=ks`, congruence/parity phenomena, general local-obstruction principles, and sharper odd lower bounds. If a clean general resonance theorem is found, reorganize the paper around it.

The manuscript must remain fully self-contained relative to the other signed-circulant paper throughout.

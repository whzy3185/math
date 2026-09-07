# Final theorem package: sharp all-jump Bloch gaps and a finite arithmetic phase transition

Date: 2026-09-07.
Branch: `research/quadratic-gap-upgrade`.

This note is the current endpoint of the `C_N(1,s)` workstream.  It assembles
only results whose stated evidence is already present in the repository.  It
does **not** claim a closed formula for `m(N,s)` for arbitrary pairs.

Throughout, for `2<=s<N/2`, let

\[
 m(N,s)=\min_\sigma\rho(A_\sigma)
\]

be the minimum signed adjacency spectral radius of the simple four-regular
circulant `C_N(1,s)`.

For the explicit parity-dependent periodic family, let `Rhat_s` be the
continuous squared Bloch spectral radius and put

\[
 \widehat g_s=8-\widehat R_s.
\]

## Final Theorem

### A. Sharp periodic theorem for every jump

For every integer `s>=2` there is an explicit periodic signing of the
step-`(1,s)` operator such that

\[
 \boxed{\widehat R_s<8.}
 \tag{A1}
\]

It may be chosen as

- the period-two alternating-flux word when `s` is odd;
- the primitive period-`4s` antipodal defect word when `s` is even.

Uniformly in `s`,

\[
 \boxed{
 \frac1{6s(s+2)}
 \le \widehat g_s
 \le 4\sin^2\frac\pi{s+2}.}
 \tag{A2}
\]

Most importantly,

\[
 \boxed{
 s^2\widehat g_s\longrightarrow\pi^2
 \qquad(s\to\infty)}.
 \tag{A3}
\]

Thus the sharp leading gap is parity-free even though the constructions and
proof mechanisms are parity-dependent.

For odd `s`, the maximizing phase is the unique solution described by
`ODD_JUMP_SHARP_GAP.md`.  For even `s=2r`, phase zero is not always optimal,
but the global phase slip has the proved boundary-layer asymptotics

\[
 \boxed{
 r^2\phi_r\longrightarrow\frac\pi{4\sqrt2},
 \qquad
 r^4(e_r-g_{2r})\longrightarrow\frac{\pi^2}{32}.}
 \tag{A4}
\]

Here `e_r` is the phase-zero endpoint gap and `phi_r` is a global optimizing
square-root Bloch phase.  In particular, the nonzero phase changes the gap at
order `r^-4`, not at the leading `r^-2` scale.

### B. Exact flat minimum on every finite circulant

For every admissible pair `(N,s)`,

\[
 \boxed{m(N,s)=2\iff N=2s+2.}
 \tag{B1}
\]

If `N!=2s+2`, every signing satisfies

\[
 \boxed{m(N,s)\ge\sqrt5.}
 \tag{B2}
\]

This is the exact flat-minimum theorem from
`../extension_20260905/FLAT_MINIMUM_AND_CHIRAL_CRITERION.md`.

### C. Complete `sqrt(8)` threshold classification on the resonance line

For every integer `s>=2`,

\[
 \boxed{
 m(3s,s)<\sqrt8
 \iff
 s\text{ is even, or }s\in\{3,5\}.}
 \tag{C1}
\]

More precisely:

1. `s=2`: since `3s=2s+2`, the flat theorem gives
   \[
   \boxed{m(6,2)=2.}
   \tag{C2}
   \]
2. even `s>=4`: the antiperiodic alternating signing gives
   \[
   m(3s,s)^2
   \le 6+2\cos\frac{2\pi}{3s}
   =8-4\sin^2\frac\pi{3s}<8,
   \tag{C3}
   \]
   while the flat theorem gives `m(3s,s)>=sqrt(5)`;
3. `s=3,5`: the explicit exact Sylvester certificates in
   `N3S_THRESHOLD_CLASSIFICATION.md` give
   \[
   \sqrt5\le m(9,3)<\sqrt8,
   \qquad
   \sqrt5\le m(15,5)<\sqrt8;
   \tag{C4}
   \]
4. every odd `s>=7`: every signing obeys the uniform obstruction
   \[
   \boxed{
   m(3s,s)^2\ge8+\frac1{70}.}
   \tag{C5}
   \]

Consequently the entire resonance line `N=3s` has the following rigorously
classified threshold phase diagram:

\[
\begin{array}{c|c}
 s & \text{proved location of }m(3s,s)\\ \hline
 2 & =2\\
 3,5 & [\sqrt5,\sqrt8)\\
 \text{even }s\ge4 & [\sqrt5,\sqrt8)\\
 \text{odd }s\ge7 & [\sqrt{8+1/70},\infty)
\end{array}
\tag{C6}
\]

The transition at odd `s=7` is genuine: the two preceding odd cases are
strictly sub-`sqrt(8)`, and every later odd case is uniformly super-`sqrt(8)`.

## Proof assembly

### Part A

- odd jumps: `ODD_JUMP_SHARP_GAP.md`;
- even sub-eight construction: `../extension_20260905/EVEN_JUMP_THEOREM_AND_PROOF.md`;
- even quadratic envelope: `QUADRATIC_GAP_THEOREM.md`;
- even global leading constant: `EVEN_GLOBAL_PI2_THEOREM.md` and
  `GLOBAL_PI2_LOCALIZATION_LEMMA.md`;
- even second-order phase slip: `EVEN_SECOND_ORDER_PHASE_SLIP_THEOREM.md` and
  `SECOND_ORDER_LOCAL_IMPLICIT_LEMMA.md`;
- parity-free assembly: `ALL_S_UNIFIED_THEOREM.md`.

### Part B

`../extension_20260905/FLAT_MINIMUM_AND_CHIRAL_CRITERION.md` proves the exact
`m=2` classification and the universal `sqrt(5)` lower bound off the flat
line.

### Part C

- even `s`: exact Fourier diagonalization of the antiperiodic alternating
  family;
- `s=3,5`: `verify_n3s_short_threshold.py` gives exact positive-definiteness
  certificates for `8I-A^2`;
- odd `s>=7`: `N3S_GLOBAL_OBSTRUCTION.md`;
- the latter uses exact base cases `C21_S7_GLOBAL_OBSTRUCTION.md` and
  `C27_S9_GLOBAL_OBSTRUCTION.md`, the exact nine-column local rule in
  `verify_triangle_strip_local_rule.py`, and a signed-triangle trace
  contradiction.

## Reproducibility audit completed on 2026-09-07

The following exact finite components were independently rerun in the current
analysis environment:

1. nine-column local-rule survivor counts
   \[
   8,56,152,440,488,1016,656,1064,128,
   \]
   with all `128` final survivors satisfying the forced middle alternation;
2. `C_27(1,9)` prefix counts ending in `1064` length-eight survivors and all
   `17,024` final cyclic checks certified at margin `1/70`;
3. `C_21(1,7)`: all `49,940` admissible `Q` necklaces and all `199,760`
   Hamilton-gauge representatives certified, with weakest generated exact
   Rayleigh excess `36/262=18/131`;
4. the `s=3,5` short positive cases, with all Sylvester minors positive.

The finite scripts may use floating eigenvectors only to propose integer
witnesses.  Acceptance, pruning, and positive-definiteness claims are decided
by exact integer/rational arithmetic.

## What is final and what remains open

The following questions are now closed within their stated scope:

- sharp `pi^2/s^2` Bloch gap for an explicit family for every jump `s`;
- leading and second-order even phase-slip constants;
- exact finite flat threshold `m=2`;
- complete sub-`sqrt(8)` feasibility classification on `N=3s`.

The following larger problem is **not** claimed solved:

\[
 \text{determine }m(N,s)\text{ exactly for every admissible }(N,s).
\]

In particular, other chord-cycle lengths `N/gcd(N,s)` and the even-jump
finite-order compatibility problem remain separate research directions.

The higher `r^-3/r^-5` phase-slip refinement in
`EVEN_THIRD_ORDER_PHASE_SLIP_REFINEMENT.md` is useful but is not needed for
this final theorem package; it should remain outside the headline theorem
until its uniform remainder bookkeeping receives the same hostile audit as
the second-order result.

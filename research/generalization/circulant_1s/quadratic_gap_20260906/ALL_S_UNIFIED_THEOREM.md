# Unified all-`s` sharp quadratic-gap theorem for `C_N(1,s)`

Date: 2026-09-06.

This note joins the even-jump antipodal construction with the odd-jump
alternating-flux construction.  It is a theorem about an explicit
parity-dependent family; it does not assert global minimization over all
signings.

## 1. The parity-dependent family

For every integer `s>=2`, define a periodic Hamilton-gauge chord word as
follows.

- If `s` is even, use the period-`4s` antipodal word from
  `../extension_20260905/EVEN_JUMP_THEOREM_AND_PROOF.md`.
- If `s` is odd, use the period-two alternating word
  `tau_i=(-1)^i`.

Let `Rhat_s` be the squared continuous Bloch spectral radius of the
corresponding periodic operator, and put

\[
 \widehat g_s=8-\widehat R_s.
\]

## 2. Uniform all-jump theorem

**Theorem A (all jumps).** For every integer `s>=2`,

\[
 \boxed{\widehat R_s<8.}
\tag{1}
\]

Moreover

\[
 \boxed{
 \frac1{6s(s+2)}
 \le \widehat g_s
 \le 4\sin^2\frac\pi{s+2}.}
\tag{2}
\]

Consequently

\[
 \boxed{8-\widehat R_s=\Theta(s^{-2})}
\qquad(s\to\infty)
\tag{3}
\]

without any parity restriction on `s`.

For even `s`, (1)--(2) are the result of `QUADRATIC_GAP_THEOREM.md`.
For odd `s`, `ODD_JUMP_SHARP_GAP.md` proves the stronger estimates

\[
 \widehat g_s\ge\frac4{1+s^2},
 \qquad
 \widehat g_s\le4\sin^2\frac\pi{2s},
\]

which imply (2).

## 3. Sharp parity-free asymptotic

The leading constant is now known on both parity subsequences.

For odd jumps, `ODD_JUMP_SHARP_GAP.md` proves

\[
 s^2\widehat g_s\to\pi^2.
\tag{4}
\]

For even jumps, `EVEN_GLOBAL_PI2_THEOREM.md` proves the same limit despite
the exact phase slip:

\[
 s^2\widehat g_s\to\pi^2.
\tag{5}
\]

Therefore

\[
 \boxed{
 s^2(8-\widehat R_s)\longrightarrow\pi^2
 \qquad(s\to\infty)}
\tag{6}
\]

through **all integer jumps**.

This is the sharp all-`s` theorem for the explicit parity-dependent family.

## 4. What the even phase slip does

For even `s=2r`, the maximizing phase is not always phase zero;
`PHASE_SLIP_COUNTEREXAMPLE.md` gives an exact `s=10` Sturm certificate.
Nevertheless `EVEN_GLOBAL_PI2_THEOREM.md` proves that if `h_r` is any global
maximizing square-root phase parameter chosen in `[0,2]`, then

\[
 r^2(2-h_r)\to0.
\tag{7}
\]

Hence the phase drift cannot alter the leading `pi^2/s^2` gap.  The stronger
second-order numerical prediction

\[
 r^2\phi_r\to\frac\pi{4\sqrt2},
 \qquad
 r^4(e_r-g_{2r})\to\frac{\pi^2}{32}
\]

remains a separate conjectural refinement.

## 5. Finite `C_N(1,s)` consequence

The construction gives explicit finite signings as follows.

- `s` odd: for every admissible even `N` with `2<=s<N/2`, the period-two
  signing exists and both holonomy sectors satisfy
  `rho^2<=Rhat_s<8`.
- `s` even: for every `N=4sL`, the period-`4s` antipodal signing exists and
  both holonomy sectors satisfy `rho^2<=Rhat_s<8`.

Hence every jump `s>=2` has infinitely many finite circulants `C_N(1,s)`
with an explicit signing of spectral radius below `sqrt(8)`.  For odd jumps
the result covers every admissible even order.

The order-compatibility problem is genuinely separate.  In particular,
`ODD_ORDER_ONE_DEFECT_OBSTRUCTION.md` proves exactly that the most naive
odd-order repair—one concentrated alternating defect—fails at
`(N,s)=(21,7)` in both holonomy/anchor sectors.

## 6. Research significance

The parity mechanisms are different but meet at the same sharp scale.

- Odd jumps are exactly tractable: the alternating-flux dispersion has a
  unique interior optimizer satisfying a Chebyshev equation and
  `pi^2/s^2` gap.
- Even jumps require an antipodal defect construction, a reduced continuant
  determinant, a quadratic inverse-trace estimate, and a phase-localization
  argument; the global phase can slip, but only below leading order.

Thus the natural manuscript story is now a **parity-resolved all-jump sharp
theory**, not merely an even-jump extension.

## 7. Remaining scope boundary

The sharp jump-parameter problem is closed for this explicit family, but the
following are still open:

1. global minimization over all signings, i.e. a closed formula for
   `m(N,s)`;
2. finite-order coverage for odd `N`;
3. finite-order coverage for even `s` when `4s` does not divide `N`;
4. the second-order even phase-slip constants;
5. full Lean formalization of the all-`s` analytic proof;
6. publication-priority comparison with periodic/magnetic operator
   literature beyond the currently audited signed-circulant sources.

These should not be conflated with the now-proved sharp all-`s` Bloch-gap
asymptotic (6).

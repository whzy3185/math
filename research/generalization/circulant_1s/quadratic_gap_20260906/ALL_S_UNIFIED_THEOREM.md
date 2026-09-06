# Unified all-`s` sub-eight theorem for `C_N(1,s)`

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

## 2. Main theorem

**Theorem (all jumps).** For every integer `s>=2`,

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

### Proof

For even `s`, (1)--(2) are exactly the quadratic-gap theorem already proved
in `QUADRATIC_GAP_THEOREM.md`.

For odd `s`, `ODD_JUMP_SHARP_GAP.md` proves

\[
 \widehat g_s=g_s^{\rm odd}\ge\frac4{1+s^2}
\]

and

\[
 \widehat g_s\le4\sin^2\frac\pi{2s}.
\]

The lower estimate in (2) follows from

\[
 \frac4{1+s^2}\ge\frac1{6s(s+2)},
\]

and, for odd `s>=3`,

\[
 \frac\pi{2s}<\frac\pi{s+2}<\frac\pi2,
\]

so monotonicity of sine gives the upper estimate in (2).  Strict positivity
of the gap proves (1), and (2) proves (3).

## 3. Odd subsequence has the sharp constant

The odd-jump theorem is substantially sharper than the unified envelope:

\[
 \boxed{
 s^2\widehat g_s\to\pi^2
 \quad(s\to\infty,\ s\text{ odd}).}
\tag{4}
\]

For the even subsequence, the phase-zero edge also has constant `pi^2`, but
the global phase-slip problem remains open.  The current rigorous even
bracket is

\[
 \frac16\le
 \liminf_{s\to\infty,\ s\ even}s^2\widehat g_s
 \le
 \limsup_{s\to\infty,\ s\ even}s^2\widehat g_s
 \le\pi^2.
\tag{5}
\]

Thus the remaining obstacle to a parity-free sharp limit

\[
 s^2\widehat g_s\to\pi^2
\]

is entirely on the even subsequence.

## 4. Finite `C_N(1,s)` consequence

The construction gives explicit finite signings as follows.

- `s` odd: for every admissible even `N` with `2<=s<N/2`, the period-two
  signing exists and both holonomy sectors satisfy
  `rho^2<=Rhat_s<8`.
- `s` even: for every `N=4sL`, the period-`4s` antipodal signing exists and
  both holonomy sectors satisfy `rho^2<=Rhat_s<8`.

Hence every jump `s>=2` has infinitely many finite circulants `C_N(1,s)`
with an explicit signing of spectral radius below `sqrt(8)`.  For odd jumps
the result covers every admissible even order rather than only a periodic
subsequence.

## 5. Research significance

The earlier project state had a parity split:

- even jumps required a new defect construction to move the Bloch edge
  below `8`;
- odd jumps had a qualitative interior maximum below `8`, but no uniform
  large-`s` gap theorem.

The two new quantitative results now produce a single all-jump statement at
quadratic scale.  The natural manuscript organization is therefore no
longer "even-jump extension" but "parity-resolved all-jump construction":
odd jumps are the exactly tractable reference model and even jumps are the
defect/phase-slip model.

## 6. Remaining scope boundary

This theorem does not yet cover every order `N`: the odd alternating word
requires even `N`, while the current even antipodal construction is stated
for `N` divisible by `4s`.  Removing these order-compatibility restrictions
is a separate finite-ring problem and should not be conflated with the
all-`s` jump-parameter theorem above.

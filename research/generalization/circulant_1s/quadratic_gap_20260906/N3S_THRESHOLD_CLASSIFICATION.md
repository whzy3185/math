# Complete sub-`sqrt(8)` threshold classification on the resonance line `N=3s`

Date: 2026-09-07.

Let

\[
 m(N,s)=\min_\sigma \rho(A_\sigma)
\]

be the minimum spectral radius over all edge signings of the simple
four-regular circulant `C_N(1,s)`, with `2<=s<N/2`.

This note completes the threshold question on the full resonance line
`N=3s`.

## Theorem R — exact threshold classification on `N=3s`

For every integer `s>=2`,

\[
 \boxed{
 m(3s,s)<\sqrt8
 \quad\Longleftrightarrow\quad
 s\text{ is even, or }s\in\{3,5\}.}
 \tag{R1}
\]

Moreover, if `s>=7` is odd, then the stronger uniform obstruction holds:

\[
 \boxed{
 m(3s,s)^2\ge 8+\frac1{70}.}
 \tag{R2}
\]

Thus the odd resonance line undergoes a genuine threshold transition:
`C_9(1,3)` and `C_15(1,5)` admit sub-`sqrt(8)` signings, whereas every
`C_(3s)(1,s)` with odd `s>=7` is uniformly separated above `sqrt(8)` for
**all** signings.

## 1. Even `s`: explicit antiperiodic alternating signing

Let `s` be even and set `N=3s`, which is even.  Use the Hamilton-gauge word

\[
 \tau_i=(-1)^i
\]

with negative Hamilton holonomy `alpha=-1`.  The exact Fourier formula from
Task 60 gives

\[
 \rho(A)^2
 =\max_k\left[
 4+2\cos(2\theta_k)+2\cos(2s\theta_k)
 \right],
 \qquad
 \theta_k=\frac{(2k+1)\pi}{3s}.
 \tag{1}
\]

Every antiperiodic grid point has distance at least `pi/(3s)` from
`pi Z`, hence

\[
 \cos(2\theta_k)\le\cos\frac{2\pi}{3s}<1.
\]

Since the second cosine is at most one,

\[
 \rho(A)^2
 \le 6+2\cos\frac{2\pi}{3s}
 =8-4\sin^2\frac\pi{3s}<8.
 \tag{2}
\]

Therefore

\[
 m(3s,s)<\sqrt8
 \qquad(s\text{ even}).
 \tag{3}
\]

No optimality claim for this particular signing is needed.

## 2. The short odd cases `s=3,5`

For `s=3`, `N=9`, take Hamilton holonomy `alpha=+1` and

\[
 \tau=(-1,1,-1,-1,1,-1,1,-1,1).
\]

For `s=5`, `N=15`, take `alpha=+1` and

\[
 \tau=(1,-1,1,-1,1,-1,1,-1,-1,1,-1,1,-1,1,-1).
\]

In both cases set

\[
 C=8I-A^2.
\]

The exact leading principal minors of `C` are respectively

\[
 4,16,60,209,722,2508,5746,15993,47304
 \tag{4}
\]

and

\[
\begin{split}
 4,16,60,225,840,2911,10082,34080,118048,408588,\\
 1166430,3383853,6382980,4663008,8636544.
\end{split}
 \tag{5}
\]

All are positive.  Sylvester's criterion therefore proves `C>0` exactly,
so in both cases

\[
 \rho(A)^2<8.
 \tag{6}
\]

The script `verify_n3s_short_threshold.py` reconstructs the seam-safe integer
matrices and verifies (4)--(5) exactly.  Both examples are one-positive-`Q`
defect near-alternating words; the defect is at index `2` for `(9,3)` and at
index `7` for `(15,5)`.

Hence

\[
 m(9,3)<\sqrt8,
 \qquad
 m(15,5)<\sqrt8.
 \tag{7}
\]

## 3. Odd `s>=7`: uniform all-signing obstruction

`N3S_GLOBAL_OBSTRUCTION.md` proves that for every odd `s>=7` and every edge
signing of `C_(3s)(1,s)`,

\[
 \rho(A)^2\ge8+\frac1{70}.
 \tag{8}
\]

Its proof is exhaustive only in a fixed finite local state space, not in `s`:

- `s=7` is covered by the exact all-signing `C_21(1,7)` certificate, with the
  stronger excess `18/131`;
- `s=9` is covered by an exact prefix-pruned all-signing certificate at
  margin `1/70`;
- every odd `s>=11` follows from the nine-column signed-triangle local rule
  and the impossibility of a signed triangle being orthogonally similar to
  its negative.

Therefore

\[
 m(3s,s)^2\ge8+\frac1{70}>8
 \qquad(s\ge7\text{ odd}).
 \tag{9}
\]

Combining (3), (7), and (9) proves Theorem R.

## 4. Why this is a genuine arithmetic phase transition

The periodic odd-jump Bloch model is below `sqrt(8)` for every odd jump and
has sharp gap `pi^2/s^2`.  Nevertheless, on the finite line `N=3s`, the chord
subgraph consists of `s` triangles.  Once `s` is odd and at least seven, the
helical closure is incompatible with every locally low-norm alternating
triangle pattern; a local spectral witness is then unavoidable.

Thus the obstruction is not merely failure of period two to fit an odd ring.
For odd `s>=7`, **no signing at all** is sub-`sqrt(8)`.

## 5. Evidence boundary

The positive cases `s=3,5` are exact finite Sylvester certificates.  The
negative cases `s>=7` use the exact finite-state/integer certificates and
structural argument of `N3S_GLOBAL_OBSTRUCTION.md`.  No floating eigenvalue is
used as theorem evidence in Theorem R.

The theorem classifies only the threshold `m(3s,s)<sqrt(8)` on the line
`N=3s`; it does not give the exact value of `m(3s,s)`.

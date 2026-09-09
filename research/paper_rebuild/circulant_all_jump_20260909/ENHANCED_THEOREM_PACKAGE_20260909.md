# Enhanced theorem package for Paper I

Date: 2026-09-09

Branch: `paper/circulant-periodic-gap-20260909`

This note supersedes the old editorial hierarchy for Paper I. It does not delete any proved result, but it changes which results should be treated as headline theorems.

The paper is independent of the finite-global extremal paper. No statement below involves the minimum over all finite signings.

## 1. Central object

For a fixed periodic Hamilton-gauge word `tau` and jump `s`, let

\[
R_s(\tau)=\max_{|z|=1}\rho(H_{s,\tau}(z))^2
\]

be the continuous squared Bloch edge of that explicit periodic phase.

The paper now studies two related questions:

1. how much structure can be proved inside natural low-period classes;
2. how short a period is sufficient to force `R_s(tau)<8` as a function of the arithmetic of `s`.

This is stronger and more precise than treating one parity-dependent family as canonical.

---

# Theorem A — complete period-two variational theory

Among all words of period dividing two, the alternating word is the unique minimizer up to translation.

For odd `s`,

\[
\min_{\operatorname{per}(\tau)\mid2}R_s(\tau)
=8-g_s<8,
\]

where

\[
g_s=4\min_\theta
\bigl(\sin^2\theta+\cos^2(s\theta)\bigr).
\]

For even `s`,

\[
\min_{\operatorname{per}(\tau)\mid2}R_s(\tau)=8.
\]

Thus the parity obstruction is not an artifact of a chosen construction: it is an exact variational statement in the smallest nontrivial periodic sector.

For odd `s>=3`, the minimizing phase is unique and satisfies

\[
\sin(2\theta_s)=s\sin(2s\theta_s).
\]

Moreover

\[
g_s\downarrow0,
\qquad
s^2g_s\uparrow\pi^2.
\]

The detailed proof is in `PERIOD_TWO_VARIATIONAL_THEORY.md`.

---

# Theorem B — high-order odd asymptotics

As odd `s` tends to infinity,

\[
\theta_s=
\frac\pi{2s}-\frac\pi{2s^3}
+\frac{\pi(6+\pi^2)}{12s^5}
-\frac{\pi(\pi^4+100\pi^2+120)}{240s^7}
+O(s^{-9}),
\]

and

\[
\begin{aligned}
g_s={}&\frac{\pi^2}{s^2}
-\frac{\pi^2(\pi^2+12)}{12s^4}\\
&+\frac{\pi^2(\pi^4+120\pi^2+360)}{360s^6}\\
&-\frac{\pi^2(\pi^6+896\pi^4+18480\pi^2+20160)}{20160s^8}
+O(s^{-10}).
\end{aligned}
\]

This turns the former leading-order statement into a genuine asymptotic expansion.

---

# Theorem C — exact fixed period eight on `v_2(s)=1`

For every

\[
s\equiv2\pmod4,
\]

the same period-eight word

\[
(1,1,-1,1,-1,-1,1,-1)
\]

has the exact Bloch edge

\[
\boxed{
4+\sqrt{10+2\sqrt5}<8.}
\]

Hence this entire congruence class has one fixed period-eight phase with the uniform squared gap

\[
4-\sqrt{10+2\sqrt5}.
\]

Proof: `UNIFORM_PERIOD8_MOD4_THEOREM.md`.

---

# Theorem D — a second period-eight phase on `v_2(s)=2`

For every

\[
s\equiv4\pmod8,
\]

the fixed period-eight word

\[
(-1,1,1,-1,-1,1,-1,1)
\]

satisfies

\[
\boxed{
R_s(\tau)<4+\sqrt{10+2\sqrt5}<8.}
\]

Thus

\[
8-R_s(\tau)
>4-\sqrt{10+2\sqrt5}
\]

uniformly on the whole congruence class.

The exact dispersion is

\[
4+\sqrt{
8+2\cos(2nt)
+\sqrt{10-8\cos(nt)+2\cos t}},
\qquad n=s/4\text{ odd},
\]

for the top squared branch.

Proof: `UNIFORM_PERIOD8_MOD8_THEOREM.md`.

---

# Theorem E — fixed period sixteen on `v_2(s)=3`

For every

\[
s\equiv8\pmod{16},
\]

the period-sixteen two-defect word

\[
(1,1,-1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1)
\]

satisfies

\[
\boxed{R_s(\tau)<8.}
\]

A completely explicit uniform estimate is

\[
\boxed{
8-R_s(\tau)\ge\frac{28}{8^7}.}
\]

The proof uses:

- a generic two-phase `16 x 16` threshold determinant identity;
- a positive Bernstein-basis certificate `F(x)>=32` on `[-2,2]`;
- a fixed-fiber inertia calculation;
- a signed-reflection chiral symmetry explaining the even characteristic polynomial.

Proof: `UNIFORM_PERIOD16_MOD16_THEOREM.md`.

---

# Corollary F — short-period theorem through the first three 2-adic layers

If `s` is even and

\[
16\nmid s,
\]

then there is an explicit periodic signing with

\[
R_s(\tau)<8
\]

whose period is at most sixteen.

More precisely:

\[
\begin{array}{c|c|c}
 v_2(s)&\text{period used}&\text{gap information}\\ \hline
 1&8&\text{exact uniform constant}\\
 2&8&\text{strictly better than the same constant}\\
 3&16&\text{explicit uniform positive bound}
\end{array}
\]

This arithmetic short-period statement is stronger on these subsequences than the old period-`4s` construction.

---

# Theorem G — all-jump fallback construction

The previously proved all-jump result remains useful for the part of the parameter space not yet compressed by Theorems C--E.

For every `s>=2` there is an explicit periodic phase with squared edge below `8`:

- period two for odd `s`;
- the previously constructed period-`4s` antipodal phase for even `s`.

For that original parity-dependent family, the gap has leading scale

\[
s^2\widehat g_s\to\pi^2,
\]

and the audited even phase-slip theorem remains valid.

Important editorial correction: this `pi^2/s^2` theorem is now a sharp asymptotic theorem **for that explicit family**, not a claim that `Theta(s^-2)` is the best gap achievable by arbitrary periodic signings. Theorems C--E show that it is not the strongest construction on several infinite even subsequences.

---

# Structural symmetry — two-defect signed reflection

The period-sixteen result reveals a general mechanism. For the two-defect word of even period `2L>=8` defined by

\[
Q_0=Q_2=1,
\qquad Q_j=-1\ (j\ne0,2),
\]

the Hamilton-gauge lift satisfies

\[
\tau_{3-j}=-\tau_j.
\]

For a jump

\[
s=L(2q+1),
\]

alternating sign times reflection gives a chiral symmetry. This explains why the natural next parameter is the `2`-adic valuation of `s` and supplies a conceptual route toward higher layers.

This symmetry is proved as part of `UNIFORM_PERIOD16_MOD16_THEOREM.md` and should become a standalone proposition in the final manuscript.

---

# Main open strengthening target

The leading conjectural theorem suggested by exact computation is:

> Let `2^k || s`, with `k>=2`. There should exist a two-defect periodic phase of period `2^{k+1}` (or another period bounded solely in terms of `k`) whose continuous squared Bloch edge is strictly below `8` for every odd multiple of `2^k`.

Exact numerical experiments currently support the two-defect period `2^{k+1}` pattern for the next layers as well, including `k=4,5`, but these cases remain **Observed**, not Proved, until a uniform continuant/transfer proof is completed.

The paper should not state the general hierarchy as a theorem yet.

---

# Revised paper-level thesis

The paper should no longer be sold primarily as

> one parity-dependent family with a common `pi^2/s^2` gap.

The stronger current thesis is:

> periodic spectral improvement in signed step circulants has a genuine arithmetic hierarchy. The smallest periodic sector exhibits an exact parity bifurcation; successive even `2`-adic layers admit unexpectedly short periodic phases with uniform sub-eight gaps; and the original all-jump family supplies a universal fallback together with sharp variational and phase-slip asymptotics.

This gives the manuscript three kinds of mathematical content:

1. **variational classification** rather than construction alone;
2. **arithmetic/2-adic structure** rather than parity alone;
3. **sharp asymptotic analysis** rather than threshold existence alone.

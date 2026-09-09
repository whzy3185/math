# Final periodic theorem package after general compression

Date: 2026-09-09

Branch: `paper/circulant-periodic-gap-20260909`

Status: this package supersedes the earlier headline hierarchy in `ENHANCED_THEOREM_PACKAGE_20260909.md`. Older notes remain proof sources and special-case sharpenings.

No theorem below concerns the global minimum over all finite signings. Paper I remains independent of the finite-extremal manuscript.

---

# Main theorem 1 — exact period-two variational bifurcation

Among all Hamilton-gauge words of period dividing two, the alternating word is the unique minimizer up to translation.

For odd `s`,

\[
\min_{\operatorname{per}(\tau)\mid2}R_s(\tau)
=8-g_s<8,
\]

where

\[
g_s=4\min_\theta\bigl(\sin^2\theta+\cos^2(s\theta)\bigr).
\]

For even `s`,

\[
\min_{\operatorname{per}(\tau)\mid2}R_s(\tau)=8.
\]

Thus the parity obstruction is an exact low-period variational statement, not an artifact of a chosen construction.

For odd `s`, the minimizing phase is unique and the full asymptotic expansion begins

\[
g_s=\frac{\pi^2}{s^2}
-\frac{\pi^2(\pi^2+12)}{12s^4}
+O(s^{-6}).
\]

The longer expansion through `s^-8` is recorded in `PERIOD_TWO_VARIATIONAL_THEORY.md`.

---

# Main theorem 2 — general two-defect period compression

Let `L>=4` be even and let

\[
s=L(2q+1).
\]

Take the period-`2L` two-defect flux phase

\[
Q_0=Q_2=1,
\qquad
Q_j=-1\quad(j\ne0,2).
\]

Then its continuous squared Bloch edge satisfies

\[
\boxed{R_{L,q}<8.}
\]

The proof folds the `2L`-dimensional fiber to an `L`-site two-component chain and reduces the characteristic problem to a `4 x 4` transfer monodromy. At the threshold `8`, the exact characteristic determinant is

\[
P_{L,q,z}(8)=F_L(d)+d-e,
\]

with

\[
d=2\cos((2q+1)t),
\qquad
e=2\cos t,
\]

and a Chebyshev expression `F_L` satisfying the uniform inequality

\[
\boxed{F_L(x)\ge20\qquad(-2\le x\le2).}
\]

Hence

\[
P_{L,q,z}(8)\ge16
\]

for every phase and every odd multiplier.

Proof: `GENERAL_TWO_DEFECT_COMPRESSION_THEOREM.md`.

---

# Main theorem 3 — `2`-adic short-period theorem for every even jump

Let `s` be even.

If

\[
v_2(s)=1,
\]

a fixed period-eight phase gives the exact edge

\[
4+\sqrt{10+2\sqrt5}<8.
\]

If

\[
v_2(s)=k\ge2,
\]
put

\[
L=2^k.
\]

Then `s/L` is odd, so Main theorem 2 gives an explicit phase of period

\[
\boxed{2^{k+1}}
\]

with edge below `8`.

Therefore every even jump admits a sub-eight periodic phase whose period depends only on its `2`-adic valuation and is completely independent of the odd part of the jump.

This replaces the former period-`4s` construction as the strongest general existence/period theorem.

---

# Main theorem 4 — quantitative compressed gap

For the two-defect family, write

\[
g_{L,q}=8-R_{L,q}.
\]

For every even `L>=6` and every `q>=0`,

\[
\boxed{
g_{L,q}\ge\frac1{10L^2}.}
\]

The proof uses the exact full characteristic formula and the identity

\[
\frac{P_y(8)}{P(8)}
=\sum_j\frac1{8-y_j},
\]

together with Chebyshev logarithmic-derivative bounds.

Thus the compression theorem has a polynomial rather than merely existential gap.

Proof: `QUADRATIC_COMPRESSED_GAP_THEOREM.md`.

---

# Main theorem 5 — sharp compressed spectral constant

The preceding quadratic scale is sharp. Put

\[
a=\arccos(1/3).
\]

For every sequence of even `L -> infinity` and every sequence `q=q(L)>=0`,

\[
\boxed{
L^2g_{L,q}
\longrightarrow
4\arccos^2(1/3).
}
\]

Equivalently, convergence is uniform in the odd multiplier.

For the `2`-adic specialization `L=2^k`,

\[
\boxed{
8-R_s^{\rm comp}
\sim
\frac{4\arccos^2(1/3)}{4^k},
\qquad k=v_2(s)\to\infty,
}
\]

uniformly in the odd part of `s`.

The constant comes from the limiting Robin equation

\[
3\cos a=1.
\]

At a maximizing phase, the scaled determinant converges to

\[
34-e-36\sin^2\left(\frac{\sqrt{\gamma-D}}2\right),
\]

where `D` is the scaled displacement of the folded long-jump phase and `e<=2` is the residual seam phase. The phase terms can only increase the limiting cost, forcing

\[
\gamma\ge4a^2.
\]

The periodic phase attains this constant asymptotically.

Proof: `SHARP_COMPRESSED_GAP_ASYMPTOTIC.md`.

---

# Special exact layers

The earlier explicit layers remain useful as exact closed-form examples, not as the general theorem.

## `v_2(s)=1`

A single period-eight word has the exact edge

\[
4+\sqrt{10+2\sqrt5}.
\]

## `v_2(s)=2`

A translated form of the general two-defect word already has period eight, with a closed top dispersion and a stronger uniform bound than the general `1/(10L^2)` estimate.

## `v_2(s)=3`

The period-sixteen threshold polynomial and Bernstein certificate give a concrete finite-dimensional model of the general transfer theorem.

These examples should appear after the general theorem, not before it.

---

# Secondary theorem — the old all-jump family and its `pi^2` law

The previous parity-dependent construction remains mathematically valuable but changes editorial role.

For every `s>=2`, it gives an explicit sub-eight phase:

- period two for odd `s`;
- period `4s` for even `s`.

For this family,

\[
s^2\widehat g_s\to\pi^2,
\]

and the even phase has the audited boundary-layer slip

\[
r^2\phi_r\to\frac{\pi}{4\sqrt2},
\qquad
r^4(e_r-g_{2r})\to\frac{\pi^2}{32}.
\]

These results should now be presented as a second, more slowly varying family with a detailed perturbative theory, not as the strongest existence construction on even jumps.

---

# Revised mathematical thesis

The paper now proves a genuine arithmetic spectral theory:

1. the smallest periodic sector has an exact parity bifurcation;
2. two local flux defects admit a universal transfer reduction for every even half-period;
3. every even jump has a short period controlled only by `v_2(s)`;
4. the compressed gap has the sharp scale
   \[
   4^{-v_2(s)}
   \]
   with constant `4 arccos^2(1/3)`;
5. a different explicit family exhibits the independent sharp constant `pi^2` and a phase-slip boundary layer.

The coexistence of the two constants

\[
\pi^2
\qquad\text{and}\qquad
4\arccos^2(1/3)
\]

should be used to organize the asymptotic discussion: they arise from two different effective boundary conditions and two genuinely different periodic mechanisms.

---

# Remaining strengthening targets

The existential `2`-adic hierarchy is closed. The next questions are now finer:

- determine whether `z=1` is the exact global maximizing phase for the compressed family for all even `L>=6`;
- obtain the next correction beyond `4 arccos^2(1/3)/L^2`;
- classify whether the period `2^{k+1}` is minimal within a natural two-defect or chiral class;
- compare the two-defect family with other bounded-defect patterns at fixed `v_2(s)`.

These are strengthening problems; they are no longer needed to justify the main arithmetic compression theorem.
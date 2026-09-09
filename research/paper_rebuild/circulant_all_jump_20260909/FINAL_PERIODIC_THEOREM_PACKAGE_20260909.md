# Final periodic theorem package after general compression and exact phase selection

Date: 2026-09-09

Branch: `paper/circulant-periodic-gap-20260909`

Status: **current headline package** for Paper I. This supersedes the earlier editorial hierarchy. Older notes remain proof sources and special-case sharpenings.

No theorem below concerns the minimum over all finite signings. Paper I remains completely independent of the finite-extremal manuscript.

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

Thus parity is an exact low-period variational obstruction, not an artifact of a chosen construction.

For odd `s`, the minimizing phase is unique and the gap has a full analytic expansion; in particular

\[
g_s=\frac{\pi^2}{s^2}
-\frac{\pi^2(\pi^2+12)}{12s^4}
+O(s^{-6}),
\]

with the expansion through `s^-8` recorded in `PERIOD_TWO_VARIATIONAL_THEORY.md`.

---

# Main theorem 2 — general two-defect compression

Let `L>=4` be even and let

\[
s=L(2q+1),
\qquad q\ge0.
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

The proof folds the `2L`-dimensional Bloch fiber to an `L`-site two-component chain and reduces the characteristic problem to a fixed `4 x 4` transfer monodromy.

At the threshold `8`,

\[
P_{L,q,z}(8)=F_L(d)+d-e,
\]

where

\[
d=2\cos((2q+1)t),
\qquad
e=2\cos t,
\]

and a Chebyshev monotonicity argument gives

\[
F_L(x)\ge20
\qquad(-2\le x\le2).
\]

Hence

\[
P_{L,q,z}(8)\ge16>0
\]

for every phase and odd multiplier; an inertia anchor at `z=1` then proves the sub-eight theorem.

Proof: `GENERAL_TWO_DEFECT_COMPRESSION_THEOREM.md`.

---

# Main theorem 3 — complete `2`-adic period compression for every even jump

Let `s` be even.

If

\[
v_2(s)=1,
\]

a fixed period-eight phase gives the exact edge

\[
\boxed{4+\sqrt{10+2\sqrt5}<8.}
\]

If

\[
v_2(s)=k\ge2,
\]
put

\[
L=2^k.
\]

Then `s/L` is odd, so Main theorem 2 supplies an explicit sub-eight phase of period

\[
\boxed{2^{k+1}}.
\]

Therefore every even jump has an explicit sub-eight periodic phase whose period depends only on the `2`-adic valuation of `s` and is completely independent of the odd part of the jump.

The older period-`4s` construction is no longer the strongest general existence/period theorem.

---

# Main theorem 4 — polynomial quantitative gap

For the general two-defect family, write

\[
g_{L,q}=8-R_{L,q}.
\]

For every even `L>=6` and every `q>=0`,

\[
\boxed{
g_{L,q}\ge\frac1{10L^2}.}
\]

This improves the elementary determinant-product lower bound from exponential to the correct polynomial scale.

The proof uses the exact full characteristic polynomial, the logarithmic-derivative identity

\[
\frac{P_y(8)}{P(8)}
=\sum_j\frac1{8-y_j},
\]

and explicit Chebyshev logarithmic-derivative estimates.

Proof: `QUADRATIC_COMPRESSED_GAP_THEOREM.md`.

---

# Main theorem 5 — exact two-phase Floquet discriminant

For a general squared spectral parameter `y=lambda^2`, define

\[
d=z^{2q+1}+z^{-(2q+1)},
\qquad
e=z+z^{-1}.
\]

With

\[
m=\frac{L-4}{2},
\qquad
t=\frac{y-d-4}{2},
\qquad
u=U_m(t),
\qquad
w=U_{m-1}(t),
\]

the characteristic equation has the exact scalar form

\[
\boxed{
\det(\lambda I-H_{L,q}(z))
=G_L(y,d)-e,
}
\]

where `G_L` is an explicit Chebyshev polynomial expression. Thus all dependence on the odd multiplier is compressed into the internal real phase `d`, while the ordinary Bloch seam enters linearly through `-e`.

This exact discriminant is the structural input for the global asymptotic theory.

Proof: `COMPRESSED_GLOBAL_SHARP_GAP_THEOREM.md` (equivalent coefficient form also appears in `QUADRATIC_COMPRESSED_GAP_THEOREM.md`).

---

# Main theorem 6 — sharp global compressed constant

Let

\[
a=\arccos(1/3).
\]

For every sequence of even `L->infinity` and every sequence `q=q(L)>=0`,

\[
\boxed{
L^2g_{L,q}
\longrightarrow
4\arccos^2\frac13
=6.0610443485\ldots .
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

The constant is forced by the continuum discriminant

\[
16+18\cos\sqrt{\gamma-D}
\]

and the limiting Robin equation

\[
3\cos a=1.
\]

At every maximizing sequence,

\[
L^2(2-d_L)\to0,
\qquad
z_L+z_L^{-1}\to2.
\]

Proof: `SHARP_COMPRESSED_GAP_ASYMPTOTIC.md` and the streamlined exact-discriminant proof in `COMPRESSED_GLOBAL_SHARP_GAP_THEOREM.md`.

---

# Main theorem 7 — first correction and phase rigidity

Uniformly in the odd multiplier,

\[
\boxed{
L^2g_{L,q}
=4a^2+rac{16a^2}{3L}+o(L^{-1}).
}
\]

Moreover, if `z_L=e^{it_L}` is a maximizing phase and

\[
d_L=2\cos((2q+1)t_L),
\qquad
e_L=2\cos t_L,
\]

then

\[
\boxed{
L^3(2-d_L)\to0,
\qquad
L(2-e_L)\to0.
}
\]

Thus there is no analogue of the old even-family phase slip at order `L^-3`.

Proof: `FIRST_CORRECTION_COMPRESSED_GAP.md`.

---

# Main theorem 8 — eventual exact phase selection

There exists an even `L_0` such that for every even `L>=L_0` and every `q>=0`,

\[
\boxed{
R_{L,q}=\rho(H_{L,q}(1))^2,
}
\]

and `z=1` is the unique maximizing Bloch phase.

The proof combines the uniform sharp localization with a local analytic implicit branch

\[
\gamma=\Gamma(h,D,E),
\qquad h=L^{-1},
\]

whose phase derivatives satisfy

\[
\partial_D\Gamma(0,0,0)=1,
\qquad
\partial_E\Gamma(0,0,0)=\frac{a}{2\sqrt2}>0.
\]

Hence any nonzero phase displacement strictly increases the scaled gap once the global maximizer lies in the local branch. Since the periodic phase already provides the competing upper gap, the maximizing phase must have `D=E=0`, i.e. `z=1`.

Proof: `EVENTUAL_EXACT_PERIODIC_PHASE_THEOREM.md`.

---

# Main theorem 9 — complete algebraic endpoint/global expansion

For all sufficiently large even `L`, Main theorem 8 reduces the global gap exactly to a scalar Robin equation. Consequently, for every fixed `M`,

\[
\boxed{
L^2g_{L,q}
=\sum_{j=0}^{M}\Gamma_jL^{-j}
+O_M(L^{-M-1}),
}
\]

uniformly in `q`.

The first four coefficients are

\[
\Gamma_0=4a^2,
\qquad
\Gamma_1=\frac{16a^2}{3},
\]

\[
\Gamma_2
=\frac{16a^2}{3}
+\frac{4\sqrt2\,a^3}{9}
-\frac{4a^4}{3},
\]

and

\[
\Gamma_3
=\frac{16a^2}{81}
\left(24+6\sqrt2\,a-13a^2\right).
\]

Proof: `HIGHER_ORDER_COMPRESSED_GAP_EXPANSION.md`.

---

# Special exact layers

The low `2`-adic layers remain useful as closed-form models, not as substitutes for the general theorem.

## `v_2(s)=1`

One period-eight word has the exact edge

\[
4+\sqrt{10+2\sqrt5}.
\]

## `v_2(s)=2`

A period-eight specialization of the compressed mechanism has a closed top dispersion and a stronger constant bound than the general quadratic estimate.

## `v_2(s)=3`

The period-sixteen threshold determinant and Bernstein certificate give a transparent finite-dimensional model of the general transfer theorem.

These should be presented as examples after the general compression mechanism has been introduced.

---

# Secondary theorem — the older all-jump family and its `pi^2` law

The previous parity-dependent family remains mathematically valuable but has a different role.

For every `s>=2` it gives an explicit sub-eight phase:

- period two for odd `s`;
- period `4s` for even `s`.

For this family,

\[
s^2\widehat g_s\to\pi^2,
\]

and the even phase has the audited phase-slip law

\[
r^2\phi_r\to\frac{\pi}{4\sqrt2},
\qquad
r^4(e_r-g_{2r})\to\frac{\pi^2}{32}.
\]

These are sharp statements for that explicit family, not global periodic-optimality claims.

---

# Revised paper-level thesis

The paper now proves a genuine arithmetic spectral theory:

1. the smallest periodic sector has an exact parity bifurcation;
2. two local flux defects admit a universal signed-reflection and `4 x 4` transfer reduction;
3. every even jump has a short period controlled only by `v_2(s)`;
4. the compressed family has a uniform `L^-2` gap and the sharp constant
   \[
   4\arccos^2(1/3);
   \]
5. the global maximizing phase is eventually exactly periodic;
6. the resulting gap has a complete algebraic asymptotic expansion;
7. a different explicit family has the independent constant `pi^2` and a genuine phase-slip boundary layer.

The coexistence of

\[
\pi^2
\qquad\text{and}\qquad
4\arccos^2(1/3)
\]

is now one of the conceptual themes: they arise from two different effective boundary conditions and two genuinely different periodic mechanisms.

---

# Remaining strengthening targets

The existential hierarchy, polynomial gap scale, sharp leading constant, and eventual phase selection are closed. Remaining problems are finer:

- remove the unspecified threshold and prove `z=1` is the exact global maximizer for every even `L>=6`;
- optimize the elementary uniform lower constant `1/10` in the finite-`L` quadratic gap;
- classify minimal period within natural two-defect/chiral subclasses;
- compare two-defect patterns with more general bounded-defect flux words;
- determine whether the compressed family is variationally optimal inside a natural fixed-defect class.

These are strengthening directions, not missing pieces of the main compression theorem.
# Above-edge bound-state hierarchy for a fixed generic complement

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I.

This theorem refines `SCALING_DEFECT_WIDTH_OBSTRUCTION.md`. The failure of the sub-eight property is not confined to the extreme case with only two generic sites. It persists whenever the number of generic sites left outside the defect block is fixed.

## 1. Geometry

Let

\[
L=2r,
\qquad h=r-k,
\]

where `k>=1` is fixed and `r>k`. The two positive local flux defects are at positions `0` and `2h`; thus the defect interval contains

\[
2h=2r-2k=L-2k
\]

sites and the complementary generic interval contains exactly `2k` sites.

Take any jump

\[
s=L(2q+1).
\]

At the antiperiodic phase `z=-1`, the long-jump phase is independent of the odd multiplier up to unitary equivalence.

## Theorem A — fixed-complement obstruction

For every fixed integer `k>=1`, there exists `r_0(k)` such that for every

\[
r\ge r_0(k)
\]

and every `q>=0`, the `z=-1` fiber has a squared eigenvalue above `8`. Hence

\[
\boxed{
R^{(r-k)}_{2r,q}>8
}
\tag{1.1}
\]

for all sufficiently large `r`.

Thus a two-defect phase cannot remain sub-eight if the generic complement has bounded length.

---

## 2. Hyperbolic transfer parameter

For `y>8`, put

\[
t=\frac{y-6}{2}>1
\]

and define the stable hyperbolic multiplier

\[
\boxed{
a=t-\sqrt{t^2-1}\in(0,1).}
\tag{2.1}
\]

Then

\[
a^2-(y-6)a+1=0,
\qquad
\boxed{y=6+a+a^{-1}.}
\tag{2.2}
\]

The long defect block has length `2(r-k)`. If

\[
U=U_{r-k}(t),
\qquad
V=U_{r-k-1}(t),
\]

then, uniformly on compact subsets of `y>8`,

\[
\frac VU\longrightarrow a,
\qquad UV\longrightarrow\infty.
\tag{2.3}
\]

The finite generic block has length `2k`, so after dividing the exact `4 x 4` transfer determinant by `UV`, one obtains a finite limiting secular function depending only on `k` and `a`.

---

## 3. The fixed-complement secular polynomial

Define polynomials `P_k(a)` recursively by

\[
P_0(a)=a^2+4a-1,
\tag{3.1}
\]

\[
P_1(a)=9a^2-4a-1,
\tag{3.2}
\]

and, for `k>=1`,

\[
\boxed{
P_{k+1}(a)
=(a^2+4a+1)P_k(a)
-a^2P_{k-1}(a)
-4a^{k+1}(a+1)^2.
}
\tag{3.3}
\]

### Proposition B — limiting secular equation

After the hyperbolic normalization (2.3), the antiperiodic characteristic determinant converges locally uniformly to a nonzero positive factor times

\[
\boxed{P_k(a).}
\tag{3.4}
\]

Consequently every zero of `P_k` in `(0,1)` gives a limiting squared bound-state energy

\[
\boxed{y=6+a+a^{-1}>8.}
\tag{3.5}
\]

### Proof

At `z=-1`, the folded transfer has a long defect factor and a fixed generic factor of length `2k`. The defect transfer has scalar-square parameter `t=(y-6)/2`; writing its two Chebyshev coefficients as `U,V` and reducing by

\[
U^2+V^2-(y-6)UV=1
\]

leaves a determinant linear in `UV` and `V^2`, plus bounded terms.

Replacing `V/U` by its limiting value `a` gives the secular polynomial. Increasing the generic complement from `2k` to `2(k+1)` multiplies the fixed generic transfer by one additional paired cell. Its trace is

\[
y-2=a+4+a^{-1}.
\]

The resulting second-order transfer recurrence becomes (3.3) after clearing the factor `a^k`. The initial cases are the direct `2 x 2` and `4 x 4` generic complements, giving (3.1)--(3.2).

---

## 4. Closed Chebyshev form

Put

\[
b(a):=\frac{a+a^{-1}+4}{2}>3.
\tag{4.1}
\]

Define

\[
Q_k(a):=a^{-k}P_k(a)-4a.
\]

Then (3.3) becomes the homogeneous recurrence

\[
Q_{k+1}=2b(a)Q_k-Q_{k-1}.
\tag{4.2}
\]

The initial values are

\[
Q_0=a^2-1,
\]

\[
Q_1=\frac{(a-1)(5a+1)}a.
\]

Therefore

\[
\boxed{
\begin{aligned}
P_k(a)=a^k\Bigg[4a+(a-1)\Bigg(&
\frac{5a+1}{a}
U_{k-1}(b(a))\\
&-(a+1)U_{k-2}(b(a))
\Bigg)\Bigg].
\end{aligned}}
\tag{4.3}
\]

For `k=1`, this gives

\[
P_1(a)=9a^2-4a-1,
\]

whose physical root is

\[
a_1=\frac{2+\sqrt{13}}9,
\]

recovering the algebraic energy in the almost-antipodal theorem.

---

## 5. Existence of a physical root

For every `k>=1`,

\[
P_k(0)=-1
\]

and

\[
\boxed{P_k(1)=4.}
\tag{5.1}
\]

Hence by continuity there exists at least one

\[
\boxed{a_k\in(0,1)}
\tag{5.2}
\]

with `P_k(a_k)=0`.

Choose the largest such root and put

\[
y_k=6+a_k+a_k^{-1}>8.
\tag{5.3}
\]

The local uniform convergence in Proposition B and the sign change around the largest simple physical zero give a finite-fiber squared eigenvalue converging to `y_k`. Therefore the antiperiodic fiber is eventually above `8`, proving Theorem A.

(If a multiple root occurred for an isolated `k`, the same conclusion follows by a small one-sided sign interval; direct Sturm analysis shows the physical root is in fact simple. Simplicity is not needed for the existence theorem.)

---

## 6. Large-`k` asymptotics of the bound state

The physical root closest to one has an especially simple asymptotic law.

### Theorem C

As `k->infinity`,

\[
\boxed{
1-a_k
\sim \frac{2}{T_k(3)}.
}
\tag{6.1}
\]

Consequently

\[
\boxed{
y_k-8
\sim\frac{4}{T_k(3)^2}.}
\tag{6.2}
\]

Since

\[
T_k(3)
=\frac{(3+2\sqrt2)^k+(3-2\sqrt2)^k}{2},
\]

we obtain

\[
\boxed{
y_k-8
\sim16(3-2\sqrt2)^{2k}.}
\tag{6.3}
\]

### Proof

Write (4.3) as

\[
4a=(1-a)B_k(a),
\tag{6.4}
\]

where

\[
B_k(a)=
\frac{5a+1}{a}U_{k-1}(b(a))
-(a+1)U_{k-2}(b(a)).
\]

At `a=1`,

\[
b(1)=3
\]

and the Chebyshev identity

\[
6U_{k-1}(3)-2U_{k-2}(3)=2T_k(3)
\]

gives

\[
\boxed{B_k(1)=2T_k(3).}
\tag{6.5}
\]

The root selected closest to `1` satisfies `a_k->1`: this follows by evaluating (6.4) at `a=1-c/T_k(3)` with any fixed `c<2` and `c>2`, using the standard hyperbolic Chebyshev estimates. On that scale,

\[
b(a_k)-3=O((1-a_k)^2)
=O(T_k(3)^{-2}),
\]

so the relative variation of the fixed-index Chebyshev combination is `o(1)`. Hence

\[
B_k(a_k)
=2T_k(3)(1+o(1)).
\]

Substitution into (6.4), together with `a_k->1`, proves (6.1).

Finally,

\[
y_k-8
=a_k+a_k^{-1}-2
=\frac{(1-a_k)^2}{a_k},
\]

which gives (6.2), and the closed form for `T_k(3)` gives (6.3).

---

## 7. Interpretation and critical growth scale

The above-edge excess for a fixed generic complement of size `2k` decays exponentially in `k`:

\[
y_k-8
\asymp(3-2\sqrt2)^{2k}.
\]

This explains a numerical phenomenon that can otherwise be misleading: for moderately large `k`, finite cells may appear sub-eight over a long preasymptotic range even though the eventual infinite-defect-background bound state lies above `8`.

The theorem also identifies the natural next scale. Since the sub-eight finite-size gaps elsewhere in the compressed theory are of order `L^{-2}`, balancing

\[
(3-2\sqrt2)^{2k}
\]

against `L^{-2}` suggests the logarithmic transition

\[
k\asymp
\frac{\log L}{|\log(3-2\sqrt2)|}.
\]

This logarithmic threshold is a **research target**, not asserted here as a theorem. The proved content is the fixed-`k` hierarchy and its exact exponential bound-state scale.
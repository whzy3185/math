# Exact quarter-period optimality in the `v_2(s)=3` minimal layer

Date: 2026-09-14

Status: **Proved** with exact rational Bernstein arithmetic.

This closes the first nontrivial finite layer not covered by the large-period balanced-optimality theorem.

## 1. Minimal cell

Let

\[
2^3\Vert s.
\]

The minimal compatible half-period is

\[
L=8,
\]

so the primitive coefficient period is

\[
p=16.
\]

In the even-separation two-defect family,

\[
N+m=L/2=4.
\]

Up to exchanging the two arcs, the possible geometries are

\[
(N,m)=(3,1),\quad(2,2),\quad(1,3).
\]

The quarter-period geometry is the balanced pair

\[
\boxed{(N,m)=(2,2),\qquad h=4=p/4.}
\]

We prove that it uniquely maximizes the full continuous Bloch gap for every odd multiplier.

---

## 2. The balanced geometry has gap larger than `1/5`

Set the rational squared-energy separator

\[
\boxed{y_0=\frac{39}{5}.}
\tag{2.1}
\]

For the balanced fiber `(N,m)=(2,2)`, direct evaluation of the fixed `4 x 4` transfer determinant gives

\[
\boxed{
P_{2,2,q,z}(y_0)=F(d)-e,
}
\tag{2.2}

where

\[
d=z^{2q+1}+z^{-(2q+1)}\in[-2,2],
\qquad
e=z+z^{-1}\le2,
\]

and

\[
\begin{aligned}
F(d)={}&d^8-\frac{1244}{25}d^6+\frac{505626}{625}d^4+4d^3\\
&-\frac{73507524}{15625}d^2-\frac{76}{25}d
+\frac{3479009391}{390625}.
\end{aligned}
\tag{2.3}
\]

Thus it suffices to prove

\[
F(d)>2
\qquad(-2\le d\le2).
\tag{2.4}
\]

Put

\[
d=4t-2,
\qquad0\le t\le1.
\]

In the degree-eight Bernstein basis `B_{j,8}(t)`, the exact polynomial `F(4t-2)-2` has coefficients

\[
\boxed{
\begin{aligned}
(&29610741/390625,\
323508191/390625,\
11411147087/2734375,\\
&26714504437/2734375,\
36676105387/2734375,\
26687441937/2734375,\\
&11382022087/2734375,\
326195691/390625,\
49860741/390625).
\end{aligned}}
\tag{2.5}
\]

Every coefficient is strictly positive; the smallest is

\[
\frac{29610741}{390625}>75.
\]

Since the Bernstein basis is nonnegative and sums to one,

\[
\boxed{F(d)-2>75}
\tag{2.6}
\]

throughout `[-2,2]`. Therefore

\[
P_{2,2,q,z}(y_0)>0
\]

for every unit Bloch phase and every odd multiplier.

At `z=1`, `BALANCED_ENDPOINT_BEATS_NEXT_DIRICHLET_LEVEL.md` with `r=2` gives

\[
e_2^+>D_3=2-\sqrt3>\frac15,
\]

so the entire endpoint spectrum lies strictly below `y_0=8-1/5`. Because the Hermitian fibers vary continuously and the determinant at `y_0` never vanishes, their inertia relative to `y_0` is constant on the Bloch circle. Hence no fiber has a squared eigenvalue at or above `y_0`.

Consequently

\[
\boxed{
\Gamma_{2,2,q}>\frac15.
}
\tag{2.7}

---

## 3. The short-defect competitor has gap smaller than `1/5`

For `(N,m)=(3,1)`, the geometry is the separation-two compressed phase with half-period

\[
L=2(N+m)=8.
\]

`SMALL_LAYER_EXACT_ENDPOINT_LOCKING.md` proves, uniformly in the odd multiplier, that its global edge is attained at `z=1`.

The endpoint top squared root is the upper root of

\[
p_4(y)=y^4-20y^3+136y^2-344y+196.
\tag{3.1}
\]

At the separator (2.1), exact arithmetic gives

\[
\boxed{
p_4(39/5)=-\frac{1559}{625}<0.}
\tag{3.2}
\]

The relevant upper root is below `8` and lies to the right of `39/5`; therefore

\[
R_{3,1,q}>\frac{39}{5}
\]

and

\[
\boxed{
\Gamma_{3,1,q}<\frac15.
}
\tag{3.3}

Combining (2.7) and (3.3),

\[
\Gamma_{2,2,q}>\Gamma_{3,1,q}.
\]

---

## 4. The long-defect competitor is already super-eight

For `(N,m)=(1,3)`, the exact all-parameter phase diagram gives

\[
R<8
\iff
2m<T_N(3).
\]

Here

\[
2m=6,
\qquad T_1(3)=3,
\]

so the inequality fails and the antiperiodic fiber is strictly super-eight:

\[
\boxed{R_{1,3,q}>8.}
\tag{4.1}
\]

Thus this geometry cannot compete with the balanced sub-eight phase.

---

## Theorem — exact `k=3` optimizer

For every jump

\[
s=8(2q+1),
\]

among all even-separation reflection-chiral two-defect phases of the minimal primitive period `16`, the unique gap-maximizing geometry is

\[
\boxed{
N=m=2,
\qquad h=4=p/4.
}
\tag{5.1}
\]

The proof is uniform in `q` and uses no floating-point acceptance test.

## 6. Relation to the all-layer problem

- `k=2` is trivial because the minimal cell contains only `N=m=1`.
- this note proves `k=3` exactly;
- the existing eventual theorem proves quarter-period optimality for all sufficiently large `k`.

The remaining task is to make the large-layer comparison effective (or prove a direct monotonic theorem) so that the intermediate powers of two are covered analytically.

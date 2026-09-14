# Exact odd-total geometry orientation for `r=1,...,5`

Date: 2026-09-14

Status: **Proved with exact rational certificates**.

This note treats the first five periods congruent to `4 mod 8` and proves that the periodic-near-balanced orientation is uniquely optimal.

## 1. Setup

Fix

\[
N+m=2r+1,
\qquad1\le r\le5.
\]

The coefficient period is

\[
p=4(N+m)=8r+4.
\]

The two nearest-balanced orientations are

\[
A_r=(r+1,r)
\]

and

\[
B_r=(r,r+1).
\]

We prove that, for every compatible odd multiplier,

\[
\boxed{
\Gamma_{r+1,r,q}
>
\Gamma_{N,m,q}
}
\tag{1.1}

for every other positive integer pair `N+m=2r+1`.

---

## 2. Rational separators

Use the following exact gaps:

\[
\begin{array}{c|c|c}
r&g_r&y_r=8-g_r\\ \hline
1&1/10&79/10\\
2&4/25&196/25\\
3&21/200&1579/200\\
4&149/2000&15851/2000\\
5&27219/500000&3972781/500000.
\end{array}
\tag{2.1}
\]

For `r>=2`, every geometry other than the two nearest-balanced orientations has

\[
M=\max\{N,m\}\ge r+2.
\]

The universal endpoint bound gives

\[
\Gamma_{N,m,q}<D_{r+2},
\qquad
D_j=2-2\cos\frac\pi{2j}.
\]

Using `D_j<pi^2/(4j^2)<10/(4j^2)`, one checks exactly that

\[
D_{r+2}<g_r
\]

for every row `r=2,3,4,5`.  For `r=1` there are no more distant geometries.

Thus it remains to separate `A_r` from `B_r`.

---

## 3. The periodic-near-balanced geometry lies above the separator

For `A_r=(r+1,r)`, evaluate the all-energy single-square characteristic polynomial at

\[
y=y_r
\]

and relax the seam coordinate to its maximal value `e=2`.

Set

\[
d=4t-2,
\qquad0\le t\le1.
\]

### Layers `r=1,2,3,4`

For these four layers the relaxed polynomial has degree `4r+2` in `t`, and its **entire Bernstein expansion on `[0,1]` has strictly positive rational coefficients**.

The exact minimum Bernstein coefficients are

\[
\begin{array}{c|c}
r&\min b_j\\ \hline
1&11992001/10^6\\[1mm]
2&\displaystyle
3000355798494097649/97656250000000000\\[2mm]
3&\displaystyle
8684222137009794004086689688954281/
163840000000000000000000000000000\\[2mm]
4&\displaystyle
22429083679590075805393701839013809813812541232059688475775801/
262144000000000000000000000000000000000000000000000000000000.
\end{array}
\tag{3.1}
\]

Hence

\[
P_{r+1,r}(y_r;d,2)>0
\qquad(-2\le d\le2).
\tag{3.2}
\]

### Critical layer `r=5`

At `r=5`, the polynomial itself is still strictly positive, but the one-shot Bernstein representation is too coarse near `t=1` and contains negative coefficients.  We therefore use exact dyadic Bernstein subdivision.

Recursive subdivision of `[0,1]` terminates after 14 positive intervals. Every Bernstein coefficient on every subinterval is strictly positive. The smallest exact certified coefficient is

\[
\frac{
2873967074721891749559554985500340040372057512744410503350359963749082592226318866589043780596694898296764527048101803244967623666601757400615803
}{
112944218112\,10^{132}
}>0.
\tag{3.3}
\]

Thus (3.2) holds for `r=5` as well.

For a physical phase `e<=2`,

\[
P(y_r;d,e)=P(y_r;d,2)+(2-e)>0.
\]

At the periodic reference fiber `z=1`, the squared characteristic polynomial factors into two monic degree `2r+1` factors.  For every row in (2.1), each factor and all of its derivatives through order `2r+1` are strictly positive at `y_r`. Descending derivative induction therefore excludes any reference-fiber root at or above `y_r`.

By inertia continuity around the Bloch circle,

\[
\boxed{
R_{r+1,r,q}<y_r,
\qquad
\Gamma_{r+1,r,q}>g_r.
}
\tag{3.4}

uniformly in the odd multiplier.

---

## 4. The opposite nearest orientation lies below the separator

For `B_r=(r,r+1)`, the physical fiber `z=-1` is available for every odd multiplier.  At this fiber

\[
d=-2,
\qquad e=-2.
\]

Exact substitution into the all-energy characteristic identity gives

\[
\boxed{
P_{r,r+1,-1}(y_r)<0
}
\tag{4.1}
\]

for each `r=1,...,5`.

Since `P(y)` is monic in the squared spectral variable and is positive above the top squared root, (4.1) implies that the `z=-1` fiber has a squared eigenvalue larger than `y_r`. Therefore

\[
\boxed{
\Gamma_{r,r+1,q}<g_r.
}
\tag{4.2}

For reference, the exact signs in (4.1) include

\[
r=1:\quad -41767999/10^6<0,
\]

and all later layers have strictly negative exact rational values of rapidly increasing magnitude.

---

## Theorem — exact early odd-total orientation

Combining Sections 2--4 gives, for every

\[
1\le r\le5
\]

and every compatible odd multiplier,

\[
\boxed{
(N,m)=(r+1,r)
}
\]

as the unique full-Bloch gap-maximizing two-defect geometry among all pairs `N+m=2r+1`.

Thus the first five periods

\[
p=12,20,28,36,44
\]

lie on the periodic-near-balanced side of the finite orientation transition.
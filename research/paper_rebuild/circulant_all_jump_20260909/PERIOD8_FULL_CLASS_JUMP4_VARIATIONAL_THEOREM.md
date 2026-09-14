# Full period-eight variational classification at jump four

Date: 2026-09-14

Status: **Proved**. This is a genuine enlargement of the variational class in Paper I: the optimization is over **all** legal period-eight Hamilton-gauge flux words, not only the reflection-chiral two-defect subfamily.

## 1. Setup

Consider the signed step operator with jumps `1` and `4`, in Hamilton gauge. The nearest-neighbor coefficients are `+1`, and the jump-four coefficients are a period-eight sign word

\[
\tau=(\tau_0,\ldots,\tau_7)\in\{\pm1\}^8.
\]

For a unit Bloch phase `z`, the `8 x 8` Hermitian fiber `H_tau(z)` has nearest-neighbor entries

\[
H_{j,j+1}=H_{j+1,j}=1\qquad(0\le j\le6),
\]

with seam

\[
H_{7,0}=z,\qquad H_{0,7}=\bar z,
\]

and jump-four pair entries

\[
\boxed{
H_{j,j+4}=\tau_j+\tau_{j+4}\bar z,
\qquad0\le j\le3,
}
\tag{1.1}
\]

together with their Hermitian conjugates.

Define the local flux word

\[
Q_j=\tau_j\tau_{j+1}\qquad(j\bmod8).
\]

Necessarily

\[
\prod_{j=0}^7Q_j=1.
\tag{1.2}
\]

Conversely every word satisfying (1.2) has two lifts `tau` and `-tau`. They have the same squared Bloch spectrum: if

\[
D=\operatorname{diag}(1,-1,1,-1,1,-1,1,-1),
\]

then

\[
H_{-\tau}(z)=-D H_\tau(z)D.
\]

Hence the full squared Bloch edge depends only on `Q`:

\[
R_8(Q):=\max_{|z|=1}\rho(H_\tau(z))^2.
\]

Cyclic translation and reversal of `Q` preserve `R_8`; therefore the natural equivalence is the dihedral action on the eight flux sites.

---

# Theorem A — exact full-class optimizer

Among **all** legal period-eight flux words,

\[
\boxed{
\min_Q R_8(Q)=4+\sqrt{14}<8.
}
\tag{2.1}
\]

Equality holds exactly for the single dihedral orbit represented by

\[
\boxed{
Q=(+,-,+,-,-,-,-,-),
}
\tag{2.2}
\]

i.e. the words having exactly two positive flux defects at cyclic distance two.

Equivalently, modulo translation, reflection, and the lift ambiguity, the balanced quarter-period two-defect phase is the unique period-eight optimizer at jump four.

Moreover:

* the all-negative flux word has edge exactly `8`;
* every other legal period-eight flux word has edge strictly larger than `8`.

Thus (2.2) is not merely optimal in the even-separation reflection-chiral ansatz: it is the **unique sub-eight orbit in the complete period-eight periodic class**.

---

## 2. Endpoint moment obstructions

Let

\[
H_+=H_\tau(1),\qquad H_-=H_\tau(-1).
\]

If `R_8(Q)<=8`, then every eigenvalue `lambda` of either endpoint fiber satisfies `lambda^2<=8`. Consequently

\[
\Delta_4^\pm
:=8\operatorname{tr}(H_\pm^2)-\operatorname{tr}(H_\pm^4)
=\sum_j\lambda_j^2(8-\lambda_j^2)\ge0,
\tag{3.1}
\]

and

\[
\Delta_6^\pm
:=8\operatorname{tr}(H_\pm^4)-\operatorname{tr}(H_\pm^6)
=\sum_j\lambda_j^4(8-\lambda_j^2)\ge0.
\tag{3.2}
\]

Let `d` be the number of positive sites in `Q`. Direct closed-walk expansion of the two fourth moments gives the especially simple identity

\[
\boxed{
\Delta_4^++\Delta_4^-
=32-16\sum_{j=0}^7Q_j
=160-32d.
}
\tag{3.3}
\]

Since legality forces `d` to be even, (3.3) immediately excludes

\[
d=6,8.
\]

Thus only `d=0,2,4` can survive the fourth-moment test.

---

## 3. The four-defect sector is impossible

There are eight dihedral orbits with `d=4`. For each orbit the following table records

\[
(\Delta_4^+,\Delta_6^+,\Delta_4^-,\Delta_6^-).
\]

\[
\begin{array}{c|r}
Q\text{ representative}&(\Delta_4^+,\Delta_6^+,\Delta_4^-,\Delta_6^-)\\ \hline
-+-+-+-+&(-48,-864,80,224)\\
--++--++&(-48,-1056,80,224)\\
--+-++-+&(16,64,16,-32)\\
--+-+-++&(-16,-448,48,96)\\
--+--+++&(-16,-640,48,192)\\
---++-++&(48,192,-16,-640)\\
---+-+++&(48,96,-16,-544)\\
----++++&(16,-128,16,-32)
\end{array}
\tag{4.1}
\]

Every row violates at least one necessary inequality (3.1)--(3.2). Hence no four-defect word can have full edge at most eight.

This is an exact finite orbit reduction, not a numerical spectral search: the table consists only of integer traces of the endpoint fibers.

---

## 4. The two-defect sector

For `d=2`, dihedral equivalence is determined by the cyclic distance between the two positive sites. The four orbit representatives and endpoint moment data are

\[
\begin{array}{c|c|r}
\text{distance}&Q\text{ representative}&(\Delta_4^+,\Delta_6^+,\Delta_4^-,\Delta_6^-)\\ \hline
4&---+---+&(80,224,16,-224)\\
3&----+--+&(48,96,48,288)\\
2&-----+-+&(48,192,48,192)\\
1&------++&(48,192,48,96).
\end{array}
\tag{5.1}
\]

The antipodal distance-four orbit is eliminated immediately by `Delta_6^-<0`.

Thus a hypothetical sub-eight word must be one of exactly four classes:

1. the all-negative word;
2. distance-one two-defect word;
3. distance-two two-defect word;
4. distance-three two-defect word.

The two remaining unwanted two-defect classes are killed by a single exact fiber certificate. At `z=1`,

\[
\boxed{
\det(8I-H^2)=-2^{10}
}
\tag{5.2}
\]

for the distance-one orbit, while

\[
\boxed{
\det(8I-H^2)=-2^{11}3^2
}
\tag{5.3}
\]

for the distance-three orbit.

Because `8I-H^2` is Hermitian, a negative determinant forces at least one negative eigenvalue. Hence both classes have a squared fiber eigenvalue strictly larger than eight.

The all-negative word is the alternating period-two phase displayed in an eight-cell repetition. Its full edge is exactly eight by the period-two variational theorem.

Therefore the distance-two orbit is the only possible sub-eight class.

---

## 5. Closed dispersion of the optimal orbit

Choose the representative

\[
Q_0=Q_2=+1,
\qquad Q_j=-1\quad(j\ne0,2).
\]

This is exactly the balanced `N=m=1` two-defect geometry. Put

\[
c=z+z^{-1}\in[-2,2].
\]

Specializing the all-energy single-square identity to `N=m=1` (where the two Bloch coordinates coincide, `d=e=c`) gives the squared characteristic polynomial

\[
\boxed{
\begin{aligned}
P(y,c)={}&y^4-16y^3+(84-2c^2)y^2\\
&+(-160+16c^2)y+c^4-20c^2+3c+90.
\end{aligned}}
\tag{6.1}
\]

Set

\[
X=y-4,
\qquad W=X^2.
\]

Then (6.1) becomes

\[
W^2-(12+2c^2)W+c^4+12c^2+3c+26=0.
\]

Its two roots are

\[
\boxed{
W_\pm(c)=6+c^2\pm\sqrt{10-3c}.
}
\tag{6.2}
\]

Hence the four squared branches are

\[
\boxed{
y_{\sigma,\tau}(c)
=4+\sigma\sqrt{6+c^2+\tau\sqrt{10-3c}},
\qquad \sigma,\tau\in\{\pm1\}.
}
\tag{6.3}
\]

The top branch is

\[
r(c)=4+\sqrt{f(c)},
\qquad
f(c)=6+c^2+\sqrt{10-3c}.
\]

Now

\[
f''(c)
=2-\frac{9}{4(10-3c)^{3/2}}
\ge2-\frac9{32}>0
\qquad(-2\le c\le2).
\tag{6.4}
\]

Thus `f` is strictly convex, so its maximum on `[-2,2]` is attained at an endpoint. Since

\[
f(-2)=14,
\qquad f(2)=12,
\]

we obtain

\[
\boxed{
R_8(Q)=r(-2)=4+\sqrt{14}.
}
\tag{6.5}
\]

The maximizing Bloch phase is `z=-1` (up to complex conjugation, which is the same point here).

Combining Sections 2--5 with (6.5) proves Theorem A.

---

## 6. Significance for the paper

This theorem changes the role of the smallest `2`-adic layer.

Previously the quarter-period word was known to be optimal only after imposing the reflection-chiral even-separation two-defect ansatz. At period eight and jump four, no such ansatz is needed:

\[
\boxed{
\text{the canonical two-defect word is the unique optimizer among all periodic flux words of that period.}
}
\]

This is the first theorem in the project that optimizes an explicit periodic Bloch edge over a **complete fixed-period signing class** rather than over a geometrically prescribed subfamily.

It supplies a natural base case for the next question: whether analogous full-period variational rigidity persists at periods `12,16,...`.
# Global obstruction when only one alternating bulk pair remains

Date: 2026-09-10

Status: **Proved**. This note belongs only to Paper I.

The endpoint theorem shows that every even-separation phase is sub-eight at `z=1`. The following result proves that this need not persist over the full Bloch circle when the defect arc is too long.

## Theorem A — `N=1` obstruction

Let `L>=10` be even and choose the even defect separation

\[
h=L-2.
\]

Equivalently, the complementary alternating bulk length is

\[
N=\frac{L-h}{2}=1.
\]

For any odd multiplier `2q+1`, let

\[
s=L(2q+1).
\]

Then the corresponding two-defect periodic phase is **not** globally sub-eight. In fact the antiperiodic Bloch fiber satisfies

\[
\boxed{
\rho(H_{L,q,L-2}(-1))^2
\ge \frac{11682}{1445}
=8+\frac{122}{1445}>8.
}
\tag{1.1}
\]

Hence

\[
\boxed{
\max_{|z|=1}\rho(H_{L,q,L-2}(z))^2>8.}
\tag{1.2}
\]

The lower bound is uniform in both `L` and the odd multiplier.

---

## 1. The `z=-1` block-Jacobi fiber

Use the exact general-separation block-Jacobi reduction. At

\[
z=-1,
\]

choose `eta=i`. Since `2q+1` is odd,

\[
\omega^2=z^{2q+1}=-1.
\]

Changing the square-root/gauge convention if necessary, we may take

\[
\cos\beta=0,
\qquad
\sin\beta=1.
\]

Thus the generic onsite blocks vanish and the defect onsite blocks equal

\[
2\sigma_y.
\]

For `h=L-2`, the `L`-site block chain therefore has

\[
V_0=V_{L-1}=0,
\qquad
V_j=2\sigma_y\quad(1\le j\le L-2),
\tag{1.3}
\]

interior nearest-neighbor blocks `sigma_z`, and closing block

\[
C=i\eta\sigma_y=-\sigma_y.
\tag{1.4}
\]

Let this Hermitian block matrix be denoted by `H`.

---

## 2. A finite-support exact witness

Write vectors at each block site as two-component columns. Define `v` by

\[
\begin{array}{c|c}
 j&v_j\\ \hline
0&(0,1)^T\\
1&(15i/8,0)^T\\
2&(0,1/2)^T\\
3&(15i/16,0)^T\\
L-4&(15i/16,0)^T\\
L-3&(0,1/2)^T\\
L-2&(15i/8,0)^T\\
L-1&(0,1)^T,
\end{array}
\tag{2.1}
\]

and put `v_j=0` at all other sites.

For `L>=10` the two displayed four-site pieces do not overlap. Because `H` has block range one, the quadratic form of `H^2` on this vector depends only on the displayed local pattern and is independent of `L`.

A direct exact multiplication using

\[
\sigma_y=
\begin{pmatrix}0&-i\\i&0\end{pmatrix},
\qquad
\sigma_z=
\begin{pmatrix}1&0\\0&-1\end{pmatrix}
\]

and the seam block `-sigma_y` gives

\[
\boxed{
\langle v,H^2v\rangle=\frac{5841}{64}}
\tag{2.2}
\]

and

\[
\boxed{
\langle v,v\rangle=\frac{1445}{128}.}
\tag{2.3}
\]

Therefore the Rayleigh quotient is

\[
\frac{\langle v,H^2v\rangle}{\langle v,v\rangle}
=
\frac{5841}{64}\frac{128}{1445}
=
\boxed{\frac{11682}{1445}}.
\tag{2.4}
\]

Since

\[
11682-8\cdot1445=122>0,
\]

we obtain

\[
\lambda_{\max}(H^2)
\ge\frac{11682}{1445}>8.
\]

Because `H` is Hermitian,

\[
\lambda_{\max}(H^2)=\rho(H)^2,
\]

which proves (1.1).

---

## 3. Interpretation

This theorem sharply separates two questions:

1. **endpoint:** for every even separation, `z=1` is strictly sub-eight;
2. **global Bloch circle:** a sufficiently long defect arc can create an off-endpoint state above `8`.

The obstruction already occurs in the extreme geometry with only one alternating bulk pair. Hence the general even-separation classification cannot depend on chirality alone.

The natural discrete parameter is

\[
N=\frac{L-h}{2},
\]

the number of alternating bulk pairs left after inserting the defect arc. The next threshold question is whether `N>=3` is exactly the regime in which the entire Bloch circle stays below `8`; current computation supports this and shows that `N=2` is a separate borderline family.
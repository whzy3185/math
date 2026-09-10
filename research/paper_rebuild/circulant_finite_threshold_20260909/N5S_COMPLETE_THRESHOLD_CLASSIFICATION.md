# Complete `sqrt(8)` threshold classification on `N=5s`

This note closes the second horizontal resonance family.  The theorem is finite-global: the minimum is over **all** signings of `C_(5s)(1,s)`.  No periodic/Bloch result is used.

## Main theorem

For every integer `s>=2`,

\[
\boxed{
 m(5s,s)<\sqrt8
 \iff
 s\text{ is even or }s\in\{3,5,7,9,11,13\}.
}
\tag{1}
\]

Equivalently, for odd `s`,

\[
\boxed{
 s\ge15\Longrightarrow m(5s,s)\ge\sqrt8.
}
\tag{2}
\]

The positive side of (1) is already available from the finite constructions on this branch: even `s` gives even order `5s`, while the odd values `3,5,7,9,11,13` are covered by the proved vertical step theorems.  The rest of this note proves (2).

---

# 1. Width-five flux coordinates

Write the vertices of `C_(5s)(1,s)` in the `s` chord-pentagon columns

\[
V_j=\{j,j+s,j+2s,j+3s,j+4s\},\qquad j\in\mathbb Z_s.
\]

Across each boundary `V_j--V_(j+1)` there are five elementary squares.  Their signed fluxes form a five-bit transition mask `delta_j`.  This mask is switching invariant.  We call the boundary **complement** when

\[
\delta_j=31,
\]

and a **defect** otherwise.

On a proper open interval one can switch all matching edges to `+1`.  If `eta_j` is the signed pentagon edge mask in column `j`, then

\[
\delta_j=\eta_j\oplus\eta_{j+1}.
\tag{3}
\]

Thus all open-strip lemmas proved earlier apply directly to these intrinsic flux variables.

---

# 2. A one-sided rigidity lemma

The uniform long-gap theorem rests on one fixed finite certificate.

## Lemma 2.1 (nineteen-complement half-line rigidity)

Let an open width-five strip satisfy

\[
\rho(M)^2<8.
\]

Suppose its transition word begins

\[
(x,d,31^{19}),
\qquad d\ne31,
\tag{4}
\]

where `x` is arbitrary.  Then, up to the simultaneous dihedral action `D_5` on the five row labels,

\[
\boxed{(x,d)=(31,15).}
\tag{5}
\]

The reversed statement also holds.

### Exact proof

Normalize the first pentagon state to zero.  The `32*31=992` labelled choices `(x,d)` reduce to exactly

\[
128
\]

`D_5` orbits.  For 127 of them an integer vector `w` satisfies

\[
w^T(M^2-8I)w\ge0,
\qquad w\ne0.
\tag{6}
\]

Only the canonical transition word

\[
(31,15,31^{19})
\]

is not rejected.  Since every rejected word already has squared spectral radius at least eight, (5) follows.  Reversing the strip preserves the spectrum and gives the right-handed version. `square`

The exact 128-to-1 certificate is reproduced by `verify_n5s_uniform_even_gap.py`.  Floating eigenvectors only propose integer directions; rejection is accepted only after (6) is checked in integer arithmetic.

---

# 3. Uniform exclusion of long even gaps

## Lemma 3.1 (three relative hard types)

Suppose `g>=20` is even and a sub-threshold strip contains

\[
(*,d,31^g,e,*),\qquad d,e\ne31.
\tag{7}
\]

Applying Lemma 2.1 to the leftmost 19 complement transitions forces the left external transition to be complement and, after a common `D_5` action,

\[
d=15.
\]

Applying the reversed lemma at the other end forces the right external transition to be complement and `e` to lie in the `D_5` orbit of the weight-four mask `15`.

The stabilizer of `15` in `D_5` has order two.  The five weight-four masks split into three stabilizer orbits, represented by

\[
\boxed{e=15,23,27.}
\tag{8}
\]

Geometrically these are the three possible cyclic distances `0,1,2` between the unique positive edges of the two defect masks.  Hence every putative word (7) reduces to one of

\[
W_e(g)=(31,15,31^g,e,31),
\qquad e\in\{15,23,27\}.
\tag{9}
\]

## Lemma 3.2 (explicit parametric Rayleigh witnesses)

For every even `g>=14` and every `e in {15,23,27}`, the strip `W_e(g)` satisfies

\[
\boxed{
\rho(M(W_e(g)))^2
\ge
8+\frac{4}{485g+2177}
>8.
}
\tag{10}
\]

### Proof

Put

\[
v=(1,-1,1,-1,1)^T,
\qquad
p=-13v,
\qquad
q=5v.
\tag{11}
\]

The long complement region alternates between pentagon masks `16` and `15`.  Their signed adjacency matrices satisfy

\[
C_{15}=-C_{16},
\qquad
C_{16}v=-2v,
\qquad
C_{15}v=2v.
\tag{12}
\]

Let the strip have `L=g+5` columns.  Away from the first and last eight columns define

\[
w_j=\begin{cases}
p,&j\text{ even},\\ q,&j\text{ odd}.
\end{cases}
\tag{13}
\]

At the left endpoint replace the first eight column vectors by

\[
\begin{array}{c|rrrrr}
j&w_j\\ \hline
0&-4&2&-4&2&-4\\
1&13&3&8&3&13\\
2&-17&10&-13&10&-17\\
3&7&-3&7&-3&7\\
4&-14&12&-13&12&-14\\
5&6&-5&6&-5&6\\
6&-13&13&-13&13&-13\\
7&5&-5&6&-5&5.
\end{array}
\tag{14}
\]

The entries in a row of (14) are the five coordinates of the corresponding column vector.

At the right endpoint write the vectors inward from the last column.  For `e=15` use the same eight vectors as (14).  For `e=23` use

\[
\begin{array}{c|rrrrr}
r&R^{23}_r\\ \hline
0&-2&4&-2&4&-4\\
1&-3&-8&-3&-13&13\\
2&-10&13&-10&17&-17\\
3&3&-7&3&-7&7\\
4&-12&13&-12&14&-14\\
5&5&-6&5&-6&6\\
6&-13&13&-13&13&-13\\
7&5&-6&5&-5&5,
\end{array}
\tag{15}
\]

and for `e=27` use

\[
\begin{array}{c|rrrrr}
r&R^{27}_r\\ \hline
0&-4&2&-4&4&-2\\
1&8&3&13&-13&-3\\
2&-13&10&-17&17&-10\\
3&7&-3&7&-7&3\\
4&-13&12&-14&14&-12\\
5&6&-5&6&-6&5\\
6&-13&13&-13&13&-13\\
7&6&-5&5&-5&5.
\end{array}
\tag{16}
\]

Thus `w_(L-1-r)=R^e_r` on the right.

Let

\[
Q_g=M(W_e(g))^2-8I.
\]

For an interior complement column the adjacent block of `Q_g` vanishes, while the distance-two blocks are identities and the diagonal block is `C_16^2-6I` (or the identical square of `C_15`).  By (12),

\[
(C_{16}^2-6I)v=-2v.
\]

Therefore on the baseline pattern (13)

\[
(Q_gw)_j=-2w_j+w_{j-2}+w_{j+2}=0
\tag{17}
\]

whenever the four neighboring baseline columns are present.  Inserting an additional pair `(p,q)` into the middle of the complement chain hence leaves `w^TQ_gw` unchanged.

It is consequently enough to multiply the fixed `g=14` matrices by the vectors (13)--(16).  In each of the three cases the exact integer result is

\[
w^TQ_{14}w=4,
\qquad
w^Tw=8967.
\tag{18}
\]

Every increase `g -> g+2` inserts one copy of `p` and one copy of `q`; their squared norms sum to

\[
\|p\|^2+\|q\|^2=845+125=970.
\]

Hence for every even `g>=14`,

\[
w^TQ_gw=4,
\qquad
w^Tw=8967+970\frac{g-14}{2}=485g+2177.
\tag{19}
\]

The Rayleigh quotient gives (10). `square`

## Theorem 3.3 (uniform positive-even-gap exclusion)

In a sub-`sqrt(8)` width-five strip:

- gaps `g=2,4` are excluded by the previously proved embedded gap-2/4 lemma;
- gaps `g=6,8,10,12,14` are excluded with one arbitrary transition on either side by the previous finite lemma;
- gaps `g=16,18` are covered by the exact finite extension in `N5S_WIDTH5_EVEN_GAP_16_30_RULE.md`;
- every even `g>=20` is excluded by Lemmas 3.1--3.2.

Thus **every positive even complement gap between consecutive defects is locally forbidden whenever the stated small-gap context is available**.  In particular, for every even `g>=6`, no sub-threshold strip contains

\[
(*,d,31^g,e,*).
\tag{20}
\]

---

# 4. Global odd-`s` obstruction

Assume now that `s>=15` is odd and that some signing of `C_(5s)(1,s)` has

\[
\rho(A)^2<8.
\tag{21}
\]

Let `r` be the number of defect transitions and let `g_1,...,g_r` be the cyclic complement gaps.

### No defects

If `r=0`, let `p_j` be the chord-pentagon flux in column `j`.  The product of the five square fluxes across a complement boundary is `p_jp_(j+1)=-1`, so `p_(j+1)=-p_j`.  This cannot close around odd `s`.

### One defect

If `r=1`, the fourteen-column single-defect lemma embeds properly for every `s>=15`, giving a contradiction.

### At least two defects

The thirteen-column complement rule excludes adjacent defects, so

\[
g_i\ge1.
\tag{22}
\]

Moreover

\[
s=r+\sum_i g_i.
\tag{23}
\]

If all `g_i` were odd, then the right side of (23) would have parity `r+r=0`, contradicting odd `s`.  Hence some `g_i` is even.

The gap-2/4 rule excludes `g_i=2,4`.  If an even gap satisfies

\[
6\le g_i\le s-6,
\]

then (20) occurs in a proper open interval and is impossible.  Thus any surviving even gap must satisfy

\[
g_i\ge s-5.
\tag{24}
\]

Equation (23), together with (22), now leaves only the following possibilities, up to cyclic rotation and reversal:

\[
\boxed{
(s-3,1),\qquad
(s-5,3),\qquad
(s-5,1,1).
}
\tag{25}
\]

Indeed `r>=4` is impossible from (24), while for `r=2` the other gap is an odd integer at most three and for `r=3` the other two gaps must both equal one.

For odd `s>=23`, all three patterns in (25) are excluded by the fixed defect-cluster lemmas:

- `(s-3,1)` contains `31^9,d,31,e,31^9` in a proper interval because `s-3>=20`;
- `(s-5,3)` contains `31^7,d,31^3,e,31^7` because `s-5>=18`;
- `(s-5,1,1)` contains `31^6,d,31,e,31,f,31^6` because `s-5>=18`.

The four remaining odd orders

\[
s=15,17,19,21
\]

are exactly the finite cyclic base cases proved in `N5S_BASE_15_17_GLOBAL_OBSTRUCTION.md` and `N5S_BASE_19_21_GLOBAL_OBSTRUCTION.md`.  They satisfy

\[
m(5s,s)\ge\sqrt8.
\]

This proves (2).

Combining the odd obstruction with the previously proved positive cases proves the main theorem (1). `square`

---

## Consequence

The first two horizontal resonance lines now have complete finite-global threshold classifications:

\[
N=3s:
\quad
m(3s,s)<\sqrt8
\iff s\text{ is even or }s\in\{3,5\},
\]

and

\[
N=5s:
\quad
m(5s,s)<\sqrt8
\iff s\text{ is even or }s\in\{3,5,7,9,11,13\}.
\]

The `N=5s` theorem is genuinely all-signing.  The explicit vertical constructions supply only its positive side; the negative side is obtained from intrinsic square fluxes, finite local rigidity, the uniform long-gap witness, and four exact cyclic bases.
# An antipodal sub-eight phase for every even jump

Date: 2026-09-05. This is a separate research note, not an edit of the frozen
period-eight manuscript. All assertions below have analytic proofs; the
accompanying exact verifier checks the algebra on a declared finite population.
These additions have not been formalized in Lean. External priority remains
to be investigated.

## 1. Main theorem and finite consequence

For an even integer `s>=2`, put `p=4s` and define the `p`-periodic word

\[
 \tau_i^{(s)}=
 \begin{cases}(-1)^i,&0\le i<2s,\\-(-1)^i,&2s\le i<4s.\end{cases}
\]

Its local word `Q_i=tau_i tau_(i+1)` has precisely two positive entries,
at `2s-1` and `4s-1`. This is a translate of conjecture C3's word, up to
the harmless global lift sign. Consider

\[
 (A_sx)_i=x_{i-1}+x_{i+1}+\tau_{i-s}^{(s)}x_{i-s}
                    +\tau_i^{(s)}x_{i+s}.
\]

Let `H_s(z)` be its `4s`-dimensional restriction to `x_(i+4s)=z x_i`.

**Theorem A.** For every even `s>=2`,

\[
 R_s:=\max_{|z|=1}\rho(H_s(z))^2<8.
\]

The word has primitive period `4s`. One explicit (very nonsharp) estimate is

\[
 R_s\le8-\delta_s,\qquad
 \delta_2=\frac1{32},\qquad
 \delta_s=\frac{4s^2-4}{8^{2s-1}}\quad(s\ge4\text{ even}).
\]

**Corollary A.1.** Repeating this word on `C_N(1,s)`, where `N=4sL`, gives
for either Hamilton holonomy `alpha=+1,-1` a finite signing satisfying

\[
 \rho(A_{s,L,\alpha})^2\le8-\delta_s<8.
\]

For each fixed even `s`, both of these explicit families have smaller radius
than either alternating-word signing for every such `N` satisfying

\[
 N>2\pi\sqrt{\frac{1+s^2}{\delta_s}}.
\]

The threshold is only a uniform explicit sufficient condition. At `s=2`
the much stronger period-eight exact formula and comparison threshold in
the frozen paper remain available.

This is an existence and strict-comparison theorem. It does not identify
the global minimum over all signings, or assert that `4s` is the smallest
possible sub-eight period for general `s`.

## 2. Chiral reduction and a pair of scalar chains

Write `s=2r`, so the fiber dimension is `8r`. The word obeys
`tau_(i+2s)=-tau_i`. Let `D x_i=(-1)^i x_i` and `T_(2s)x_i=x_(i+2s)`.
For a square root `xi` of `z` on the unit circle,

\[
 J=\xi^{-1}DT_{2s},\qquad J^2=I,\qquad JH_s(z)=-H_s(z)J.
\]

These identities follow by conjugating the displacement-one and
displacement-`s` terms: `s` is even, and half-cell translation negates
their chord coefficients. The two eigenspaces of `J` have dimension `2s`.
In an orthonormal adapted basis,

\[
 H_s(z)=\begin{pmatrix}0&B^*\\B&0\end{pmatrix},\qquad
 K_s(\xi)=H_s(z)^2\big|_{J=+1}=B^*B.
\]

The two squared blocks are isospectral, including zero multiplicities.
Consequently it suffices to prove that

\[
 C_s(\xi):=8I_{2s}-K_s(\xi)>0.
\]

The `J=+1` coordinates satisfy `x_(i+2s)=xi (-1)^i x_i`. Put

\[
 h=\xi+\xi^{-1}\in[-2,2],\qquad
 E_j=x_{2j},\quad O_j=x_{2j+1}\quad(0\le j<s).
\]

For `r>=2`, the following list specifies every entry of `C_s`:

* the `E` diagonal is `4-h` for `0<=j<r`, then `4+h`;
* the `O` diagonal is `4+h` for `0<=j<r`, then `4-h`;
* successive entries in each chain are `-1`;
* the seam entries are `C[E_0,E_(s-1)]=-xi^(-1)` and
  `C[O_0,O_(s-1)]=+xi^(-1)`;
* the only cross-chain entries are `C[E_0,O_(r-1)]=-2` and
  `C[E_r,O_(s-1)]=2xi^(-1)`;
* reverse entries are the complex conjugates.

To check this list, square the original range-`s` operator. Its pure
channels have displacements `2` and `2s`; its mixed channels have
displacements `s-1,s+1` and coefficients proportional to `1+Q_i`.
Only the two indicated defect sites contribute mixed terms. Replacing
each `x_(i+2s)` by `xi (-1)^i x_i` gives exactly the entries above.
In particular the reduced diagonal is `4-h(-1)^i tau_i tau_(i+s)`.
The two-step seam factors must be aggregated, rather than dropped.

When `r=1`, seam and interior edges coincide. That case is the frozen
period-eight calculation; a direct four-dimensional check is also given
in Section 7 below.

## 3. Exact determinant formula for every even jump

Define the continuants

\[
 D_{-1}(d)=0,\quad D_0(d)=1,\quad
 D_j(d)=dD_{j-1}(d)-D_{j-2}(d)=U_j(d/2).
\]

For a general squared spectral parameter `y`, set `d_-=y-4-h`,
`d_+=y-4+h` and abbreviate

\[
 a=D_{r-1}(d_-),\quad b=D_{r-1}(d_+),\quad
 c_0=D_{r-2}(d_-),\quad d_0=D_{r-2}(d_+),\quad
 e=D_r(d_-),\quad f=D_r(d_+).
\]

**Proposition B.** The squared characteristic polynomial is

\[
\begin{split}
 q_r(y,h)={}&(ef)^2-12abef+38a^2b^2-12abc_0d_0+c_0^2d_0^2\\
 &+(4h-10)b^2-(4h+10)a^2+4ab(h^2-4)-(h^2-2).
\end{split}\tag{1}
\]

More precisely,

\[
 \det(\lambda I_{4s}-H_s(z))=q_r(\lambda^2,h),
 \qquad h=\xi+\xi^{-1},\quad \xi^2=z.
\]

This expression is unchanged by `h -> -h`, so it is a polynomial in
`y` and `z+z^(-1)=h^2-2`. It describes all squared branches implicitly,
without asserting their expressibility by radicals at arbitrary `s`.

**Proof.** For `r>=2`, split the two chains into their four constant-diagonal
paths of length `r`. A path with diagonal `d` and off-diagonal `-1` has
determinant `D_r(d)`. Eliminating its `r-2` interior vertices produces the
endpoint matrix

\[
 \begin{pmatrix}D_{r-1}(d)/D_{r-2}(d)&-1/D_{r-2}(d)\\
 -1/D_{r-2}(d)&D_{r-1}(d)/D_{r-2}(d)\end{pmatrix}.
\]

At `y=8`, all these denominators are positive since `d_-,d_+>=2`.
For the polynomial identity it is enough to work first where they are
nonzero and then use polynomial continuation.

Order the endpoints as

`E_0,E_(r-1),E_r,E_(2r-1),O_0,O_(r-1),O_r,O_(2r-1)`.

Put `l=a/c_0`, `k=b/d_0`, `u=1/c_0`, `v=1/d_0`. The remaining
eight-dimensional matrix has diagonal `(l,l,k,k,k,k,l,l)` and upper entries

\[
\begin{array}{c|rrrrrrrrrr}
(i,j)&(0,1)&(2,3)&(4,5)&(6,7)&(1,2)&(5,6)&(0,3)&(4,7)&(0,5)&(2,7)\\
M_{ij}&-u&-v&-v&-u&-1&-1&-\xi^{-1}&\xi^{-1}&-2&2\xi^{-1}.
\end{array}
\]

Expanding this fixed-size determinant gives

\[
\begin{split}
 \det M={}&(l^2-u^2)^2(k^2-v^2)^2
 -12kl(l^2-u^2)(k^2-v^2)+38k^2l^2-12kl+1\\
 &-u^2v^2(h^2-2)+(4h-10)u^2k^2
 -(4h+10)v^2l^2+4uvkl(h^2-4).
\end{split}
\]

The continuant identity `D_(j)^2-D_(j-1)D_(j+1)=1` implies
`l^2-u^2=e/c_0` and `k^2-v^2=f/d_0`. Multiplication by the eliminated
interior determinant `c_0^2 d_0^2` gives (1). Chiral block decomposition
identifies this determinant with the full characteristic polynomial in
`lambda^2`. The `r=1` identity follows directly from its four-dimensional
squared block. This proves the proposition.

## 4. A positive generating function

From now on `y=8`. Put `t=4-h^2`, so `0<=t<=4`, and define

\[
 F_j(t)=D_j(4-h)D_j(4+h),\quad F_{-1}=F_{-2}=0,\qquad
 S_r(t)=F_r(t)-6F_{r-1}(t)+F_{r-2}(t).
\]

Each product is even in `h` and therefore is a polynomial in `t`.
The product of the two continuant recurrences gives the formal generating
function

\[
 \sum_{j\ge0}F_j(t)w^j
 =\frac{1-w^2}{(1-6w+w^2)^2-tw(1+w)^2}.
\tag{2}
\]

For direct verification, the denominator is
`1-(12+t)w+(38-2t)w^2-(12+t)w^3+w^4`;
`F_0=1`, `F_1=12+t`, `F_2=105+26t+t^2`, and the numerator is
`1-w^2`. The fourth-order recurrence follows either by multiplying the
two scalar recurrences or by their characteristic roots; coincident roots
are covered by polynomial continuity.

It follows that

\[
 \sum_{r\ge0}S_r(t)w^r
 =\frac{1-w^2}{1-6w+w^2}
  \sum_{j\ge0}t^j
   \left(\frac{w(1+w)^2}{(1-6w+w^2)^2}\right)^j.
\tag{3}
\]

All coefficients in the bivariate formal series on the right are
nonnegative. Indeed,

\[
 \frac1{1-6w+w^2}=\sum_{j\ge0}U_j(3)w^j,
 \qquad
 \frac{1-w^2}{1-6w+w^2}=1+\sum_{j\ge1}2T_j(3)w^j,
\]

and these coefficients are positive. In particular, for `r>=1`,

\[
 S_r(t)\ge S_r(0)=2T_r(3).
\tag{4}
\]

This coefficient argument holds for every `r`. No extrapolation from a
finite table is used.

## 5. Threshold determinant is strictly positive

The identity `ec_0=a^2-1`, and its plus counterpart, reduces (1) to

\[
 q_r(8,h)=S_r(t)^2
 -4\big((2+h)a^2+(2-h)b^2+(4-h^2)ab\big)-h^2.
\tag{5}
\]

We bound the positive square and the subtracted terms separately.
The expansion

\[
 U_n(1+x)=\sum_{j=0}^n {n+j+1\choose 2j+1}(2x)^j
\]

shows that `D_n(d)` is increasing and convex for `d>=2`. Thus
`D_(r-1)(4-h)+D_(r-1)(4+h)` is even and nondecreasing in `|h|`, and

\[
 a+b\le r+U_{r-1}(3).
\tag{6}
\]

For `r>=2`,

\[
 2T_r(3)\ge4\big(r+U_{r-1}(3)\big).
\tag{7}
\]

To see this, use `2T_r(3)=6U_(r-1)(3)-2U_(r-2)(3)`.
Inequality (7) is equivalent to
`U_(r-1)(3)-U_(r-2)(3)>=2r`. It holds at `r=2`, where the difference
is `5`. If `b_j=U_j(3)`, its increments satisfy
`(b_(j+1)-b_j)-(b_j-b_(j-1))=4b_j>=4`; induction proves the claim.

Combining (4), (6) and (7) yields `S_r(t)>=4(a+b)`.
Since `a,b>=r`, `|h|<=2`, and `0<=4-h^2<=4`, equation (5) gives

\[
\begin{split}
 q_r(8,h)
 &\ge16(a+b)^2-16(a^2+b^2+ab)-4\\
 &=16ab-4\ge16r^2-4>0\qquad(r\ge2).
\end{split}\tag{8}
\]

## 6. From a positive determinant to a spectral bound

A positive determinant alone does not establish positive definiteness.
We supply the missing inertia argument.

At `xi=i`, we have `h=0`, and every diagonal entry of `C_s` is `4`.
Each row has the two unit chain entries; four rows also have a cross entry
of modulus `2`. Therefore `C_s(i)` is Hermitian diagonally dominant.
For `r>=2`, some rows are strictly dominant and its off-diagonal graph is
connected. Its quadratic form is a sum of squared edge differences plus
the nonnegative diagonal surplus. A null vector must vanish at a strictly
dominant vertex and then, by connectivity, everywhere. Thus `C_s(i)>0`.

As `xi` ranges over the connected unit circle, `C_s(xi)` varies
continuously. Equation (8) ensures that no eigenvalue can pass through
zero. Its inertia is constant, hence `C_s(xi)>0` for all unit `xi`.

Since `K_s(xi)>=0`, the eigenvalues of `C_s(xi)` lie in `(0,8]`.
The product estimate (8) implies

\[
 \lambda_{\min}(C_s(\xi))
 \ge\frac{16r^2-4}{8^{4r-1}}
 =\frac{4s^2-4}{8^{2s-1}}.
\]

This proves Theorem A for `s>=4`. The `Q` word has primitive period `2s`,
whereas the `tau` word changes sign under translation by `2s`. Its
primitive period is therefore `4s`.

## 7. The base case and finite rings

For `s=2`, write `c=z+z^(-1)=h^2-2`. The known squared polynomial gives

\[
 q_1(8,h)=c^2-13c+38=t^2+9t+16\ge16.
\]

The four-dimensional matrix at `xi=i` has diagonal `4` and absolute
off-diagonal row sum `2+sqrt(2)<4`; hence the same inertia argument applies.
Since this squared block has order four, `delta_2=16/8^3=1/32` is valid.

On a ring of order `N=4sL`, cell translation gives the exact direct sum

\[
 A_{s,L,\alpha}\simeq\bigoplus_{z^L=\alpha}H_s(z).
\]

Every finite fiber is covered by Theorem A, proving the uniform finite
bound. For the alternating word `tau_i=(-1)^i` and even `s`, the squared
Fourier eigenvalues are

\[
 4\cos^2\theta+4\cos^2(s\theta),\qquad e^{iN\theta}=\alpha.
\]

The positive sector attains `8`. In the negative sector `theta=pi/N` is
an allowed phase, whether or not it is the maximizer. The elementary
inequality `sin^2 u<=u^2` therefore gives

\[
 \rho(A^{\rm alt}_{N,s,-})^2
 \ge8-\frac{4\pi^2(1+s^2)}{N^2}.
\]

Under the stated lower bound on `N`, this exceeds `8-delta_s`.
This proves the finite strict-comparison corollary for both alternating
holonomies, without assuming a smallest-angle maximization rule.

## 8. Interpretation and open questions

The period-eight mechanism is the first member (`s=2`) of an explicit
family for every even jump. The uniform-in-phase proof uses a fixed
eight-endpoint determinant and one positive generating function. It needs
no classification of the other sign words.

The next substantive questions are the sharp dependence of `8-R_s` on
`s`, the exact maximizing Bloch phase, and whether a shorter period can
already cross the threshold for a given jump. None is assumed in the
theorem. Odd jumps have a different alternating threshold and are not
covered by its conclusion.

AI-assisted derivation and exact symbolic checks were used to develop this
note. The proof above, rather than finite sampling, supports the all-even
quantifier. There is no claim of external independent review or Lean
verification for this extension.

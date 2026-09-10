# A two-by-two seam-response criterion for odd resonances

This note strengthens `ODD_RESONANCE_SEAM_DEFECT_FRAMEWORK.md`.  The latter writes the explicit odd-order certificate as a signed Laplacian plus two exceptional off-diagonal pairs.  Here that rank-four perturbation is reduced exactly to a `2x2` positive-definiteness test.

The argument is elementary Schur-complement linear algebra.  It is closely analogous to effective-resistance criteria for Laplacians with a small number of adverse edge perturbations, but no external theorem is needed for the result below.

## Theorem 1 (two-port seam-response reduction)

Let

\[
N=ks,
\qquad k\ge3\text{ odd},
\qquad s\ge5\text{ odd},
\]

and take the Hamilton-seam/chord-alternating signing from the general odd seam-defect theorem.  After multiplication-by-two reindexing write

\[
K:=8I-A^2=L_\Sigma+E_-+E_+,
\tag{1}
\]

where

\[
E_-=-2(e_u e_v^T+e_v e_u^T),
\qquad
u=0,
\quad
v=N-\frac{s+1}{2},
\tag{2}
\]

and

\[
E_+=2(e_p e_q^T+e_q e_p^T),
\qquad
p=\frac{N-s}{2},
\quad
q=\frac{N-1}{2}.
\tag{3}
\]

Define

\[
d_-=e_u-e_v,
\qquad
r_-=e_u+e_v,
\]

and

\[
d_+=e_p-e_q,
\qquad
r_+=e_p+e_q.
\]

Set

\[
H:=L_\Sigma+d_-d_-^T+r_+r_+^T
\tag{4}
\]

and let

\[
U:=\begin{pmatrix}r_-&d_+\end{pmatrix}.
\tag{5}
\]

Then `H` is positive definite and

\[
\boxed{K=H-UU^T.}
\tag{6}
\]

Consequently

\[
\boxed{
8I-A^2\succ0
\iff
I_2-U^TH^{-1}U\succ0.
}
\tag{7}
\]

Equivalently, writing

\[
R:=U^TH^{-1}U=
\begin{pmatrix}
r_{11}&r_{12}\\
r_{12}&r_{22}
\end{pmatrix},
\tag{8}
\]

the explicit signing is strictly sub-`sqrt(8)` if and only if

\[
\boxed{
1-r_{11}>0,
\qquad
(1-r_{11})(1-r_{22})-r_{12}^2>0.
}
\tag{9}
\]

Moreover

\[
\boxed{
\det(8I-A^2)
=
\det(H)\det(I_2-R).
}
\tag{10}
\]

### Proof

First observe the rank-one identities

\[
d_-d_-^T-r_-r_-^T
=-2(e_u e_v^T+e_v e_u^T)=E_-,
\tag{11}
\]

and

\[
r_+r_+^T-d_+d_+^T
=2(e_p e_q^T+e_q e_p^T)=E_+.
\tag{12}
\]

Substituting (11)--(12) into (1) gives (6).

It remains to justify `H>0`.  In fact `L_Sigma` itself is positive definite.  A signed Laplacian is a sum of squares

\[
x^TL_\Sigma x
=
\sum_{ij\in E}(x_i-\sigma_{ij}x_j)^2,
\tag{13}
\]

so a nonzero kernel vector can exist on a connected signed graph only if every cycle has positive flux.  Here the cycle

\[
0,1,2,\ldots,s,0
\tag{14}
\]

has negative flux.  Indeed, the `s` step-one base edges in (14) have sign `+1`, while the step-`s` edge from `0` to `s` has sign `-1`; these signs follow directly from the two-walk channel formulas in the seam-defect theorem, and none of the displayed edges crosses the Hamilton seam.  Thus `Sigma` is unbalanced and connected, whence

\[
L_\Sigma\succ0.
\tag{15}
\]

Adding the two positive semidefinite rank-one matrices in (4) preserves positive definiteness, so `H>0`.

Now factor

\[
K
=H^{1/2}\left(I-H^{-1/2}UU^TH^{-1/2}\right)H^{1/2}.
\tag{16}
\]

Put `W=H^(-1/2)U`.  The nonzero eigenvalues of `WW^T` are exactly the eigenvalues of the `2x2` matrix

\[
W^TW=U^TH^{-1}U=R.
\]

Therefore

\[
I-WW^T\succ0
\iff
I_2-R\succ0,
\]

which proves (7).  Sylvester's criterion on the `2x2` matrix gives (9).  Finally the matrix determinant lemma gives (10). `square`

---

## Corollary 1.1 (finite-global interpretation)

For the universal odd seam signing, the entire positive-side question is controlled by a two-port response matrix.  The large matrix `8I-A^2` need not be tested directly once the three numbers

\[
r_{11},\quad r_{12},\quad r_{22}
\]

are known or bounded.

This provides a conceptual replacement for the fixed-step absorber calculations.  Those local absorbers are sufficient certificates for (9); the response matrix is the exact global criterion.

---

## 2. Research direction suggested by the response matrix

Numerical reconnaissance, kept strictly at **Observed** status, shows a sharp pattern for the unmodified alternating seam signing: for tested odd `k,s`, its first response eigenvalue changes sign close to

\[
s=2k-1.
\]

For example the alternating signing is positive definite at `(k,s)=(5,9),(7,13),(9,17)` and becomes indefinite at the next odd steps `(5,11),(7,15),(9,19)`.  This is not yet a theorem.  The next analytic target is to evaluate or bound the response matrix (8) in the helical `s x k` coordinates and determine whether the sufficient region

\[
s\le2k-1
\]

can be proved uniformly.

If successful, this would replace many vertical fixed-step constructions by a single two-parameter finite theorem.
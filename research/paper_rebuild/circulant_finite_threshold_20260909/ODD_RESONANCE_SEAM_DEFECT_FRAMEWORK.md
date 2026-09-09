# A two-seam-defect framework for odd `sqrt(8)` resonances

The fixed-step theorems for steps `3,5,7,9` are manifestations of one exact finite identity.  This note isolates the reusable structure for all odd resonances.

## Theorem 1 (two-seam-defect decomposition)

Let

\[
N=ks,
\qquad
k\ge3\text{ odd},
\qquad
s\ge5\text{ odd}.
\tag{1}
\]

On `C_N(1,s)`, choose Hamilton-gauge step-one signs

\[
h_i=1\quad(0\le i<N-1),
\qquad
h_{N-1}=-1,
\tag{2}
\]

and chord signs

\[
c_i=(-1)^i,
\qquad 0\le i<N.
\tag{3}
\]

Let `A` be the resulting signed adjacency matrix and set

\[
K=8I-A^2.
\tag{4}
\]

After reindexing the vertices by

\[
\pi(j)=2j\pmod N,
\tag{5}
\]

there is an edge-signed copy `Sigma_(N,s)` of the same underlying graph `C_N(1,s)` such that

\[
\boxed{
K=L_{\Sigma_{N,s}}+E_-+E_+,
}
\tag{6}
\]

where `L_Sigma` is the signed Laplacian and the only nonzero entries of the two exceptional matrices are

\[
(E_-)_{0,\,N-(s+1)/2}
=(E_-)_{N-(s+1)/2,\,0}
=-2,
\tag{7}
\]

and

\[
(E_+)_{(N-s)/2,\,(N-1)/2}
=(E_+)_{(N-1)/2,\,(N-s)/2}
=+2.
\tag{8}
\]

Thus the explicit odd-order signing problem at `sqrt(8)` is reduced exactly to a signed-Laplacian energy plus two rank-two seam defects.

### Proof

Since `A` is 4-regular,

\[
(A^2)_{xx}=4,
\qquad
K_{xx}=4.
\tag{9}
\]

For `s>=5`, the possible nonzero off-diagonal two-walk displacements are distinct modulo `N=ks`, `k>=3`:

\[
\pm2,
\qquad
\pm2s,
\qquad
\pm(s-1),
\qquad
\pm(s+1).
\tag{10}
\]

The four positive-displacement channels are as follows.

### Step-one square channel

There is one two-walk of displacement `2`, so

\[
(A^2)_{x,x+2}=h_xh_{x+1}.
\tag{11}
\]

Using (2), this equals `+1` except for `x=N-2,N-1`, where it equals `-1`.

### Pure-chord channel

Similarly,

\[
(A^2)_{x,x+2s}=c_xc_{x+s}.
\tag{12}
\]

Because `s` is odd, this is `-1` until the canonical representative `x+s` wraps through `N`; since `N` is odd, the wrap reverses the parity comparison.  Hence

\[
c_xc_{x+s}
=
\begin{cases}
-1,&0\le x<N-s,\\
+1,&N-s\le x<N.
\end{cases}
\tag{13}
\]

### Mixed channel `s+1`

The two intermediate vertices give

\[
(A^2)_{x,x+s+1}
=h_xc_{x+1}+c_xh_{x+s}.
\tag{14}
\]

Away from the Hamilton seam the two terms cancel because `c_(x+1)=-c_x`.  Direct substitution at the seam gives exactly one survivor:

\[
(A^2)_{x,x+s+1}
=
\begin{cases}
2,&x=N-s-1,\\
0,&\text{otherwise}.
\end{cases}
\tag{15}
\]

### Mixed channel `s-1`

Likewise

\[
(A^2)_{x,x+s-1}
=h_{x-1}c_{x-1}+c_xh_{x+s-1},
\tag{16}
\]

and

\[
(A^2)_{x,x+s-1}
=
\begin{cases}
-2,&x=N-s,\\
0,&\text{otherwise}.
\end{cases}
\tag{17}
\]

Now pass from `A^2` to `K=8I-A^2`.  The displacement-2 and displacement-`2s` entries are all `+-1`; after (5) they become respectively step-one and step-`s` edges.  Together with the diagonal value `4`, they are exactly the matrix of a signed Laplacian `L_Sigma` on `C_N(1,s)`.

The survivor (15) becomes a `K`-entry `-2`.  Since

\[
2\left(N-\frac{s+1}{2}\right)
\equiv N-s-1\pmod N,
\]

its endpoints after (5) are the pair in (7).

The survivor (17) becomes a `K`-entry `+2`.  The old endpoints are `N-s` and `N-1`, which under the inverse of multiplication by `2` become

\[
\frac{N-s}{2},
\qquad
\frac{N-1}{2},
\]

proving (8).  No other off-diagonal entries occur, so (6) follows. `square`

---

## 2. Quadratic-form reformulation

For every real vector `x`,

\[
x^TKx
=
\sum_{\{i,j\}\in E(C_N(1,s))}
(x_i-\sigma_{ij}x_j)^2
-4x_0x_{N-(s+1)/2}
+4x_{(N-s)/2}x_{(N-1)/2}.
\tag{18}
\]

Consequently, proving the explicit signing strictly sub-`sqrt(8)` is equivalent to proving that the signed-edge energy absorbs the two displayed bilinear seam terms.

This is precisely what happens in the fixed-step theorems:

- `s=5`: two fixed local positive-definite absorbers after finitely many small bases;
- `s=7`: radius-two absorbers;
- `s=9`: radius-three absorbers.

The case `s=3` is a collision of the `s-1` mixed channel with the displacement-two square channel.  After combining the collided entries, only one genuine non-Laplacian `-2` edge remains; that special degeneration is treated analytically in `ODD_RESONANCE_STEP3_SUBSQRT8.md`.

---

## 3. Research consequence

For odd resonances, the remaining positive-side classification is no longer an unstructured optimization over `2^(2N)` signatures.  The explicit family (2)--(3) converts it into a finite-energy problem with only two defects whose separation is controlled by `s` while the ambient signed geometry is controlled by the chord-cycle length `k`.

This gives a concrete route toward a general `(k,s)` phase boundary: construct local or effective-resistance certificates that absorb (7)--(8), and compare their required radius with the available separation before the two seam neighborhoods interact.

# Exact vertical `sqrt(8)` threshold for step nine

The step-nine family behaves exactly like the step-seven family at the threshold: the chord-cycle-length-three point is obstructed, while every larger chord-cycle length is sub-threshold.

## Theorem 1

For every admissible integer `k>=3`,

\[
\boxed{
 m(9k,9)<\sqrt8
 \iff
 k\ge4.
}
\tag{1}
\]

The negative point is `(N,s)=(27,9)`.  The previously proved exact certificate gives

\[
m(27,9)^2\ge8+\frac2{139}>8.
\tag{2}
\]

Every even `k` is positive by the all-even-order theorem.  It remains to handle odd `k>=5`.

---

## 1. Odd-order construction and signed-Laplacian defect form

Let `N=9k`, with `k>=5` odd.  In Hamilton gauge set

\[
h_i=1\ (0\le i<N-1),
\qquad h_{N-1}=-1,
\tag{3}
\]

and choose step-nine signs

\[
c_i=(-1)^i.
\tag{4}
\]

For the resulting signed adjacency matrix `A`, put

\[
K=8I-A^2.
\]

After reindexing by multiplication by `2` on `Z_N`, exact two-walk expansion gives

\[
K=L_\Sigma+E_-+E_+,
\tag{5}
\]

where `L_Sigma` is a signed Laplacian on a signed copy of `C_N(1,9)`.  The only two non-Laplacian off-diagonal entries are

\[
(E_-)_{0,N-5}=(E_-)_{N-5,0}=-2
\tag{6}
\]

and

\[
(E_+)_{a,a+4}=(E_+)_{a+4,a}=+2,
\qquad a=\frac{N-9}{2}.
\tag{7}
\]

All other nonzero off-diagonal entries are `+-1` base edges.

---

## 2. Uniform local absorption for odd `k>=13`

Around each exceptional pair take the base-graph radius-three induced edge set.  For odd `k>=13` the two allocated edge sets are disjoint and their signed patterns no longer depend on `k`, up to relabelling.

The negative absorber has 44 vertices and 72 allocated base edges.  Exact rational `LDL^T` factorization has 44 positive diagonal pivots; its determinant is

\[
4755725738737168>0.
\tag{8}
\]

The positive absorber has 43 vertices and 68 allocated base edges.  Its exact rational `LDL^T` factorization has 43 positive diagonal pivots and determinant

\[
169914513354912>0.
\tag{9}
\]

The complete exact pivot checks are reproduced by `verify_step9_subsqrt8_local.py`.

Therefore both local exceptional forms are positive definite.  The full quadratic form is their sum plus the nonnegative signed-edge squares from all unallocated base edges.  Equality would force the local supports to zero and then propagate zero through the connected base graph.  Hence

\[
8I-A^2\succ0
\qquad(k\ge13\text{ odd}).
\tag{10}
\]

---

## 3. Exact finite odd bases `k=5,7,9,11`

For these four chord-cycle lengths the two radius-three neighborhoods overlap, so they are certified directly.  Exact rational `LDL^T` factorization of the full matrices `K=8I-A^2` has only positive pivots.  The exact determinants are

\[
\begin{array}{c|c}
k&\det(8I-A^2)\\ \hline
5&5778082039393928857600,\\
7&31457372231947501970186116635000,\\
9&56393166545984053083524808491473067473032,\\
11&87405434664864892313642576876982893413875798493048.
\end{array}
\tag{11}
\]

The script records and checks positivity of every exact LDL pivot, not only the final determinant.

Thus all odd `k>=5` are strictly sub-threshold.  Together with the even-order theorem and (2), this proves (1). `square`

---

## Corollary 1.1

The controlled vertical families now read

\[
\begin{array}{c|c}
\text{fixed step}&m(sk,s)<\sqrt8\\ \hline
3&k\ge3,\\
5&k\ge3,\\
7&k\ge4,\\
9&k\ge4.
\end{array}
\tag{12}
\]

The natural next question is whether these finite-step results are shadows of a general phase boundary in the odd `(k,s)` plane.

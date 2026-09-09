# The boundary `m(N,s)^2=6`: root quotients and exact examples

This note records the correct structural replacement for the strict sub-six defect reduction at the equality boundary.

Let

\[
A=A_\sigma,\qquad B=A^2-4I.
\]

Assume

\[
\rho(A)^2\le6.
\]

Then

\[
K:=6I-A^2=2I-B\succeq0. \tag{1}
\]

The matrix `K` is integral and has every diagonal entry equal to `2`.

## 1. Root-quotient lemma

### Lemma 1

For every signing with `rho(A)^2<=6`, there are Euclidean vectors `r_0,...,r_(N-1)` such that

\[
K_{ij}=\langle r_i,r_j\rangle,
\qquad \|r_i\|^2=2,
\]

and

\[
\langle r_i,r_j\rangle\in\{-2,-1,0,1,2\}.
\]

Moreover,

\[
|K_{ij}|=2\iff r_i=\pm r_j. \tag{2}
\]

The relation

\[
i\sim j\iff r_i=\pm r_j
\]

is therefore an equivalence relation. After switching the original signing, all roots in each equivalence class may be chosen equal. If one representative is retained from each class, its Gram matrix `K_0` satisfies

\[
(K_0)_{ii}=2,
\qquad (K_0)_{ij}\in\{0,\pm1\}\quad(i\ne j),
\qquad K_0\succeq0. \tag{3}
\]

Thus

\[
S_0:=K_0-2I
\]

is the adjacency matrix of an ordinary edge-signed graph with

\[
\lambda_{\min}(S_0)\ge-2. \tag{4}
\]

The full matrix `K` is obtained from `K_0` by duplicating roots according to the equivalence-class multiplicities.

### Proof

Positive semidefiniteness in (1) gives a Gram representation. Integrality of `K` and Cauchy--Schwarz give

\[
|K_{ij}|\le\sqrt{K_{ii}K_{jj}}=2,
\]

hence the stated five possible inner products. Equality in Cauchy--Schwarz is equivalent to parallel roots, proving (2).

For each equivalence class choose a representative root `r`. Every other root in the class is `+-r`. Switching a vertex conjugates `K` by the same diagonal `+-1` matrix that conjugates `A`, so we may reverse the signs of the antipodal roots and make the whole class equal to `r`. A principal submatrix on one representative per class then has no off-diagonal inner product of absolute value `2`, giving (3). Finally `K_0=2I+S_0` is positive semidefinite, which is exactly (4). `square`

### Corollary 1.1

If `rho(A)^2<6`, then `K` is positive definite. Therefore no two roots can be parallel, every equivalence class is a singleton, and `B` itself has only entries `0,+-1` off the diagonal. This recovers the strict-support reduction used in `SUB_SQRT6_CLASSIFICATION.md`.

At equality, by contrast, repeated roots are possible and produce entries

\[
B_{ij}=\mp2.
\]

Hence the classification of signed graphs with least eigenvalue at least `-2` cannot be applied directly to `B`; it applies only after the root quotient.

This is the conceptual reason the equality boundary is harder than the strict sub-six region.

---

## 2. Literature at the non-strict `-2` boundary

Rowlinson--Stanić, *Signed graphs whose spectrum is bounded by -2*, Applied Mathematics and Computation 423 (2022), 126991, classify connected signed graphs with smallest eigenvalue at least `-2`, using signed line graphs, star complements, and exceptional classes.

The correct future strategy for a complete `m^2=6` classification is therefore:

1. form `K=6I-A^2`;
2. quotient repeated/antipodal roots by Lemma 1;
3. apply the `lambda_min>=-2` signed-graph structure to the quotient `S_0`;
4. impose the very rigid parity-defect and two-walk lift constraints coming from `C_N(1,s)`.

Skipping Step 2 is false, as the exact `(16,3)` example below shows.

---

## 3. Four exact equality cases

### Theorem 2

\[
\boxed{
 m(12,4)^2=m(16,3)^2=m(16,5)^2=m(20,8)^2=6.
} \tag{5}
\]

### Proof: lower bounds

None of the four parameter pairs occurs in the complete strict sub-six classification. Hence Theorem A of `SUB_SQRT6_CLASSIFICATION.md` gives

\[
m(N,s)^2\ge6
\]

for all four pairs. It remains only to construct a signing of squared radius at most `6`.

### The pair `(12,4)`

Let `T` be the signed cyclic shift with `T^12=-I`, and let

\[
D=\operatorname{diag}((-1)^j).
\]

Then `DT=-TD`. For

\[
A=T+T^{-1}+DT^4+T^{-4}D,
\]

direct squaring gives

\[
B=A^2-4I=T^2+T^{-2}+T^8+T^{-8}. \tag{6}
\]

The eigenvalues of `T` are `z=e^{i\theta}` with

\[
\theta=\frac{(2k+1)\pi}{12}.
\]

Set `phi=2theta=(2k+1)pi/6`. Since `6phi` is an odd multiple of `pi`,

\[
\cos4\phi=-\cos2\phi.
\]

Thus the defect eigenvalues are

\[
\mu=2\cos\phi-2\cos2\phi.
\]

For the six possible odd multiples of `pi/6`, the maximum is exactly `2`, attained at `phi=pi/2`. Therefore `rho(A)^2=6`.

### The pair `(20,8)`

Use the same finite construction with `T^20=-I` and the alternating `D`. Then

\[
B=T^2+T^{-2}+T^{16}+T^{-16}. \tag{7}
\]

Now `phi=2theta` ranges over odd multiples of `pi/10`, and `10phi` is an odd multiple of `pi`, so

\[
\cos8\phi=-\cos2\phi.
\]

Again

\[
\mu=2\cos\phi-2\cos2\phi.
\]

The nonnegative cosine values on this finite grid are

\[
\cos\frac\pi{10},\quad \cos\frac{3\pi}{10},\quad 0.
\]

Direct substitution gives values strictly below `2` for the first two and exactly `2` for `0`. Hence `rho(A)^2=6`.

### The pair `(16,3)`

Use Hamilton gauge: all path edges

\[
01,12,\ldots,14\,15
\]

have sign `+1`, the seam `15\,0` has sign

\[
\alpha=-1,
\]

and the step-3 edge from `i` to `i+3` has sign `tau_i`, where

\[
(\tau_0,\ldots,\tau_{15})=
(-,+,-,+,-,+,-,-,+,-,+,-,-,-,+,-). \tag{8}
\]

Exact determinant expansion gives

\[
\boxed{
\chi_A(x)=x^2(x-2)(x+2)(x^2-6)^4(x^2-2)^2.
} \tag{9}
\]

Hence `rho(A)=sqrt(6)`.

This example also demonstrates why equality needs the root quotient. Its defect has exact characteristic polynomial

\[
\chi_B(x)=x^2(x-2)^8(x+2)^4(x+4)^2, \tag{10}
\]

and in Hamilton gauge it contains two off-parity entries equal to `-2`. Equivalently `K=2I-B` contains two pairs of repeated roots. After quotienting those pairs, the reduced Gram system has 14 roots and its reduced signed matrix has spectrum contained in `{-2,0,2}`.

### The pair `(16,5)`

Multiplication by `5` on `Z_16` sends

\[
\{\pm1,\pm3\}\longmapsto\{\pm5,\pm15\}=\{\pm1,\pm5\}.
\]

Therefore

\[
C_{16}(1,3)\cong C_{16}(1,5).
\]

Transporting the signing (8) through this graph isomorphism gives a signing of `C_16(1,5)` with the same characteristic polynomial, hence the same squared radius `6`.

Combining the four upper bounds with the strict sub-six lower classification proves (5). `square`

---

## 4. Status of the equality classification

Theorem 2 is **not** claimed to classify all parameter pairs with `m(N,s)^2=6`.

Current exact/finite evidence shows at least two mechanisms:

1. **duplicate-free root systems**, as in `(12,4)` and `(20,8)`, where `B` remains a genuine signed adjacency matrix at the boundary;
2. **repeated-root quotients**, as in `(16,3)` and `(16,5)`, where `B` has `+-2` entries and the non-strict signed-graph theory becomes visible only after quotienting.

A complete equality theorem should classify the possible root multiplicities and then solve the liftability of the resulting `lambda_min>=-2` signed quotient. Until that is done, all statements beyond the four exact cases above remain open.
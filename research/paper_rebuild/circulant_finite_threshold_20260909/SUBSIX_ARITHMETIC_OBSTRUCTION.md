# Sub-six support rigidity and arithmetic obstructions

This note develops a finite-global consequence of the parity defect

\[
B:=A_\sigma^2-4I.
\]

It is independent of any periodic/Bloch analysis. Throughout,

\[
2\le s<N/2,
\qquad
G=C_N(1,s),
\qquad
m(N,s)=\min_\sigma\rho(A_\sigma).
\]

## 1. Sub-six support rigidity

Recall the parity-defect trichotomy

\[
\operatorname{supp}(B\bmod2)=
\begin{cases}
\varnothing,&N=2s+2,\\
\operatorname{Cay}(\mathbb Z_N,\{\pm2\}),&N=4s,\\
\operatorname{Cay}(\mathbb Z_N,\{\pm2,\pm2s\}),&\text{otherwise}.
\end{cases} \tag{1}
\]

### Lemma 1 (sub-six support rigidity)

If a signing satisfies

\[
\rho(A_\sigma)^2<6,
\]

then every off-diagonal entry of `B` belongs to `{0,+-1}` and

\[
\boxed{
\operatorname{supp}B=\operatorname{supp}(B\bmod2).
} \tag{2}
\]

#### Proof

Put

\[
M=\lambda_{\max}(B)=\rho(A_\sigma)^2-4<2.
\]

For every pair `i!=j`, the principal submatrix of `B` on `{i,j}` is

\[
\begin{pmatrix}0&b_{ij}\\ b_{ij}&0\end{pmatrix},
\]

whose largest eigenvalue is `|b_ij|`. Interlacing gives

\[
|b_{ij}|\le M<2.
\]

Since `b_ij` is an integer, it belongs to `{0,+-1}`. If `(B mod 2)_ij=1`, then `b_ij` is odd and hence equals `+-1`; if `(B mod 2)_ij=0`, then `b_ij` is even and hence equals zero. This proves (2). ∎

Thus below squared radius six, the signing may change only the **signs** of the forced parity defects; it cannot change their support.

## 2. A cubic-moment lower bound

The following elementary matrix lemma is useful whenever the forced defect support is triangle-free.

### Lemma 2 (zero third moment)

Let `X` be a nonzero real symmetric `n x n` matrix satisfying

\[
\operatorname{tr}X=0,
\qquad
\operatorname{tr}X^3=0.
\]

Then

\[
\boxed{
\lambda_{\max}(X)^2\ge \frac{\operatorname{tr}X^2}{n}.
} \tag{3}
\]

Equality holds if and only if

\[
X^2=\lambda_{\max}(X)^2I.
\]

#### Proof

Let `M=lambda_max(X)`. Since `X` is nonzero and has trace zero, `M>0`. For every eigenvalue `mu<=M`,

\[
\frac{(M-\mu)(\mu+M)^2}{M}\ge0.
\]

Expanding gives

\[
M^2+M\mu-\mu^2-\frac{\mu^3}{M}\ge0.
\]

Summing over the spectrum and using `tr X=tr X^3=0` yields

\[
nM^2-\operatorname{tr}X^2\ge0,
\]

which is (3). Equality in the sum forces equality term by term, hence every eigenvalue belongs to `{+-M}`. This is equivalent to `X^2=M^2I`. ∎

## 3. Triangle-free forced defects imply a universal `sqrt(6)` obstruction

Away from the two collision lines in (1), define the forced parity graph

\[
\Gamma_{N,s}:=\operatorname{Cay}(\mathbb Z_N,\{\pm2,\pm2s\}). \tag{4}
\]

It is 4-regular.

### Theorem 3 (triangle-free parity obstruction)

Assume

\[
N\ne2s+2,
\qquad
N\ne4s,
\]

and suppose `Gamma_{N,s}` is triangle-free. Then

\[
\boxed{
m(N,s)^2\ge6.} \tag{5}
\]

#### Proof

Suppose for contradiction that some signing has `rho(A_sigma)^2<6`. By Lemma 1, `B` is a `{+-1}` signing of the 4-regular graph `Gamma_{N,s}`. Therefore

\[
\operatorname{tr}B^2=4N.
\]

Because the support graph is triangle-free and `B` has zero diagonal,

\[
\operatorname{tr}B^3=0.
\]

Also `tr B=0`. Lemma 2 gives

\[
\lambda_{\max}(B)^2\ge\frac{4N}{N}=4,
\]

so `lambda_max(B)>=2`. Hence

\[
\rho(A_\sigma)^2=4+\lambda_{\max}(B)\ge6,
\]

contradiction. ∎

The theorem is genuinely global: it excludes **every** signing below `sqrt(6)` whenever a parameter-dependent unsigned Cayley graph is triangle-free.

## 4. Arithmetic classification of triangles in the parity graph

Let

\[
d:=\gcd(N,2),
\qquad
q:=N/d.
\]

The graph `Gamma_{N,s}` has `d` connected components. Dividing every displacement by 2 identifies each component with a two-step circulant

\[
C_q(1,t), \tag{6}
\]

where

\[
t=\min(r,q-r),
\qquad
r\equiv s\pmod q,
\qquad
0<r<q.
\]

Under the generic assumptions `N!=2s+2,4s`, one has

\[
2\le t<q/2. \tag{7}
\]

### Lemma 4 (triangle criterion for `C_q(1,t)`)

Assume (7). Then `C_q(1,t)` contains a triangle if and only if at least one of

\[
\boxed{
t=2,\qquad q=2t+1,\qquad q=3t} \tag{8}
\]

holds.

#### Proof

A triangle based at zero gives three increments

\[
u,v,w\in\{\pm1,\pm t\}
\]

whose sum is zero modulo `q`. Since `2t<q`, classify by the number of `+-t` increments.

- Three `+-1` increments have sum in `{+-3,+-1}` and cannot vanish modulo `q`, since `q>2t>=4`.
- Two `+-1` and one `+-t` can vanish only as `t-1-1=0`, giving `t=2`; wraparound by `+-q` is impossible because `q>2t`.
- One `+-1` and two `+-t` have possible large absolute sum `2t+1`; the only admissible wraparound is `q=2t+1`.
- Three `+-t` increments can close only when `q=3t`.

Conversely, each relation in (8) visibly gives a triangle. ∎

Combining Theorem 3 and Lemma 4 gives an explicit arithmetic theorem.

### Theorem 5 (arithmetic `sqrt(6)` obstruction)

Assume

\[
N\ne2s+2,
\qquad
N\ne4s.
\]

Let `d,q,t` be as above. If

\[
\boxed{
t\ne2,\qquad q\ne2t+1,\qquad q\ne3t,} \tag{9}
\]

then

\[
\boxed{m(N,s)\ge\sqrt6.} \tag{10}
\]

## 5. Odd-order corollary

If `N` is odd, then `d=1`, `q=N`, and because `s<N/2` we have `t=s`. Hence:

### Corollary 6

For odd `N`,

\[
\boxed{
s\ne2,\quad N\ne2s+1,\quad N\ne3s
\quad\Longrightarrow\quad
m(N,s)\ge\sqrt6.} \tag{11}
\]

Thus among odd-order two-step circulants, the only parameter families not automatically excluded from the interval `[2,sqrt(6))` by the parity-defect argument are the three arithmetic triangle families

\[
s=2,\qquad N=2s+1,\qquad N=3s.
\]

This gives a structural reason for the special role of the `N=3s` resonance line: after squaring, its mandatory defect support contains triangles.

## 6. General resonance corollary for `N=ks`

The preceding theorem directly advances the `N=ks` program.

### Corollary 7 (all odd resonance ratios `k>=5`)

Let `k>=5` be odd and `s>=3`. Then

\[
\boxed{
m(ks,s)\ge\sqrt6.} \tag{12}
\]

#### Proof

The collision lines are impossible: `ks=2s+2` would give `(k-2)s=2`, and `ks=4s` would give `k=4`.

If `s` is odd, then `N=ks` is odd, so `q=ks` and `t=s`. The three triangle conditions become

\[
s=2,
\qquad
ks=2s+1,
\qquad
ks=3s,
\]

none of which is possible for odd `k>=5` and `s>=3`.

If `s` is even, then `q=ks/2`. Since `k>=5`, one has `q>2s`, so again `t=s`. The three triangle conditions become

\[
s=2,
\qquad
\frac{ks}{2}=2s+1,
\qquad
\frac{ks}{2}=3s.
\]

The first is excluded by `s>=3`; the second is `(k-4)s=2`, impossible; and the third gives `k=6`. Therefore the forced parity graph is triangle-free and Theorem 3 applies. ∎

This is a uniform theorem for every odd chord-cycle length at least five. It does **not** decide the larger `sqrt(8)` threshold for odd `ks`; it proves a universal finite-global floor `sqrt(6)`.

## 7. Defect self-similarity below six

Lemma 1 also gives a useful structural observation.

- If `N` is odd and the parameters are generic, multiplication by `2^{-1}` in `Z_N` identifies `Gamma_{N,s}` with the original underlying graph `C_N(1,s)`. Hence any hypothetical signing with squared radius below six has a defect `B` which is itself a signing of the same unsigned two-step circulant.
- If `N` is even and generic, `Gamma_{N,s}` is the disjoint union of two copies of `C_{N/2}(1,t)`.

This may be viewed as a finite **defect renormalization** under squaring. It is not, by itself, a recursive inequality for `m(N,s)`, because the extremal quantity controlling `A` is `lambda_max(B)` rather than the spectral radius of `B`. We therefore record it as structure, not as a stronger theorem.

## 8. Relation to the existing theorem package

The parity-defect mechanism now separates the finite parameter space into four structurally distinct regimes:

1. `N=2s+2`: the forced defect vanishes and the trace bound `m=2` is attainable;
2. `N=4s`: the forced defect is two cycles and the exact formula
   `m(4s,s)^2=4+2 cos(pi/(2s))` holds;
3. generic triangle-free parity support: the universal lower bound improves to `m>=sqrt(6)`;
4. generic parity support containing triangles: the remaining arithmetic families include the exceptional `sqrt(5)` cases and the difficult `N=3s` threshold line.

This organization should replace a purely case-by-case presentation in the manuscript.

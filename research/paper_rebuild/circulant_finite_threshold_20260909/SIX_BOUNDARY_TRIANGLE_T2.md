# Complete analysis of the triangle locus `t=2`

This note closes the first of the three triangle loci left by
`SIX_BOUNDARY_ARITHMETIC_LOCALIZATION.md`.

Throughout

\[
B=A_\sigma^2-4I,
\qquad
 d=\gcd(N,2),
\qquad
 q=N/d,
\qquad
 t=\min\{s,q-s\}.
\]

The flat line `N=2s+2` and the exact `N=4s` family are treated separately.

## Theorem 1 (complete `t=2` locus)

Assume `N!=2s+2`, `N!=4s`, and `t=2`.  Then

\[
\boxed{m(N,s)^2\le6}
\]

if and only if

\[
\boxed{
(N,s)\in
\{(5,2),(10,3),(12,4),(14,5),(20,8)\}.
}
\tag{1}
\]

The exact values are

\[
\begin{array}{c|c}
(N,s)&m(N,s)^2\\ \hline
(5,2),(10,3)&5,\\
(14,5)&4+\beta,\\
(12,4),(20,8)&6,
\end{array}
\tag{2}
\]

where `beta` is the largest root of `x^3-7x+7`.

In particular, within the generic `t=2` locus,

\[
\boxed{m(N,s)^2=6
\iff
(N,s)=(12,4)\text{ or }(20,8).}
\tag{3}
\]

The proof is mostly analytic.  Its key input is an exact local classification of signed `C_q(1,2)` components at index at most two.

---

# 1. Component theorem for `C_q(1,2)`

Let `C` be a signed adjacency matrix of

\[
X_q:=C_q(1,2).
\]

## Theorem 2 (index-two component classification)

For `q>=7`, a signing of `X_q` with

\[
\lambda_{\max}(C)\le2
\tag{4}
\]

exists if and only if

\[
\boxed{q\in\{7,8,9,10,12\}.}
\tag{5}
\]

For each of these five orders there is exactly one labelled switching class satisfying (4).  In that class every consecutive triangle has negative flux.  If `alpha` denotes the holonomy of the step-one Hamilton cycle after Hamilton-path switching, then

\[
\begin{array}{c|ccccc}
q&7&8&9&10&12\\ \hline
\alpha&+1&+1&-1&-1&+1.
\end{array}
\tag{6}
\]

For `q=7` its index is

\[
\beta=\max\operatorname{root}(x^3-7x+7)<2;
\]

for `q=8,9,10,12` its index is exactly `2`.

### Proof, Step 1: a five-vertex Gram obstruction

Assume (4).  Then

\[
G:=2I-C\succeq0.
\tag{7}
\]

Take any five consecutive cyclic vertices.  For `q>=7` their induced graph consists exactly of the four step-one edges and the three step-two edges.  Switch the four step-one edges to sign `+1`, and write

\[
b_0,b_1,b_2\in\{\pm1\}
\]

for the three step-two edge signs.  These are precisely the fluxes of the three consecutive triangles in this local gauge.

The determinant of the corresponding `5x5` principal submatrix of `G` is as follows:

\[
\begin{array}{c|rrrrrrrr}
(b_0,b_1,b_2)
&---&--+&-+-&-++&+--&+-+&++-&+++\\ \hline
\det G
&4&-4&0&-16&-4&-4&-16&-40.
\end{array}
\tag{8}
\]

Positive semidefiniteness leaves only

\[
---\qquad\text{or}\qquad-+-.
\tag{9}
\]

In particular the first and third triangle fluxes in every five-vertex window are negative.  Sliding the window around the cycle shows that **every consecutive triangle has negative flux**.

This table is only eight elementary `5x5` determinants; it is reproduced in `verify_t2_component_local.py`.

### Step 2: negative triangles determine the switching class up to one holonomy

Let `h_i` be the step-one edge signs and `c_i` the step-two edge signs.  Negative flux on every consecutive triangle is exactly

\[
c_i=-h_i h_{i+1}.
\tag{10}
\]

After switching a Hamilton path, let `T` be its signed cyclic shift, with

\[
T^q=\alpha I,
\qquad \alpha\in\{\pm1\}.
\]

Equation (10) gives the exact finite identity

\[
C=T+T^{-1}-T^2-T^{-2}.
\tag{11}
\]

Thus the eigenvalues are

\[
\mu(\theta)=2\cos\theta-2\cos2\theta
=2+2c-4c^2,
\qquad c=\cos\theta,
\tag{12}
\]

where

\[
\theta=\frac{2\pi k}{q}
\quad(\alpha=+1),
\qquad
\theta=\frac{(2k+1)\pi}{q}
\quad(\alpha=-1).
\tag{13}
\]

Now

\[
\mu(\theta)>2
\iff
0<\cos\theta<\frac12.
\tag{14}
\]

For `alpha=+1`, condition (14) occurs as soon as there is an integer

\[
\frac q6<k<\frac q4.
\tag{15}
\]

For `alpha=-1`, it occurs as soon as there is an odd integer `j` with

\[
\frac q3<j<\frac q2.
\tag{16}
\]

If `q>=13`, the interval in (15) has length `q/12>1` and the interval in (16) has length `q/6>2`; hence each holonomy has a forbidden Fourier point.  Therefore no signing satisfies (4).

For `7<=q<=12`, direct inspection of the finite grids (13) gives exactly the table (6):

- `q=7`: only `alpha=+1`, with index `beta<2`;
- `q=8`: only `alpha=+1`, with index `2`;
- `q=9`: only `alpha=-1`, with index `2`;
- `q=10`: only `alpha=-1`, with index `2`;
- `q=11`: neither holonomy;
- `q=12`: only `alpha=+1`, with index `2`.

This proves Theorem 2. `square`

### Order five

For later lifting we also need `q=5`.  Here `X_5=K_5`.  If a signed `K_5` with index at most `2` contained a positive triangle, switch that triangle to all positive.  The vector `(1,1,1)` on the triangle has Rayleigh quotient `2`; equality with the global upper bound would make its zero-extension a global eigenvector.  At either of the two outside vertices the eigenvalue equation would require a sum of three `+-1` numbers to vanish, which is impossible.  Thus all triangles are negative.  Such a signing is switching-equivalent to the all-negative `K_5`, whose largest eigenvalue is `1`.

Hence `K_5` also has a unique switching class of index at most two.

---

# 2. Lifting the component classification

Assume now that a signing of the original `C_N(1,s)` satisfies

\[
\rho(A)^2\le6.
\tag{17}
\]

Then every defect component has largest eigenvalue at most `2`.

The case `q=6` is the twin resonance and has already been completely settled in `SIX_BOUNDARY_TWIN_LINE.md`:

\[
m(12,4)^2=6,
\qquad
m(12,2)^2=5+\sqrt3>6.
\tag{18}
\]

We may therefore assume `q!=6`.  Since `C_q(1,2)` has twins only for `q=6`, the root-quotient lemma implies that no off-diagonal defect entry can have absolute value `2` unless its position already belongs to a collided parity channel.  In the cases below we use an explicitly non-colliding mixed channel.

## 2.1 Odd order

If `N` is odd and `t=2`, then `q=N` and `s=2`.  For `N>=7`, the mixed displacement `s-1=1` lies outside the parity support.  It therefore vanishes:

\[
h_{i-1}c_{i-1}+c_i h_{i+1}=0,
\tag{19}
\]

where `h_i` and `c_i` are the original step-one and step-two edge signs.  Multiplying (19), after rearrangement, over all `i` gives

\[
1=(-1)^N,
\]

a contradiction.  Thus every odd `N>=7` on this locus satisfies

\[
m(N,2)>\sqrt6.
\tag{20}
\]

The remaining odd case is `(5,2)`, where the already proved exact low-end theorem gives `m^2=5`.

## 2.2 Even order, original step `s=2`

Let `N=2q`, `q>=5`, and `s=2`.  Away from the already separated `(8,2)` resonance and the `q=6` twin case, the mixed channels vanish.  Equation (19) and its shift imply

\[
c_{i+2}=h_i h_{i+1}h_{i+2}h_{i+3}c_i.
\tag{21}
\]

The step-one defect edge from `i` to `i+2` has sign

\[
u_i=h_i h_{i+1},
\]

whereas its step-two defect edge from `i` to `i+4` has sign

\[
v_i=c_i c_{i+2}=u_i u_{i+2}.
\tag{22}
\]

Therefore every consecutive triangle in either reduced defect component has flux

\[
u_i u_{i+2}v_i=+1.
\tag{23}
\]

For `q>=7` this contradicts Theorem 2, which forces every such triangle to be negative.  For `q=5`, the component is `K_5` and all its triangles must likewise be negative.  The `q=6` case is excluded by (18).

Hence no generic even pair with original step `s=2` lies at or below six.

## 2.3 Even order, `s=q-2`

Let

\[
N=2q,
\qquad
s=q-2.
\tag{24}
\]

For `q>=8`, the mixed displacements `s+-1=q-3,q-1` are distinct from the parity-support displacements `+-2,+-4`.  Since `q!=6`, they vanish.  Thus

\[
c_{i+1}=-h_i h_{i+s}c_i.
\tag{25}
\]

Let

\[
\alpha:=\prod_{i=0}^{2q-1}h_i
\]

be the original Hamilton holonomy.  The step-one holonomy of either reduced parity component is also `alpha`, because

\[
\prod_{j=0}^{q-1}(h_{2j}h_{2j+1})=\alpha.
\tag{26}
\]

We now compute the triangle flux induced by (25).  Iterating it through `s=q-2` steps gives, for every `a`,

\[
c_a c_{a+s}
=(-1)^s
\prod_{k=a}^{a+s-1}h_k h_{k+s}.
\tag{27}
\]

The two intervals in the product comprise `N-4` consecutive Hamilton edges.  Taking `a=2j+4`, the four omitted signs are exactly

\[
h_{2j},h_{2j+1},h_{2j+2},h_{2j+3}.
\]

Consequently the flux of every consecutive triangle in the reduced parity component is

\[
\boxed{(-1)^q\alpha.}
\tag{28}
\]

Theorem 2 requires this flux to be `-1`, hence

\[
\alpha=(-1)^{q+1}.
\tag{29}
\]

Compare (29) with the unique admissible component holonomies (6).  For `q>=8`, compatibility occurs only at

\[
q=10,\qquad \alpha=-1.
\]

This is precisely `(N,s)=(20,8)`, for which the exact anti-periodic construction already proves

\[
m(20,8)^2=6.
\]

The cases `q=8,9,12` fail the holonomy/flux compatibility, `q=11` has no component of index at most two, and `q>=13` is excluded by Theorem 2.

The small values `q=5,7` have already been solved exactly in the low-end and order-14 analyses:

\[
m(10,3)^2=5,
\qquad
m(14,5)^2=4+\beta.
\]

Together with the `q=6` twin result (18), this proves Theorem 1. `square`

---

# 3. Consequences

The non-strict six-boundary localization originally left three triangle loci and one twin locus.  The twin locus and the complete `t=2` locus are now closed.  Therefore every still-unclassified equality pair

\[
m(N,s)^2=6
\]

must lie on one of only two reduced arithmetic resonances:

\[
\boxed{q=2t+1\qquad\text{or}\qquad q=3t.}
\tag{30}
\]

This is the new equality frontier.

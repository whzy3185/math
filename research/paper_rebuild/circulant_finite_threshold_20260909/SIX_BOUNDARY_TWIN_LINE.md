# Complete analysis of the twin resonance `q=2t+2`

This note closes one of the four arithmetic loci left by `SIX_BOUNDARY_ARITHMETIC_LOCALIZATION.md`.

Write

\[
N=4r,
\qquad
s=r+\varepsilon,
\qquad
\varepsilon\in\{-1,+1\},
\qquad r\ge3.
\tag{1}
\]

These are exactly the original parameter pairs for which the reduced parity component

\[
C_q(1,t),\qquad q=N/2,\quad t=\min(s,q-s),
\]

lies on its flat line `q=2t+2`: indeed `q=2r` and `t=r-1`.

## Theorem 1 (twin-line classification)

On the whole twin resonance (1),

\[
\boxed{
 m(N,s)^2=6
 \iff
 (N,s)\in\{(12,4),(16,3),(16,5)\}.
}
\tag{2}
\]

More precisely,

\[
\boxed{m(12,2)^2=5+\sqrt3>6,}
\tag{3}
\]

while for every `r>=5`,

\[
\boxed{m(4r,r-1)^2>6,
\qquad
m(4r,r+1)^2>6.}
\tag{4}
\]

The three equality cases in (2) were constructed exactly in `SIX_BOUNDARY_ROOT_QUOTIENT.md`.  The purpose here is to prove that there are no others on this arithmetic locus.

---

## 1. Flat-defect normal form used below

Let

\[
F=C_{2r}(1,r-1).
\]

The previously proved exact flat-rigidity theorem, applied to `F`, gives the following two consequences (they are immediate from its Hamilton-gauge normal form).

### Flat-rigidity consequences

If a signing `C` of `F` satisfies

\[
C^2=4I,
\tag{5}
\]

then:

1. the holonomy of its step-one Hamilton cycle is
   \[
   (-1)^r;
   \tag{6}
   \]
2. if `r` is odd, the step-`(r-1)` subgraph consists of two `r`-cycles, and their signed cycle fluxes are opposite.

These statements are switching-invariant consequences of the already established flat classification, not additional computational assumptions.

---

## 2. Repeated roots disappear for `r>=5`

Fix `r>=5` and suppose, for contradiction, that a signing of `C_(4r)(1,r+epsilon)` satisfies

\[
\rho(A)^2\le6.
\]

Put

\[
B=A^2-4I,
\qquad
K=6I-A^2=2I-B\succeq0.
\]

The parity graph `P=supp(B mod 2)` consists of two copies of

\[
C_{2r}(1,r-1).
\]

For `r>=5`, this reduced graph is triangle-free.  Its only nonzero translational twin period is `r`: the order-four stabilizer occurs only for `C_8(1,3)`, i.e. `r=4`.

In the original graph, twins inside one parity component are therefore separated by

\[
2r=N/2.
\tag{7}
\]

On the other hand, an off-parity-support entry of `B` can occur only in a mixed two-walk channel.  Its displacement is one of

\[
s-1,\quad s+1,
\]

namely

\[
\{r-2,r\}\quad(\varepsilon=-1),
\qquad
\{r,r+2\}\quad(\varepsilon=+1).
\tag{8}
\]

All numbers in (8) lie strictly between `0` and `2r` when `r>=5`.

If one of these mixed entries had absolute value `2`, the root lemma for `K` would force its endpoints to be twins in `P`.  This contradicts (7)--(8).  Hence every mixed entry is zero.  Since parity-support entries are odd and `|B_ij|<=2`, we obtain

\[
B_{ij}=\pm1\text{ on }P,
\qquad
B_{ij}=0\text{ off }P.
\tag{9}
\]

Thus each component `C` of `B` is a signing of the triangle-free 4-regular graph `C_(2r)(1,r-1)`.

Because `lambda_max(C)<=2`,

\[
0\le\sum_\lambda(2-\lambda)(2+\lambda)^2
=8(2r)-2\operatorname{tr}(C^2)-\operatorname{tr}(C^3)=0.
\]

Here `tr(C^2)=4(2r)` and `tr(C^3)=0`.  Every summand vanishes, so every eigenvalue of `C` is `+-2`; therefore

\[
C^2=4I.
\tag{10}
\]

We now show that (10) cannot lift from the original signed circulant.

---

## 3. Odd `r>=5`: chord-flux mismatch

Assume `r` is odd.  Then

\[
s=r\pm1
\]

is even.  Let `c_i` be the sign of the original step-`s` edge from `i` to `i+s`.

Consider the even parity component of `B`, identified with `Z_(2r)` by the vertex map `j -> 2j`.  A pure chord two-walk gives its step-`s` defect edge the sign

\[
v_j=c_{2j}c_{2j+s}.
\tag{11}
\]

Modulo `2r`, step `s=r+-1` is `+-(r-1)`, so these are exactly the edges of the step-`(r-1)` subgraph.  Since `r-1` is even, this subgraph has two `r`-cycles, indexed by the parity of `j`.

Write `s=2u`.  The two cycle fluxes are

\[
P_p=\prod_{j\equiv p\ (2)} c_{2j}c_{2(j+u)},
\qquad p=0,1.
\tag{12}
\]

If `u` is even, each product in (12) is a square and hence equals `+1`.  If `u` is odd, both products equal the same product of the two parity classes.  In either case

\[
\boxed{P_0=P_1.}
\tag{13}
\]

But (10) and the flat-rigidity consequence above require the two chord-cycle fluxes to be opposite when `r` is odd.  This contradiction proves (4) for odd `r>=5`.

---

## 4. Even `r>=6`: an antipodal two-walk obstruction

Assume `r` is even.  By (10) and the flat-rigidity holonomy (6), each parity component of `B` has step-one holonomy `+1`.

Let `h_i` be the signs of the original step-one edges.  The product of the step-one defect signs in either parity component is

\[
\prod_{j=0}^{2r-1} h_{2j}h_{2j+1}
=
\prod_{i=0}^{4r-1}h_i.
\tag{14}
\]

Hence the original Hamilton holonomy is `+1`.  Switch the original signing to Hamilton gauge; then

\[
h_i=+1\qquad\text{for every }i.
\tag{15}
\]

The mixed channels vanish by (9).  For example the displacement `s+1` equation is

\[
h_i c_{i+1}+c_i h_{i+s}=0.
\]

Using (15),

\[
c_{i+1}=-c_i,
\qquad\text{so}\qquad c_i=(-1)^i c_0.
\tag{16}
\]

Since `s=r+-1` is odd,

\[
c_i c_{i+s}=-1.
\tag{17}
\]

Therefore, on either reduced parity component `C=C_(2r)(1,r-1)`, all step-one defect edges have sign `+1` and all step-`(r-1)` defect edges have sign `-1`.

Now inspect the entry of `C^2` joining antipodal vertices `j` and `j+r`.  There are exactly four ordered two-step walks joining them, with increment pairs

\[
(1,r-1),\quad(r-1,1),\quad(-1,-(r-1)),\quad(-(r-1),-1).
\]

Each uses one positive step-one edge and one negative chord edge.  Hence

\[
(C^2)_{j,j+r}=-4,
\]

contradicting (10).  This proves (4) for even `r>=6`.

---

## 5. The two small values `r=3,4`

### `r=4`

Here the reduced parity graph is `C_8(1,3)=K_(4,4)`.  It has the exceptional order-four translation stabilizer, so the argument excluding repeated roots is no longer valid.  This is exactly the repeated-root mechanism seen in the explicit `(16,3)` signing.  The exact constructions already give

\[
m(16,3)^2=m(16,5)^2=6.
\]

### `r=3`

The pairs are `(12,2)` and `(12,4)`.  The latter has the exact finite construction

\[
m(12,4)^2=6.
\]

For `(12,2)` one can go further and determine the exact global minimum.

Put

\[
c=1+\sqrt3.
\]

Hamilton-path gauge gives exactly

\[
2^{N+1}=2^{13}=8192
\]

labelled switching classes, parametrized by the Hamilton holonomy `alpha=+-1` and the twelve chord signs.

The exact script `verify_twin_line_base_exact.py` performs an ordered-field LDL/Schur-complement test in `Q(sqrt(3))` for

\[
cI-(A^2-4I)\succeq0.
\tag{18}
\]

Exactly two gauge representatives satisfy (18).  They have `alpha=-1` and opposite chord vectors

\[
(-,+,-,+,-,+,-,+,-,+,+,-)
\]

and its negative.  For either representative, exact characteristic-polynomial expansion gives

\[
\chi_A(x)
=(x^2-2)^2(x^4-10x^2+22)^2.
\tag{19}
\]

The largest squared root of (19) is

\[
5+\sqrt3.
\]

Every other switching class makes (18) fail, hence has defect index strictly larger than `1+sqrt(3)`.  Consequently

\[
\boxed{m(12,2)^2=5+\sqrt3,}
\]

and the two displayed gauge representatives are the only labelled minimizing switching classes.

The finite computation in this paragraph is exact: no floating-point comparison is used for branch acceptance.

Combining the small cases with Sections 2--4 proves Theorem 1.  `square`

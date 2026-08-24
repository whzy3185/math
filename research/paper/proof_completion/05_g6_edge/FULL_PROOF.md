# Full Proof

Throughout, write

```text
J_6=[7905369311620327/10^15,7905369311620328/10^15]
```

for the certified rational isolating interval of `c6`.  This notation avoids
confusing that interval with equation (1), which is the bulk reciprocal
quartic below.

## 1. Bulk hyperbolicity and the essential spectrum

Let `M(y)` denote the eight-step transfer matrix of either reference bulk.
Its reciprocal characteristic polynomial is

```text
chi(z;y)=z^4+a(y)z^3+b(y)z^2+a(y)z+1,                (1)
a(y)=-2y^2+16y-13,
b(y)=y^4-16y^3+80y^2-128y+40.
```

After division by `z^2` and the substitution `w=z+z^(-1)`, equation (1)
becomes

```text
f(w;y)=w^2+(-2y^2+16y-13)w
       +y^4-16y^3+80y^2-128y+38=0.                  (2)
```

If `|z|=1`, then `w in [-2,2]`. At the endpoints,

```text
f(2;y)=y^4-16y^3+76y^2-96y+16,
f(-2;y)=(y^2-12y+34)(y^2-4y+2).                     (3)
```

The largest zero of the first polynomial is `eta`; every zero of the second
is below `eta`. Exact root geometry for (2) shows that no root enters
`[-2,2]` for `y>eta`. Hence (1) has no unit-circle multiplier there. Because
its constant term is one and its roots occur in reciprocal pairs, exactly
two multipliers lie inside and two outside the unit circle. Their spectral
subspaces, denoted `S(y)` and `U(y)`, both have algebraic dimension two.

The only multiplier collision in the interval from the upper endpoint of
`J_6` through `16` occurs at

```text
y_*=4+sqrt(627)/6,   w=95/12>2.                      (4)
```

Thus the collision is away from the unit circle and does not destroy the
stable/unstable splitting.

The direct argument in `ESSENTIAL_SPECTRUM_LEMMA.md` now applies.  It first
decouples `H_6` into two periodic half-line operators and a finite middle
block; the difference is finite rank.  A cutoff Bloch-wave Weyl sequence and
a resolvent parametrix prove that the essential spectrum of each periodic
half-line compression equals the spectrum of its whole-line bulk.  Since the
two G6 limit operators are translated and diagonally switched copies of the
same period-eight operator,

```text
sigma_ess(H_6)=sigma(H_L) union sigma(H_R)=sigma(H_ref),
sup sigma_ess(H_6)=eta.
```

Consequently every spectral point of `H_6` above `eta` is an isolated
eigenvalue of finite multiplicity.  Decomposing its eigenvector into the
`A_6` branches `+sqrt(y)` and `-sqrt(y)` proves exponential decay on both
tails and places each nonzero branch in the stable/unstable matching problem
used next.

## 2. Coordinate-free physical matching

Choose the positive unsquared branch `lambda=sqrt(y)`, choose cuts in the
left and right reference bulks, and let `D_6(lambda)` be the ordered transfer
through the finite interface core. Let `U_L(lambda)` be the two-plane of data
decaying toward `-infinity`, represented at the left cut, and let
`S_R(lambda)` be the two-plane of data decaying toward `+infinity`, represented
at the right cut. The transfer recurrence is invertible.

A nonzero bilateral solution decays at both ends if and only if its left-cut
state lies in `U_L(lambda)` and its transported right-cut state lies in
`S_R(lambda)`.
Equivalently,

```text
D_6(lambda) U_L(lambda) intersect S_R(lambda) != {0}. (5)
```

For any oriented bases `u_1,u_2` of `U_L(lambda)` and `s_1,s_2` of
`S_R(lambda)`, (5) is equivalent to

```text
E_6(lambda)=det[D_6(lambda)u_1,D_6(lambda)u_2,s_1,s_2]=0,
lambda^2=y.                                           (6)
```

Changing either basis multiplies (6) by a nonzero determinant, so its zero
set is intrinsic. This geometric condition precedes every chart choice.

Reflection exchanges the two asymptotic planes and reverses the core. It is
implemented by a unitary permutation followed, if necessary, by a diagonal
switching. Hence forward and reflected interfaces have identical spectra.
Changing the `tau` lift also preserves the squared spectrum by diagonal
conjugacy.

## 3. Realization and algebraic identification of `c6`

On the rational interval `J_6`, the stable multipliers are distinct, positive,
and uniformly separated from the unit circle. Cofactor coordinates for the
four plane vectors are nonzero throughout the interval. Exact outward
rational interval evaluation of the genuine positive-`lambda` determinant
(6) gives opposite endpoint signs, while automatic differentiation gives a
strictly positive derivative enclosure on the whole interval. The
intermediate-value theorem and the derivative test therefore give exactly
one simple physical eigenvalue `lambda_+>0` whose square lies in `J_6`.

To identify that square, symmetrize the matching determinant in the two
stable multipliers. If `S=z_1+z_2` and `P=z_1z_2`, the reciprocal relations
are

```text
S(P+1)+a(y)P=0,
P^2+S^2+1-b(y)P=0.                                   (7)
```

After eliminating `S`, write the unsquared Evans numerator as
`E_0(y,P)+lambda E_1(y,P)`. Using `lambda^2=y`, eliminate `P` from (7) and
`E_0^2-yE_1^2`. Exact factorization contains `p_6(y)^2`, and Sturm isolation
shows that `p_6` has exactly one root in `J_6`. Since the already established
physical root is in that interval, its square is `c6`.

This elimination identifies a known physical zero; by itself, a resultant
zero is only a candidate because denominators, squaring, a nonphysical
Floquet sheet, or a vanishing chart section may introduce extra factors.

## 4. Complete exclusion above `c6`

The small interval argument above proves simplicity and excludes another
positive zero through the rational upper endpoint of `J_6`. It remains to
exclude positive physical zeros in

```text
I=[7905369311620328/10^15,16].                        (8)
```

The stable plane can be written continuously in symmetric multiplier
coordinates. If `t=P+P^(-1)`, then

```text
(t+2)(t-b(y))+a(y)^2=0,                               (9)
```

and the larger real solution of (9) gives the physical branch

```text
P=2/(t+sqrt(t^2-4)),   S=-a(y)P/(P+1).                (10)
```

Formula (10) remains real and continuous through (4). A finite Grassmann
atlas covers (8): the outer intervals use cofactor section `013`, a bridge
around the sole section zero uses `012`, and the overlaps have certified
nonzero transition denominators. Thus no physical plane or matching zero is
lost at a chart transition.

Exact resultant factorization and Sturm counting give precisely two
candidate intervals in (8):

```text
[8.080985802104273,8.080985802104274],
[8.139856563339260,8.139856563339280].                (11)
```

On both intervals the genuine unsquared G6 determinant has a fixed nonzero
sign in chart `013`; an independent reconstruction obtains the same
exclusions in chart `023`. The first interval is a physical level for the
gap-two transfer, but not for `D_6`; the second is an extraneous elimination
branch. The repeated-multiplier value (4) is treated by the confluent
symmetric quotient and is not an omitted resultant candidate. Therefore no
positive G6 eigenvalue has square in (8).

The absolute row sum of `A_6` is four, so `||A_6||<=4` and
`sigma(H_6) subset [0,16]`. Equations (8)-(11) therefore complete the
positive-branch exclusion.

## 5. Rank-two symmetry and the negative branch

The G6 word obeys, for every integer `i`,

```text
Q_(6-i)=Q_i,   tau_(7-i)=-tau_i.                     (12)
```

The first identity is checked on the finite core and the four residue
classes of each periodic tail. An anchor equality and the recurrence
`tau_(i+1)=Q_i tau_i` then prove the second identity by induction in both
directions.

Define

```text
(K u)_i=(-1)^i u_(9-i).                               (13)
```

Applying (13) twice gives `K^2=-I`. Direct substitution of (12) into the
four terms of `A_6` gives

```text
K A_6=-A_6 K,
K H_6=H_6 K.                                         (14)
```

If `A_6 psi_+=sqrt(c6) psi_+`, then

```text
A_6(K psi_+)=-sqrt(c6) K psi_+.
```

The positive root is simple, and (14) makes the negative partner simple as
well. Since `A_6` is self-adjoint, the two vectors are orthogonal. Moreover,

```text
ker(H_6-c6)=ker(A_6-sqrt(c6))
             direct_sum ker(A_6+sqrt(c6)),            (15)
```

so (15) has dimension two. Any negative spectral value of `A_6` with larger
absolute value would be sent by `K` to an excluded positive value. Hence
`sup sigma(H_6)=c6`, and the theorem follows.  Exponential localization is
the conclusion of the essential-spectrum and tail-matching lemma, applied at
`y=c6>eta`.

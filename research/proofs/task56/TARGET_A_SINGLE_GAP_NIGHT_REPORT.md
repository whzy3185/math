# Task 56 Lane G: The Complete Abnormal Single-Gap Theorem

Status: `ANALYTIC_PROVED_RELATIVE_TO_THE_CERTIFIED_G6_EDGE`.

This report closes the physical single-gap hierarchy.  The quotient
involution and the order-five recurrence do not themselves select the stable
Floquet sheet.  A shorter variational argument bypasses that obstruction: six
explicit finite witnesses close the small gaps, and one fixed witness closes
every gap `g>=9`.

## 1. Convention And Necessary Scope

For an integer `g>=1`, put defects at

```text
D_g=(-4 Z_{>=0}) union {0,g} union (g+4 Z_{>=0}).
```

Set `Q_i=+1` on `D_g` and `Q_i=-1` elsewhere.  Anchor `tau_0=1` and extend

```text
tau_(i+1)=Q_i tau_i.                                      (1)
```

The bilateral signed adjacency and its square are

```text
(A_g v)_k=v_(k-1)+v_(k+1)
          +tau_(k-2)v_(k-2)+tau_k v_(k+2),
H_g=A_g^2.                                                (2)
```

The gap `g=4` is not an interface: then `D_4=4Z`, so (1) is exactly the
reference period-eight bulk.  Its squared spectral edge is

```text
eta=4+sqrt(10+2sqrt(5))<c6.
```

Thus a statement covering literally every positive `g` would be false.  In
what follows, *single gap* means an abnormal gap `g!=4`, as in the earlier
single-gap search.

The accepted Task 51 isolating interval is

```text
L=7905369311620327/10^15
  < c6 <
C=7905369311620328/10^15.                                (3)
```

Here `c6` is the unique root in `(L,C)` of

```text
16y^10-520y^9+6913y^8-48448y^7+191768y^6
-423904y^5+484528y^4-270464y^3+137856y^2
-19968y+256.                                             (4)
```

## 2. Theorem

**Theorem (complete abnormal single-gap hierarchy).**  For every integer
`g>=1`, `g!=4`, for either lift of `tau` and for either interface orientation,

```text
sup sigma(H_g)>=c6.                                      (5)
```

More precisely,

```text
sup sigma(H_6)=c6,
sup sigma(H_g)>c6  for every g not in {4,6}.              (6)
```

For `g=6`, the eigenspace of `H_6` at `c6` has rank two, not rank one.

The strict part of (6) is an analytic finite-support proof with displayed
integer arithmetic.  The equality at `g=6` uses the already accepted
computer-assisted global G6 edge theorem.

## 3. Two Elementary Reductions

Let `(Du)_i=(-1)^i u_i`.  Direct substitution in (2) gives

```text
A_(-tau)=-D A_tau D,
A_(-tau)^2=D A_tau^2 D.                                  (7)
```

Hence it suffices to use the anchor `tau_0=1`; the witness for the other lift
is `Dv`.  Reflection of the integer line is unitary and sends the forward
single gap to its reflected orientation, so it also preserves (5).

For a finitely supported integer vector `v`, evaluate (2) on the full image
window, including the two outgoing coordinates at each end.  Then

```text
<v,H_g v>/<v,v>=||A_g v||^2/||v||^2=N/D.                 (8)
```

If

```text
M=N*10^15-7905369311620328*D>0,                          (9)
```

then (3), (8), and the variational principle give
`sup sigma(H_g)>=N/D>C>c6`.

## 4. Exact Small-Gap Certificates

Coordinates in each `v` are ordered over the displayed support `I`; coordinates
in `A_gv` are ordered over `J=I+[-2,2]`.  Every line below follows by direct
substitution in (1)--(2).  The final integer is the margin `M` in (9).

### Gap 1

```text
I=[-2,3], J=[-4,5]
v   =(2,0,4,4,6,5)
A_1v=(-2,2,4,2,12,15,13,10,11,-5)
D=97, N=812,
M=45179176772828184>0.                                   (10)
```

### Gap 2

```text
I=[-4,6], J=[-6,8]
v   =(1,-1,-2,-1,-4,-5,-6,-2,1,4,2)
A_2v=(-1,0,1,0,-7,0,-14,-11,-12,-14,10,5,5,-2,2)
D=109, N=866,
M=4314745033384248>0.                                    (11)
```

### Gap 3

```text
I=[-5,8], J=[-7,10]
v   =(0,1,-1,-3,0,-6,-8,-6,-10,-6,-8,-6,1,-3)
A_3v=(0,-1,0,2,-2,-8,0,-17,-22,-18,-28,-18,-23,-16,
      -1,-5,-4,3)
D=393, N=3114,
M=7189860533211096>0.                                    (12)
```

### Gap 5

```text
I=[-2,7], J=[-4,9]
v   =(2,0,4,4,4,4,1,3,3,3)
A_5v=(-2,2,4,2,10,12,11,12,0,11,5,6,6,-3)
D=96, N=764,
M=5084546084448512>0.                                    (13)
```

### Gap 7

```text
I=[-2,9], J=[-4,11]
v   =(2,0,3,4,4,4,1,3,2,3,2,3)
A_7v=(-2,2,3,1,10,11,10,12,1,10,3,10,4,5,5,-3)
D=97, N=768,
M=1179176772828184>0.                                    (14)
```

### Gap 8

```text
I=[-8,16], J=[-10,18]
v=(4,4,4,3,-3,3,9,1,19,22,21,22,4,16,8,12,5,6,0,-4,
   -1,1,0,1,0)
A_8v=(4,0,8,11,14,8,-7,8,26,3,53,61,59,63,9,46,19,35,
      10,21,-4,-8,-3,4,1,1,1,1,0)
D=2487, N=19672,
M=11346522000244264>0.                                   (15)
```

Equations (10)--(15) prove the strict claim for every abnormal gap below
nine except `g=6`.

## 5. One Fixed Witness For Every `g>=9`

Use the same vector for every `g>=9`:

```text
I=[-2,11], J=[-4,13],
v_*=(4,0,7,8,8,9,1,7,3,6,1,4,1,2),
||v_*||^2=391.                                           (16)
```

Only `tau_i` with `-4<=i<=11` can occur in the nonzero terms of (2).
Consequently the right defect can affect this calculation only for `g=9`
or `g=10`; all `g>=11` give the same local pattern.  Direct use of (1) gives

```text
g=9:
A_gv_*=(-4,4,7,3,20,24,23,24,5,19,11,15,6,10,5,5,3,-2),
||A_gv_*||^2=3102;

g=10:
A_gv_*=(-4,4,7,3,20,24,23,24,5,19,11,15,6,10,5,5,1,-2),
||A_gv_*||^2=3094;

g>=11:
A_gv_*=(-4,4,7,3,20,24,23,24,5,19,11,15,6,10,5,5,1,2),
||A_gv_*||^2=3094.                                      (17)
```

Thus the uniform tail quotient is bounded below by

```text
3094/391=182/23,
3094*10^15-7905369311620328*391
  =3000599156451752>0.                                  (18)
```

Equations (16)--(18) prove `sup sigma(H_g)>c6` for every `g>=9`.

## 6. The G6 Equality And Completion Of The Proof

The accepted G6 global-edge proof supplies

```text
sup sigma(H_6)=c6.                                      (19)
```

Its proof chain is complete: the unsquared interval Evans determinant has one
simple positive physical root in (3); the exact symmetry

```text
(Ku)_i=(-1)^i u_(9-i),  K^2=-I,  KA=-AK,  KH=HK
```

produces the simple negative partner and hence rank two after squaring; the
global Grassmann atlas and exact resultant/Sturm audit exclude every other
physical candidate above `c6`; and `||A_6||<=4` closes the interval through
16.  This proves (19), including the corrected rank-two statement.

The cases `g=1,2,3,5,7,8` are (10)--(15), the case `g=6` is (19), and every
`g>=9` is covered by (18).  These are all positive abnormal gaps.  Equations
(7)--(8) extend the result to both lifts and both orientations.  This proves
the theorem.

For completeness, the exclusion of `g=4` is strict.  Since
`sqrt(5)<9/4` and `(191/50)^2>29/2`,

```text
eta<4+191/50=391/50<L<c6.                               (20)
```

So `g=4` cannot be inserted into the theorem.

## 7. What The Quotient Involution And Recurrence Actually Give

The Task 55 exact quotient identity is

```text
e_6(lambda,P)=P^3 e_2(-lambda,P^-1).                    (21)
```

On the physical positive bulk branch, the product of the two stable Floquet
multipliers satisfies `0<P<1`.  The map in (21) sends it to `P^-1>1`, the
unstable sheet.  Thus `sign(1-P)` is an exact sheet separator, but it reverses
under (21); the involution cannot identify the two physical Evans spectra.

For every fixed gap residue modulo eight, each exterior-square observable
satisfies

```text
d_(k+5)=U d_(k+4)-V d_(k+3)+V d_(k+2)-U d_(k+1)+d_k,
U=(y-3)(y^3-13y^2+49y-53),
V=(y-3)(3y^3-23y^2+55y-43).                             (22)
```

The reciprocal quartic in (22) has reduced discriminant

```text
(y-8)(y-4)(y-2)^2(y^2-8y+14)^2.                         (23)
```

By (3), `4<c6<8`, so (23) is negative at `c6`.  The nonconstant recurrence
modes therefore occur in complex reciprocal pairs of equal modulus.  There
is no real dominant mode from which an eventual-sign or invariant-cone proof
could follow.  This is the exact obstruction: (21) changes the physical
sheet, while (22) has no one-mode positivity at the comparison energy.

The theorem above does not pretend to repair either mechanism.  It replaces
physical root ordering by the variational inequality (8), for which compact
support makes the arbitrary tail a finite local calculation.

## 8. Consequences And Boundary

The previously open statement

```text
every abnormal physical single-gap interface has spectral top at least c6
```

is now proved, with equality at G6 and strict inequality for every other
abnormal gap.  Since the two asymptotic bulks have edge `eta<c6`, the strict
finite-support bounds also force spectrum above the essential bulk edge.

This result does **not** prove the universal finite-core `B0 -> B2` theorem,
an ordering among all non-G6 single-gap levels, simplicity of those levels,
or any multi-gap replacement principle.  The next finite lemma for the
remaining universal program should seek a bounded local witness for every
motif-free primitive multi-gap core, analogous to the fixed vector (16).

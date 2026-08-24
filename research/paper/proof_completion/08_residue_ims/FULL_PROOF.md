# Full Proof: IMS, Patch Classification, and Residue Upper Bounds

## 1. Exact discrete IMS identity

[MAIN_TEXT_REQUIRED]

Let `H` be any self-adjoint matrix and let `chi_j` be real diagonal matrices
such that `sum_j chi_j^2=I`. Entrywise,

```text
[chi,[chi,H]]_(ab)=(chi(a)-chi(b))^2 H_(ab).
```

For fixed `a,b`, the coefficient of `H_(ab)` in

```text
sum_j chi_j H chi_j + (1/2)sum_j[chi_j,[chi_j,H]]
```

is

```text
sum_j chi_j(a)chi_j(b)
 +(1/2)sum_j(chi_j(a)-chi_j(b))^2
=1.
```

Therefore

```text
H=sum_j chi_j H chi_j +(1/2)sum_j[chi_j,[chi_j,H]].     (4)
```

No limit, approximation, or boundary convention enters (4).

## 2. Cyclic tent partition and exact error

[APPENDIX_REQUIRED]

For `R>=4`, let

```text
f_R(k)=max(0,1-dist(k,0)/R)
```

on the cycle and use every cyclic translate. If `n>2R+4`, the support does
not self-collide in any range-four calculation. Direct summation gives

```text
C_R=sum_k f_R(k)^2=(2R^2+1)/(3R).
```

Set `chi_j(a)=f_R(a-j)/sqrt(C_R)`. Translation invariance gives
`sum_j chi_j(a)^2=1`.

For sites at cyclic distance `d<=4`, exact summation of the two translated
tents gives

```text
S_d(R):=sum_j(chi_j(a)-chi_j(b))^2
 =3(2d^2R-d(d^2-1))/(R(2R^2+1)).                       (5)
```

The squared step-one/step-two adjacency has range four. At distinct cyclic
offsets its absolute entries are bounded by

```text
d:                    1  2  3  4
|H_(a,a+/-d)| <=      2  1  2  1.
```

The Schur row bound for the remainder in (4) is therefore

```text
2S_1+S_2+2S_3+S_4
 =(240R-342)/(R(2R^2+1))
 <=120/R^2.                                             (6)
```

The inequality in (6) follows after multiplying by the positive denominator:
`240R-342<=120(2R^2+1)/R`, which is immediate for `R>=1`. Thus (6) is an
operator-norm estimate valid uniformly in the signing.

## 3. Local patch classification

[MAIN_TEXT_REQUIRED]

Suppose the gap word contains exactly `t in {1,2,3}` gaps equal to six and
only gaps equal to four otherwise. Let `D` be the minimum cyclic site
distance between G6 cores. If

```text
2(R+4)<D,                                               (7)
```

then the range-four enlargement of a radius-`R` tent support meets at most
one non-four gap.

If it meets none, all visible gaps are four. The local coefficient word is a
translate `B_s` of the period-eight bulk. Translation and a diagonal tree
gauge map it unitarily to the canonical bulk operator.

If it meets one gap six, translate its left endpoint to the origin. The
oriented local word is the canonical forward G6 interface or its reversal.
Reflection followed by a diagonal tree gauge maps the reversal to the
canonical reflected interface. These operations preserve the spectrum.

Finally, the ring holonomy can be represented by one step-one cut. On every
proper localization arc, successive diagonal switchings move that cut
outside the range-four enlargement. Hence the same three local classes cover
both holonomies, including arcs crossing the initially displayed cut.

Condition (7) leaves no fourth class: an enlarged support sees zero or one
non-four gap, and the two orientations of the latter are exactly the forward
and reflected models.

## 4. Fixed-interface spectral cap

[MAIN_TEXT_REQUIRED]

Let `x` be a unit vector. The reference bulk has squared edge `eta<c6`; both
G6 orientations have squared edge `c6`. The patch classification therefore
gives

```text
<chi_j x,H chi_j x> <=c6 ||chi_j x||^2
```

for every `j`. Sum this inequality, use `sum_j chi_j^2=I`, and apply (4)-(6):

```text
<x,Hx>
 <=c6+(240R-342)/(R(2R^2+1))
 <=c6+120/R^2.
```

Taking the supremum over unit vectors proves (1). This controls the full
finite-ring spectrum, not just approximate interface states.

For `D>=1040`, the separated phase-slip theorem gives exactly `2t` levels in
the fixed near-`c6` window, all satisfying

```text
|lambda-c6|<3505t(9/25)^ell,
ell=floor((floor(D/4)-12)/8).
```

The codimension-`2t` complement lies below `c6-1/200`; hence the spectral top
belongs to the cluster. This proves the optional refinement (2).

## 5. Legality of the residue constructions

[MAIN_TEXT_REQUIRED]

### Residue two

For `n=8k+2`, take `[6,4^(2k-1)]`. Its sum is

```text
6+4(2k-1)=8k+2.
```

It has `2k` positive-`Q` defects and one G6 interface. Its unique return
distance is `D=n`.

### Residue four

For `n=8k+4`, take `[6,4^(k-1),6,4^(k-1)]`. Its sum is

```text
12+8(k-1)=8k+4.
```

It has `2k` positive-`Q` defects and two G6 interfaces, with both cyclic
separations equal to `n/2`.

### Residue six

For `n=8k+6`, put

```text
a=floor((2k-3)/3),
b=floor((2k-2)/3),
c=floor((2k-1)/3).
```

Writing `2k-3=3u+v`, with `v=0,1,2`, checks directly that
`a+b+c=2k-3`. Thus the third gap word has sum

```text
18+4(a+b+c)=8k+6
```

and `2k` positive-`Q` defects. Its minimum interface separation is

```text
D=6+4 floor((2k-3)/3).
```

In all three cases, `n` and the positive-defect count `2k` are even. Since
the word has `n-2k` negative `Q` entries,

```text
product_i Q_i=(-1)^(n-2k)=1,
```

so a cyclic `tau` lift exists. A G6 interface has charge `+2` and changes the
bulk sector by two modulo four. The total shifts are therefore `2`, `4`, and
`6`, congruent respectively to `n modulo 4`. This is exactly the sector
closure condition. After the lift, either Hamilton holonomy may be chosen.

## 6. Limsup conclusion

[MAIN_TEXT_REQUIRED]

For residues `2,4,6`, the interface counts are fixed at `1,2,3`, while the
displayed minimum separations tend to infinity with `k`. Choose the largest
admissible `R`; then `R` tends to infinity. Formula (1) supplies a legal
signing with

```text
m_(8k+s)^2 <=c6+120/R(k)^2.
```

Taking the upper limit proves

```text
limsup_(k->infinity)m_(8k+s)^2<=c6,
s in {2,4,6}.
```

The direction is one-sided because only explicit competitors were
constructed. No lower bound on arbitrary minimizers has been used.

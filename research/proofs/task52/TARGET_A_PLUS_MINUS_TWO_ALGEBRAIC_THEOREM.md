# Plus/Minus-Two Algebraic Theorem

Put

```text
p(y)=16y^10-520y^9+6913y^8-48448y^7+191768y^6
     -423904y^5+484528y^4-270464y^3+137856y^2
     -19968y+256.
```

## Theorem

The G6 (`q=+2`) and gap-2 (`q=-2`) physical interface levels are two
different real roots of the same irreducible polynomial `p`. They satisfy

```text
7905369311620327/10^15 < c_(+2) < 7905369311620328/10^15 < 8,
8 < 8080985802104273/10^15 < c_(-2)
  < 8080985802104274/10^15.
```

Each displayed interval contains exactly one zero of its corresponding
Evans determinant and exactly one zero of `p`.

## Exact elimination proof

Use the Task 50 transfer order and cut. Let `z1,z2` be the two stable roots
of the period-eight monodromy. Divide the four-column matching determinant
only by the nonzero factor `(z1-z2)^2`; Task 50 proves that the stable roots
are distinct on both physical intervals. The quotient is symmetric in
`z1,z2`. Set `S=z1+z2`, `P=z1*z2`. The reciprocal bulk quartic gives

```text
S(P+1)+aP=0,
P^2+S^2+1-bP=0,
```

with the exact Task 50 polynomials `a,b`. Substitute the first relation,
split the remaining expression as `E0(y,P)+lambda E1(y,P)`, replace
`lambda^2` by `y`, and eliminate `P` between
`E0^2-y E1^2` and the second reciprocal relation.

For gaps 2 and 6 the resulting degree-108 polynomials in `y` are exactly
equal, coefficient by coefficient. Their complete irreducible
factorizations, including multiplicities, are also equal, and contain `p`
with multiplicity two. This is an exact stable-branch elimination identity,
not a numerical coincidence or PSLQ acceptance.

## Physical root selection

For gap 2, exact-rational interval evaluation gives opposite Evans signs at
the two endpoints above. Automatic interval differentiation has strictly
positive derivative throughout the interval, and every cofactor basis has
a certified nonzero pivot. Hence there is one simple physical gap-2 root.
Sturm counting gives one root of `p` in the same interval. Task 50 supplies
the corresponding statements for G6. Since the intervals are disjoint,
the two interfaces select different roots of `p`.

The proof asserts equality after exact reciprocal stable-branch elimination.
It does not assert an unproved constant conjugacy between the unsquared
matching matrices.

Machine artifact: `certificates/plus_minus_two_algebra.json`.

Status: `PLUS_MINUS_TWO_COMMON_POLYNOMIAL_PROVED`.

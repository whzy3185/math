# Complete period-eight dispersion

**Status:** analytic closure of the existing quartic calculation; independent
symbolic audit passed.  This is not counted as a separate major theorem and is
not part of the frozen Lean claim.

## 1. Four squared branches

The period-eight squared-fiber polynomial is

```text
P(y,c)
 = y^4-16y^3+(80-2c)y^2+(-128+16c)y+c^2-13c+38,
```

where `c=z+z^(-1)` lies in `[-2,2]`.  With `y=X+4`,

```text
P(X+4,c)=X^4-(16+2c)X^2+c^2+19c+38.
```

Putting `W=X^2` gives

```text
W^2-(16+2c)W+c^2+19c+38=0,
```

whose two roots are

```text
W_tau(c)=8+c+tau sqrt(26-3c),   tau in {+1,-1}.
```

Consequently all four squared branches are

```text
y_(sigma,tau)(c)=4+sigma sqrt(W_tau(c)),
sigma,tau in {+1,-1}.
```

## 2. Reality, positivity, and ordering

For `-2<=c<=2`, `26-3c` lies in `[20,32]`.  Clearly `W_+>W_-`.  To see
that the smaller root is positive, note that `8+c>0` and

```text
(8+c)^2-(26-3c)=c^2+19c+38 >= 4,
```

because the last polynomial is increasing on `[-2,2]` and has value four at
`c=-2`.  Hence

```text
0<W_-(c)<W_+(c).
```

Both are strictly increasing:

```text
W_+'(c)=1-3/(2sqrt(26-3c))>0,
W_-'(c)=1+3/(2sqrt(26-3c))>0.
```

Moreover `W_+(c)<=W_+(2)=10+2sqrt(5)<16`.  Thus every squared branch is
strictly positive.  Their order is uniform on the full Brillouin zone:

```text
y_(+,+) > y_(+,-) > y_(-,-) > y_(-,+) > 0.
```

The two `sigma=+` branches are increasing in `c`; the two `sigma=-` branches
are decreasing.

## 3. Recovery of the chiral spectrum

The chiral reduction gives

```text
det(lambda I-H(z))=P(lambda^2,c).
```

Since the four roots above are positive and distinct, the eight eigenvalues
of the Hermitian fiber are

```text
spec H(z)
 = { +sqrt(y_(sigma,tau)(c)), -sqrt(y_(sigma,tau)(c))
     : sigma,tau in {+1,-1} }.
```

Every eigenvalue is simple in a fixed fiber.  The symmetry about zero is the
spectral consequence of the chiral involution, while positivity of all four
squared branches shows that zero is absent for every unit Bloch phase.

## 4. Exact endpoint values

At `c=-2`,

```text
W_+(-2)=(2+sqrt(2))^2,
W_-(-2)=(2-sqrt(2))^2,
```

so the squared roots are

```text
6+sqrt(2), 6-sqrt(2), 2+sqrt(2), 2-sqrt(2).
```

Equivalently,

```text
P(y,-2)
 =(y-6-sqrt(2))(y-6+sqrt(2))
  (y-2-sqrt(2))(y-2+sqrt(2)).
```

At `c=2`, put

```text
a=sqrt(10+2sqrt(5)),
b=sqrt(10-2sqrt(5)).
```

Then the squared roots are

```text
4+a, 4+b, 4-b, 4-a,
```

and

```text
P(y,2)
 =(y^2-8y+6-2sqrt(5))(y^2-8y+6+2sqrt(5)).
```

There is no internal fiber degeneracy at either endpoint: the discriminants
with respect to `y` are respectively `2^20` and `8192000`, both nonzero.

For real coefficients, the fibers at `z` and `z^(-1)=conj(z)` have the same
spectrum.  Hence non-real conjugate Bloch phases give paired copies in a
finite direct sum.  At `c=2` (`z=1`) and `c=-2` (`z=-1`) the conjugate phase is
the same phase, so this phase-pair duplication collapses; it is not an
eigenvalue degeneracy inside `H(1)` or `H(-1)`.

## 5. Exact bands and visible gaps

The four squared spectral bands, written from top to bottom, are

```text
B_(+,+) = [6+sqrt(2), 4+a],
B_(+,-) = [6-sqrt(2), 4+b],
B_(-,-) = [4-b,       2+sqrt(2)],
B_(-,+) = [4-a,       2-sqrt(2)].
```

They are pairwise disjoint.  The three positive-axis gaps in the squared
problem are

```text
(2-sqrt(2), 4-b),
(2+sqrt(2), 6-sqrt(2)),
(4+b,       6+sqrt(2)).
```

The middle gap has length `4-2sqrt(2)>0`.  The other two have the same
positive separation `2+sqrt(2)-b`: indeed `b<2+sqrt(2)` follows after
squaring from

```text
10-2sqrt(5) < 6+4sqrt(2),
```

and the latter inequality is immediate from `sqrt(5)>2`.

The actual Hermitian spectrum is obtained by taking positive square roots and
their negatives.  In particular it has the exact central chiral gap

```text
(-sqrt(4-a), sqrt(4-a)).
```

These gaps are direct consequences of the closed branches; no band plot or
numerical sampling is needed in the proof.

## 6. Finite sectors revisited

The top branch is

```text
r(c)=y_(+,+)(c)=4+sqrt(8+c+sqrt(26-3c)).
```

Its strict monotonicity gives immediately:

- for `z^L=1`, the maximum is attained at `z=1`, so
  `rho(A_(8L,+))^2=4+a`;
- for `z^L=-1`, the largest phase parameter is `2cos(pi/L)`, giving the
  previously recorded exact negative-holonomy formula.

Thus the earlier top-edge theorem is the upper endpoint of a complete,
four-branch dispersion rather than an isolated root calculation.

## 7. Independent audit

Run

```text
uv run --with sympy python \
  research/paper_strengthening/verifiers/verify_full_period8_dispersion.py
```

The audit reconstructs the quartic, all four roots, the endpoint
factorizations, simplicity, derivatives, and the exact central gap endpoint.

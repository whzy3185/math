# 5. The Exact Period-Eight Spectral Edge

The rational number in Section 4 is convenient for proving strict finite
counterexamples, but it is not the true band edge. We now prove Theorem C.

## 5.1 The endpoint roots

At `c=2`, equation (4.5) becomes

```text
P(y,2)=y^4-16y^3+76y^2-96y+16.                                 (5.1)
```

Translate `y=x+4`. Then

```text
P(x+4,2)=x^4-20x^2+80.                                          (5.2)
```

Putting `w=x^2` gives `w^2-20w+80=0`, whose roots are
`10+-2sqrt(5)`. The four real roots of (5.1), in increasing order, are

```text
4-sqrt(10+2sqrt(5)),
4-sqrt(10-2sqrt(5)),
4+sqrt(10-2sqrt(5)),
4+sqrt(10+2sqrt(5)).                                             (5.3)
```

Thus the largest endpoint root is

```text
eta=4+sqrt(10+2sqrt(5)).                                        (5.4)
```

## 5.2 Sharp positivity and uniqueness

Set

```text
s=sqrt(10+2sqrt(5)),       eta=4+s,
u=y-eta,                   t=2-c.
```

Substitution in (4.5) yields the identity

```text
P(eta+u,2-t)
 =u^4+4s u^3+2u^2t+(40+12sqrt(5))u^2
  +4s ut+8sqrt(5)s u+t^2+(4sqrt(5)-3)t.                         (5.5)
```

All coefficients are positive. Hence for `u,t>=0`, the right side is
nonnegative, and it vanishes only at `u=t=0`. Since every unit-circle fiber
has `c<=2`, equation (5.5) excludes every squared eigenvalue above `eta` and
permits equality only when `c=2`.

At `c=2`, equation (5.1) has `eta` as a root, so `+-sqrt(eta)` are eigenvalues
of `H(1)`. Therefore

```text
sup_(|z|=1) rho(H(z))^2=eta.                                    (5.6)
```

On the unit circle, `z+z^(-1)=2` if and only if `z=1`. This proves both the
value and the uniqueness assertion in Theorem C. `square`

For later use we also record that `eta` has minimal polynomial

```text
Y^4-16Y^3+76Y^2-96Y+16                                         (5.7)
```

Indeed, translation `Y=X+4` reduces (5.7) to
`X^4-20X^2+80`. By Gauss's lemma, a rational factorization may be taken into
monic integral quadratics. Vanishing of the cubic and linear coefficients
reduces it either to `(X^2+a)(X^2+b)`, where
`a+b=-20` and `ab=80`, or to
`(X^2+rX+s)(X^2-rX+s)`, where `s^2=80`. The first case would make `a,b`
roots of `T^2+20T+80`, whose discriminant 80 is not a square; the second has
no rational `s`. Thus (5.7) is irreducible over `Q`. The number `eta` lies in
`(1951/250,1561/200)`; in particular `eta<8`.

## 5.3 Monotonicity of the top band

Let `r(c)` be the largest real root of `P(y,c)`. At `c=-2`,

```text
P(y,-2)=(y^2-12y+34)(y^2-4y+2),
r(-2)=6+sqrt(2)=:y_0.                                           (5.8)
```

For `-2<c<=2`, substitution gives

```text
P(y_0,c)=(c+2)(c+5-8sqrt(2))<0.                                (5.9)
```

Since `P(y,c)` tends to positive infinity with `y`, (5.9) implies
`r(c)>y_0` for `c>-2`.

Moreover,

```text
P_c(y,c)=2(c-c_0(y)),       c_0(y)=y^2-8y+13/2.                 (5.10)
```

The function `c_0` is increasing for `y>=y_0>4`, and

```text
c_0(y_0)=-7/2+4sqrt(2)>2.
```

Thus `P_c(y,c)<0` throughout `y>=y_0` and `c<=2`. If
`-2<=c_1<c_2<=2` and `y_1=r(c_1)`, then
`P(y_1,c_2)<P(y_1,c_1)=0`; hence `P(.,c_2)` has a root above `y_1`.
Therefore `r(c)` is strictly increasing on `[-2,2]`.

## 5.4 Finite holonomies

For `alpha=+1`, the finite set `z^L=1` contains `z=1`. By (5.6),

```text
rho(A_(8L,+1))^2=eta.                                           (5.11)
```

For `alpha=-1`, the admissible parameters are
`z_k=exp((2k+1)pi i/L)`. Their largest `c` value is `2cos(pi/L)`, which is
strictly less than two. The monotonicity just proved gives

```text
rho(A_(8L,-1))^2=r(2cos(pi/L))<eta.                             (5.12)
```

As `L` tends to infinity, `2cos(pi/L)` tends to two, and continuity of the
eigenvalues of the Hermitian fiber gives convergence of (5.12) to `eta`.
Thus both holonomy sectors have the same infinite-volume edge, but only the
positive sector attains it at each finite size.

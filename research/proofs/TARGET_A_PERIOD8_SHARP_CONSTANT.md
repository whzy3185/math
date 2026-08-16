# Target A: Sharp Period-8 Spectral Constant

Date: 2026-08-16

Status: **PERIOD8_SHARP_SPECTRAL_CONSTANT_PROVED**

## Theorem

Let `H(z)` be the independently audited period-8 Floquet block, with
`|z|=1` and `c=z+z^-1`. Define

```text
eta = 4 + sqrt(10+2sqrt(5)),
rho_star = sqrt(eta).
```

Then

```text
sup_(|z|=1) rho(H(z))^2 = eta,
sup_(|z|=1) rho(H(z))   = rho_star.
```

The squared band edge is attained only at `c=2`, equivalently at the unique
unit-circle Bloch parameter `z=1`.

For every integer `L>=1`, the corresponding finite blocks also satisfy:

```text
rho(A_(8L,+1))^2 = eta,
rho(A_(8L,-1))^2 = r(2cos(pi/L)) < eta,
```

where `r(c)` is the largest real root in `y` of the audited polynomial
`P(y,c)`. Moreover the second expression tends to `eta` as `L` tends to
infinity.

## Audited dependencies

The proof script pins and recomputes these frozen dependencies:

```text
cc26dedfee3fe3e6c0674f1b217fde592a043a5d8b4913752dc37ad2a62193b2  target_a_period8_independent_polynomial.json
2a5657d0791b1e1a3c742ae8e0a738f083115b4e4516e5e8d8fd4d1999d6c3ee  period8_floquet_independent_audit.json
b36bce66ec367e418e1499a1400773147d29537da92a49695b8d7dc9c1c08fa8  period8_infinite_family_independent_audit.json
```

It reconstructs `P` from the Task 38 coefficient map rather than entering a
new polynomial by hand:

```text
P(y,c)=y^4-16y^3+(80-2c)y^2+(-128+16c)y+c^2-13c+38.
```

## Endpoint derivation

At `c=2`, exact substitution gives

```text
P(y,2)=y^4-16y^3+76y^2-96y+16.
```

The automatically chosen translation `x=y-4` gives

```text
P(x+4,2)=x^4-20x^2+80.
```

Putting `w=x^2`, the equation `w^2-20w+80=0` has exact roots
`10+-2sqrt(5)`. Exact algebraic ordering of the resulting four `y` roots is

```text
4-sqrt(10+2sqrt(5)),
4-sqrt(10-2sqrt(5)),
4+sqrt(10-2sqrt(5)),
4+sqrt(10+2sqrt(5)).
```

Thus the largest endpoint root is

```text
eta=4+sqrt(10+2sqrt(5)).
```

No decimal ordering is used.

## Exact polynomial data

The minimal polynomial generated from `eta` is

```text
Y^4-16Y^3+76Y^2-96Y+16.
```

An exact Sturm certificate isolates `eta` in

```text
(1951/250,1561/200).
```

The positive square root `rho_star` has the smaller minimal polynomial

```text
R^4-2R^3-6R^2+12R-4,
```

and also satisfies the even relation obtained by replacing `Y` with `R^2`:

```text
R^8-16R^6+76R^4-96R^2+16=0.
```

Its exact isolating interval is `(2793/1000,1397/500)`.

## Sharp positivity certificate

Write

```text
s=sqrt(10+2sqrt(5)),
eta=4+s,
u=y-eta,
t=2-c.
```

Exact substitution into the audited polynomial gives

```text
P(eta+u,2-t)
 = u^4
 + 4s*u^3
 + 2u^2*t
 + (40+12sqrt(5))*u^2
 + 4s*u*t
 + 8sqrt(5)*s*u
 + t^2
 + (4sqrt(5)-3)*t.
```

All eight displayed coefficients are strictly positive and the constant
coefficient is zero. For `u,t>=0`, the expression is nonnegative. The positive
pure-`u` and pure-`t` linear terms show that equality occurs exactly when
`u=t=0`. Equivalently,

```text
P(y,c)>0 for y>=eta and c<=2,
```

except at the single point `(y,c)=(eta,2)`.

## Band-edge upper bound and attainment

For `|z|=1`, Task 38 identifies squared block eigenvalues with nonnegative
roots of `P(y,c)`, where `c in [-2,2]`. The sharp positivity certificate
excludes every root above `eta` and permits equality only at `c=2`. Hence

```text
rho(H(z))^2<=eta.
```

At `c=2`, `P(eta,2)=0`, so `+-sqrt(eta)` are eigenvalues of `H(1)` and the
upper bound is attained. On the unit circle,

```text
z+z^-1=2  iff  (z-1)^2=0,
```

so `z=1` is the unique band-edge Bloch parameter.

## Monotonicity of the top band

Let `r(c)` denote the largest real root of `P(y,c)`. At the left endpoint,

```text
P(y,-2)=(y^2-12y+34)(y^2-4y+2),
r(-2)=y0=6+sqrt(2).
```

Substituting `y0` gives

```text
P(y0,c)=(c+2)(c+5-8sqrt(2)).
```

For `-2<c<=2`, the first factor is positive while the second is at most
`7-8sqrt(2)<0`. Thus `P(y0,c)<0`, and the positive leading coefficient in `y`
forces at least one root above `y0`. Therefore `r(c)>y0` for `c>-2`.

Next,

```text
P_c(y,c)=2c-2y^2+16y-13=2(c-c0(y)),
c0(y)=y^2-8y+13/2.
```

Since `y0>4`, `c0` is increasing for `y>=y0`, and

```text
c0(y0)=-7/2+4sqrt(2)>2.
```

Hence `P_c(y,c)<0` throughout `y>=y0, c<=2`. If
`-2<=c1<c2<=2` and `y1=r(c1)`, then

```text
P(y1,c2)<P(y1,c1)=0.
```

Again using `P(y,c2)->+infinity` as `y->+infinity`, there is a root above
`y1`. Consequently `r(c2)>r(c1)`, so the top band is strictly increasing on
`[-2,2]`.

## Finite alpha=+1 consequence

For `alpha=+1`, the admissible relation `z^L=1` always includes `z=1`.
Strict monotonicity of `r(c)` and `c<=2` therefore give, for every `L>=1`,

```text
rho(A_(8L,+1))^2=eta,
rho(A_(8L,+1))=sqrt(eta).
```

This is exact finite-size attainment, not merely an infinite-volume limit.

## Finite alpha=-1 consequence

For `alpha=-1`, the admissible parameters are

```text
z_k=exp(i(2k+1)pi/L).
```

Their largest `c=z+z^-1` value is `2cos(pi/L)`, attained at the parameters
with angles `+-pi/L`. Strict top-band monotonicity gives

```text
rho(A_(8L,-1))^2=r(2cos(pi/L))<eta
```

for every finite `L`.

## Infinite-volume limit

As `L` tends to infinity, `2cos(pi/L)` tends to 2. The matrix entries of
`H(exp(i theta))` depend continuously on `theta`, and the spectral radius of a
Hermitian matrix is continuous in its entries. Equivalently, the endpoint top
root is simple because

```text
P_y(eta,2)=8sqrt(50+10sqrt(5))>0.
```

Therefore

```text
lim_(L->infinity) rho(A_(8L,-1))^2=eta.
```

Both holonomies share the same infinite-volume sharp constant, but only
`alpha=+1` attains it at every finite size.

## Comparison with the rational certificate

The exact difference is

```text
1561/200-eta=761/200-sqrt(10+2sqrt(5))>0.
```

The Sturm interval above proves this strict comparison without decimals.
Thus `1561/200` is a convenient strict rational certificate but not the sharp
period-8 constant.

For diagnostics only,

```text
eta      = 7.8042260651806142885...,
rho_star = 2.7936044933348411065....
```

## Scope boundary

This theorem concerns one audited period-8 phase. It does not prove that the
phase is optimal among period-8 patterns, globally optimal among all periodic
patterns, or globally optimal over all signings. It also does not imply that
all sufficiently large even orders fail.

## Independent checker

`verify_target_a_period8_sharp_constant.py` reads the three frozen dependencies
and the machine result without recomputing the Floquet determinant. It verifies
dependency hashes, endpoint root ordering, both minimal polynomials, the sharp
coefficient map and equality condition, band-edge uniqueness, top-root
monotonicity, both finite holonomy consequences, the limit certificate, and
the exact comparison with `1561/200`. Its final output is

```text
TARGET_A_PERIOD8_SHARP_CONSTANT_PASS
```

## Evidence

```text
b83879735be6641b82b4ab032b825e06ea999ba23d83eaa141f0557c3b1e0c3e  research/scripts/target_a_period8_sharp_constant.py
04aadb96462b3cd7febe75887cacdffffbbcd1c8d7b641dec80489994cbe049b  research/scripts/verify_target_a_period8_sharp_constant.py
f742f79d804f3c44da18dcb4b6562d4d7d1eb75e9f631133bc7314c475dbaa63  research/proofs/target_a_period8_sharp_constant.json
```

## Conclusion

`PERIOD8_SHARP_SPECTRAL_CONSTANT_PROVED`

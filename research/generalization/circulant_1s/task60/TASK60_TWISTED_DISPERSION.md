# Task 60 Twisted Dispersion

Define

```text
f_s(theta)=4+2cos(2theta)+2(-1)^s cos(2s theta).
```

The parity split is exact:

```text
s even: f_s(theta)=4cos^2(theta)+4cos^2(s theta),
s odd:  f_s(theta)=4cos^2(theta)+4sin^2(s theta).
```

## Even chord length

The continuous maximum is `8`, attained only at `theta=0 (mod pi)`.
Therefore the periodic sector has squared radius exactly `8`, while the
antiperiodic sector is strictly below `8` at every admissible even order.
Consequently `alpha=-1` is the better alternating-flux sector for every even
`s`, although its finite maximum need not occur at the smallest angle for
small `N`. For example,

```text
s=4, N=12, alpha=-1: rho_tw^2=6,
```

and the maximizing grid point is not `theta=pi/N`.

## Odd chord length

Put `x=2theta`. On `[0,pi]`,

```text
F_s(x)=4+2cos x-2cos(sx).
```

For odd `s>=3`, its unique global maximizer in the first half-period is the
point

```text
x_s in (pi/(2s),pi/s),
s sin(s x_s)=sin x_s.
```

To prove uniqueness, set `y=sx`. The ratio
`sin(y)/sin(y/s)` is strictly decreasing on `(0,pi)` because `z cot z` is
strictly decreasing; it crosses `1/s` once. Points with `x>=pi/s` cannot
beat `F_s(pi/s)`, while the derivative changes from positive to negative
before that endpoint.

Equivalently, `z_s=cos x_s` is the distinguished root of

```text
s U_(s-1)(z)-1=0
```

in `(cos(pi/s),cos(pi/(2s)))`, and the continuous squared threshold is

```text
M_s=4+2z_s-2T_s(z_s)<8.
```

The maximum is interior, so the `s=2` smallest-angle rule does not extend to
odd `s`.

For `s=3`, `z_3=1/sqrt(3)` and

```text
M_3=4+16/(3sqrt(3)).
```

## No uniform odd-`s` holonomy

The better finite grid depends on arithmetic alignment with the interior
maximizer. Exact examples for `s=3` are

| `N` | periodic `alpha=+1` | antiperiodic `alpha=-1` | better sector |
|---:|---:|---:|---|
| 8 | `4` | `4+2sqrt(2)` | periodic |
| 12 | `7` | `4+sqrt(3)` | antiperiodic |
| 18 | `<7` | `7` | periodic |

Thus no holonomy choice is uniformly best for odd `s`.

## Collision corollaries

If `N=2s+2`, then `T^(2s)=alpha T^(-2)` and

```text
A^2=4I+(1+(-1)^s alpha)(T^2+T^(-2)).
```

Choosing `alpha=-(-1)^s` gives the flat identity `A^2=4I`. If `N=4s` and
`alpha=-1`, the two `2s` chord channels cancel each other. These are exact
finite-ring effects, not failures of the universal operator formula.

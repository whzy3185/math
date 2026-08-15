# Target A: Period-10 Counterexample Family

Date: 2026-08-15

Evidence status: **Proved**, subject to independent human audit.

## Theorem

For every integer `L>=5`, let `n=10L`.  On `C_n(1,2)`, choose triangle
fluxes with period 10

`tau = (+,+,-,+,-,-,+,-,+,-)`

and either Hamilton-cycle holonomy `alpha=+1` or `alpha=-1`.  Then the
resulting signing satisfies

`rho(A)^2 < 198/25 < rho_-(n)^2`.

Consequently Conjecture 3 of *Signed circulants at the Ramanujan bound* is
false.  This gives an infinite family of counterexamples for every multiple
of 10 with `n>=50`.

The corresponding quadrilateral flux period is

`Q = (+,-,-,-,+,-,-,-,-,-)`,

so the defects occur at residues `0,4 mod 10`.

## Floquet reduction

After switching the step-1 edges into the Hamilton-cycle gauge, work with
the twisted boundary condition `x_(i+n)=alpha*x_i`.  The operator is

`(Ax)_i = x_(i-1)+x_(i+1)+tau_(i-2)x_(i-2)+tau_i*x_(i+2)`.

Because `tau` has period 10, block Fourier decomposition gives 10 by 10
Hermitian matrices `H(z)`, where `|z|=1` and `z^L=alpha`.  Direct symbolic
calculation gives

`det(xI-H(z)) = P(x^2,z+z^(-1))`,

where

`P(y,c) = y^5-20y^4+142y^3-(426+c)y^2+(485+10c)y-c^2-9c-114`.

For `|z|=1`, write `c=z+z^(-1)=2 cos(theta)`, so `c` lies in `[-2,2]`.

## Uniform spectral bound

For fixed `y`, `P(y,c)` is concave in `c`, since

`partial_c^2 P = -2`.

It therefore attains its minimum over `[-2,2]` at an endpoint.  Put
`y=198/25+u`, with `u>=0`.  At `c=-2`,

```text
P(198/25+u,-2)
= u^5 + (98/5)u^4 + (16958/125)u^3
  + (1220884/3125)u^2 + (31237941/78125)u
  + 14079218/9765625.
```

At `c=2`,

```text
P(198/25+u,2)
= u^5 + (98/5)u^4 + (16958/125)u^3
  + (1208384/3125)u^2 + (29412941/78125)u
  + 306016718/9765625.
```

All coefficients are positive.  Hence `P(y,c)>0` for every
`y>=198/25` and every `c in [-2,2]`.  Every squared eigenvalue of every
Floquet block is a nonnegative root of `P(y,c)`, so

`rho(A)^2 < 198/25`.

## Threshold bound

The threshold can be written as

`rho_-(n)^2 = 4 + 2 cos(2pi/n) + 2 cos(4pi/n)`.

It is strictly increasing with `n` for `n>=8`.  At `n=50`, the elementary
bounds `cos(t)>1-t^2/2` for nonzero `t` and `pi^2<10` give

```text
cos(pi/25)+cos(2pi/25)
> 2-pi^2/250
> 2-10/250
= 49/25.
```

Therefore

`rho_-(50)^2 > 4+2*(49/25) = 198/25`,

and the same holds for every `n>=50`.  Combining the two strict inequalities
proves the theorem.

## Independent finite certificate

The explicit `n=50, alpha=+1` candidate is also checked without Floquet
analysis.  Exact fraction-free Bareiss elimination and an independent
rational `LDL^T` decomposition both prove

`791 I - 100 A^2` is positive definite.

Thus this concrete candidate satisfies

`rho(A)^2 < 791/100 < rho_-(50)^2`.

The rational sandwich is intentionally stronger than needed for the family
proof and provides an independent implementation-level audit.

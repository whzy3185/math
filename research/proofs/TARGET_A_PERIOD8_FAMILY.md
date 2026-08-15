# Target A: Period-8 Counterexample Family

Date: 2026-08-15

Evidence status: **Proved**, subject to independent human audit.

## Theorem

For every integer `L>=4`, let `n=8L`.  On `C_n(1,2)`, choose triangle
fluxes with period 8

`tau = (+,+,-,+,-,-,+,-)`

and either Hamilton-cycle holonomy `alpha=+1` or `alpha=-1`.  Then

`rho(A)^2 < 1561/200 < rho_-(n)^2`.

Thus Conjecture 3 of *Signed circulants at the Ramanujan bound* is false for
every multiple of 8 with `n>=32`.

The quadrilateral flux is the period-4 pattern

`Q = (+,-,-,-)`,

so defects occur at one residue modulo 4.

## Floquet polynomial

In Hamilton-cycle gauge, with twisted boundary condition
`x_(i+n)=alpha*x_i`, the operator is

`(Ax)_i=x_(i-1)+x_(i+1)+tau_(i-2)x_(i-2)+tau_i*x_(i+2)`.

The period-8 block Fourier matrices `H(z)` have `|z|=1` and `z^L=alpha`.
Writing `c=z+z^(-1)=2cos(theta)`, direct symbolic calculation gives

`det(xI-H(z))=P(x^2,c)`, where

```text
P(y,c)=y^4-16y^3+(80-2c)y^2+(-128+16c)y+c^2-13c+38.
```

## Uniform spectral bound

As a quadratic in `c`, the vertex of `P(y,c)` is

`c_0(y)=y^2-8y+13/2`.

For `y>=1561/200`, this is increasing and

`c_0(1561/200)=199121/40000>2`.

Hence `P(y,c)` decreases throughout `c in [-2,2]`, and its minimum there is
at `c=2`.  Put `y=1561/200+u`.  Then

```text
P(1561/200+u,2)
= u^4 + (761/50)u^3 + (1337363/20000)u^2
  + (136311081/2000000)u + 84332641/1600000000.
```

Every coefficient is positive.  Therefore `P(y,c)>0` whenever
`y>=1561/200` and `c in [-2,2]`.  Since every squared eigenvalue of every
Floquet block is a nonnegative root of this polynomial,

`rho(A)^2<1561/200`.

## Threshold bound

At `n=32`, write `a=pi/16`.  The alternating Taylor bound

`cos(t)>1-t^2/2+t^4/24-t^6/720`

is valid for `0<t<1`.  Applying it to `a` and `2a`, then using
`9<pi^2<10`, gives

```text
cos(pi/16)+cos(pi/8)
> 2 - 50/512 + (17*81)/(24*256^2)
    - (65*1000)/(720*256^3).
```

Consequently

```text
rho_-(32)^2
> 1178731111/150994944
> 1561/200.
```

The function `rho_-(n)^2=4+2cos(2pi/n)+2cos(4pi/n)` increases with `n` in
the relevant range, so the same strict threshold bound holds for all
`n>=32`.  This completes the proof.

## Concrete witness

The file `research/counterexamples/target_a_n32_period8.json` records the
`n=32, alpha=+1` signing.  It is also checked independently by the rational
positive-definiteness verifier, separately from the Floquet proof.

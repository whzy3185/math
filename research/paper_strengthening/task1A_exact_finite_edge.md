# Task 1A: exact finite positive-holonomy edge

**Verdict:** PASS.  
**New theorem class:** Tier A.  
**Proof status:** analytic proof closed; independent symbolic audit passed.  
**Lean status:** deliberately unchanged under the frozen-kernel instruction.

## Theorem

Let `A_(8L,+)` be the finite Hamilton-gauge signing obtained by repeating

```text
tau_*=(1,1,-1,1,-1,-1,1,-1)
```

on `L` cells with positive Hamilton holonomy. Then, for every `L>=1`,

```text
rho(A_(8L,+))^2 = eta = 4+sqrt(10+2sqrt(5)).
```

Consequently, for every `L>=4`,

```text
rho(A_(8L,+))^2 = eta < rho_-(8L)^2.
```

## Proof

The finite cell shift is unitary. Its eigenvalues are the roots of
`z^L=1`, and its eigenspaces give the orthogonal decomposition

```text
A_(8L,+)  ~=  direct_sum_(z^L=1) H(z).
```

The dimensions are `L*8=8L`, so no finite eigenvalue or multiplicity is
lost. Each allowed z lies on the unit circle, and every `H(z)` is Hermitian.

For a squared fiber eigenvalue y put `c=z+z^(-1)`. The chiral determinant
reduction gives `P(y,c)=0`. At `c=2`,

```text
P(y,2)=(y^2-8y+6-2sqrt(5))(y^2-8y+6+2sqrt(5)),
```

whose largest root is eta. Put `s=sqrt(10+2sqrt(5))`, `u=y-eta`, and
`t=2-c`. Direct expansion gives

```text
P(eta+u,2-t)
 = u^4+4s u^3+2u^2t+(40+12sqrt(5))u^2
   +4sut+8sqrt(5)su+t^2+(4sqrt(5)-3)t.
```

Every coefficient is positive. For a unit-circle phase, `t>=0`. Hence no
fiber can have squared eigenvalue greater than eta. Equality forces `u=t=0`,
so `c=2`. On the unit circle this implies `z=1`.

The positive-holonomy grid always contains `z=1`. The real symmetric matrix
`H(1)` has characteristic polynomial `P(x^2,2)`, so
`x=+sqrt(eta)` and `x=-sqrt(eta)` are eigenvalues. They are simple, as the
derivative of the characteristic polynomial is nonzero at both roots. Thus
the finite direct sum both obeys the upper bound and attains it.

## Square-root and Hermitian checks

The auxiliary choice `xi^2=z` imposes no extra phase condition. The original
fiber is a function of z. Replacing xi by -xi changes the sign of the chiral
involution and exchanges its plus/minus coordinate spaces; the final
polynomial contains only `xi^2+xi^(-2)=z+z^(-1)`. When `|z|=1`, every square
root xi also has modulus one.

The chiral coordinate matrix need only be a similarity for the determinant
calculation. Hermitian reality is established in the original fiber basis,
where reverse entries are complex conjugates.

## Rational separator

The previous bound is retained only as

```text
eta < 1561/200 < rho_-(8L)^2.
```

For example, `sqrt(5)<2239/1000` follows by squaring. It implies

```text
10+2sqrt(5) < 7239/500 < (761/200)^2,
```

and hence `eta<1561/200`. This explains the rational number without treating
it as a fitted spectral constant.

## Independent audit

Run

```text
uv run --with sympy python research/paper_strengthening/verifiers/verify_exact_finite_edge.py
```

The verifier rebuilds `P`, the positive expansion, `H(1)`, its characteristic
polynomial, both edge eigenvalues, their simplicity, and the finite
positive-holonomy phase condition. It imports no project constructor or stored
certificate.

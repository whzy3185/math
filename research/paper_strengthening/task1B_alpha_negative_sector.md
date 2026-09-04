# Task 1B: exact negative-holonomy sector

**Verdict:** PASS.  
**New theorem class:** Tier B, with possible promotion because it follows from
a clean closed dispersion law.  
**Proof status:** analytic proof closed; independent symbolic audit passed.  
**Lean status:** not pursued under the frozen-kernel instruction.

## Closed squared-edge dispersion

Writing `y=X+4` transforms the period-eight squared-fiber polynomial into

```text
P(X+4,c)=X^4-(16+2c)X^2+c^2+19c+38.
```

Set `W=X^2`. The discriminant of the resulting quadratic is `104-12c`, so
the larger W-root is

```text
W_+(c)=8+c+sqrt(26-3c).
```

For `-2<=c<=2`, both W-roots are nonnegative and the largest squared fiber
eigenvalue is therefore

```text
r(c)=4+sqrt(8+c+sqrt(26-3c)).
```

This is the exact upper-band dispersion in the phase variable
`c=z+z^(-1)`.

## Monotonicity

The inner function satisfies

```text
W_+'(c)=1-3/(2sqrt(26-3c))>0
```

on `[-2,2]`, since `sqrt(26-3c)>=sqrt(20)>3/2`. Thus `r(c)` is strictly
increasing.

## Positive holonomy

For `z^L=1`, the maximal phase parameter is `c=2`, attained at `z=1`.
Consequently

```text
rho(A_(8L,+))^2=r(2)=4+sqrt(10+2sqrt(5))=eta.
```

## Negative holonomy

For `z^L=-1`, the allowed phases are

```text
z_j=exp((2j+1)pi i/L).
```

The largest real phase parameter is attained by the two phases nearest one
and equals

```text
c_L^-=2cos(pi/L).
```

Hence, for every `L>=1`,

```text
rho(A_(8L,-))^2
 =4+sqrt(8+2cos(pi/L)+sqrt(26-6cos(pi/L))).
```

Since `2cos(pi/L)<2` for finite L and r is strictly increasing,

```text
rho(A_(8L,-))^2 < eta < 8.
```

Moreover `cos(pi/L)` tends to one, so the negative-holonomy edge increases
to eta as `L` tends to infinity.

## Article value

This result removes an apparent asymmetry in the finite analysis and reveals
that both holonomy sectors are governed by one explicit dispersion law. The
positive sector attains the crystalline edge exactly; the negative sector
samples the same band away from its unique maximizer. A concise corollary is
worth retaining in a matrix/Floquet version of the article.

## Independent audit

Run

```text
uv run --with sympy python research/paper_strengthening/verifiers/verify_period8_dispersion.py
```

The verifier reconstructs the shifted polynomial, quadratic discriminant,
both W-roots, the exact top branch, its eta endpoint, derivative formula, and
negative-sector limit.

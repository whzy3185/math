# Period-8 Infinite-Family Independent Audit

Date: 2026-08-16

Status: **PERIOD8_INFINITE_FAMILY_INDEPENDENTLY_AUDITED**

## Theorem

For every integer `L>=4` and each `alpha` in `{-1,+1}`, the period-8 signing
on `C_(8L)(1,2)` with

```text
tau = (+,+,-,+,-,-,+,-)
```

satisfies the strict inequalities

```text
rho(A)^2 < 1561/200 < rho_-(8L)^2.
```

Consequently Conjecture 3 fails at every multiple of 8 at least 32. This is
not a claim about all even orders at least 32.

## Dependency on Task 38

The Task 39 script pins and recomputes the SHA-256 values of the independently
audited Task 38 evidence:

```text
2a5657d0791b1e1a3c742ae8e0a738f083115b4e4516e5e8d8fd4d1999d6c3ee  period8_floquet_independent_audit.json
cc26dedfee3fe3e6c0674f1b217fde592a043a5d8b4913752dc37ad2a62193b2  target_a_period8_independent_polynomial.json
```

It checks the Floquet status, Hermitian property, direct-sum theorem,
`c in [-2,2]`, squared-eigenvalue root link, both holonomies, and agreement of
the two stored coefficient maps. It reconstructs `P` from that map; it does
not hardcode `P` as a new proof input.

The dependency gives

```text
P(y,c) = y^4 - 16y^3 + (80-2c)y^2
         + (-128+16c)y + c^2 - 13c + 38.
```

## Uniform positivity certificate

Put

```text
B = 1561/200,
u = y-B,
t = 2-c.
```

The target region `y>=B, c in [-2,2]` becomes `u>=0, 0<=t<=4`. Exact
symbolic substitution into the Task 38 polynomial automatically gives

```text
P(B+u,2-t)
 = u^4
 + (761/50)u^3
 + 2u^2 t
 + (1337363/20000)u^2
 + (761/50)u t
 + (136311081/2000000)u
 + t^2
 + (119121/20000)t
 + 84332641/1600000000.
```

Every coefficient is nonnegative and the constant is strictly positive.
Therefore

```text
P(y,c)>0 whenever y>=B and c<=2.
```

This is stronger than the required region. In particular, strict positivity
also holds at `y=B`; equality at the spectral bound is impossible.

The expansion, all nine monomial coefficients, dependency hashes, and source
hash were frozen before the secondary Taylor route was run.

## Secondary positivity check

As an algebraically different cross-check, regard `P` as a quadratic in `c`.
The script derives

```text
dP/dc = 2c - 2y^2 + 16y - 13,
c0(y) = y^2 - 8y + 13/2.
```

Since `B>4`, `c0'(y)=2y-8>0` for `y>=B`, and

```text
c0(B)=199121/40000>2.
```

Thus `P` is strictly decreasing in `c` throughout `c<=2`. The exact expansion
of `P(B+u,2)` has five strictly positive coefficients, independently
confirming positivity on the target region.

## Spectral consequence

For every admissible `z`, Task 38 proves that `H(z)` is Hermitian and that
every real block eigenvalue `lambda` satisfies

```text
P(lambda^2,c)=0,  lambda^2>=0.
```

If `lambda^2>=B`, the positive-coefficient certificate would instead give
`P(lambda^2,c)>0`, a contradiction. Hence every block satisfies

```text
rho(H(z))^2 < B.
```

The audited direct-sum decomposition then yields

```text
rho(A_(8L,alpha))^2 < 1561/200
```

for both `alpha=-1` and `alpha=+1`.

## Exact threshold at n=32

From the threshold definition in `TARGET_A_SPEC.md` and
`cos(theta)^2=(1+cos(2theta))/2`, the script derives

```text
rho_-(n)^2 = 4 + 2cos(2pi/n) + 2cos(4pi/n).
```

At `n=32`, two positive half-angle steps give the exact radical

```text
r = rho_-(32)^2
  = 4 + sqrt(2+sqrt(2))
      + sqrt(2+sqrt(2+sqrt(2))).
```

SymPy verifies the half-angle identities and the exact algebraic equality
between the trigonometric expression and this radical. No decimal comparison
is used.

## Minimal polynomial and isolation

The minimal polynomial is generated from the radical, not supplied as the
elimination input:

```text
f(X) = X^8 - 32X^7 + 432X^6 - 3216X^5
       + 14456X^4 - 40224X^3 + 67736X^2
       - 63184X + 25022.
```

Exact endpoint evaluation gives

```text
f(7809/1000) < 0,
f(781/100)   > 0.
```

A Sturm count proves that this interval contains exactly one real root. Exact
algebraic comparisons place the displayed radical at that root. Therefore

```text
1561/200 < 7809/1000 < rho_-(32)^2 < 781/100.
```

This is the primary threshold proof.

## Threshold monotonicity

If `n2>n1>=32`, then both positive angles `2pi/n` and `4pi/n` strictly
decrease and remain in `(0,pi)`. Since cosine is strictly decreasing on that
interval, both cosine terms strictly increase as `n` increases. Hence

```text
rho_-(n)^2 >= rho_-(32)^2 > 1561/200
```

for every integer `n>=32`. Restricting to `n=8L`, `L>=4`, gives precisely the
period-8 family domain.

## Both holonomies

Task 38 proves that `H(z)` is independent of `alpha`; the holonomy only selects
the roots satisfying `z^L=alpha`. The uniform block argument applies to every
unit-modulus `z`, so it covers both root sets and therefore both
`alpha=-1` and `alpha=+1`.

## Secondary threshold cross-check

After the primary snapshot was frozen, a separate alternating-Taylor argument
was recomputed. Applying

```text
cos(s)>1-s^2/2+s^4/24-s^6/720,  0<s<1,
```

at `s=pi/16` and `s=pi/8`, together with `9<pi^2<10`, yields the exact
rational lower bound

```text
rho_-(32)^2 > 1178731111/150994944 > 1561/200.
```

The final rational difference from `B` is
`5389327/3774873600>0`. This cross-check is secondary; the radical and Sturm
certificate are the primary proof.

## Infinite-family checker

`verify_target_a_period8_infinite_family.py` does not redo the determinant.
It independently reads and verifies the Task 38 audit, Task 38 polynomial
snapshot, Task 39 positivity snapshot, and Task 39 total audit. It recomputes
all dependency hashes, reconstructs the positive expansion from its monomial
map, reruns the Sturm count and exact radical placement, verifies the domain
`n=8L, L>=4`, and requires both holonomies. Its final output is

```text
TARGET_A_PERIOD8_INFINITE_FAMILY_PASS
```

## Independence statement

The Task 39 core imports only the Python standard library and SymPy. It uses
the independently audited Task 38 coefficient map as its sole polynomial
source. It does not import the old period-8 family helper, use floating-point
sampling, perform a spectral search, or use the old positivity/Taylor
certificate as a primary input.

The audit proves the stated infinite family only. It does not prove failure at
all even orders at least 32, period-8 optimality, uniqueness of the order-32
witness, or an exact global minimum over all signings.

## Evidence

```text
a33c15a20f44c3fe5f64c0047576862569a1f88e3aeeab213f552bba5189c227  research/scripts/target_a_period8_uniform_bound_audit.py
04bc8fc08b0af24970d77c7f4a73bc9a577caff8e47ac69db90bee478d38d8d6  research/scripts/verify_target_a_period8_infinite_family.py
86d2e7d09534162187699a693d1432a976f2183d9ce06a96cbb40148bb939124  research/audit/target_a_period8_uniform_positivity_snapshot.json
b36bce66ec367e418e1499a1400773147d29537da92a49695b8d7dc9c1c08fa8  research/audit/period8_infinite_family_independent_audit.json
```

## Conclusion

`PERIOD8_INFINITE_FAMILY_INDEPENDENTLY_AUDITED`

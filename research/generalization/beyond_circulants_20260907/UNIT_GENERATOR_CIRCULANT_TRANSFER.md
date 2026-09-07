# Transfer theorem for unit-generated two-step circulants

Date: 2026-09-07.

Let

\[
G_N(a,b)=\operatorname{Cay}(\mathbb Z_N,\{\pm a,\pm b\})
\]

be a simple four-regular circulant.  Assume `gcd(a,N)=1` (or symmetrically
`gcd(b,N)=1`).

Choose `u` with `ua=1 mod N`, put

\[
s_0\equiv ub\pmod N,
\qquad
s=\min(s_0,N-s_0),
\]

and assume the simple four-regular range `2<=s<N/2`.

## Theorem U

Multiplication by `u` is a group automorphism of `Z_N` and induces a graph
isomorphism

\[
\boxed{G_N(a,b)\cong C_N(1,s).}
\tag{U1}
\]

Edge signings pull back and push forward bijectively under this isomorphism,
with identical signed adjacency spectra.  Therefore, writing `m_(a,b)(N)`
for the minimum signed spectral radius on `G_N(a,b)`,

\[
\boxed{m_{a,b}(N)=m(N,s).}
\tag{U2}
\]

Every finite theorem proved in the `C_N(1,s)` workstream transfers verbatim.
In particular:

1. **flat threshold**
   \[
   m_{a,b}(N)=2\iff N=2s+2;
   \]
   otherwise `m_(a,b)(N)>=sqrt(5)`;
2. **resonance threshold** when `N=3s`
   \[
   m_{a,b}(N)<\sqrt8
   \iff s\text{ is even or }s\in\{3,5\};
   \]
3. for odd `s>=7` on the resonance line,
   \[
   m_{a,b}(N)^2\ge8+1/70.
   \]

Thus the final `C_N(1,s)` theorem package already classifies every
four-regular two-generator circulant in which at least one generator is a
unit modulo `N`.

## Boundary

This is an isomorphism-transfer theorem, not a genuinely new graph geometry.
The genuinely new cyclic cases are connected pairs with

\[
\gcd(N,a,b)=1
\]

but neither `a` nor `b` a unit.  Those are treated structurally in
`TWO_GENERATOR_LATTICE_QUOTIENT.md` and form a natural next finite-arithmetic
research class.

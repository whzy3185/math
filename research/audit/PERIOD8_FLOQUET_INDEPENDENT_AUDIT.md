# Period-8 Floquet Independent Audit

Date: 2026-08-15

Status: **PERIOD8_FLOQUET_DETERMINANT_INDEPENDENTLY_AUDITED**

## Purpose

This audit derives the Target A period-8 Floquet reduction and characteristic
determinant with a second implementation. The derivation snapshot was written
and hashed before the frozen family certificate or proof was opened. The
uniform `1561/200` bound is deliberately outside this audit and remains Task 39.

## Mathematical input

The only family data used by the independent derivation are

```text
tau = (+,+,-,+,-,-,+,-),
n = 8L,
x_(i+n) = alpha*x_i,  alpha in {+1,-1}.
```

The local operator is derived below rather than imported from an existing
Target A helper.

## Operator derivation

In Hamilton-cycle gauge, put `a_i=1` for `0<=i<n-1` and
`a_(n-1)=alpha`. The triangle relation

```text
tau_i = a_i*a_(i+1)*b_i
```

determines every finite step-2 edge sign. Equivalently, extend a vector from
`0,...,n-1` to the integers by `x_(i+n)=alpha*x_i`. All local step-1 signs
and step-2 signs then become respectively `1` and `tau_i`; crossing the cut
contributes exactly the missing factor `alpha`. Thus

```text
(Ax)_i = x_(i-1) + x_(i+1)
         + tau_(i-2)*x_(i-2) + tau_i*x_(i+2).
```

The script directly compares the two finite `32 x 32` matrices for both
`alpha=+1` and `alpha=-1`. Both exact integer comparisons pass.

## Cell decomposition

Write `i=8m+r`, with `0<=r<8`, and set `u_m(r)=x_(8m+r)`. For each output
residue and each `delta` in `{-2,-1,+1,+2}`, Euclidean division

```text
r+delta = 8q+s,  0<=s<8
```

determines the target residue `s` and cell shift `q`. The coefficient is `1`
for `delta=+-1`, `tau_(r-2)` for `delta=-2`, and `tau_r` for `delta=+2`.
The resulting 32 rows are frozen in
`research/audit/target_a_period8_cell_transitions.json`; this table is the
sole input to the independent block constructor.

## Twisted boundary

Use the convention

```text
u_m = z^m*v.
```

Since `n=8L`, the global boundary is `u_(m+L)=alpha*u_m`. Substitution gives
`z^(m+L)v=alpha*z^m v`; for a nonzero Bloch vector this is exactly

```text
z^L = alpha.
```

Consequently `|z|^L=1`, hence every admissible `z` has `|z|=1`. For
`alpha=+1` the admissible values are the `L` roots of `+1`; for `alpha=-1`
they are the `L` roots of `-1`.

## Explicit H(z)

Each transition with cell shift `q` contributes its coefficient times `z^q`.
This gives

```text
H(z) =
[ 0  1  1  0  0  0   z^-1   z^-1 ]
[ 1  0  1  1  0  0    0    -z^-1 ]
[ 1  1  0  1 -1  0    0      0   ]
[ 0  1  1  0  1  1    0      0   ]
[ 0  0 -1  1  0  1   -1      0   ]
[ 0  0  0  1  1  0    1     -1   ]
[ z  0  0  0 -1  1    0      1   ]
[ z -z  0  0  0 -1    1      0   ].
```

This matrix was generated from the transition table; it is not copied from
the frozen proof.

## Hermitian property

All coefficients are real. On the unit circle, conjugation sends `z` to
`z^-1`. Entry-by-entry symbolic comparison gives

```text
H(z)_(r,s) = conjugate(H(z)_(s,r)),  |z|=1.
```

Therefore every admissible block is Hermitian and has only real eigenvalues.

## Direct-sum theorem

Let the cell shift be `(Su)_m=u_(m+1)`, interpreted with
`u_(m+L)=alpha*u_m`. It is unitary because `alpha` is a sign. For every root
`z^L=alpha`, the vector `w_z(m)=L^(-1/2)z^m` satisfies `S w_z=z w_z`.
For two distinct roots, their ratio is a nontrivial `L`th root of unity, so
the geometric sum proves that the corresponding vectors are orthogonal.

The transition formula expresses the full operator as a finite sum of residue
matrices tensored with powers of `S`. Hence it commutes with `S` and preserves

```text
E_z = {u_m=z^m*v : v in C^8}.
```

Its restriction to `E_z` is exactly `H(z)`. There are `L` distinct roots,
each space has dimension 8, and `L*8=8L`; orthogonality and the dimension
count give completeness. Thus the normalized Bloch basis proves the unitary
equivalence

```text
A_(8L,alpha) ~= direct_sum_(z^L=alpha) H(z).
```

As implementation regressions, the script independently constructs the full
order-32 matrices for `L=4` and both holonomies. Their exact characteristic
polynomials equal the product of block determinants, computed with a
resultant against `z^4-alpha`. Both checks pass.

## Independent determinant

The first exact route uses SymPy on the independently generated matrix and
obtains the Laurent polynomial

```text
D(x,z) = x^8 - 16x^6
         - 2x^4(z+z^-1) + 80x^4
         + 16x^2(z+z^-1) - 128x^2
         + (z^2+z^-2) - 13(z+z^-1) + 40.
```

Its coefficients are exact integers, it is invariant under `z -> z^-1`, and
it is even in `x`.

## Reduction from z to c

The reduction code starts from the Laurent coefficient map. It pairs the
coefficients at exponents `k` and `-k`, then generates

```text
S_0=2,  S_1=c,  S_(k+1)=c*S_k-S_(k-1)
```

so that `S_k=z^k+z^-k`. Only after verifying that all powers of `x` are even
does it set `y=x^2`. This automatic reduction produces

```text
P_ind(y,c) = y^4 - 16y^3 + (80-2c)y^2
             + (-128+16c)y + c^2 - 13c + 38.
```

Substituting `y=x^2` and `c=z+z^-1` reconstructs `D(x,z)` exactly.

## Second determinant route

The second route is a hand-written fraction-free Bareiss elimination over the
Laurent polynomial ring. It does not call `Matrix.det()`. Every division is
checked to leave only a Laurent monomial denominator, and its final expression
equals the first determinant term by term.

## Comparison with frozen polynomial

The independent polynomial snapshot was written before the old family
certificate was opened. The later comparison parses the frozen polynomial and
compares every monomial separately:

| y degree | c degree | independent | frozen | match |
|---:|---:|---:|---:|:---:|
| 4 | 0 | 1 | 1 | yes |
| 3 | 0 | -16 | -16 | yes |
| 2 | 1 | -2 | -2 | yes |
| 2 | 0 | 80 | 80 | yes |
| 1 | 1 | 16 | 16 | yes |
| 1 | 0 | -128 | -128 | yes |
| 0 | 2 | 1 | 1 | yes |
| 0 | 1 | -13 | -13 | yes |
| 0 | 0 | 38 | 38 | yes |

Therefore `FLOQUET_POLYNOMIAL_MATCH_PASS`.

## Allowed c range

For `|z|=1`, write `z=exp(i*theta)`. Then

```text
c=z+z^-1=2*cos(theta) in [-2,2].
```

At finite `L` only the discrete values coming from `z^L=alpha` occur. A later
bound on the full interval `[-2,2]` will be stronger and will cover both
holonomies because `H(z)` itself does not depend on `alpha`; only the allowed
set of `z` does.

## Squared-eigenvalue interpretation

For admissible `z`, Hermiticity makes every eigenvalue `lambda` real. If
`det(lambda*I-H(z))=0`, the determinant identity gives
`P(lambda^2,c)=0`. Hence `y=lambda^2` is a nonnegative real root. This is the
logical link needed by the uniform argument in Task 39.

## Independence statement

The new script imports only the Python standard library and SymPy. It does not
import an existing Target A family, search, reconstruction, Floquet symbol,
polynomial, or determinant helper. No frozen polynomial coefficient is coded
as an input. The old certificate is read only after the independent transition
table and polynomial snapshot are atomically written and hashed.

This audit does not prove positivity of `P(y,c)` above `1561/200` and does not
re-audit the all-`n` threshold inequality. Accordingly it does not claim
`PERIOD8_INFINITE_FAMILY_INDEPENDENTLY_AUDITED`.

## Evidence

```text
e40f49a274904c73765c5703c099bbb3307d67b3905cb8cecd9d9016f26e6f17  research/audit/target_a_period8_cell_transitions.json
cc26dedfee3fe3e6c0674f1b217fde592a043a5d8b4913752dc37ad2a62193b2  research/audit/target_a_period8_independent_polynomial.json
2a5657d0791b1e1a3c742ae8e0a738f083115b4e4516e5e8d8fd4d1999d6c3ee  research/audit/period8_floquet_independent_audit.json
96b7a6f62768597556670e1115ef5d42ce82e534d5a6469d0725329c6c0c6309  research/scripts/target_a_floquet_independent_audit.py
```

## Conclusion

`PERIOD8_FLOQUET_DETERMINANT_INDEPENDENTLY_AUDITED`

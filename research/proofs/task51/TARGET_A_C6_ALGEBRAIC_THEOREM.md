# Exact Algebraic Theorem for the G6 Interface Level

Let `c6` be the unique G6 squared interface level isolated in Task 50. Then
`c6` is the unique root in

`[7905369311620327/10^15, 7905369311620328/10^15]`

of the irreducible polynomial

```text
16 y^10 - 520 y^9 + 6913 y^8 - 48448 y^7 + 191768 y^6
- 423904 y^5 + 484528 y^4 - 270464 y^3 + 137856 y^2
- 19968 y + 256.
```

## Exact elimination

The proof does not use PSLQ.  Form the exact G6 matching determinant from the
two unstable left bulk modes and the two stable right bulk modes.  After the
nonzero Vandermonde factor `(z1-z2)^2` is removed, the determinant is symmetric
in the two stable multipliers.  Put `S=z1+z2` and `P=z1 z2`.  The reciprocal
bulk quartic gives

```text
S(P+1)+a(y)P=0,
P^2+S^2+1-b(y)P=0.
```

Substitution eliminates `S`.  Splitting the remaining Evans expression as
`E0(y,P)+lambda E1(y,P)` and using `lambda^2=y` gives the exact polynomial
`E0^2-y E1^2`.  Its resultant with the quartic `P` relation has degree 108 in
`y`; exact factorization contains the displayed degree-ten factor with
multiplicity two.

Task 50 proves that the stable multipliers are distinct and positive and that
the Evans determinant has exactly one zero in the rational interval.  Exact
Sturm counts show that only the displayed resultant factor has a root there,
and that it has exactly one.  SymPy factorization over `Q` certifies that this
factor is irreducible.  The machine certificate is
`certificates/c6_exact_evans_elimination.json`.

Status: `C6_DEGREE10_EVANS_POLYNOMIAL_PROVED`.

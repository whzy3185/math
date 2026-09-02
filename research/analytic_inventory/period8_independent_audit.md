# Independent period-eight package audit

The audit verifier is intentionally separate from the earlier period-8
generators.  It takes the triangle-flux word as input and directly rebuilds:

1. the eight-by-eight Bloch matrix;
2. the exact finite \(n=32\) Hamilton-gauge realization in both holonomy
   sectors;
3. the normalized chiral involution and its anticommutation identity;
4. the Floquet determinant \(\det(xI-H)=P(x^2,z+z^{-1})\);
5. the boundary factorization yielding the exact edge \(\eta\), and the
   rational arithmetic in the cosine threshold;
6. the three finite exact closed-walk excesses for non-antipodal two defects.

It imports no prior period-8 coefficient map, sharp-constant artifact, orbit
table, or stored Rayleigh vector.

Run:

```text
python research/scripts/verify_target_a_period8_analytic_package.py
```

Passing this verifier does not replace a human proof review.  It confirms
that the principal algebraic identities and the finite sublemma agree with a
second implementation path.

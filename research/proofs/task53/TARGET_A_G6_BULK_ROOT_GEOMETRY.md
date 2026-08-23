# G6 Bulk Root Geometry

The complete z-discriminant factors as

```text
(y^2-12y+34)(y^2-4y+2)
(12y^2-96y-17)^2
(y^4-16y^3+76y^2-96y+16).
```

Exact Sturm counts show that only `12y^2-96y-17` has a root in
`[c6_upper,16]`. Therefore the root atlas has three cells:

1. Before `y_*`, two distinct real w roots exceed 2, giving four distinct
   positive real reciprocal multipliers.
2. At `y_*`, `w=95/12` is double. The stable and unstable multipliers are
   distinct from the unit circle and each has algebraic multiplicity two.
3. After `y_*`, the w roots are nonreal conjugates. The z roots form a
   reciprocal-conjugate quadruple, with two inside and two outside the unit
   circle.

The repeated-root energy is fully classified; it is not an unresolved loss
of hyperbolicity.

Certificate: `certificates/bulk_global_hyperbolicity.json`.

Status: PROVED.

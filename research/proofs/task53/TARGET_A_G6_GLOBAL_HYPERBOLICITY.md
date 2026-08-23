# G6 Bulk Global Hyperbolicity

Let `chi(z;y)` be the exact reciprocal period-eight transfer polynomial.
Writing `w=z+z^(-1)` gives

```text
z^(-2) chi(z;y)=w^2+(-2y^2+16y-13)w
                 +y^4-16y^3+80y^2-128y+38.
```

For `|z|=1`, `w` is real and belongs to `[-2,2]`. The two endpoint
polynomials are

```text
f(2;y)=y^4-16y^3+76y^2-96y+16,
f(-2;y)=(y^2-12y+34)(y^2-4y+2).
```

The largest zero of `f(2;y)` is the proved bulk edge
`eta=4+sqrt(10+2sqrt(5))`; every zero of `f(-2;y)` is below eta. Hence no
root can cross into `[-2,2]` above eta.

At the rational Task 52 upper endpoint for c6, exact squared inequalities
show that both real w roots exceed 2. Their discriminant is

```text
-12y^2+96y+17.
```

It has one zero in the task interval,
`y_*=4+sqrt(627)/6`, and there the repeated root is `w=95/12>2`. Above
`y_*` the w roots form a nonreal conjugate pair. Thus no unit-circle
multiplier occurs for any `y>eta`, and throughout `[c6_upper,16]` the
transfer has stable algebraic dimension two and unstable algebraic dimension
two.

The machine producer uses exact polynomial arithmetic and Sturm counts. The
independent checker reconstructs every polynomial and interval count.

Status: `GATE_A1_PASS` / PROVED.

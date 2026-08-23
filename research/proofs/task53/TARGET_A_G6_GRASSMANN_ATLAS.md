# Global Grassmann Atlas for the G6 Interface

Put `y=lambda^2`, and let `M(y)` be the period-eight transfer matrix. By the
global hyperbolicity theorem, its stable and unstable spectral subspaces have
dimension two throughout

```text
I=[7905369311620328/10^15,16].
```

Write the reciprocal characteristic polynomial as

```text
z^4+a z^3+b z^2+a z+1,
a=-2y^2+16y-13,
b=y^4-16y^3+80y^2-128y+40.
```

If `z1,z2` are the stable multipliers, set `S=z1+z2` and `P=z1*z2`. Dividing
the exact reciprocal relations by `P^2` shows that `t=P+P^-1` satisfies

```text
(t+2)(t-b)+a^2=0.
```

The larger real root `t_large` is greater than two on `I`; the physical
stable branch is therefore

```text
P=2/(t_large+sqrt(t_large^2-4)),   S=-aP/(P+1).
```

This representation is real on both sides of the repeated-multiplier energy
and is continuous there. The unstable plane is obtained from the reciprocal
multipliers.

## Certified cover

For a three-row cofactor section, wedge the two eigenvectors, divide by the
Vandermonde `z1-z2`, and symmetrize in `S,P`. Exact elimination of a selected
section against the bulk relation gives the complete list of possible chart
zeros. Rows `013`, with right minor `p23` and left minor `p01`, have only the
factor

```text
3y^2-24y+2
```

in `I`. Its unique root lies in
`[7.915780041490243,7.915780041490244]`. This is a cofactor-section
degeneracy, not a loss of the physical plane.

Use the following closed charts:

| chart | interval | cofactor rows | right minor | left minor |
|---|---|---|---|---|
| outer left | `[c6_upper,7.91575]` | `013` | `p23` | `p01` |
| bridge | `[7.9157,7.9159]` | `012` | `p01` | `p02` |
| outer right | `[7.91585,16]` | `013` | `p23` | `p01` |

On the bridge, exact-rational outward intervals exclude zero for both chosen
sections. The two overlaps are nonempty. On each chart divide all Plucker
coordinates by the chosen section; its normalized lower bound is exactly
one. On an overlap the transition is the exact ratio of the two selected
sections, whose denominator is already certified nonzero. Thus every point,
including both endpoints and both algebraic section/multiplier degeneracies,
is covered.

The producer derives the sections from exact transfer matrices. The checker
reconstructs the wedges, resultants, Sturm counts, and bridge intervals; it
does not trust a stored status field.

Status: `GATE_A2_PASS` / COMPUTER_ASSISTED_PROVED.

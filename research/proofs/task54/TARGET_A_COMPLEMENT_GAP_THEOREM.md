# Complement Gap for Separated G6 Modes

Fix `r in {1,2,3}`. Around each interface choose a piecewise sine/cosine
cutoff `chi_j` with transition width `R`, disjoint from the other interface
cores, and put `phi_j=chi_j psi_j`. The supports are disjoint, so the
`phi_j` are orthogonal; normalize them to obtain `u_j` and let `V_L` be their
span.

The central orthogonality point is exact. If `x perpendicular V_L`, then

```text
<psi_j,chi_j x>=<chi_j psi_j,x>=<phi_j,x>=0.
```

Thus the interface-localized vector has no component in the unique `c6`
eigenspace. Spectral isolation gives its quadratic-form bound
`c6-1/100`. Every bulk-localized vector is bounded by `eta`, which is lower.

Complete these functions to a cyclic, two-overlap sine/cosine partition.
For sites at distance `d<=4`,

```text
sum_j |chi_j(a)-chi_j(b)|^2 <= pi^2 d^2/(4R^2).
```

Since `pi^2<10`, `H` has range four and absolute row sum at most 16, the
exact IMS identity gives `||E_IMS||<=320/R^2`. At `R>=256` this is less than
`1/200`. A minimum site separation `D>=4R+16` makes every enlarged support
exactly a bulk or single-G6 model. Consequently

```text
<x,H_ring x> <= (c6-1/200)||x||^2,  x perpendicular V_L.
```

The estimate is uniform in ring size, orientations, and holonomy.

Status: `EXACT_R_BY_COMPLEMENT_GAP_PROVED` / PROVED.

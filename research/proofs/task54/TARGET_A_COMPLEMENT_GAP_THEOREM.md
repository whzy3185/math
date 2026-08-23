# Complement Gap for Separated G6 Modes

> **Superseded / not proved.** The single-G6 `H=A^2` eigenspace at `c6` has
> rank two, not one. The span below removes only one mode per interface, so
> the asserted codimension-`r` complement cap does not follow. The cutoff and
> IMS arithmetic remain valid inputs for a future codimension-`2r` proof.

First fix `r in {2,3}` and list the interface centers cyclically as `p_j`. Let
`d_j` be the forward site distance from `p_j` to `p_(j+1)` and put

```text
D=min d_j,  S=floor(D/4),
L_site=S-12,  ell=floor(L_site/8).
```

## Exact cyclic partition

On each arc retain endpoint plateaux of length `S`. Across its middle segment
of length `T_j=d_j-2S`, define the only two nonzero cutoffs by

```text
chi_j(t)=cos(pi t/(2T_j)),
chi_(j+1)(t)=sin(pi t/(2T_j)).
```

The definitions agree on adjacent plateaux and give
`sum_j chi_j^2=1` exactly. Put `phi_j=chi_j psi_j` and let `V_L` be their
span. Each `phi_j` is nonzero near `p_j`, where all other cutoffs vanish, so
the `r` vectors are linearly independent. Their transition tails overlap;
disjointness is neither asserted nor required.

For `r=1`, let `D` be the length of the unique bulk return arc, use the same
`S=floor(D/4)`, and write `d(x)` for cyclic distance from the interface.
Define

```text
chi_I(x)=1,                                  d(x)<=S-8,
        =cos(pi(d(x)-S+8)/(2S)),   S-8<d(x)<2S-8,
        =0,                                  d(x)>=2S-8,
chi_B(x)=sqrt(1-chi_I(x)^2).
```

Thus the transition has radial width `S` and the antipodal seam lies in an
eight-site radial zero plateau. Their squares sum to one. After range-four enlargement,
the first support is a single-G6 patch and still misses the seam; the second
is pure bulk and still misses the interface.
Put `phi_1=chi_interface psi_1` and `V_L=span{phi_1}`.

If `x perpendicular V_L`, then for every interface

```text
<psi_j,chi_j x>=<chi_j psi_j,x>=<phi_j,x>=0.
```

Thus every interface-localized vector is exactly orthogonal to the unique
`c6` mode. Bulk-localized vectors in the `r=1` construction are bounded by
`eta<c6-1/100`. The single-G6 isolation theorem gives

```text
<chi_j x,H6 chi_j x> <=(c6-1/100)||chi_j x||^2.
```

## IMS error and geometry

The cutoff vector moves along a unit-circle arc. For sites at cyclic distance
`d<=4`, with `T_min=min T_j`,

```text
sum_j |chi_j(a)-chi_j(b)|^2 <=pi^2 d^2/(4T_min^2).
```

The plateau of width `S>4` around each neighboring interface ensures that the
range-four enlargement of `supp chi_j` contains exactly interface `j`. It is
a proper arc gauge-equivalent to the infinite G6 model; a holonomy cut can be
placed in an excluded plateau.

Using `pi^2<10`, range four, and absolute row sum 16 in the exact IMS identity
gives `||E_IMS||<=320/T_min^2`. The single-interface transition has width
`S`; the multi-interface transitions have width at least `D-2S`. If
`D>=1040`, then

```text
S>=260, L_site>=248, ell>=31, T_min>=260,
320/T_min^2 <=320/260^2 <1/200.
```

Consequently

```text
<x,H_ring x> <=(c6-1/200)||x||^2,  x perpendicular V_L.
```

The cutoffs begin changing beyond site distance `L_site+4` from an interface.
After the
range-four operator is applied, the G6 tail estimate yields residual
`O((9/25)^ell)`, because `9/25` is the decay per complete period-eight bulk
cell rather than per site. The Gram matrix
tends to the identity, so the at-least-`r` spectral-projection argument
applies to the same span.

Historical status withdrawn. Current status:
`OPEN_PENDING_CODIMENSION_2R_RECONSTRUCTION`.

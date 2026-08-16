# Target A Notation Freeze

Status: **TARGET_A_NOTATION_FROZEN**

## Graph and Signing

| Symbol | Frozen meaning |
|---|---|
| `G_n=C_n(1,2)` | The circulant graph on `Z/nZ` with steps `+-1,+-2`. |
| `sigma:E(G_n)->{+-1}` | An edge signing. |
| `A_sigma` | The signed adjacency matrix; `rho(A_sigma)` is its ordinary, unsquared spectral radius. |
| `alpha` | Product of signs on the step-1 Hamilton cycle, hence `alpha in {+-1}`. |

In Hamilton gauge the step-1 signs are one on the infinite lift and the
step-2 sign from `i` to `i+2` is `tau_i`. At finite order, crossing the cut
encodes `alpha`; it must not be silently absorbed into `tau`.

## Flux Coordinates

| Symbol | Frozen meaning |
|---|---|
| `tau_i` | Triangle flux, or equivalently the step-2 coefficient in Hamilton gauge. |
| `Q_i=tau_i tau_{i+1}` | Adjacent triangle-flux product. A legal periodic word satisfies `product_i Q_i=1`. |
| `D(Q)={i:Q_i=+1}` | Positive-flux defect positions. |
| `d=|D(Q)|` | Number of positive defects in one chosen cell. |
| `a` | Cyclic count of `i` with `Q_i=Q_{i+1}=+1`. |
| `b` | Cyclic count of `i` with `Q_i=Q_{i+2}=+1`. |

Binary tables use `1` for `Q_i=+1` and `0` for `Q_i=-1`, with `Q_0` at the
left. The two lifts `tau` and `-tau` are global matrix-negation partners and
have the same spectral radius. Translation and reflection act dihedrally on
`Q`. Cell repetition does not create a new infinite phase; primitive period
always refers to `tau` unless explicitly written `primitive Q period`.

## Periodic Spectrum

| Symbol | Frozen meaning |
|---|---|
| `p` | Length of a periodic unit cell; in bounded results, the displayed-cell length. |
| `L` | Number of cells in a finite graph, so `n=pL` when that cell is used. |
| `H_Q(z)` or `H_{p,Q}(z)` | The `p`-dimensional Bloch matrix for a chosen lift of `Q`; its spectrum is lift-independent up to the recorded negation identity. |
| `z` | Bloch multiplier. Finite matrices use the discrete set `z^L=alpha`; infinite volume uses all `|z|=1`. |
| `c=z+z^{-1}` | Real band parameter in `[-2,2]` on the unit circle. |
| `y=lambda^2` | Squared fiber eigenvalue. |
| `R(Q)` | **Always** `sup_{|z|=1} rho(H_Q(z))^2`, the squared infinite-volume spectral radius. |
| `eta` | `4+sqrt(10+2sqrt(5))`, the target value of `R(Q)`. |
| `rho_*` | `sqrt(eta)`, the unsquared target spectral radius. |

`R(Q)` is never used for a finite matrix radius and never denotes an
unsquared quantity. Finite statements must write `rho(A_sigma)^2` and state
the admissible set `z^L=alpha`.

## Closed-Walk Quantities

| Symbol | Frozen meaning |
|---|---|
| `M_k(Q)` | `CT_z tr(H_{p,Q}(z)^{2k})`, equivalently normalized phase average of the even spectral moment. |
| `F_k(Q)` | `M_{k+1}(Q)-8M_k(Q)`. |

The only barrier implication is

```text
F_k(Q)>0  =>  R(Q)>8.
```

Neither `F_k<=0 => R(Q)<=8` nor “the first finitely many excesses are
nonpositive” is valid. The target upper bound comes from the sharp Floquet
theorem, not from negative moments.

## Equivalence Boundary

Switching equivalence preserves all cycle fluxes. The finite minimality
quotient additionally uses global matrix negation and graph dihedral
automorphisms, while retaining `alpha`. The bounded-period theorem uses
translation, reflection, global `tau` negation, and unit-cell repetition.
These equivalence relations are related but are not interchangeable.

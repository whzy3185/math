# Gap, Charge, and Translation Sectors

## Definitions

Let `Q in {+1,-1}^n` be a cyclic quadrilateral-flux word with positive sites

```text
D(Q)={x_1,...,x_d},
```

listed in cyclic order. Let `g_j` be the positive cyclic distance from `x_j`
to `x_(j+1)`, and define the local charge

```text
q_j=g_j-4.
```

Here the gap coordinates are used when `d>=1`; the defect-free word is a
separate degenerate case with no gap list.

For `s in Z/4Z`, let `B_s` be the reference bulk whose positive `Q` sites are
the congruence class `s mod 4`.

## Theorem

The gap coordinates satisfy

```text
sum_(j=1)^d g_j=n,
sum_(j=1)^d q_j=n-4d.                                (1)
```

If `n` is even and `Q` admits a cyclic `tau` lift, then `d` is even and

```text
sum_j q_j = n (mod 8).                               (2)
```

An oriented interface of charge `q` taking a left reference bulk `B_s` to a
right reference bulk has sector shift `sigma_sec(q)` (also abbreviated
`sigma(q)` when no signing is present), where

```text
sigma_sec(q)=sigma(q)=q mod 4,
B_s -> B_(s+sigma_sec(q)).                           (3)
```

For concatenated interfaces the shifts add:

```text
sigma_sec(q_1+...+q_k)
=sigma_sec(q_1)+...+sigma_sec(q_k) mod 4.             (4)
```

These laws are independent of the two `tau` lifts and of the Hamilton-cycle
holonomy.

## Consequence for G6 slips

A G6 slip has `q=6-4=2`. Thus `r` such slips have total charge `2r`, select
the even-order residue `2r mod 8`, and shift the reference sector by
`2r mod 4`. In particular one, two, and three G6 slips provide the charge
patterns required for residues `2`, `4`, and `6` modulo eight.

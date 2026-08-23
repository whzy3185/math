# Gap-2/Gap-6 Quotient Involution

## Statement

Let `e_g(lam,P)` be the primitive symmetric Evans numerator for a single gap
`g`, after substituting the exact reciprocal-bulk relation for
`S=z_1+z_2`, and then reducing to degree less than four in `P=z_1z_2`.
In the quotient algebra

```text
Q(lam)[P,P^-1]/(R_lam)
```

one has the exact unsquared identity

```text
e_6(lam,P) = P^3 e_2(-lam,P^-1).                    (1)
```

This is a quotient spectral-curve involution. It is stronger than equality
of the squared elimination resultants, but it is not an equality of the two
physical interface spectra because `P -> P^-1` exchanges stable and unstable
Floquet branches.

Evidence status: `COMPUTER_ASSISTED_PROVED`.

## Transfer And Bulk Relations

Fix `tau_0=1` and `tau_(i+1)=Q_i tau_i`, where the left reference phase has
`Q_i=+1` on `4Z` through zero and the right phase has `Q_i=+1` on
`g+4Z` from `g` onward. In the state

```text
(u_(i+1),u_i,u_(i-1),u_(i-2)),
```

the site transfer is

```text
T_i = [[-tau_i, tau_i*lam, -tau_i, -tau_i*tau_(i-2)],
       [       1,         0,      0,                    0],
       [       0,         1,      0,                    0],
       [       0,         0,      1,                    0]].
```

Products are left multiplied in increasing site order. If `z_1,z_2` are the
stable bulk multipliers, `S=z_1+z_2`, and `P=z_1z_2`, reciprocal pairing of
the four bulk roots gives

```text
S(P+1)+aP = 0,
P^2+S^2+1-bP = 0,
```

where

```text
a = -2 lam^4 + 16 lam^2 - 13,
b = lam^8 - 16 lam^6 + 80 lam^4 - 128 lam^2 + 40.
```

Eliminating `S` gives the palindromic quartic `R_lam(P)`. With `y=lam^2`,

```text
R_y(P) = P^4 + c(y)P^3 + d(y)P^2 + c(y)P + 1,
c(y) = -y^4 + 16y^3 - 80y^2 + 128y - 38,
d(y) = 2y^4 - 32y^3 + 148y^2 - 160y + 91.       (2)
```

## Evans Reduction

For each gap, use the cut `[-8,g+8)`. Three-row cofactor vectors with rows
`(0,1,2)` represent the two stable and two unstable bulk eigenspaces. Divide
the resulting matching determinant by `(z_1-z_2)^2`, symmetrize in
`z_1,z_2`, and substitute `S=-aP/(P+1)`. Taking the primitive numerator in
`P` gives `E_g(lam,P)`. Define

```text
e_g = rem_P(E_g,R_lam),       deg_P(e_g)<4.         (3)
```

Direct exact reduction verifies (1). The certificate stores both reduced
polynomials, their hashes, the unreduced hashes, and the complete transfer
convention. The independent checker rebuilds `Q`, `tau`, all transfer
products, cofactor vectors, symmetric Evans determinants, and quotient
remainders without importing the producer.

## Common Norm

Taking the quotient norm by a resultant gives the same polynomial for gaps
2 and 6. Its exact factorization is

```text
(2y^2-16y+13)^8
(y^4-16y^3+68y^2-32y+52)
(9y^4-144y^3+708y^2-1056y+404)
p_6(y)
p_aux(y)^2,                                             (4)
```

where

```text
p_6(y) = 16y^10-520y^9+6913y^8-48448y^7+191768y^6
         -423904y^5+484528y^4-270464y^3+137856y^2
         -19968y+256,

p_aux(y) = 16y^10-484y^9+5796y^8-34617y^7+105000y^6
           -135904y^5+7632y^4+60620y^3+57232y^2
           -52880y+64.
```

Thus the common degree-ten factor observed in Task 52 is the norm image of
the exact involution (1), rather than an unexplained coincidence.

## Logical Boundary

For physical decaying modes, stable multipliers satisfy `|P|<1`. Equation
(1) sends them to the reciprocal sheet `|P|>1`; it therefore does not identify
the gap-2 and gap-6 physical Evans zeros. In particular, the localized gap-2
level above 8 and the G6 level `c6<8` remain distinct. No physical branch
ordering or all-gap lower theorem follows from (1) alone.

## Verification

Run:

```bash
PYTHONPATH=research/scripts python3 research/scripts/target_a_task55_single_gap.py
PYTHONPATH=research/scripts python3 research/scripts/verify_target_a_task55_single_gap.py
python3 -m pytest -q research/scripts/test_target_a_task55_single_gap.py
```

The checker is fail-closed on symbol names, cut, multiplication order,
exterior basis, polynomial coefficients, full matrix entries, matrix hashes,
Krylov witnesses, stored checks, and duplicate JSON keys.

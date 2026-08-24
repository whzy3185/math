# Proof Overview: IMS and Residue Classes

## Mathematical reduction

[MAIN_TEXT_REQUIRED]

The proof has four steps.

1. Square the signed adjacency, obtaining a self-adjoint operator `H=A^2` of
   propagation range four.
2. Localize with a cyclic partition of unity. The exact double-commutator
   identity separates the localized quadratic forms from an explicitly
   bounded IMS error.
3. Use separation to classify every enlarged localization window as pure
   period-eight bulk, a forward G6 interface, or a reflected G6 interface.
   Their squared spectral edges are at most `eta` and `c6`, respectively.
4. Insert the three explicit gap words. Their gap sums, flux parity, sector
   shift, holonomy, and minimum separation are checked symbolically. The IMS
   error tends to zero, yielding the three `limsup` inequalities.

## Finite exact object

[APPENDIX_REQUIRED]

No enumeration is needed for the IMS identity or the residue algebra. The
finite exact object is the offset table of `H`: for displacements
`d=1,2,3,4`, the absolute coefficients are bounded by `2,1,2,1`. Combined
with the exact translate sum for the cyclic tent, this gives the rational
error in the theorem.

The only machine-assisted inputs are upstream spectral statements:

```text
sup sigma(H_bulk)=eta,
sup sigma(H_6)=c6,
eta<c6,
```

and, for the optional exponential refinement, the exact-`2t` cluster
certificate.

## Machine verification

[REPRODUCIBILITY_ONLY]

The original exact certificate recomputes the tent normalization, gap sums,
flux legality, interface counts, and a conservative IMS constant. A later
exact threshold certificate recomputes the sharper offset sum and the
`120/R^2` bound. These checks audit arithmetic; the displayed proof is the
logical argument.

## Mathematical consequence

[MAIN_TEXT_REQUIRED]

Every localized quadratic form is at most `c6` times its localized norm.
The partition of unity sums those norms to one, so only the explicit IMS
error remains. In each nonzero even residue class the number of interfaces is
fixed while the minimum separation diverges. Hence the error vanishes and
the explicit signing bounds `m_n`, proving the `limsup` theorem.

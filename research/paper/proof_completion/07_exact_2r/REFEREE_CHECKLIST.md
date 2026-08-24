# Referee Checklist

- [x] The local G6 squared eigenspace has dimension two.
- [x] Both local modes are retained at every interface.
- [x] The theorem scope is exactly `r in {1,2,3}` and `D>=1040`.
- [x] Orientation, holonomy, multiplicity, and the `r=1` distance convention
  are stated.
- [x] Same-interface `+/-` overlap is included in the Gram estimate.
- [x] The Gram matrix has size `2r x 2r` and is proved invertible.
- [x] The residual argument proves a lower count of `2r`.
- [x] Orthogonality to the truncated space implies orthogonality to both local
  G6 modes.
- [x] The IMS error is computed with range four and the actual minimum
  transition width.
- [x] Min-max gives an upper count of `2r`.
- [x] The Feshbach coordinate operator acts on `C^(2r)`.
- [x] The eigenvalue equation is `H_eff(z)-zI_(2r)`, not `H_eff-zP`.
- [x] The `3505r` constant follows from separate first- and second-order
  bounds.
- [x] No individual simplicity or arbitrary-`r` statement is inferred.
- [x] Historical exact-`r`, codimension-`r`, and `r x r` claims are marked
  false as stated.

## Referee recomputation

After accepting the three certified inputs, check equations (4), (7)-(12),
(15)-(18), and (20)-(27) of `FULL_PROOF.md`. These contain every numerical
inequality used in the exact count and Feshbach estimate.

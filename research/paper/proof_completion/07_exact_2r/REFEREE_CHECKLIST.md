# Referee Checklist

- [x] The local G6 squared eigenspace has dimension two.
- [x] Both local modes are retained at every interface.
- [x] The theorem scope is exactly `r in {1,2,3}` and `D>=1040`.
- [x] Orientation, holonomy, multiplicity, and the `r=1` distance convention
  are stated.
- [x] Interface centers are the left endpoints of the marked length-six
  positive-`Q` gaps, and all cyclic distances are site distances.
- [x] Interface cutoffs, bulk cutoffs, width-`S` transition zones, range-four
  enlarged supports, and the two-site coefficient collar are defined.
- [x] Every interface patch is identified coefficient by coefficient with a
  finite G6 section after translation, optional reflection, and switching.
- [x] The identification separately covers both `tau` lifts, both Hamilton
  holonomies, `r=1,2,3`, and cyclic wraparound.
- [x] The pure-bulk plateau has length at least 16, and the selected seam is
  at distance at least eight from every interface support when `D>=1040`.
- [x] Every noninterface patch is a translated period-eight bulk section and
  has local squared edge at most `eta`.
- [x] The transported full G6 pair remains normalized and orthogonal before
  truncation, and the truncated vectors are exactly the columns of `Phi`.
- [x] The identity
  `<psi_(j,+/-),chi_j x>=<phi_(j,+/-),x>` uses the same local unitary as the
  certified complement gap.
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

First check equations (1)-(23) of `PATCH_IDENTIFICATION_LEMMA.md`, especially
the 16-site bulk plateau, the eight-site seam clearance, the lift identity
(18), and the mode identity (22). After accepting the three certified
single-interface inputs, check equations (5), (8)-(13), (16)-(19), and
(21)-(28) of `FULL_PROOF.md`. These contain every numerical inequality used
in the exact count and Feshbach estimate.

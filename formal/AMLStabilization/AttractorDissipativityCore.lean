import Mathlib

namespace AMLStabilization

/-- A continuous strictly positive coefficient on a nonempty compact set has a uniform positive lower bound. -/
theorem compact_positive_uniform_lower_bound
    {S : Set ℝ} {h : ℝ → ℝ}
    (hScompact : IsCompact S) (hSnonempty : S.Nonempty)
    (hcont : ContinuousOn h S)
    (hpos : ∀ s ∈ S, 0 < h s) :
    ∃ beta > 0, ∀ s ∈ S, beta ≤ h s := by
  obtain ⟨x, hxS, hxmin⟩ := hScompact.exists_isMinOn hSnonempty hcont
  refine ⟨h x, hpos x hxS, ?_⟩
  intro s hs
  exact hxmin hs

/-- Positive factorization around an equilibrium yields uniform quadratic dissipativity. -/
theorem quadraticDissipativity_of_positive_factor
    {S : Set ℝ} {F h : ℝ → ℝ} {vstar beta : ℝ}
    (hbeta : 0 ≤ beta)
    (hlower : ∀ s ∈ S, beta ≤ h s)
    (hfactor : ∀ s ∈ S, F s = -h s * (s - vstar)) :
    ∀ s ∈ S, (s - vstar) * F s ≤ -beta * (s - vstar) ^ 2 := by
  intro s hs
  rw [hfactor s hs]
  have hsquare : 0 ≤ (s - vstar) ^ 2 := sq_nonneg _
  have hmul := mul_le_mul_of_nonneg_right (hlower s hs) hsquare
  nlinarith

/-- Compact positive factorization automatically supplies the manuscript's quantitative `beta`. -/
theorem exists_quadraticDissipativity_of_compact_positive_factor
    {S : Set ℝ} {F h : ℝ → ℝ} {vstar : ℝ}
    (hScompact : IsCompact S) (hSnonempty : S.Nonempty)
    (hcont : ContinuousOn h S)
    (hpos : ∀ s ∈ S, 0 < h s)
    (hfactor : ∀ s ∈ S, F s = -h s * (s - vstar)) :
    ∃ beta > 0, ∀ s ∈ S,
      (s - vstar) * F s ≤ -beta * (s - vstar) ^ 2 := by
  obtain ⟨beta, hbeta, hlower⟩ :=
    compact_positive_uniform_lower_bound hScompact hSnonempty hcont hpos
  refine ⟨beta, hbeta, ?_⟩
  exact quadraticDissipativity_of_positive_factor hbeta.le hlower hfactor

/-- Strict attraction on the left of an equilibrium forces positive reaction. -/
theorem reaction_pos_left_of_strict_attraction
    {F : ℝ → ℝ} {s vstar : ℝ}
    (hleft : s < vstar)
    (hattr : (s - vstar) * F s < 0) :
    0 < F s := by
  have hdiff : s - vstar < 0 := sub_neg.mpr hleft
  by_contra hnot
  have hF : F s ≤ 0 := le_of_not_gt hnot
  have : 0 ≤ (s - vstar) * F s := mul_nonneg_of_nonpos_of_nonpos hdiff.le hF
  linarith

/-- Strict attraction on the right of an equilibrium forces negative reaction. -/
theorem reaction_neg_right_of_strict_attraction
    {F : ℝ → ℝ} {s vstar : ℝ}
    (hright : vstar < s)
    (hattr : (s - vstar) * F s < 0) :
    F s < 0 := by
  have hdiff : 0 < s - vstar := sub_pos.mpr hright
  by_contra hnot
  have hF : 0 ≤ F s := le_of_not_gt hnot
  have : 0 ≤ (s - vstar) * F s := mul_nonneg hdiff.le hF
  linarith

end AMLStabilization

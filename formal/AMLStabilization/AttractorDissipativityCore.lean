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

/-- A positive factor multiplying the degenerate restoring law yields uniform
`(2+theta)`-order dissipativity for every real `theta>0`. -/
theorem degenerateDissipativity_of_positive_factor
    {S : Set ℝ} {F h : ℝ → ℝ} {vstar beta theta : ℝ}
    (htheta : 0 < theta)
    (hbeta : 0 ≤ beta)
    (hlower : ∀ s ∈ S, beta ≤ h s)
    (hfactor : ∀ s ∈ S,
      F s = -h s * (s - vstar) * |s - vstar| ^ theta) :
    ∀ s ∈ S,
      (s - vstar) * F s ≤ -beta * |s - vstar| ^ (theta + 2) := by
  intro s hs
  rw [hfactor s hs]
  by_cases hx : s - vstar = 0
  · have htheta0 : theta ≠ 0 := ne_of_gt htheta
    have htheta2 : theta + 2 ≠ 0 := ne_of_gt (by linarith)
    rw [hx]
    simp [Real.zero_rpow htheta0, Real.zero_rpow htheta2]
  · have habs : 0 < |s - vstar| := abs_pos.mpr hx
    have hsquare :
        (s - vstar) * (s - vstar) = |s - vstar| ^ (2 : ℝ) := by
      rw [Real.rpow_two, sq_abs, pow_two]
    have hpow0 : 0 ≤ |s - vstar| ^ (theta + 2) :=
      Real.rpow_nonneg (abs_nonneg _) _
    have hmul :
        beta * |s - vstar| ^ (theta + 2) ≤
          h s * |s - vstar| ^ (theta + 2) :=
      mul_le_mul_of_nonneg_right (hlower s hs) hpow0
    calc
      (s - vstar) * (-h s * (s - vstar) * |s - vstar| ^ theta) =
          -h s * ((s - vstar) * (s - vstar)) * |s - vstar| ^ theta := by ring
      _ = -h s * (|s - vstar| ^ (2 : ℝ) * |s - vstar| ^ theta) := by
        rw [hsquare]
      _ = -h s * |s - vstar| ^ ((2 : ℝ) + theta) := by
        rw [Real.rpow_add habs]
      _ = -h s * |s - vstar| ^ (theta + 2) := by
        rw [add_comm (2 : ℝ) theta]
      _ = -(h s * |s - vstar| ^ (theta + 2)) := by ring
      _ ≤ -(beta * |s - vstar| ^ (theta + 2)) := neg_le_neg hmul
      _ = -beta * |s - vstar| ^ (theta + 2) := by ring

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

/-- On a compact invariant signal set, a continuous positive factor in front of
the degenerate restoring law automatically produces a quantitative damping
constant `beta>0`. -/
theorem exists_degenerateDissipativity_of_compact_positive_factor
    {S : Set ℝ} {F h : ℝ → ℝ} {vstar theta : ℝ}
    (htheta : 0 < theta)
    (hScompact : IsCompact S) (hSnonempty : S.Nonempty)
    (hcont : ContinuousOn h S)
    (hpos : ∀ s ∈ S, 0 < h s)
    (hfactor : ∀ s ∈ S,
      F s = -h s * (s - vstar) * |s - vstar| ^ theta) :
    ∃ beta > 0, ∀ s ∈ S,
      (s - vstar) * F s ≤ -beta * |s - vstar| ^ (theta + 2) := by
  obtain ⟨beta, hbeta, hlower⟩ :=
    compact_positive_uniform_lower_bound hScompact hSnonempty hcont hpos
  refine ⟨beta, hbeta, ?_⟩
  exact degenerateDissipativity_of_positive_factor
    htheta hbeta.le hlower hfactor

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

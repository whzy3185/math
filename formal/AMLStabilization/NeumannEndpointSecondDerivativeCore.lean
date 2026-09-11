import Mathlib

open Set Filter
open scoped Topology

namespace AMLStabilization

private lemma choose_small_step
    {a b r : ℝ} (hab : a < b) (hr : 0 < r) :
    ∃ d : ℝ, 0 < d ∧ d < r ∧ d < b - a := by
  refine ⟨min (r / 2) ((b - a) / 2), ?_, ?_, ?_⟩
  · exact lt_min (half_pos hr) (half_pos (sub_pos.mpr hab))
  · exact lt_of_le_of_lt (min_le_left _ _) (half_lt_self hr)
  · exact lt_of_le_of_lt (min_le_right _ _) (half_lt_self (sub_pos.mpr hab))

/-- At the left endpoint of an interval, a global maximum together with the
Neumann condition `f'(a)=0` forces the second derivative to be nonpositive. -/
theorem secondDeriv_nonpos_at_left_endpoint_of_isMaxOn_of_deriv_zero
    {f : ℝ → ℝ} {a b : ℝ}
    (hab : a < b)
    (hmax : IsMaxOn f (Icc a b) a)
    (hcont : ContinuousOn f (Icc a b))
    (hderiv0 : deriv f a = 0) :
    deriv (deriv f) a ≤ 0 := by
  by_contra hnot
  have hsec : 0 < deriv (deriv f) a := lt_of_not_ge hnot
  have hsign := eventually_nhdsWithin_sign_eq_of_deriv_pos
    (f := deriv f) hsec hderiv0
  rcases Metric.eventually_nhds_iff_ball.mp hsign with ⟨r, hr, hsignr⟩
  rcases choose_small_step hab hr with ⟨d, hd, hdr, hdab⟩
  let y : ℝ := a + d
  have hay : a < y := by dsimp [y]; linarith
  have hyb : y < b := by dsimp [y]; linarith
  have hderivPos : ∀ c ∈ Ioo a y, 0 < deriv f c := by
    intro c hc
    have hcball : c ∈ Metric.ball a r := by
      rw [Metric.mem_ball, Real.dist_eq]
      have hca : 0 < c - a := sub_pos.mpr hc.1
      rw [abs_of_pos hca]
      have hcar : c - a < r := by
        dsimp [y] at hc
        linarith [hc.2, hdr]
      exact hcar
    have hs := hsignr c hcball
    have hca : 0 < c - a := sub_pos.mpr hc.1
    have hs' : SignType.sign (deriv f c) = 1 := by
      simpa [sign_pos hca] using hs
    exact sign_eq_one_iff.mp hs'
  have hcont' : ContinuousOn f (Icc a y) := by
    apply hcont.mono
    intro x hx
    exact ⟨hx.1, hx.2.trans hyb.le⟩
  have hdiff : DifferentiableOn ℝ f (Ioo a y) := by
    intro c hc
    exact (differentiableAt_of_deriv_ne_zero (ne_of_gt (hderivPos c hc))).differentiableWithinAt
  obtain ⟨c, hc, hceq⟩ := exists_deriv_eq_slope f hay hcont' hdiff
  have hcpos := hderivPos c hc
  have hyMem : y ∈ Icc a b := ⟨hay.le, hyb.le⟩
  have hfy : f y ≤ f a := hmax hyMem
  have hslope : (f y - f a) / (y - a) ≤ 0 := by
    exact div_nonpos_of_nonpos_of_nonneg (sub_nonpos.mpr hfy) (sub_nonneg.mpr hay.le)
  rw [hceq] at hcpos
  linarith

/-- Right-endpoint analogue for a global maximum. -/
theorem secondDeriv_nonpos_at_right_endpoint_of_isMaxOn_of_deriv_zero
    {f : ℝ → ℝ} {a b : ℝ}
    (hab : a < b)
    (hmax : IsMaxOn f (Icc a b) b)
    (hcont : ContinuousOn f (Icc a b))
    (hderiv0 : deriv f b = 0) :
    deriv (deriv f) b ≤ 0 := by
  by_contra hnot
  have hsec : 0 < deriv (deriv f) b := lt_of_not_ge hnot
  have hsign := eventually_nhdsWithin_sign_eq_of_deriv_pos
    (f := deriv f) hsec hderiv0
  rcases Metric.eventually_nhds_iff_ball.mp hsign with ⟨r, hr, hsignr⟩
  rcases choose_small_step hab hr with ⟨d, hd, hdr, hdab⟩
  let x : ℝ := b - d
  have hax : a < x := by dsimp [x]; linarith
  have hxb : x < b := by dsimp [x]; linarith
  have hderivNeg : ∀ c ∈ Ioo x b, deriv f c < 0 := by
    intro c hc
    have hcball : c ∈ Metric.ball b r := by
      rw [Metric.mem_ball, Real.dist_eq]
      have hcb : c - b < 0 := sub_neg.mpr hc.2
      rw [abs_of_neg hcb]
      have hbcr : -(c - b) < r := by
        dsimp [x] at hc
        linarith [hc.1, hdr]
      exact hbcr
    have hs := hsignr c hcball
    have hcb : c - b < 0 := sub_neg.mpr hc.2
    have hs' : SignType.sign (deriv f c) = -1 := by
      simpa [sign_neg hcb] using hs
    exact sign_eq_neg_one_iff.mp hs'
  have hcont' : ContinuousOn f (Icc x b) := by
    apply hcont.mono
    intro y hy
    exact ⟨hax.le.trans hy.1, hy.2⟩
  have hdiff : DifferentiableOn ℝ f (Ioo x b) := by
    intro c hc
    exact (differentiableAt_of_deriv_ne_zero (ne_of_lt (hderivNeg c hc))).differentiableWithinAt
  obtain ⟨c, hc, hceq⟩ := exists_deriv_eq_slope f hxb hcont' hdiff
  have hcneg := hderivNeg c hc
  have hxMem : x ∈ Icc a b := ⟨hax.le, hxb.le⟩
  have hfx : f x ≤ f b := hmax hxMem
  have hslope : 0 ≤ (f b - f x) / (b - x) := by
    exact div_nonneg (sub_nonneg.mpr hfx) (sub_nonneg.mpr hxb.le)
  rw [hceq] at hcneg
  linarith

/-- At the left endpoint, a global minimum and zero Neumann derivative force
nonnegative second derivative. -/
theorem secondDeriv_nonneg_at_left_endpoint_of_isMinOn_of_deriv_zero
    {f : ℝ → ℝ} {a b : ℝ}
    (hab : a < b)
    (hmin : IsMinOn f (Icc a b) a)
    (hcont : ContinuousOn f (Icc a b))
    (hderiv0 : deriv f a = 0) :
    0 ≤ deriv (deriv f) a := by
  by_contra hnot
  have hsec : deriv (deriv f) a < 0 := lt_of_not_ge hnot
  have hsign := eventually_nhdsWithin_sign_eq_of_deriv_neg
    (f := deriv f) hsec hderiv0
  rcases Metric.eventually_nhds_iff_ball.mp hsign with ⟨r, hr, hsignr⟩
  rcases choose_small_step hab hr with ⟨d, hd, hdr, hdab⟩
  let y : ℝ := a + d
  have hay : a < y := by dsimp [y]; linarith
  have hyb : y < b := by dsimp [y]; linarith
  have hderivNeg : ∀ c ∈ Ioo a y, deriv f c < 0 := by
    intro c hc
    have hcball : c ∈ Metric.ball a r := by
      rw [Metric.mem_ball, Real.dist_eq]
      have hca : 0 < c - a := sub_pos.mpr hc.1
      rw [abs_of_pos hca]
      have hcar : c - a < r := by
        dsimp [y] at hc
        linarith [hc.2, hdr]
      exact hcar
    have hs := hsignr c hcball
    have hac : a - c < 0 := sub_neg.mpr hc.1
    have hs' : SignType.sign (deriv f c) = -1 := by
      simpa [sign_neg hac] using hs
    exact sign_eq_neg_one_iff.mp hs'
  have hcont' : ContinuousOn f (Icc a y) := by
    apply hcont.mono
    intro x hx
    exact ⟨hx.1, hx.2.trans hyb.le⟩
  have hdiff : DifferentiableOn ℝ f (Ioo a y) := by
    intro c hc
    exact (differentiableAt_of_deriv_ne_zero (ne_of_lt (hderivNeg c hc))).differentiableWithinAt
  obtain ⟨c, hc, hceq⟩ := exists_deriv_eq_slope f hay hcont' hdiff
  have hcneg := hderivNeg c hc
  have hyMem : y ∈ Icc a b := ⟨hay.le, hyb.le⟩
  have hfy : f a ≤ f y := hmin hyMem
  have hslope : 0 ≤ (f y - f a) / (y - a) := by
    exact div_nonneg (sub_nonneg.mpr hfy) (sub_nonneg.mpr hay.le)
  rw [hceq] at hcneg
  linarith

/-- Right-endpoint analogue for a global minimum. -/
theorem secondDeriv_nonneg_at_right_endpoint_of_isMinOn_of_deriv_zero
    {f : ℝ → ℝ} {a b : ℝ}
    (hab : a < b)
    (hmin : IsMinOn f (Icc a b) b)
    (hcont : ContinuousOn f (Icc a b))
    (hderiv0 : deriv f b = 0) :
    0 ≤ deriv (deriv f) b := by
  by_contra hnot
  have hsec : deriv (deriv f) b < 0 := lt_of_not_ge hnot
  have hsign := eventually_nhdsWithin_sign_eq_of_deriv_neg
    (f := deriv f) hsec hderiv0
  rcases Metric.eventually_nhds_iff_ball.mp hsign with ⟨r, hr, hsignr⟩
  rcases choose_small_step hab hr with ⟨d, hd, hdr, hdab⟩
  let x : ℝ := b - d
  have hax : a < x := by dsimp [x]; linarith
  have hxb : x < b := by dsimp [x]; linarith
  have hderivPos : ∀ c ∈ Ioo x b, 0 < deriv f c := by
    intro c hc
    have hcball : c ∈ Metric.ball b r := by
      rw [Metric.mem_ball, Real.dist_eq]
      have hcb : c - b < 0 := sub_neg.mpr hc.2
      rw [abs_of_neg hcb]
      have hbcr : -(c - b) < r := by
        dsimp [x] at hc
        linarith [hc.1, hdr]
      exact hbcr
    have hs := hsignr c hcball
    have hbc : 0 < b - c := sub_pos.mpr hc.2
    have hs' : SignType.sign (deriv f c) = 1 := by
      simpa [sign_pos hbc] using hs
    exact sign_eq_one_iff.mp hs'
  have hcont' : ContinuousOn f (Icc x b) := by
    apply hcont.mono
    intro y hy
    exact ⟨hax.le.trans hy.1, hy.2⟩
  have hdiff : DifferentiableOn ℝ f (Ioo x b) := by
    intro c hc
    exact (differentiableAt_of_deriv_ne_zero (ne_of_gt (hderivPos c hc))).differentiableWithinAt
  obtain ⟨c, hc, hceq⟩ := exists_deriv_eq_slope f hxb hcont' hdiff
  have hcpos := hderivPos c hc
  have hxMem : x ∈ Icc a b := ⟨hax.le, hxb.le⟩
  have hfx : f b ≤ f x := hmin hxMem
  have hslope : (f b - f x) / (b - x) ≤ 0 := by
    exact div_nonpos_of_nonpos_of_nonneg (sub_nonpos.mpr hfx) (sub_nonneg.mpr hxb.le)
  rw [hceq] at hcpos
  linarith

end AMLStabilization

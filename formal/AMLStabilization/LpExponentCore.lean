import Mathlib

namespace AMLStabilization

/-- The Hölder partner `s` determined by `1/r = 1/p + 1/s`. -/
noncomputable def holderPartner (p r : ℝ) : ℝ :=
  p * r / (p - r)

/-- Lower threshold used to choose an exponent `r` suitable both for
Neumann gradient smoothing (`r > n`) and for obtaining a Hölder partner
`s >= 2`. -/
noncomputable def lpLowerThreshold (n p : ℝ) : ℝ :=
  max n (2 * p / (p + 2))

/-- Canonical midpoint choice of the spatial exponent `r`. -/
noncomputable def lpChoice (n p : ℝ) : ℝ :=
  (lpLowerThreshold n p + p) / 2

/-- If `p > 2`, then the threshold `2p/(p+2)` lies strictly below `p`. -/
theorem two_mul_p_div_p_add_two_lt_p
    {p : ℝ} (hp : 2 < p) :
    2 * p / (p + 2) < p := by
  have hp0 : 0 < p := lt_trans (by norm_num) hp
  have hden : 0 < p + 2 := by linarith
  rw [div_lt_iff₀ hden]
  nlinarith [sq_pos_of_pos hp0]

/-- The combined lower threshold lies below `p` whenever `p > max n 2`. -/
theorem lpLowerThreshold_lt_p
    {n p : ℝ} (hp : max n 2 < p) :
    lpLowerThreshold n p < p := by
  unfold lpLowerThreshold
  have hn : n < p := lt_of_le_of_lt (le_max_left n 2) hp
  have h2 : 2 < p := lt_of_le_of_lt (le_max_right n 2) hp
  exact max_lt hn (two_mul_p_div_p_add_two_lt_p h2)

/-- The midpoint choice lies strictly between the lower threshold and `p`. -/
theorem lpChoice_between
    {n p : ℝ} (hp : max n 2 < p) :
    lpLowerThreshold n p < lpChoice n p ∧ lpChoice n p < p := by
  have hlow := lpLowerThreshold_lt_p hp
  unfold lpChoice
  constructor <;> linarith

/-- In particular, the chosen exponent satisfies `n < r < p`. -/
theorem lpChoice_gt_n_and_lt_p
    {n p : ℝ} (hp : max n 2 < p) :
    n < lpChoice n p ∧ lpChoice n p < p := by
  obtain ⟨hlow, hrp⟩ := lpChoice_between hp
  have hnlow : n ≤ lpLowerThreshold n p := by
    unfold lpLowerThreshold
    exact le_max_left _ _
  exact ⟨lt_of_le_of_lt hnlow hlow, hrp⟩

/-- The choice also satisfies the precise lower bound ensuring that its
Hölder partner is at least two. -/
theorem two_mul_p_div_p_add_two_lt_lpChoice
    {n p : ℝ} (hp : max n 2 < p) :
    2 * p / (p + 2) < lpChoice n p := by
  obtain ⟨hlow, _⟩ := lpChoice_between hp
  have hthreshold : 2 * p / (p + 2) ≤ lpLowerThreshold n p := by
    unfold lpLowerThreshold
    exact le_max_right _ _
  exact lt_of_le_of_lt hthreshold hlow

/-- For `0 < r < p`, the algebraic Hölder identity holds exactly. -/
theorem holderPartner_identity
    {p r : ℝ}
    (hr0 : 0 < r) (hrp : r < p) :
    1 / r = 1 / p + 1 / holderPartner p r := by
  have hp0 : 0 < p := lt_trans hr0 hrp
  have hpr : 0 < p - r := sub_pos.mpr hrp
  unfold holderPartner
  field_simp [ne_of_gt hr0, ne_of_gt hp0, ne_of_gt hpr]
  ring

/-- The threshold `r > 2p/(p+2)` is equivalent to the Hölder partner being
strictly larger than two, under `0 < r < p`. -/
theorem two_lt_holderPartner_of_threshold
    {p r : ℝ}
    (hp : 2 < p)
    (hrp : r < p)
    (hthreshold : 2 * p / (p + 2) < r) :
    2 < holderPartner p r := by
  have hp0 : 0 < p := lt_trans (by norm_num) hp
  have hden : 0 < p + 2 := by linarith
  have hr0 : 0 < r := by
    have hfrac0 : 0 < 2 * p / (p + 2) := div_pos (mul_pos (by norm_num) hp0) hden
    exact lt_trans hfrac0 hthreshold
  have hpr : 0 < p - r := sub_pos.mpr hrp
  unfold holderPartner
  rw [lt_div_iff₀ hpr]
  have hthreshold' : 2 * p < r * (p + 2) := by
    rwa [div_lt_iff₀ hden] at hthreshold
  nlinarith

/-- Complete exponent package used in the strengthened eventual-`L^p`
stabilization theorem. -/
theorem lpChoice_exponent_package
    {n p : ℝ} (hp : max n 2 < p) :
    n < lpChoice n p ∧
    lpChoice n p < p ∧
    2 < holderPartner p (lpChoice n p) ∧
    1 / lpChoice n p =
      1 / p + 1 / holderPartner p (lpChoice n p) := by
  obtain ⟨hrn, hrp⟩ := lpChoice_gt_n_and_lt_p hp
  have h2 : 2 < p := lt_of_le_of_lt (le_max_right n 2) hp
  have hthreshold := two_mul_p_div_p_add_two_lt_lpChoice hp
  have hp0 : 0 < p := lt_trans (by norm_num) h2
  have hr0 : 0 < lpChoice n p := lt_trans (by linarith) hrn
  refine ⟨hrn, hrp, ?_, ?_⟩
  · exact two_lt_holderPartner_of_threshold h2 hrp hthreshold
  · exact holderPartner_identity hr0 hrp

/-- The transfer exponent appearing after Hölder interpolation. -/
noncomputable def transferRate (theta p r : ℝ) : ℝ :=
  2 * (p - r) / (theta * p * r)

/-- Under the natural sign conditions, the transfer exponent is positive. -/
theorem transferRate_pos
    {theta p r : ℝ}
    (htheta : 0 < theta) (hr0 : 0 < r) (hrp : r < p) :
    0 < transferRate theta p r := by
  unfold transferRate
  have hp0 : 0 < p := lt_trans hr0 hrp
  positivity

end AMLStabilization

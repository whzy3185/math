import Mathlib

namespace AMLStabilization

/-- A concrete finite time exponent for the mixed-norm parabolic step.
The choice is arranged so that `n / p + 2 / Q < 1` whenever `n < p`. -/
noncomputable def mixedTimeExponent (n p : ℝ) : ℝ :=
  4 * p / (p - n)

/-- Under the eventual finite-`L^p` hypothesis, the chosen time exponent is strictly larger than two. -/
theorem two_lt_mixedTimeExponent
    {n p : ℝ}
    (hn : 0 ≤ n) (hp : max n 2 < p) :
    2 < mixedTimeExponent n p := by
  have hnp : n < p := lt_of_le_of_lt (le_max_left n 2) hp
  have h2p : 2 < p := lt_of_le_of_lt (le_max_right n 2) hp
  have hp0 : 0 < p := lt_trans (by norm_num) h2p
  have hpn : 0 < p - n := sub_pos.mpr hnp
  unfold mixedTimeExponent
  rw [lt_div_iff₀ hpn]
  nlinarith

/-- The explicit choice `Q = 4p/(p-n)` satisfies the strict parabolic mixed-norm condition. -/
theorem mixedTimeExponent_subcritical
    {n p : ℝ}
    (hn : 0 ≤ n) (hp : max n 2 < p) :
    n / p + 2 / mixedTimeExponent n p < 1 := by
  have hnp : n < p := lt_of_le_of_lt (le_max_left n 2) hp
  have h2p : 2 < p := lt_of_le_of_lt (le_max_right n 2) hp
  have hp0 : 0 < p := lt_trans (by norm_num) h2p
  have hpn : 0 < p - n := sub_pos.mpr hnp
  have hrecip :
      2 / mixedTimeExponent n p = (p - n) / (2 * p) := by
    unfold mixedTimeExponent
    field_simp [ne_of_gt hp0, ne_of_gt hpn]
    ring
  rw [hrecip]
  have hid :
      n / p + (p - n) / (2 * p) = (p + n) / (2 * p) := by
    field_simp [ne_of_gt hp0]
    ring
  rw [hid]
  have h2p0 : 0 < 2 * p := mul_pos (by norm_num) hp0
  rw [div_lt_iff₀ h2p0]
  nlinarith

/-- Complete mixed-norm exponent package used by the Choi/conormal upgrade stage. -/
theorem mixedTimeExponent_package
    {n p : ℝ}
    (hn : 0 ≤ n) (hp : max n 2 < p) :
    2 < mixedTimeExponent n p ∧
    n / p + 2 / mixedTimeExponent n p < 1 := by
  exact ⟨two_lt_mixedTimeExponent hn hp,
    mixedTimeExponent_subcritical hn hp⟩

/-- In spatial dimension one, the standard cylinder lift to `Omega × (0,1)`
has effective dimension two.  Thus the manuscript assumption `p > 2` is
exactly enough to choose a finite mixed time exponent after the lift. -/
theorem oneDimensionalLift_mixedTimeExponent_package
    {p : ℝ} (hp : 2 < p) :
    2 < mixedTimeExponent 2 p ∧
    2 / p + 2 / mixedTimeExponent 2 p < 1 := by
  have hpmax : max (2 : ℝ) 2 < p := by simpa using hp
  exact mixedTimeExponent_package (n := 2) (p := p) (by norm_num) hpmax

end AMLStabilization

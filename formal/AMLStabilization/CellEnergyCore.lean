import Mathlib

namespace AMLStabilization

/-- Exact Young estimate used in the cell-density `L²` energy balance. -/
theorem young_gradient_forcing
    {a H g : ℝ}
    (ha : 0 < a) (hH : 0 ≤ H) (hg : 0 ≤ g) :
    2 * H * g ≤ a * g ^ 2 + H ^ 2 / a := by
  have hsquare : 0 ≤ (a * g - H) ^ 2 := sq_nonneg _
  have hmul :
      (2 * H * g) * a ≤ (a * g ^ 2 + H ^ 2 / a) * a := by
    field_simp [ne_of_gt ha]
    nlinarith
  exact le_of_mul_le_mul_right hmul ha

/-- A cell-energy balance closes to a forced scalar ODE by Young and Poincare. -/
theorem cellEnergy_to_forcedLinearODE
    {dQ Q g H a Cp : ℝ}
    (ha : 0 < a) (hCp : 0 < Cp)
    (hQ : 0 ≤ Q) (hg : 0 ≤ g) (hH : 0 ≤ H)
    (hPoincare : Q ≤ Cp ^ 2 * g ^ 2)
    (henergy : dQ + 2 * a * g ^ 2 ≤ 2 * H * g) :
    dQ + (a / Cp ^ 2) * Q ≤ H ^ 2 / a := by
  have hyoung := young_gradient_forcing ha hH hg
  have hgrad : dQ + a * g ^ 2 ≤ H ^ 2 / a := by
    linarith [henergy, hyoung]
  have hCpSq : 0 < Cp ^ 2 := pow_pos hCp 2
  have hscale : (a / Cp ^ 2) * Q ≤ a * g ^ 2 := by
    have hdiv := mul_le_mul_of_nonneg_left hPoincare (div_nonneg (le_of_lt ha) hCpSq.le)
    calc
      (a / Cp ^ 2) * Q ≤ (a / Cp ^ 2) * (Cp ^ 2 * g ^ 2) := hdiv
      _ = a * g ^ 2 := by field_simp [ne_of_gt hCpSq]
  linarith

/-- Squaring an exponential forcing doubles its exponent. -/
theorem square_exponential_forcing
    {H C lambda T t : ℝ}
    (hH0 : 0 ≤ H) (hC : 0 ≤ C)
    (hH : H ≤ C * Real.exp (-lambda * (t - T))) :
    H ^ 2 ≤ C ^ 2 * Real.exp (-(2 * lambda) * (t - T)) := by
  have hexp0 : 0 ≤ Real.exp (-lambda * (t - T)) := Real.exp_nonneg _
  have hrhs0 : 0 ≤ C * Real.exp (-lambda * (t - T)) := mul_nonneg hC hexp0
  have hsq := (sq_le_sq₀ hH0 hrhs0).2 hH
  have hexpsq :
      Real.exp (-lambda * (t - T)) ^ 2 =
        Real.exp (-(2 * lambda) * (t - T)) := by
    rw [pow_two, ← Real.exp_add]
    congr 1
    ring
  calc
    H ^ 2 ≤ (C * Real.exp (-lambda * (t - T))) ^ 2 := hsq
    _ = C ^ 2 * Real.exp (-lambda * (t - T)) ^ 2 := by rw [mul_pow]
    _ = C ^ 2 * Real.exp (-(2 * lambda) * (t - T)) := by rw [hexpsq]

end AMLStabilization

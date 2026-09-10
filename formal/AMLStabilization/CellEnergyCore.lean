import Mathlib

namespace AMLStabilization

/-- Exact Young estimate used in the cell-density `L²` energy balance. -/
theorem young_gradient_forcing
    {a H g : ℝ}
    (ha : 0 < a) (hH : 0 ≤ H) (hg : 0 ≤ g) :
    2 * H * g ≤ a * g ^ 2 + H ^ 2 / a := by
  have hsquare : 0 ≤ (Real.sqrt a * g - H / Real.sqrt a) ^ 2 := sq_nonneg _
  have hsqrt : 0 < Real.sqrt a := Real.sqrt_pos.2 ha
  have hsqrtSq : (Real.sqrt a) ^ 2 = a := Real.sq_sqrt (le_of_lt ha)
  field_simp [ne_of_gt hsqrt, ne_of_gt ha] at hsquare ⊢
  nlinarith

/--
A cell-energy balance with a linear gradient forcing closes to a forced scalar
ODE by Young and Poincare.  `g` is the gradient `L²` norm and `H` is the size
of the decaying coefficient multiplying it.
-/
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
  calc
    H ^ 2 ≤ (C * Real.exp (-lambda * (t - T))) ^ 2 := hsq
    _ = C ^ 2 * Real.exp (-(2 * lambda) * (t - T)) := by
      rw [mul_pow, ← Real.exp_nat_mul]
      congr 1
      ring

end AMLStabilization

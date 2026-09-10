import Mathlib
import AMLStabilization.CellEnergyCore
import AMLStabilization.ForcedEnergyDecay
import AMLStabilization.PolynomialForcedEnergyDecay

namespace AMLStabilization

/-- Time-dependent cell `L²` energy assembly with exponentially decaying coefficient forcing. -/
theorem cellEnergy_exponentialDecay_from_gradientRate
    {Q dQ g H : ℝ → ℝ}
    {a Cp CH lambda T s t : ℝ}
    (ha : 0 < a) (hCp : 0 < Cp) (hCH : 0 ≤ CH) (hlambda : 0 < lambda)
    (hrate : 2 * lambda < a / Cp ^ 2)
    (hQderiv : ∀ τ, HasDerivAt Q (dQ τ) τ)
    (hQ0 : ∀ τ, 0 ≤ Q τ) (hg0 : ∀ τ, 0 ≤ g τ) (hH0 : ∀ τ, 0 ≤ H τ)
    (hPoincare : ∀ τ, Q τ ≤ Cp ^ 2 * g τ ^ 2)
    (henergy : ∀ τ, dQ τ + 2 * a * g τ ^ 2 ≤ 2 * H τ * g τ)
    (hHrate : ∀ τ, H τ ≤ CH * Real.exp (-lambda * (τ - T)))
    (hst : s ≤ t) :
    Q t ≤
      (Q s - exponentialBarrier (a / Cp ^ 2) (2 * lambda) (CH ^ 2 / a) *
          Real.exp (-(2 * lambda) * (s - T))) *
        Real.exp (-(a / Cp ^ 2) * (t - s)) +
      exponentialBarrier (a / Cp ^ 2) (2 * lambda) (CH ^ 2 / a) *
        Real.exp (-(2 * lambda) * (t - T)) := by
  have hdamp : 0 < a / Cp ^ 2 := div_pos ha (pow_pos hCp 2)
  have hb : 0 < 2 * lambda := mul_pos (by norm_num) hlambda
  let Cbase : ℝ := CH ^ 2 / a
  let C0 : ℝ := Cbase * Real.exp ((2 * lambda) * T)
  have hforced0 : ∀ τ,
      dQ τ + (a / Cp ^ 2) * Q τ ≤ C0 * Real.exp (-(2 * lambda) * τ) := by
    intro τ
    have hcell := cellEnergy_to_forcedLinearODE ha hCp (hQ0 τ) (hg0 τ) (hH0 τ)
      (hPoincare τ) (henergy τ)
    have hsq := square_exponential_forcing (hH0 τ) hCH (hHrate τ)
    have hscale : H τ ^ 2 / a ≤
        Cbase * Real.exp (-(2 * lambda) * (τ - T)) := by
      have hdiv := div_le_div_of_nonneg_right hsq (le_of_lt ha)
      simpa [Cbase, div_eq_mul_inv, mul_assoc, mul_left_comm, mul_comm] using hdiv
    have hexpShift :
        Real.exp (-(2 * lambda) * (τ - T)) =
          Real.exp ((2 * lambda) * T) * Real.exp (-(2 * lambda) * τ) := by
      rw [← Real.exp_add]
      congr 1
      ring
    have hshift :
        Cbase * Real.exp (-(2 * lambda) * (τ - T)) =
          C0 * Real.exp (-(2 * lambda) * τ) := by
      rw [hexpShift]
      simp only [C0]
      ring
    exact hcell.trans (hscale.trans_eq hshift)
  have hmain := forcedEnergy_exponential_bound
    hdamp hb hrate hQderiv hforced0 hst
  have hbar :
      exponentialBarrier (a / Cp ^ 2) (2 * lambda) C0 =
        exponentialBarrier (a / Cp ^ 2) (2 * lambda) Cbase *
          Real.exp ((2 * lambda) * T) := by
    dsimp [C0]
    unfold exponentialBarrier
    ring
  rw [hbar] at hmain
  have hshiftSFull :
      exponentialBarrier (a / Cp ^ 2) (2 * lambda) Cbase *
          Real.exp ((2 * lambda) * T) * Real.exp (-(2 * lambda) * s) =
        exponentialBarrier (a / Cp ^ 2) (2 * lambda) Cbase *
          Real.exp (-(2 * lambda) * (s - T)) := by
    rw [mul_assoc]
    congr 1
    rw [← Real.exp_add]
    congr 1
    ring
  have hshiftTFull :
      exponentialBarrier (a / Cp ^ 2) (2 * lambda) Cbase *
          Real.exp ((2 * lambda) * T) * Real.exp (-(2 * lambda) * t) =
        exponentialBarrier (a / Cp ^ 2) (2 * lambda) Cbase *
          Real.exp (-(2 * lambda) * (t - T)) := by
    rw [mul_assoc]
    congr 1
    rw [← Real.exp_add]
    congr 1
    ring
  rw [hshiftSFull, hshiftTFull] at hmain
  simpa [Cbase] using hmain

/-- Squaring a polynomial coefficient rate doubles its exponent. -/
theorem square_polynomial_forcing
    {H C b T t : ℝ}
    (hb : 0 ≤ b) (hTt : T ≤ t)
    (hH0 : 0 ≤ H) (hC : 0 ≤ C)
    (hH : H ≤ C * (1 + (t - T)) ^ (-b)) :
    H ^ 2 ≤ C ^ 2 * (1 + (t - T)) ^ (-(2 * b)) := by
  have hbase : 0 < 1 + (t - T) := by linarith
  have hrhs0 : 0 ≤ C * (1 + (t - T)) ^ (-b) :=
    mul_nonneg hC (Real.rpow_nonneg (le_of_lt hbase) _)
  have hsq := (sq_le_sq₀ hH0 hrhs0).2 hH
  have hpowsq :
      ((1 + (t - T)) ^ (-b)) ^ 2 =
        (1 + (t - T)) ^ (-(2 * b)) := by
    rw [pow_two, ← Real.rpow_add hbase]
    congr 1
    ring
  calc
    H ^ 2 ≤ (C * (1 + (t - T)) ^ (-b)) ^ 2 := hsq
    _ = C ^ 2 * ((1 + (t - T)) ^ (-b)) ^ 2 := by rw [mul_pow]
    _ = C ^ 2 * (1 + (t - T)) ^ (-(2 * b)) := by rw [hpowsq]

/-- Time-dependent cell `L²` assembly for polynomially decaying coefficient forcing. -/
theorem cellEnergy_polynomialDecay_from_gradientRate
    {Q dQ g H : ℝ → ℝ}
    {a Cp CH b T t : ℝ}
    (ha : 0 < a) (hCp : 0 < Cp) (hCH : 0 ≤ CH) (hb : 0 < b)
    (hrate : 2 * b < a / Cp ^ 2)
    (hTt : T ≤ t)
    (hQderiv : ∀ τ ∈ Set.Icc T t, HasDerivAt Q (dQ τ) τ)
    (hQ0 : ∀ τ ∈ Set.Icc T t, 0 ≤ Q τ)
    (hg0 : ∀ τ ∈ Set.Icc T t, 0 ≤ g τ)
    (hH0 : ∀ τ ∈ Set.Icc T t, 0 ≤ H τ)
    (hPoincare : ∀ τ ∈ Set.Icc T t, Q τ ≤ Cp ^ 2 * g τ ^ 2)
    (henergy : ∀ τ ∈ Set.Icc T t,
      dQ τ + 2 * a * g τ ^ 2 ≤ 2 * H τ * g τ)
    (hHrate : ∀ τ ∈ Set.Icc T t,
      H τ ≤ CH * (1 + (τ - T)) ^ (-b)) :
    Q t ≤
      (Q T - polynomialBarrier (a / Cp ^ 2) (2 * b) (CH ^ 2 / a)) *
          Real.exp (-(a / Cp ^ 2) * (t - T)) +
        polynomialBarrier (a / Cp ^ 2) (2 * b) (CH ^ 2 / a) *
          (1 + (t - T)) ^ (-(2 * b)) := by
  have hdamp : 0 < a / Cp ^ 2 := div_pos ha (pow_pos hCp 2)
  have hb2 : 0 < 2 * b := mul_pos (by norm_num) hb
  have hforce : ∀ τ ∈ Set.Icc T t,
      dQ τ + (a / Cp ^ 2) * Q τ ≤
        (CH ^ 2 / a) * (1 + (τ - T)) ^ (-(2 * b)) := by
    intro τ hτ
    have hcell := cellEnergy_to_forcedLinearODE ha hCp (hQ0 τ hτ) (hg0 τ hτ)
      (hH0 τ hτ) (hPoincare τ hτ) (henergy τ hτ)
    have hsq := square_polynomial_forcing (le_of_lt hb) hτ.1 (hH0 τ hτ) hCH (hHrate τ hτ)
    have hdiv := div_le_div_of_nonneg_right hsq (le_of_lt ha)
    exact hcell.trans (by simpa [div_eq_mul_inv, mul_assoc, mul_left_comm, mul_comm] using hdiv)
  exact forcedEnergy_polynomial_bound hdamp hb2 hrate
    (div_nonneg (sq_nonneg CH) (le_of_lt ha)) hTt hQderiv hforce

end AMLStabilization

import Mathlib
import AMLStabilization.CellEnergyAssembly
import AMLStabilization.RateComparisonCore

namespace AMLStabilization

/-- The two-term exponential cell-energy estimate is bounded by a single slower exponential envelope. -/
theorem cellEnergy_exponentialEnvelope_from_gradientRate
    {Q dQ g H : ℝ → ℝ}
    {a Cp CH lambda T t : ℝ}
    (ha : 0 < a) (hCp : 0 < Cp) (hCH : 0 ≤ CH) (hlambda : 0 < lambda)
    (hrate : 2 * lambda < a / Cp ^ 2)
    (hTt : T ≤ t)
    (hQderiv : ∀ tau, HasDerivAt Q (dQ tau) tau)
    (hQ0 : ∀ tau, 0 ≤ Q tau) (hg0 : ∀ tau, 0 ≤ g tau) (hH0 : ∀ tau, 0 ≤ H tau)
    (hPoincare : ∀ tau, Q tau ≤ Cp ^ 2 * g tau ^ 2)
    (henergy : ∀ tau, dQ tau + 2 * a * g tau ^ 2 ≤ 2 * H tau * g tau)
    (hHrate : ∀ tau, H tau ≤ CH * Real.exp (-lambda * (tau - T))) :
    Q t ≤
      (Q T + exponentialBarrier (a / Cp ^ 2) (2 * lambda) (CH ^ 2 / a)) *
        Real.exp (-(2 * lambda) * (t - T)) := by
  let damp : ℝ := a / Cp ^ 2
  let B : ℝ := exponentialBarrier damp (2 * lambda) (CH ^ 2 / a)
  have hdamp : 0 < damp := by dsimp [damp]; positivity
  have hden : 0 < damp - 2 * lambda := sub_pos.mpr (by simpa [damp] using hrate)
  have hB0 : 0 ≤ B := by
    dsimp [B]
    unfold exponentialBarrier
    exact div_nonneg (div_nonneg (sq_nonneg CH) ha.le) hden.le
  have hmain := cellEnergy_exponentialDecay_from_gradientRate
    (Q := Q) (dQ := dQ) (g := g) (H := H)
    (a := a) (Cp := Cp) (CH := CH) (lambda := lambda)
    (T := T) (s := T) (t := t)
    ha hCp hCH hlambda hrate hQderiv hQ0 hg0 hH0 hPoincare henergy hHrate hTt
  have hmain' : Q t ≤
      (Q T - B) * Real.exp (-damp * (t - T)) +
        B * Real.exp (-(2 * lambda) * (t - T)) := by
    simpa [B, damp] using hmain
  have hx : 0 ≤ t - T := sub_nonneg.mpr hTt
  have hexpCmp :
      Real.exp (-damp * (t - T)) ≤ Real.exp (-(2 * lambda) * (t - T)) := by
    apply Real.exp_le_exp.mpr
    have hdle : 2 * lambda ≤ damp := hden.le_sub_iff_add_le.mp (by linarith)
    nlinarith
  have hdrop :
      (Q T - B) * Real.exp (-damp * (t - T)) ≤
        Q T * Real.exp (-damp * (t - T)) := by
    exact mul_le_mul_of_nonneg_right (sub_le_self _ hB0) (Real.exp_nonneg _)
  have hslow :
      Q T * Real.exp (-damp * (t - T)) ≤
        Q T * Real.exp (-(2 * lambda) * (t - T)) :=
    mul_le_mul_of_nonneg_left hexpCmp (hQ0 T)
  calc
    Q t ≤ (Q T - B) * Real.exp (-damp * (t - T)) +
        B * Real.exp (-(2 * lambda) * (t - T)) := hmain'
    _ ≤ Q T * Real.exp (-(2 * lambda) * (t - T)) +
        B * Real.exp (-(2 * lambda) * (t - T)) :=
      add_le_add (hdrop.trans hslow) le_rfl
    _ = (Q T + B) * Real.exp (-(2 * lambda) * (t - T)) := by ring
    _ = (Q T + exponentialBarrier (a / Cp ^ 2) (2 * lambda) (CH ^ 2 / a)) *
        Real.exp (-(2 * lambda) * (t - T)) := by rfl

/-- The two-term polynomial cell-energy estimate is bounded by a single polynomial envelope. -/
theorem cellEnergy_polynomialEnvelope_from_gradientRate
    {Q dQ g H : ℝ → ℝ}
    {a Cp CH b T t : ℝ}
    (ha : 0 < a) (hCp : 0 < Cp) (hCH : 0 ≤ CH) (hb : 0 < b)
    (hrate : 2 * b < a / Cp ^ 2)
    (hTt : T ≤ t)
    (hQderiv : ∀ tau ∈ Set.Icc T t, HasDerivAt Q (dQ tau) tau)
    (hQ0 : ∀ tau ∈ Set.Icc T t, 0 ≤ Q tau)
    (hg0 : ∀ tau ∈ Set.Icc T t, 0 ≤ g tau)
    (hH0 : ∀ tau ∈ Set.Icc T t, 0 ≤ H tau)
    (hPoincare : ∀ tau ∈ Set.Icc T t, Q tau ≤ Cp ^ 2 * g tau ^ 2)
    (henergy : ∀ tau ∈ Set.Icc T t,
      dQ tau + 2 * a * g tau ^ 2 ≤ 2 * H tau * g tau)
    (hHrate : ∀ tau ∈ Set.Icc T t,
      H tau ≤ CH * (1 + (tau - T)) ^ (-b)) :
    Q t ≤
      (Q T + polynomialBarrier (a / Cp ^ 2) (2 * b) (CH ^ 2 / a)) *
        (1 + (t - T)) ^ (-(2 * b)) := by
  let damp : ℝ := a / Cp ^ 2
  let B : ℝ := polynomialBarrier damp (2 * b) (CH ^ 2 / a)
  have hdamp : 0 < damp := by dsimp [damp]; positivity
  have hden : 0 < damp - 2 * b := sub_pos.mpr (by simpa [damp] using hrate)
  have hB0 : 0 ≤ B := by
    dsimp [B]
    unfold polynomialBarrier
    exact div_nonneg (div_nonneg (sq_nonneg CH) ha.le) hden.le
  have hmain := cellEnergy_polynomialDecay_from_gradientRate
    (Q := Q) (dQ := dQ) (g := g) (H := H)
    (a := a) (Cp := Cp) (CH := CH) (b := b) (T := T) (t := t)
    ha hCp hCH hb hrate hTt hQderiv hQ0 hg0 hH0 hPoincare henergy hHrate
  have hmain' : Q t ≤
      (Q T - B) * Real.exp (-damp * (t - T)) +
        B * (1 + (t - T)) ^ (-(2 * b)) := by
    simpa [B, damp] using hmain
  have hx : 0 ≤ t - T := sub_nonneg.mpr hTt
  have hpolyCmp :
      Real.exp (-damp * (t - T)) ≤
        (1 + (t - T)) ^ (-(2 * b)) :=
    exp_neg_mul_le_one_add_rpow_neg_of_lt hx (by positivity) (by simpa [damp] using hrate)
  have hdrop :
      (Q T - B) * Real.exp (-damp * (t - T)) ≤
        Q T * Real.exp (-damp * (t - T)) := by
    exact mul_le_mul_of_nonneg_right (sub_le_self _ hB0) (Real.exp_nonneg _)
  have hslow :
      Q T * Real.exp (-damp * (t - T)) ≤
        Q T * (1 + (t - T)) ^ (-(2 * b)) :=
    mul_le_mul_of_nonneg_left hpolyCmp (hQ0 T ⟨le_rfl, hTt⟩)
  calc
    Q t ≤ (Q T - B) * Real.exp (-damp * (t - T)) +
        B * (1 + (t - T)) ^ (-(2 * b)) := hmain'
    _ ≤ Q T * (1 + (t - T)) ^ (-(2 * b)) +
        B * (1 + (t - T)) ^ (-(2 * b)) :=
      add_le_add (hdrop.trans hslow) le_rfl
    _ = (Q T + B) * (1 + (t - T)) ^ (-(2 * b)) := by ring
    _ = (Q T + polynomialBarrier (a / Cp ^ 2) (2 * b) (CH ^ 2 / a)) *
        (1 + (t - T)) ^ (-(2 * b)) := by rfl

end AMLStabilization

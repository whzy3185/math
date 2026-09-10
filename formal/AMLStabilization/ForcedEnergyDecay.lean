import Mathlib
import AMLStabilization.EnergyDecay

namespace AMLStabilization

/-- Exponential barrier coefficient for a linearly damped forced energy. -/
noncomputable def exponentialBarrier (a b C : ℝ) : ℝ := C / (a - b)

/--
If `Q' + a Q <= C exp(-b t)` and `0 < b < a`, subtracting the exact
exponential barrier converts the inequality into homogeneous linear damping.
-/
theorem forcedEnergy_shift_dissipation
    {Q dQ : ℝ → ℝ} {a b C : ℝ}
    (ha : 0 < a) (hb : 0 < b) (hba : b < a)
    (hQ : ∀ t, HasDerivAt Q (dQ t) t)
    (hforce : ∀ t, dQ t + a * Q t ≤ C * Real.exp (-b * t)) :
    (∀ t, HasDerivAt
      (fun x => Q x - exponentialBarrier a b C * Real.exp (-b * x))
      (dQ t + b * exponentialBarrier a b C * Real.exp (-b * t)) t) ∧
    (∀ t,
      (dQ t + b * exponentialBarrier a b C * Real.exp (-b * t)) +
        a * (Q t - exponentialBarrier a b C * Real.exp (-b * t)) ≤ 0) := by
  constructor
  · intro t
    have hlin : HasDerivAt (fun x : ℝ => -b * x) (-b) t :=
      hasDerivAt_const_mul (-b)
    have hexp := hlin.exp
    have hbar := hexp.const_mul (exponentialBarrier a b C)
    have hsub : HasDerivAt
        (fun x => Q x - exponentialBarrier a b C * Real.exp (-b * x))
        (dQ t - exponentialBarrier a b C * (Real.exp (-b * t) * (-b))) t :=
      (hQ t).sub hbar
    convert hsub using 1
    ring
  · intro t
    have hab : 0 < a - b := sub_pos.mpr hba
    have hidentity :
        (a - b) * exponentialBarrier a b C = C := by
      unfold exponentialBarrier
      field_simp [ne_of_gt hab]
    calc
      (dQ t + b * exponentialBarrier a b C * Real.exp (-b * t)) +
          a * (Q t - exponentialBarrier a b C * Real.exp (-b * t)) =
        (dQ t + a * Q t) -
          (a - b) * exponentialBarrier a b C * Real.exp (-b * t) := by ring
      _ ≤ C * Real.exp (-b * t) -
          (a - b) * exponentialBarrier a b C * Real.exp (-b * t) := by
        linarith [hforce t]
      _ = 0 := by rw [hidentity]; ring

/--
Explicit two-rate estimate for a linearly damped energy with exponential forcing.
No positivity assumption on `Q` is needed for the comparison calculation.
-/
theorem forcedEnergy_exponential_bound
    {Q dQ : ℝ → ℝ} {a b C s t : ℝ}
    (ha : 0 < a) (hb : 0 < b) (hba : b < a)
    (hQ : ∀ tau, HasDerivAt Q (dQ tau) tau)
    (hforce : ∀ tau, dQ tau + a * Q tau ≤ C * Real.exp (-b * tau))
    (hst : s ≤ t) :
    Q t ≤
      (Q s - exponentialBarrier a b C * Real.exp (-b * s)) *
        Real.exp (-a * (t - s)) +
      exponentialBarrier a b C * Real.exp (-b * t) := by
  obtain ⟨hYderiv, hYdiss⟩ :=
    forcedEnergy_shift_dissipation ha hb hba hQ hforce
  have hdec := energy_le_exp_of_differential_inequality
    (E := fun tau => Q tau - exponentialBarrier a b C * Real.exp (-b * tau))
    (dE := fun tau => dQ tau + b * exponentialBarrier a b C * Real.exp (-b * tau))
    (c := a) (s := s) (t := t) hYderiv hYdiss hst
  linarith

/-- A simpler positive-coefficient estimate useful for manuscript assembly. -/
theorem forcedEnergy_exponential_bound_of_nonnegative
    {Q dQ : ℝ → ℝ} {a b C s t : ℝ}
    (ha : 0 < a) (hb : 0 < b) (hba : b < a)
    (hC : 0 ≤ C)
    (hQ : ∀ tau, HasDerivAt Q (dQ tau) tau)
    (hforce : ∀ tau, dQ tau + a * Q tau ≤ C * Real.exp (-b * tau))
    (hst : s ≤ t) :
    Q t ≤
      Q s * Real.exp (-a * (t - s)) +
      exponentialBarrier a b C * Real.exp (-b * t) := by
  have hbar0 : 0 ≤ exponentialBarrier a b C := by
    unfold exponentialBarrier
    exact div_nonneg hC (sub_nonneg.mpr hba.le)
  have hfull := forcedEnergy_exponential_bound ha hb hba hQ hforce hst
  have hexp0 := Real.exp_nonneg (-a * (t - s))
  have hdrop :
      (Q s - exponentialBarrier a b C * Real.exp (-b * s)) *
          Real.exp (-a * (t - s)) ≤
        Q s * Real.exp (-a * (t - s)) := by
    apply mul_le_mul_of_nonneg_right _ hexp0
    nlinarith [Real.exp_nonneg (-b * s), hbar0]
  linarith

end AMLStabilization

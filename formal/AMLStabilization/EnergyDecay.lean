import Mathlib

namespace AMLStabilization

/-- Exponentially weighted energy used in the Gronwall argument. -/
noncomputable def weightedEnergy (c : ℝ) (E : ℝ → ℝ) (t : ℝ) : ℝ :=
  Real.exp (c * t) * E t

/--
If `E' + c E ≤ 0` pointwise, then the weighted energy `exp(c t) E(t)`
is antitone.  This is the exact calculus step behind the PDE energy-decay argument.
-/
theorem weightedEnergy_antitone
    {E dE : ℝ → ℝ} {c : ℝ}
    (hE : ∀ t, HasDerivAt E (dE t) t)
    (hdiss : ∀ t, dE t + c * E t ≤ 0) :
    Antitone (weightedEnergy c E) := by
  refine antitone_of_hasDerivAt_nonpos
    (f' := fun t => Real.exp (c * t) * (dE t + c * E t)) ?_ ?_
  · intro t
    unfold weightedEnergy
    have hlin : HasDerivAt (fun x : ℝ => c * x) c t :=
      hasDerivAt_const_mul c
    have hexp :
        HasDerivAt (fun x : ℝ => Real.exp (c * x))
          (c * Real.exp (c * t)) t := by
      simpa [mul_comm] using hlin.exp
    simpa [mul_add, mul_assoc, mul_left_comm, mul_comm, add_comm, add_left_comm, add_assoc] using
      hexp.mul (hE t)
  · intro t
    exact mul_nonpos_of_nonneg_of_nonpos (Real.exp_nonneg _) (hdiss t)

/--
Differential energy inequality implies the two-time exponential comparison
`E(t) ≤ E(s) exp(-c (t-s))` for `s ≤ t`.
-/
theorem energy_le_exp_of_differential_inequality
    {E dE : ℝ → ℝ} {c s t : ℝ}
    (hE : ∀ τ, HasDerivAt E (dE τ) τ)
    (hdiss : ∀ τ, dE τ + c * E τ ≤ 0)
    (hst : s ≤ t) :
    E t ≤ E s * Real.exp (-c * (t - s)) := by
  have hanti := weightedEnergy_antitone hE hdiss
  have hwt := hanti hst
  dsimp [weightedEnergy] at hwt
  have hscaled :=
    mul_le_mul_of_nonneg_right hwt (Real.exp_nonneg (-c * t))
  have hcancel : Real.exp (c * t) * Real.exp (-c * t) = 1 := by
    calc
      Real.exp (c * t) * Real.exp (-c * t) =
          Real.exp (c * t + (-c * t)) := by
            rw [Real.exp_add]
      _ = Real.exp 0 := by congr 1 <;> ring
      _ = 1 := Real.exp_zero
  have hratio :
      Real.exp (c * s) * Real.exp (-c * t) =
        Real.exp (-c * (t - s)) := by
    calc
      Real.exp (c * s) * Real.exp (-c * t) =
          Real.exp (c * s + (-c * t)) := by
            rw [Real.exp_add]
      _ = Real.exp (-c * (t - s)) := by congr 1 <;> ring
  calc
    E t = (Real.exp (c * t) * E t) * Real.exp (-c * t) := by
      calc
        E t = E t * 1 := by ring
        _ = E t * (Real.exp (c * t) * Real.exp (-c * t)) := by rw [hcancel]
        _ = (Real.exp (c * t) * E t) * Real.exp (-c * t) := by ring
    _ ≤ (Real.exp (c * s) * E s) * Real.exp (-c * t) := hscaled
    _ = E s * Real.exp (-c * (t - s)) := by
      calc
        (Real.exp (c * s) * E s) * Real.exp (-c * t) =
            E s * (Real.exp (c * s) * Real.exp (-c * t)) := by ring
        _ = E s * Real.exp (-c * (t - s)) := by rw [hratio]

/-- Initial-time version used most often in the manuscript. -/
theorem energy_le_exp_from_zero
    {E dE : ℝ → ℝ} {c t : ℝ}
    (hE : ∀ τ, HasDerivAt E (dE τ) τ)
    (hdiss : ∀ τ, dE τ + c * E τ ≤ 0)
    (ht : 0 ≤ t) :
    E t ≤ E 0 * Real.exp (-c * t) := by
  simpa using
    (energy_le_exp_of_differential_inequality
      (E := E) (dE := dE) (c := c) (s := 0) (t := t) hE hdiss ht)

end AMLStabilization

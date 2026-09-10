import Mathlib

namespace AMLStabilization

/-- Transformed energy used for arbitrary superquadratic damping. -/
noncomputable def powerEnergyShift (theta c : ℝ) (E : ℝ → ℝ) (t : ℝ) : ℝ :=
  E t ^ (-theta / 2) - theta * c * t

/--
For `theta > 0`, if a positive differentiable energy satisfies
`E' + 2 c E^(1+theta/2) <= 0`, then
`E^(-theta/2) - theta*c*t` is monotone.
-/
theorem powerEnergyShift_monotone
    {E dE : ℝ → ℝ} {theta c : ℝ}
    (htheta : 0 < theta)
    (hc : 0 ≤ c)
    (hE : ∀ t, HasDerivAt E (dE t) t)
    (hpos : ∀ t, 0 < E t)
    (hdiss : ∀ t, dE t + 2 * c * E t ^ (1 + theta / 2) ≤ 0) :
    Monotone (powerEnergyShift theta c E) := by
  refine monotone_of_hasDerivAt_nonneg
    (f' := fun t => dE t * (-theta / 2) * E t ^ (-theta / 2 - 1) - theta * c) ?_ ?_
  · intro t
    unfold powerEnergyShift
    have hrpow := (hE t).rpow_const (Or.inl (ne_of_gt (hpos t))) (p := -theta / 2)
    have hlin : HasDerivAt (fun x : ℝ => theta * c * x) (theta * c) t :=
      hasDerivAt_const_mul (theta * c)
    exact hrpow.sub hlin
  · intro t
    have hEt : 0 < E t := hpos t
    have hpowpos : 0 < E t ^ (-theta / 2 - 1) := Real.rpow_pos_of_pos hEt _
    have hfac : 0 < (theta / 2) * E t ^ (-theta / 2 - 1) :=
      mul_pos (by linarith) hpowpos
    have hnegd : 2 * c * E t ^ (1 + theta / 2) ≤ -dE t := by
      linarith [hdiss t]
    have hprod :
        E t ^ (1 + theta / 2) * E t ^ (-theta / 2 - 1) = 1 := by
      rw [← Real.rpow_add hEt]
      convert Real.rpow_zero (E t) using 1 <;> ring
    have hmul := mul_le_mul_of_nonneg_right hnegd (le_of_lt hfac)
    have hmain : theta * c ≤ (-dE t) * (theta / 2) * E t ^ (-theta / 2 - 1) := by
      calc
        theta * c = (2 * c * E t ^ (1 + theta / 2)) *
            ((theta / 2) * E t ^ (-theta / 2 - 1)) := by
              rw [mul_assoc, ← mul_assoc (E t ^ (1 + theta / 2)), hprod]
              ring
        _ ≤ (-dE t) * ((theta / 2) * E t ^ (-theta / 2 - 1)) := hmul
        _ = (-dE t) * (theta / 2) * E t ^ (-theta / 2 - 1) := by ring
    have : theta * c ≤ dE t * (-theta / 2) * E t ^ (-theta / 2 - 1) := by
      convert hmain using 1 <;> ring
    linarith

/-- Lower bound for the transformed energy under arbitrary-order damping. -/
theorem powerEnergy_lower_of_superquadratic_dissipation
    {E dE : ℝ → ℝ} {theta c s t : ℝ}
    (htheta : 0 < theta)
    (hc : 0 ≤ c)
    (hE : ∀ tau, HasDerivAt E (dE tau) tau)
    (hpos : ∀ tau, 0 < E tau)
    (hdiss : ∀ tau, dE tau + 2 * c * E tau ^ (1 + theta / 2) ≤ 0)
    (hst : s ≤ t) :
    E s ^ (-theta / 2) + theta * c * (t - s) ≤ E t ^ (-theta / 2) := by
  have hmono := powerEnergyShift_monotone htheta hc hE hpos hdiss
  have h := hmono hst
  dsimp [powerEnergyShift] at h
  linarith

/--
Explicit Bihari-type decay for arbitrary `theta > 0`:
`E' + 2 c E^(1+theta/2) <= 0` implies the exact polynomial upper bound.
-/
theorem energy_le_rpow_of_superquadratic_dissipation
    {E dE : ℝ → ℝ} {theta c s t : ℝ}
    (htheta : 0 < theta)
    (hc : 0 ≤ c)
    (hE : ∀ tau, HasDerivAt E (dE tau) tau)
    (hpos : ∀ tau, 0 < E tau)
    (hdiss : ∀ tau, dE tau + 2 * c * E tau ^ (1 + theta / 2) ≤ 0)
    (hst : s ≤ t) :
    E t ≤
      (E s ^ (-theta / 2) + theta * c * (t - s)) ^ (-2 / theta) := by
  have hlow := powerEnergy_lower_of_superquadratic_dissipation
    htheta hc hE hpos hdiss hst
  have hdt : 0 ≤ t - s := sub_nonneg.mpr hst
  have hEsPow : 0 < E s ^ (-theta / 2) := Real.rpow_pos_of_pos (hpos s) _
  have hterm : 0 ≤ theta * c * (t - s) :=
    mul_nonneg (mul_nonneg (le_of_lt htheta) hc) hdt
  let A : ℝ := E s ^ (-theta / 2) + theta * c * (t - s)
  have hA : 0 < A := by
    dsimp [A]
    linarith
  have hz : -2 / theta ≤ 0 := by
    have : 0 < 2 / theta := div_pos (by norm_num) htheta
    linarith
  have hrpow := Real.rpow_le_rpow_of_nonpos hA hlow hz
  have hsimp : (E t ^ (-theta / 2)) ^ (-2 / theta) = E t := by
    rw [← Real.rpow_mul (le_of_lt (hpos t))]
    have htheta0 : theta ≠ 0 := ne_of_gt htheta
    convert Real.rpow_one (E t) using 1
    field_simp [htheta0]
  rw [hsimp] at hrpow
  simpa [A] using hrpow

/-- Reformulation in terms of `q = 2 + theta`, matching the manuscript. -/
theorem energy_le_rpow_of_q_dissipation
    {E dE : ℝ → ℝ} {q c s t : ℝ}
    (hq : 2 < q)
    (hc : 0 ≤ c)
    (hE : ∀ tau, HasDerivAt E (dE tau) tau)
    (hpos : ∀ tau, 0 < E tau)
    (hdiss : ∀ tau, dE tau + 2 * c * E tau ^ (q / 2) ≤ 0)
    (hst : s ≤ t) :
    E t ≤
      (E s ^ (-(q - 2) / 2) + (q - 2) * c * (t - s)) ^ (-2 / (q - 2)) := by
  have htheta : 0 < q - 2 := by linarith
  have hdiss' : ∀ tau, dE tau + 2 * c * E tau ^ (1 + (q - 2) / 2) ≤ 0 := by
    intro tau
    convert hdiss tau using 1 <;> ring
  simpa only [sub_eq_add_neg] using
    energy_le_rpow_of_superquadratic_dissipation
      (theta := q - 2) htheta hc hE hpos hdiss' hst

end AMLStabilization

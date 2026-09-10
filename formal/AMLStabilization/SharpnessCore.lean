import Mathlib

namespace AMLStabilization

/-- Positive homogeneous profile for a degenerate damping ODE. -/
noncomputable def homogeneousSharpProfile
    (theta k w0 t : ℝ) : ℝ :=
  (w0 ^ (-theta) + theta * k * t) ^ (-1 / theta)

/-- The sharpness profile starts from the prescribed positive datum. -/
theorem homogeneousSharpProfile_zero
    {theta k w0 : ℝ}
    (htheta : 0 < theta) (hw0 : 0 < w0) :
    homogeneousSharpProfile theta k w0 0 = w0 := by
  unfold homogeneousSharpProfile
  simp only [mul_zero, add_zero]
  have htheta0 : theta ≠ 0 := ne_of_gt htheta
  rw [← Real.rpow_mul (le_of_lt hw0)]
  have hexp : (-theta) * (-1 / theta) = 1 := by
    field_simp [htheta0]
  rw [hexp, Real.rpow_one]

/-- Power identity converting the closed profile into the nonlinear damping term. -/
theorem homogeneousSharpProfile_power
    {theta k w0 t : ℝ}
    (htheta : 0 < theta) (hw0 : 0 < w0)
    (hk : 0 ≤ k) (ht : 0 ≤ t) :
    (homogeneousSharpProfile theta k w0 t) ^ (theta + 1) =
      (w0 ^ (-theta) + theta * k * t) ^ (-1 / theta - 1) := by
  have hbase0 : 0 < w0 ^ (-theta) := Real.rpow_pos_of_pos hw0 _
  have hterm0 : 0 ≤ theta * k * t :=
    mul_nonneg (mul_nonneg (le_of_lt htheta) hk) ht
  have hden : 0 < w0 ^ (-theta) + theta * k * t := by linarith
  unfold homogeneousSharpProfile
  rw [← Real.rpow_mul (le_of_lt hden)]
  have htheta0 : theta ≠ 0 := ne_of_gt htheta
  congr 1
  field_simp [htheta0]
  ring

/--
The explicit homogeneous profile solves `w' = -k w^(theta+1)` on `t >= 0`.
This is the scalar ODE behind sharpness of the manuscript's signal decay rate.
-/
theorem homogeneousSharpProfile_hasDerivAt
    {theta k w0 t : ℝ}
    (htheta : 0 < theta) (hw0 : 0 < w0)
    (hk : 0 ≤ k) (ht : 0 ≤ t) :
    HasDerivAt (homogeneousSharpProfile theta k w0)
      (-k * (homogeneousSharpProfile theta k w0 t) ^ (theta + 1)) t := by
  have hbase0 : 0 < w0 ^ (-theta) := Real.rpow_pos_of_pos hw0 _
  have hterm0 : 0 ≤ theta * k * t :=
    mul_nonneg (mul_nonneg (le_of_lt htheta) hk) ht
  have hden : 0 < w0 ^ (-theta) + theta * k * t := by linarith
  have hmul : HasDerivAt (fun x : ℝ => theta * k * x) (theta * k) t :=
    hasDerivAt_const_mul (theta * k)
  have hinner :
      HasDerivAt (fun x : ℝ => w0 ^ (-theta) + theta * k * x) (theta * k) t := by
    simpa using (hasDerivAt_const t (w0 ^ (-theta))).add hmul
  have hrpow := hinner.rpow_const
    (Or.inl (ne_of_gt hden)) (p := -1 / theta)
  have htheta0 : theta ≠ 0 := ne_of_gt htheta
  have hcoef : theta * k * (-1 / theta) = -k := by
    field_simp [htheta0]
    ring
  have hpow := homogeneousSharpProfile_power htheta hw0 hk ht
  change HasDerivAt
    (fun y : ℝ => (w0 ^ (-theta) + theta * k * y) ^ (-1 / theta))
    (-k * ((w0 ^ (-theta) + theta * k * t) ^ (-1 / theta)) ^ (theta + 1)) t
  rw [hpow]
  simpa [hcoef] using hrpow

/-- Exact ODE statement in derivative notation on the nonnegative time axis. -/
theorem homogeneousSharpProfile_deriv
    {theta k w0 t : ℝ}
    (htheta : 0 < theta) (hw0 : 0 < w0)
    (hk : 0 ≤ k) (ht : 0 ≤ t) :
    deriv (homogeneousSharpProfile theta k w0) t =
      -k * (homogeneousSharpProfile theta k w0 t) ^ (theta + 1) := by
  exact (homogeneousSharpProfile_hasDerivAt htheta hw0 hk ht).deriv

end AMLStabilization

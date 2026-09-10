import Mathlib
import AMLStabilization.SharpnessCore

open SignType

namespace AMLStabilization

/-- Signed homogeneous profile for arbitrary nonzero initial deviation. -/
noncomputable def signedHomogeneousSharpProfile
    (theta k w0 t : ℝ) : ℝ :=
  (sign w0 : ℝ) * homogeneousSharpProfile theta k |w0| t

/-- The positive profile stays strictly positive for nonnegative time and
nonnegative damping coefficient. -/
theorem homogeneousSharpProfile_pos
    {theta k w0 t : ℝ}
    (htheta : 0 < theta) (hw0 : 0 < w0)
    (hk : 0 ≤ k) (ht : 0 ≤ t) :
    0 < homogeneousSharpProfile theta k w0 t := by
  unfold homogeneousSharpProfile
  have hbase : 0 < w0 ^ (-theta) := Real.rpow_pos_of_pos hw0 _
  have hterm : 0 ≤ theta * k * t := by positivity
  exact Real.rpow_pos_of_pos (by linarith) _

/-- The signed profile recovers an arbitrary nonzero initial datum. -/
theorem signedHomogeneousSharpProfile_zero
    {theta k w0 : ℝ}
    (htheta : 0 < theta) (hw0 : w0 ≠ 0) :
    signedHomogeneousSharpProfile theta k w0 0 = w0 := by
  unfold signedHomogeneousSharpProfile
  rw [homogeneousSharpProfile_zero htheta (abs_pos.mpr hw0)]
  exact sign_mul_abs w0

/-- Exact absolute-value formula appearing in the sharpness proposition. -/
theorem abs_signedHomogeneousSharpProfile
    {theta k w0 t : ℝ}
    (htheta : 0 < theta) (hw0 : w0 ≠ 0)
    (hk : 0 ≤ k) (ht : 0 ≤ t) :
    |signedHomogeneousSharpProfile theta k w0 t| =
      (|w0| ^ (-theta) + theta * k * t) ^ (-1 / theta) := by
  have hprof : 0 < homogeneousSharpProfile theta k |w0| t :=
    homogeneousSharpProfile_pos htheta (abs_pos.mpr hw0) hk ht
  have hsignAbs : |(sign w0 : ℝ)| = 1 := by
    rcases lt_or_gt_of_ne hw0 with hwneg | hwpos
    · simp [hwneg]
    · simp [hwpos]
  calc
    |signedHomogeneousSharpProfile theta k w0 t| =
        |(sign w0 : ℝ)| * |homogeneousSharpProfile theta k |w0| t| := by
      rw [signedHomogeneousSharpProfile, abs_mul]
    _ = homogeneousSharpProfile theta k |w0| t := by
      rw [hsignAbs, abs_of_pos hprof, one_mul]
    _ = (|w0| ^ (-theta) + theta * k * t) ^ (-1 / theta) := rfl

/-- Manuscript form with the damping coefficient split as `kappa * ubar`. -/
theorem sharpness_absolute_formula
    {theta kappa ubar w0 t : ℝ}
    (htheta : 0 < theta) (hw0 : w0 ≠ 0)
    (hkappa : 0 ≤ kappa) (hubar : 0 ≤ ubar) (ht : 0 ≤ t) :
    |signedHomogeneousSharpProfile theta (kappa * ubar) w0 t| =
      (|w0| ^ (-theta) + theta * kappa * ubar * t) ^ (-1 / theta) := by
  have h := abs_signedHomogeneousSharpProfile
    (theta := theta) (k := kappa * ubar) (w0 := w0) (t := t)
    htheta hw0 (mul_nonneg hkappa hubar) ht
  simpa [mul_assoc] using h

end AMLStabilization

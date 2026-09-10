import Mathlib
import AMLStabilization.BoxPoincareCore

namespace AMLStabilization

/--
Finite-coordinate tensorization algebra for a rectangular box.  If the total
variance is dominated by a sum of coordinate-fiber variances, each fiber obeys
a one-dimensional Poincare estimate, and every side length is bounded by `C`,
then the full variance is bounded by `C^2` times the total coordinate energy.
-/
theorem boxPoincareTensorization_algebra
    {ι : Type*} [Fintype ι]
    {V C : ℝ} {fiberVar side energy : ι → ℝ}
    (hC : 0 ≤ C)
    (henergy : ∀ i, 0 ≤ energy i)
    (hV : V ≤ ∑ i, fiberVar i)
    (hfiber : ∀ i, fiberVar i ≤ (side i) ^ 2 * energy i)
    (hside : ∀ i, |side i| ≤ C) :
    V ≤ C ^ 2 * ∑ i, energy i := by
  calc
    V ≤ ∑ i, fiberVar i := hV
    _ ≤ ∑ i, (side i) ^ 2 * energy i := by
      exact Finset.sum_le_sum fun i _ => hfiber i
    _ ≤ ∑ i, C ^ 2 * energy i := by
      exact Finset.sum_le_sum fun i _ => by
        have hs0 : 0 ≤ |side i| := abs_nonneg _
        have hsq : (side i) ^ 2 ≤ C ^ 2 := by
          rw [← sq_abs]
          exact (sq_le_sq₀ hs0 hC).2 (hside i)
        exact mul_le_mul_of_nonneg_right hsq (henergy i)
    _ = C ^ 2 * ∑ i, energy i := by
      rw [Finset.mul_sum]

/-- Square-root form of the tensorized box estimate. -/
theorem boxPoincareTensorization_sqrt
    {ι : Type*} [Fintype ι]
    {V C : ℝ} {fiberVar side energy : ι → ℝ}
    (hV0 : 0 ≤ V) (hC : 0 ≤ C)
    (henergy : ∀ i, 0 ≤ energy i)
    (hV : V ≤ ∑ i, fiberVar i)
    (hfiber : ∀ i, fiberVar i ≤ (side i) ^ 2 * energy i)
    (hside : ∀ i, |side i| ≤ C) :
    Real.sqrt V ≤ C * Real.sqrt (∑ i, energy i) := by
  have hmain := boxPoincareTensorization_algebra hC henergy hV hfiber hside
  have hsum0 : 0 ≤ ∑ i, energy i := Finset.sum_nonneg fun i _ => henergy i
  have hsqrt := Real.sqrt_le_sqrt hmain
  rw [Real.sqrt_mul (sq_nonneg C), Real.sqrt_sq_eq_abs, abs_of_nonneg hC] at hsqrt
  exact hsqrt

/--
Interface-form tensorization theorem matching the manuscript notation.  The
only geometric/Fubini datum is the variance decomposition `V <= sum V_i`;
all coordinate Poincare and side-length bookkeeping is discharged internally.
-/
theorem boxPoincare_from_coordinate_variances
    {ι : Type*} [Fintype ι]
    {V Cp gradSq : ℝ} {fiberVar side energy : ι → ℝ}
    (hV0 : 0 ≤ V) (hCp : 0 ≤ Cp)
    (henergy : ∀ i, 0 ≤ energy i)
    (hVarianceDecomp : V ≤ ∑ i, fiberVar i)
    (hFiberPoincare : ∀ i, fiberVar i ≤ (side i) ^ 2 * energy i)
    (hSideBound : ∀ i, |side i| ≤ Cp)
    (hGradEnergy : ∑ i, energy i ≤ gradSq)
    (hGradSq : 0 ≤ gradSq) :
    Real.sqrt V ≤ Cp * Real.sqrt gradSq := by
  have hbox := boxPoincareTensorization_sqrt hV0 hCp henergy
    hVarianceDecomp hFiberPoincare hSideBound
  have hsum0 : 0 ≤ ∑ i, energy i := Finset.sum_nonneg fun i _ => henergy i
  have hsqrtGrad := Real.sqrt_le_sqrt hGradEnergy
  have hmul := mul_le_mul_of_nonneg_left hsqrtGrad hCp
  exact hbox.trans hmul

end AMLStabilization

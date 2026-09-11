import Mathlib
import AMLStabilization.FiniteGradientCauchyCore
import AMLStabilization.MotilityChainRuleCore

open MeasureTheory

namespace AMLStabilization

/-- The finite-coordinate Euclidean length is nonnegative. -/
theorem finiteCoordinateL2Norm_nonneg
    {ι : Type*} [Fintype ι] (f : ι → ℝ) :
    0 ≤ finiteCoordinateL2Norm f := by
  unfold finiteCoordinateL2Norm
  exact Real.sqrt_nonneg _

/-- A scalar pointwise bound propagates to the finite-coordinate Euclidean length. -/
theorem finiteCoordinateL2Norm_scalar_mul_le
    {ι : Type*} [Fintype ι]
    (f : ι → ℝ) {r C : ℝ}
    (hC : 0 ≤ C) (hr : |r| ≤ C) :
    finiteCoordinateL2Norm (fun i => r * f i) ≤
      C * finiteCoordinateL2Norm f := by
  have hrSq : r ^ 2 ≤ C ^ 2 := by
    rw [sq_le_sq]
    simpa [abs_of_nonneg hC] using hr
  have hsumNonneg : 0 ≤ ∑ i, (f i) ^ 2 :=
    Finset.sum_nonneg fun i hi => sq_nonneg (f i)
  have hsq :
      (finiteCoordinateL2Norm (fun i => r * f i)) ^ 2 ≤
        (C * finiteCoordinateL2Norm f) ^ 2 := by
    calc
      (finiteCoordinateL2Norm (fun i => r * f i)) ^ 2 =
          ∑ i, (r * f i) ^ 2 := finiteCoordinateL2Norm_sq _
      _ = r ^ 2 * ∑ i, (f i) ^ 2 := by
        simp only [mul_pow]
        rw [Finset.mul_sum]
      _ ≤ C ^ 2 * ∑ i, (f i) ^ 2 := by
        gcongr
      _ = C ^ 2 * (finiteCoordinateL2Norm f) ^ 2 := by
        rw [finiteCoordinateL2Norm_sq]
      _ = (C * finiteCoordinateL2Norm f) ^ 2 := by ring
  exact (sq_le_sq₀
    (finiteCoordinateL2Norm_nonneg _)
    (mul_nonneg hC (finiteCoordinateL2Norm_nonneg _))).mp hsq

/--
Pointwise motility-drift estimate.  If `|u| ≤ U` and `|phi'| ≤ L`, then
`|u phi' gradV|_{ell²} ≤ U L |gradV|_{ell²}`.
-/
theorem motilityDrift_finiteCoordinateL2Norm_le
    {ι : Type*} [Fintype ι]
    (gradV : ι → ℝ) {u phiPrime U L : ℝ}
    (hU0 : 0 ≤ U) (hL0 : 0 ≤ L)
    (hU : |u| ≤ U) (hPhi : |phiPrime| ≤ L) :
    finiteCoordinateL2Norm (fun i => u * (phiPrime * gradV i)) ≤
      (U * L) * finiteCoordinateL2Norm gradV := by
  have hC : 0 ≤ U * L := mul_nonneg hU0 hL0
  have hscalar : |u * phiPrime| ≤ U * L := by
    rw [abs_mul]
    exact mul_le_mul hU hPhi (abs_nonneg phiPrime) hU0
  simpa [mul_assoc] using
    finiteCoordinateL2Norm_scalar_mul_le gradV hC hscalar

/--
`L²` forcing package for the cell-energy drift term.

From the pointwise bounds `|u| ≤ U`, `|phi'| ≤ L` and the `L²` control of
`gradV`, this theorem derives both the `L²` membership of
`u phi' gradV` and the manuscript estimate

`||u phi' gradV||₂ ≤ U L ||gradV||₂`.
-/
theorem motilityDrift_memLp_and_L2_bound
    {Ω ι : Type*} [MeasurableSpace Ω] [Fintype ι]
    {μ : Measure Ω}
    (u phiPrime : Ω → ℝ) (gradV : Ω → ι → ℝ)
    {U L : ℝ}
    (hU0 : 0 ≤ U) (hL0 : 0 ≤ L)
    (hU : ∀ᵐ x ∂μ, |u x| ≤ U)
    (hPhi : ∀ᵐ x ∂μ, |phiPrime x| ≤ L)
    (hGradLp : MemLp (fun x => finiteCoordinateL2Norm (gradV x)) 2 μ)
    (hDriftMeas : AEStronglyMeasurable
      (fun x => finiteCoordinateL2Norm
        (fun i => u x * (phiPrime x * gradV x i))) μ) :
    MemLp
        (fun x => finiteCoordinateL2Norm
          (fun i => u x * (phiPrime x * gradV x i))) 2 μ ∧
      Real.sqrt (∫ x, ∑ i, (u x * (phiPrime x * gradV x i)) ^ 2 ∂μ) ≤
        (U * L) * Real.sqrt (∫ x, ∑ i, (gradV x i) ^ 2 ∂μ) := by
  have hC : 0 ≤ U * L := mul_nonneg hU0 hL0
  have hpoint : ∀ᵐ x ∂μ,
      finiteCoordinateL2Norm
          (fun i => u x * (phiPrime x * gradV x i)) ≤
        (U * L) * finiteCoordinateL2Norm (gradV x) := by
    filter_upwards [hU, hPhi] with x hxU hxPhi
    exact motilityDrift_finiteCoordinateL2Norm_le
      (gradV x) hU0 hL0 hxU hxPhi
  have hDriftLp : MemLp
      (fun x => finiteCoordinateL2Norm
        (fun i => u x * (phiPrime x * gradV x i))) 2 μ := by
    refine MemLp.of_le_mul hGradLp hDriftMeas ?_
    filter_upwards [hpoint] with x hx
    have hd0 := finiteCoordinateL2Norm_nonneg
      (fun i => u x * (phiPrime x * gradV x i))
    have hg0 := finiteCoordinateL2Norm_nonneg (gradV x)
    simpa [Real.norm_eq_abs, abs_of_nonneg hd0, abs_of_nonneg hg0] using hx
  have hDriftSqInt := hDriftLp.integrable_sq
  have hGradSqInt := hGradLp.integrable_sq
  have hRightInt : Integrable
      (fun x => (U * L) ^ 2 * (finiteCoordinateL2Norm (gradV x)) ^ 2) μ :=
    Integrable.const_mul hGradSqInt ((U * L) ^ 2)
  have hSqPoint : ∀ᵐ x ∂μ,
      (finiteCoordinateL2Norm
          (fun i => u x * (phiPrime x * gradV x i))) ^ 2 ≤
        (U * L) ^ 2 * (finiteCoordinateL2Norm (gradV x)) ^ 2 := by
    filter_upwards [hpoint] with x hx
    have hd0 := finiteCoordinateL2Norm_nonneg
      (fun i => u x * (phiPrime x * gradV x i))
    have hg0 := finiteCoordinateL2Norm_nonneg (gradV x)
    have hs := (sq_le_sq₀ hd0 (mul_nonneg hC hg0)).2 hx
    simpa [mul_pow] using hs
  have hIntNorm :
      (∫ x,
        (finiteCoordinateL2Norm
          (fun i => u x * (phiPrime x * gradV x i))) ^ 2 ∂μ) ≤
        (U * L) ^ 2 *
          (∫ x, (finiteCoordinateL2Norm (gradV x)) ^ 2 ∂μ) := by
    calc
      (∫ x,
        (finiteCoordinateL2Norm
          (fun i => u x * (phiPrime x * gradV x i))) ^ 2 ∂μ) ≤
          ∫ x, (U * L) ^ 2 *
            (finiteCoordinateL2Norm (gradV x)) ^ 2 ∂μ :=
        integral_mono_ae hDriftSqInt hRightInt hSqPoint
      _ = (U * L) ^ 2 *
          (∫ x, (finiteCoordinateL2Norm (gradV x)) ^ 2 ∂μ) := by
        rw [integral_const_mul]
  have hDriftRewrite :
      (∫ x,
        (finiteCoordinateL2Norm
          (fun i => u x * (phiPrime x * gradV x i))) ^ 2 ∂μ) =
        ∫ x, ∑ i, (u x * (phiPrime x * gradV x i)) ^ 2 ∂μ := by
    apply integral_congr_ae
    filter_upwards with x
    exact finiteCoordinateL2Norm_sq _
  have hGradRewrite :
      (∫ x, (finiteCoordinateL2Norm (gradV x)) ^ 2 ∂μ) =
        ∫ x, ∑ i, (gradV x i) ^ 2 ∂μ := by
    apply integral_congr_ae
    filter_upwards with x
    exact finiteCoordinateL2Norm_sq _
  rw [hDriftRewrite, hGradRewrite] at hIntNorm
  have hsqrt := Real.sqrt_le_sqrt hIntNorm
  have hbound :
      Real.sqrt (∫ x, ∑ i, (u x * (phiPrime x * gradV x i)) ^ 2 ∂μ) ≤
        (U * L) * Real.sqrt (∫ x, ∑ i, (gradV x i) ^ 2 ∂μ) := by
    calc
      Real.sqrt (∫ x, ∑ i, (u x * (phiPrime x * gradV x i)) ^ 2 ∂μ) ≤
          Real.sqrt ((U * L) ^ 2 *
            (∫ x, ∑ i, (gradV x i) ^ 2 ∂μ)) := hsqrt
      _ = (U * L) * Real.sqrt (∫ x, ∑ i, (gradV x i) ^ 2 ∂μ) := by
        rw [Real.sqrt_mul (sq_nonneg (U * L)), Real.sqrt_sq hC]
  exact ⟨hDriftLp, hbound⟩

end AMLStabilization

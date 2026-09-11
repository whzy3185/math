import Mathlib
import AMLStabilization.HolderCore

open MeasureTheory

namespace AMLStabilization

/-- Euclidean length of a finite real coordinate family. -/
noncomputable def finiteCoordinateL2Norm
    {ι : Type*} [Fintype ι] (f : ι → ℝ) : ℝ :=
  Real.sqrt (∑ i, (f i) ^ 2)

/-- Finite-dimensional Cauchy-Schwarz in absolute-value form. -/
theorem abs_sum_mul_le_finiteCoordinateL2Norm_mul
    {ι : Type*} [Fintype ι]
    (f g : ι → ℝ) :
    |∑ i, f i * g i| ≤ finiteCoordinateL2Norm f * finiteCoordinateL2Norm g := by
  have hupper := Real.sum_mul_le_sqrt_mul_sqrt Finset.univ f g
  have hlower := Real.sum_mul_le_sqrt_mul_sqrt Finset.univ (fun i => -f i) g
  have hlower' :
      -(∑ i, f i * g i) ≤ finiteCoordinateL2Norm f * finiteCoordinateL2Norm g := by
    simpa [finiteCoordinateL2Norm] using hlower
  have hupper' :
      (∑ i, f i * g i) ≤ finiteCoordinateL2Norm f * finiteCoordinateL2Norm g := by
    simpa [finiteCoordinateL2Norm] using hupper
  exact abs_le.mpr ⟨hlower', hupper'⟩

/-- The square of the finite-coordinate `L²` length is the sum of coordinate squares. -/
theorem finiteCoordinateL2Norm_sq
    {ι : Type*} [Fintype ι]
    (f : ι → ℝ) :
    (finiteCoordinateL2Norm f) ^ 2 = ∑ i, (f i) ^ 2 := by
  unfold finiteCoordinateL2Norm
  rw [Real.sq_sqrt]
  exact Finset.sum_nonneg fun i hi => sq_nonneg (f i)

/--
Integrated finite-dimensional Cauchy-Schwarz.  The only regularity input beyond
`L²` membership of the pointwise Euclidean lengths is integrability of the dot
product itself; the Cauchy-Schwarz bound is derived internally.
-/
theorem integral_finiteCoordinate_dot_cauchySchwarz
    {Ω ι : Type*} [MeasurableSpace Ω] [Fintype ι]
    {μ : Measure Ω}
    (f g : Ω → ι → ℝ)
    (hDotInt : Integrable (fun x => ∑ i, f x i * g x i) μ)
    (hf : MemLp (fun x => finiteCoordinateL2Norm (f x)) 2 μ)
    (hg : MemLp (fun x => finiteCoordinateL2Norm (g x)) 2 μ) :
    |∫ x, ∑ i, f x i * g x i ∂μ| ≤
      Real.sqrt (∫ x, ∑ i, (f x i) ^ 2 ∂μ) *
        Real.sqrt (∫ x, ∑ i, (g x i) ^ 2 ∂μ) := by
  have hNormProdInt : Integrable
      (fun x => finiteCoordinateL2Norm (f x) * finiteCoordinateL2Norm (g x)) μ := by
    simpa only [Pi.mul_apply] using hf.integrable_mul hg
  have hPoint : ∀ x,
      |∑ i, f x i * g x i| ≤
        finiteCoordinateL2Norm (f x) * finiteCoordinateL2Norm (g x) :=
    fun x => abs_sum_mul_le_finiteCoordinateL2Norm_mul (f x) (g x)
  have hScalarCS := integral_mul_cauchySchwarz
    (μ := μ)
    (f := fun x => finiteCoordinateL2Norm (f x))
    (g := fun x => finiteCoordinateL2Norm (g x)) hf hg
  have hfSq :
      (∫ x, (finiteCoordinateL2Norm (f x)) ^ 2 ∂μ) =
        ∫ x, ∑ i, (f x i) ^ 2 ∂μ := by
    apply integral_congr_ae
    filter_upwards with x
    exact finiteCoordinateL2Norm_sq (f x)
  have hgSq :
      (∫ x, (finiteCoordinateL2Norm (g x)) ^ 2 ∂μ) =
        ∫ x, ∑ i, (g x i) ^ 2 ∂μ := by
    apply integral_congr_ae
    filter_upwards with x
    exact finiteCoordinateL2Norm_sq (g x)
  calc
    |∫ x, ∑ i, f x i * g x i ∂μ| =
        ‖∫ x, ∑ i, f x i * g x i ∂μ‖ := by
      simp [Real.norm_eq_abs]
    _ ≤ ∫ x, ‖∑ i, f x i * g x i‖ ∂μ :=
      norm_integral_le_integral_norm _
    _ = ∫ x, |∑ i, f x i * g x i| ∂μ := by
      apply integral_congr_ae
      filter_upwards with x
      simp [Real.norm_eq_abs]
    _ ≤ ∫ x,
        finiteCoordinateL2Norm (f x) * finiteCoordinateL2Norm (g x) ∂μ := by
      apply integral_mono_ae hDotInt.abs hNormProdInt
      exact Filter.Eventually.of_forall hPoint
    _ ≤ Real.sqrt (∫ x, (finiteCoordinateL2Norm (f x)) ^ 2 ∂μ) *
        Real.sqrt (∫ x, (finiteCoordinateL2Norm (g x)) ^ 2 ∂μ) := hScalarCS
    _ = Real.sqrt (∫ x, ∑ i, (f x i) ^ 2 ∂μ) *
        Real.sqrt (∫ x, ∑ i, (g x i) ^ 2 ∂μ) := by
      rw [hfSq, hgSq]

end AMLStabilization

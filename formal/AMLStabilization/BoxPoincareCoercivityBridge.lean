import Mathlib
import AMLStabilization.BoxPoincareTensorCore
import AMLStabilization.PoincareMeanCore

open MeasureTheory

namespace AMLStabilization

/--
Bridge from finite-coordinate box Poincare tensorization to the mean-square
estimate used by the mass-weighted coercivity chain.  Once the coordinate
variance decomposition/Fubini datum and one-dimensional fiber estimates are
available, the Poincare constant is consumed internally.
-/
theorem meanSquareBase_of_boxPoincareTensorization
    {ι Ω : Type*} [Fintype ι] [MeasurableSpace Ω]
    {μ : Measure Ω} {f : Ω → ℝ}
    {fbar V Cp gradSq : ℝ}
    {fiberVar side energy : ι → ℝ}
    (hCp : 0 ≤ Cp)
    (hV : 0 ≤ V)
    (hGradSq : 0 ≤ gradSq)
    (henergy : ∀ i, 0 ≤ energy i)
    (hVarianceDecomp :
      (∫ x, (f x - fbar) ^ 2 ∂μ) ≤ ∑ i, fiberVar i)
    (hFiberPoincare : ∀ i,
      fiberVar i ≤ (side i) ^ 2 * energy i)
    (hSideBound : ∀ i, |side i| ≤ Cp)
    (hGradEnergy : ∑ i, energy i ≤ gradSq)
    (hdecomp :
      (∫ x, f x ^ 2 ∂μ) =
        (∫ x, (f x - fbar) ^ 2 ∂μ) + V * fbar ^ 2) :
    (∫ x, f x ^ 2 ∂μ) ≤
      2 * Cp ^ 2 * gradSq + 2 * V * fbar ^ 2 := by
  have hdev0 : 0 ≤ (∫ x, (f x - fbar) ^ 2 ∂μ) :=
    integral_nonneg fun x => sq_nonneg (f x - fbar)
  have hPoincare := boxPoincare_from_coordinate_variances
    (V := ∫ x, (f x - fbar) ^ 2 ∂μ)
    (Cp := Cp) (gradSq := gradSq)
    (fiberVar := fiberVar) (side := side) (energy := energy)
    hdev0 hCp henergy hVarianceDecomp hFiberPoincare hSideBound
    hGradEnergy hGradSq
  have hbase := meanSquareBase_of_Poincare
    (μ := μ) (f := f) (fbar := fbar) (V := V)
    (Cp := Cp) (grad := Real.sqrt gradSq)
    hCp (Real.sqrt_nonneg _) hV hdev0 hPoincare hdecomp
  rw [Real.sq_sqrt hGradSq] at hbase
  exact hbase

end AMLStabilization

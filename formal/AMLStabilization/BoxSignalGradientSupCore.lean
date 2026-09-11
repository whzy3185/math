import Mathlib
import AMLStabilization.BoxMotilityCellScalarInterfaceCore
import AMLStabilization.BoxProductMeasureCore

open Set Finset MeasureTheory Real

namespace AMLStabilization

/-- Explicit finite-volume constant converting a coordinatewise gradient
`L^infinity` envelope into the finite-coordinate spatial `L^2` gradient norm
on a rectangular box. -/
noncomputable def boxSignalGradientSupToL2Constant
    {n : ℕ} (a b : Fin (n + 1) → ℝ) : ℝ :=
  Real.sqrt ((n + 1 : ℝ) * ∏ j : Fin (n + 1), (b j - a j))

/--
A coordinatewise uniform gradient bound on a nondegenerate rectangular box
implies an explicit `L^2` gradient bound.

This removes the abstract strong-norm-to-`L^2`-gradient comparison constant from
the final box stabilization assembly whenever the strong norm directly controls
each coordinate derivative.
-/
theorem boxSignalGradientNorm_le_of_component_bound
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    (hside : ∀ j, a j < b j)
    (gradV : ℝ → (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    {t M : ℝ}
    (hM0 : 0 ≤ M)
    (hgradCont : ∀ i, ContinuousOn (fun x => gradV t x i) (Icc a b))
    (hbound : ∀ x ∈ Icc a b, ∀ i, |gradV t x i| ≤ M) :
    boxSignalGradientNorm a b gradV t ≤
      boxSignalGradientSupToL2Constant a b * M := by
  let G : ℝ := ∫ x in Icc a b,
    ∑ i : Fin (n + 1), (gradV t x i) ^ 2
  let V : ℝ := ∏ j : Fin (n + 1), (b j - a j)
  have hGradSqCont : ContinuousOn
      (fun x => ∑ i : Fin (n + 1), (gradV t x i) ^ 2) (Icc a b) := by
    apply continuousOn_finsetSum
    intro i hi
    exact (hgradCont i).pow 2
  have hGradSqInt : IntegrableOn
      (fun x => ∑ i : Fin (n + 1), (gradV t x i) ^ 2) (Icc a b) :=
    ContinuousOn.integrableOn_compact isCompact_Icc hGradSqCont
  have hConstInt : IntegrableOn
      (fun _ : Fin (n + 1) → ℝ => (n + 1 : ℝ) * M ^ 2) (Icc a b) :=
    integrableOn_const
  have hPoint : ∀ x ∈ Icc a b,
      (∑ i : Fin (n + 1), (gradV t x i) ^ 2) ≤
        (n + 1 : ℝ) * M ^ 2 := by
    intro x hx
    calc
      (∑ i : Fin (n + 1), (gradV t x i) ^ 2) ≤
          ∑ _i : Fin (n + 1), M ^ 2 := by
        apply Finset.sum_le_sum
        intro i hi
        rw [sq_le_sq]
        simpa [abs_of_nonneg hM0] using hbound x hx i
      _ = (n + 1 : ℝ) * M ^ 2 := by simp
  have hIntegralLe : G ≤
      ∫ _x in Icc a b, (n + 1 : ℝ) * M ^ 2 := by
    dsimp [G]
    exact setIntegral_mono_on hGradSqInt hConstInt measurableSet_Icc hPoint
  have hConstEval :
      (∫ _x in Icc a b, (n + 1 : ℝ) * M ^ 2) =
        V * ((n + 1 : ℝ) * M ^ 2) := by
    dsimp [V]
    rw [MeasureTheory.integral_const]
    simp only [MeasurableSet.univ, measureReal_restrict_apply, Set.univ_inter,
      smul_eq_mul]
    rw [boxVolumeReal_eq_prod_side (fun j => (hside j).le)]
  have hIntegralLe' : G ≤ V * ((n + 1 : ℝ) * M ^ 2) := by
    calc
      G ≤ ∫ _x in Icc a b, (n + 1 : ℝ) * M ^ 2 := hIntegralLe
      _ = V * ((n + 1 : ℝ) * M ^ 2) := hConstEval
  calc
    boxSignalGradientNorm a b gradV t = Real.sqrt G := by
      rfl
    _ ≤ Real.sqrt (V * ((n + 1 : ℝ) * M ^ 2)) :=
      Real.sqrt_le_sqrt.mpr hIntegralLe'
    _ = Real.sqrt (((n + 1 : ℝ) * V) * M ^ 2) := by
      congr 1
      ring
    _ = Real.sqrt ((n + 1 : ℝ) * V) * Real.sqrt (M ^ 2) := by
      rw [Real.sqrt_mul' _ (sq_nonneg M)]
    _ = Real.sqrt ((n + 1 : ℝ) * V) * M := by
      rw [Real.sqrt_sq_eq_abs, abs_of_nonneg hM0]
    _ = boxSignalGradientSupToL2Constant a b * M := by
      rfl

end AMLStabilization

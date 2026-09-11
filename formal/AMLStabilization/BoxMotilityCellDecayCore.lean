import Mathlib
import AMLStabilization.BoxMotilityCellScalarInterfaceCore
import AMLStabilization.CellEnergyInterfaceAssemblyCore

open Set

namespace AMLStabilization

/-- The effective rectangular-box Poincare constant is strictly positive once
all side lengths are positive and bounded above by `C`. -/
theorem boxPoincareConstant_pos
    {n : ℕ} {a b : Fin (n + 1) → ℝ} {C : ℝ}
    (hside : ∀ j, a j < b j)
    (hSideBound : ∀ j, b j - a j ≤ C) :
    0 < boxPoincareConstant n C := by
  let i0 : Fin (n + 1) := ⟨0, by omega⟩
  have hCpos : 0 < C :=
    (sub_pos.mpr (hside i0)).trans_le (hSideBound i0)
  unfold boxPoincareConstant
  exact mul_pos (Real.sqrt_pos.2 (by positivity)) hCpos

/--
Exponential box cell-energy decay for signal-dependent motility once the
pointwise PDE interfaces have been generated and the signal gradient has an
exponential `L²` rate.
-/
theorem boxMotilityCell_exponentialDecay_from_signalGradientRate
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    (hside : ∀ j, a j < b j)
    {C U L CV a0 lambda T s t ubar : ℝ}
    (hSideBound : ∀ j, b j - a j ≤ C)
    (hU0 : 0 ≤ U) (hL0 : 0 ≤ L) (hCV0 : 0 ≤ CV)
    (ha0 : 0 < a0) (hlambda : 0 < lambda)
    (u ut : ℝ → (Fin (n + 1) → ℝ) → ℝ)
    (gradU gradV : ℝ → (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (hrate : 2 * lambda < a0 / (boxPoincareConstant n C) ^ 2)
    (hinterfaces : ∀ τ,
      CellEnergyPointwiseInterfaces
        (boxCellEnergy a b u ubar)
        (boxCellEnergyDerivative a b u ut ubar)
        (boxCellGradientNorm a b gradU)
        (boxMotilityForcingNorm a b U L gradV)
        a0 (boxPoincareConstant n C) τ)
    (hVrate : ∀ τ,
      boxSignalGradientNorm a b gradV τ ≤
        CV * Real.exp (-lambda * (τ - T)))
    (hst : s ≤ t) :
    boxCellEnergy a b u ubar t ≤
      (boxCellEnergy a b u ubar s -
          exponentialBarrier
            (a0 / (boxPoincareConstant n C) ^ 2) (2 * lambda)
            ((U * L * CV) ^ 2 / a0) *
          Real.exp (-(2 * lambda) * (s - T))) *
        Real.exp (-(a0 / (boxPoincareConstant n C) ^ 2) * (t - s)) +
      exponentialBarrier
        (a0 / (boxPoincareConstant n C) ^ 2) (2 * lambda)
        ((U * L * CV) ^ 2 / a0) *
        Real.exp (-(2 * lambda) * (t - T)) := by
  have hCp : 0 < boxPoincareConstant n C :=
    boxPoincareConstant_pos hside hSideBound
  have hUL0 : 0 ≤ U * L := mul_nonneg hU0 hL0
  have hCH0 : 0 ≤ U * L * CV := mul_nonneg hUL0 hCV0
  have hHrate : ∀ τ,
      boxMotilityForcingNorm a b U L gradV τ ≤
        (U * L * CV) * Real.exp (-lambda * (τ - T)) := by
    intro τ
    unfold boxMotilityForcingNorm
    calc
      (U * L) * boxSignalGradientNorm a b gradV τ ≤
          (U * L) * (CV * Real.exp (-lambda * (τ - T))) :=
        mul_le_mul_of_nonneg_left (hVrate τ) hUL0
      _ = (U * L * CV) * Real.exp (-lambda * (τ - T)) := by ring
  exact cellEnergy_exponentialDecay_from_pointwiseInterfaces
    ha0 hCp hCH0 hlambda hrate hinterfaces hHrate hst

/--
Polynomial counterpart of
`boxMotilityCell_exponentialDecay_from_signalGradientRate`.
-/
theorem boxMotilityCell_polynomialDecay_from_signalGradientRate
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    (hside : ∀ j, a j < b j)
    {C U L CV a0 beta T t ubar : ℝ}
    (hSideBound : ∀ j, b j - a j ≤ C)
    (hU0 : 0 ≤ U) (hL0 : 0 ≤ L) (hCV0 : 0 ≤ CV)
    (ha0 : 0 < a0) (hbeta : 0 < beta)
    (u ut : ℝ → (Fin (n + 1) → ℝ) → ℝ)
    (gradU gradV : ℝ → (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (hrate : 2 * beta < a0 / (boxPoincareConstant n C) ^ 2)
    (hTt : T ≤ t)
    (hinterfaces : ∀ τ ∈ Icc T t,
      CellEnergyPointwiseInterfaces
        (boxCellEnergy a b u ubar)
        (boxCellEnergyDerivative a b u ut ubar)
        (boxCellGradientNorm a b gradU)
        (boxMotilityForcingNorm a b U L gradV)
        a0 (boxPoincareConstant n C) τ)
    (hVrate : ∀ τ ∈ Icc T t,
      boxSignalGradientNorm a b gradV τ ≤
        CV * (1 + (τ - T)) ^ (-beta)) :
    boxCellEnergy a b u ubar t ≤
      (boxCellEnergy a b u ubar T -
          polynomialBarrier
            (a0 / (boxPoincareConstant n C) ^ 2) (2 * beta)
            ((U * L * CV) ^ 2 / a0)) *
          Real.exp (-(a0 / (boxPoincareConstant n C) ^ 2) * (t - T)) +
        polynomialBarrier
          (a0 / (boxPoincareConstant n C) ^ 2) (2 * beta)
          ((U * L * CV) ^ 2 / a0) *
          (1 + (t - T)) ^ (-(2 * beta)) := by
  have hCp : 0 < boxPoincareConstant n C :=
    boxPoincareConstant_pos hside hSideBound
  have hUL0 : 0 ≤ U * L := mul_nonneg hU0 hL0
  have hCH0 : 0 ≤ U * L * CV := mul_nonneg hUL0 hCV0
  have hHrate : ∀ τ ∈ Icc T t,
      boxMotilityForcingNorm a b U L gradV τ ≤
        (U * L * CV) * (1 + (τ - T)) ^ (-beta) := by
    intro τ hτ
    unfold boxMotilityForcingNorm
    calc
      (U * L) * boxSignalGradientNorm a b gradV τ ≤
          (U * L) * (CV * (1 + (τ - T)) ^ (-beta)) :=
        mul_le_mul_of_nonneg_left (hVrate τ hτ) hUL0
      _ = (U * L * CV) * (1 + (τ - T)) ^ (-beta) := by ring
  exact cellEnergy_polynomialDecay_from_pointwiseInterfaces
    ha0 hCp hCH0 hbeta hrate hTt hinterfaces hHrate

end AMLStabilization

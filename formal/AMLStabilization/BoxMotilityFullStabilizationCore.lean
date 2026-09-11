import Mathlib
import AMLStabilization.BoxMotilityCellDecayCore
import AMLStabilization.FullStabilizationAssembly

namespace AMLStabilization

/--
Full exponential stabilization assembly for the rectangular-box motility
system.  The cell energy derivative, Poincare inequality, and raw cell-energy
identity are supplied by the packaged box PDE interfaces; only the strong
signal rate, comparison of the `L²` signal gradient with that strong norm, and
the Choi-type parabolic upgrade remain as analytic interfaces.
-/
theorem boxMotilityFullExponentialStabilization_from_analytic_interfaces
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    (hside : ∀ j, a j < b j)
    {C Ubd Lphi Cvg CV Cq Ch a0 lambda T t ubar : ℝ}
    (hSideBound : ∀ j, b j - a j ≤ C)
    (hUbd0 : 0 ≤ Ubd) (hLphi0 : 0 ≤ Lphi) (hCvg0 : 0 ≤ Cvg)
    (hCV0 : 0 ≤ CV) (hCq : 0 ≤ Cq) (hCh : 0 ≤ Ch)
    (ha0 : 0 < a0) (hlambda : 0 < lambda)
    (u ut : ℝ → (Fin (n + 1) → ℝ) → ℝ)
    (gradU gradV : ℝ → (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (Vstrong CellSup : ℝ → ℝ)
    (hrate : 2 * lambda < a0 / (boxPoincareConstant n C) ^ 2)
    (hTt : T ≤ t)
    (hVrate : ∀ τ,
      Vstrong τ ≤ CV * Real.exp (-lambda * (τ - T)))
    (hGradByStrong : ∀ τ,
      boxSignalGradientNorm a b gradV τ ≤ Cvg * Vstrong τ)
    (hinterfaces : ∀ τ,
      CellEnergyPointwiseInterfaces
        (boxCellEnergy a b u ubar)
        (boxCellEnergyDerivative a b u ut ubar)
        (boxCellGradientNorm a b gradU)
        (boxMotilityForcingNorm a b Ubd Lphi gradV)
        a0 (boxPoincareConstant n C) τ)
    (hChoi : CellSup t ≤
      Cq * Real.sqrt (boxCellEnergy a b u ubar t) +
        Ch * boxMotilityForcingNorm a b Ubd Lphi gradV t) :
    Vstrong t ≤ CV * Real.exp (-lambda * (t - T)) ∧
    CellSup t ≤
      (Cq * Real.sqrt
          (boxCellEnergy a b u ubar T +
            exponentialBarrier
              (a0 / (boxPoincareConstant n C) ^ 2) (2 * lambda)
              (((Ubd * Lphi * Cvg) * CV) ^ 2 / a0)) +
        Ch * ((Ubd * Lphi * Cvg) * CV)) *
        Real.exp (-lambda * (t - T)) := by
  have hCp : 0 < boxPoincareConstant n C :=
    boxPoincareConstant_pos hside hSideBound
  have hUL0 : 0 ≤ Ubd * Lphi := mul_nonneg hUbd0 hLphi0
  have hLtot0 : 0 ≤ Ubd * Lphi * Cvg := mul_nonneg hUL0 hCvg0
  have hHbyV : ∀ τ,
      boxMotilityForcingNorm a b Ubd Lphi gradV τ ≤
        (Ubd * Lphi * Cvg) * Vstrong τ := by
    intro τ
    unfold boxMotilityForcingNorm
    calc
      (Ubd * Lphi) * boxSignalGradientNorm a b gradV τ ≤
          (Ubd * Lphi) * (Cvg * Vstrong τ) :=
        mul_le_mul_of_nonneg_left (hGradByStrong τ) hUL0
      _ = (Ubd * Lphi * Cvg) * Vstrong τ := by ring
  exact fullExponentialStabilization_from_analytic_interfaces
    (Vnorm := Vstrong)
    (H := boxMotilityForcingNorm a b Ubd Lphi gradV)
    (Q := boxCellEnergy a b u ubar)
    (dQ := boxCellEnergyDerivative a b u ut ubar)
    (g := boxCellGradientNorm a b gradU)
    (U := CellSup)
    (a := a0) (Cp := boxPoincareConstant n C)
    (CV := CV) (L := Ubd * Lphi * Cvg)
    (Cq := Cq) (Ch := Ch) (lambda := lambda) (T := T) (t := t)
    ha0 hCp hCV0 hLtot0 hCq hCh hlambda hrate hTt hVrate
    (fun τ => (hinterfaces τ).H_nonneg)
    hHbyV
    (fun τ => (hinterfaces τ).deriv)
    (fun τ => (hinterfaces τ).Q_nonneg)
    (fun τ => (hinterfaces τ).g_nonneg)
    (fun τ => (hinterfaces τ).poincare)
    (fun τ => (hinterfaces τ).energy)
    hChoi

/-- Polynomial full-stabilization counterpart for the degenerate branch. -/
theorem boxMotilityFullPolynomialStabilization_from_analytic_interfaces
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    (hside : ∀ j, a j < b j)
    {C Ubd Lphi Cvg CV Cq Ch a0 beta T t ubar : ℝ}
    (hSideBound : ∀ j, b j - a j ≤ C)
    (hUbd0 : 0 ≤ Ubd) (hLphi0 : 0 ≤ Lphi) (hCvg0 : 0 ≤ Cvg)
    (hCV0 : 0 ≤ CV) (hCq : 0 ≤ Cq) (hCh : 0 ≤ Ch)
    (ha0 : 0 < a0) (hbeta : 0 < beta)
    (u ut : ℝ → (Fin (n + 1) → ℝ) → ℝ)
    (gradU gradV : ℝ → (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (Vstrong CellSup : ℝ → ℝ)
    (hrate : 2 * beta < a0 / (boxPoincareConstant n C) ^ 2)
    (hTt : T ≤ t)
    (hVrate : ∀ τ ∈ Set.Icc T t,
      Vstrong τ ≤ CV * (1 + (τ - T)) ^ (-beta))
    (hGradByStrong : ∀ τ ∈ Set.Icc T t,
      boxSignalGradientNorm a b gradV τ ≤ Cvg * Vstrong τ)
    (hinterfaces : ∀ τ ∈ Set.Icc T t,
      CellEnergyPointwiseInterfaces
        (boxCellEnergy a b u ubar)
        (boxCellEnergyDerivative a b u ut ubar)
        (boxCellGradientNorm a b gradU)
        (boxMotilityForcingNorm a b Ubd Lphi gradV)
        a0 (boxPoincareConstant n C) τ)
    (hChoi : CellSup t ≤
      Cq * Real.sqrt (boxCellEnergy a b u ubar t) +
        Ch * boxMotilityForcingNorm a b Ubd Lphi gradV t) :
    Vstrong t ≤ CV * (1 + (t - T)) ^ (-beta) ∧
    CellSup t ≤
      (Cq * Real.sqrt
          (boxCellEnergy a b u ubar T +
            polynomialBarrier
              (a0 / (boxPoincareConstant n C) ^ 2) (2 * beta)
              (((Ubd * Lphi * Cvg) * CV) ^ 2 / a0)) +
        Ch * ((Ubd * Lphi * Cvg) * CV)) *
        (1 + (t - T)) ^ (-beta) := by
  have hCp : 0 < boxPoincareConstant n C :=
    boxPoincareConstant_pos hside hSideBound
  have hUL0 : 0 ≤ Ubd * Lphi := mul_nonneg hUbd0 hLphi0
  have hLtot0 : 0 ≤ Ubd * Lphi * Cvg := mul_nonneg hUL0 hCvg0
  have hHbyV : ∀ τ ∈ Set.Icc T t,
      boxMotilityForcingNorm a b Ubd Lphi gradV τ ≤
        (Ubd * Lphi * Cvg) * Vstrong τ := by
    intro τ hτ
    unfold boxMotilityForcingNorm
    calc
      (Ubd * Lphi) * boxSignalGradientNorm a b gradV τ ≤
          (Ubd * Lphi) * (Cvg * Vstrong τ) :=
        mul_le_mul_of_nonneg_left (hGradByStrong τ hτ) hUL0
      _ = (Ubd * Lphi * Cvg) * Vstrong τ := by ring
  exact fullPolynomialStabilization_from_analytic_interfaces
    (Vnorm := Vstrong)
    (H := boxMotilityForcingNorm a b Ubd Lphi gradV)
    (Q := boxCellEnergy a b u ubar)
    (dQ := boxCellEnergyDerivative a b u ut ubar)
    (g := boxCellGradientNorm a b gradU)
    (U := CellSup)
    (a := a0) (Cp := boxPoincareConstant n C)
    (CV := CV) (L := Ubd * Lphi * Cvg)
    (Cq := Cq) (Ch := Ch) (b := beta) (T := T) (t := t)
    ha0 hCp hCV0 hLtot0 hCq hCh hbeta hrate hTt hVrate
    (fun τ hτ => (hinterfaces τ hτ).H_nonneg)
    hHbyV
    (fun τ hτ => (hinterfaces τ hτ).deriv)
    (fun τ hτ => (hinterfaces τ hτ).Q_nonneg)
    (fun τ hτ => (hinterfaces τ hτ).g_nonneg)
    (fun τ hτ => (hinterfaces τ hτ).poincare)
    (fun τ hτ => (hinterfaces τ hτ).energy)
    hChoi

end AMLStabilization

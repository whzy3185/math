import Mathlib
import AMLStabilization.BoxMotilityCellScalarInterfaceCore
import AMLStabilization.CellEnergyAssembly

namespace AMLStabilization

/--
Exponential cell-energy decay driven by a single packaged pointwise interface.
The derivative, nonnegativity, Poincare, and raw energy hypotheses are extracted
from `CellEnergyPointwiseInterfaces` instead of being supplied independently.
-/
theorem cellEnergy_exponentialDecay_from_pointwiseInterfaces
    {Q dQ g H : ℝ → ℝ}
    {a Cp CH lambda T s t : ℝ}
    (ha : 0 < a) (hCp : 0 < Cp) (hCH : 0 ≤ CH) (hlambda : 0 < lambda)
    (hrate : 2 * lambda < a / Cp ^ 2)
    (hinterfaces : ∀ τ, CellEnergyPointwiseInterfaces Q dQ g H a Cp τ)
    (hHrate : ∀ τ, H τ ≤ CH * Real.exp (-lambda * (τ - T)))
    (hst : s ≤ t) :
    Q t ≤
      (Q s - exponentialBarrier (a / Cp ^ 2) (2 * lambda) (CH ^ 2 / a) *
          Real.exp (-(2 * lambda) * (s - T))) *
        Real.exp (-(a / Cp ^ 2) * (t - s)) +
      exponentialBarrier (a / Cp ^ 2) (2 * lambda) (CH ^ 2 / a) *
        Real.exp (-(2 * lambda) * (t - T)) := by
  apply cellEnergy_exponentialDecay_from_gradientRate
    ha hCp hCH hlambda hrate
    (fun τ => (hinterfaces τ).deriv)
    (fun τ => (hinterfaces τ).Q_nonneg)
    (fun τ => (hinterfaces τ).g_nonneg)
    (fun τ => (hinterfaces τ).H_nonneg)
    (fun τ => (hinterfaces τ).poincare)
    (fun τ => (hinterfaces τ).energy)
    hHrate hst

/--
Polynomial cell-energy decay driven by packaged pointwise interfaces on the
relevant time interval.
-/
theorem cellEnergy_polynomialDecay_from_pointwiseInterfaces
    {Q dQ g H : ℝ → ℝ}
    {a Cp CH b T t : ℝ}
    (ha : 0 < a) (hCp : 0 < Cp) (hCH : 0 ≤ CH) (hb : 0 < b)
    (hrate : 2 * b < a / Cp ^ 2)
    (hTt : T ≤ t)
    (hinterfaces : ∀ τ ∈ Set.Icc T t,
      CellEnergyPointwiseInterfaces Q dQ g H a Cp τ)
    (hHrate : ∀ τ ∈ Set.Icc T t,
      H τ ≤ CH * (1 + (τ - T)) ^ (-b)) :
    Q t ≤
      (Q T - polynomialBarrier (a / Cp ^ 2) (2 * b) (CH ^ 2 / a)) *
          Real.exp (-(a / Cp ^ 2) * (t - T)) +
        polynomialBarrier (a / Cp ^ 2) (2 * b) (CH ^ 2 / a) *
          (1 + (t - T)) ^ (-(2 * b)) := by
  apply cellEnergy_polynomialDecay_from_gradientRate
    ha hCp hCH hb hrate hTt
    (fun τ hτ => (hinterfaces τ hτ).deriv)
    (fun τ hτ => (hinterfaces τ hτ).Q_nonneg)
    (fun τ hτ => (hinterfaces τ hτ).g_nonneg)
    (fun τ hτ => (hinterfaces τ hτ).H_nonneg)
    (fun τ hτ => (hinterfaces τ hτ).poincare)
    (fun τ hτ => (hinterfaces τ hτ).energy)
    hHrate

end AMLStabilization

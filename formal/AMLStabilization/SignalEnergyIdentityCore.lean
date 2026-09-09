import Mathlib
import AMLStabilization.SignalEnergyBridge

open MeasureTheory

namespace AMLStabilization

/--
Pointwise one-sided dissipativity, after multiplication by a nonnegative density,
implies the corresponding integral reaction estimate.
-/
theorem dissipativeReactionIntegral
    {Ω : Type*} [MeasurableSpace Ω]
    {μ : Measure Ω} {u w R : Ω → ℝ} {beta : ℝ}
    (hu : ∀ x, 0 ≤ u x)
    (hpoint : ∀ x, w x * R x ≤ -beta * w x ^ 2)
    (hreaction : Integrable (fun x => u x * (w x * R x)) μ)
    (hweighted : Integrable (fun x => u x * w x ^ 2) μ) :
    (∫ x, u x * (w x * R x) ∂μ) ≤
      -beta * (∫ x, u x * w x ^ 2 ∂μ) := by
  have hright : Integrable (fun x => (-beta) * (u x * w x ^ 2)) μ :=
    hweighted.const_mul (-beta)
  calc
    (∫ x, u x * (w x * R x) ∂μ) ≤
        ∫ x, (-beta) * (u x * w x ^ 2) ∂μ := by
      refine integral_mono_ae hreaction hright ?_
      filter_upwards with x
      have hx := mul_le_mul_of_nonneg_left (hpoint x) (hu x)
      simpa [mul_assoc, mul_left_comm, mul_comm] using hx
    _ = -beta * (∫ x, u x * w x ^ 2 ∂μ) := by
      rw [integral_const_mul]

/--
Concrete energy-identity interface.  `hEnergyDerivative` is differentiation of
`E = ∫ w^2`; `hPDEPairing` is the PDE tested against `w`; and `hGreen` is the
Neumann integration-by-parts identity.  Lean verifies all algebra after these
standard analytic identities.
-/
theorem signalEnergyInequality_from_integralPDE
    {Ω : Type*} [MeasurableSpace Ω]
    {μ : Measure Ω} {u w wt lap R : Ω → ℝ}
    {dE gradSq beta : ℝ}
    (hu : ∀ x, 0 ≤ u x)
    (hpoint : ∀ x, w x * R x ≤ -beta * w x ^ 2)
    (hreaction : Integrable (fun x => u x * (w x * R x)) μ)
    (hweighted : Integrable (fun x => u x * w x ^ 2) μ)
    (hEnergyDerivative : dE = 2 * (∫ x, w x * wt x ∂μ))
    (hPDEPairing :
      (∫ x, w x * wt x ∂μ) =
        (∫ x, w x * lap x ∂μ) +
          (∫ x, u x * (w x * R x) ∂μ))
    (hGreen : (∫ x, w x * lap x ∂μ) = -gradSq) :
    dE + 2 * (gradSq + beta * (∫ x, u x * w x ^ 2 ∂μ)) ≤ 0 := by
  have hreact := dissipativeReactionIntegral
    (μ := μ) (u := u) (w := w) (R := R) (beta := beta)
    hu hpoint hreaction hweighted
  rw [hPDEPairing, hGreen] at hEnergyDerivative
  linarith

/-- Exact production-consumption specialization after shifting `v` by `1/alpha`.
The reaction is `R = -alpha*w`, so the dissipativity is an equality. -/
theorem productionConsumption_signalEnergyInequality
    {Ω : Type*} [MeasurableSpace Ω]
    {μ : Measure Ω} {u w wt lap : Ω → ℝ}
    {dE gradSq alpha : ℝ}
    (hu : ∀ x, 0 ≤ u x)
    (hreaction : Integrable (fun x => u x * (w x * (-alpha * w x))) μ)
    (hweighted : Integrable (fun x => u x * w x ^ 2) μ)
    (hEnergyDerivative : dE = 2 * (∫ x, w x * wt x ∂μ))
    (hPDEPairing :
      (∫ x, w x * wt x ∂μ) =
        (∫ x, w x * lap x ∂μ) +
          (∫ x, u x * (w x * (-alpha * w x)) ∂μ))
    (hGreen : (∫ x, w x * lap x ∂μ) = -gradSq) :
    dE + 2 * (gradSq + alpha * (∫ x, u x * w x ^ 2 ∂μ)) ≤ 0 := by
  apply signalEnergyInequality_from_integralPDE
    (μ := μ) (u := u) (w := w) (wt := wt) (lap := lap)
    (R := fun x => -alpha * w x)
    (dE := dE) (gradSq := gradSq) (beta := alpha)
    hu
  · intro x
    ring_nf
    exact le_rfl
  · exact hreaction
  · exact hweighted
  · exact hEnergyDerivative
  · exact hPDEPairing
  · exact hGreen

end AMLStabilization

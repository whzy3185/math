import Mathlib

open MeasureTheory

namespace AMLStabilization

/--
Arbitrary-order pointwise dissipativity, after multiplication by a nonnegative
weight, implies the corresponding weighted integral reaction estimate.
-/
theorem dissipativeReactionIntegral_q
    {Omega : Type*} [MeasurableSpace Omega]
    {mu : Measure Omega} {u w R : Omega → ℝ} {beta q : ℝ}
    (hu : ∀ x, 0 ≤ u x)
    (hpoint : ∀ x, w x * R x ≤ -beta * |w x| ^ q)
    (hreaction : Integrable (fun x => u x * (w x * R x)) mu)
    (hweighted : Integrable (fun x => u x * |w x| ^ q) mu) :
    (∫ x, u x * (w x * R x) ∂mu) ≤
      -beta * (∫ x, u x * |w x| ^ q ∂mu) := by
  have hright : Integrable (fun x => (-beta) * (u x * |w x| ^ q)) mu :=
    hweighted.const_mul (-beta)
  calc
    (∫ x, u x * (w x * R x) ∂mu) ≤
        ∫ x, (-beta) * (u x * |w x| ^ q) ∂mu := by
      refine integral_mono_ae hreaction hright ?_
      filter_upwards with x
      have hx := mul_le_mul_of_nonneg_left (hpoint x) (hu x)
      simpa [mul_assoc, mul_left_comm, mul_comm] using hx
    _ = -beta * (∫ x, u x * |w x| ^ q ∂mu) := by
      rw [integral_const_mul]

/--
Arbitrary-`q` signal energy inequality from the same three analytic interfaces
used in the quadratic proof: differentiation of `∫w²`, PDE pairing against
`w`, and the Neumann Green identity.  All reaction and coefficient algebra is
internal to Lean.
-/
theorem signalEnergyInequality_q_from_integralPDE
    {Omega : Type*} [MeasurableSpace Omega]
    {mu : Measure Omega} {u w wt lap R : Omega → ℝ}
    {dE gradSq beta q : ℝ}
    (hu : ∀ x, 0 ≤ u x)
    (hpoint : ∀ x, w x * R x ≤ -beta * |w x| ^ q)
    (hreaction : Integrable (fun x => u x * (w x * R x)) mu)
    (hweighted : Integrable (fun x => u x * |w x| ^ q) mu)
    (hEnergyDerivative : dE = 2 * (∫ x, w x * wt x ∂mu))
    (hPDEPairing :
      (∫ x, w x * wt x ∂mu) =
        (∫ x, w x * lap x ∂mu) +
          (∫ x, u x * (w x * R x) ∂mu))
    (hGreen : (∫ x, w x * lap x ∂mu) = -gradSq) :
    dE + 2 * (gradSq + beta * (∫ x, u x * |w x| ^ q ∂mu)) ≤ 0 := by
  have hreact := dissipativeReactionIntegral_q
    (mu := mu) (u := u) (w := w) (R := R) (beta := beta) (q := q)
    hu hpoint hreaction hweighted
  rw [hPDEPairing, hGreen] at hEnergyDerivative
  linarith

/-- Cubically degenerate reaction specializes the arbitrary-order energy identity to `q=4`. -/
theorem cubicDegenerate_signalEnergyInequality
    {Omega : Type*} [MeasurableSpace Omega]
    {mu : Measure Omega} {u w wt lap : Omega → ℝ}
    {dE gradSq kappa : ℝ}
    (hkappa : 0 ≤ kappa)
    (hu : ∀ x, 0 ≤ u x)
    (hreaction : Integrable (fun x => u x * (w x * (-kappa * w x ^ 3))) mu)
    (hweighted : Integrable (fun x => u x * |w x| ^ (4 : ℝ)) mu)
    (hEnergyDerivative : dE = 2 * (∫ x, w x * wt x ∂mu))
    (hPDEPairing :
      (∫ x, w x * wt x ∂mu) =
        (∫ x, w x * lap x ∂mu) +
          (∫ x, u x * (w x * (-kappa * w x ^ 3)) ∂mu))
    (hGreen : (∫ x, w x * lap x ∂mu) = -gradSq) :
    dE + 2 * (gradSq + kappa * (∫ x, u x * |w x| ^ (4 : ℝ) ∂mu)) ≤ 0 := by
  apply signalEnergyInequality_q_from_integralPDE
    (mu := mu) (u := u) (w := w) (wt := wt) (lap := lap)
    (R := fun x => -kappa * w x ^ 3)
    (dE := dE) (gradSq := gradSq) (beta := kappa) (q := (4 : ℝ))
    hu
  · intro x
    have habs4 : |w x| ^ (4 : ℝ) = w x ^ 4 := by
      rw [Real.rpow_natCast]
      norm_num [abs_pow]
    rw [habs4]
    ring_nf
    exact le_rfl
  · exact hreaction
  · exact hweighted
  · exact hEnergyDerivative
  · exact hPDEPairing
  · exact hGreen

end AMLStabilization

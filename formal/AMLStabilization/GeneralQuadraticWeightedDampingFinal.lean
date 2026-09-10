import Mathlib
import AMLStabilization.FinalSignalAssembly
import AMLStabilization.SignalEnergyIdentityCore

open MeasureTheory

namespace AMLStabilization

/--
End-to-end general quadratic weighted-damping theorem under the same named
analytic interfaces as the production-consumption specialization.  Unlike
`ProductionConsumptionSignalFinal`, the reaction `R` is arbitrary and is only
assumed to satisfy `w R <= -beta w^2`.
-/
theorem generalQuadraticWeightedDamping_exponentialDecay_from_interfaces
    {Omega : Type*} [MeasurableSpace Omega]
    {mu : Measure Omega}
    {u w wt lap R : ℝ → Omega → ℝ}
    {wbar E dE grad : ℝ → ℝ}
    {m K Cp V beta s t : ℝ}
    (hm : 0 < m)
    (hK : 0 ≤ K)
    (hCp : 0 ≤ Cp)
    (hV : 0 ≤ V)
    (hbeta : 0 < beta)
    (hEderiv : ∀ tau, HasDerivAt E (dE tau) tau)
    (hEvalue : ∀ tau, E tau = (∫ x, w tau x ^ 2 ∂mu))
    (huNonneg : ∀ tau x, 0 ≤ u tau x)
    (hgradNonneg : ∀ tau, 0 ≤ grad tau)
    (huInt : ∀ tau, Integrable (u tau) mu)
    (huwInt : ∀ tau, Integrable (fun x => u tau x * w tau x) mu)
    (hmass : ∀ tau, (∫ x, u tau x ∂mu) = m)
    (hsqrtu : ∀ tau, MemLp (fun x => Real.sqrt (u tau x)) 2 mu)
    (hsqrtuw : ∀ tau, MemLp (fun x => Real.sqrt (u tau x) * w tau x) 2 mu)
    (huL2 : ∀ tau, MemLp (u tau) 2 mu)
    (hdevL2 : ∀ tau, MemLp (fun x => w tau x - wbar tau) 2 mu)
    (huL2bound : ∀ tau, Real.sqrt (∫ x, u tau x ^ 2 ∂mu) ≤ K)
    (hwInt : ∀ tau, Integrable (w tau) mu)
    (hw2Int : ∀ tau, Integrable (fun x => w tau x ^ 2) mu)
    (honeInt : Integrable (fun _ : Omega => (1 : ℝ)) mu)
    (hvol : (∫ _ : Omega, (1 : ℝ) ∂mu) = V)
    (hmean : ∀ tau, (∫ x, w tau x ∂mu) = V * wbar tau)
    (hPoincare : ∀ tau,
      Real.sqrt (∫ x, (w tau x - wbar tau) ^ 2 ∂mu) ≤ Cp * grad tau)
    (hweightedInt : ∀ tau, Integrable (fun x => u tau x * w tau x ^ 2) mu)
    (hreactionInt : ∀ tau,
      Integrable (fun x => u tau x * (w tau x * R tau x)) mu)
    (hpoint : ∀ tau x, w tau x * R tau x ≤ -beta * w tau x ^ 2)
    (hEnergyDerivative : ∀ tau,
      dE tau = 2 * (∫ x, w tau x * wt tau x ∂mu))
    (hPDEPairing : ∀ tau,
      (∫ x, w tau x * wt tau x ∂mu) =
        (∫ x, w tau x * lap tau x ∂mu) +
          (∫ x, u tau x * (w tau x * R tau x) ∂mu))
    (hGreen : ∀ tau,
      (∫ x, w tau x * lap tau x ∂mu) = -(grad tau) ^ 2)
    (hst : s ≤ t) :
    E t ≤ E s *
      Real.exp (-(2 * min 1 beta /
        (1 + massWeightedA m K Cp V + massWeightedB m V)) * (t - s)) := by
  let weighted : ℝ → ℝ := fun tau => ∫ x, u tau x * w tau x ^ 2 ∂mu
  let gradSq : ℝ → ℝ := fun tau => (grad tau) ^ 2
  have hgradSq : ∀ tau, 0 ≤ gradSq tau := by
    intro tau
    exact sq_nonneg (grad tau)
  have hweighted : ∀ tau, 0 ≤ weighted tau := by
    intro tau
    exact integral_nonneg (fun x => mul_nonneg (huNonneg tau x) (sq_nonneg (w tau x)))
  have hcoerc : ∀ tau,
      E tau ≤ massWeightedA m K Cp V * gradSq tau +
        massWeightedB m V * weighted tau := by
    intro tau
    have hc := integralMassWeightedCoercivity_of_MemLp_and_Poincare
      (μ := mu) (ρ := u tau) (f := w tau)
      (m := m) (K := K) (Cp := Cp) (grad := grad tau)
      (fbar := wbar tau) (V := V)
      hm hK hCp (hgradNonneg tau) hV (huNonneg tau)
      (huInt tau) (huwInt tau) (hmass tau)
      (hsqrtu tau) (hsqrtuw tau) (huL2 tau) (hdevL2 tau) (huL2bound tau)
      (hwInt tau) (hw2Int tau) honeInt hvol (hmean tau) (hPoincare tau)
    rw [hEvalue tau]
    simpa [massWeightedA, massWeightedB, gradSq, weighted] using hc
  have henergy : ∀ tau,
      dE tau + 2 * (gradSq tau + beta * weighted tau) ≤ 0 := by
    intro tau
    have he := signalEnergyInequality_from_integralPDE
      (μ := mu) (u := u tau) (w := w tau) (wt := wt tau) (lap := lap tau)
      (R := R tau) (dE := dE tau) (gradSq := gradSq tau) (beta := beta)
      (huNonneg tau) (hpoint tau) (hreactionInt tau) (hweightedInt tau)
      (hEnergyDerivative tau) (hPDEPairing tau)
      (by simpa [gradSq] using hGreen tau)
    simpa [weighted] using he
  have hdelta : 0 ≤ min 1 beta := le_min zero_le_one (le_of_lt hbeta)
  exact massWeightedSignal_exponentialDecay
    (E := E) (dE := dE) (gradSq := gradSq) (weighted := weighted)
    (m := m) (K := K) (Cp := Cp) (V := V)
    (alpha := beta) (delta := min 1 beta) (s := s) (t := t)
    hEderiv hm hK hCp hV hdelta (min_le_left _ _) (min_le_right _ _)
    hgradSq hweighted hcoerc henergy hst

end AMLStabilization

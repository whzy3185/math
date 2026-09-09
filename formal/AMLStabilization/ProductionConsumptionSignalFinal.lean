import AMLStabilization.FinalSignalAssembly

open MeasureTheory

namespace AMLStabilization

/--
End-to-end formal theorem for the signal L2-decay mechanism in the
production-consumption model, up to the explicitly named analytic interfaces
that are not presently available in mathlib for arbitrary smooth bounded
Neumann domains.

Here `w = v - 1/alpha`, `grad t` is the L2 norm of the spatial gradient of
`w(t)`, and `E(t) = int w(t)^2`.  All Holder, mean-decomposition, weighted
coercivity, reaction-dissipation, coefficient normalization, and Gronwall steps
are discharged internally.
-/
theorem productionConsumptionSignal_exponentialDecay_from_interfaces
    {Ω : Type*} [MeasurableSpace Ω]
    {μ : Measure Ω}
    {u w wt lap : ℝ → Ω → ℝ}
    {wbar E dE grad : ℝ → ℝ}
    {m K Cp V alpha s t : ℝ}
    (hm : 0 < m)
    (hK : 0 ≤ K)
    (hCp : 0 ≤ Cp)
    (hV : 0 ≤ V)
    (halpha : 0 < alpha)
    (hEderiv : ∀ τ, HasDerivAt E (dE τ) τ)
    (hEvalue : ∀ τ, E τ = (∫ x, w τ x ^ 2 ∂μ))
    (huNonneg : ∀ τ x, 0 ≤ u τ x)
    (hgradNonneg : ∀ τ, 0 ≤ grad τ)
    (huInt : ∀ τ, Integrable (u τ) μ)
    (huwInt : ∀ τ, Integrable (fun x => u τ x * w τ x) μ)
    (hmass : ∀ τ, (∫ x, u τ x ∂μ) = m)
    (hsqrtu : ∀ τ, MemLp (fun x => Real.sqrt (u τ x)) 2 μ)
    (hsqrtuw : ∀ τ, MemLp (fun x => Real.sqrt (u τ x) * w τ x) 2 μ)
    (huL2 : ∀ τ, MemLp (u τ) 2 μ)
    (hdevL2 : ∀ τ, MemLp (fun x => w τ x - wbar τ) 2 μ)
    (huL2bound : ∀ τ, Real.sqrt (∫ x, u τ x ^ 2 ∂μ) ≤ K)
    (hwInt : ∀ τ, Integrable (w τ) μ)
    (hw2Int : ∀ τ, Integrable (fun x => w τ x ^ 2) μ)
    (honeInt : Integrable (fun _ : Ω => (1 : ℝ)) μ)
    (hvol : (∫ _ : Ω, (1 : ℝ) ∂μ) = V)
    (hmean : ∀ τ, (∫ x, w τ x ∂μ) = V * wbar τ)
    (hPoincare : ∀ τ,
      Real.sqrt (∫ x, (w τ x - wbar τ) ^ 2 ∂μ) ≤ Cp * grad τ)
    (hweightedInt : ∀ τ, Integrable (fun x => u τ x * w τ x ^ 2) μ)
    (hreactionInt : ∀ τ,
      Integrable (fun x => u τ x * (w τ x * (-alpha * w τ x))) μ)
    (hEnergyDerivative : ∀ τ,
      dE τ = 2 * (∫ x, w τ x * wt τ x ∂μ))
    (hPDEPairing : ∀ τ,
      (∫ x, w τ x * wt τ x ∂μ) =
        (∫ x, w τ x * lap τ x ∂μ) +
          (∫ x, u τ x * (w τ x * (-alpha * w τ x)) ∂μ))
    (hGreen : ∀ τ,
      (∫ x, w τ x * lap τ x ∂μ) = -(grad τ) ^ 2)
    (hst : s ≤ t) :
    E t ≤ E s *
      Real.exp (-(2 * min 1 alpha /
        (1 + massWeightedA m K Cp V + massWeightedB m V)) * (t - s)) := by
  let weighted : ℝ → ℝ := fun τ => ∫ x, u τ x * w τ x ^ 2 ∂μ
  let gradSq : ℝ → ℝ := fun τ => (grad τ) ^ 2
  have hgradSq : ∀ τ, 0 ≤ gradSq τ := by
    intro τ
    exact sq_nonneg (grad τ)
  have hweighted : ∀ τ, 0 ≤ weighted τ := by
    intro τ
    exact integral_nonneg (fun x => mul_nonneg (huNonneg τ x) (sq_nonneg (w τ x)))
  have hcoerc : ∀ τ,
      E τ ≤ massWeightedA m K Cp V * gradSq τ +
        massWeightedB m V * weighted τ := by
    intro τ
    have hc := integralMassWeightedCoercivity_of_MemLp_and_Poincare
      (μ := μ) (ρ := u τ) (f := w τ)
      (m := m) (K := K) (Cp := Cp) (grad := grad τ)
      (fbar := wbar τ) (V := V)
      hm hK hCp (hgradNonneg τ) hV (huNonneg τ)
      (huInt τ) (huwInt τ) (hmass τ)
      (hsqrtu τ) (hsqrtuw τ) (huL2 τ) (hdevL2 τ) (huL2bound τ)
      (hwInt τ) (hw2Int τ) honeInt hvol (hmean τ) (hPoincare τ)
    rw [hEvalue τ]
    simpa [massWeightedA, massWeightedB, gradSq, weighted] using hc
  have henergy : ∀ τ,
      dE τ + 2 * (gradSq τ + alpha * weighted τ) ≤ 0 := by
    intro τ
    have he := productionConsumption_signalEnergyInequality
      (μ := μ) (u := u τ) (w := w τ) (wt := wt τ) (lap := lap τ)
      (dE := dE τ) (gradSq := gradSq τ) (alpha := alpha)
      (huNonneg τ) (hreactionInt τ) (hweightedInt τ)
      (hEnergyDerivative τ) (hPDEPairing τ)
      (by simpa [gradSq] using hGreen τ)
    simpa [weighted] using he
  have hdelta : 0 ≤ min 1 alpha := by
    exact le_min zero_le_one (le_of_lt halpha)
  have hdelta1 : min 1 alpha ≤ 1 := min_le_left _ _
  have hdeltaAlpha : min 1 alpha ≤ alpha := min_le_right _ _
  exact massWeightedSignal_exponentialDecay
    (E := E) (dE := dE) (gradSq := gradSq) (weighted := weighted)
    (m := m) (K := K) (Cp := Cp) (V := V)
    (alpha := alpha) (delta := min 1 alpha) (s := s) (t := t)
    hEderiv hm hK hCp hV hdelta hdelta1 hdeltaAlpha
    hgradSq hweighted hcoerc henergy hst

end AMLStabilization

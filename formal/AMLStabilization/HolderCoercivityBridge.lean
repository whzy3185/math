import AMLStabilization.HolderCore

open MeasureTheory

namespace AMLStabilization

/--
Full integral mass-weighted coercivity theorem with both Cauchy-Schwarz inputs
discharged internally from `MemLp` hypotheses.  The Poincare inequality and the
basic mean-decomposition estimate remain explicit analytic inputs.
-/
theorem integralMassWeightedCoercivity_of_MemLp
    {Ω : Type*} [MeasurableSpace Ω]
    {μ : Measure Ω} {ρ f : Ω → ℝ}
    {m K Cp grad fbar V : ℝ}
    (hm : 0 < m)
    (hK0 : 0 ≤ K)
    (hCp : 0 ≤ Cp)
    (hgrad : 0 ≤ grad)
    (hV : 0 ≤ V)
    (hρnonneg : ∀ x, 0 ≤ ρ x)
    (hρint : Integrable ρ μ)
    (hρfint : Integrable (fun x => ρ x * f x) μ)
    (hmass : (∫ x, ρ x ∂μ) = m)
    (hsqrtρ : MemLp (fun x => Real.sqrt (ρ x)) 2 μ)
    (hsqrtρf : MemLp (fun x => Real.sqrt (ρ x) * f x) 2 μ)
    (hρL2 : MemLp ρ 2 μ)
    (hdevL2 : MemLp (fun x => f x - fbar) 2 μ)
    (hρL2bound : Real.sqrt (∫ x, ρ x ^ 2 ∂μ) ≤ K)
    (hPoincare :
      Real.sqrt (∫ x, (f x - fbar) ^ 2 ∂μ) ≤ Cp * grad)
    (hbase :
      (∫ x, f x ^ 2 ∂μ) ≤
        2 * Cp ^ 2 * grad ^ 2 + 2 * V * fbar ^ 2) :
    (∫ x, f x ^ 2 ∂μ) ≤
      (2 * Cp ^ 2 + 4 * V * (K * Cp / m) ^ 2) * grad ^ 2 +
        4 * V * (Real.sqrt m / m) ^ 2 *
          (∫ x, ρ x * f x ^ 2 ∂μ) := by
  apply integralMassWeightedCoercivity
    (μ := μ) (ρ := ρ) (f := f)
    (m := m) (K := K) (Cp := Cp) (grad := grad) (fbar := fbar) (V := V)
    hm hK0 hCp hgrad hV hρnonneg hρint hρfint hmass
  · simpa [hmass] using
      (weightedFirstMoment_cauchySchwarz
        (μ := μ) (ρ := ρ) (f := f) hρnonneg hsqrtρ hsqrtρf)
  · exact weightedDeviation_cauchySchwarz_of_bound
      (μ := μ) (ρ := ρ) (f := f) (fbar := fbar) hρL2 hdevL2 hρL2bound
  · exact hPoincare
  · exact hbase

end AMLStabilization

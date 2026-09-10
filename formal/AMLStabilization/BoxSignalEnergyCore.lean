import Mathlib
import AMLStabilization.CanonicalBoxGreenCore
import AMLStabilization.SignalPDEPairingCore
import AMLStabilization.GeneralSignalEnergyIdentityQ

open Set Finset MeasureTheory

namespace AMLStabilization

/--
On a rectangular box, the arbitrary-`q` signal energy inequality is derived
from a pointwise reaction-diffusion equation and local Fréchet derivative data.
The integral PDE pairing, local product rule, divergence theorem, zero-Neumann
Green identity, and reaction dissipation are all discharged internally.
-/
theorem boxSignalEnergyInequality_q_from_pointwisePDE
    {n : ℕ}
    {a b : Fin (n + 1) → ℝ}
    (hle : a ≤ b)
    (u w wt R : (Fin (n + 1) → ℝ) → ℝ)
    (dw : (Fin (n + 1) → ℝ) →
      (Fin (n + 1) → ℝ) →L[ℝ] ℝ)
    (dgrad : (Fin (n + 1) → ℝ) → Fin (n + 1) →
      (Fin (n + 1) → ℝ) →L[ℝ] ℝ)
    (bad : Set (Fin (n + 1) → ℝ))
    {dE beta q : ℝ}
    (hu : ∀ x, 0 ≤ u x)
    (hpoint : ∀ x, w x * R x ≤ -beta * |w x| ^ q)
    (hPDE : ∀ x,
      wt x = derivativeTraceLaplacian dgrad x + u x * R x)
    (hEnergyDerivative :
      dE = 2 * (∫ x in Icc a b, w x * wt x))
    (hreaction : IntegrableOn
      (fun x => u x * (w x * R x)) (Icc a b))
    (hweighted : IntegrableOn
      (fun x => u x * |w x| ^ q) (Icc a b))
    (hbad : bad.Countable)
    (hwcont : ContinuousOn w (Icc a b))
    (hgradcont : ∀ i, ContinuousOn
      (fun x => derivativeCoordinateGradient dw x i) (Icc a b))
    (hwdiff : ∀ x,
      x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad →
      HasFDerivAt w (dw x) x)
    (hgradDiff : ∀ x,
      x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad →
      ∀ i, HasFDerivAt
        (fun y => derivativeCoordinateGradient dw y i) (dgrad x i) x)
    (hfront : ∀ i (x : Fin n → ℝ),
      derivativeCoordinateGradient dw (i.insertNth (b i) x) i = 0)
    (hback : ∀ i (x : Fin n → ℝ),
      derivativeCoordinateGradient dw (i.insertNth (a i) x) i = 0)
    (hGradInt : IntegrableOn
      (fun x => ∑ i : Fin (n + 1),
        (derivativeCoordinateGradient dw x i) ^ 2) (Icc a b))
    (hWLapInt : IntegrableOn
      (fun x => w x * derivativeTraceLaplacian dgrad x) (Icc a b)) :
    dE + 2 *
      ((∫ x in Icc a b,
          ∑ i : Fin (n + 1), (derivativeCoordinateGradient dw x i) ^ 2) +
        beta * (∫ x in Icc a b, u x * |w x| ^ q)) ≤ 0 := by
  let mu : Measure (Fin (n + 1) → ℝ) := volume.restrict (Icc a b)
  let lap : (Fin (n + 1) → ℝ) → ℝ :=
    fun x => derivativeTraceLaplacian dgrad x
  have hgreenSet := boxGreenIdentity_from_frechet_data
    hle w dw dgrad bad hbad hwcont hgradcont hwdiff hgradDiff
    hfront hback hGradInt hWLapInt
  have hgreen :
      (∫ x, w x * lap x ∂mu) =
        -(∫ x,
          ∑ i : Fin (n + 1), (derivativeCoordinateGradient dw x i) ^ 2 ∂mu) := by
    simpa [mu, lap] using hgreenSet
  have hLapIntegrable : Integrable (fun x => w x * lap x) mu := by
    simpa [mu, lap] using hWLapInt.integrable
  have hReactionIntegrable : Integrable (fun x => u x * (w x * R x)) mu := by
    simpa [mu] using hreaction.integrable
  have hWeightedIntegrable : Integrable (fun x => u x * |w x| ^ q) mu := by
    simpa [mu] using hweighted.integrable
  have hpair := signalPDEPairing_from_pointwise
    (mu := mu) (u := u) (w := w) (wt := wt) (lap := lap) (R := R)
    (by
      intro x
      simpa [lap] using hPDE x)
    hLapIntegrable hReactionIntegrable
  have hmain := signalEnergyInequality_q_from_integralPDE
    (mu := mu) (u := u) (w := w) (wt := wt) (lap := lap) (R := R)
    (dE := dE)
    (gradSq := ∫ x,
      ∑ i : Fin (n + 1), (derivativeCoordinateGradient dw x i) ^ 2 ∂mu)
    (beta := beta) (q := q)
    hu hpoint
    hReactionIntegrable
    hWeightedIntegrable
    (by simpa [mu] using hEnergyDerivative)
    hpair hgreen
  simpa [mu] using hmain

end AMLStabilization

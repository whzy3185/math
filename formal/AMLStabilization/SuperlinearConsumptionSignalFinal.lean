import Mathlib
import AMLStabilization.SuperlinearConsumptionCore
import AMLStabilization.GeneralWeightedDampingNonnegativeFinal

open MeasureTheory

namespace AMLStabilization

/--
Concrete signal-rate specialization for the superlinear-consumption law

`F(s) = -s * |s|^(ell-1)`,  `ell > 1`.

The pointwise damping hypothesis of the abstract weighted-damping theorem is
no longer an input: it is discharged internally by
`superlinearConsumptionIdentity`.  The remaining hypotheses are precisely the
named geometric/PDE interfaces already isolated in the abstract theorem.
-/
theorem superlinearConsumption_polynomialSignalDecay_from_interfaces
    {Omega : Type*} [MeasurableSpace Omega]
    {mu : Measure Omega}
    {u w wt lap : ℝ → Omega → ℝ}
    {wbar E dE grad : ℝ → ℝ}
    {ell mass K Cp V M s t : ℝ}
    (hell : 1 < ell)
    (hmassPos : 0 < mass)
    (hK : 0 ≤ K)
    (hCp : 0 < Cp)
    (hV : 0 ≤ V)
    (hM : 0 ≤ M)
    (hEderiv : ∀ tau, HasDerivAt E (dE tau) tau)
    (hEvalue : ∀ tau, E tau = (∫ x, w tau x ^ 2 ∂mu))
    (hEnonneg : ∀ tau, 0 ≤ E tau)
    (hEbound : ∀ tau, E tau ≤ M)
    (huNonneg : ∀ tau x, 0 ≤ u tau x)
    (hgradNonneg : ∀ tau, 0 ≤ grad tau)
    (huMeas : ∀ tau, AEStronglyMeasurable (u tau) mu)
    (hwMeas : ∀ tau, AEStronglyMeasurable (w tau) mu)
    (huInt : ∀ tau, Integrable (u tau) mu)
    (huwInt : ∀ tau, Integrable (fun x => u tau x * w tau x) mu)
    (hmass : ∀ tau, (∫ x, u tau x ∂mu) = mass)
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
    (hweightedInt : ∀ tau,
      Integrable (fun x => u tau x * |w tau x| ^ (ell + 1)) mu)
    (hreactionInt : ∀ tau,
      Integrable (fun x =>
        u tau x * (w tau x * superlinearConsumption ell (w tau x))) mu)
    (hEnergyDerivative : ∀ tau,
      dE tau = 2 * (∫ x, w tau x * wt tau x ∂mu))
    (hPDEPairing : ∀ tau,
      (∫ x, w tau x * wt tau x ∂mu) =
        (∫ x, w tau x * lap tau x ∂mu) +
          (∫ x,
            u tau x *
              (w tau x * superlinearConsumption ell (w tau x)) ∂mu))
    (hGreen : ∀ tau,
      (∫ x, w tau x * lap tau x ∂mu) = -(grad tau) ^ 2)
    (hst : s ≤ t) :
    E t ≤
      (E s ^ (-((ell + 1) - 2) / 2) +
        ((ell + 1) - 2) *
          (rateGamma (ell + 1)
            (nonlinearMassWeightedA Cp V K mass)
            (nonlinearMassWeightedB V mass (ell + 1)) 1 M) ^
              (-(ell + 1) / 2) *
          (t - s)) ^ (-2 / ((ell + 1) - 2)) := by
  have hq : 2 < ell + 1 := by linarith
  have hpoint : ∀ tau x,
      w tau x * superlinearConsumption ell (w tau x) ≤
        -(1 : ℝ) * |w tau x| ^ (ell + 1) := by
    intro tau x
    have hid := superlinearConsumptionIdentity
      (m := ell) (s := w tau x) hell
    simpa using hid.le
  exact generalWeightedDamping_polynomialDecay_nonnegative_from_interfaces
    (mu := mu)
    (u := u) (w := w) (wt := wt) (lap := lap)
    (R := fun tau x => superlinearConsumption ell (w tau x))
    (wbar := wbar) (E := E) (dE := dE) (grad := grad)
    (m := mass) (K := K) (Cp := Cp) (V := V)
    (beta := 1) (q := ell + 1) (M := M) (s := s) (t := t)
    hq hmassPos hK hCp hV (by norm_num) hM
    hEderiv hEvalue hEnonneg hEbound huNonneg hgradNonneg
    huMeas hwMeas huInt huwInt hmass huL2 hdevL2 huL2bound
    hwInt hw2Int honeInt hvol hmean hPoincare hweightedInt
    hreactionInt hpoint hEnergyDerivative hPDEPairing hGreen hst

/-- The superlinear damping order satisfies `q-2 = ell-1`, hence the signal
energy exponent is exactly `2/(ell-1)` and the corresponding `L²` norm
exponent is `1/(ell-1)`. -/
theorem superlinearConsumption_rate_exponent_identity
    {ell : ℝ} :
    ((ell + 1) - 2) = ell - 1 ∧
    2 / ((ell + 1) - 2) = 2 / (ell - 1) := by
  constructor <;> ring

end AMLStabilization

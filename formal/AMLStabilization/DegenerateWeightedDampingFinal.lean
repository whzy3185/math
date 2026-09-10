import Mathlib
import AMLStabilization.GeneralWeightedDampingNonnegativeFinal

open MeasureTheory

namespace AMLStabilization

/--
Manuscript-facing degenerate weighted-damping endpoint.  This is the
`q = theta + 2` specialization of the arbitrary-`q` theorem, with the rate
written in the paper's natural parameter `theta`.

In particular the energy power is exactly `2/theta`; after taking a square
root the signal `L²` rate is `1/theta`.
-/
theorem degenerateWeightedDamping_polynomialDecay_from_interfaces
    {Omega : Type*} [MeasurableSpace Omega]
    {mu : Measure Omega}
    {u w wt lap R : ℝ → Omega → ℝ}
    {wbar E dE grad : ℝ → ℝ}
    {mass K Cp V beta theta M s t : ℝ}
    (htheta : 0 < theta)
    (hmass : 0 < mass)
    (hK : 0 ≤ K)
    (hCp : 0 < Cp)
    (hV : 0 ≤ V)
    (hbeta : 0 < beta)
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
    (hmassFixed : ∀ tau, (∫ x, u tau x ∂mu) = mass)
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
      Integrable (fun x => u tau x * |w tau x| ^ (theta + 2)) mu)
    (hreactionInt : ∀ tau,
      Integrable (fun x => u tau x * (w tau x * R tau x)) mu)
    (hpoint : ∀ tau x,
      w tau x * R tau x ≤ -beta * |w tau x| ^ (theta + 2))
    (hEnergyDerivative : ∀ tau,
      dE tau = 2 * (∫ x, w tau x * wt tau x ∂mu))
    (hPDEPairing : ∀ tau,
      (∫ x, w tau x * wt tau x ∂mu) =
        (∫ x, w tau x * lap tau x ∂mu) +
          (∫ x, u tau x * (w tau x * R tau x) ∂mu))
    (hGreen : ∀ tau,
      (∫ x, w tau x * lap tau x ∂mu) = -(grad tau) ^ 2)
    (hst : s ≤ t) :
    E t ≤
      (E s ^ (-theta / 2) +
        theta *
          (rateGamma (theta + 2)
            (nonlinearMassWeightedA Cp V K mass)
            (nonlinearMassWeightedB V mass (theta + 2)) beta M) ^
              (-(theta + 2) / 2) *
          (t - s)) ^ (-2 / theta) := by
  have hq : 2 < theta + 2 := by linarith
  have hmain :=
    generalWeightedDamping_polynomialDecay_nonnegative_from_interfaces
      (mu := mu)
      (u := u) (w := w) (wt := wt) (lap := lap) (R := R)
      (wbar := wbar) (E := E) (dE := dE) (grad := grad)
      (m := mass) (K := K) (Cp := Cp) (V := V)
      (beta := beta) (q := theta + 2) (M := M) (s := s) (t := t)
      hq hmass hK hCp hV hbeta hM
      hEderiv hEvalue hEnonneg hEbound huNonneg hgradNonneg
      huMeas hwMeas huInt huwInt hmassFixed huL2 hdevL2 huL2bound
      hwInt hw2Int honeInt hvol hmean hPoincare hweightedInt
      hreactionInt hpoint hEnergyDerivative hPDEPairing hGreen hst
  have hqminus : (theta + 2) - 2 = theta := by ring
  simpa [hqminus] using hmain

/-- The manuscript's signal exponent is the square-root of the energy exponent. -/
theorem degenerate_energy_to_signal_exponent
    {theta : ℝ} (htheta : 0 < theta) :
    (2 / theta) / 2 = 1 / theta := by
  field_simp [ne_of_gt htheta]

end AMLStabilization

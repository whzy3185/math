import Mathlib

open MeasureTheory

namespace AMLStabilization

/--
The integral PDE pairing used in the signal energy identity follows directly
from the pointwise equation `wt = lap + u*R`.  It is therefore not a genuine
analytic interface once the two summands are integrable.
-/
theorem signalPDEPairing_from_pointwise
    {Omega : Type*} [MeasurableSpace Omega]
    {mu : Measure Omega} {u w wt lap R : Omega → ℝ}
    (hPDE : ∀ x, wt x = lap x + u x * R x)
    (hWLap : Integrable (fun x => w x * lap x) mu)
    (hReaction : Integrable (fun x => u x * (w x * R x)) mu) :
    (∫ x, w x * wt x ∂mu) =
      (∫ x, w x * lap x ∂mu) +
        (∫ x, u x * (w x * R x) ∂mu) := by
  calc
    (∫ x, w x * wt x ∂mu) =
        ∫ x, (w x * lap x + u x * (w x * R x)) ∂mu := by
      apply integral_congr_ae
      filter_upwards with x
      rw [hPDE x]
      ring
    _ = (∫ x, w x * lap x ∂mu) +
        (∫ x, u x * (w x * R x) ∂mu) := by
      rw [integral_add hWLap hReaction]

end AMLStabilization

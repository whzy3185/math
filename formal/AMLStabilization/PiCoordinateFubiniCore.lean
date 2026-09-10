import Mathlib

open MeasureTheory

namespace AMLStabilization

/-- Bochner Fubini for one chosen coordinate of a finite product.  The full
`Measure.pi` integral is rewritten as an integral in that coordinate followed
by an integral over all remaining coordinates. -/
theorem integral_pi_split_coordinate
    {X : Type*} [MeasurableSpace X] {n : ℕ}
    (μ : Fin (n + 1) → Measure X) [∀ j, SigmaFinite (μ j)]
    (i : Fin (n + 1))
    (f : (Fin (n + 1) → X) → ℝ)
    (hf : Integrable f (Measure.pi μ)) :
    (∫ x : Fin (n + 1) → X, f x ∂Measure.pi μ) =
      ∫ xi : X,
        ∫ xr : Fin n → X, f (i.insertNth xi xr)
          ∂Measure.pi (fun j => μ (i.succAbove j))
        ∂μ i := by
  let e := MeasurableEquiv.piFinSuccAbove (fun _ : Fin (n + 1) => X) i
  have hmp := measurePreserving_piFinSuccAbove μ i
  have hcomp : Integrable (f ∘ e.symm)
      ((μ i).prod (Measure.pi fun j => μ (i.succAbove j))) := by
    exact (hmp.symm.integrable_comp_emb e.symm.measurableEmbedding).2 hf
  have hsplit : Integrable
      (fun p : X × (Fin n → X) => f (i.insertNth p.1 p.2))
      ((μ i).prod (Measure.pi fun j => μ (i.succAbove j))) := by
    simpa [e, Function.comp_def, MeasurableEquiv.piFinSuccAbove_symm_apply,
      Fin.insertNthEquiv] using hcomp
  have htransport := hmp.symm.integral_comp' f
  calc
    (∫ x : Fin (n + 1) → X, f x ∂Measure.pi μ) =
        ∫ p : X × (Fin n → X), f (i.insertNth p.1 p.2)
          ∂((μ i).prod (Measure.pi fun j => μ (i.succAbove j))) := by
      symm
      simpa [e, Function.comp_def, MeasurableEquiv.piFinSuccAbove_symm_apply,
        Fin.insertNthEquiv] using htransport
    _ = ∫ xi : X,
        ∫ xr : Fin n → X, f (i.insertNth xi xr)
          ∂Measure.pi (fun j => μ (i.succAbove j))
        ∂μ i := by
      rw [integral_prod _ hsplit]

end AMLStabilization

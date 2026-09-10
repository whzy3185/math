import Mathlib

open MeasureTheory

namespace AMLStabilization

/-- Integration over a product of coordinate pairs is the same as integration
over two independent product samples after the canonical measurable
reassociation `(ι → α × β) ≃ (ι → α) × (ι → β)`. -/
theorem integral_pairedCoordinates_eq_productProducts
    {ι α β : Type*} [Fintype ι]
    [MeasurableSpace α] [MeasurableSpace β]
    (μ : ι → Measure α) (ν : ι → Measure β)
    [∀ i, SigmaFinite (μ i)] [∀ i, SigmaFinite (ν i)]
    (g : (ι → α) × (ι → β) → ℝ) :
    (∫ z : ι → α × β,
        g ((fun i => (z i).1), (fun i => (z i).2))
        ∂Measure.pi (fun i => (μ i).prod (ν i))) =
      ∫ p : (ι → α) × (ι → β), g p
        ∂((Measure.pi μ).prod (Measure.pi ν)) := by
  have h :=
    (measurePreserving_arrowProdEquivProdArrow α β ι μ ν).integral_comp' g
  simpa [MeasurableEquiv.arrowProdEquivProdArrow,
    Equiv.arrowProdEquivProdArrow] using h

/-- Specialization of the paired-coordinate transport to the squared
difference of a scalar observable on two independent product samples. -/
theorem integral_pairedCoordinateDifference_sq
    {ι α : Type*} [Fintype ι] [MeasurableSpace α]
    (μ : ι → Measure α) [∀ i, SigmaFinite (μ i)]
    (f : (ι → α) → ℝ) :
    (∫ z : ι → α × α,
        (f (fun i => (z i).1) - f (fun i => (z i).2)) ^ 2
        ∂Measure.pi (fun i => (μ i).prod (μ i))) =
      ∫ p : (ι → α) × (ι → α), (f p.1 - f p.2) ^ 2
        ∂((Measure.pi μ).prod (Measure.pi μ)) := by
  simpa using integral_pairedCoordinates_eq_productProducts
    μ μ (fun p : (ι → α) × (ι → α) => (f p.1 - f p.2) ^ 2)

end AMLStabilization

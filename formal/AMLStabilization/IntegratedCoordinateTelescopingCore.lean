import Mathlib
import AMLStabilization.CoordinateTelescopingCore

open MeasureTheory

namespace AMLStabilization

/-- One coordinate increment along the hybrid path from the first to the second
component of a paired sample. -/
noncomputable def pairedCoordinateIncrement
    {α : Type*} {n : ℕ}
    (f : (Fin n → α) → ℝ) (z : Fin n → α × α) (k : ℕ) : ℝ :=
  f (coordinateHybrid (fun i => (z i).1) (fun i => (z i).2) k) -
    f (coordinateHybrid (fun i => (z i).1) (fun i => (z i).2) (k + 1))

/-- The finite-coordinate pointwise telescoping inequality can be integrated
against any measure on paired samples.  Integrability of the coordinate
increments is the only analytic input at this layer. -/
theorem integral_coordinateTelescoping_sq_le
    {α : Type*} [MeasurableSpace α] {n : ℕ}
    (ν : Measure (Fin n → α × α))
    (f : (Fin n → α) → ℝ)
    (hDiffInt : Integrable
      (fun z : Fin n → α × α =>
        (f (fun i => (z i).1) - f (fun i => (z i).2)) ^ 2) ν)
    (hStepInt : ∀ k ∈ Finset.range n,
      Integrable (fun z : Fin n → α × α =>
        (pairedCoordinateIncrement f z k) ^ 2) ν) :
    (∫ z : Fin n → α × α,
        (f (fun i => (z i).1) - f (fun i => (z i).2)) ^ 2 ∂ν) ≤
      (n : ℝ) * ∑ k ∈ Finset.range n,
        ∫ z : Fin n → α × α,
          (pairedCoordinateIncrement f z k) ^ 2 ∂ν := by
  have hSumInt : Integrable
      (fun z : Fin n → α × α =>
        ∑ k ∈ Finset.range n, (pairedCoordinateIncrement f z k) ^ 2) ν := by
    simpa only [Finset.sum_apply] using
      (integrable_finsetSum' (Finset.range n) hStepInt)
  have hScaledInt : Integrable
      (fun z : Fin n → α × α =>
        (n : ℝ) * ∑ k ∈ Finset.range n,
          (pairedCoordinateIncrement f z k) ^ 2) ν :=
    hSumInt.const_mul n
  have hmono :
      (∫ z : Fin n → α × α,
        (f (fun i => (z i).1) - f (fun i => (z i).2)) ^ 2 ∂ν) ≤
        ∫ z : Fin n → α × α,
          (n : ℝ) * ∑ k ∈ Finset.range n,
            (pairedCoordinateIncrement f z k) ^ 2 ∂ν := by
    apply integral_mono_ae hDiffInt hScaledInt
    exact Filter.Eventually.of_forall fun z => by
      simpa [pairedCoordinateIncrement] using
        (coordinateTelescoping_sq_le f
          (fun i => (z i).1) (fun i => (z i).2))
  calc
    (∫ z : Fin n → α × α,
        (f (fun i => (z i).1) - f (fun i => (z i).2)) ^ 2 ∂ν)
        ≤ ∫ z : Fin n → α × α,
          (n : ℝ) * ∑ k ∈ Finset.range n,
            (pairedCoordinateIncrement f z k) ^ 2 ∂ν := hmono
    _ = (n : ℝ) *
        ∫ z : Fin n → α × α,
          ∑ k ∈ Finset.range n, (pairedCoordinateIncrement f z k) ^ 2 ∂ν := by
      rw [integral_const_mul]
    _ = (n : ℝ) * ∑ k ∈ Finset.range n,
        ∫ z : Fin n → α × α,
          (pairedCoordinateIncrement f z k) ^ 2 ∂ν := by
      rw [integral_finsetSum (Finset.range n) hStepInt]

end AMLStabilization

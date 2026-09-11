import Mathlib
import AMLStabilization.FullBoxPoincareCore

open Set MeasureTheory Real

namespace AMLStabilization

/-- Square-root form of the fully assembled rectangular-box Poincare theorem.
The effective Poincare constant is `sqrt (n+1) * C`, while the gradient norm
is the square root of the sum of the coordinate derivative energies. -/
theorem rectangularBoxPoincareL2_sqrt
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    (hside : ∀ j, a j < b j)
    {C : ℝ} (hC : 0 ≤ C)
    (hSideBound : ∀ j, b j - a j ≤ C)
    (f : (Fin (n + 1) → ℝ) → ℝ)
    (df : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (hfLp : MemLp f 2 (rectangularBoxMeasure a b))
    (hDiffInt : Integrable
      (fun z : Fin (n + 1) → ℝ × ℝ =>
        (f (fun i => (z i).1) - f (fun i => (z i).2)) ^ 2)
      (rectangularPairedBoxMeasure a b))
    (hStepInt : ∀ i : Fin (n + 1), Integrable
      (fun z : Fin (n + 1) → ℝ × ℝ =>
        (pairedCoordinateIncrement f z i.val) ^ 2)
      (rectangularPairedBoxMeasure a b))
    (hDerivInt : ∀ i : Fin (n + 1), Integrable
      (fun x : Fin (n + 1) → ℝ => (df x i) ^ 2)
      (rectangularBoxMeasure a b))
    (hFiberDeriv : ∀ i : Fin (n + 1), ∀ xr : Fin n → ℝ,
      ∀ t ∈ Icc (a i) (b i),
        HasDerivAt (fun s => f (i.insertNth s xr))
          (df (i.insertNth t xr) i) t)
    (hFiberCont : ∀ i : Fin (n + 1), ∀ xr : Fin n → ℝ,
      ContinuousOn (fun t => f (i.insertNth t xr)) (Icc (a i) (b i)))
    (hFiberDCont : ∀ i : Fin (n + 1), ∀ xr : Fin n → ℝ,
      ContinuousOn (fun t => df (i.insertNth t xr) i) (Icc (a i) (b i))) :
    Real.sqrt
        (∫ x : Fin (n + 1) → ℝ,
          (f x - rectangularBoxMean a b f) ^ 2
          ∂rectangularBoxMeasure a b) ≤
      Real.sqrt (n + 1 : ℝ) * C *
        Real.sqrt
          (∑ i : Fin (n + 1),
            ∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2
              ∂rectangularBoxMeasure a b) := by
  let G : ℝ :=
    ∑ i : Fin (n + 1),
      ∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2
        ∂rectangularBoxMeasure a b
  have hEi0 : ∀ i : Fin (n + 1),
      0 ≤ ∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2
        ∂rectangularBoxMeasure a b := by
    intro i
    apply integral_nonneg_of_ae
    exact Filter.Eventually.of_forall fun x => sq_nonneg _
  have hG0 : 0 ≤ G := by
    dsimp [G]
    exact Finset.sum_nonneg fun i hi => hEi0 i
  have hp := rectangularBoxPoincareL2
    hside hC hSideBound f df hfLp hDiffInt hStepInt hDerivInt
    hFiberDeriv hFiberCont hFiberDCont
  have hN0 : 0 ≤ (n + 1 : ℝ) := by positivity
  have hsqN : (Real.sqrt (n + 1 : ℝ)) ^ 2 = (n + 1 : ℝ) :=
    Real.sq_sqrt hN0
  have hsqG : (Real.sqrt G) ^ 2 = G := Real.sq_sqrt hG0
  rw [Real.sqrt_le_iff]
  constructor
  · positivity
  · calc
      (∫ x : Fin (n + 1) → ℝ,
          (f x - rectangularBoxMean a b f) ^ 2
          ∂rectangularBoxMeasure a b) ≤
          (n + 1 : ℝ) * C ^ 2 * G := by
            simpa [G] using hp
      _ = (Real.sqrt (n + 1 : ℝ)) ^ 2 * C ^ 2 *
          (Real.sqrt G) ^ 2 := by rw [hsqN, hsqG]
      _ = (Real.sqrt (n + 1 : ℝ) * C * Real.sqrt G) ^ 2 := by ring

end AMLStabilization

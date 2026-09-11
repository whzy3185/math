import Mathlib
import AMLStabilization.FullBoxPoincareCore
import AMLStabilization.BoxProductMeasureCore

open Set MeasureTheory

namespace AMLStabilization

/--
Cell-energy form of the fully assembled rectangular-box Poincare inequality.

The geometric theorem is rewritten from `rectangularBoxMeasure` to the usual
set integral on `Icc a b`, the coordinate-energy sum is moved under the
integral, and the effective constant is exposed as `sqrt (n+1) * C`.
-/
theorem rectangularBoxPoincare_cellEnergyForm
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    (hside : ∀ j, a j < b j)
    {C ubar : ℝ}
    (hC : 0 ≤ C)
    (hSideBound : ∀ j, b j - a j ≤ C)
    (f : (Fin (n + 1) → ℝ) → ℝ)
    (df : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (hmean : rectangularBoxMean a b f = ubar)
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
    (∫ x in Icc a b, (f x - ubar) ^ 2) ≤
      (Real.sqrt (n + 1 : ℝ) * C) ^ 2 *
        (Real.sqrt (∫ x in Icc a b,
          ∑ i : Fin (n + 1), (df x i) ^ 2)) ^ 2 := by
  have hp := rectangularBoxPoincareL2
    hside hC hSideBound f df hfLp hDiffInt hStepInt hDerivInt
    hFiberDeriv hFiberCont hFiberDCont
  rw [hmean] at hp
  have hmu : rectangularBoxMeasure a b = volume.restrict (Icc a b) := by
    exact (volumeRestrictIcc_eq_pi_restrict a b).symm
  rw [hmu] at hp
  have hsumEq :
      (∑ i : Fin (n + 1),
        ∫ x in Icc a b, (df x i) ^ 2) =
      ∫ x in Icc a b, ∑ i : Fin (n + 1), (df x i) ^ 2 := by
    symm
    have hfin := MeasureTheory.integral_finsetSum
      (μ := volume.restrict (Icc a b))
      Finset.univ
      (f := fun i x => (df x i) ^ 2)
      (fun i hi => by
        have hint := hDerivInt i
        rw [hmu] at hint
        exact hint)
    simpa using hfin
  rw [hsumEq] at hp
  let G : ℝ := ∫ x in Icc a b, ∑ i : Fin (n + 1), (df x i) ^ 2
  have hG0 : 0 ≤ G := by
    dsimp [G]
    apply integral_nonneg
    intro x
    exact Finset.sum_nonneg fun i hi => sq_nonneg _
  have hN0 : 0 ≤ (n + 1 : ℝ) := by positivity
  have hp' :
      (∫ x in Icc a b, (f x - ubar) ^ 2) ≤
        (n + 1 : ℝ) * C ^ 2 * G := by
    simpa [G] using hp
  calc
    (∫ x in Icc a b, (f x - ubar) ^ 2) ≤
        (n + 1 : ℝ) * C ^ 2 * G := hp'
    _ = (Real.sqrt (n + 1 : ℝ) * C) ^ 2 * (Real.sqrt G) ^ 2 := by
      rw [mul_pow, Real.sq_sqrt hN0, Real.sq_sqrt hG0]
    _ = (Real.sqrt (n + 1 : ℝ) * C) ^ 2 *
        (Real.sqrt (∫ x in Icc a b,
          ∑ i : Fin (n + 1), (df x i) ^ 2)) ^ 2 := by
      rfl

end AMLStabilization

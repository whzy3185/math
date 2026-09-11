import Mathlib
import AMLStabilization.IntervalPairPoincareCore
import AMLStabilization.IntegratedCoordinateTelescopingCore
import AMLStabilization.HybridFiberCore
import AMLStabilization.PiCoordinateFubiniCore
import AMLStabilization.RestHybridMeasureCore

open Set MeasureTheory Real intervalIntegral

namespace AMLStabilization

/-- One-coordinate estimate for the hybrid-path proof of Poincare on a box.
The chosen hybrid increment is controlled by the squared derivative in that
coordinate.  All Fubini and unused-copy mass factors are discharged internally;
the only analytic inputs are the natural global integrability and fiber `C¹`
hypotheses. -/
theorem boxHybridCoordinateIncrement_sq_le
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    (hside : ∀ j, a j < b j)
    (f : (Fin (n + 1) → ℝ) → ℝ)
    (df : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (i : Fin (n + 1))
    (hStepInt : Integrable
      (fun z : Fin (n + 1) → ℝ × ℝ =>
        (pairedCoordinateIncrement f z i.val) ^ 2)
      (Measure.pi (fun j =>
        (volume.restrict (Icc (a j) (b j))).prod
          (volume.restrict (Icc (a j) (b j))))))
    (hDerivInt : Integrable
      (fun x : Fin (n + 1) → ℝ => (df x i) ^ 2)
      (Measure.pi (fun j => volume.restrict (Icc (a j) (b j)))))
    (hFiberDeriv : ∀ xr : Fin n → ℝ, ∀ t ∈ Icc (a i) (b i),
      HasDerivAt (fun s => f (i.insertNth s xr))
        (df (i.insertNth t xr) i) t)
    (hFiberCont : ∀ xr : Fin n → ℝ,
      ContinuousOn (fun t => f (i.insertNth t xr)) (Icc (a i) (b i)))
    (hFiberDCont : ∀ xr : Fin n → ℝ,
      ContinuousOn (fun t => df (i.insertNth t xr) i) (Icc (a i) (b i))) :
    (∫ z : Fin (n + 1) → ℝ × ℝ,
        (pairedCoordinateIncrement f z i.val) ^ 2
        ∂Measure.pi (fun j =>
          (volume.restrict (Icc (a j) (b j))).prod
            (volume.restrict (Icc (a j) (b j))))) ≤
      2 * (b i - a i) ^ 3 *
        (∏ j : Fin n,
          (volume.restrict
            (Icc (a (i.succAbove j)) (b (i.succAbove j))) Set.univ)).toReal *
        (∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2
          ∂Measure.pi (fun j => volume.restrict (Icc (a j) (b j)))) := by
  let μ : Fin (n + 1) → Measure ℝ :=
    fun j => volume.restrict (Icc (a j) (b j))
  let μpair : Fin (n + 1) → Measure (ℝ × ℝ) :=
    fun j => (μ j).prod (μ j)
  let μrest : Fin n → Measure ℝ := fun j => μ (i.succAbove j)
  let μpairRest : Fin n → Measure (ℝ × ℝ) :=
    fun j => (μrest j).prod (μrest j)
  let G : (Fin n → ℝ) → ℝ := fun xr =>
    ∫ t : ℝ, (df (i.insertNth t xr) i) ^ 2 ∂μ i
  have hStepOuter : Integrable
      (fun zr : Fin n → ℝ × ℝ =>
        ∫ p : ℝ × ℝ,
          (pairedCoordinateIncrement f (i.insertNth p zr) i.val) ^ 2 ∂μpair i)
      (Measure.pi μpairRest) := by
    simpa [μpairRest, μpair, μrest] using
      (integrable_integral_pi_split_coordinate_symm
        μpair i
        (fun z : Fin (n + 1) → ℝ × ℝ =>
          (pairedCoordinateIncrement f z i.val) ^ 2) hStepInt)
  have hGInt : Integrable G (Measure.pi μrest) := by
    simpa [G, μrest, μ] using
      (integrable_integral_pi_split_coordinate_symm
        μ i (fun x : Fin (n + 1) → ℝ => (df x i) ^ 2) hDerivInt)
  have hGPairInt : Integrable
      (fun zr : Fin n → ℝ × ℝ => G (pairedRestHybrid i zr))
      (Measure.pi μpairRest) := by
    simpa [μpairRest] using
      (Integrable.comp_pairedRestHybrid i μrest hGInt)
  have hGScaledInt : Integrable
      (fun zr : Fin n → ℝ × ℝ =>
        (2 * (b i - a i) ^ 3) * G (pairedRestHybrid i zr))
      (Measure.pi μpairRest) := hGPairInt.const_mul _
  have hFiber : ∀ zr : Fin n → ℝ × ℝ,
      (∫ p : ℝ × ℝ,
          (pairedCoordinateIncrement f (i.insertNth p zr) i.val) ^ 2 ∂μpair i) ≤
        2 * (b i - a i) ^ 3 * G (pairedRestHybrid i zr) := by
    intro zr
    have hp := intervalPairDifferenceL2
      (hside i)
      (f := fun t => f (i.insertNth t (pairedRestHybrid i zr)))
      (f' := fun t => df (i.insertNth t (pairedRestHybrid i zr)) i)
      (hFiberDeriv (pairedRestHybrid i zr))
      (hFiberCont (pairedRestHybrid i zr))
      (hFiberDCont (pairedRestHybrid i zr))
    dsimp only at hp
    have hmu : μ i = volume.restrict (Icc (a i) (b i)) := rfl
    have hinc : ∀ p : ℝ × ℝ,
        pairedCoordinateIncrement f (i.insertNth p zr) i.val =
          f (i.insertNth p.1 (pairedRestHybrid i zr)) -
            f (i.insertNth p.2 (pairedRestHybrid i zr)) := by
      intro p
      exact pairedCoordinateIncrement_insertNth f i p zr
    have hGset :
        G (pairedRestHybrid i zr) =
          ∫ t in a i..b i,
            |df (i.insertNth t (pairedRestHybrid i zr)) i| ^ 2 := by
      dsimp [G, μ, hmu]
      change (∫ t in Icc (a i) (b i),
          (df (i.insertNth t (pairedRestHybrid i zr)) i) ^ 2) = _
      rw [MeasureTheory.integral_Icc_eq_integral_Ioc,
        ← intervalIntegral.integral_of_le (hside i).le]
      apply intervalIntegral.integral_congr
      intro t ht
      exact (sq_abs _).symm
    simpa [μpair, hmu, hinc, hGset] using hp
  have hsplit := integral_pi_split_coordinate_symm
    μpair i
    (fun z : Fin (n + 1) → ℝ × ℝ =>
      (pairedCoordinateIncrement f z i.val) ^ 2) hStepInt
  have hmono :
      (∫ zr : Fin n → ℝ × ℝ,
        ∫ p : ℝ × ℝ,
          (pairedCoordinateIncrement f (i.insertNth p zr) i.val) ^ 2 ∂μpair i
        ∂Measure.pi μpairRest) ≤
      ∫ zr : Fin n → ℝ × ℝ,
        (2 * (b i - a i) ^ 3) * G (pairedRestHybrid i zr)
        ∂Measure.pi μpairRest := by
    apply integral_mono_ae hStepOuter hGScaledInt
    exact Filter.Eventually.of_forall hFiber
  have htransport := integral_pairedRestHybrid_of_integrable i μrest G hGInt
  have hGfull := integral_pi_split_coordinate_symm
    μ i (fun x : Fin (n + 1) → ℝ => (df x i) ^ 2) hDerivInt
  calc
    (∫ z : Fin (n + 1) → ℝ × ℝ,
        (pairedCoordinateIncrement f z i.val) ^ 2 ∂Measure.pi μpair) =
      ∫ zr : Fin n → ℝ × ℝ,
        ∫ p : ℝ × ℝ,
          (pairedCoordinateIncrement f (i.insertNth p zr) i.val) ^ 2 ∂μpair i
        ∂Measure.pi μpairRest := by
          simpa [μpairRest, μrest] using hsplit
    _ ≤ ∫ zr : Fin n → ℝ × ℝ,
        (2 * (b i - a i) ^ 3) * G (pairedRestHybrid i zr)
        ∂Measure.pi μpairRest := hmono
    _ = (2 * (b i - a i) ^ 3) *
        ∫ zr : Fin n → ℝ × ℝ, G (pairedRestHybrid i zr)
          ∂Measure.pi μpairRest := by rw [MeasureTheory.integral_const_mul]
    _ = (2 * (b i - a i) ^ 3) *
        ((∏ j, μrest j Set.univ).toReal *
          ∫ xr : Fin n → ℝ, G xr ∂Measure.pi μrest) := by
          rw [htransport]
    _ = (2 * (b i - a i) ^ 3) *
        ((∏ j, μrest j Set.univ).toReal *
          ∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂Measure.pi μ) := by
          rw [← hGfull]
    _ = 2 * (b i - a i) ^ 3 *
        (∏ j, μrest j Set.univ).toReal *
        (∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂Measure.pi μ) := by ring
    _ = 2 * (b i - a i) ^ 3 *
        (∏ j : Fin n,
          (volume.restrict
            (Icc (a (i.succAbove j)) (b (i.succAbove j))) Set.univ)).toReal *
        (∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2
          ∂Measure.pi (fun j => volume.restrict (Icc (a j) (b j)))) := by
          rfl

end AMLStabilization

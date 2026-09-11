import Mathlib
import AMLStabilization.BoxProductMeasureCore

open Set MeasureTheory Real

namespace AMLStabilization

/-- The unused-coordinate mass factor in the hybrid proof is exactly the
product of the remaining side lengths. -/
theorem boxRestMass_toReal_eq_prod_side
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    (hside : ∀ j, a j < b j) (i : Fin (n + 1)) :
    (∏ j : Fin n,
      (volume.restrict
        (Icc (a (i.succAbove j)) (b (i.succAbove j))) Set.univ)).toReal =
      ∏ j : Fin n, (b (i.succAbove j) - a (i.succAbove j)) := by
  rw [ENNReal.toReal_prod]
  apply Finset.prod_congr rfl
  intro j hj
  rw [Measure.restrict_apply_univ]
  simpa [Measure.real] using
    (Real.volume_real_Icc_of_le (hside (i.succAbove j)).le)

/-- The integral of one over the product representation of a nondegenerate
rectangular box is the product of its side lengths. -/
theorem integralOne_piBox_eq_prod_side
    {ι : Type*} [Fintype ι] {a b : ι → ℝ}
    (hside : ∀ j, a j < b j) :
    (∫ _ : ι → ℝ, (1 : ℝ)
      ∂Measure.pi (fun j => volume.restrict (Icc (a j) (b j)))) =
      ∏ j, (b j - a j) := by
  rw [← volumeRestrictIcc_eq_pi_restrict a b]
  rw [MeasureTheory.integral_const]
  simp only [MeasurableSet.univ, measureReal_restrict_apply, Set.univ_inter,
    smul_eq_mul, mul_one]
  exact boxVolumeReal_eq_prod_side (fun j => (hside j).le)

/-- In the one-coordinate hybrid estimate, the cubic side-length factor times
the unused-copy mass is the full box volume times the squared side length. -/
theorem boxSideCube_mul_restMass_eq_volume_mul_sideSq
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    (hside : ∀ j, a j < b j) (i : Fin (n + 1)) :
    (b i - a i) ^ 3 *
        (∏ j : Fin n,
          (volume.restrict
            (Icc (a (i.succAbove j)) (b (i.succAbove j))) Set.univ)).toReal =
      (∏ j : Fin (n + 1), (b j - a j)) * (b i - a i) ^ 2 := by
  rw [boxRestMass_toReal_eq_prod_side hside i]
  rw [Fin.prod_univ_succAbove (fun j => b j - a j) i]
  ring

end AMLStabilization

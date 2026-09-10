import Mathlib

open Set MeasureTheory

namespace AMLStabilization

/-- Lebesgue volume restricted to a rectangular box is exactly the finite
product of the coordinatewise restricted Lebesgue measures. -/
theorem volumeRestrictIcc_eq_pi_restrict
    {ι : Type*} [Fintype ι]
    (a b : ι → ℝ) :
    volume.restrict (Icc a b) =
      Measure.pi (fun i => volume.restrict (Icc (a i) (b i))) := by
  rw [← Set.pi_univ_Icc, volume_pi, Measure.restrict_pi_pi]

/-- The real volume of a rectangular box is the product of its side lengths
when the lower corner is coordinatewise below the upper corner. -/
theorem boxVolumeReal_eq_prod_side
    {ι : Type*} [Fintype ι]
    {a b : ι → ℝ} (hle : a ≤ b) :
    volume.real (Icc a b) = ∏ i, (b i - a i) := by
  simpa [Measure.real] using Real.volume_Icc_pi_toReal hle

/-- The real mass of one coordinate interval is its length. -/
theorem intervalVolumeReal_eq_length {a b : ℝ} (hab : a ≤ b) :
    volume.real (Icc a b) = b - a :=
  Real.volume_real_Icc_of_le hab

end AMLStabilization

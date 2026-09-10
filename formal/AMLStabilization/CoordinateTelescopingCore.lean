import Mathlib

namespace AMLStabilization

/-- Cauchy--Schwarz telescoping bound for a finite real sequence. -/
theorem sequenceTelescoping_sq_le
    (g : ℕ → ℝ) (n : ℕ) :
    (g 0 - g n) ^ 2 ≤
      (n : ℝ) * ∑ k ∈ Finset.range n, (g k - g (k + 1)) ^ 2 := by
  have htel :
      (∑ k ∈ Finset.range n, (g k - g (k + 1))) = g 0 - g n := by
    calc
      (∑ k ∈ Finset.range n, (g k - g (k + 1))) =
          -(∑ k ∈ Finset.range n, (g (k + 1) - g k)) := by
            rw [← Finset.sum_neg_distrib]
            apply Finset.sum_congr rfl
            intro k hk
            ring
      _ = -(g n - g 0) := by rw [Finset.sum_range_sub]
      _ = g 0 - g n := by ring
  have hcs := sq_sum_le_card_mul_sum_sq
    (s := Finset.range n) (f := fun k => g k - g (k + 1))
  rw [Finset.card_range] at hcs
  rw [htel] at hcs
  exact hcs

/-- Hybrid point between two product points: coordinates with index `< k` are
taken from `y`, while the remaining coordinates are taken from `x`. -/
noncomputable def coordinateHybrid
    {α : Type*} {n : ℕ} (x y : Fin n → α) (k : ℕ) : Fin n → α :=
  fun i => if (i : ℕ) < k then y i else x i

@[simp]
theorem coordinateHybrid_zero
    {α : Type*} {n : ℕ} (x y : Fin n → α) :
    coordinateHybrid x y 0 = x := by
  funext i
  simp [coordinateHybrid]

@[simp]
theorem coordinateHybrid_full
    {α : Type*} {n : ℕ} (x y : Fin n → α) :
    coordinateHybrid x y n = y := by
  funext i
  simp [coordinateHybrid, i.isLt]

/-- Pointwise finite-coordinate telescoping estimate.  No measure theory is
used here; this is the Cauchy--Schwarz part of the product Poincare argument. -/
theorem coordinateTelescoping_sq_le
    {α : Type*} {n : ℕ}
    (f : (Fin n → α) → ℝ) (x y : Fin n → α) :
    (f x - f y) ^ 2 ≤
      (n : ℝ) * ∑ k ∈ Finset.range n,
        (f (coordinateHybrid x y k) -
          f (coordinateHybrid x y (k + 1))) ^ 2 := by
  simpa using
    (sequenceTelescoping_sq_le
      (g := fun k => f (coordinateHybrid x y k)) n)

end AMLStabilization

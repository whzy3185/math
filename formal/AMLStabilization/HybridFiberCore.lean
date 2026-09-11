import Mathlib
import AMLStabilization.IntegratedCoordinateTelescopingCore

namespace AMLStabilization

/-- Remaining coordinates of a paired sample, already chosen according to the
hybrid path at the distinguished coordinate `i`: lower coordinates use the
second copy, higher coordinates use the first copy. -/
noncomputable def pairedRestHybrid
    {α : Type*} {n : ℕ}
    (i : Fin (n + 1)) (zr : Fin n → α × α) : Fin n → α :=
  fun j => if (i.succAbove j : Fin (n + 1)).val < i.val then
    (zr j).2 else (zr j).1

private theorem coordinateHybrid_insertNth_first
    {α : Type*} {n : ℕ}
    (i : Fin (n + 1)) (p : α × α) (zr : Fin n → α × α) :
    coordinateHybrid
        (fun j => (((i.insertNth p zr : Fin (n + 1) → α × α) j)).1)
        (fun j => (((i.insertNth p zr : Fin (n + 1) → α × α) j)).2) i.val =
      i.insertNth p.1 (pairedRestHybrid i zr) := by
  rw [funext_iff, i.forall_iff_succAbove]
  constructor
  · simp [coordinateHybrid]
  · intro j
    simp only [i.insertNth_apply_succAbove]
    have hne : (i.succAbove j : Fin (n + 1)).val ≠ i.val := by
      intro h
      exact i.succAbove_ne j (Fin.ext h)
    by_cases hlt : (i.succAbove j : Fin (n + 1)).val < i.val
    · simp [coordinateHybrid, pairedRestHybrid, hlt]
    · simp [coordinateHybrid, pairedRestHybrid, hlt]

private theorem coordinateHybrid_insertNth_second
    {α : Type*} {n : ℕ}
    (i : Fin (n + 1)) (p : α × α) (zr : Fin n → α × α) :
    coordinateHybrid
        (fun j => (((i.insertNth p zr : Fin (n + 1) → α × α) j)).1)
        (fun j => (((i.insertNth p zr : Fin (n + 1) → α × α) j)).2) (i.val + 1) =
      i.insertNth p.2 (pairedRestHybrid i zr) := by
  rw [funext_iff, i.forall_iff_succAbove]
  constructor
  · simp [coordinateHybrid]
  · intro j
    simp only [i.insertNth_apply_succAbove]
    have hne : (i.succAbove j : Fin (n + 1)).val ≠ i.val := by
      intro h
      exact i.succAbove_ne j (Fin.ext h)
    by_cases hlt : (i.succAbove j : Fin (n + 1)).val < i.val
    · have hlt' : (i.succAbove j : Fin (n + 1)).val < i.val + 1 := by omega
      simp [coordinateHybrid, pairedRestHybrid, hlt, hlt']
    · have hnot : ¬(i.succAbove j : Fin (n + 1)).val < i.val + 1 := by omega
      simp [coordinateHybrid, pairedRestHybrid, hlt, hnot]

/-- The `i.val`-th hybrid increment changes exactly coordinate `i`. -/
theorem pairedCoordinateIncrement_insertNth
    {α : Type*} {n : ℕ}
    (f : (Fin (n + 1) → α) → ℝ)
    (i : Fin (n + 1)) (p : α × α) (zr : Fin n → α × α) :
    pairedCoordinateIncrement f (i.insertNth p zr : Fin (n + 1) → α × α) i.val =
      f (i.insertNth p.1 (pairedRestHybrid i zr)) -
        f (i.insertNth p.2 (pairedRestHybrid i zr)) := by
  rw [pairedCoordinateIncrement,
    coordinateHybrid_insertNth_first i p zr,
    coordinateHybrid_insertNth_second i p zr]

end AMLStabilization

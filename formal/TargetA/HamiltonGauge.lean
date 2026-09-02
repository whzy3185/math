import Mathlib

namespace TargetA

/-!
The forward-edge part of the finite Hamilton-gauge realization. A periodic
lift has coefficient one on a step-one edge and tau(i) on a step-two edge;
crossing the cut from n - 1 back to 0 multiplies the coefficient by the
holonomy alpha. The reverse entries are their symmetric counterparts.
-/

def periodEightValue (tau : Fin 8 → ℤ) (i : ℕ) : ℤ :=
  tau ⟨i % 8, Nat.mod_lt _ (by omega)⟩

def forwardStepOne (n : ℕ) (alpha : ℤ) (i : ℕ) : ℤ :=
  if i + 1 < n then 1 else alpha

def forwardStepTwo (n : ℕ) (alpha : ℤ) (tau : ℕ → ℤ) (i : ℕ) : ℤ :=
  if i + 2 < n then tau i else alpha * tau i

def cyclicNext {n : ℕ} (i : Fin n) (step : ℕ) : Fin n :=
  ⟨(i.val + step) % n, Nat.mod_lt _ (Fin.pos i)⟩

def hamiltonGaugeMatrix {n : ℕ} (alpha : ℤ) (tau : ℕ → ℤ) :
    Matrix (Fin n) (Fin n) ℤ :=
  fun i j =>
    (if j = cyclicNext i 1 then forwardStepOne n alpha i.val else 0) +
    (if i = cyclicNext j 1 then forwardStepOne n alpha j.val else 0) +
    (if j = cyclicNext i 2 then forwardStepTwo n alpha tau i.val else 0) +
    (if i = cyclicNext j 2 then forwardStepTwo n alpha tau j.val else 0)

theorem hamilton_gauge_matrix_symmetric {n : ℕ} (alpha : ℤ) (tau : ℕ → ℤ) :
    Matrix.transpose (hamiltonGaugeMatrix (n := n) alpha tau) =
      hamiltonGaugeMatrix (n := n) alpha tau := by
  ext i j
  simp only [Matrix.transpose_apply, hamiltonGaugeMatrix]
  ac_rfl

theorem cyclic_next_one_ne_self {n : ℕ} (hn : 2 ≤ n) (i : Fin n) :
    cyclicNext i 1 ≠ i := by
  intro h
  have hval : (i.val + 1) % n = i.val := by
    exact Fin.ext_iff.mp h
  by_cases hcut : i.val + 1 < n
  · rw [Nat.mod_eq_of_lt hcut] at hval
    omega
  · have hseam : i.val + 1 = n := by omega
    rw [hseam, Nat.mod_self] at hval
    omega

theorem cyclic_next_two_ne_self {n : ℕ} (hn : 3 ≤ n) (i : Fin n) :
    cyclicNext i 2 ≠ i := by
  intro h
  have hval : (i.val + 2) % n = i.val := by
    exact Fin.ext_iff.mp h
  by_cases hcut : i.val + 2 < n
  · rw [Nat.mod_eq_of_lt hcut] at hval
    omega
  · have hbound : n ≤ i.val + 2 := by omega
    have hupper : i.val + 2 < 2 * n := by omega
    have hmod : (i.val + 2) % n = i.val + 2 - n := by
      rw [Nat.mod_eq_sub_mod hbound]
      apply Nat.mod_eq_of_lt
      omega
    rw [hmod] at hval
    omega

theorem cyclic_next_one_then_one {n : ℕ} (i : Fin n) :
    cyclicNext (cyclicNext i 1) 1 = cyclicNext i 2 := by
  apply Fin.ext
  simp only [cyclicNext, Fin.val_mk]
  simp [Nat.add_assoc, Nat.mod_add_mod]

theorem cyclic_next_one_ne_two {n : ℕ} (hn : 2 ≤ n) (i : Fin n) :
    cyclicNext i 1 ≠ cyclicNext i 2 := by
  intro h
  have hself : cyclicNext (cyclicNext i 1) 1 = cyclicNext i 1 := by
    rw [cyclic_next_one_then_one]
    exact h.symm
  exact cyclic_next_one_ne_self hn (cyclicNext i 1) hself

def IsSign (x : ℤ) : Prop := x = 1 ∨ x = -1

theorem period_eight_value_is_sign (tau : Fin 8 → ℤ)
    (htau : ∀ r, IsSign (tau r)) (i : ℕ) :
    IsSign (periodEightValue tau i) := by
  exact htau ⟨i % 8, Nat.mod_lt _ (by omega)⟩

theorem forward_step_one_is_sign (n : ℕ) (alpha : ℤ) (halpha : IsSign alpha)
    (i : ℕ) :
    IsSign (forwardStepOne n alpha i) := by
  simp only [forwardStepOne]
  split <;> simp_all [IsSign]

theorem forward_step_two_is_sign (n : ℕ) (alpha : ℤ) (tau : ℕ → ℤ)
    (halpha : IsSign alpha) (htau : ∀ i, IsSign (tau i)) (i : ℕ) :
    IsSign (forwardStepTwo n alpha tau i) := by
  simp only [forwardStepTwo]
  split
  · exact htau i
  · rcases halpha with rfl | rfl
    · simpa using htau i
    · rcases htau i with h | h <;> simp [h, IsSign]

theorem period_eight_repeat (tau : Fin 8 → ℤ) (i L : ℕ) :
    periodEightValue tau (i + 8 * L) = periodEightValue tau i := by
  simp [periodEightValue, Nat.add_mul_mod_self_left]

theorem step_one_cut_rule {n i : ℕ} :
    forwardStepOne n (-1) i = if i + 1 < n then 1 else -1 := by
  rfl

theorem step_two_cut_rule {n i : ℕ} (tau : ℕ → ℤ) :
    forwardStepTwo n (-1) tau i = if i + 2 < n then tau i else -tau i := by
  simp [forwardStepTwo]

theorem step_one_no_cut {n i : ℕ} (h : i + 1 < n) (alpha : ℤ) :
    forwardStepOne n alpha i = 1 := by
  simp [forwardStepOne, h]

theorem step_one_cut {n i : ℕ} (h : ¬ i + 1 < n) (alpha : ℤ) :
    forwardStepOne n alpha i = alpha := by
  simp [forwardStepOne, h]

theorem step_two_no_cut {n i : ℕ} (h : i + 2 < n) (alpha : ℤ) (tau : ℕ → ℤ) :
    forwardStepTwo n alpha tau i = tau i := by
  simp [forwardStepTwo, h]

theorem step_two_cut {n i : ℕ} (h : ¬ i + 2 < n)
    (alpha : ℤ) (tau : ℕ → ℤ) :
    forwardStepTwo n alpha tau i = alpha * tau i := by
  simp [forwardStepTwo, h]

theorem period_eight_fits_multiple {L : ℕ} :
    8 ∣ 8 * L := by
  exact ⟨L, by ring⟩

end TargetA

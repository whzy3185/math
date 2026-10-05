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

def cyclicPrev {n : ℕ} (i : Fin n) : Fin n :=
  cyclicNext i (n - 1)

theorem cyclic_next_prev {n : ℕ} (hn : 0 < n) (i : Fin n) :
    cyclicNext (cyclicPrev i) 1 = i := by
  by_cases hunit : n = 1
  · subst n
    fin_cases i
    rfl
  have hn2 : 1 < n := by omega
  apply Fin.ext
  change (((i.val + (n - 1)) % n) + 1) % n = i.val
  have hone : 1 % n = 1 := Nat.mod_eq_of_lt hn2
  rw [← hone, ← Nat.add_mod]
  simp only [Nat.mod_eq_of_lt (by omega)]
  have hsum : i.val + (n - 1) + 1 = i.val + n := by omega
  rw [hsum, Nat.add_mod_right, Nat.mod_eq_of_lt i.isLt]

theorem cyclic_prev_next {n : ℕ} (hn : 0 < n) (i : Fin n) :
    cyclicPrev (cyclicNext i 1) = i := by
  by_cases hunit : n = 1
  · subst n
    fin_cases i
    rfl
  apply Fin.ext
  change (((i.val + 1) % n + (n - 1)) % n) = i.val
  by_cases hinterior : i.val + 1 < n
  · rw [Nat.mod_eq_of_lt hinterior]
    have hsum : i.val + 1 + (n - 1) = i.val + n := by omega
    rw [hsum, Nat.add_mod_right, Nat.mod_eq_of_lt i.isLt]
  · have hseam : i.val + 1 = n := by omega
    rw [hseam, Nat.mod_self]
    have hi : i.val = n - 1 := by omega
    rw [hi, Nat.mod_eq_of_lt (by omega)]
    omega

theorem cyclic_next_eq_iff {n : ℕ} (hn : 0 < n) (i j : Fin n) :
    cyclicNext i 1 = j ↔ i = cyclicPrev j := by
  constructor
  · intro h
    rw [← h, cyclic_prev_next hn]
  · intro h
    rw [h, cyclic_next_prev hn]

def hamiltonGaugeMatrix {n : ℕ} (alpha : ℤ) (tau : ℕ → ℤ) :
    Matrix (Fin n) (Fin n) ℤ :=
  fun i j =>
    (if j = cyclicNext i 1 then forwardStepOne n alpha i.val else 0) +
    (if i = cyclicNext j 1 then forwardStepOne n alpha j.val else 0) +
    (if j = cyclicNext i 2 then forwardStepTwo n alpha tau i.val else 0) +
    (if i = cyclicNext j 2 then forwardStepTwo n alpha tau j.val else 0)

def hamiltonGaugeForwardMatrix {n : ℕ} (alpha : ℤ) (tau : ℕ → ℤ) :
    Matrix (Fin n) (Fin n) ℤ :=
  fun i j =>
    (if j = cyclicNext i 1 then forwardStepOne n alpha i.val else 0) +
    (if j = cyclicNext i 2 then forwardStepTwo n alpha tau i.val else 0)

theorem hamilton_gauge_matrix_eq_forward_add_transpose {n : ℕ}
    (alpha : ℤ) (tau : ℕ → ℤ) :
    hamiltonGaugeMatrix (n := n) alpha tau =
      hamiltonGaugeForwardMatrix (n := n) alpha tau +
        Matrix.transpose (hamiltonGaugeForwardMatrix (n := n) alpha tau) := by
  ext i j
  simp only [hamiltonGaugeMatrix, hamiltonGaugeForwardMatrix,
    Matrix.add_apply, Matrix.transpose_apply]
  ac_rfl

theorem hamilton_gauge_forward_matrix_mulVec {n : ℕ}
    (alpha : ℤ) (tau : ℕ → ℤ) (x : Fin n → ℤ) (i : Fin n) :
    (hamiltonGaugeForwardMatrix (n := n) alpha tau).mulVec x i =
      forwardStepOne n alpha i.val * x (cyclicNext i 1) +
        forwardStepTwo n alpha tau i.val * x (cyclicNext i 2) := by
  simp only [hamiltonGaugeForwardMatrix, Matrix.mulVec, dotProduct]
  simp_rw [add_mul]
  rw [Finset.sum_add_distrib]
  simp

noncomputable def hamiltonGaugeForwardMatrixC {n : ℕ}
    (alpha : ℤ) (tau : ℕ → ℤ) : Matrix (Fin n) (Fin n) ℂ :=
  fun i j => (hamiltonGaugeForwardMatrix (n := n) alpha tau i j : ℂ)

theorem hamilton_gauge_forward_matrixC_mulVec {n : ℕ}
    (alpha : ℤ) (tau : ℕ → ℤ) (x : Fin n → ℂ) (i : Fin n) :
    (hamiltonGaugeForwardMatrixC (n := n) alpha tau).mulVec x i =
      (forwardStepOne n alpha i.val : ℂ) * x (cyclicNext i 1) +
        (forwardStepTwo n alpha tau i.val : ℂ) * x (cyclicNext i 2) := by
  simp only [hamiltonGaugeForwardMatrixC, hamiltonGaugeForwardMatrix,
    Matrix.mulVec, dotProduct, Int.cast_add, Int.cast_ite, Int.cast_zero]
  simp_rw [add_mul]
  rw [Finset.sum_add_distrib]
  simp

theorem hamilton_gauge_matrix_symmetric {n : ℕ} (alpha : ℤ) (tau : ℕ → ℤ) :
    Matrix.transpose (hamiltonGaugeMatrix (n := n) alpha tau) =
      hamiltonGaugeMatrix (n := n) alpha tau := by
  ext i j
  simp only [Matrix.transpose_apply, hamiltonGaugeMatrix]
  ac_rfl

/-!
The next two lemmas record the graph-theoretic content of the matrix
definition, independently of the values of the edge signs.  In particular,
no entry away from the four cyclic step-neighbours can be created by the
Hamilton gauge convention, and (once the two step sizes do not wrap onto the
base vertex) there is no diagonal entry.
-/

theorem hamilton_gauge_matrix_zero_of_not_neighbour {n : ℕ}
    (alpha : ℤ) (tau : ℕ → ℤ) (i j : Fin n)
    (hforwardOne : j ≠ cyclicNext i 1)
    (hbackwardOne : i ≠ cyclicNext j 1)
    (hforwardTwo : j ≠ cyclicNext i 2)
    (hbackwardTwo : i ≠ cyclicNext j 2) :
    hamiltonGaugeMatrix alpha tau i j = 0 := by
  simp [hamiltonGaugeMatrix, hforwardOne, hbackwardOne, hforwardTwo,
    hbackwardTwo]

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

theorem hamilton_gauge_matrix_diagonal_zero {n : ℕ} (hn : 3 ≤ n)
    (alpha : ℤ) (tau : ℕ → ℤ) (i : Fin n) :
    hamiltonGaugeMatrix alpha tau i i = 0 := by
  apply hamilton_gauge_matrix_zero_of_not_neighbour
  · exact (cyclic_next_one_ne_self (by omega) i).symm
  · exact (cyclic_next_one_ne_self (by omega) i).symm
  · exact (cyclic_next_two_ne_self hn i).symm
  · exact (cyclic_next_two_ne_self hn i).symm

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

theorem forward_step_one_periodic_holonomy (n i : ℕ) :
    forwardStepOne n 1 i = 1 := by
  simp [forwardStepOne]

theorem forward_step_two_periodic_holonomy (n i : ℕ) (tau : ℕ → ℤ) :
    forwardStepTwo n 1 tau i = tau i := by
  simp [forwardStepTwo]

theorem period_eight_repeat (tau : Fin 8 → ℤ) (i L : ℕ) :
    periodEightValue tau (i + 8 * L) = periodEightValue tau i := by
  simp [periodEightValue, Nat.add_mul_mod_self_left]

def period8TargetTau : Fin 8 → ℤ :=
  ![1, 1, -1, 1, -1, -1, 1, -1]

def period8TargetLift (i : ℕ) : ℤ :=
  periodEightValue period8TargetTau i

theorem period8_target_lift_cell_value (m : ℕ) (r : Fin 8) :
    period8TargetLift (8 * m + r.val) = period8TargetTau r := by
  simp [period8TargetLift, periodEightValue]
  congr 1
  apply Fin.ext
  change r.val % 8 = r.val
  exact Nat.mod_eq_of_lt r.isLt

theorem period8_target_tau_is_sign (r : Fin 8) :
    IsSign (period8TargetTau r) := by
  fin_cases r <;> simp [period8TargetTau, IsSign]

theorem period8_target_lift_is_sign (i : ℕ) :
    IsSign (period8TargetLift i) := by
  exact period_eight_value_is_sign period8TargetTau period8_target_tau_is_sign i

theorem period8_target_lift_periodic (i L : ℕ) :
    period8TargetLift (i + 8 * L) = period8TargetLift i := by
  exact period_eight_repeat period8TargetTau i L

def period8TargetMatrix (L : ℕ) (alpha : ℤ) :
    Matrix (Fin (8 * L)) (Fin (8 * L)) ℤ :=
  hamiltonGaugeMatrix alpha period8TargetLift

noncomputable def period8TargetMatrixC (L : ℕ) (alpha : ℤ) :
    Matrix (Fin (8 * L)) (Fin (8 * L)) ℂ :=
  fun i j => (period8TargetMatrix L alpha i j : ℂ)

theorem period8_target_step_two_is_sign (L : ℕ) (alpha : ℤ)
    (halpha : IsSign alpha) (i : ℕ) :
    IsSign (forwardStepTwo (8 * L) alpha period8TargetLift i) := by
  exact forward_step_two_is_sign (8 * L) alpha period8TargetLift halpha
    period8_target_lift_is_sign i

theorem period8_target_step_one_is_sign (L : ℕ) (alpha : ℤ)
    (halpha : IsSign alpha) (i : ℕ) :
    IsSign (forwardStepOne (8 * L) alpha i) := by
  exact forward_step_one_is_sign (8 * L) alpha halpha i

theorem period8_target_matrix_symmetric (L : ℕ) (alpha : ℤ) :
    Matrix.transpose (period8TargetMatrix L alpha) =
      period8TargetMatrix L alpha :=
  hamilton_gauge_matrix_symmetric alpha period8TargetLift

theorem period8_target_matrix_isHermitian (L : ℕ) (alpha : ℤ) :
    (period8TargetMatrixC L alpha).IsHermitian := by
  rw [Matrix.IsHermitian]
  ext i j
  have hsymm : period8TargetMatrix L alpha j i =
      period8TargetMatrix L alpha i j := by
    exact congrFun (congrFun (period8_target_matrix_symmetric L alpha) i) j
  simp [period8TargetMatrixC, Matrix.conjTranspose, hsymm]

theorem period8_target_matrix_diagonal_zero {L : ℕ} (hL : 0 < L)
    (alpha : ℤ) (i : Fin (8 * L)) :
    period8TargetMatrix L alpha i i = 0 := by
  apply hamilton_gauge_matrix_diagonal_zero
  omega

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

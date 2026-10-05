import TargetA.Period8AntiperiodicBridge

namespace TargetA

def period8DoubleLow (L : ℕ) (i : Fin (8 * L)) : Fin (8 * (2 * L)) :=
  ⟨i.val, by omega⟩

def period8DoubleHigh (L : ℕ) (i : Fin (8 * L)) : Fin (8 * (2 * L)) :=
  ⟨8 * L + i.val, by omega⟩

/-- The two consecutive halves of the periodic double cover. -/
def period8DoubleIndex (L : ℕ) :
    (Fin (8 * L) ⊕ Fin (8 * L)) ≃ Fin (8 * (2 * L)) where
  toFun := Sum.elim (period8DoubleLow L) (period8DoubleHigh L)
  invFun i := if hi : i.val < 8 * L then Sum.inl ⟨i.val, hi⟩
    else Sum.inr ⟨i.val - 8 * L, by omega⟩
  left_inv i := by
    cases i with
    | inl i => simp [period8DoubleLow, i.isLt]
    | inr i => simp [period8DoubleHigh, show ¬ (8 * L + i.val < 8 * L) by omega]
  right_inv i := by
    dsimp only
    split_ifs with hi
    · rfl
    · apply Fin.ext
      change 8 * L + (i.val - 8 * L) = i.val
      omega

/-- The explicit unnormalised antiperiodic lift `u ↦ [u,-u]`. -/
noncomputable def period8DoubleLift (L : ℕ) (u : Fin (8 * L) → ℂ) :
    Fin (8 * (2 * L)) → ℂ :=
  fun i => Sum.elim u (fun j => -u j) ((period8DoubleIndex L).symm i)

@[simp] theorem period8_double_lift_low (L : ℕ) (u : Fin (8 * L) → ℂ)
    (i : Fin (8 * L)) : period8DoubleLift L u (period8DoubleLow L i) = u i := by
  change Sum.elim u (fun j => -u j)
    ((period8DoubleIndex L).symm ((period8DoubleIndex L) (Sum.inl i))) = u i
  simp

@[simp] theorem period8_double_lift_high (L : ℕ) (u : Fin (8 * L) → ℂ)
    (i : Fin (8 * L)) : period8DoubleLift L u (period8DoubleHigh L i) = -u i := by
  change Sum.elim u (fun j => -u j)
    ((period8DoubleIndex L).symm ((period8DoubleIndex L) (Sum.inr i))) = -u i
  simp

theorem period8_double_lift_injective (L : ℕ) :
    Function.Injective (period8DoubleLift L) := by
  intro u v h
  funext i
  have he := congrFun h (period8DoubleLow L i)
  simpa using he

theorem period8_double_low_half_shift (L : ℕ) (hL : 0 < L)
    (i : Fin (8 * L)) :
    cyclicNext (period8DoubleLow L i) (8 * L) = period8DoubleHigh L i := by
  apply Fin.ext
  change (i.val + 8 * L) % (8 * (2 * L)) = 8 * L + i.val
  rw [Nat.mod_eq_of_lt (by omega)]
  omega

theorem period8_double_high_half_shift (L : ℕ) (hL : 0 < L)
    (i : Fin (8 * L)) :
    cyclicNext (period8DoubleHigh L i) (8 * L) = period8DoubleLow L i := by
  apply Fin.ext
  change (8 * L + i.val + 8 * L) % (8 * (2 * L)) = i.val
  rw [show 8 * L + i.val + 8 * L = i.val + 8 * (2 * L) by omega]
  simp [Nat.mod_eq_of_lt (by omega : i.val < 8 * (2 * L))]

theorem period8_double_lift_antiperiodic (L : ℕ) (hL : 0 < L)
    (u : Fin (8 * L) → ℂ) :
    ∀ i, period8DoubleLift L u (cyclicNext i (8 * L)) = -period8DoubleLift L u i := by
  intro i
  obtain ⟨j, rfl⟩ := (period8DoubleIndex L).surjective i
  cases j with
  | inl j =>
    change period8DoubleLift L u (cyclicNext (period8DoubleLow L j) (8 * L)) = _
    rw [period8_double_low_half_shift L hL]
    simp [period8DoubleIndex]
  | inr j =>
    change period8DoubleLift L u (cyclicNext (period8DoubleHigh L j) (8 * L)) = _
    rw [period8_double_high_half_shift L hL]
    simp [period8DoubleIndex]

/-- Simultaneously changing both half labels preserves a forward neighbour relation. -/
theorem period8_double_same_half_next (L : ℕ) (hL : 0 < L)
    (i j : Fin (8 * L)) (s : ℕ) (hs : s ≤ 2) :
    (period8DoubleHigh L j = cyclicNext (period8DoubleHigh L i) s) ↔
      (period8DoubleLow L j = cyclicNext (period8DoubleLow L i) s) := by
  simp only [Fin.ext_iff, period8DoubleHigh, period8DoubleLow, cyclicNext]
  by_cases hi : i.val + s < 8 * L
  · rw [Nat.mod_eq_of_lt (by omega : 8 * L + i.val + s < 8 * (2 * L))]
    rw [Nat.mod_eq_of_lt (by omega : i.val + s < 8 * (2 * L))]
    omega
  · rw [Nat.mod_eq_sub_mod (by omega : 8 * (2 * L) ≤ 8 * L + i.val + s)]
    rw [Nat.mod_eq_of_lt (by omega : 8 * L + i.val + s - 8 * (2 * L) < 8 * (2 * L))]
    rw [Nat.mod_eq_of_lt (by omega : i.val + s < 8 * (2 * L))]
    omega

/-- Exchanging the half labels reverses which seam crossing is used. -/
theorem period8_double_cross_half_next (L : ℕ) (hL : 0 < L)
    (i j : Fin (8 * L)) (s : ℕ) (hs : s ≤ 2) :
    (period8DoubleLow L j = cyclicNext (period8DoubleHigh L i) s) ↔
      (period8DoubleHigh L j = cyclicNext (period8DoubleLow L i) s) := by
  simp only [Fin.ext_iff, period8DoubleHigh, period8DoubleLow, cyclicNext]
  by_cases hi : i.val + s < 8 * L
  · rw [Nat.mod_eq_of_lt (by omega : 8 * L + i.val + s < 8 * (2 * L))]
    rw [Nat.mod_eq_of_lt (by omega : i.val + s < 8 * (2 * L))]
    omega
  · rw [Nat.mod_eq_sub_mod (by omega : 8 * (2 * L) ≤ 8 * L + i.val + s)]
    rw [Nat.mod_eq_of_lt (by omega : 8 * L + i.val + s - 8 * (2 * L) < 8 * (2 * L))]
    rw [Nat.mod_eq_of_lt (by omega : i.val + s < 8 * (2 * L))]
    omega

/-- A positive edge in the cover acquires exactly the cut sign in the negative sector. -/
theorem period8_double_signed_forward_entry (L : ℕ) (hL : 0 < L)
    (i j : Fin (8 * L)) (s : ℕ) (hs : s ≤ 2) (a : ℤ) :
    (if period8DoubleLow L j = cyclicNext (period8DoubleLow L i) s then a else 0) -
      (if period8DoubleHigh L j = cyclicNext (period8DoubleLow L i) s then a else 0) =
    (if j = cyclicNext i s then (if i.val + s < 8 * L then a else -a) else 0) := by
  simp only [Fin.ext_iff, period8DoubleLow, period8DoubleHigh, cyclicNext]
  rw [Nat.mod_eq_of_lt (by omega : i.val + s < 8 * (2 * L))]
  by_cases hi : i.val + s < 8 * L
  · rw [Nat.mod_eq_of_lt hi]
    simp only [hi, if_true]
    have hne : ¬ (8 * L + j.val = i.val + s) := by omega
    simp [hne]
  · rw [Nat.mod_eq_sub_mod (by omega : 8 * L ≤ i.val + s)]
    rw [Nat.mod_eq_of_lt (by omega : i.val + s - 8 * L < 8 * L)]
    simp only [hi, if_false]
    have hne : ¬ (j.val = i.val + s) := by omega
    simp only [hne, if_false, zero_sub]
    have he : 8 * L + j.val = i.val + s ↔ j.val = i.val + s - 8 * L := by omega
    simp only [he]
    split_ifs <;> ring

@[simp] theorem period8_double_low_lift (L : ℕ) (i : Fin (8 * L)) :
    period8TargetLift (period8DoubleLow L i).val = period8TargetLift i.val := rfl

@[simp] theorem period8_double_high_lift (L : ℕ) (i : Fin (8 * L)) :
    period8TargetLift (period8DoubleHigh L i).val = period8TargetLift i.val := by
  change period8TargetLift (8 * L + i.val) = period8TargetLift i.val
  rw [Nat.add_comm, period8_target_lift_periodic]

theorem period8_periodic_matrix_entry (M : ℕ) (i j : Fin (8 * M)) :
    period8TargetMatrix M 1 i j =
      (if j = cyclicNext i 1 then 1 else 0) +
      (if i = cyclicNext j 1 then 1 else 0) +
      (if j = cyclicNext i 2 then period8TargetLift i.val else 0) +
      (if i = cyclicNext j 2 then period8TargetLift j.val else 0) := by
  simp [period8TargetMatrix, hamiltonGaugeMatrix, forwardStepOne, forwardStepTwo]

theorem period8_double_matrix_same_blocks (L : ℕ) (hL : 0 < L)
    (i j : Fin (8 * L)) :
    period8TargetMatrix (2 * L) 1 (period8DoubleHigh L i) (period8DoubleHigh L j) =
      period8TargetMatrix (2 * L) 1 (period8DoubleLow L i) (period8DoubleLow L j) := by
  simp only [period8_periodic_matrix_entry, period8_double_high_lift, period8_double_low_lift,
    period8_double_same_half_next L hL i j 1 (by omega),
    period8_double_same_half_next L hL j i 1 (by omega),
    period8_double_same_half_next L hL i j 2 (by omega),
    period8_double_same_half_next L hL j i 2 (by omega)]

theorem period8_double_matrix_cross_blocks (L : ℕ) (hL : 0 < L)
    (i j : Fin (8 * L)) :
    period8TargetMatrix (2 * L) 1 (period8DoubleHigh L i) (period8DoubleLow L j) =
      period8TargetMatrix (2 * L) 1 (period8DoubleLow L i) (period8DoubleHigh L j) := by
  simp only [period8_periodic_matrix_entry, period8_double_high_lift, period8_double_low_lift,
    period8_double_cross_half_next L hL i j 1 (by omega),
    period8_double_cross_half_next L hL j i 1 (by omega),
    period8_double_cross_half_next L hL i j 2 (by omega),
    period8_double_cross_half_next L hL j i 2 (by omega)]

/-- Exact graph-entry identity, including all three seam edges. -/
theorem period8_double_matrix_difference (L : ℕ) (hL : 0 < L)
    (i j : Fin (8 * L)) :
    period8TargetMatrix (2 * L) 1 (period8DoubleLow L i) (period8DoubleLow L j) -
      period8TargetMatrix (2 * L) 1 (period8DoubleLow L i) (period8DoubleHigh L j) =
        period8TargetMatrix L (-1) i j := by
  have e1 := period8_double_signed_forward_entry L hL i j 1 (by omega) 1
  have e2 := period8_double_signed_forward_entry L hL j i 1 (by omega) 1
  have e3 := period8_double_signed_forward_entry L hL i j 2 (by omega)
    (period8TargetLift i.val)
  have e4 := period8_double_signed_forward_entry L hL j i 2 (by omega)
    (period8TargetLift j.val)
  rw [period8_periodic_matrix_entry, period8_periodic_matrix_entry]
  simp only [period8_double_high_lift, period8_double_low_lift,
    period8_double_cross_half_next L hL j i 1 (by omega),
    period8_double_cross_half_next L hL j i 2 (by omega)]
  simp only [period8TargetMatrix, hamiltonGaugeMatrix, forwardStepOne, forwardStepTwo,
    neg_one_mul]
  linear_combination e1 + e2 + e3 + e4

/-- Sum over the cover as the two explicit vertex halves. -/
theorem period8_sum_double (L : ℕ) (f : Fin (8 * (2 * L)) → ℂ) :
    (∑ i, f i) = (∑ i, f (period8DoubleLow L i)) +
      ∑ i, f (period8DoubleHigh L i) := by
  rw [← (period8DoubleIndex L).sum_comp f, Fintype.sum_sum_type]
  rfl

theorem period8_double_matrixC_difference (L : ℕ) (hL : 0 < L)
    (i j : Fin (8 * L)) :
    period8TargetMatrixC (2 * L) 1 (period8DoubleLow L i) (period8DoubleLow L j) -
      period8TargetMatrixC (2 * L) 1 (period8DoubleLow L i) (period8DoubleHigh L j) =
        period8TargetMatrixC L (-1) i j := by
  have h := period8_double_matrix_difference L hL i j
  unfold period8TargetMatrixC
  exact_mod_cast h

theorem period8_double_matrixC_same_blocks (L : ℕ) (hL : 0 < L)
    (i j : Fin (8 * L)) :
    period8TargetMatrixC (2 * L) 1 (period8DoubleHigh L i) (period8DoubleHigh L j) =
      period8TargetMatrixC (2 * L) 1 (period8DoubleLow L i) (period8DoubleLow L j) := by
  unfold period8TargetMatrixC
  exact_mod_cast period8_double_matrix_same_blocks L hL i j

theorem period8_double_matrixC_cross_blocks (L : ℕ) (hL : 0 < L)
    (i j : Fin (8 * L)) :
    period8TargetMatrixC (2 * L) 1 (period8DoubleHigh L i) (period8DoubleLow L j) =
      period8TargetMatrixC (2 * L) 1 (period8DoubleLow L i) (period8DoubleHigh L j) := by
  unfold period8TargetMatrixC
  exact_mod_cast period8_double_matrix_cross_blocks L hL i j

theorem period8_double_action_low (L : ℕ) (hL : 0 < L)
    (u : Fin (8 * L) → ℂ) (i : Fin (8 * L)) :
    (period8TargetMatrixC (2 * L) 1).mulVec (period8DoubleLift L u)
      (period8DoubleLow L i) = (period8TargetMatrixC L (-1)).mulVec u i := by
  simp only [Matrix.mulVec, dotProduct]
  rw [period8_sum_double L]
  simp only [period8_double_lift_low, period8_double_lift_high]
  rw [← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro j _
  rw [mul_neg, ← sub_eq_add_neg, ← sub_mul, period8_double_matrixC_difference L hL]

theorem period8_double_action_high (L : ℕ) (hL : 0 < L)
    (u : Fin (8 * L) → ℂ) (i : Fin (8 * L)) :
    (period8TargetMatrixC (2 * L) 1).mulVec (period8DoubleLift L u)
      (period8DoubleHigh L i) = -(period8TargetMatrixC L (-1)).mulVec u i := by
  simp only [Matrix.mulVec, dotProduct]
  rw [period8_sum_double L]
  simp only [period8_double_lift_low, period8_double_lift_high,
    period8_double_matrixC_same_blocks L hL, period8_double_matrixC_cross_blocks L hL]
  rw [← Finset.sum_add_distrib, ← Finset.sum_neg_distrib]
  apply Finset.sum_congr rfl
  intro j _
  have h := period8_double_matrixC_difference L hL i j
  linear_combination -h * u j

/-- The complete raw-graph operator intertwining; no spectral or cell hypothesis is assumed. -/
theorem period8_double_lift_intertwines (L : ℕ) (hL : 0 < L)
    (u : Fin (8 * L) → ℂ) :
    (period8TargetMatrixC (2 * L) 1).mulVec (period8DoubleLift L u) =
      period8DoubleLift L ((period8TargetMatrixC L (-1)).mulVec u) := by
  funext i
  obtain ⟨j, rfl⟩ := (period8DoubleIndex L).surjective i
  cases j with
  | inl j =>
    change (period8TargetMatrixC (2 * L) 1).mulVec (period8DoubleLift L u)
      (period8DoubleLow L j) = period8DoubleLift L _ (period8DoubleLow L j)
    rw [period8_double_action_low L hL, period8_double_lift_low]
  | inr j =>
    change (period8TargetMatrixC (2 * L) 1).mulVec (period8DoubleLift L u)
      (period8DoubleHigh L j) = period8DoubleLift L _ (period8DoubleHigh L j)
    rw [period8_double_action_high L hL, period8_double_lift_high]

theorem period8_double_lift_smul (L : ℕ) (u : Fin (8 * L) → ℂ) (c : ℂ) :
    period8DoubleLift L (c • u) = c • period8DoubleLift L u := by
  funext i
  obtain ⟨j, rfl⟩ := (period8DoubleIndex L).surjective i
  cases j with
  | inl j =>
    change period8DoubleLift L (c • u) (period8DoubleLow L j) =
      c * period8DoubleLift L u (period8DoubleLow L j)
    simp
  | inr j =>
    change period8DoubleLift L (c • u) (period8DoubleHigh L j) =
      c * period8DoubleLift L u (period8DoubleHigh L j)
    simp

/-- Every real eigenvalue of the raw alpha-minus signed adjacency matrix is
strictly below the continuous endpoint in squared modulus, for every L ≥ 1. -/
theorem period8_alpha_minus_raw_eigen_square_lt_edge (L : ℕ) (hL : 0 < L)
    (u : Fin (8 * L) → ℂ) (lambda : ℝ) (hu : u ≠ 0)
    (hEig : (period8TargetMatrixC L (-1)).mulVec u = (lambda : ℂ) • u) :
    lambda^2 < period8Edge := by
  apply period8_double_cover_antisector_eigen_square_lt_edge L hL
    (period8DoubleLift L u) lambda
  · intro hz
    apply hu
    funext i
    have he := congrFun hz (period8DoubleLow L i)
    simpa using he
  · exact period8_double_lift_antiperiodic L hL u
  · rw [period8_double_lift_intertwines L hL, hEig, period8_double_lift_smul]

/-- Unconditional raw-graph spectral conclusion in the existing Hermitian eigenvalue API. -/
theorem period8_alpha_minus_main_theorem (L : ℕ) (hL : 0 < L) :
    ∀ i : Fin (8 * L),
      ((period8_target_matrix_isHermitian L (-1)).eigenvalues i)^2 < period8Edge := by
  intro i
  apply period8_alpha_minus_raw_eigen_square_lt_edge L hL
    (u := ⇑((period8_target_matrix_isHermitian L (-1)).eigenvectorBasis i))
  · exact (WithLp.ofLp_eq_zero 2).ne.2 <|
      (period8_target_matrix_isHermitian L (-1)).eigenvectorBasis.orthonormal.ne_zero i
  · exact (period8_target_matrix_isHermitian L (-1)).mulVec_eigenvectorBasis i

end TargetA

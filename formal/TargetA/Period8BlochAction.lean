import TargetA.FiniteBloch
import TargetA.Period8Fiber

namespace TargetA

/-!
The three cell matrices below isolate the zero, positive, and negative cell
translations in the period-eight Hamiltonian.  Their exact sum is the fibre
symbol already used in the chiral calculation.
-/

noncomputable def period8IntraCell : Matrix (Fin 8) (Fin 8) ℂ :=
  !![0, 1, 1, 0, 0, 0, 0, 0;
     1, 0, 1, 1, 0, 0, 0, 0;
     1, 1, 0, 1, -1, 0, 0, 0;
     0, 1, 1, 0, 1, 1, 0, 0;
     0, 0, -1, 1, 0, 1, -1, 0;
     0, 0, 0, 1, 1, 0, 1, -1;
     0, 0, 0, 0, -1, 1, 0, 1;
     0, 0, 0, 0, 0, -1, 1, 0]

noncomputable def period8ForwardIntraCell : Matrix (Fin 8) (Fin 8) ℂ :=
  !![0, 1, 1, 0, 0, 0, 0, 0;
     0, 0, 1, 1, 0, 0, 0, 0;
     0, 0, 0, 1, -1, 0, 0, 0;
     0, 0, 0, 0, 1, 1, 0, 0;
     0, 0, 0, 0, 0, 1, -1, 0;
     0, 0, 0, 0, 0, 0, 1, -1;
     0, 0, 0, 0, 0, 0, 0, 1;
     0, 0, 0, 0, 0, 0, 0, 0]

noncomputable def period8ForwardCell : Matrix (Fin 8) (Fin 8) ℂ :=
  !![0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0;
     1, 0, 0, 0, 0, 0, 0, 0;
     1, -1, 0, 0, 0, 0, 0, 0]

noncomputable def period8BackwardCell : Matrix (Fin 8) (Fin 8) ℂ :=
  !![0, 0, 0, 0, 0, 0, 1, 1;
     0, 0, 0, 0, 0, 0, 0, -1;
     0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0]

set_option maxHeartbeats 1500000 in
theorem period8_intra_as_forward_add_transpose :
    period8IntraCell = period8ForwardIntraCell +
      Matrix.transpose period8ForwardIntraCell := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [period8IntraCell, period8ForwardIntraCell, Matrix.transpose_apply]

set_option maxHeartbeats 1500000 in
theorem period8_backward_is_forward_transpose :
    period8BackwardCell = Matrix.transpose period8ForwardCell := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [period8BackwardCell, period8ForwardCell, Matrix.transpose_apply]

noncomputable def period8ForwardCellOperatorFin (L : ℕ)
    (F : Fin L → Fin 8 → ℂ) (m : Fin L) : Fin 8 → ℂ :=
  period8ForwardIntraCell.mulVec (F m) +
    period8ForwardCell.mulVec (F (cyclicNext m 1))

noncomputable def period8BackwardCellOperatorFin (L : ℕ)
    (F : Fin L → Fin 8 → ℂ) (m : Fin L) : Fin 8 → ℂ :=
  (Matrix.transpose period8ForwardIntraCell).mulVec (F m) +
    (Matrix.transpose period8ForwardCell).mulVec (F (cyclicPrev m))

noncomputable def period8CellActionFin (L : ℕ)
    (F : Fin L → Fin 8 → ℂ) (m : Fin L) : Fin 8 → ℂ :=
  period8IntraCell.mulVec (F m) +
    period8ForwardCell.mulVec (F (cyclicNext m 1)) +
      period8BackwardCell.mulVec (F (cyclicPrev m))

theorem period8_cell_action_fin_eq_forward_add_backward (L : ℕ)
    (F : Fin L → Fin 8 → ℂ) (m : Fin L) :
    period8CellActionFin L F m =
      period8ForwardCellOperatorFin L F m +
        period8BackwardCellOperatorFin L F m := by
  simp only [period8CellActionFin, period8ForwardCellOperatorFin,
    period8BackwardCellOperatorFin]
  rw [period8_intra_as_forward_add_transpose,
    period8_backward_is_forward_transpose]
  simp only [Matrix.add_mulVec]
  abel

theorem period8_forward_cell_operator_fin_apply (L : ℕ)
    (F : Fin L → Fin 8 → ℂ) (m : Fin L) (r : Fin 8) :
    period8ForwardCellOperatorFin L F m r =
      F (cellForwardOne L (m, r)).1 (cellForwardOne L (m, r)).2 +
        (period8TargetTau r : ℂ) *
          F (cellForwardTwo L (m, r)).1 (cellForwardTwo L (m, r)).2 := by
  fin_cases r <;>
    simp [period8ForwardCellOperatorFin, period8ForwardIntraCell,
      period8ForwardCell, period8TargetTau, cellForwardOne, cellForwardTwo,
      Matrix.vecHead, Matrix.vecTail]

theorem period8_forward_reindex_actionC_eq_cell_operator (L : ℕ) (hL : 0 < L)
    (F : Fin L → Fin 8 → ℂ) (m : Fin L) (r : Fin 8) :
    (hamiltonGaugeForwardMatrixC (n := 8 * L) 1 period8TargetLift).mulVec
        (cellEncodeC L hL F) ((cellReindex L hL).symm (m, r)) =
      period8ForwardCellOperatorFin L F m r := by
  rw [period8_forward_reindex_actionC]
  exact (period8_forward_cell_operator_fin_apply L F m r).symm

noncomputable def period8ReindexedForwardOperator (L : ℕ) (hL : 0 < L)
    (F : Fin L → Fin 8 → ℂ) (m : Fin L) (r : Fin 8) : ℂ :=
  (hamiltonGaugeForwardMatrixC (n := 8 * L) 1 period8TargetLift).mulVec
    (cellEncodeC L hL F) ((cellReindex L hL).symm (m, r))

noncomputable def period8ReindexedForwardMatrixC (L : ℕ) (hL : 0 < L) :
    Matrix (Fin L × Fin 8) (Fin L × Fin 8) ℂ :=
  fun p q => (hamiltonGaugeForwardMatrixC (n := 8 * L) 1 period8TargetLift)
    ((cellReindex L hL).symm p) ((cellReindex L hL).symm q)

noncomputable def period8ForwardCellMatrixFin (L : ℕ) :
    Matrix (Fin L × Fin 8) (Fin L × Fin 8) ℂ :=
  fun p q =>
    (if q.1 = p.1 then period8ForwardIntraCell p.2 q.2 else 0) +
      if q.1 = cyclicNext p.1 1 then period8ForwardCell p.2 q.2 else 0

theorem period8_forward_cell_matrix_fin_mulVec (L : ℕ)
    (F : Fin L → Fin 8 → ℂ) (m : Fin L) (r : Fin 8) :
    (period8ForwardCellMatrixFin L).mulVec (fun p => F p.1 p.2) (m, r) =
      period8ForwardCellOperatorFin L F m r := by
  simp only [period8ForwardCellMatrixFin, period8ForwardCellOperatorFin,
    Matrix.mulVec, dotProduct, Fintype.sum_prod_type]
  simp_rw [add_mul]
  simp_rw [Finset.sum_add_distrib]
  simp
  rfl

theorem period8_forward_cell_matrix_fin_transpose_mulVec (L : ℕ) (hL : 0 < L)
    (F : Fin L → Fin 8 → ℂ) (m : Fin L) (r : Fin 8) :
    (Matrix.transpose (period8ForwardCellMatrixFin L)).mulVec
        (fun p => F p.1 p.2) (m, r) =
      period8BackwardCellOperatorFin L F m r := by
  simp only [period8ForwardCellMatrixFin, period8BackwardCellOperatorFin,
    Matrix.mulVec, dotProduct, Matrix.transpose_apply, Fintype.sum_prod_type]
  simp_rw [add_mul, Finset.sum_add_distrib]
  have hnext (q : Fin L) : m = cyclicNext q 1 ↔ q = cyclicPrev m := by
    rw [eq_comm, cyclic_next_eq_iff hL]
  simp_rw [hnext]
  simp
  rfl

noncomputable def period8CellMatrixFin (L : ℕ) :
    Matrix (Fin L × Fin 8) (Fin L × Fin 8) ℂ :=
  period8ForwardCellMatrixFin L + Matrix.transpose (period8ForwardCellMatrixFin L)

theorem period8_cell_matrix_fin_mulVec (L : ℕ) (hL : 0 < L)
    (F : Fin L → Fin 8 → ℂ) (m : Fin L) (r : Fin 8) :
    (period8CellMatrixFin L).mulVec (fun p => F p.1 p.2) (m, r) =
      period8CellActionFin L F m r := by
  simp only [period8CellMatrixFin, Matrix.add_mulVec]
  simp only [Pi.add_apply]
  rw [period8_forward_cell_matrix_fin_mulVec L F m r,
    period8_forward_cell_matrix_fin_transpose_mulVec L hL F m r]
  exact (congrFun (period8_cell_action_fin_eq_forward_add_backward L F m).symm r)

theorem period8_reindexed_forward_matrix_mulVec (L : ℕ) (hL : 0 < L)
    (F : Fin L → Fin 8 → ℂ) (m : Fin L) (r : Fin 8) :
    (period8ReindexedForwardMatrixC L hL).mulVec (fun p => F p.1 p.2) (m, r) =
      period8ForwardCellOperatorFin L F m r := by
  change (∑ q : Fin L × Fin 8,
    (hamiltonGaugeForwardMatrixC (n := 8 * L) 1 period8TargetLift)
      ((cellReindex L hL).symm (m, r)) ((cellReindex L hL).symm q) * F q.1 q.2) = _
  let g : Fin (8 * L) → ℂ := fun i =>
    (hamiltonGaugeForwardMatrixC (n := 8 * L) 1 period8TargetLift)
      ((cellReindex L hL).symm (m, r)) i * cellEncodeC L hL F i
  have hencode (q : Fin L × Fin 8) :
      cellEncodeC L hL F ((cellReindex L hL).symm q) = F q.1 q.2 := by
    simp [cellEncodeC]
  simp_rw [← hencode]
  change (∑ q : Fin L × Fin 8, g ((cellReindex L hL).symm q)) = _
  rw [(cellReindex L hL).symm.sum_comp]
  change (hamiltonGaugeForwardMatrixC (n := 8 * L) 1 period8TargetLift).mulVec
      (cellEncodeC L hL F) ((cellReindex L hL).symm (m, r)) = _
  exact period8_forward_reindex_actionC_eq_cell_operator L hL F m r

theorem period8_reindexed_forward_matrix_eq_cell_matrix (L : ℕ) (hL : 0 < L) :
    period8ReindexedForwardMatrixC L hL = period8ForwardCellMatrixFin L := by
  ext p q
  let F : Fin L → Fin 8 → ℂ := fun m r => if (m, r) = q then 1 else 0
  have hleft := period8_reindexed_forward_matrix_mulVec L hL F p.1 p.2
  have hright := period8_forward_cell_matrix_fin_mulVec L F p.1 p.2
  have haction :
      (period8ReindexedForwardMatrixC L hL).mulVec (fun x => F x.1 x.2) p =
        (period8ForwardCellMatrixFin L).mulVec (fun x => F x.1 x.2) p :=
    hleft.trans hright.symm
  simpa [F, Matrix.mulVec, dotProduct] using haction

noncomputable def period8ReindexedMatrixC (L : ℕ) (hL : 0 < L) :
    Matrix (Fin L × Fin 8) (Fin L × Fin 8) ℂ :=
  fun p q => period8TargetMatrixC L 1
    ((cellReindex L hL).symm p) ((cellReindex L hL).symm q)

theorem period8_reindexed_matrix_eq_forward_add_transpose (L : ℕ) (hL : 0 < L) :
    period8ReindexedMatrixC L hL =
      period8ReindexedForwardMatrixC L hL +
        Matrix.transpose (period8ReindexedForwardMatrixC L hL) := by
  ext p q
  simp [period8ReindexedMatrixC, period8ReindexedForwardMatrixC,
    period8TargetMatrixC, period8TargetMatrix, hamiltonGaugeMatrix,
    hamiltonGaugeForwardMatrixC, hamiltonGaugeForwardMatrix,
    Matrix.transpose_apply]
  ac_rfl

theorem period8_reindexed_matrix_eq_cell_matrix (L : ℕ) (hL : 0 < L) :
    period8ReindexedMatrixC L hL = period8CellMatrixFin L := by
  rw [period8_reindexed_matrix_eq_forward_add_transpose,
    period8_reindexed_forward_matrix_eq_cell_matrix]
  rfl

theorem period8_reindexed_matrix_mulVec (L : ℕ) (hL : 0 < L)
    (F : Fin L → Fin 8 → ℂ) (m : Fin L) (r : Fin 8) :
    (period8ReindexedMatrixC L hL).mulVec (fun p => F p.1 p.2) (m, r) =
      period8CellActionFin L F m r := by
  rw [period8_reindexed_matrix_eq_cell_matrix]
  exact period8_cell_matrix_fin_mulVec L hL F m r

theorem period8_reindexed_forward_operator_eq (L : ℕ) (hL : 0 < L)
    (F : Fin L → Fin 8 → ℂ) :
    period8ReindexedForwardOperator L hL F =
      fun m r => period8ForwardCellOperatorFin L F m r := by
  funext m r
  exact period8_forward_reindex_actionC_eq_cell_operator L hL F m r

set_option maxHeartbeats 1500000 in
theorem period8_fiber_as_cell_symbol (xi : ℂ) :
    period8Fiber xi = period8IntraCell +
      (xi^2) • period8ForwardCell + (xi⁻¹^2) • period8BackwardCell := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [period8Fiber, period8IntraCell, period8ForwardCell,
      period8BackwardCell]

noncomputable def period8CellTranslation {L : ℕ} (a : ZMod L)
    (F : ZMod L → Fin 8 → ℂ) : ZMod L → Fin 8 → ℂ :=
  fun m => F (a + m)

noncomputable def period8CellDFT {L : ℕ} [NeZero L]
    (F : ZMod L → Fin 8 → ℂ) (k : ZMod L) : Fin 8 → ℂ :=
  ZMod.dft F k

theorem period8_cell_dft_translation {L : ℕ} [NeZero L]
    (a k : ZMod L) (F : ZMod L → Fin 8 → ℂ) :
    period8CellDFT (period8CellTranslation a F) k =
      ZMod.stdAddChar (a * k) • period8CellDFT F k := by
  ext r
  simp only [period8CellDFT, period8CellTranslation, ZMod.dft_apply,
    Finset.sum_apply, Pi.smul_apply, smul_eq_mul]
  exact dft_cellTranslation a k (fun m => F m r)

theorem period8_cell_dft_matrix {L : ℕ} [NeZero L]
    (B : Matrix (Fin 8) (Fin 8) ℂ) (F : ZMod L → Fin 8 → ℂ)
    (k : ZMod L) :
    period8CellDFT (fun m => B.mulVec (F m)) k =
      B.mulVec (period8CellDFT F k) := by
  ext r
  simp only [period8CellDFT, ZMod.dft_apply, Finset.sum_apply,
    Pi.smul_apply, smul_eq_mul, Matrix.mulVec, dotProduct]
  simp_rw [Finset.mul_sum]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro s _
  apply Finset.sum_congr rfl
  intro m _
  ring

noncomputable def period8CellAction {L : ℕ}
    (F : ZMod L → Fin 8 → ℂ) : ZMod L → Fin 8 → ℂ :=
  fun m =>
    period8IntraCell.mulVec (F m) +
      period8ForwardCell.mulVec (F (1 + m)) +
        period8BackwardCell.mulVec (F (-1 + m))

noncomputable def finCellToZModState (L : ℕ) [NeZero L]
    (F : Fin L → Fin 8 → ℂ) : ZMod L → Fin 8 → ℂ :=
  fun z r => F ((ZMod.finEquiv L).symm z) r

theorem period8_fin_cell_action_to_zmod (L : ℕ) [NeZero L] (hL : 0 < L)
    (F : Fin L → Fin 8 → ℂ) (m : Fin L) :
    period8CellAction (finCellToZModState L F) (ZMod.finEquiv L m) =
      period8CellActionFin L F m := by
  have hzero : finCellToZModState L F (ZMod.finEquiv L m) = F m := by
    funext r
    simp [finCellToZModState]
  have hforward :
      finCellToZModState L F (1 + ZMod.finEquiv L m) = F (cyclicNext m 1) := by
    rw [add_comm, ← zmod_finEquiv_cyclic_next L hL]
    funext r
    simp [finCellToZModState]
  have hbackward :
      finCellToZModState L F (-1 + ZMod.finEquiv L m) = F (cyclicPrev m) := by
    rw [show (-1 : ZMod L) + ZMod.finEquiv L m = ZMod.finEquiv L m - 1 by ring,
      ← zmod_finEquiv_cyclic_prev L hL]
    funext r
    simp [finCellToZModState]
  rw [period8CellAction, hzero, hforward, hbackward]
  rfl

theorem exists_nonzero_period8_cell_dft {L : ℕ} [NeZero L]
    (F : ZMod L → Fin 8 → ℂ) (hF : F ≠ 0) :
    ∃ k : ZMod L, period8CellDFT F k ≠ 0 := by
  by_contra h
  push Not at h
  apply hF
  apply (ZMod.dft (N := L)).injective
  funext k
  simpa [period8CellDFT] using h k

theorem period8_cell_dft_action {L : ℕ} [NeZero L]
    (F : ZMod L → Fin 8 → ℂ) (k : ZMod L) (xi : ℂ)
    (hxi : xi^2 = ZMod.stdAddChar k) :
    period8CellDFT (period8CellAction F) k =
      (period8Fiber xi).mulVec (period8CellDFT F k) := by
  let D := period8CellDFT F k
  have hzero :
      period8CellDFT (fun m => period8IntraCell.mulVec (F m)) k =
        period8IntraCell.mulVec D := by
    simpa [D] using period8_cell_dft_matrix period8IntraCell F k
  have hforward :
      period8CellDFT (fun m => period8ForwardCell.mulVec (F (1 + m))) k =
        ZMod.stdAddChar k • period8ForwardCell.mulVec D := by
    calc
      period8CellDFT (fun m => period8ForwardCell.mulVec (F (1 + m))) k =
          period8ForwardCell.mulVec
            (period8CellDFT (period8CellTranslation 1 F) k) := by
              simpa [period8CellTranslation] using
                period8_cell_dft_matrix period8ForwardCell
                  (period8CellTranslation 1 F) k
      _ = period8ForwardCell.mulVec
            (ZMod.stdAddChar k • period8CellDFT F k) := by
              rw [period8_cell_dft_translation]
              simp only [one_mul]
      _ = ZMod.stdAddChar k • period8ForwardCell.mulVec D := by
              rw [Matrix.mulVec_smul]
  have hbackward :
      period8CellDFT (fun m => period8BackwardCell.mulVec (F (-1 + m))) k =
        ZMod.stdAddChar (-k) • period8BackwardCell.mulVec D := by
    calc
      period8CellDFT (fun m => period8BackwardCell.mulVec (F (-1 + m))) k =
          period8BackwardCell.mulVec
            (period8CellDFT (period8CellTranslation (-1) F) k) := by
              simpa [period8CellTranslation] using
                period8_cell_dft_matrix period8BackwardCell
                  (period8CellTranslation (-1) F) k
      _ = period8BackwardCell.mulVec
            (ZMod.stdAddChar ((-1) * k) • period8CellDFT F k) := by
              rw [period8_cell_dft_translation]
      _ = ZMod.stdAddChar (-k) • period8BackwardCell.mulVec D := by
              rw [Matrix.mulVec_smul]
              simp [D]
  have hsplit : period8CellDFT (period8CellAction F) k =
      period8CellDFT (fun m => period8IntraCell.mulVec (F m)) k +
        period8CellDFT (fun m => period8ForwardCell.mulVec (F (1 + m))) k +
          period8CellDFT (fun m => period8BackwardCell.mulVec (F (-1 + m))) k := by
    change ZMod.dft (period8CellAction F) k =
      ZMod.dft (fun m => period8IntraCell.mulVec (F m)) k +
        ZMod.dft (fun m => period8ForwardCell.mulVec (F (1 + m))) k +
          ZMod.dft (fun m => period8BackwardCell.mulVec (F (-1 + m))) k
    rw [show period8CellAction F =
      (fun m => period8IntraCell.mulVec (F m)) +
        (fun m => period8ForwardCell.mulVec (F (1 + m))) +
          (fun m => period8BackwardCell.mulVec (F (-1 + m))) by rfl]
    simp only [map_add]
    rfl
  rw [hsplit, hzero, hforward, hbackward, period8_fiber_as_cell_symbol]
  have hback : ZMod.stdAddChar (-k) = xi⁻¹^2 := by
    rw [AddChar.map_neg_eq_inv, ← hxi, inv_pow]
  rw [hxi, hback]
  simp only [Matrix.add_mulVec, Matrix.smul_mulVec]
  rfl

theorem period8_cell_eigen_dft_fiber {L : ℕ} [NeZero L]
    (F : ZMod L → Fin 8 → ℂ) (lambda : ℂ) (k : ZMod L) (xi : ℂ)
    (hxi : xi^2 = ZMod.stdAddChar k)
    (hEig : period8CellAction F = lambda • F) :
    (period8Fiber xi).mulVec (period8CellDFT F k) =
      lambda • period8CellDFT F k := by
  calc
    (period8Fiber xi).mulVec (period8CellDFT F k) =
        period8CellDFT (period8CellAction F) k := by
          rw [period8_cell_dft_action F k xi hxi]
    _ = period8CellDFT (lambda • F) k := by rw [hEig]
    _ = lambda • period8CellDFT F k := by
          simpa [period8CellDFT] using congrFun ((ZMod.dft (N := L)).map_smul lambda F) k

end TargetA

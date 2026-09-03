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

end TargetA

import TargetA.R2FirstInverseCertificate
namespace TargetA
open scoped Matrix
set_option maxHeartbeats 300000
set_option linter.unusedSimpArgs false
def r2StepX0 : Matrix (Fin 4) (Fin 4) ℚ := !![(98/25:ℚ), 0, -1, 0; 0, (98/25:ℚ), 0, -1; -1, 0, (98/25:ℚ), 0; 0, -1, 0, (98/25:ℚ)]
def r2StepR0 : Matrix (Fin 2) (Fin 4) ℚ := !![-1, -2, 1, 0; -2, -1, 0, -1]
def r2StepW0 : Matrix (Fin 4) (Fin 4) ℚ := !![0, 0, -1, 0; 0, 0, 0, 1; 0, 0, 0, 0; 0, 0, 0, 0]
def r2StepG0 : Matrix (Fin 2) (Fin 2) ℚ := !![(98/25:ℚ), 0; 0, (98/25:ℚ)]
def r2StepH0 : Matrix (Fin 4) (Fin 4) ℚ := !![(98/25:ℚ), 0, -1, 0; 0, (98/25:ℚ), 0, -1; -1, 0, (98/25:ℚ), 0; 0, -1, 0, (98/25:ℚ)]
def r2StepC0 : Matrix (Fin 2) (Fin 4) ℚ := !![-1, 0, -1, 0; 0, -1, 0, -1]
def r2StepState0 : R2RecurrenceState ℚ where
  X := r2StepX0
  R := r2StepR0
  W := r2StepW0
  G := r2StepG0
  H := r2StepH0
  C := r2StepC0
def r2StepX1 : Matrix (Fin 4) (Fin 4) ℚ := !![(481192/224475:ℚ), (9800/8979:ℚ), (-48/73:ℚ), (4900/8979:ℚ); (9800/8979:ℚ), (543692/224475:ℚ), (-4900/8979:ℚ), (-148/123:ℚ); (-48/73:ℚ), (-4900/8979:ℚ), (818692/224475:ℚ), 0; (4900/8979:ℚ), (-148/123:ℚ), 0, (818692/224475:ℚ)]
def r2StepR1 : Matrix (Fin 2) (Fin 4) ℚ := !![(2500/8979:ℚ), 0, (-25/123:ℚ), (-1250/8979:ℚ); 0, (2500/8979:ℚ), (1250/8979:ℚ), (-25/73:ℚ)]
def r2StepW1 : Matrix (Fin 4) (Fin 4) ℚ := !![0, 0, (-25/73:ℚ), (-1250/8979:ℚ); 0, 0, (1250/8979:ℚ), (-25/123:ℚ); 0, 0, (625/8979:ℚ), 0; 0, 0, 0, (625/8979:ℚ)]
def r2StepG1 : Matrix (Fin 2) (Fin 2) ℚ := !![(543692/224475:ℚ), (-9800/8979:ℚ); (-9800/8979:ℚ), (481192/224475:ℚ)]
def r2StepH1 : Matrix (Fin 4) (Fin 4) ℚ := !![(98/25:ℚ), 0, -1, 0; 0, (98/25:ℚ), 0, -1; -1, 0, (818692/224475:ℚ), 0; 0, -1, 0, (818692/224475:ℚ)]
def r2StepC1 : Matrix (Fin 2) (Fin 4) ℚ := !![-1, 0, (-148/123:ℚ), (4900/8979:ℚ); 0, -1, (-4900/8979:ℚ), (-48/73:ℚ)]
def r2StepState1 : R2RecurrenceState ℚ where
  X := r2StepX1
  R := r2StepR1
  W := r2StepW1
  G := r2StepG1
  H := r2StepH1
  C := r2StepC1

theorem r2_first_recorded_initial : r2StepState0 = r2InitialState ℚ := by
  apply R2RecurrenceState.ext
  all_goals try rfl
  all_goals
    ext i j
    fin_cases i <;> fin_cases j <;>
      norm_num [r2StepState0, r2StepX0, r2StepR0, r2StepW0, r2StepG0, r2StepH0, r2StepC0,
        r2InitialState, r2D, Matrix.one_apply]

theorem r2_first_transition_X :
    (r2StepState1).X =
      (r2UpdateWithInverse ℚ 0 r2StepState0 r2FirstInverseQ).X := by
  have he : r2Coupling ℚ 0 = r2EP ℚ := rfl
  ext i j
  fin_cases i <;> fin_cases j
  all_goals
    simp [r2StepState0, r2StepState1, r2UpdateWithInverse, he, r2D, r2EP,
      r2FirstInverseQ, r2StepX0, r2StepR0, r2StepW0, r2StepG0, r2StepH0, r2StepC0, r2StepX1, r2StepR1, r2StepW1, r2StepG1, r2StepH1, r2StepC1,
      Matrix.mul_apply, Matrix.vecMul, Matrix.mulVec, dotProduct, Matrix.transpose_apply,
      Matrix.sub_apply, Matrix.neg_apply, Matrix.of_apply, Fin.sum_univ_succ,
      Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
      Matrix.cons_val_three, Matrix.cons_val_four, Matrix.vecHead, Matrix.vecTail,
      Fin.val_zero, Fin.val_one, Fin.reduceFinMk, Fin.reduceAdd,
      mul_zero, zero_mul, add_zero, zero_add, mul_one, one_mul, neg_zero] <;>
      field_simp <;> norm_num

theorem r2_first_transition_R :
    (r2StepState1).R =
      (r2UpdateWithInverse ℚ 0 r2StepState0 r2FirstInverseQ).R := by
  have he : r2Coupling ℚ 0 = r2EP ℚ := rfl
  ext i j
  fin_cases i <;> fin_cases j
  all_goals
    simp [r2StepState0, r2StepState1, r2UpdateWithInverse, he, r2D, r2EP,
      r2FirstInverseQ, r2StepX0, r2StepR0, r2StepW0, r2StepG0, r2StepH0, r2StepC0, r2StepX1, r2StepR1, r2StepW1, r2StepG1, r2StepH1, r2StepC1,
      Matrix.mul_apply, Matrix.vecMul, Matrix.mulVec, dotProduct, Matrix.transpose_apply,
      Matrix.sub_apply, Matrix.neg_apply, Matrix.of_apply, Fin.sum_univ_succ,
      Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
      Matrix.cons_val_three, Matrix.cons_val_four, Matrix.vecHead, Matrix.vecTail,
      Fin.val_zero, Fin.val_one, Fin.reduceFinMk, Fin.reduceAdd,
      mul_zero, zero_mul, add_zero, zero_add, mul_one, one_mul, neg_zero] <;>
      field_simp <;> norm_num

theorem r2_first_transition_W :
    (r2StepState1).W =
      (r2UpdateWithInverse ℚ 0 r2StepState0 r2FirstInverseQ).W := by
  have he : r2Coupling ℚ 0 = r2EP ℚ := rfl
  ext i j
  fin_cases i <;> fin_cases j
  all_goals
    simp [r2StepState0, r2StepState1, r2UpdateWithInverse, he, r2D, r2EP,
      r2FirstInverseQ, r2StepX0, r2StepR0, r2StepW0, r2StepG0, r2StepH0, r2StepC0, r2StepX1, r2StepR1, r2StepW1, r2StepG1, r2StepH1, r2StepC1,
      Matrix.mul_apply, Matrix.vecMul, Matrix.mulVec, dotProduct, Matrix.transpose_apply,
      Matrix.sub_apply, Matrix.neg_apply, Matrix.of_apply, Fin.sum_univ_succ,
      Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
      Matrix.cons_val_three, Matrix.cons_val_four, Matrix.vecHead, Matrix.vecTail,
      Fin.val_zero, Fin.val_one, Fin.reduceFinMk, Fin.reduceAdd,
      mul_zero, zero_mul, add_zero, zero_add, mul_one, one_mul, neg_zero] <;>
      field_simp <;> norm_num

theorem r2_first_transition_G :
    (r2StepState1).G =
      (r2UpdateWithInverse ℚ 0 r2StepState0 r2FirstInverseQ).G := by
  have he : r2Coupling ℚ 0 = r2EP ℚ := rfl
  ext i j
  fin_cases i <;> fin_cases j
  all_goals
    simp [r2StepState0, r2StepState1, r2UpdateWithInverse, he, r2D, r2EP,
      r2FirstInverseQ, r2StepX0, r2StepR0, r2StepW0, r2StepG0, r2StepH0, r2StepC0, r2StepX1, r2StepR1, r2StepW1, r2StepG1, r2StepH1, r2StepC1,
      Matrix.mul_apply, Matrix.vecMul, Matrix.mulVec, dotProduct, Matrix.transpose_apply,
      Matrix.sub_apply, Matrix.neg_apply, Matrix.of_apply, Fin.sum_univ_succ,
      Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
      Matrix.cons_val_three, Matrix.cons_val_four, Matrix.vecHead, Matrix.vecTail,
      Fin.val_zero, Fin.val_one, Fin.reduceFinMk, Fin.reduceAdd,
      mul_zero, zero_mul, add_zero, zero_add, mul_one, one_mul, neg_zero] <;>
      field_simp <;> norm_num

theorem r2_first_transition_H :
    (r2StepState1).H =
      (r2UpdateWithInverse ℚ 0 r2StepState0 r2FirstInverseQ).H := by
  have he : r2Coupling ℚ 0 = r2EP ℚ := rfl
  ext i j
  fin_cases i <;> fin_cases j
  all_goals
    simp [r2StepState0, r2StepState1, r2UpdateWithInverse, he, r2D, r2EP,
      r2FirstInverseQ, r2StepX0, r2StepR0, r2StepW0, r2StepG0, r2StepH0, r2StepC0, r2StepX1, r2StepR1, r2StepW1, r2StepG1, r2StepH1, r2StepC1,
      Matrix.mul_apply, Matrix.vecMul, Matrix.mulVec, dotProduct, Matrix.transpose_apply,
      Matrix.sub_apply, Matrix.neg_apply, Matrix.of_apply, Fin.sum_univ_succ,
      Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
      Matrix.cons_val_three, Matrix.cons_val_four, Matrix.vecHead, Matrix.vecTail,
      Fin.val_zero, Fin.val_one, Fin.reduceFinMk, Fin.reduceAdd,
      mul_zero, zero_mul, add_zero, zero_add, mul_one, one_mul, neg_zero] <;>
      field_simp <;> norm_num

theorem r2_first_transition_C :
    (r2StepState1).C =
      (r2UpdateWithInverse ℚ 0 r2StepState0 r2FirstInverseQ).C := by
  have he : r2Coupling ℚ 0 = r2EP ℚ := rfl
  ext i j
  fin_cases i <;> fin_cases j
  all_goals
    simp [r2StepState0, r2StepState1, r2UpdateWithInverse, he, r2D, r2EP,
      r2FirstInverseQ, r2StepX0, r2StepR0, r2StepW0, r2StepG0, r2StepH0, r2StepC0, r2StepX1, r2StepR1, r2StepW1, r2StepG1, r2StepH1, r2StepC1,
      Matrix.mul_apply, Matrix.vecMul, Matrix.mulVec, dotProduct, Matrix.transpose_apply,
      Matrix.sub_apply, Matrix.neg_apply, Matrix.of_apply, Fin.sum_univ_succ,
      Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
      Matrix.cons_val_three, Matrix.cons_val_four, Matrix.vecHead, Matrix.vecTail,
      Fin.val_zero, Fin.val_one, Fin.reduceFinMk, Fin.reduceAdd,
      mul_zero, zero_mul, add_zero, zero_add, mul_one, one_mul, neg_zero] <;>
      field_simp <;> norm_num

theorem r2_first_recorded_transition : r2StepState1 =
    r2UpdateWithInverse ℚ 0 r2StepState0 r2FirstInverseQ := by
  exact R2RecurrenceState.ext r2_first_transition_X r2_first_transition_R
    r2_first_transition_W r2_first_transition_G r2_first_transition_H r2_first_transition_C

theorem r2_first_actual_orbit : r2Orbit ℚ 1 = r2StepState1 := by
  rw [r2Orbit, r2RecurrenceStep, r2Orbit, r2_first_actual_inverse]
  rw [← r2_first_recorded_initial]
  exact r2_first_recorded_transition.symm

/-- The checked first six-field update is also the genuine real recurrence state. -/
theorem r2_first_actual_real_orbit : r2Orbit ℝ 1 = r2RealState r2StepState1 := by
  change r2UpdateWithInverse ℝ 0 (r2InitialState ℝ) (r2InitialState ℝ).X⁻¹ = _
  rw [r2_first_actual_real_inverse, ← r2_real_initial, ← r2_first_recorded_initial,
    ← r2_real_update, ← r2_first_recorded_transition]

end TargetA

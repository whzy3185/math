import TargetA.R2RecurrenceCast

namespace TargetA
open scoped Matrix Kronecker
set_option maxHeartbeats 300000

/-- The generic two-dimensional adjugate identity, before any numerical normalization. -/
theorem r2_adjugate_two_identity {K : Type*} [CommRing K] (a b c d : K) :
    !![a, b; c, d] * !![d, -b; -c, a] =
      (a*d-b*c) • (1 : Matrix (Fin 2) (Fin 2) K) := by
  simpa only [Matrix.adjugate_fin_two_of, Matrix.det_fin_two_of] using
    Matrix.mul_adjugate (!![a,b;c,d])

theorem r2_inverse_two_formula {K : Type*} [Field K] (a b c d : K)
    (h : a*d-b*c ≠ 0) :
    (!![a,b;c,d])⁻¹ = (a*d-b*c)⁻¹ • !![d,-b;-c,a] := by
  apply Matrix.inv_eq_right_inv
  rw [Matrix.mul_smul, r2_adjugate_two_identity, smul_smul, inv_mul_cancel₀ h, one_smul]

def r2PairIndex : (Fin 2 × Fin 2) ≃ Fin 4 := finProdFinEquiv

def r2PairLift {K : Type*} [CommSemiring K]
    (A : Matrix (Fin 2) (Fin 2) K) : Matrix (Fin 4) (Fin 4) K :=
  (A ⊗ₖ (1 : Matrix (Fin 2) (Fin 2) K)).submatrix r2PairIndex.symm r2PairIndex.symm

theorem r2_pair_lift_mul {K : Type*} [CommSemiring K]
    (A B : Matrix (Fin 2) (Fin 2) K) :
    r2PairLift (A*B) = r2PairLift A * r2PairLift B := by
  unfold r2PairLift
  rw [Matrix.submatrix_mul_equiv, ← Matrix.mul_kronecker_mul, Matrix.one_mul]

theorem r2_pair_lift_one {K : Type*} [CommSemiring K] :
    r2PairLift (1 : Matrix (Fin 2) (Fin 2) K) = 1 := by
  simp [r2PairLift, Matrix.one_kronecker_one, Matrix.submatrix_one_equiv]

theorem r2_pair_lift_two {K : Type*} [CommSemiring K] (a b c d : K) :
    r2PairLift !![a,b;c,d] =
      !![a,0,b,0; 0,a,0,b; c,0,d,0; 0,c,0,d] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [r2PairLift, r2PairIndex, finProdFinEquiv, Fin.divNat, Fin.modNat, Matrix.kroneckerMap,
      Matrix.submatrix_apply, Matrix.one_apply,
      Matrix.cons_val_two, Matrix.cons_val_three, Matrix.cons_val_four,
      Matrix.vecHead, Matrix.vecTail]

def r2FirstIntegerPivot : Matrix (Fin 2) (Fin 2) ℚ := !![98,-25;-25,98]
def r2FirstIntegerAdjugate : Matrix (Fin 2) (Fin 2) ℚ := !![98,25;25,98]

theorem r2_first_integer_determinant : (98 : ℤ)*98 - (-25)*(-25) = 8979 := by
  norm_num

theorem r2_first_integer_adjugate_product :
    r2FirstIntegerPivot * r2FirstIntegerAdjugate =
      (8979 : ℚ) • (1 : Matrix (Fin 2) (Fin 2) ℚ) := by
  have hd : (98 : ℚ)*98 - (-25)*(-25) = 8979 := by
    exact_mod_cast r2_first_integer_determinant
  simpa only [r2FirstIntegerPivot, r2FirstIntegerAdjugate, neg_neg, hd] using
    r2_adjugate_two_identity (98 : ℚ) (-25) (-25) 98

/-- Only this scalar equation needs denominator clearing; matrix products were
already reduced symbolically to the integer adjugate identity. -/
theorem r2_first_denominator_clearing :
    (1/25 : ℚ) * (25/8979) * 8979 = 1 := by
  field_simp <;> norm_num

theorem r2_first_scaled_product :
    ((1/25 : ℚ) • r2FirstIntegerPivot) *
      ((25/8979 : ℚ) • r2FirstIntegerAdjugate) =
      (1 : Matrix (Fin 2) (Fin 2) ℚ) := by
  rw [Matrix.smul_mul, Matrix.mul_smul, r2_first_integer_adjugate_product,
    smul_smul, smul_smul, r2_first_denominator_clearing, one_smul]

theorem r2_first_scaled_pivot_entries :
    (1/25 : ℚ) • r2FirstIntegerPivot = !![98/25,-1;-1,98/25] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [r2FirstIntegerPivot]

theorem r2_first_scaled_adjugate_entries :
    (25/8979 : ℚ) • r2FirstIntegerAdjugate =
      !![2450/8979,625/8979;625/8979,2450/8979] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [r2FirstIntegerAdjugate]

def r2FirstInverseQ : Matrix (Fin 4) (Fin 4) ℚ :=
  !![2450/8979,0,625/8979,0; 0,2450/8979,0,625/8979;
     625/8979,0,2450/8979,0; 0,625/8979,0,2450/8979]

theorem r2_first_pivot_pair_lift :
    r2D ℚ = r2PairLift ((1/25 : ℚ) • r2FirstIntegerPivot) := by
  rw [r2_first_scaled_pivot_entries, r2_pair_lift_two]
  rfl

theorem r2_first_inverse_pair_lift :
    r2FirstInverseQ = r2PairLift ((25/8979 : ℚ) • r2FirstIntegerAdjugate) := by
  rw [r2_first_scaled_adjugate_entries, r2_pair_lift_two]
  rfl

/-- The actual first 4-by-4 inverse multiplication identity. -/
theorem r2_first_inverse_product :
    (r2InitialState ℚ).X * r2FirstInverseQ = 1 := by
  change r2D ℚ * r2FirstInverseQ = 1
  rw [r2_first_pivot_pair_lift, r2_first_inverse_pair_lift,
    ← r2_pair_lift_mul, r2_first_scaled_product, r2_pair_lift_one]

theorem r2_first_actual_inverse : (r2InitialState ℚ).X⁻¹ = r2FirstInverseQ :=
  Matrix.inv_eq_right_inv r2_first_inverse_product

/-- The same closed first-inverse formula for the actual real R2 recurrence. -/
theorem r2_first_actual_real_inverse :
    (r2InitialState ℝ).X⁻¹ = r2RealMatrix r2FirstInverseQ := by
  change (r2D ℝ)⁻¹ = r2RealMatrix r2FirstInverseQ
  rw [← r2_real_D]
  exact r2_real_inverse_of_certificate _ _ r2_first_inverse_product

end TargetA

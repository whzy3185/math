import C029BoundaryIncidenceEstimate
import Mathlib.Analysis.InnerProductSpace.PiL2
import Mathlib.Analysis.Normed.Operator.Basic

/-!
# C029: the actual inner-product/operator-norm cross estimate

This module uses continuous linear maps and their induced operator norms, not
scalar hypotheses that assume the desired cross-form estimate.  Its generic
result applies to all real inner-product spaces, and its matrix specialization
uses the Euclidean (L2) space.  The actual C029 Schur assembly is not identified
here.  The imported seven-theorem scalar module is unchanged.
-/

open scoped BigOperators

noncomputable section

namespace C029InnerProductCross

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- Cauchy-Schwarz followed by the genuine induced operator-norm inequality. -/
theorem abs_inner_apply_le (F : E →L[ℝ] E) (x y : E) :
    |inner ℝ x (F y)| ≤ ‖F‖ * ‖x‖ * ‖y‖ := by
  calc
    |inner ℝ x (F y)| ≤ ‖x‖ * ‖F y‖ := abs_real_inner_le_norm x (F y)
    _ ≤ ‖x‖ * (‖F‖ * ‖y‖) :=
      mul_le_mul_of_nonneg_left (F.le_opNorm y) (norm_nonneg x)
    _ = ‖F‖ * ‖x‖ * ‖y‖ := by rw [← mul_assoc, mul_comm ‖x‖ ‖F‖]

/-- The absolute quadratic cross estimate for a finite permutation of blocks.
The coefficient cap is a bound on actual continuous-linear-map operator norms.
Those norms are nonnegative without any additional hypothesis. -/
theorem permutation_inner_cross_le {ι : Type*} [Fintype ι]
    (σ : Equiv.Perm ι) (F : ι → (E →L[ℝ] E)) (v : ι → E) (M : ℝ)
    (hM : ∀ i, ‖F i‖ ≤ M) :
    |2 * ∑ i, inner ℝ (v i) ((F i) (v (σ i)))| ≤
      2 * M * ∑ i, ‖v i‖ ^ 2 := by
  have hterm (i : ι) :
      |2 * inner ℝ (v i) ((F i) (v (σ i)))| ≤
        2 * ‖F i‖ * ‖v i‖ * ‖v (σ i)‖ := by
    calc
      |2 * inner ℝ (v i) ((F i) (v (σ i)))| =
          2 * |inner ℝ (v i) ((F i) (v (σ i)))| := by
            rw [abs_mul, abs_of_nonneg (show (0 : ℝ) ≤ 2 from zero_le_two)]
      _ ≤ 2 * (‖F i‖ * ‖v i‖ * ‖v (σ i)‖) :=
        mul_le_mul_of_nonneg_left (abs_inner_apply_le (F i) (v i) (v (σ i)))
          (show (0 : ℝ) ≤ 2 from zero_le_two)
      _ = 2 * ‖F i‖ * ‖v i‖ * ‖v (σ i)‖ := by simp only [mul_assoc]
  simpa only [Finset.mul_sum] using
    C029BoundaryIncidence.abs_cross_form_le σ (fun i => ‖F i‖) (fun i => ‖v i‖)
      (fun i => 2 * inner ℝ (v i) ((F i) (v (σ i)))) M
      (fun i => norm_nonneg (F i)) hM hterm

/-- Every cyclic block count is allowed, with the one-cell loop and the two
parallel contributions retained by the same `finRotate` indexing. -/
theorem cyclic_inner_cross_le (r : ℕ) (F : Fin r → (E →L[ℝ] E))
    (v : Fin r → E) (M : ℝ) (hM : ∀ i, ‖F i‖ ≤ M) :
    |2 * ∑ i, inner ℝ (v i) ((F i) (v (finRotate r i)))| ≤
      2 * M * ∑ i, ‖v i‖ ^ 2 :=
  permutation_inner_cross_le (finRotate r) F v M hM

/-- A real square matrix as a continuous linear map on Euclidean space.
Its norm is the induced L2 operator norm, not the default norm on matrix entries. -/
def matrixOperator {n : Type*} [Fintype n] [DecidableEq n]
    (A : Matrix n n ℝ) : EuclideanSpace ℝ n →L[ℝ] EuclideanSpace ℝ n :=
  LinearMap.toContinuousLinearMap (Matrix.toEuclideanLin A)

/-- The Euclidean operator above acts by ordinary matrix-vector multiplication. -/
theorem matrixOperator_apply {n : Type*} [Fintype n] [DecidableEq n]
    (A : Matrix n n ℝ) (v : EuclideanSpace ℝ n) :
    matrixOperator A v = WithLp.toLp 2 (Matrix.mulVec A (WithLp.ofLp v)) := rfl

/-- Literal finite-dimensional matrix version with an explicit induced-norm cap.
For C029 the block dimension is `d = 6`.  This does not assert that any specific
matrices have been obtained by the manuscript's Schur elimination. -/
theorem cyclic_matrix_cross_le (r d : ℕ)
    (A : Fin r → Matrix (Fin d) (Fin d) ℝ)
    (v : Fin r → EuclideanSpace ℝ (Fin d)) (M : ℝ)
    (hM : ∀ i, ‖matrixOperator (A i)‖ ≤ M) :
    |2 * ∑ i, inner ℝ (v i)
      (WithLp.toLp 2 (Matrix.mulVec (A i) (WithLp.ofLp (v (finRotate r i)))))| ≤
        2 * M * ∑ i, ‖v i‖ ^ 2 := by
  simpa only [matrixOperator_apply] using
    cyclic_inner_cross_le r (fun i => matrixOperator (A i)) v M hM

end C029InnerProductCross

#print axioms C029InnerProductCross.abs_inner_apply_le
#print axioms C029InnerProductCross.permutation_inner_cross_le
#print axioms C029InnerProductCross.cyclic_inner_cross_le
#print axioms C029InnerProductCross.matrixOperator
#print axioms C029InnerProductCross.matrixOperator_apply
#print axioms C029InnerProductCross.cyclic_matrix_cross_le

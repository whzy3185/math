import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Logic.Equiv.Fin.Rotate
import Mathlib.Tactic.Linarith

/-!
# C029: degree-two boundary incidence estimate

This is a structural, finite-sum lemma for the cross-term estimate in
`manuscript_v3/sections/06_cells.tex`.  It imports no C029 numerical certificates.
Every outgoing edge is indexed separately, so a one-vertex loop has two endpoint
incidences, and the two directed edges for two vertices are never deduplicated.

The manuscript application is `x i = ||v_i||`, `f i = ||F_i||`, and `M` a common
upper bound for these operator norms.  Matrix assembly, the bound on each actual
matrix cross term, and the passage to an operator-norm bound are separate tasks.
-/

open scoped BigOperators

namespace C029BoundaryIncidence

/-- Weighted arithmetic-geometric mean, with an explicit coefficient cap. -/
theorem weighted_pair_le (f M a b : ℝ) (hf : 0 ≤ f) (hfM : f ≤ M) :
    2 * f * a * b ≤ M * (a ^ 2 + b ^ 2) := by
  calc
    2 * f * a * b ≤ f * (a ^ 2 + b ^ 2) := by
      nlinarith [mul_nonneg hf (sq_nonneg (a - b))]
    _ ≤ M * (a ^ 2 + b ^ 2) :=
      mul_le_mul_of_nonneg_right hfM (add_nonneg (sq_nonneg a) (sq_nonneg b))

/-- A permutation gives one outgoing and one incoming endpoint incidence.
This identity does not require distinct endpoints or distinct unordered edges. -/
theorem sum_squared_endpoint_incidences {ι : Type*} [Fintype ι]
    (σ : Equiv.Perm ι) (x : ι → ℝ) :
    (∑ i, ((x i) ^ 2 + (x (σ i)) ^ 2)) = 2 * ∑ i, (x i) ^ 2 := by
  rw [Finset.sum_add_distrib, Equiv.sum_comp σ (fun i => (x i) ^ 2)]
  exact (two_mul _).symm

/-- Uniform degree-two estimate, independent of the number of indices.
The real values `x` need not be nonnegative; norms are a permitted specialization. -/
theorem permutation_cross_le {ι : Type*} [Fintype ι]
    (σ : Equiv.Perm ι) (f x : ι → ℝ) (M : ℝ)
    (hf : ∀ i, 0 ≤ f i) (hfM : ∀ i, f i ≤ M) :
    (∑ i, 2 * f i * x i * x (σ i)) ≤ 2 * M * ∑ i, (x i) ^ 2 := by
  calc
    (∑ i, 2 * f i * x i * x (σ i))
        ≤ ∑ i, M * ((x i) ^ 2 + (x (σ i)) ^ 2) := by
          exact Finset.sum_le_sum (fun i _ => weighted_pair_le (f i) M
            (x i) (x (σ i)) (hf i) (hfM i))
    _ = M * (∑ i, ((x i) ^ 2 + (x (σ i)) ^ 2)) :=
      (Finset.mul_sum ..).symm
    _ = 2 * M * ∑ i, (x i) ^ 2 := by
      rw [sum_squared_endpoint_incidences σ x]
      rw [← mul_assoc, mul_comm M 2]

/-- Once each actual scalar cross term has the usual norm bound, the entire
signed quadratic cross form has the same dimension-independent estimate. -/
theorem abs_cross_form_le {ι : Type*} [Fintype ι]
    (σ : Equiv.Perm ι) (f x q : ι → ℝ) (M : ℝ)
    (hf : ∀ i, 0 ≤ f i) (hfM : ∀ i, f i ≤ M)
    (hq : ∀ i, |q i| ≤ 2 * f i * x i * x (σ i)) :
    |∑ i, q i| ≤ 2 * M * ∑ i, (x i) ^ 2 := by
  calc
    |∑ i, q i| ≤ ∑ i, |q i| := Finset.abs_sum_le_sum_abs q Finset.univ
    _ ≤ ∑ i, 2 * f i * x i * x (σ i) :=
      Finset.sum_le_sum (fun i _ => hq i)
    _ ≤ 2 * M * ∑ i, (x i) ^ 2 := permutation_cross_le σ f x M hf hfM

/-- Cyclic successor specialization. It holds for every `r`, including `r = 1`
and `r = 2`; the vacuous zero-cell statement also holds. -/
theorem cyclic_cross_le (r : ℕ) (f x : Fin r → ℝ) (M : ℝ)
    (hf : ∀ i, 0 ≤ f i) (hfM : ∀ i, f i ≤ M) :
    (∑ i, 2 * f i * x i * x (finRotate r i)) ≤ 2 * M * ∑ i, (x i) ^ 2 :=
  permutation_cross_le (finRotate r) f x M hf hfM

/-- For one cell the self-loop contributes twice, rather than disappearing. -/
theorem one_cell_loop_expansion (f x : Fin 1 → ℝ) :
    (∑ i, 2 * f i * x i * x (finRotate 1 i)) = 2 * f 0 * (x 0) ^ 2 := by
  simp [pow_two, mul_assoc]

/-- For two cells both directed/parallel edge contributions remain in the sum. -/
theorem two_cell_parallel_expansion (f x : Fin 2 → ℝ) :
    (∑ i, 2 * f i * x i * x (finRotate 2 i)) =
      2 * f 0 * x 0 * x 1 + 2 * f 1 * x 1 * x 0 := by
  simp [Fin.sum_univ_succ]

end C029BoundaryIncidence

#print axioms C029BoundaryIncidence.weighted_pair_le
#print axioms C029BoundaryIncidence.sum_squared_endpoint_incidences
#print axioms C029BoundaryIncidence.permutation_cross_le
#print axioms C029BoundaryIncidence.abs_cross_form_le
#print axioms C029BoundaryIncidence.cyclic_cross_le
#print axioms C029BoundaryIncidence.one_cell_loop_expansion
#print axioms C029BoundaryIncidence.two_cell_parallel_expansion

import C029InnerProductCrossEstimate
import Mathlib.Analysis.InnerProductSpace.Adjoint
import Mathlib.Tactic.Ring

/-!
# C029: additive assembly and strict quadratic positivity

The assembled object is a linear map on ordinary block functions, but every
energy statement is explicitly a sum of the squared norms of the blocks.
The ordinary function-space sup norm is never used as a global L2 norm.

Each indexed edge supplies both its outgoing map and its incoming adjoint.
No simple-graph representation or edge deduplication is used.  Consequently,
the definition retains both loop incidences and both parallel edges.

This proves strict quadratic positivity.  Arbitrary diagonal perturbations
need not be self-adjoint, so no global operator `PosDef` claim is made.
Actual C029 endpoint identification and the certified norm bounds are not
proved here.
-/

open scoped BigOperators

noncomputable section

namespace C029AssembledQuadratic

variable {ι E : Type*} [Fintype ι]
variable [NormedAddCommGroup E] [InnerProductSpace ℝ E] [CompleteSpace E]

/-- Additive block assembly. The edge `j` acts from `σ j` to `j`, while its
adjoint acts from `j` to `σ j`. Real seam signs are absorbed into the maps. -/
def assembledOperator (σ : Equiv.Perm ι) (S : E →L[ℝ] E)
    (D F : ι → (E →L[ℝ] E)) (ω : ι → ℝ) : (ι → E) →ₗ[ℝ] (ι → E) :=
  LinearMap.pi fun i =>
    S.toLinearMap.comp (LinearMap.proj i) +
    (D i).toLinearMap.comp (LinearMap.proj i) -
    (ω i • F i).toLinearMap.comp (LinearMap.proj (σ i)) -
    (ContinuousLinearMap.adjoint (ω (σ.symm i) • F (σ.symm i))).toLinearMap.comp
      (LinearMap.proj (σ.symm i))

omit [Fintype ι] in
theorem assembledOperator_apply (σ : Equiv.Perm ι) (S : E →L[ℝ] E)
    (D F : ι → (E →L[ℝ] E)) (ω : ι → ℝ) (v : ι → E) (i : ι) :
    assembledOperator σ S D F ω v i =
      S (v i) + D i (v i) - (ω i • F i) (v (σ i)) -
      (ContinuousLinearMap.adjoint (ω (σ.symm i) • F (σ.symm i))) (v (σ.symm i)) :=
  rfl

/-- The two endpoint incidences yield exactly twice the signed cross form,
including when a permutation has fixed points or two-cycles. -/
theorem assembled_quadratic_identity (σ : Equiv.Perm ι) (S : E →L[ℝ] E)
    (D F : ι → (E →L[ℝ] E)) (ω : ι → ℝ) (v : ι → E) :
    (∑ i, inner ℝ (v i) (assembledOperator σ S D F ω v i)) =
      (∑ i, inner ℝ (v i) (S (v i))) +
      (∑ i, inner ℝ (v i) (D i (v i))) -
      2 * ∑ i, inner ℝ (v i) ((ω i • F i) (v (σ i))) := by
  have hincoming :
      (∑ i, inner ℝ (v i)
        ((ContinuousLinearMap.adjoint (ω (σ.symm i) • F (σ.symm i)))
          (v (σ.symm i)))) =
      ∑ i, inner ℝ (v i) ((ω i • F i) (v (σ i))) := by
    calc
      _ = ∑ i, inner ℝ (v (σ.symm i))
          ((ω (σ.symm i) • F (σ.symm i)) (v i)) := by
        apply Finset.sum_congr rfl
        intro i _
        rw [ContinuousLinearMap.adjoint_inner_right, real_inner_comm]
      _ = _ := by
        simpa only [Equiv.apply_symm_apply] using
          Equiv.sum_comp σ.symm (fun i => inner ℝ (v i) ((ω i • F i) (v (σ i))))
  simp only [assembledOperator_apply, inner_sub_right, inner_add_right,
    Finset.sum_sub_distrib, Finset.sum_add_distrib]
  rw [hincoming]
  ring

omit [Fintype ι] [CompleteSpace E] in
/-- Signs `+1` and `-1` preserve the genuine induced operator-norm cap. -/
theorem signed_edge_norm_le (F : ι → (E →L[ℝ] E)) (ω : ι → ℝ) (M : ℝ)
    (hω : ∀ i, ω i = 1 ∨ ω i = -1) (hF : ∀ i, ‖F i‖ ≤ M) :
    ∀ i, ‖ω i • F i‖ ≤ M := by
  intro i
  rcases hω i with h | h
  · simpa [h] using hF i
  · simpa [h] using hF i

omit [CompleteSpace E] in
/-- A diagonal operator-norm cap bounds its quadratic contribution from below.
Self-adjointness of the perturbation is not needed for this estimate. -/
theorem diagonal_quadratic_lower (D : E →L[ℝ] E) (δ : ℝ)
    (hD : ‖D‖ ≤ δ) (x : E) :
    -δ * ‖x‖ ^ 2 ≤ inner ℝ x (D x) := by
  have habs : |inner ℝ x (D x)| ≤ δ * ‖x‖ ^ 2 := by
    calc
      |inner ℝ x (D x)| ≤ ‖D‖ * ‖x‖ * ‖x‖ :=
        C029InnerProductCross.abs_inner_apply_le D x x
      _ ≤ δ * ‖x‖ * ‖x‖ :=
        mul_le_mul_of_nonneg_right
          (mul_le_mul_of_nonneg_right hD (norm_nonneg x)) (norm_nonneg x)
      _ = δ * ‖x‖ ^ 2 := by ring
  simpa only [neg_mul] using neg_le_of_abs_le habs

/-- Uniform lower bound for the explicitly assembled quadratic form.
The block count contributes no extra multiplicative error. -/
theorem assembled_quadratic_lower_bound (σ : Equiv.Perm ι) (S : E →L[ℝ] E)
    (D F : ι → (E →L[ℝ] E)) (ω : ι → ℝ) (γ δ M : ℝ)
    (hS : ∀ x, γ * ‖x‖ ^ 2 ≤ inner ℝ x (S x))
    (hD : ∀ i, ‖D i‖ ≤ δ) (hF : ∀ i, ‖F i‖ ≤ M)
    (hω : ∀ i, ω i = 1 ∨ ω i = -1) (v : ι → E) :
    (γ - δ - 2 * M) * (∑ i, ‖v i‖ ^ 2) ≤
      ∑ i, inner ℝ (v i) (assembledOperator σ S D F ω v i) := by
  have hcore : γ * (∑ i, ‖v i‖ ^ 2) ≤ ∑ i, inner ℝ (v i) (S (v i)) := by
    rw [Finset.mul_sum]
    exact Finset.sum_le_sum (fun i _ => hS (v i))
  have hdiag : -δ * (∑ i, ‖v i‖ ^ 2) ≤ ∑ i, inner ℝ (v i) (D i (v i)) := by
    rw [Finset.mul_sum]
    exact Finset.sum_le_sum (fun i _ => diagonal_quadratic_lower (D i) δ (hD i) (v i))
  have hcross := C029InnerProductCross.permutation_inner_cross_le σ
    (fun i => ω i • F i) v M (signed_edge_norm_le F ω M hω hF)
  have hcross_upper := (le_abs_self _).trans hcross
  rw [assembled_quadratic_identity]
  nlinarith

omit [InnerProductSpace ℝ E] [CompleteSpace E] in
/-- A nonzero block vector has positive explicit L2 energy. This does not use
the default norm of the ordinary function space. -/
theorem block_energy_pos (v : ι → E) (hv : v ≠ 0) : 0 < ∑ i, ‖v i‖ ^ 2 := by
  classical
  have hex : ∃ i, v i ≠ 0 := by
    by_contra h
    apply hv
    funext i
    simpa using (not_exists.mp h i)
  obtain ⟨i, hi⟩ := hex
  have hpos : 0 < ‖v i‖ ^ 2 := sq_pos_of_pos (norm_pos_iff.mpr hi)
  exact hpos.trans_le (Finset.single_le_sum (fun j _ => sq_nonneg ‖v j‖) (Finset.mem_univ i))

/-- Strict quadratic positivity for every nonzero block vector. This stronger
version needs only the common core's stated quadratic lower bound. -/
theorem assembled_strict_quadratic_pos (σ : Equiv.Perm ι) (S : E →L[ℝ] E)
    (D F : ι → (E →L[ℝ] E)) (ω : ι → ℝ) (γ δ M : ℝ)
    (hS : ∀ x, γ * ‖x‖ ^ 2 ≤ inner ℝ x (S x))
    (hD : ∀ i, ‖D i‖ ≤ δ) (hF : ∀ i, ‖F i‖ ≤ M)
    (hω : ∀ i, ω i = 1 ∨ ω i = -1) (hmargin : δ + 2 * M < γ)
    (v : ι → E) (hv : v ≠ 0) :
    0 < ∑ i, inner ℝ (v i) (assembledOperator σ S D F ω v i) := by
  have hcoeff : 0 < γ - δ - 2 * M := by linarith
  exact (mul_pos hcoeff (block_energy_pos v hv)).trans_le
    (assembled_quadratic_lower_bound σ S D F ω γ δ M hS hD hF hω v)

/-- Requested cyclic self-adjoint-common-core specialization. The diagonal
perturbations need not be self-adjoint, so the conclusion remains explicitly
strict quadratic positivity rather than a self-adjoint operator `PosDef` claim. -/
theorem cyclic_selfAdjoint_core_strict_quadratic_pos (r : ℕ)
    (S : {T : E →L[ℝ] E // IsSelfAdjoint T})
    (D F : Fin r → (E →L[ℝ] E)) (ω : Fin r → ℝ) (γ δ M : ℝ)
    (hS : ∀ x, γ * ‖x‖ ^ 2 ≤ inner ℝ x (S.val x))
    (hD : ∀ i, ‖D i‖ ≤ δ) (hF : ∀ i, ‖F i‖ ≤ M)
    (hω : ∀ i, ω i = 1 ∨ ω i = -1) (hmargin : δ + 2 * M < γ)
    (v : Fin r → E) (hv : v ≠ 0) :
    0 < ∑ i, inner ℝ (v i) (assembledOperator (finRotate r) S.val D F ω v i) :=
  assembled_strict_quadratic_pos (finRotate r) S.val D F ω γ δ M hS hD hF hω hmargin v hv

end C029AssembledQuadratic

#print axioms C029AssembledQuadratic.assembledOperator
#print axioms C029AssembledQuadratic.assembledOperator_apply
#print axioms C029AssembledQuadratic.assembled_quadratic_identity
#print axioms C029AssembledQuadratic.signed_edge_norm_le
#print axioms C029AssembledQuadratic.diagonal_quadratic_lower
#print axioms C029AssembledQuadratic.assembled_quadratic_lower_bound
#print axioms C029AssembledQuadratic.block_energy_pos
#print axioms C029AssembledQuadratic.assembled_strict_quadratic_pos
#print axioms C029AssembledQuadratic.cyclic_selfAdjoint_core_strict_quadratic_pos

import C029AssembledQuadraticPositivity
import Mathlib.Analysis.Matrix.Hermitian
import Mathlib.LinearAlgebra.Matrix.PosDef

/-!
# C029: L2 flattening and positive-definite assembled matrices

The existing additive boundary operator is lifted to `PiLp 2` and represented
in the product-indexed orthonormal basis.  Both its quadratic-form identity and
its symmetry are proved.  Matrix positive definiteness is conditional on the
local core lower bound, induced operator-norm caps, real unit seam signs, and
self-adjointness of both the core and each diagonal perturbation.

There is no simple-graph deduplication, global operator-norm claim, or assertion
that actual C029 endpoint matrices/certificates have been identified.
-/

open scoped BigOperators

noncomputable section

namespace C029FlattenedMatrix

open C029AssembledQuadratic

section HilbertBlocks

variable {ι E : Type*} [Fintype ι]
variable [NormedAddCommGroup E] [InnerProductSpace ℝ E] [CompleteSpace E]

/-- The additive block operator conjugated by the L2 type-tag equivalence.
Only the linear structure is transported; the target carries its genuine L2 norm. -/
def l2Operator (σ : Equiv.Perm ι) (S : E →L[ℝ] E)
    (D F : ι → (E →L[ℝ] E)) (ω : ι → ℝ) :
    PiLp 2 (fun _ : ι => E) →ₗ[ℝ] PiLp 2 (fun _ : ι => E) :=
  (WithLp.linearEquiv 2 ℝ (ι → E)).symm.toLinearMap.comp
    ((assembledOperator σ S D F ω).comp
      (WithLp.linearEquiv 2 ℝ (ι → E)).toLinearMap)

omit [Fintype ι] in
theorem l2Operator_apply (σ : Equiv.Perm ι) (S : E →L[ℝ] E)
    (D F : ι → (E →L[ℝ] E)) (ω : ι → ℝ)
    (v : PiLp 2 (fun _ : ι => E)) (i : ι) :
    l2Operator σ S D F ω v i = assembledOperator σ S D F ω (WithLp.ofLp v) i := rfl

/-- Incoming adjoints reindex to the second outgoing bilinear contribution. -/
theorem assembled_bilinear_identity (σ : Equiv.Perm ι) (S : E →L[ℝ] E)
    (D F : ι → (E →L[ℝ] E)) (ω : ι → ℝ) (x y : ι → E) :
    (∑ i, inner ℝ (x i) (assembledOperator σ S D F ω y i)) =
      (∑ i, inner ℝ (x i) (S (y i))) +
      (∑ i, inner ℝ (x i) (D i (y i))) -
      (∑ i, inner ℝ (x i) ((ω i • F i) (y (σ i)))) -
      (∑ i, inner ℝ (y i) ((ω i • F i) (x (σ i)))) := by
  have hincoming :
      (∑ i, inner ℝ (x i)
        ((ContinuousLinearMap.adjoint (ω (σ.symm i) • F (σ.symm i)))
          (y (σ.symm i)))) =
      ∑ i, inner ℝ (y i) ((ω i • F i) (x (σ i))) := by
    calc
      _ = ∑ i, inner ℝ (y (σ.symm i))
          ((ω (σ.symm i) • F (σ.symm i)) (x i)) := by
        apply Finset.sum_congr rfl
        intro i _
        rw [ContinuousLinearMap.adjoint_inner_right, real_inner_comm]
      _ = _ := by
        simpa only [Equiv.apply_symm_apply] using
          Equiv.sum_comp σ.symm (fun i => inner ℝ (y i) ((ω i • F i) (x (σ i))))
  simp only [assembledOperator_apply, inner_sub_right, inner_add_right,
    Finset.sum_sub_distrib, Finset.sum_add_distrib]
  rw [hincoming]

/-- Actual symmetry of the bilinear block pairing, using both diagonal
self-adjointness hypotheses. No symmetry hypothesis on the assembled object is assumed. -/
theorem assembled_pairing_symmetric (σ : Equiv.Perm ι) (S : E →L[ℝ] E)
    (D F : ι → (E →L[ℝ] E)) (ω : ι → ℝ)
    (hS : IsSelfAdjoint S) (hD : ∀ i, IsSelfAdjoint (D i)) (x y : ι → E) :
    (∑ i, inner ℝ (x i) (assembledOperator σ S D F ω y i)) =
      ∑ i, inner ℝ (y i) (assembledOperator σ S D F ω x i) := by
  have hcore : (∑ i, inner ℝ (x i) (S (y i))) =
      ∑ i, inner ℝ (y i) (S (x i)) := by
    apply Finset.sum_congr rfl
    intro i _
    exact (hS.isSymmetric (x i) (y i)).symm.trans (real_inner_comm (y i) (S (x i)))
  have hdiag : (∑ i, inner ℝ (x i) (D i (y i))) =
      ∑ i, inner ℝ (y i) (D i (x i)) := by
    apply Finset.sum_congr rfl
    intro i _
    exact ((hD i).isSymmetric (x i) (y i)).symm.trans
      (real_inner_comm (y i) (D i (x i)))
  rw [assembled_bilinear_identity, assembled_bilinear_identity, hcore, hdiag]
  ring

/-- Symmetry for the correct block L2 inner product. -/
theorem l2Operator_isSymmetric (σ : Equiv.Perm ι) (S : E →L[ℝ] E)
    (D F : ι → (E →L[ℝ] E)) (ω : ι → ℝ)
    (hS : IsSelfAdjoint S) (hD : ∀ i, IsSelfAdjoint (D i)) :
    (l2Operator σ S D F ω).IsSymmetric := by
  intro x y
  rw [real_inner_comm]
  change (∑ i, inner ℝ (y i) (assembledOperator σ S D F ω (WithLp.ofLp x) i)) =
    ∑ i, inner ℝ (x i) (assembledOperator σ S D F ω (WithLp.ofLp y) i)
  exact assembled_pairing_symmetric σ S D F ω hS hD (WithLp.ofLp y) (WithLp.ofLp x)

end HilbertBlocks

section EuclideanBlocks

variable {ι κ : Type*} [Fintype ι] [Fintype κ] [DecidableEq ι] [DecidableEq κ]

abbrev BlockSpace (ι κ : Type*) [Fintype ι] [Fintype κ] :=
  PiLp 2 (fun _ : ι => EuclideanSpace ℝ κ)

/-- Standard blockwise orthonormal coordinates, flattened with product indices. -/
def blockBasis : OrthonormalBasis (ι × κ) ℝ (BlockSpace ι κ) :=
  (Pi.orthonormalBasis (fun _ : ι => EuclideanSpace.basisFun κ ℝ)).reindex
    (Equiv.sigmaEquivProd ι κ)

omit [DecidableEq ι] [DecidableEq κ] in
/-- The isometric flattening uses coordinate `(i,a)` for coordinate `a` in block `i`. -/
theorem blockBasis_repr_apply (v : BlockSpace ι κ) (i : ι) (a : κ) :
    blockBasis.repr v (i, a) = v i a := rfl

omit [DecidableEq ι] [DecidableEq κ] in
/-- This is an L2 flattening, not the ordinary function-space sup norm. -/
theorem flatten_norm_sq (v : BlockSpace ι κ) :
    ‖blockBasis.repr v‖ ^ 2 = ∑ i, ‖v i‖ ^ 2 := by
  rw [LinearIsometryEquiv.norm_map]
  exact PiLp.norm_sq_eq_of_L2 _ v

/-- Matrix representation of the already-defined additive operator.
Every overlapping outgoing/incoming contribution is inherited additively. -/
def assembledMatrix (σ : Equiv.Perm ι)
    (S : EuclideanSpace ℝ κ →L[ℝ] EuclideanSpace ℝ κ)
    (D F : ι → (EuclideanSpace ℝ κ →L[ℝ] EuclideanSpace ℝ κ)) (ω : ι → ℝ) :
    Matrix (ι × κ) (ι × κ) ℝ :=
  (l2Operator σ S D F ω).toMatrix blockBasis.toBasis blockBasis.toBasis

/-- Verified matrix-vector action in the flattened orthonormal coordinates. -/
theorem assembledMatrix_mulVec_repr (σ : Equiv.Perm ι)
    (S : EuclideanSpace ℝ κ →L[ℝ] EuclideanSpace ℝ κ)
    (D F : ι → (EuclideanSpace ℝ κ →L[ℝ] EuclideanSpace ℝ κ)) (ω : ι → ℝ)
    (v : BlockSpace ι κ) :
    Matrix.mulVec (assembledMatrix σ S D F ω) (WithLp.ofLp (blockBasis.repr v)) =
      WithLp.ofLp (blockBasis.repr (l2Operator σ S D F ω v)) := by
  ext a
  have h := congrFun ((l2Operator σ S D F ω).toMatrix_mulVec_repr
    blockBasis.toBasis blockBasis.toBasis v) a
  simpa only [assembledMatrix, Matrix.mulVec, dotProduct,
    OrthonormalBasis.coe_toBasis_repr_apply] using h

/-- The actual matrix quadratic form equals the previously checked block sum. -/
theorem assembledMatrix_quadratic_eq (σ : Equiv.Perm ι)
    (S : EuclideanSpace ℝ κ →L[ℝ] EuclideanSpace ℝ κ)
    (D F : ι → (EuclideanSpace ℝ κ →L[ℝ] EuclideanSpace ℝ κ)) (ω : ι → ℝ)
    (v : BlockSpace ι κ) :
    dotProduct (star (WithLp.ofLp (blockBasis.repr v)))
      (Matrix.mulVec (assembledMatrix σ S D F ω) (WithLp.ofLp (blockBasis.repr v))) =
      ∑ i, inner ℝ (v i) (assembledOperator σ S D F ω (WithLp.ofLp v) i) := by
  rw [assembledMatrix_mulVec_repr]
  calc
    _ = inner ℝ (blockBasis.repr v) (blockBasis.repr (l2Operator σ S D F ω v)) := by
      rw [EuclideanSpace.inner_eq_star_dotProduct, dotProduct_comm]
    _ = inner ℝ v (l2Operator σ S D F ω v) :=
      blockBasis.repr.inner_map_map v (l2Operator σ S D F ω v)
    _ = _ := rfl

/-- Real-matrix Hermitian symmetry is derived from the core/diagonal hypotheses. -/
theorem assembledMatrix_isHermitian (σ : Equiv.Perm ι)
    (S : EuclideanSpace ℝ κ →L[ℝ] EuclideanSpace ℝ κ)
    (D F : ι → (EuclideanSpace ℝ κ →L[ℝ] EuclideanSpace ℝ κ)) (ω : ι → ℝ)
    (hS : IsSelfAdjoint S) (hD : ∀ i, IsSelfAdjoint (D i)) :
    (assembledMatrix σ S D F ω).IsHermitian := by
  apply (LinearMap.isHermitian_toMatrix_iff blockBasis).mpr
  exact l2Operator_isSymmetric σ S D F ω hS hD

/-- Conditional generic positive definiteness of the actual flattened matrix. -/
theorem assembledMatrix_posDef (σ : Equiv.Perm ι)
    (S : EuclideanSpace ℝ κ →L[ℝ] EuclideanSpace ℝ κ)
    (D F : ι → (EuclideanSpace ℝ κ →L[ℝ] EuclideanSpace ℝ κ)) (ω : ι → ℝ)
    (γ δ M : ℝ) (hSself : IsSelfAdjoint S) (hDself : ∀ i, IsSelfAdjoint (D i))
    (hS : ∀ x, γ * ‖x‖ ^ 2 ≤ inner ℝ x (S x))
    (hD : ∀ i, ‖D i‖ ≤ δ) (hF : ∀ i, ‖F i‖ ≤ M)
    (hω : ∀ i, ω i = 1 ∨ ω i = -1) (hmargin : δ + 2 * M < γ) :
    (assembledMatrix σ S D F ω).PosDef := by
  apply Matrix.PosDef.of_dotProduct_mulVec_pos
    (assembledMatrix_isHermitian σ S D F ω hSself hDself)
  intro x hx
  let v : BlockSpace ι κ := blockBasis.repr.symm (WithLp.toLp 2 x)
  have hrepr : WithLp.ofLp (blockBasis.repr v) = x := by simp [v]
  have hv : WithLp.ofLp v ≠ 0 := by
    intro h
    have hv0 : v = 0 := (WithLp.ofLp_eq_zero 2).mp h
    apply hx
    rw [← hrepr, hv0]
    simp
  have hpos := assembled_strict_quadratic_pos σ S D F ω γ δ M hS hD hF hω hmargin
    (WithLp.ofLp v) hv
  rw [← assembledMatrix_quadratic_eq σ S D F ω v, hrepr] at hpos
  exact hpos

end EuclideanBlocks

/-- The requested matrix on the finite flattened index type `Fin r × Fin n`. -/
theorem cyclic_assembledMatrix_posDef (r n : ℕ)
    (S : EuclideanSpace ℝ (Fin n) →L[ℝ] EuclideanSpace ℝ (Fin n))
    (D F : Fin r → (EuclideanSpace ℝ (Fin n) →L[ℝ] EuclideanSpace ℝ (Fin n)))
    (ω : Fin r → ℝ) (γ δ M : ℝ)
    (hSself : IsSelfAdjoint S) (hDself : ∀ i, IsSelfAdjoint (D i))
    (hS : ∀ x, γ * ‖x‖ ^ 2 ≤ inner ℝ x (S x))
    (hD : ∀ i, ‖D i‖ ≤ δ) (hF : ∀ i, ‖F i‖ ≤ M)
    (hω : ∀ i, ω i = 1 ∨ ω i = -1) (hmargin : δ + 2 * M < γ) :
    (assembledMatrix (finRotate r) S D F ω).PosDef :=
  assembledMatrix_posDef (finRotate r) S D F ω γ δ M hSself hDself hS hD hF hω hmargin

end C029FlattenedMatrix

#print axioms C029FlattenedMatrix.l2Operator
#print axioms C029FlattenedMatrix.l2Operator_apply
#print axioms C029FlattenedMatrix.assembled_bilinear_identity
#print axioms C029FlattenedMatrix.assembled_pairing_symmetric
#print axioms C029FlattenedMatrix.l2Operator_isSymmetric
#print axioms C029FlattenedMatrix.BlockSpace
#print axioms C029FlattenedMatrix.blockBasis
#print axioms C029FlattenedMatrix.blockBasis_repr_apply
#print axioms C029FlattenedMatrix.flatten_norm_sq
#print axioms C029FlattenedMatrix.assembledMatrix
#print axioms C029FlattenedMatrix.assembledMatrix_mulVec_repr
#print axioms C029FlattenedMatrix.assembledMatrix_quadratic_eq
#print axioms C029FlattenedMatrix.assembledMatrix_isHermitian
#print axioms C029FlattenedMatrix.assembledMatrix_posDef
#print axioms C029FlattenedMatrix.cyclic_assembledMatrix_posDef

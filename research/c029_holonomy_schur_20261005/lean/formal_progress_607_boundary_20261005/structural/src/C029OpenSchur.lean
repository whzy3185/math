import Mathlib.Analysis.Matrix.Order
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.Data.Matrix.ColumnRowPartitioned
import Mathlib.Logic.Equiv.Fin.Basic

namespace C029OpenSchur
open scoped Matrix
set_option maxHeartbeats 300000
set_option linter.unusedSimpArgs false

/-- Independent generic state; no identification with TargetA.R2RecurrenceState
is asserted in this module. The typed project bridge is a separate obligation. -/
structure OpenState where
  X : Matrix (Fin 4) (Fin 4) ℝ
  R : Matrix (Fin 2) (Fin 4) ℝ
  W : Matrix (Fin 4) (Fin 4) ℝ
  G : Matrix (Fin 2) (Fin 2) ℝ
  H : Matrix (Fin 4) (Fin 4) ℝ
  C : Matrix (Fin 2) (Fin 4) ℝ

theorem posDef_submatrix_equiv {m n : Type*} [Fintype m] [Fintype n]
    [DecidableEq m] [DecidableEq n] (A : Matrix n n ℝ) (e : m ≃ n) :
    (A.submatrix e e).PosDef ↔ A.PosDef := by
  have hp : (A.submatrix e e).PosSemidef ↔ A.PosSemidef :=
    Matrix.posSemidef_submatrix_equiv e
  have hu : IsUnit (A.submatrix e e) ↔ IsUnit A := by
    simp only [Matrix.isUnit_iff_isUnit_det, Matrix.det_submatrix_equiv_self]
  constructor
  · intro h
    exact (hp.mp h.posSemidef).posDef_iff_isUnit.mpr (hu.mp h.isUnit)
  · intro h
    exact (hp.mpr h.posSemidef).posDef_iff_isUnit.mpr (hu.mpr h.isUnit)

/-- Strict Schur positivity over the reals, derived from Mathlib's semidefinite and
invertibility criteria, without a new positivity assumption on the retained block. -/
theorem strict_schur_criterion {m n : Type*} [Fintype m] [Fintype n]
    [DecidableEq m] [DecidableEq n] (X : Matrix n n ℝ)
    (T : Matrix m n ℝ) (B : Matrix m m ℝ) (hX : X.PosDef) :
    (Matrix.fromBlocks X Tᵀ T B).PosDef ↔ (B - T * X⁻¹ * Tᵀ).PosDef := by
  letI : Invertible X := hX.isUnit.invertible
  have hp : (Matrix.fromBlocks X Tᵀ T B).PosSemidef ↔
      (B - T * X⁻¹ * Tᵀ).PosSemidef := by
    simpa only [Matrix.conjTranspose_eq_transpose_of_trivial, Matrix.transpose_transpose] using
      Matrix.PosDef.fromBlocks₁₁ Tᵀ B hX
  have hu : IsUnit (Matrix.fromBlocks X Tᵀ T B) ↔ IsUnit (B - T * X⁻¹ * Tᵀ) := by
    simpa only [Matrix.invOf_eq_nonsing_inv] using
      (Matrix.isUnit_fromBlocks_iff_of_invertible₁₁ (A := X) (B := Tᵀ) (C := T) (D := B))
  constructor
  · intro h
    exact (hp.mp h.posSemidef).posDef_iff_isUnit.mpr (hu.mp h.isUnit)
  · intro h
    exact (hp.mpr h.posSemidef).posDef_iff_isUnit.mpr (hu.mpr h.isUnit)

abbrev OpenRetained := Fin 2 ⊕ (Fin 4 ⊕ Fin 4)

def openRetainedIndex : OpenRetained ≃ Fin 10 :=
  (Equiv.sumCongr (Equiv.refl (Fin 2))
    (finSumFinEquiv : Fin 4 ⊕ Fin 4 ≃ Fin 8)).trans
      (finSumFinEquiv : Fin 2 ⊕ Fin 8 ≃ Fin 10)

def openFullIndex : (Fin 4 ⊕ Fin 10) ≃ Fin 14 := finSumFinEquiv

/-- The six open updates with an arbitrary bulk diagonal and coupling. -/
def openUpdateWithInverse (D E : Matrix (Fin 4) (Fin 4) ℝ)
    (s : OpenState) (Y : Matrix (Fin 4) (Fin 4) ℝ) :
    OpenState where
  X := D - Eᵀ * Y * E
  R := -s.R * Y * E
  W := -Eᵀ * Y * s.W
  G := s.G - s.R * Y * s.Rᵀ
  H := s.H - s.Wᵀ * Y * s.W
  C := s.C - s.R * Y * s.W

/-- Before eliminating the current pivot: head pair, next pivot, retained tail. -/
def openBoundarySum (D : Matrix (Fin 4) (Fin 4) ℝ)
    (s : OpenState) : Matrix OpenRetained OpenRetained ℝ :=
  Matrix.fromBlocks s.G (Matrix.fromCols 0 s.C) (Matrix.fromRows 0 s.Cᵀ)
    (Matrix.fromBlocks D 0 0 s.H)

def openCouplingSum (E : Matrix (Fin 4) (Fin 4) ℝ)
    (s : OpenState) : Matrix OpenRetained (Fin 4) ℝ :=
  Matrix.fromRows s.R (Matrix.fromRows Eᵀ s.Wᵀ)

/-- The updated state retains all three off-diagonal block pairs. -/
def openPackedSum (s : OpenState) :
    Matrix OpenRetained OpenRetained ℝ :=
  Matrix.fromBlocks s.G (Matrix.fromCols s.R s.C) (Matrix.fromRows s.Rᵀ s.Cᵀ)
    (Matrix.fromBlocks s.X s.W s.Wᵀ s.H)

def openBoundary (D : Matrix (Fin 4) (Fin 4) ℝ)
    (s : OpenState) : Matrix (Fin 10) (Fin 10) ℝ :=
  (openBoundarySum D s).submatrix openRetainedIndex.symm openRetainedIndex.symm

def openCoupling (E : Matrix (Fin 4) (Fin 4) ℝ)
    (s : OpenState) : Matrix (Fin 10) (Fin 4) ℝ :=
  (openCouplingSum E s).submatrix openRetainedIndex.symm id

def openPacked (s : OpenState) : Matrix (Fin 10) (Fin 10) ℝ :=
  (openPackedSum s).submatrix openRetainedIndex.symm openRetainedIndex.symm

noncomputable def openSchurCore (D E : Matrix (Fin 4) (Fin 4) ℝ)
    (s : OpenState) : Matrix (Fin 10) (Fin 10) ℝ :=
  openBoundary D s - openCoupling E s * s.X⁻¹ * (openCoupling E s)ᵀ

/-- Explicit pivot-first fourteen-dimensional local system. -/
def openMatrix (D E : Matrix (Fin 4) (Fin 4) ℝ)
    (s : OpenState) : Matrix (Fin 14) (Fin 14) ℝ :=
  (Matrix.fromBlocks s.X (openCoupling E s)ᵀ
    (openCoupling E s) (openBoundary D s)).submatrix
      openFullIndex.symm openFullIndex.symm

/-- Pure block algebra; the supplied inverse-shaped matrix is explicitly symmetric. -/
theorem open_sum_schur_eq_update (D E : Matrix (Fin 4) (Fin 4) ℝ)
    (s : OpenState) (Y : Matrix (Fin 4) (Fin 4) ℝ) (hY : Yᵀ = Y) :
    openBoundarySum D s - openCouplingSum E s * Y * (openCouplingSum E s)ᵀ =
      openPackedSum (openUpdateWithInverse D E s Y) := by
  unfold openBoundarySum openCouplingSum openPackedSum openUpdateWithInverse
  simp only [Matrix.transpose_fromRows, Matrix.transpose_transpose,
    Matrix.fromRows_mul, Matrix.mul_fromCols]
  ext i j
  rcases i with i | (i | i) <;> rcases j with j | (j | j)
  all_goals
    simp [Matrix.fromBlocks, Matrix.fromRows, Matrix.fromCols, Matrix.sub_apply,
      Matrix.transpose_sub, Matrix.transpose_mul, Matrix.transpose_neg, hY,
      Matrix.neg_mul, Matrix.mul_neg, Matrix.mul_assoc, Matrix.of_apply, Sum.elim]

/-- A positive current pivot supplies the genuine inverse and its symmetry. -/
theorem open_schur_eq_update (D E : Matrix (Fin 4) (Fin 4) ℝ)
    (s : OpenState) (hX : s.X.PosDef) :
    openSchurCore D E s =
      openPacked (openUpdateWithInverse D E s s.X⁻¹) := by
  have hY : (s.X⁻¹)ᵀ = s.X⁻¹ := by
    simpa only [Matrix.conjTranspose_eq_transpose_of_trivial] using hX.isHermitian.inv.eq
  have hp : openCoupling E s * s.X⁻¹ * (openCoupling E s)ᵀ =
      (openCouplingSum E s * s.X⁻¹ * (openCouplingSum E s)ᵀ).submatrix
        openRetainedIndex.symm openRetainedIndex.symm := by
    ext i j
    rfl
  unfold openSchurCore
  rw [hp]
  change (openBoundarySum D s -
      openCouplingSum E s * s.X⁻¹ * (openCouplingSum E s)ᵀ).submatrix
        openRetainedIndex.symm openRetainedIndex.symm = _
  exact congrArg (fun A => A.submatrix openRetainedIndex.symm openRetainedIndex.symm)
    (open_sum_schur_eq_update D E s s.X⁻¹ hY)

/-- Strict positivity of the fourteen-dimensional system is exactly positivity
of the updated ten-dimensional packed state, assuming the positive pivot. -/
theorem open_posDef_iff (D E : Matrix (Fin 4) (Fin 4) ℝ)
    (s : OpenState) (hX : s.X.PosDef) :
    (openMatrix D E s).PosDef ↔
      (openPacked (openUpdateWithInverse D E s s.X⁻¹)).PosDef := by
  unfold openMatrix
  rw [posDef_submatrix_equiv]
  rw [strict_schur_criterion s.X (openCoupling E s) (openBoundary D s) hX]
  change (openSchurCore D E s).PosDef ↔ _
  rw [open_schur_eq_update D E s hX]


#print axioms posDef_submatrix_equiv
#print axioms strict_schur_criterion
#print axioms open_sum_schur_eq_update
#print axioms open_schur_eq_update
#print axioms open_posDef_iff
end C029OpenSchur

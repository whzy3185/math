import Mathlib.Analysis.Matrix.Order
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.Data.Matrix.ColumnRowPartitioned
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Logic.Equiv.Fin.Basic
import Mathlib.Tactic.Abel

namespace TargetA

open scoped Matrix

/-- Canonical retained order: the two head sites followed by the four terminal sites. -/
def r2BoundaryIndex : (Fin 2 ⊕ Fin 4) ≃ Fin 6 := finSumFinEquiv

/-- Pivot-first order of the terminal ten-dimensional matrix. -/
def r2TerminalIndex : (Fin 4 ⊕ Fin 6) ≃ Fin 10 := finSumFinEquiv

def r2EPlus : Matrix (Fin 4) (Fin 4) ℝ :=
  !![-1, 0, 0, 0; 0, 1, 0, 0; -1, 2, 1, 0; 2, -1, 0, -1]

def r2BoundaryMatrix (G : Matrix (Fin 2) (Fin 2) ℝ)
    (C : Matrix (Fin 2) (Fin 4) ℝ) (H : Matrix (Fin 4) (Fin 4) ℝ) :
    Matrix (Fin 6) (Fin 6) ℝ :=
  (Matrix.fromBlocks G C Cᵀ H).submatrix r2BoundaryIndex.symm r2BoundaryIndex.symm

/-- The physical last edge is added to the propagated response before elimination. -/
def r2TerminalCoupling (R : Matrix (Fin 2) (Fin 4) ℝ)
    (W E : Matrix (Fin 4) (Fin 4) ℝ) : Matrix (Fin 6) (Fin 4) ℝ :=
  (Matrix.fromRows R (W + E)ᵀ).submatrix r2BoundaryIndex.symm id

noncomputable def r2TerminalCore (X : Matrix (Fin 4) (Fin 4) ℝ)
    (G : Matrix (Fin 2) (Fin 2) ℝ) (C R : Matrix (Fin 2) (Fin 4) ℝ)
    (H W E : Matrix (Fin 4) (Fin 4) ℝ) : Matrix (Fin 6) (Fin 6) ℝ :=
  r2BoundaryMatrix G C H -
    r2TerminalCoupling R W E * X⁻¹ * (r2TerminalCoupling R W E)ᵀ

def r2TerminalMatrix (X : Matrix (Fin 4) (Fin 4) ℝ)
    (G : Matrix (Fin 2) (Fin 2) ℝ) (C R : Matrix (Fin 2) (Fin 4) ℝ)
    (H W E : Matrix (Fin 4) (Fin 4) ℝ) : Matrix (Fin 10) (Fin 10) ℝ :=
  (Matrix.fromBlocks X (r2TerminalCoupling R W E)ᵀ
    (r2TerminalCoupling R W E) (r2BoundaryMatrix G C H)).submatrix
      r2TerminalIndex.symm r2TerminalIndex.symm

/-- Positivity is unchanged by an explicit finite coordinate permutation. -/
theorem r2_posDef_submatrix_equiv {m n : Type*} [Fintype m] [Fintype n]
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
theorem r2_strict_schur_criterion {m n : Type*} [Fintype m] [Fintype n]
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

/-- Actual R2 dimensions: a positive four-dimensional pivot reduces the terminal
10-by-10 problem exactly to its retained 6-by-6 core. -/
theorem r2_terminal_posDef_iff (X : Matrix (Fin 4) (Fin 4) ℝ)
    (G : Matrix (Fin 2) (Fin 2) ℝ) (C R : Matrix (Fin 2) (Fin 4) ℝ)
    (H W E : Matrix (Fin 4) (Fin 4) ℝ) (hX : X.PosDef) :
    (r2TerminalMatrix X G C R H W E).PosDef ↔
      (r2TerminalCore X G C R H W E).PosDef := by
  unfold r2TerminalMatrix
  rw [r2_posDef_submatrix_equiv]
  exact r2_strict_schur_criterion X (r2TerminalCoupling R W E) (r2BoundaryMatrix G C H) hX

/-- Full terminal block expansion, including the off-diagonal correction. -/
theorem r2_terminal_core_blocks (X : Matrix (Fin 4) (Fin 4) ℝ)
    (G : Matrix (Fin 2) (Fin 2) ℝ) (C R : Matrix (Fin 2) (Fin 4) ℝ)
    (H W E : Matrix (Fin 4) (Fin 4) ℝ) :
    r2TerminalCore X G C R H W E =
      (Matrix.fromBlocks
        (G - R * X⁻¹ * Rᵀ)
        (C - R * X⁻¹ * (W + E))
        (Cᵀ - (W + E)ᵀ * X⁻¹ * Rᵀ)
        (H - (W + E)ᵀ * X⁻¹ * (W + E))).submatrix
          r2BoundaryIndex.symm r2BoundaryIndex.symm := by
  have hp : r2TerminalCoupling R W E * X⁻¹ * (r2TerminalCoupling R W E)ᵀ =
      (Matrix.fromRows R (W + E)ᵀ * X⁻¹ * (Matrix.fromRows R (W + E)ᵀ)ᵀ).submatrix
        r2BoundaryIndex.symm r2BoundaryIndex.symm := by
    ext i j
    rfl
  unfold r2TerminalCore r2BoundaryMatrix
  rw [hp]
  have hb : Matrix.fromBlocks G C Cᵀ H -
      Matrix.fromRows R (W + E)ᵀ * X⁻¹ * (Matrix.fromRows R (W + E)ᵀ)ᵀ =
      Matrix.fromBlocks (G - R * X⁻¹ * Rᵀ) (C - R * X⁻¹ * (W + E))
        (Cᵀ - (W + E)ᵀ * X⁻¹ * Rᵀ) (H - (W + E)ᵀ * X⁻¹ * (W + E)) := by
    rw [Matrix.transpose_fromRows, Matrix.transpose_transpose,
      Matrix.fromRows_mul, Matrix.fromRows_mul_fromCols]
    ext i j
    cases i <;> cases j <;> rfl
  exact congrArg (fun A => A.submatrix r2BoundaryIndex.symm r2BoundaryIndex.symm) hb

/-- Under the positive-pivot hypothesis the lower-left block is the transpose of C'. -/
theorem r2_terminal_core_symmetric_blocks (X : Matrix (Fin 4) (Fin 4) ℝ)
    (G : Matrix (Fin 2) (Fin 2) ℝ) (C R : Matrix (Fin 2) (Fin 4) ℝ)
    (H W E : Matrix (Fin 4) (Fin 4) ℝ) (hX : X.PosDef) :
    r2TerminalCore X G C R H W E =
      r2BoundaryMatrix (G - R * X⁻¹ * Rᵀ)
        (C - R * X⁻¹ * (W + E)) (H - (W + E)ᵀ * X⁻¹ * (W + E)) := by
  have hi : (X⁻¹)ᵀ = X⁻¹ := by
    simpa only [Matrix.conjTranspose_eq_transpose_of_trivial] using hX.isHermitian.inv.eq
  have hc : Cᵀ - (W + E)ᵀ * X⁻¹ * Rᵀ = (C - R * X⁻¹ * (W + E))ᵀ := by
    rw [Matrix.transpose_sub, Matrix.transpose_mul, Matrix.transpose_mul, hi]
    simp only [Matrix.mul_assoc]
  rw [r2_terminal_core_blocks, hc]
  rfl

/-- The terminal C block has its own linear E correction. -/
theorem r2_terminal_cross_correction (X : Matrix (Fin 4) (Fin 4) ℝ)
    (C R : Matrix (Fin 2) (Fin 4) ℝ) (W E : Matrix (Fin 4) (Fin 4) ℝ) :
    C - R * X⁻¹ * (W + E) = (C - R * X⁻¹ * W) - R * X⁻¹ * E := by
  rw [Matrix.mul_add]
  abel

/-- Both H cross terms and the pure E term survive terminal elimination. -/
theorem r2_terminal_H_corrections (X H W E : Matrix (Fin 4) (Fin 4) ℝ) :
    H - (W + E)ᵀ * X⁻¹ * (W + E) =
      H - Wᵀ * X⁻¹ * W - Wᵀ * X⁻¹ * E -
        Eᵀ * X⁻¹ * W - Eᵀ * X⁻¹ * E := by
  simp only [Matrix.transpose_add, Matrix.add_mul, Matrix.mul_add]
  abel

/-- Instantiation with the physical positive-parity R2 terminal coupling. -/
theorem r2_terminal_EPlus_posDef_iff (X : Matrix (Fin 4) (Fin 4) ℝ)
    (G : Matrix (Fin 2) (Fin 2) ℝ) (C R : Matrix (Fin 2) (Fin 4) ℝ)
    (H W : Matrix (Fin 4) (Fin 4) ℝ) (hX : X.PosDef) :
    (r2TerminalMatrix X G C R H W r2EPlus).PosDef ↔
      (r2BoundaryMatrix (G - R * X⁻¹ * Rᵀ)
        (C - R * X⁻¹ * (W + r2EPlus))
        (H - (W + r2EPlus)ᵀ * X⁻¹ * (W + r2EPlus))).PosDef := by
  rw [r2_terminal_posDef_iff X G C R H W r2EPlus hX,
    r2_terminal_core_symmetric_blocks X G C R H W r2EPlus hX]

end TargetA

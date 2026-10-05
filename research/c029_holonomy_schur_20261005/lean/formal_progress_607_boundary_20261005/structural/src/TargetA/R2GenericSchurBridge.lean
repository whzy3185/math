import TargetA.R2RationalRecurrence
import C029OpenSchur

namespace TargetA
open scoped Matrix
set_option maxHeartbeats 300000

/-- Explicit two-sided typed correspondence, proved from the actual record fields. -/
def r2GenericStateEquiv : R2RecurrenceState ℝ ≃ C029OpenSchur.OpenState where
  toFun s := { X := s.X, R := s.R, W := s.W, G := s.G, H := s.H, C := s.C }
  invFun s := { X := s.X, R := s.R, W := s.W, G := s.G, H := s.H, C := s.C }
  left_inv s := by cases s; rfl
  right_inv s := by cases s; rfl

/-- The packed retained matrix written directly in the original recurrence fields. -/
def r2ActualPackedOpenState (s : R2RecurrenceState ℝ) : Matrix (Fin 10) (Fin 10) ℝ :=
  (Matrix.fromBlocks s.G (Matrix.fromCols s.R s.C) (Matrix.fromRows s.Rᵀ s.Cᵀ)
    (Matrix.fromBlocks s.X s.W s.Wᵀ s.H)).submatrix
      C029OpenSchur.openRetainedIndex.symm C029OpenSchur.openRetainedIndex.symm

theorem r2_generic_update_bridge (j : ℕ) (s : R2RecurrenceState ℝ)
    (Y : Matrix (Fin 4) (Fin 4) ℝ) :
    r2GenericStateEquiv (r2UpdateWithInverse ℝ j s Y) =
      C029OpenSchur.openUpdateWithInverse (r2D ℝ) (r2Coupling ℝ j)
        (r2GenericStateEquiv s) Y := rfl

theorem r2_generic_packed_bridge (s : R2RecurrenceState ℝ) :
    C029OpenSchur.openPacked (r2GenericStateEquiv s) = r2ActualPackedOpenState s := rfl

theorem r2_generic_updated_packed_bridge (j : ℕ) (s : R2RecurrenceState ℝ)
    (Y : Matrix (Fin 4) (Fin 4) ℝ) :
    r2ActualPackedOpenState (r2UpdateWithInverse ℝ j s Y) =
      C029OpenSchur.openPacked (C029OpenSchur.openUpdateWithInverse
        (r2D ℝ) (r2Coupling ℝ j) (r2GenericStateEquiv s) Y) := by
  rw [← r2_generic_packed_bridge, r2_generic_update_bridge]

theorem r2_generic_schur_bridge (j : ℕ) (s : R2RecurrenceState ℝ)
    (hX : s.X.PosDef) :
    C029OpenSchur.openSchurCore (r2D ℝ) (r2Coupling ℝ j) (r2GenericStateEquiv s) =
      r2ActualPackedOpenState (r2UpdateWithInverse ℝ j s s.X⁻¹) := by
  have hX' : (r2GenericStateEquiv s).X.PosDef := hX
  rw [C029OpenSchur.open_schur_eq_update (r2D ℝ) (r2Coupling ℝ j)
    (r2GenericStateEquiv s) hX']
  rw [← r2_generic_update_bridge, r2_generic_packed_bridge]
  rfl

/-- The generic fourteen-dimensional criterion now specializes to the actual
recurrence update, with the positive-pivot hypothesis retained explicitly. -/
theorem r2_generic_open_posDef_iff (j : ℕ) (s : R2RecurrenceState ℝ)
    (hX : s.X.PosDef) :
    (C029OpenSchur.openMatrix (r2D ℝ) (r2Coupling ℝ j) (r2GenericStateEquiv s)).PosDef ↔
      (r2ActualPackedOpenState (r2UpdateWithInverse ℝ j s s.X⁻¹)).PosDef := by
  have hX' : (r2GenericStateEquiv s).X.PosDef := hX
  rw [C029OpenSchur.open_posDef_iff (r2D ℝ) (r2Coupling ℝ j)
    (r2GenericStateEquiv s) hX']
  rw [← r2_generic_update_bridge, r2_generic_packed_bridge]
  rfl

end TargetA

#print axioms TargetA.r2_posDef_submatrix_equiv
#print axioms TargetA.r2_strict_schur_criterion
#print axioms TargetA.r2_terminal_posDef_iff
#print axioms TargetA.r2_terminal_core_blocks
#print axioms TargetA.r2_terminal_core_symmetric_blocks
#print axioms TargetA.r2_terminal_cross_correction
#print axioms TargetA.r2_terminal_H_corrections
#print axioms TargetA.r2_terminal_EPlus_posDef_iff
#print axioms TargetA.R2RecurrenceState.ext
#print axioms TargetA.r2D
#print axioms TargetA.r2EP
#print axioms TargetA.r2EM
#print axioms TargetA.r2Coupling
#print axioms TargetA.r2InitialState
#print axioms TargetA.r2UpdateWithInverse
#print axioms TargetA.r2RecurrenceStep
#print axioms TargetA.r2Orbit
#print axioms TargetA.r2CoreWithInverse
#print axioms TargetA.r2Core26
#print axioms C029OpenSchur.posDef_submatrix_equiv
#print axioms C029OpenSchur.strict_schur_criterion
#print axioms C029OpenSchur.open_sum_schur_eq_update
#print axioms C029OpenSchur.open_schur_eq_update
#print axioms C029OpenSchur.open_posDef_iff
#print axioms TargetA.r2GenericStateEquiv
#print axioms TargetA.r2_generic_update_bridge
#print axioms TargetA.r2_generic_packed_bridge
#print axioms TargetA.r2_generic_updated_packed_bridge
#print axioms TargetA.r2_generic_schur_bridge
#print axioms TargetA.r2_generic_open_posDef_iff

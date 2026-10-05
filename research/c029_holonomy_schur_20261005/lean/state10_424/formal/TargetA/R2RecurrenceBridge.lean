import TargetA.R2RationalRecurrence
import TargetA.R2Seed106Certificate

namespace TargetA

open scoped Matrix

/-- Multiplication certificates determine the genuine finite recurrence; no
inverse value is silently supplied as an assumption about the orbit. -/
theorem r2_orbit_eq_of_certificates {K : Type*} [Field K] (N : ℕ)
    (s : ℕ → R2RecurrenceState K)
    (Y : ℕ → Matrix (Fin 4) (Fin 4) K)
    (h0 : s 0 = r2InitialState K)
    (hInv : ∀ j, j < N → (s j).X * Y j = 1)
    (hStep : ∀ j, j < N → s (j+1) = r2UpdateWithInverse K j (s j) (Y j)) :
    ∀ j, j ≤ N → r2Orbit K j = s j := by
  intro j
  induction j with
  | zero => intro _; exact h0.symm
  | succ j ih =>
      intro hj
      have hjN : j < N := by omega
      have hi : (s j).X⁻¹ = Y j := Matrix.inv_eq_right_inv (hInv j hjN)
      rw [r2Orbit, r2RecurrenceStep, ih (by omega), hi]
      exact (hStep j hjN).symm

/-- The terminal correction used by the recurrence is the exact Schur core
already verified in the dimension-specific terminal theorem. -/
theorem r2_core_with_actual_inverse_eq_terminal (s : R2RecurrenceState ℝ) :
    r2CoreWithInverse ℝ s s.X⁻¹ =
      r2TerminalCore s.X s.G s.C s.R s.H s.W r2EPlus := by
  rw [r2_terminal_core_blocks]
  rfl

/-- Positivity of the recurrence terminal core is equivalent to positivity of
the corresponding ten-dimensional terminal block, given a positive pivot. -/
theorem r2_recurrence_terminal_posDef_iff (s : R2RecurrenceState ℝ)
    (hX : s.X.PosDef) :
    (r2TerminalMatrix s.X s.G s.C s.R s.H s.W r2EPlus).PosDef ↔
      (r2CoreWithInverse ℝ s s.X⁻¹).PosDef := by
  rw [r2_core_with_actual_inverse_eq_terminal]
  exact r2_terminal_posDef_iff s.X s.G s.C s.R s.H s.W r2EPlus hX

/-- At n=106, 24 open eliminations precede the terminal W_24+E_plus correction.
This theorem isolates every finite certificate needed to identify S_26. -/
theorem r2_core26_eq_of_certificates {K : Type*} [Field K]
    (s : ℕ → R2RecurrenceState K)
    (Y : ℕ → Matrix (Fin 4) (Fin 4) K)
    (h0 : s 0 = r2InitialState K)
    (hInv : ∀ j, j ≤ 24 → (s j).X * Y j = 1)
    (hStep : ∀ j, j < 24 → s (j+1) = r2UpdateWithInverse K j (s j) (Y j)) :
    r2Core26 K = r2CoreWithInverse K (s 24) (Y 24) := by
  have ho := r2_orbit_eq_of_certificates 24 s Y h0
    (fun j hj => hInv j (by omega)) hStep 24 (by omega)
  unfold r2Core26
  rw [ho, Matrix.inv_eq_right_inv (hInv 24 (by omega))]

/-- A finite certificate matching the separately verified seed suffices for the
strict margin of the actual recurrence core. The finite identities are premises,
not claims that the recorded n=106 orbit has already been checked. -/
theorem r2_core26_margin_of_seed_certificate
    (s : ℕ → R2RecurrenceState ℝ)
    (Y : ℕ → Matrix (Fin 4) (Fin 4) ℝ)
    (h0 : s 0 = r2InitialState ℝ)
    (hInv : ∀ j, j ≤ 24 → (s j).X * Y j = 1)
    (hStep : ∀ j, j < 24 → s (j+1) = r2UpdateWithInverse ℝ j (s j) (Y j))
    (hTerminal : r2CoreWithInverse ℝ (s 24) (Y 24) = r2Seed106Core) :
    (r2Core26 ℝ - (1/50 : ℝ) • (1 : Matrix (Fin 6) (Fin 6) ℝ)).PosDef := by
  rw [r2_core26_eq_of_certificates s Y h0 hInv hStep, hTerminal]
  exact r2_seed106_margin_posDef

end TargetA

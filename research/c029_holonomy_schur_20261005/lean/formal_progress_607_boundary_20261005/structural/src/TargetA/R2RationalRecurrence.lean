import TargetA.R2TerminalSchur

namespace TargetA

open scoped Matrix

/-- Actual R2 open-chain state: a 4-site pivot, 2-site head and retained 4-site tail. -/
@[ext] structure R2RecurrenceState (K : Type*) where
  X : Matrix (Fin 4) (Fin 4) K
  R : Matrix (Fin 2) (Fin 4) K
  W : Matrix (Fin 4) (Fin 4) K
  G : Matrix (Fin 2) (Fin 2) K
  H : Matrix (Fin 4) (Fin 4) K
  C : Matrix (Fin 2) (Fin 4) K

def r2D (K : Type*) [Field K] : Matrix (Fin 4) (Fin 4) K :=
  !![98/25, 0, -1, 0; 0, 98/25, 0, -1; -1, 0, 98/25, 0; 0, -1, 0, 98/25]

def r2EP (K : Type*) [Field K] : Matrix (Fin 4) (Fin 4) K :=
  !![-1, 0, 0, 0; 0, 1, 0, 0; -1, 2, 1, 0; 2, -1, 0, -1]

def r2EM (K : Type*) [Field K] : Matrix (Fin 4) (Fin 4) K :=
  !![-1, 0, 0, 0; 0, 1, 0, 0; -1, -2, 1, 0; -2, -1, 0, -1]

def r2Coupling (K : Type*) [Field K] (j : ℕ) : Matrix (Fin 4) (Fin 4) K :=
  if j % 2 = 0 then r2EP K else r2EM K

def r2InitialState (K : Type*) [Field K] : R2RecurrenceState K where
  X := r2D K
  R := !![-1, -2, 1, 0; -2, -1, 0, -1]
  W := !![0, 0, -1, 0; 0, 0, 0, 1; 0, 0, 0, 0; 0, 0, 0, 0]
  G := (98/25 : K) • 1
  H := r2D K
  C := !![-1, 0, -1, 0; 0, -1, 0, -1]

/-- The six exact open-response updates, with the inverse made an explicit argument. -/
def r2UpdateWithInverse (K : Type*) [Field K] (j : ℕ)
    (s : R2RecurrenceState K) (Y : Matrix (Fin 4) (Fin 4) K) : R2RecurrenceState K where
  X := r2D K - (r2Coupling K j)ᵀ * Y * r2Coupling K j
  R := -s.R * Y * r2Coupling K j
  W := -(r2Coupling K j)ᵀ * Y * s.W
  G := s.G - s.R * Y * s.Rᵀ
  H := s.H - s.Wᵀ * Y * s.W
  C := s.C - s.R * Y * s.W

noncomputable def r2RecurrenceStep (K : Type*) [Field K] (j : ℕ)
    (s : R2RecurrenceState K) : R2RecurrenceState K :=
  r2UpdateWithInverse K j s s.X⁻¹

/-- Zero-based open recurrence: X_0=D; state j is after exactly j open eliminations. -/
noncomputable def r2Orbit (K : Type*) [Field K] : ℕ → R2RecurrenceState K
  | 0 => r2InitialState K
  | j+1 => r2RecurrenceStep K j (r2Orbit K j)

/-- The terminal elimination at p=24 uses W_24+E_plus, not an extra open update. -/
def r2CoreWithInverse (K : Type*) [Field K] (s : R2RecurrenceState K)
    (Y : Matrix (Fin 4) (Fin 4) K) : Matrix (Fin 6) (Fin 6) K :=
  (Matrix.fromBlocks (s.G - s.R * Y * s.Rᵀ)
    (s.C - s.R * Y * (s.W + r2EP K))
    (s.Cᵀ - (s.W + r2EP K)ᵀ * Y * s.Rᵀ)
    (s.H - (s.W + r2EP K)ᵀ * Y * (s.W + r2EP K))).submatrix
      r2BoundaryIndex.symm r2BoundaryIndex.symm

noncomputable def r2Core26 (K : Type*) [Field K] : Matrix (Fin 6) (Fin 6) K :=
  r2CoreWithInverse K (r2Orbit K 24) (r2Orbit K 24).X⁻¹

end TargetA

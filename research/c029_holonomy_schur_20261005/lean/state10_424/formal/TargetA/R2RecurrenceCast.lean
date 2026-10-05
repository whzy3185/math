import TargetA.R2RecurrenceBridge

namespace TargetA

open scoped Matrix

noncomputable def r2RealMatrix {m n : Type*} (A : Matrix m n ℚ) : Matrix m n ℝ :=
  A.map (Rat.castHom ℝ)

noncomputable def r2RealState (s : R2RecurrenceState ℚ) : R2RecurrenceState ℝ where
  X := r2RealMatrix s.X
  R := r2RealMatrix s.R
  W := r2RealMatrix s.W
  G := r2RealMatrix s.G
  H := r2RealMatrix s.H
  C := r2RealMatrix s.C

@[simp] theorem r2_real_matrix_add {m n : Type*} (A B : Matrix m n ℚ) :
    r2RealMatrix (A+B) = r2RealMatrix A + r2RealMatrix B := by
  ext i j
  simp [r2RealMatrix, Matrix.map_apply]

@[simp] theorem r2_real_matrix_sub {m n : Type*} (A B : Matrix m n ℚ) :
    r2RealMatrix (A-B) = r2RealMatrix A - r2RealMatrix B := by
  ext i j
  simp [r2RealMatrix, Matrix.map_apply]

@[simp] theorem r2_real_matrix_neg {m n : Type*} (A : Matrix m n ℚ) :
    r2RealMatrix (-A) = -r2RealMatrix A := by
  ext i j
  simp [r2RealMatrix, Matrix.map_apply]

@[simp] theorem r2_real_matrix_mul {m n p : Type*} [Fintype n]
    (A : Matrix m n ℚ) (B : Matrix n p ℚ) :
    r2RealMatrix (A*B) = r2RealMatrix A * r2RealMatrix B := Matrix.map_mul

@[simp] theorem r2_real_matrix_transpose {m n : Type*} (A : Matrix m n ℚ) :
    r2RealMatrix Aᵀ = (r2RealMatrix A)ᵀ := rfl

@[simp] theorem r2_real_matrix_one {n : Type*} [DecidableEq n] :
    r2RealMatrix (1 : Matrix n n ℚ) = (1 : Matrix n n ℝ) := by
  ext i j
  by_cases hij : i=j <;> simp [r2RealMatrix, Matrix.map_apply, Matrix.one_apply, hij]

@[simp] theorem r2_real_matrix_submatrix {m n p q : Type*} (A : Matrix m n ℚ)
    (f : p → m) (g : q → n) :
    r2RealMatrix (A.submatrix f g) = (r2RealMatrix A).submatrix f g := rfl

@[simp] theorem r2_real_matrix_fromBlocks {m n p q : Type*}
    (A : Matrix m p ℚ) (B : Matrix m q ℚ) (C : Matrix n p ℚ) (D : Matrix n q ℚ) :
    r2RealMatrix (Matrix.fromBlocks A B C D) =
      Matrix.fromBlocks (r2RealMatrix A) (r2RealMatrix B) (r2RealMatrix C) (r2RealMatrix D) := by
  ext i j
  cases i <;> cases j <;> rfl

@[simp] theorem r2_real_D : r2RealMatrix (r2D ℚ) = r2D ℝ := by
  ext i j
  fin_cases i <;> fin_cases j <;> norm_num [r2RealMatrix, r2D]

@[simp] theorem r2_real_EP : r2RealMatrix (r2EP ℚ) = r2EP ℝ := by
  ext i j
  fin_cases i <;> fin_cases j <;> norm_num [r2RealMatrix, r2EP]

@[simp] theorem r2_real_EM : r2RealMatrix (r2EM ℚ) = r2EM ℝ := by
  ext i j
  fin_cases i <;> fin_cases j <;> norm_num [r2RealMatrix, r2EM]

@[simp] theorem r2_real_coupling (j : ℕ) :
    r2RealMatrix (r2Coupling ℚ j) = r2Coupling ℝ j := by
  by_cases h : j % 2 = 0 <;> simp [r2Coupling, h]

theorem r2_real_initial : r2RealState (r2InitialState ℚ) = r2InitialState ℝ := by
  apply R2RecurrenceState.ext
  all_goals
    ext i j
    fin_cases i <;> fin_cases j <;>
      norm_num [r2RealState, r2RealMatrix, r2InitialState, r2D, Matrix.one_apply]

/-- Rational response updates commute exactly with the embedding into real matrices. -/
theorem r2_real_update (j : ℕ) (s : R2RecurrenceState ℚ)
    (Y : Matrix (Fin 4) (Fin 4) ℚ) :
    r2RealState (r2UpdateWithInverse ℚ j s Y) =
      r2UpdateWithInverse ℝ j (r2RealState s) (r2RealMatrix Y) := by
  apply R2RecurrenceState.ext <;> simp [r2RealState, r2UpdateWithInverse]

/-- A checked multiplication identity supplies the actual inverse, over the reals as well. -/
theorem r2_real_inverse_of_certificate (X Y : Matrix (Fin 4) (Fin 4) ℚ)
    (h : X * Y = 1) : (r2RealMatrix X)⁻¹ = r2RealMatrix Y := by
  apply Matrix.inv_eq_right_inv
  rw [← r2_real_matrix_mul, h, r2_real_matrix_one]

theorem r2_pivot_isUnit_of_certificate {K : Type*} [Field K]
    (X Y : Matrix (Fin 4) (Fin 4) K) (h : X * Y = 1) : IsUnit X := by
  rw [Matrix.isUnit_iff_isUnit_det, isUnit_iff_ne_zero]
  intro hz
  have hd := congrArg Matrix.det h
  rw [Matrix.det_mul, hz, zero_mul, Matrix.det_one] at hd
  exact zero_ne_one hd

/-- Terminal correction also commutes with rational-to-real transport. -/
theorem r2_real_core_with_inverse (s : R2RecurrenceState ℚ)
    (Y : Matrix (Fin 4) (Fin 4) ℚ) :
    r2RealMatrix (r2CoreWithInverse ℚ s Y) =
      r2CoreWithInverse ℝ (r2RealState s) (r2RealMatrix Y) := by
  simp [r2CoreWithInverse, r2RealState]

/-- Rational certificate values represent the actual real recurrence at every
checked index. All transition and inverse identities remain explicit premises. -/
theorem r2_real_orbit_eq_of_certificates (N : ℕ)
    (s : ℕ → R2RecurrenceState ℚ)
    (Y : ℕ → Matrix (Fin 4) (Fin 4) ℚ)
    (h0 : s 0 = r2InitialState ℚ)
    (hInv : ∀ j, j < N → (s j).X * Y j = 1)
    (hStep : ∀ j, j < N → s (j+1) = r2UpdateWithInverse ℚ j (s j) (Y j)) :
    ∀ j, j ≤ N → r2Orbit ℝ j = r2RealState (s j) := by
  apply r2_orbit_eq_of_certificates N (fun j => r2RealState (s j))
    (fun j => r2RealMatrix (Y j))
  · rw [h0, r2_real_initial]
  · intro j hj
    change r2RealMatrix (s j).X * r2RealMatrix (Y j) = 1
    rw [← r2_real_matrix_mul, hInv j hj, r2_real_matrix_one]
  · intro j hj
    rw [hStep j hj, r2_real_update]

/-- At n=106, 24 open eliminations precede the terminal W_24+E_plus correction.
This theorem isolates every finite certificate needed to identify S_26. -/
theorem r2_real_core26_eq_of_certificates
    (s : ℕ → R2RecurrenceState ℚ)
    (Y : ℕ → Matrix (Fin 4) (Fin 4) ℚ)
    (h0 : s 0 = r2InitialState ℚ)
    (hInv : ∀ j, j ≤ 24 → (s j).X * Y j = 1)
    (hStep : ∀ j, j < 24 → s (j+1) = r2UpdateWithInverse ℚ j (s j) (Y j)) :
    r2Core26 ℝ = r2RealMatrix (r2CoreWithInverse ℚ (s 24) (Y 24)) := by
  have ho := r2_real_orbit_eq_of_certificates 24 s Y h0
    (fun j hj => hInv j (by omega)) hStep 24 (by omega)
  unfold r2Core26
  rw [ho]
  change r2CoreWithInverse ℝ (r2RealState (s 24)) (r2RealMatrix (s 24).X)⁻¹ = _
  rw [r2_real_inverse_of_certificate _ _ (hInv 24 (by omega)),
    r2_real_core_with_inverse]


/-- Explicit rational initial, inverse, transition and terminal identities imply
the strict margin for the genuine real S_26 recurrence. Numerical verification
of the recorded orbit is a separate obligation, not asserted here. -/
theorem r2_core26_margin_of_rational_seed_certificate
    (s : ℕ → R2RecurrenceState ℚ)
    (Y : ℕ → Matrix (Fin 4) (Fin 4) ℚ)
    (h0 : s 0 = r2InitialState ℚ)
    (hInv : ∀ j, j ≤ 24 → (s j).X * Y j = 1)
    (hStep : ∀ j, j < 24 → s (j+1) = r2UpdateWithInverse ℚ j (s j) (Y j))
    (hTerminal : r2CoreWithInverse ℚ (s 24) (Y 24) = r2Seed106CoreQ) :
    (r2Core26 ℝ - (1/50 : ℝ) • (1 : Matrix (Fin 6) (Fin 6) ℝ)).PosDef := by
  rw [r2_real_core26_eq_of_certificates s Y h0 hInv hStep, hTerminal]
  exact r2_seed106_margin_posDef

end TargetA

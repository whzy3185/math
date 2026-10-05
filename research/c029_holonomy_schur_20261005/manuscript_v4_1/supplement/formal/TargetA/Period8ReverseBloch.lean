import TargetA.Period8DoubleCover

namespace TargetA

/-- Inverse of the raw-to-cell coordinate permutation. -/
noncomputable def period8CellToRaw (M : ℕ) [NeZero M] (hM : 0 < M)
    (G : ZMod M → Fin 8 → ℂ) : Fin (8 * M) → ℂ :=
  fun i => G (ZMod.finEquiv M (cellReindex M hM i).1) (cellReindex M hM i).2

theorem period8_cell_to_raw_right_inverse (M : ℕ) [NeZero M] (hM : 0 < M)
    (G : ZMod M → Fin 8 → ℂ) :
    rawToZModCellState M hM (period8CellToRaw M hM G) = G := by
  funext z r
  obtain ⟨m, rfl⟩ := (ZMod.finEquiv M).surjective z
  simp [rawToZModCellState, finCellToZModState, rawToFinCellState, period8CellToRaw]

theorem period8_raw_to_cell_smul (M : ℕ) [NeZero M] (hM : 0 < M)
    (u : Fin (8 * M) → ℂ) (c : ℂ) :
    rawToZModCellState M hM (c • u) = c • rawToZModCellState M hM u := rfl

theorem period8_cell_eigen_gives_raw_periodic_eigen (M : ℕ) [NeZero M] (hM : 0 < M)
    (G : ZMod M → Fin 8 → ℂ) (lambda : ℂ)
    (he : period8CellAction G = lambda • G) :
    (period8TargetMatrixC M 1).mulVec (period8CellToRaw M hM G) =
      lambda • period8CellToRaw M hM G := by
  apply period8_raw_to_cell_injective M hM
  rw [← period8_raw_to_cell_intertwines, period8_raw_to_cell_smul,
    period8_cell_to_raw_right_inverse, he]

theorem period8_cell_antiperiodic_gives_raw_half_shift (L : ℕ) (hL : 0 < L)
    [NeZero (2 * L)] (G : ZMod (2 * L) → Fin 8 → ℂ)
    (hg : period8CellTranslation (L : ZMod (2 * L)) G = -G) :
    ∀ i, period8CellToRaw (2 * L) (by omega) G (cyclicNext i (8 * L)) =
      -period8CellToRaw (2 * L) (by omega) G i := by
  intro i
  obtain ⟨⟨m, r⟩, rfl⟩ := (cellReindex (2 * L) (by omega)).symm.surjective i
  rw [← period8_double_cell_shift_unindex L hL]
  have he := congrFun (congrFun hg (ZMod.finEquiv (2 * L) m)) r
  simp only [period8CellTranslation, Pi.neg_apply] at he
  rw [← zmod_finEquiv_cyclic_step] at he
  simpa [period8CellToRaw] using he

/-- Every raw negative half-shift vector is exactly the explicit lift of its first half. -/
theorem period8_half_shift_is_double_lift (L : ℕ) (hL : 0 < L)
    (v : Fin (8 * (2 * L)) → ℂ)
    (hv : ∀ i, v (cyclicNext i (8 * L)) = -v i) :
    period8DoubleLift L (fun i => v (period8DoubleLow L i)) = v := by
  funext i
  obtain ⟨j, rfl⟩ := (period8DoubleIndex L).surjective i
  cases j with
  | inl j =>
    change period8DoubleLift L _ (period8DoubleLow L j) = _
    simp [period8DoubleIndex]
  | inr j =>
    change period8DoubleLift L _ (period8DoubleHigh L j) = v (period8DoubleHigh L j)
    rw [period8_double_lift_high]
    have he := hv (period8DoubleLow L j)
    rw [period8_double_low_half_shift L hL] at he
    exact he.symm

/-- Reverse transfer from a genuine finite antiperiodic cell eigenmode to the raw graph. -/
theorem period8_antiperiodic_cell_eigen_gives_raw_minus_eigenvector
    (L : ℕ) (hL : 0 < L) [NeZero (2 * L)]
    (G : ZMod (2 * L) → Fin 8 → ℂ) (lambda : ℂ) (hg : G ≠ 0)
    (hanti : period8CellTranslation (L : ZMod (2 * L)) G = -G)
    (he : period8CellAction G = lambda • G) :
    ∃ u : Fin (8 * L) → ℂ, u ≠ 0 ∧
      (period8TargetMatrixC L (-1)).mulVec u = lambda • u := by
  let v := period8CellToRaw (2 * L) (by omega) G
  let u := fun i => v (period8DoubleLow L i)
  have hv : v ≠ 0 := by
    intro hz
    apply hg
    rw [← period8_cell_to_raw_right_inverse (2 * L) (by omega) G]
    change rawToZModCellState (2 * L) (by omega) v = 0
    rw [hz]
    rfl
  have hantiV : ∀ i, v (cyclicNext i (8 * L)) = -v i :=
    period8_cell_antiperiodic_gives_raw_half_shift L hL G hanti
  have hvu : period8DoubleLift L u = v := period8_half_shift_is_double_lift L hL v hantiV
  have hu : u ≠ 0 := by
    intro hz
    apply hv
    rw [← hvu, hz]
    funext i
    obtain ⟨j, rfl⟩ := (period8DoubleIndex L).surjective i
    cases j <;> simp [period8DoubleIndex]
  refine ⟨u, hu, ?_⟩
  apply period8_double_lift_injective L
  rw [← period8_double_lift_intertwines L hL, period8_double_lift_smul, hvu]
  exact period8_cell_eigen_gives_raw_periodic_eigen (2 * L) (by omega) G lambda he

/-- Explicit inverse-Bloch plane wave on the doubled cycle. -/
noncomputable def period8FirstPlaneWave (N : ℕ) [NeZero N]
    (u : Fin 8 → ℂ) : ZMod N → Fin 8 → ℂ :=
  fun m => ZMod.stdAddChar m • u

theorem period8_first_plane_wave_nonzero (N : ℕ) [NeZero N]
    (u : Fin 8 → ℂ) (hu : u ≠ 0) : period8FirstPlaneWave N u ≠ 0 := by
  intro hz
  apply hu
  have he := congrFun hz 0
  simpa [period8FirstPlaneWave] using he

theorem period8_first_plane_wave_action (N : ℕ) [NeZero N]
    (xi : ℂ) (hxi : xi^2 = ZMod.stdAddChar (1 : ZMod N))
    (u : Fin 8 → ℂ) :
    period8CellAction (period8FirstPlaneWave N u) =
      period8FirstPlaneWave N ((period8Fiber xi).mulVec u) := by
  have hb : ZMod.stdAddChar (-1 : ZMod N) = xi⁻¹^2 := by
    rw [AddChar.map_neg_eq_inv, ← hxi, inv_pow]
  funext m r
  simp only [period8CellAction, period8FirstPlaneWave,
    AddChar.map_add_eq_mul, Matrix.mulVec_smul, ← hxi, hb,
    period8_fiber_as_cell_symbol, Matrix.add_mulVec, Matrix.smul_mulVec,
    Pi.add_apply, Pi.smul_apply, smul_eq_mul]
  ring

theorem period8_first_plane_wave_antiperiodic (L : ℕ) [NeZero (2 * L)]
    (u : Fin 8 → ℂ) (hz : (ZMod.stdAddChar (1 : ZMod (2 * L)))^L = -1) :
    period8CellTranslation (L : ZMod (2 * L)) (period8FirstPlaneWave (2 * L) u) =
      -period8FirstPlaneWave (2 * L) u := by
  have hc : ZMod.stdAddChar ((L : ZMod (2 * L)) * 1) =
      (ZMod.stdAddChar (1 : ZMod (2 * L)))^L := by
    rw [← nsmul_eq_mul, AddChar.map_nsmul_eq_pow]
  simp only [mul_one] at hc
  funext m r
  simp [period8CellTranslation, period8FirstPlaneWave, AddChar.map_add_eq_mul, hc, hz]

/-- Fiber attainment at the first antiperiodic phase transfers to the raw alpha-minus graph. -/
theorem period8_first_fiber_eigen_gives_raw_minus_eigenvector
    (L : ℕ) (hL : 0 < L) [NeZero (2 * L)] (xi lambda : ℂ)
    (hxi : xi^2 = ZMod.stdAddChar (1 : ZMod (2 * L)))
    (hz : (ZMod.stdAddChar (1 : ZMod (2 * L)))^L = -1)
    (u : Fin 8 → ℂ) (hu : u ≠ 0)
    (he : (period8Fiber xi).mulVec u = lambda • u) :
    ∃ v : Fin (8 * L) → ℂ, v ≠ 0 ∧
      (period8TargetMatrixC L (-1)).mulVec v = lambda • v := by
  apply period8_antiperiodic_cell_eigen_gives_raw_minus_eigenvector L hL
    (period8FirstPlaneWave (2 * L) u) lambda
  · exact period8_first_plane_wave_nonzero (2 * L) u hu
  · exact period8_first_plane_wave_antiperiodic L u hz
  · rw [period8_first_plane_wave_action (2 * L) xi hxi, he]
    funext m r
    simp [period8FirstPlaneWave, smul_smul, mul_comm, mul_assoc]

end TargetA

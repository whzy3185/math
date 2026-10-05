import TargetA.Period8AntiperiodicCells

namespace TargetA

/-- The existing raw-to-cell permutation is injective. -/
theorem period8_raw_to_cell_injective (M : ℕ) [NeZero M] (hM : 0 < M) :
    Function.Injective (rawToZModCellState M hM) := by
  intro u v huv
  funext i
  have he := congrFun (congrFun huv
    (ZMod.finEquiv M (cellReindex M hM i).1)) (cellReindex M hM i).2
  simpa [rawToZModCellState, finCellToZModState, rawToFinCellState] using he

/-- Exact operator intertwining for the already verified periodic reindexing. -/
theorem period8_raw_to_cell_intertwines (M : ℕ) [NeZero M] (hM : 0 < M)
    (u : Fin (8 * M) → ℂ) :
    period8CellAction (rawToZModCellState M hM u) =
      rawToZModCellState M hM ((period8TargetMatrixC M 1).mulVec u) := by
  funext z r
  obtain ⟨m, rfl⟩ := (ZMod.finEquiv M).surjective z
  change period8CellAction (finCellToZModState M (rawToFinCellState M hM u))
      (ZMod.finEquiv M m) r = _
  rw [period8_fin_cell_action_to_zmod M hM]
  rw [← period8_reindexed_matrix_mulVec M hM (rawToFinCellState M hM u) m r]
  rw [period8_reindexed_matrix_mulVec_raw, cellEncode_rawToFinCell]
  simp [rawToZModCellState, finCellToZModState, rawToFinCellState]

/-- Translation of a finite cell index agrees with addition in `ZMod`. -/
theorem zmod_finEquiv_cyclic_step (M : ℕ) [NeZero M]
    (m : Fin M) (s : ℕ) :
    ZMod.finEquiv M (cyclicNext m s) = (s : ZMod M) + ZMod.finEquiv M m := by
  rw [zmod_finEquiv_eq_natCast, zmod_finEquiv_eq_natCast]
  change (((m.val + s) % M : ℕ) : ZMod M) = (s : ZMod M) + (m.val : ZMod M)
  rw [ZMod.natCast_mod, Nat.cast_add]
  ring

/-- On a doubled cycle, half-period cell translation is half-period raw translation. -/
theorem period8_double_cell_shift_unindex (L : ℕ) (hL : 0 < L)
    (m : Fin (2 * L)) (r : Fin 8) :
    (cellReindex (2 * L) (by omega)).symm (cyclicNext m L, r) =
      cyclicNext ((cellReindex (2 * L) (by omega)).symm (m, r)) (8 * L) := by
  apply Fin.ext
  change 8 * ((m.val + L) % (2 * L)) + r.val =
    (8 * m.val + r.val + 8 * L) % (8 * (2 * L))
  by_cases hm : m.val < L
  · rw [Nat.mod_eq_of_lt (by omega : m.val + L < 2 * L)]
    rw [Nat.mod_eq_of_lt (by omega : 8 * m.val + r.val + 8 * L < 8 * (2 * L))]
    omega
  · rw [Nat.mod_eq_sub_mod (by omega : 2 * L ≤ m.val + L)]
    rw [Nat.mod_eq_of_lt (by omega : m.val + L - 2 * L < 2 * L)]
    rw [Nat.mod_eq_sub_mod (by omega : 8 * (2 * L) ≤ 8 * m.val + r.val + 8 * L)]
    rw [Nat.mod_eq_of_lt (by omega : 8 * m.val + r.val + 8 * L - 8 * (2 * L) < 8 * (2 * L))]
    omega

/-- Antiperiodicity is preserved by the explicit raw-to-cell permutation. -/
theorem period8_raw_half_shift_to_cell_antiperiodic (L : ℕ) (hL : 0 < L)
    (u : Fin (8 * (2 * L)) → ℂ)
    (hu : ∀ i, u (cyclicNext i (8 * L)) = -u i) :
    letI : NeZero (2 * L) := ⟨by omega⟩
    period8CellTranslation (L : ZMod (2 * L))
        (rawToZModCellState (2 * L) (by omega) u) =
      -rawToZModCellState (2 * L) (by omega) u := by
  letI : NeZero (2 * L) := ⟨by omega⟩
  funext z r
  obtain ⟨m, rfl⟩ := (ZMod.finEquiv (2 * L)).surjective z
  change rawToZModCellState (2 * L) (by omega) u
    ((L : ZMod (2 * L)) + ZMod.finEquiv (2 * L) m) r = _
  rw [← zmod_finEquiv_cyclic_step]
  simp only [rawToZModCellState, finCellToZModState, rawToFinCellState, Pi.neg_apply]
  simp only [RingEquiv.symm_apply_apply]
  rw [period8_double_cell_shift_unindex L hL]
  exact hu _

/-- A raw eigenvector on the periodic double cover in the negative half-shift
sector has the sharp strict bound. The following raw-graph extension will
supply this sector from the alpha-minus graph by an explicit embedding. -/
theorem period8_double_cover_antisector_eigen_square_lt_edge
    (L : ℕ) (hL : 0 < L) (u : Fin (8 * (2 * L)) → ℂ) (lambda : ℝ)
    (hu : u ≠ 0)
    (hanti : ∀ i, u (cyclicNext i (8 * L)) = -u i)
    (hEig : (period8TargetMatrixC (2 * L) 1).mulVec u = (lambda : ℂ) • u) :
    lambda^2 < period8Edge := by
  letI : NeZero (2 * L) := ⟨by omega⟩
  let G := rawToZModCellState (2 * L) (by omega) u
  apply period8_antiperiodic_cell_eigen_square_lt_edge (N := 2 * L) (L := L) (by omega) G lambda
  · intro hz
    apply hu
    apply period8_raw_to_cell_injective (2 * L) (by omega)
    change G = 0
    exact hz
  · exact period8_raw_half_shift_to_cell_antiperiodic L hL u hanti
  · rw [show G = rawToZModCellState (2 * L) (by omega) u by rfl]
    rw [period8_raw_to_cell_intertwines, hEig]
    rfl

end TargetA

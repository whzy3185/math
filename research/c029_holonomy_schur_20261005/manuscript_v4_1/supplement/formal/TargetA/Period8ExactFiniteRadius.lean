import TargetA.Period8FiberAttainment
import TargetA.Period8PhaseMaximum
import TargetA.Period8ReverseBloch

namespace TargetA

/-- Exact squared radius predicted by the first antiperiodic phase. -/
noncomputable def period8FiniteTop (L : ℕ) : ℝ :=
  period8TopRoot (2 * Real.cos (Real.pi / (L : ℝ)))

noncomputable def period8FiniteRadius (L : ℕ) : ℝ := Real.sqrt (period8FiniteTop L)

theorem period8_finite_top_pos (L : ℕ) : 0 < period8FiniteTop L := by
  have hc : -2 ≤ 2 * Real.cos (Real.pi / (L : ℝ)) := by
    nlinarith [Real.neg_one_le_cos (Real.pi / (L : ℝ))]
  have ht := period8_top_root_gt_four hc
  exact lt_trans (by norm_num : (0 : ℝ) < 4) ht

theorem period8_unit_parameter_eq_two_re {xi z : ℂ}
    (hu : xi * (starRingEnd ℂ) xi = 1) (hx : xi^2 = z) :
    (xi^2 + xi⁻¹^2).re = 2 * z.re := by
  have hinv : xi⁻¹ = (starRingEnd ℂ) xi := (period8_unit_conj_eq_inv hu).symm
  rw [hinv, ← map_pow, hx]
  simp
  ring

/-- The exact finite upper bound for every real eigenvector of the raw graph. -/
theorem period8_alpha_minus_raw_eigen_square_le_finite_top
    (L : ℕ) (hL : 0 < L) (u : Fin (8 * L) → ℂ) (lambda : ℝ)
    (hu : u ≠ 0)
    (he : (period8TargetMatrixC L (-1)).mulVec u = (lambda : ℂ) • u) :
    lambda^2 ≤ period8FiniteTop L := by
  letI : NeZero (2 * L) := ⟨by omega⟩
  let v := period8DoubleLift L u
  let G := rawToZModCellState (2 * L) (by omega) v
  have hv : v ≠ 0 := by
    intro hz
    apply hu
    funext i
    have hi := congrFun hz (period8DoubleLow L i)
    simpa [v] using hi
  have hg : G ≠ 0 := by
    intro hz
    apply hv
    apply period8_raw_to_cell_injective (2 * L) (by omega)
    change G = 0
    exact hz
  have hanti : period8CellTranslation (L : ZMod (2 * L)) G = -G :=
    period8_raw_half_shift_to_cell_antiperiodic L hL v
      (period8_double_lift_antiperiodic L hL u)
  have hvEig : (period8TargetMatrixC (2 * L) 1).mulVec v = (lambda : ℂ) • v := by
    rw [show v = period8DoubleLift L u by rfl,
      period8_double_lift_intertwines L hL, he, period8_double_lift_smul]
  have hgEig : period8CellAction G = (lambda : ℂ) • G := by
    rw [show G = rawToZModCellState (2 * L) (by omega) v by rfl,
      period8_raw_to_cell_intertwines, hvEig, period8_raw_to_cell_smul]
  obtain ⟨k, hk⟩ := exists_nonzero_period8_cell_dft G hg
  have hz := period8_antiperiodic_nonzero_dft_holonomy G k hanti hk
  obtain ⟨xi, hxi⟩ := IsAlgClosed.exists_pow_nat_eq (ZMod.stdAddChar k) (by norm_num : 0 < 2)
  have hunit := period8_xi_unit_from_holonomy (by omega : L ≠ 0) hxi hz (by norm_num)
  have hbound := period8_unit_fiber_eigen_square_le_top hunit (period8CellDFT G k) hk
    (period8_cell_eigen_dft_fiber G (lambda : ℂ) k xi hxi hgEig)
  have hparam := period8_unit_parameter_eq_two_re hunit hxi
  have hphase := period8_antiperiodic_phase_re_le_first L hL k hz
  have hc := period8_unit_parameter_mem_interval hunit
  have hcmax : 2 * Real.cos (Real.pi / (L : ℝ)) ≤ 2 := by
    nlinarith [Real.cos_le_one (Real.pi / (L : ℝ))]
  have hflux : (xi^2 + xi⁻¹^2).re ≤ 2 * Real.cos (Real.pi / (L : ℝ)) := by
    rw [hparam]
    linarith
  apply le_trans hbound
  rcases lt_or_eq_of_le hflux with hlt | heq
  · exact le_of_lt (period8_top_root_strict_mono hc.1 hcmax hlt)
  · rw [heq]
    exact le_rfl

/-- A genuine nonzero raw-graph eigenvector attains the positive exact radius. -/
theorem period8_alpha_minus_finite_radius_attained_vector
    (L : ℕ) (hL : 0 < L) :
    ∃ u : Fin (8 * L) → ℂ, u ≠ 0 ∧
      (period8TargetMatrixC L (-1)).mulVec u = (period8FiniteRadius L : ℂ) • u := by
  letI : NeZero (2 * L) := ⟨by omega⟩
  obtain ⟨xi, hxi⟩ := IsAlgClosed.exists_pow_nat_eq
    (ZMod.stdAddChar (1 : ZMod (2 * L))) (by norm_num : 0 < 2)
  have hz := period8_first_phase_antiperiodic L hL
  have hunit := period8_xi_unit_from_holonomy (by omega : L ≠ 0) hxi hz (by norm_num)
  have hparam : (xi^2 + xi⁻¹^2).re = 2 * Real.cos (Real.pi / (L : ℝ)) := by
    rw [period8_unit_parameter_eq_two_re hunit hxi, period8_first_phase_re L hL]
  obtain ⟨u, hu, he⟩ := period8_unit_fiber_top_attained hunit
  rw [hparam] at he
  exact period8_first_fiber_eigen_gives_raw_minus_eigenvector L hL xi
    (period8FiniteRadius L : ℂ) hxi hz u hu he

/-- A nonzero real eigenvector occurs in the complete Hermitian eigenvalue list. -/
theorem period8_hermitian_eigenvector_has_index {n : Type*} [Fintype n] [DecidableEq n]
    (A : Matrix n n ℂ) (hA : A.IsHermitian) (lambda : ℝ) (u : n → ℂ)
    (hu : u ≠ 0) (he : A.mulVec u = (lambda : ℂ) • u) :
    ∃ i, hA.eigenvalues i = lambda := by
  have hs : (lambda : ℂ) ∈ spectrum ℂ A := by
    rw [Matrix.mem_spectrum_iff_isRoot_charpoly]
    change A.charpoly.eval (lambda : ℂ) = 0
    rw [Matrix.eval_charpoly]
    apply Matrix.exists_mulVec_eq_zero_iff.mp
    refine ⟨u, hu, ?_⟩
    have hscalar : Matrix.scalar n (lambda : ℂ) =
        (lambda : ℂ) • (1 : Matrix n n ℂ) := by
      ext i j
      by_cases hij : i = j <;> simp [Matrix.scalar, Matrix.one_apply, hij]
    rw [hscalar, Matrix.sub_mulVec, Matrix.smul_mulVec, Matrix.one_mulVec, he, sub_self]
  have hsR : lambda ∈ spectrum ℝ A := spectrum.of_algebraMap_mem ℂ hs
  rw [hA.spectrum_real_eq_range_eigenvalues] at hsR
  exact hsR

theorem period8_alpha_minus_eigenvalue_square_le_finite_top (L : ℕ) (hL : 0 < L)
    (i : Fin (8 * L)) :
    ((period8_target_matrix_isHermitian L (-1)).eigenvalues i)^2 ≤ period8FiniteTop L := by
  apply period8_alpha_minus_raw_eigen_square_le_finite_top L hL
    (u := ⇑((period8_target_matrix_isHermitian L (-1)).eigenvectorBasis i))
  · exact (WithLp.ofLp_eq_zero 2).ne.2 <|
      (period8_target_matrix_isHermitian L (-1)).eigenvectorBasis.orthonormal.ne_zero i
  · exact (period8_target_matrix_isHermitian L (-1)).mulVec_eigenvectorBasis i

theorem period8_alpha_minus_finite_radius_attained_index (L : ℕ) (hL : 0 < L) :
    ∃ i : Fin (8 * L),
      (period8_target_matrix_isHermitian L (-1)).eigenvalues i = period8FiniteRadius L := by
  obtain ⟨u, hu, he⟩ := period8_alpha_minus_finite_radius_attained_vector L hL
  exact period8_hermitian_eigenvector_has_index _ (period8_target_matrix_isHermitian L (-1))
    (period8FiniteRadius L) u hu he

theorem period8_finite_radius_radical (L : ℕ) :
    period8FiniteRadius L =
      Real.sqrt (4 + Real.sqrt (8 + 2 * Real.cos (Real.pi / (L : ℝ)) +
        Real.sqrt (26 - 6 * Real.cos (Real.pi / (L : ℝ))))) := by
  unfold period8FiniteRadius period8FiniteTop period8TopRoot
  rw [show 26 - 3 * (2 * Real.cos (Real.pi / (L : ℝ))) =
    26 - 6 * Real.cos (Real.pi / (L : ℝ)) by ring]

/-- Exact spectral-radius certificate: all eigenvalue moduli are bounded by the displayed
finite radical, and an eigenvalue attains it. This includes every L ≥ 1. -/
theorem period8_alpha_minus_exact_finite_radius (L : ℕ) (hL : 0 < L) :
    (∀ i : Fin (8 * L),
      |(period8_target_matrix_isHermitian L (-1)).eigenvalues i| ≤ period8FiniteRadius L) ∧
    (∃ i : Fin (8 * L),
      |(period8_target_matrix_isHermitian L (-1)).eigenvalues i| = period8FiniteRadius L) := by
  constructor
  · intro i
    have h := Real.sqrt_le_sqrt (period8_alpha_minus_eigenvalue_square_le_finite_top L hL i)
    simpa only [Real.sqrt_sq_eq_abs, period8FiniteRadius] using h
  · obtain ⟨i, hi⟩ := period8_alpha_minus_finite_radius_attained_index L hL
    refine ⟨i, ?_⟩
    rw [hi]
    exact abs_of_nonneg (Real.sqrt_nonneg _)

end TargetA

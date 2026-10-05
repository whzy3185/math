import TargetA.Period8SharpEdge
import TargetA.Period8BlochAction

namespace TargetA

theorem period8_antiperiodic_parameter_re_lt_two {xi z : ℂ} {L : ℕ}
    (hL : L ≠ 0) (hxi : xi^2 = z) (hz : z^L = -1) :
    (xi^2 + xi⁻¹^2).re < 2 := by
  have hu := period8_xi_unit_from_holonomy hL hxi hz (by norm_num : (-1 : ℂ)^2 = 1)
  have hle := period8_unit_parameter_re_le_two hu
  have hinv : xi⁻¹ = (starRingEnd ℂ) xi := (period8_unit_conj_eq_inv hu).symm
  have hcre : (xi^2 + xi⁻¹^2).re = 2 * z.re := by
    rw [hinv, ← map_pow, hxi]
    simp
    ring
  have hpow : z^(2 * L) = 1 := by
    calc
      z^(2 * L) = (z^L)^2 := by ring_nf
      _ = 1 := by rw [hz]; norm_num
  have hn : ‖z‖ = 1 := Complex.norm_eq_one_of_pow_eq_one hpow (by omega)
  have hns : Complex.normSq z = 1 := by
    rw [← Complex.norm_mul_self_eq_normSq, hn]
    norm_num
  have hri : z.re * z.re + z.im * z.im = 1 := by
    simpa only [Complex.normSq_apply] using hns
  by_contra h
  have hre : z.re = 1 := by linarith
  have himsq : z.im * z.im = 0 := by nlinarith
  have him : z.im = 0 := (mul_self_eq_zero).mp himsq
  have hz1 : z = 1 := by
    apply Complex.ext
    · simpa using hre
    · simpa using him
  simp [hz1] at hz
  norm_num at hz

theorem period8_antiperiodic_holonomy_root_lt_edge {xi z : ℂ} {L : ℕ} {y : ℝ}
    (hL : L ≠ 0) (hxi : xi^2 = z) (hz : z^L = -1)
    (hroot : period8PolynomialC (y : ℂ) (xi^2 + xi⁻¹^2) = 0) :
    y < period8Edge := by
  apply period8_root_lt_edge (period8_antiperiodic_parameter_re_lt_two hL hxi hz)
  exact period8_unit_complex_root_is_real_root
    (period8_xi_unit_from_holonomy hL hxi hz (by norm_num)) hroot

/-- Every real eigenvalue in an antiperiodic fiber is strictly below the
continuous endpoint in squared modulus. This does not assert the finite
alpha-minus matrix-to-fiber decomposition. -/
theorem period8_antiperiodic_fiber_eigen_square_lt_edge
    {xi z : ℂ} {L : ℕ} {lambda : ℝ} {u : Fin 8 → ℂ}
    (hL : L ≠ 0) (hxi_sq : xi^2 = z) (hz : z^L = -1)
    (hEig : (period8Fiber xi).mulVec u = (lambda : ℂ) • u)
    (hu : u ≠ 0) : lambda^2 < period8Edge := by
  by_cases hlambda : lambda = 0
  · rw [hlambda]
    have he := period8_edge_ge_fifteen_halves
    norm_num
    linarith
  · have hcast : (lambda : ℂ) ≠ 0 := by exact_mod_cast hlambda
    have hxi : xi ≠ 0 := by
      intro hzero
      have hz0 : z = 0 := by simpa [hzero] using hxi_sq.symm
      simp [hz0, hL] at hz
    have hroot_fiber := period8_fiber_eigen_square_root
      (xi := xi) (lambda := (lambda : ℂ)) hxi hcast hEig hu
    have hroot : period8PolynomialC ((lambda^2 : ℝ) : ℂ)
        (xi^2 + xi⁻¹^2) = 0 := by
      rw [← period8_fiber_polynomialC_eq]
      simpa using hroot_fiber
    exact period8_antiperiodic_holonomy_root_lt_edge hL hxi_sq hz hroot

/-- An antiperiodic state can have nonzero Fourier mass only at a phase
whose L-th power is minus one. -/
theorem period8_antiperiodic_nonzero_dft_holonomy
    {N L : ℕ} [NeZero N] (F : ZMod N → Fin 8 → ℂ) (k : ZMod N)
    (hanti : period8CellTranslation (L : ZMod N) F = -F)
    (hk : period8CellDFT F k ≠ 0) :
    (ZMod.stdAddChar k)^L = -1 := by
  have hshift := congrArg (fun G => period8CellDFT G k) hanti
  rw [period8_cell_dft_translation] at hshift
  have hneg : period8CellDFT (-F) k = (-1 : ℂ) • period8CellDFT F k := by
    change ZMod.dft (-F) k = (-1 : ℂ) • ZMod.dft F k
    rw [map_neg]
    simp
  rw [hneg] at hshift
  have hchar : ZMod.stdAddChar ((L : ZMod N) * k) = (ZMod.stdAddChar k)^L := by
    rw [← nsmul_eq_mul, AddChar.map_nsmul_eq_pow]
  rw [hchar] at hshift
  exact (smul_left_injective ℂ hk) hshift

/-- The complete strict spectral statement for an antiperiodic sector of
the finite period-eight cell operator. A separate seam/reindexing lemma is
still needed to instantiate it for the raw alpha-minus adjacency matrix. -/
theorem period8_antiperiodic_cell_eigen_square_lt_edge
    {N L : ℕ} [NeZero N] (hL : L ≠ 0)
    (F : ZMod N → Fin 8 → ℂ) (lambda : ℝ)
    (hF : F ≠ 0)
    (hanti : period8CellTranslation (L : ZMod N) F = -F)
    (hEig : period8CellAction F = (lambda : ℂ) • F) :
    lambda^2 < period8Edge := by
  obtain ⟨k, hk⟩ := exists_nonzero_period8_cell_dft F hF
  obtain ⟨xi, hxi⟩ :=
    IsAlgClosed.exists_pow_nat_eq (ZMod.stdAddChar k) (by norm_num : 0 < 2)
  exact period8_antiperiodic_fiber_eigen_square_lt_edge hL hxi
    (period8_antiperiodic_nonzero_dft_holonomy F k hanti hk)
    (period8_cell_eigen_dft_fiber F (lambda : ℂ) k xi hxi hEig) hk

end TargetA

import TargetA.Period8ExactFiniteRadius

namespace TargetA

/-- The quartic used to specify the proposed constant in Conjecture 28. -/
def period8ConjecturePolynomial (x : ℝ) : ℝ :=
  x^4 - 2*x^3 - 6*x^2 + 12*x - 4

/-- Continuous period-eight radius, now identified with the quartic's largest real root. -/
noncomputable def period8ConjectureConstant : ℝ := Real.sqrt period8Edge

theorem period8_endpoint_quartic_factorization (x : ℝ) :
    period8Polynomial (x^2) 2 =
      period8ConjecturePolynomial x * period8ConjecturePolynomial (-x) := by
  unfold period8Polynomial period8ConjecturePolynomial
  ring

theorem period8_conjecture_constant_square :
    period8ConjectureConstant^2 = period8Edge := by
  unfold period8ConjectureConstant
  apply Real.sq_sqrt
  have h := period8_edge_ge_fifteen_halves
  linarith

theorem period8_conjecture_constant_nonneg : 0 ≤ period8ConjectureConstant :=
  Real.sqrt_nonneg _

/-- The negative argument cannot be the root selected by the positive continuous edge. -/
theorem period8_negative_argument_polynomial_pos {x : ℝ}
    (hx : 0 ≤ x) (hs : (15 / 2 : ℝ) ≤ x^2) :
    0 < period8ConjecturePolynomial (-x) := by
  have hm1 : 0 ≤ (x^2 - (15 / 2 : ℝ)) * (x^2 - 6) :=
    mul_nonneg (by linarith) (by linarith)
  have hm2 : 0 ≤ (2 * x) * (x^2 - 6) :=
    mul_nonneg (by linarith) (by linarith)
  unfold period8ConjecturePolynomial
  nlinarith

theorem period8_conjecture_constant_is_root :
    period8ConjecturePolynomial period8ConjectureConstant = 0 := by
  have hs : (15 / 2 : ℝ) ≤ period8ConjectureConstant^2 := by
    rw [period8_conjecture_constant_square]
    exact period8_edge_ge_fifteen_halves
  have hn := period8_negative_argument_polynomial_pos period8_conjecture_constant_nonneg hs
  have hp : period8Polynomial (period8ConjectureConstant^2) 2 = 0 := by
    rw [period8_conjecture_constant_square]
    exact period8_edge_is_boundary_root
  rw [period8_endpoint_quartic_factorization] at hp
  exact (mul_eq_zero.mp hp).resolve_right (ne_of_gt hn)

theorem period8_conjecture_constant_greatest_root {x : ℝ}
    (hx : period8ConjecturePolynomial x = 0) : x ≤ period8ConjectureConstant := by
  have hp : period8Polynomial (x^2) 2 = 0 := by
    rw [period8_endpoint_quartic_factorization, hx, zero_mul]
  have hb := period8_root_le_edge (by norm_num : (2 : ℝ) ≤ 2) hp
  have hs := Real.sqrt_le_sqrt hb
  rw [Real.sqrt_sq_eq_abs] at hs
  exact (le_abs_self x).trans hs

/-- Exact characterization of the paper's named constant by its largest-root definition. -/
theorem period8_conjecture_constant_largest_real_root :
    period8ConjecturePolynomial period8ConjectureConstant = 0 ∧
      ∀ x : ℝ, period8ConjecturePolynomial x = 0 → x ≤ period8ConjectureConstant :=
  ⟨period8_conjecture_constant_is_root, fun _ hx => period8_conjecture_constant_greatest_root hx⟩

/-- The explicit raw alpha-minus family lies strictly below that same algebraic constant. -/
theorem period8_alpha_minus_eigenvalue_abs_lt_conjecture_constant
    (L : ℕ) (hL : 0 < L) (i : Fin (8 * L)) :
    |(period8_target_matrix_isHermitian L (-1)).eigenvalues i| < period8ConjectureConstant := by
  have h := Real.sqrt_lt_sqrt (sq_nonneg ((period8_target_matrix_isHermitian L (-1)).eigenvalues i))
    (period8_alpha_minus_main_theorem L hL i)
  simpa only [Real.sqrt_sq_eq_abs, period8ConjectureConstant] using h

/-- Counterexample kernel in the conjecture's range: a largest-root characterization and
strict spectral improvement by the explicit raw signed matrix for every L ≥ 4. -/
theorem period8_conjecture28_strict_family (L : ℕ) (hL : 4 ≤ L) :
    (period8ConjecturePolynomial period8ConjectureConstant = 0 ∧
      ∀ x : ℝ, period8ConjecturePolynomial x = 0 → x ≤ period8ConjectureConstant) ∧
    ∀ i : Fin (8 * L),
      |(period8_target_matrix_isHermitian L (-1)).eigenvalues i| < period8ConjectureConstant := by
  refine ⟨period8_conjecture_constant_largest_real_root, ?_⟩
  intro i
  exact period8_alpha_minus_eigenvalue_abs_lt_conjecture_constant L (by omega) i

end TargetA

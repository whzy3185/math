import Mathlib

namespace TargetA

noncomputable def period8Fiber (xi : ℂ) : Matrix (Fin 8) (Fin 8) ℂ :=
  !![0, 1, 1, 0, 0, 0, xi⁻¹ ^ 2, xi⁻¹ ^ 2;
     1, 0, 1, 1, 0, 0, 0, -xi⁻¹ ^ 2;
     1, 1, 0, 1, -1, 0, 0, 0;
     0, 1, 1, 0, 1, 1, 0, 0;
     0, 0, -1, 1, 0, 1, -1, 0;
     0, 0, 0, 1, 1, 0, 1, -1;
     xi ^ 2, 0, 0, 0, -1, 1, 0, 1;
     xi ^ 2, -xi ^ 2, 0, 0, 0, -1, 1, 0]

noncomputable def period8ChiralInvolution (xi : ℂ) : Matrix (Fin 8) (Fin 8) ℂ :=
  !![0, 0, 0, 0, xi⁻¹, 0, 0, 0;
     0, 0, 0, 0, 0, -xi⁻¹, 0, 0;
     0, 0, 0, 0, 0, 0, xi⁻¹, 0;
     0, 0, 0, 0, 0, 0, 0, -xi⁻¹;
     xi, 0, 0, 0, 0, 0, 0, 0;
     0, -xi, 0, 0, 0, 0, 0, 0;
     0, 0, xi, 0, 0, 0, 0, 0;
     0, 0, 0, -xi, 0, 0, 0, 0]

set_option maxHeartbeats 1000000 in
theorem period8_chiral_square {xi : ℂ} (hxi : xi ≠ 0) :
    period8ChiralInvolution xi * period8ChiralInvolution xi =
      (1 : Matrix (Fin 8) (Fin 8) ℂ) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [period8ChiralInvolution, hxi]

set_option maxHeartbeats 1000000 in
theorem period8_chiral_anticommutes {xi : ℂ} (hxi : xi ≠ 0) :
    period8ChiralInvolution xi * period8Fiber xi +
      period8Fiber xi * period8ChiralInvolution xi =
        0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [period8ChiralInvolution, period8Fiber]
  all_goals
    field_simp [hxi]
    ring

end TargetA

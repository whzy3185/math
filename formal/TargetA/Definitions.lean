import Mathlib

namespace TargetA

def AdmissibleOrder (n : Nat) : Prop := 8 ≤ n ∧ Even n

def ResidueZero (n : Nat) : Prop := 8 ∣ n

theorem residueZero_mod (n : Nat) (h : ResidueZero n) : n % 8 = 0 := by
  exact Nat.mod_eq_zero_of_dvd h

theorem residueZero_even (n : Nat) (h : ResidueZero n) : Even n := by
  rcases h with ⟨k, rfl⟩
  exact ⟨4 * k, by ring⟩

theorem residueZero_admissible (n : Nat) (hn : 32 ≤ n) (h : ResidueZero n) :
    AdmissibleOrder n := by
  exact ⟨le_trans (by norm_num) hn, residueZero_even n h⟩

end TargetA

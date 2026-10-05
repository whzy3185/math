import Mathlib

namespace TargetA

def GapCharge (g : Nat) : Nat := g - 4

theorem gapCharge_mod_four (g : Nat) (hg : 4 ≤ g) :
    GapCharge g % 4 = g % 4 := by
  simp only [GapCharge]
  omega

theorem sector_after_gap (s g : Nat) (hg : 4 ≤ g) :
    (s + GapCharge g) % 4 = (s + g) % 4 := by
  simp only [GapCharge]
  omega

end TargetA

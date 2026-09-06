from pathlib import Path

root = Path('formal/lean-lonely-runner/project')
(root / 'LonelyRunner/SecondSign.lean').write_text(r'''import LonelyRunner.SecondCoefficients
import Mathlib.Algebra.Ring.NegOnePow

namespace LonelyRunner

/-- Odd integer parity gives the negative sign in `(-1)^natAbs`. -/
lemma negOnePow_natAbs_eq_neg_one {z : ℤ} (hz : Odd z) :
    ((-1 : ℤ) ^ z.natAbs) = -1 := by
  calc
    ((-1 : ℤ) ^ z.natAbs) = (z.negOnePow : ℤ) := by
      symm
      exact Int.coe_negOnePow ℤ z
    _ = -1 := by
      exact congrArg (fun u : ℤˣ => (u : ℤ)) (Int.negOnePow_odd z hz)

/-- Even integer parity gives the positive sign in `(-1)^natAbs`. -/
lemma negOnePow_natAbs_eq_one {z : ℤ} (hz : Even z) :
    ((-1 : ℤ) ^ z.natAbs) = 1 := by
  calc
    ((-1 : ℤ) ^ z.natAbs) = (z.negOnePow : ℤ) := by
      symm
      exact Int.coe_negOnePow ℤ z
    _ = 1 := by
      exact congrArg (fun u : ℤˣ => (u : ℤ)) (Int.negOnePow_even z hz)

lemma secondCoeff_neg_of_odd_of_bracket_pos
    (k : ℕ) (s : Relation)
    (hodd : Odd (coordSum s))
    (hbr : 0 < secondBracket k s) :
    secondCoeff k s < 0 := by
  unfold secondCoeff
  rw [negOnePow_natAbs_eq_neg_one hodd]
  nlinarith

lemma secondCoeff_pos_of_even_of_bracket_pos
    (k : ℕ) (s : Relation)
    (heven : Even (coordSum s))
    (hbr : 0 < secondBracket k s) :
    0 < secondCoeff k s := by
  unfold secondCoeff
  rw [negOnePow_natAbs_eq_one heven]
  simpa using hbr

lemma odd_of_secondCoeff_neg_of_bracket_pos
    (k : ℕ) (s : Relation)
    (hbr : 0 < secondBracket k s)
    (hneg : secondCoeff k s < 0) :
    Odd (coordSum s) := by
  rw [← Int.not_even_iff_odd]
  intro heven
  have hpos := secondCoeff_pos_of_even_of_bracket_pos k s heven hbr
  linarith

/-- On the `k=3` support, negativity is exactly odd coordinate sum. -/
theorem secondCoeff_neg_iff_odd_k3 {s : Relation} (hs : InSecondSupport 3 s) :
    secondCoeff 3 s < 0 ↔ Odd (coordSum s) := by
  have hbr := secondBracket_pos_k3 hs
  constructor
  · exact odd_of_secondCoeff_neg_of_bracket_pos 3 s hbr
  · intro hodd
    exact secondCoeff_neg_of_odd_of_bracket_pos 3 s hodd hbr

/-- On the `k=4` support, negativity is exactly odd coordinate sum. -/
theorem secondCoeff_neg_iff_odd_k4 {s : Relation} (hs : InSecondSupport 4 s) :
    secondCoeff 4 s < 0 ↔ Odd (coordSum s) := by
  have hbr := secondBracket_pos_k4 hs
  constructor
  · exact odd_of_secondCoeff_neg_of_bracket_pos 4 s hbr
  · intro hodd
    exact secondCoeff_neg_of_odd_of_bracket_pos 4 s hodd hbr

/-- On the `k=9` support, negativity is exactly odd coordinate sum. -/
theorem secondCoeff_neg_iff_odd_k9 {s : Relation} (hs : InSecondSupport 9 s) :
    secondCoeff 9 s < 0 ↔ Odd (coordSum s) := by
  have hbr := secondBracket_pos_k9 hs
  constructor
  · exact odd_of_secondCoeff_neg_of_bracket_pos 9 s hbr
  · intro hodd
    exact secondCoeff_neg_of_odd_of_bracket_pos 9 s hodd hbr

#print axioms secondCoeff_neg_iff_odd_k3
#print axioms secondCoeff_neg_iff_odd_k4
#print axioms secondCoeff_neg_iff_odd_k9

end LonelyRunner
''')

main = root / 'LonelyRunner.lean'
s = main.read_text()
imp = 'import LonelyRunner.SecondSign\n'
if imp not in s:
    s += imp
main.write_text(s)

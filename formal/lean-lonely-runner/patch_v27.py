from pathlib import Path

p = Path('formal/lean-lonely-runner/project/LonelyRunner/SecondAnalytic.lean')
s = p.read_text()
start = s.index('/-- If one cosine is positive')
end = s.index('/-- Algebraic sign of `G_k`', start)
replacement = r'''/-- If one cosine is positive, then the four-factor product is strictly below `128`. -/
theorem secondPValue_lt_128
    (c0 c1 c2 c3 : ℝ)
    (h0lo : -1 ≤ c0) (h1lo : -1 ≤ c1) (h2lo : -1 ≤ c2) (h3lo : -1 ≤ c3)
    (h0hi : c0 ≤ 1) (h1hi : c1 ≤ 1) (h2hi : c2 ≤ 1) (h3hi : c3 ≤ 1)
    (hpos : 0 < c0 ∨ 0 < c1 ∨ 0 < c2 ∨ 0 < c3) :
    secondPValue c0 c1 c2 c3 < 128 := by
  let f0 : ℝ := 2 - 2 * c0
  let f1 : ℝ := 2 - 2 * c1
  let f2 : ℝ := 2 - 2 * c2
  let f3 : ℝ := 2 - 2 * c3
  have hf0n : 0 ≤ f0 := by dsimp [f0]; linarith
  have hf1n : 0 ≤ f1 := by dsimp [f1]; linarith
  have hf2n : 0 ≤ f2 := by dsimp [f2]; linarith
  have hf3n : 0 ≤ f3 := by dsimp [f3]; linarith
  have hf0u : f0 ≤ 4 := by dsimp [f0]; linarith
  have hf1u : f1 ≤ 4 := by dsimp [f1]; linarith
  have hf2u : f2 ≤ 4 := by dsimp [f2]; linarith
  have hf3u : f3 ≤ 4 := by dsimp [f3]; linarith
  have hP : f0 * f1 * f2 * f3 < 128 := by
    rcases hpos with h0 | hrest
    · have hf0lt : f0 < 2 := by dsimp [f0]; linarith
      exact fourProduct_lt_128_of_first_lt_two hf0n hf1n hf2n hf3n hf0lt hf1u hf2u hf3u
    · rcases hrest with h1 | hrest
      · have hf1lt : f1 < 2 := by dsimp [f1]; linarith
        calc
          f0 * f1 * f2 * f3 = f1 * f0 * f2 * f3 := by ring
          _ < 128 := fourProduct_lt_128_of_first_lt_two hf1n hf0n hf2n hf3n hf1lt hf0u hf2u hf3u
      · rcases hrest with h2 | h3
        · have hf2lt : f2 < 2 := by dsimp [f2]; linarith
          calc
            f0 * f1 * f2 * f3 = f2 * f0 * f1 * f3 := by ring
            _ < 128 := fourProduct_lt_128_of_first_lt_two hf2n hf0n hf1n hf3n hf2lt hf0u hf1u hf3u
        · have hf3lt : f3 < 2 := by dsimp [f3]; linarith
          calc
            f0 * f1 * f2 * f3 = f3 * f0 * f1 * f2 := by ring
            _ < 128 := fourProduct_lt_128_of_first_lt_two hf3n hf0n hf1n hf2n hf3lt hf0u hf1u hf2u
  simpa [secondPValue, f0, f1, f2, f3] using hP

'''
s = s[:start] + replacement + s[end:]
s = s.replace('/-- Second certificate along the natural-speed orbit. -/\ndef secondCertificateAt',
              '/-- Second certificate along the natural-speed orbit. -/\nnoncomputable def secondCertificateAt', 1)
p.write_text(s)

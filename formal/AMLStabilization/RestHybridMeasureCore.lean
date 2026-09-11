import Mathlib
import AMLStabilization.HybridFiberCore
import AMLStabilization.PairedSelectorMeasureCore

open Set MeasureTheory

namespace AMLStabilization

/-- The hybrid choice of one component from every paired remaining coordinate
has pushforward equal to the ordinary remaining-coordinate product measure,
multiplied by the total mass of the unused copy. -/
theorem map_pairedRestHybrid
    {α : Type*} [MeasurableSpace α] {n : ℕ}
    (i : Fin (n + 1))
    (μ : Fin n → Measure α) [∀ j, IsFiniteMeasure (μ j)] :
    (Measure.pi (fun j => (μ j).prod (μ j))).map (pairedRestHybrid i) =
      (∏ j, μ j Set.univ) • Measure.pi μ := by
  simpa [pairedRestHybrid] using
    (map_pi_prod_select μ
      (fun j => (i.succAbove j : Fin (n + 1)).val < i.val))

/-- Integrability is preserved when an ordinary rest-coordinate function is
composed with the hybrid selector and integrated against all paired rest
coordinates.  Finiteness of the unused-copy mass is automatic from the finite
coordinate measures. -/
theorem Integrable.comp_pairedRestHybrid
    {α : Type*} [MeasurableSpace α] {n : ℕ}
    (i : Fin (n + 1))
    (μ : Fin n → Measure α) [∀ j, IsFiniteMeasure (μ j)]
    {g : (Fin n → α) → ℝ}
    (hg : Integrable g (Measure.pi μ)) :
    Integrable (fun z : Fin n → α × α => g (pairedRestHybrid i z))
      (Measure.pi (fun j => (μ j).prod (μ j))) := by
  let ν : Measure (Fin n → α × α) :=
    Measure.pi (fun j => (μ j).prod (μ j))
  let c : ℝ≥0∞ := ∏ j, μ j Set.univ
  have hc : c ≠ ∞ := by
    dsimp [c]
    exact ENNReal.prod_ne_top fun j _ => measure_ne_top (μ j) Set.univ
  have hscaled : Integrable g (c • Measure.pi μ) := hg.smul_measure hc
  have hmapped : Integrable g (Measure.map (pairedRestHybrid i) ν) := by
    rw [show Measure.map (pairedRestHybrid i) ν = c • Measure.pi μ by
      simpa [ν, c] using map_pairedRestHybrid i μ]
    exact hscaled
  have hsel : AEMeasurable (pairedRestHybrid i : (Fin n → α × α) → (Fin n → α)) ν := by
    apply Measurable.aemeasurable
    apply measurable_pi_lambda
    intro j
    by_cases h : (i.succAbove j : Fin (n + 1)).val < i.val
    · simpa [pairedRestHybrid, h] using
        (measurable_pi_apply j).snd
    · simpa [pairedRestHybrid, h] using
        (measurable_pi_apply j).fst
  have hcomp := hmapped.comp_aemeasurable hsel
  simpa [ν, Function.comp_def] using hcomp

/-- Integral transport from an integrability hypothesis.  This is the version
used by the box Poincare assembly, where integrability of the fiber-energy
function is itself obtained from Fubini. -/
theorem integral_pairedRestHybrid_of_integrable
    {α : Type*} [MeasurableSpace α] {n : ℕ}
    (i : Fin (n + 1))
    (μ : Fin n → Measure α) [∀ j, IsFiniteMeasure (μ j)]
    (g : (Fin n → α) → ℝ)
    (hg : Integrable g (Measure.pi μ)) :
    (∫ z : Fin n → α × α, g (pairedRestHybrid i z)
        ∂Measure.pi (fun j => (μ j).prod (μ j))) =
      (∏ j, μ j Set.univ).toReal *
        ∫ x : Fin n → α, g x ∂Measure.pi μ := by
  let ν : Measure (Fin n → α × α) :=
    Measure.pi (fun j => (μ j).prod (μ j))
  let c : ℝ≥0∞ := ∏ j, μ j Set.univ
  have hc : c ≠ ∞ := by
    dsimp [c]
    exact ENNReal.prod_ne_top fun j _ => measure_ne_top (μ j) Set.univ
  have hscaled : Integrable g (c • Measure.pi μ) := hg.smul_measure hc
  have hmapped : Integrable g (Measure.map (pairedRestHybrid i) ν) := by
    rw [show Measure.map (pairedRestHybrid i) ν = c • Measure.pi μ by
      simpa [ν, c] using map_pairedRestHybrid i μ]
    exact hscaled
  have hsel : AEMeasurable (pairedRestHybrid i : (Fin n → α × α) → (Fin n → α)) ν := by
    apply Measurable.aemeasurable
    apply measurable_pi_lambda
    intro j
    by_cases h : (i.succAbove j : Fin (n + 1)).val < i.val
    · simpa [pairedRestHybrid, h] using
        (measurable_pi_apply j).snd
    · simpa [pairedRestHybrid, h] using
        (measurable_pi_apply j).fst
  have hmapInt := integral_map hsel hmapped.aestronglyMeasurable
  calc
    (∫ z : Fin n → α × α, g (pairedRestHybrid i z) ∂ν) =
        ∫ x : Fin n → α, g x ∂Measure.map (pairedRestHybrid i) ν := by
      exact hmapInt.symm
    _ = ∫ x : Fin n → α, g x ∂(c • Measure.pi μ) := by
      rw [show Measure.map (pairedRestHybrid i) ν = c • Measure.pi μ by
        simpa [ν, c] using map_pairedRestHybrid i μ]
    _ = c.toReal * ∫ x : Fin n → α, g x ∂Measure.pi μ := by
      simp [MeasureTheory.integral_smul_measure, smul_eq_mul]
    _ = (∏ j, μ j Set.univ).toReal *
        ∫ x : Fin n → α, g x ∂Measure.pi μ := by rfl

/-- Integral transport form of `map_pairedRestHybrid`.  Integrating a function
of the selected hybrid rest-coordinates against all paired rest-coordinates
produces exactly the unused-copy mass factor times the ordinary product
integral. -/
theorem integral_pairedRestHybrid
    {α : Type*} [MeasurableSpace α] {n : ℕ}
    (i : Fin (n + 1))
    (μ : Fin n → Measure α) [∀ j, IsFiniteMeasure (μ j)]
    (g : (Fin n → α) → ℝ)
    (hg : StronglyMeasurable g) :
    (∫ z : Fin n → α × α, g (pairedRestHybrid i z)
        ∂Measure.pi (fun j => (μ j).prod (μ j))) =
      (∏ j, μ j Set.univ).toReal *
        ∫ x : Fin n → α, g x ∂Measure.pi μ := by
  let ν : Measure (Fin n → α × α) :=
    Measure.pi (fun j => (μ j).prod (μ j))
  have hsel : Measurable (pairedRestHybrid i : (Fin n → α × α) → (Fin n → α)) := by
    apply measurable_pi_lambda
    intro j
    by_cases h : (i.succAbove j : Fin (n + 1)).val < i.val
    · simpa [pairedRestHybrid, h] using
        (measurable_pi_apply j).snd
    · simpa [pairedRestHybrid, h] using
        (measurable_pi_apply j).fst
  have hmapInt := integral_map
    (μ := ν) hsel.aemeasurable hg.aestronglyMeasurable
  calc
    (∫ z : Fin n → α × α, g (pairedRestHybrid i z) ∂ν) =
        ∫ x : Fin n → α, g x ∂Measure.map (pairedRestHybrid i) ν := by
      exact hmapInt.symm
    _ = ∫ x : Fin n → α, g x
        ∂((∏ j, μ j Set.univ) • Measure.pi μ) := by
      rw [show Measure.map (pairedRestHybrid i) ν =
          (∏ j, μ j Set.univ) • Measure.pi μ by
        simpa [ν] using map_pairedRestHybrid i μ]
    _ = (∏ j, μ j Set.univ).toReal *
        ∫ x : Fin n → α, g x ∂Measure.pi μ := by
      simp [MeasureTheory.integral_smul_measure, smul_eq_mul]

end AMLStabilization

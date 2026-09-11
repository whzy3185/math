import Mathlib

open Set MeasureTheory

namespace AMLStabilization

/-- Selecting, independently in each coordinate, either the first or the second
component of a paired finite-product sample pushes the paired product measure
to the original product measure multiplied by the total mass of the unused
copy.  This is the measure-theoretic bookkeeping needed for hybrid-coordinate
Poincare estimates on non-normalized boxes. -/
theorem map_pi_prod_select
    {ι α : Type*} [Fintype ι] [MeasurableSpace α]
    (μ : ι → Measure α) [∀ i, IsFiniteMeasure (μ i)]
    (pickSecond : ι → Prop) [DecidablePred pickSecond] :
    (Measure.pi (fun i => (μ i).prod (μ i))).map
        (fun z i => if pickSecond i then (z i).2 else (z i).1) =
      (∏ i, μ i Set.univ) • Measure.pi μ := by
  let sel : (i : ι) → (α × α → α) :=
    fun i z => if pickSecond i then z.2 else z.1
  have hsel_meas : ∀ i, AEMeasurable (sel i) ((μ i).prod (μ i)) := by
    intro i
    by_cases hi : pickSecond i
    · simpa [sel, hi] using
        (measurable_snd.aemeasurable : AEMeasurable (Prod.snd : α × α → α) ((μ i).prod (μ i)))
    · simpa [sel, hi] using
        (measurable_fst.aemeasurable : AEMeasurable (Prod.fst : α × α → α) ((μ i).prod (μ i)))
  have hcoord : ∀ i,
      ((μ i).prod (μ i)).map (sel i) = (μ i Set.univ) • μ i := by
    intro i
    by_cases hi : pickSecond i
    · simp [sel, hi, Measure.map_snd_prod]
    · simp [sel, hi, Measure.map_fst_prod]
  have hmap := Measure.pi_map_pi
    (μ := fun i => (μ i).prod (μ i)) (f := sel) hsel_meas
  have hmap' :
      (Measure.pi (fun i => (μ i).prod (μ i))).map
          (fun z i => sel i (z i)) =
        Measure.pi (fun i => (μ i Set.univ) • μ i) := by
    simpa only [hcoord] using hmap
  letI : ∀ i, IsFiniteMeasure ((μ i Set.univ) • μ i) := fun i =>
    { measure_univ_lt_top := by
        rw [Measure.smul_apply MeasurableSet.univ]
        exact ENNReal.mul_lt_top (measure_lt_top (μ i) Set.univ)
          (measure_lt_top (μ i) Set.univ) }
  have hscaled :
      Measure.pi (fun i => (μ i Set.univ) • μ i) =
        (∏ i, μ i Set.univ) • Measure.pi μ := by
    apply Measure.pi_eq
    intro s hs
    simp [Measure.pi_pi, Measure.smul_apply, hs, Finset.prod_mul_distrib]
  simpa [sel] using hmap'.trans hscaled

end AMLStabilization

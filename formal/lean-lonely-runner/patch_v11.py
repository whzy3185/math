from pathlib import Path

root = Path('formal/lean-lonely-runner/project')
p = root / 'LonelyRunner/FirstLaurent.lean'
p.write_text(r'''import LonelyRunner.LowQuarter
import LonelyRunner.FirstRelationShape
import LonelyRunner.FourierOrthogonality
import Mathlib.Algebra.BigOperators.Finsupp.Basic

namespace LonelyRunner

set_option maxRecDepth 100000
set_option maxHeartbeats 0

/-!
# A kernel-computable Laurent certificate

We deliberately use the underlying sparse coefficient table `Relation →₀ ℤ`, equipped with an
explicit convolution product.  This avoids the noncomputable multiplication instances of
`AddMonoidAlgebra` while retaining exactly the Laurent algebra needed by the proof.
-/

abbrev Laurent4 := Relation →₀ ℤ

/-- Standard basis exponent in the Laurent exponent lattice. -/
def basisRelation (i : Fin 4) : Relation := fun j => if j = i then 1 else 0

/-- A sparse Laurent monomial. -/
def laurentMonomial (r : Relation) (c : ℤ) : Laurent4 := Finsupp.single r c

/-- Explicit convolution product of two sparse Laurent coefficient tables. -/
def laurentMul (p q : Laurent4) : Laurent4 :=
  p.sum fun r c =>
    q.sum fun s d =>
      laurentMonomial (r + s) (c * d)

/-- The cube used in the certificate. -/
def laurentCube (p : Laurent4) : Laurent4 := laurentMul (laurentMul p p) p

/-- The basic factor `2-zᵢ-zᵢ⁻¹`. -/
def qBase (i : Fin 4) : Laurent4 :=
  laurentMonomial zeroRelation 2 +
  laurentMonomial (basisRelation i) (-1) +
  laurentMonomial (-basisRelation i) (-1)

/-- The factor `6+Σᵢ(zᵢ+zᵢ⁻¹)`. -/
def firstLinear : Laurent4 :=
  laurentMonomial zeroRelation 6 +
  (laurentMonomial (basisRelation 0) 1 + laurentMonomial (-basisRelation 0) 1) +
  (laurentMonomial (basisRelation 1) 1 + laurentMonomial (-basisRelation 1) 1) +
  (laurentMonomial (basisRelation 2) 1 + laurentMonomial (-basisRelation 2) 1) +
  (laurentMonomial (basisRelation 3) 1 + laurentMonomial (-basisRelation 3) 1)

/-- The compact first Laurent certificate. -/
def firstLaurentPolynomial : Laurent4 :=
  - laurentMul
      (laurentMul
        (laurentMul
          (laurentMul firstLinear (laurentCube (qBase 0)))
          (laurentCube (qBase 1)))
        (laurentCube (qBase 2)))
      (laurentCube (qBase 3))

/-- The same polynomial reconstructed from the explicit coefficient table. -/
def firstCoeffPolynomial : Laurent4 :=
  (supportBox.map fun r => laurentMonomial r (firstCoeff r)).sum

/-- Exact finite coefficient identity, checked by kernel reduction on the sparse tables. -/
theorem firstLaurentPolynomial_eq_firstCoeffPolynomial :
    firstLaurentPolynomial = firstCoeffPolynomial := by decide

/-- Additivity of the integer frequency pairing. -/
theorem relationDot_add (r s : Relation) (v : Fin 4 → ℤ) :
    relationDot (r + s) v = relationDot r v + relationDot s v := by
  simp [relationDot, add_mul, Finset.sum_add_distrib]

/-- The zero relation produces frequency zero. -/
theorem relationDot_zero (v : Fin 4 → ℤ) : relationDot zeroRelation v = 0 := by
  simp [relationDot, zeroRelation]

/-- Fourier modes multiply according to addition of Laurent exponents. -/
theorem relationMode_add (r s : Relation) (v : Fin 4 → ℤ) (t : ℝ) :
    relationMode (r + s) v t = relationMode r v t * relationMode s v t := by
  unfold relationMode fourierMode
  rw [relationDot_add]
  rw [show
      ((((relationDot r v + relationDot s v : ℤ) : ℂ) *
          (2 * (Real.pi : ℂ) * Complex.I)) * (t : ℂ)) =
        (((relationDot r v : ℂ) * (2 * (Real.pi : ℂ) * Complex.I)) * (t : ℂ)) +
        (((relationDot s v : ℂ) * (2 * (Real.pi : ℂ) * Complex.I)) * (t : ℂ)) by
      push_cast
      ring]
  exact Complex.exp_add _ _

/-- The zero Laurent exponent evaluates to one. -/
theorem relationMode_zero (v : Fin 4 → ℤ) (t : ℝ) :
    relationMode zeroRelation v t = 1 := by
  simp [relationMode, fourierMode, relationDot_zero]

/-- Coefficient evaluation at one Laurent exponent. -/
noncomputable def coeffEvalHom (v : Fin 4 → ℤ) (t : ℝ) (r : Relation) : ℤ →+ ℂ where
  toFun := fun c => (c : ℂ) * relationMode r v t
  map_zero' := by simp
  map_add' := by
    intro a b
    push_cast
    ring

/-- Additive evaluation of a sparse Laurent table on the four-speed orbit. -/
noncomputable def evalLaurentHom (v : Fin 4 → ℤ) (t : ℝ) : Laurent4 →+ ℂ :=
  Finsupp.liftAddHom (fun r => coeffEvalHom v t r)

noncomputable def evalLaurent (v : Fin 4 → ℤ) (t : ℝ) (p : Laurent4) : ℂ :=
  evalLaurentHom v t p

@[simp] theorem evalLaurent_zero (v : Fin 4 → ℤ) (t : ℝ) :
    evalLaurent v t 0 = 0 := by simp [evalLaurent]

@[simp] theorem evalLaurent_add (v : Fin 4 → ℤ) (t : ℝ) (p q : Laurent4) :
    evalLaurent v t (p + q) = evalLaurent v t p + evalLaurent v t q := by
  exact (evalLaurentHom v t).map_add p q

@[simp] theorem evalLaurent_neg (v : Fin 4 → ℤ) (t : ℝ) (p : Laurent4) :
    evalLaurent v t (-p) = -evalLaurent v t p := by
  exact (evalLaurentHom v t).map_neg p

/-- Evaluation of one sparse monomial. -/
@[simp] theorem evalLaurent_monomial (v : Fin 4 → ℤ) (t : ℝ) (r : Relation) (c : ℤ) :
    evalLaurent v t (laurentMonomial r c) = (c : ℂ) * relationMode r v t := by
  simp [evalLaurent, evalLaurentHom, coeffEvalHom, laurentMonomial]

/-- Evaluation respects the explicit convolution product. -/
theorem evalLaurent_mul (v : Fin 4 → ℤ) (t : ℝ) (p q : Laurent4) :
    evalLaurent v t (laurentMul p q) = evalLaurent v t p * evalLaurent v t q := by
  classical
  unfold laurentMul evalLaurent
  simp_rw [map_finsuppSum, evalLaurent_monomial]
  rw [Finsupp.sum_mul]
  simp_rw [Finsupp.mul_sum, relationMode_add]
  push_cast
  congr 1
  ext r c
  congr 1
  ext s d
  ring

/-- Evaluation of the explicit cube. -/
theorem evalLaurent_cube (v : Fin 4 → ℤ) (t : ℝ) (p : Laurent4) :
    evalLaurent v t (laurentCube p) = (evalLaurent v t p) ^ 3 := by
  unfold laurentCube
  rw [evalLaurent_mul, evalLaurent_mul]
  ring

/-- Dot product with a standard exponent basis vector. -/
theorem relationDot_basis (v : Fin 4 → ℤ) (i : Fin 4) :
    relationDot (basisRelation i) v = v i := by
  classical
  simp [relationDot, basisRelation]

/-- Dot product with the negative basis vector. -/
theorem relationDot_neg_basis (v : Fin 4 → ℤ) (i : Fin 4) :
    relationDot (-basisRelation i) v = -v i := by
  simp [relationDot, basisRelation]

/-- Real phase angle for a signed integer speed. -/
noncomputable def phaseAngleInt (v : Fin 4 → ℤ) (i : Fin 4) (t : ℝ) : ℝ :=
  2 * Real.pi * ((v i : ℝ) * t)

/-- The positive basis mode is the ordinary unit-circle exponential. -/
theorem relationMode_basis (v : Fin 4 → ℤ) (i : Fin 4) (t : ℝ) :
    relationMode (basisRelation i) v t =
      Complex.exp ((phaseAngleInt v i t : ℂ) * Complex.I) := by
  unfold relationMode fourierMode phaseAngleInt
  rw [relationDot_basis]
  congr 1
  push_cast
  ring

/-- The negative basis mode has the opposite phase. -/
theorem relationMode_neg_basis (v : Fin 4 → ℤ) (i : Fin 4) (t : ℝ) :
    relationMode (-basisRelation i) v t =
      Complex.exp ((-phaseAngleInt v i t : ℂ) * Complex.I) := by
  unfold relationMode fourierMode phaseAngleInt
  rw [relationDot_neg_basis]
  congr 1
  push_cast
  ring

/-- Symmetric Euler identity. -/
theorem exp_I_add_exp_neg_I (x : ℝ) :
    Complex.exp ((x : ℂ) * Complex.I) +
      Complex.exp ((-x : ℂ) * Complex.I) = (2 * Real.cos x : ℝ) := by
  rw [Complex.exp_mul_I, Complex.exp_mul_I]
  simp [Real.cos_neg, Real.sin_neg]
  push_cast
  ring

/-- Evaluation of `2-zᵢ-zᵢ⁻¹`. -/
theorem eval_qBase (v : Fin 4 → ℤ) (i : Fin 4) (t : ℝ) :
    evalLaurent v t (qBase i) =
      ((2 - 2 * Real.cos (phaseAngleInt v i t) : ℝ) : ℂ) := by
  simp only [qBase, evalLaurent_add, evalLaurent_monomial]
  rw [relationMode_zero, relationMode_basis, relationMode_neg_basis]
  have h := exp_I_add_exp_neg_I (phaseAngleInt v i t)
  push_cast at h ⊢
  norm_num at h ⊢
  linarith

/-- Evaluation of the linear factor is twice `3+Σ cos θᵢ`. -/
theorem eval_firstLinear (v : Fin 4 → ℤ) (t : ℝ) :
    evalLaurent v t firstLinear =
      ((2 * (3 + Real.cos (phaseAngleInt v 0 t) + Real.cos (phaseAngleInt v 1 t) +
        Real.cos (phaseAngleInt v 2 t) + Real.cos (phaseAngleInt v 3 t)) : ℝ) : ℂ) := by
  simp only [firstLinear, evalLaurent_add, evalLaurent_monomial]
  rw [relationMode_zero,
      relationMode_basis, relationMode_neg_basis,
      relationMode_basis, relationMode_neg_basis,
      relationMode_basis, relationMode_neg_basis,
      relationMode_basis, relationMode_neg_basis]
  have h0 := exp_I_add_exp_neg_I (phaseAngleInt v 0 t)
  have h1 := exp_I_add_exp_neg_I (phaseAngleInt v 1 t)
  have h2 := exp_I_add_exp_neg_I (phaseAngleInt v 2 t)
  have h3 := exp_I_add_exp_neg_I (phaseAngleInt v 3 t)
  push_cast at h0 h1 h2 h3 ⊢
  norm_num at h0 h1 h2 h3 ⊢
  linarith

/-- Signed-integer version of the real certificate formula. -/
noncomputable def firstCertificateAtInt (v : Fin 4 → ℤ) (t : ℝ) : ℝ :=
  firstCertificateValue
    (Real.cos (phaseAngleInt v 0 t))
    (Real.cos (phaseAngleInt v 1 t))
    (Real.cos (phaseAngleInt v 2 t))
    (Real.cos (phaseAngleInt v 3 t))

/-- Evaluating the compact sparse Laurent certificate gives exactly the real certificate. -/
theorem eval_firstLaurentPolynomial (v : Fin 4 → ℤ) (t : ℝ) :
    evalLaurent v t firstLaurentPolynomial = (firstCertificateAtInt v t : ℂ) := by
  unfold firstLaurentPolynomial
  rw [evalLaurent_neg,
      evalLaurent_mul, evalLaurent_mul, evalLaurent_mul, evalLaurent_mul,
      eval_firstLinear,
      evalLaurent_cube, eval_qBase,
      evalLaurent_cube, eval_qBase,
      evalLaurent_cube, eval_qBase,
      evalLaurent_cube, eval_qBase]
  unfold firstCertificateAtInt firstCertificateValue
  push_cast
  ring

/-- Explicit finite Fourier sum of the first coefficient table. -/
noncomputable def firstFourierSum (v : Fin 4 → ℤ) (t : ℝ) : ℂ :=
  (supportBox.map fun r => (firstCoeff r : ℂ) * relationMode r v t).sum

/-- Evaluating the coefficient reconstruction gives the explicit Fourier sum. -/
theorem eval_firstCoeffPolynomial (v : Fin 4 → ℤ) (t : ℝ) :
    evalLaurent v t firstCoeffPolynomial = firstFourierSum v t := by
  unfold firstCoeffPolynomial firstFourierSum
  induction supportBox with
  | nil => simp
  | cons r rs ih => simp [ih]

/-- Pointwise bridge from the finite Fourier expansion to the real certificate. -/
theorem firstFourierSum_eq_certificate (v : Fin 4 → ℤ) (t : ℝ) :
    firstFourierSum v t = (firstCertificateAtInt v t : ℂ) := by
  calc
    firstFourierSum v t = evalLaurent v t firstCoeffPolynomial :=
      (eval_firstCoeffPolynomial v t).symm
    _ = evalLaurent v t firstLaurentPolynomial := by
      rw [firstLaurentPolynomial_eq_firstCoeffPolynomial]
    _ = (firstCertificateAtInt v t : ℂ) := eval_firstLaurentPolynomial v t

#print axioms firstLaurentPolynomial_eq_firstCoeffPolynomial
#print axioms evalLaurent_mul
#print axioms firstFourierSum_eq_certificate

end LonelyRunner
''')

from pathlib import Path

root = Path('formal/lean-lonely-runner/project')
p = root / 'LonelyRunner/FirstLaurent.lean'
p.write_text(r'''import LonelyRunner.LowQuarter
import LonelyRunner.FirstRelationShape
import LonelyRunner.FourierOrthogonality

namespace LonelyRunner

set_option maxRecDepth 200000
set_option maxHeartbeats 0

/-!
# The first certificate via a fully computable sparse Laurent model

The formal proof does not use `Finsupp` multiplication.  A sparse Laurent polynomial is a sorted
list of exponent/coefficient pairs.  Multiplication is implemented by raw convolution followed by a
computable normalization.  This keeps the coefficient identity kernel-reducible while evaluation is
proved abstractly from Fourier characters.
-/

abbrev SparseLaurent := List (Relation × ℤ)

/-- Standard basis exponent. -/
def basisRelation (i : Fin 4) : Relation := fun j => if j = i then 1 else 0

/-- Lexicographic order used only to canonicalize sparse coefficient tables. -/
def relationLexLT (r s : Relation) : Bool :=
  if r 0 < s 0 then true else if s 0 < r 0 then false else
  if r 1 < s 1 then true else if s 1 < r 1 then false else
  if r 2 < s 2 then true else if s 2 < r 2 then false else
  decide (r 3 < s 3)

/-- Insert a nonzero term into a canonical sparse list, merging equal exponents. -/
def insertNonzero (r : Relation) (c : ℤ) : SparseLaurent → SparseLaurent
  | [] => [(r, c)]
  | (s, d) :: xs =>
      if h : r = s then
        let e := c + d
        if e = 0 then xs else (s, e) :: xs
      else if relationLexLT r s then
        (r, c) :: (s, d) :: xs
      else
        (s, d) :: insertNonzero r c xs

/-- Insert a term, dropping zero coefficients. -/
def insertTerm (r : Relation) (c : ℤ) (p : SparseLaurent) : SparseLaurent :=
  if c = 0 then p else insertNonzero r c p

/-- Canonicalize a raw list of Laurent terms. -/
def normalizeSparse (p : SparseLaurent) : SparseLaurent :=
  p.foldr (fun rc acc => insertTerm rc.1 rc.2 acc) []

/-- Raw convolution terms. -/
def rawMul (p q : SparseLaurent) : SparseLaurent :=
  p.flatMap fun rc => q.map fun sd => (rc.1 + sd.1, rc.2 * sd.2)

/-- Computable sparse Laurent multiplication. -/
def sparseMul (p q : SparseLaurent) : SparseLaurent := normalizeSparse (rawMul p q)

def sparseCube (p : SparseLaurent) : SparseLaurent := sparseMul (sparseMul p p) p

def sparseNeg (p : SparseLaurent) : SparseLaurent := p.map fun rc => (rc.1, -rc.2)

/-- The factor `2-zᵢ-zᵢ⁻¹`. -/
def qBase (i : Fin 4) : SparseLaurent :=
  [(zeroRelation, 2), (basisRelation i, -1), (-basisRelation i, -1)]

/-- The factor `6+Σᵢ(zᵢ+zᵢ⁻¹)`. -/
def firstLinear : SparseLaurent :=
  [(zeroRelation, 6),
   (basisRelation 0, 1), (-basisRelation 0, 1),
   (basisRelation 1, 1), (-basisRelation 1, 1),
   (basisRelation 2, 1), (-basisRelation 2, 1),
   (basisRelation 3, 1), (-basisRelation 3, 1)]

/-- Compact sparse Laurent certificate. -/
def firstLaurentPolynomial : SparseLaurent :=
  sparseNeg <|
    sparseMul
      (sparseMul
        (sparseMul
          (sparseMul firstLinear (sparseCube (qBase 0)))
          (sparseCube (qBase 1)))
        (sparseCube (qBase 2)))
      (sparseCube (qBase 3))

/-- Explicit coefficient reconstruction. -/
def firstCoeffPolynomial : SparseLaurent :=
  normalizeSparse (supportBox.map fun r => (r, firstCoeff r))

/-- Kernel-computable coefficient identity. -/
theorem firstLaurentPolynomial_eq_firstCoeffPolynomial :
    firstLaurentPolynomial = firstCoeffPolynomial := by decide

/-- Additivity of the integer frequency pairing. -/
theorem relationDot_add (r s : Relation) (v : Fin 4 → ℤ) :
    relationDot (r + s) v = relationDot r v + relationDot s v := by
  simp [relationDot, add_mul, Finset.sum_add_distrib]

/-- Zero exponent has zero frequency. -/
theorem relationDot_zero (v : Fin 4 → ℤ) : relationDot zeroRelation v = 0 := by
  simp [relationDot, zeroRelation]

/-- Fourier characters multiply under addition of exponents. -/
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

@[simp] theorem relationMode_zero (v : Fin 4 → ℤ) (t : ℝ) :
    relationMode zeroRelation v t = 1 := by
  simp [relationMode, fourierMode, relationDot_zero]

/-- Evaluation of an arbitrary sparse term list. -/
noncomputable def evalSparse (v : Fin 4 → ℤ) (t : ℝ) (p : SparseLaurent) : ℂ :=
  (p.map fun rc => (rc.2 : ℂ) * relationMode rc.1 v t).sum

@[simp] theorem evalSparse_nil (v : Fin 4 → ℤ) (t : ℝ) : evalSparse v t [] = 0 := by
  simp [evalSparse]

@[simp] theorem evalSparse_cons (v : Fin 4 → ℤ) (t : ℝ) (r : Relation) (c : ℤ)
    (p : SparseLaurent) :
    evalSparse v t ((r,c)::p) = (c : ℂ) * relationMode r v t + evalSparse v t p := by
  simp [evalSparse]

@[simp] theorem evalSparse_append (v : Fin 4 → ℤ) (t : ℝ) (p q : SparseLaurent) :
    evalSparse v t (p ++ q) = evalSparse v t p + evalSparse v t q := by
  simp [evalSparse, List.map_append, List.sum_append]

/-- Insertion preserves evaluation while adding the requested monomial. -/
theorem eval_insertNonzero (v : Fin 4 → ℤ) (t : ℝ) (r : Relation) (c : ℤ)
    (p : SparseLaurent) :
    evalSparse v t (insertNonzero r c p) =
      (c : ℂ) * relationMode r v t + evalSparse v t p := by
  induction p with
  | nil => simp [insertNonzero]
  | cons hd xs ih =>
      rcases hd with ⟨s,d⟩
      by_cases hrs : r = s
      · subst s
        simp [insertNonzero, hrs]
        by_cases hz : c + d = 0
        · simp [hz]
          have hcast : ((c + d : ℤ) : ℂ) = 0 := by exact_mod_cast hz
          push_cast at hcast
          ring_nf at hcast ⊢
          exact hcast
        · simp [hz]
          push_cast
          ring
      · by_cases hlt : relationLexLT r s
        · simp [insertNonzero, hrs, hlt]
          ring
        · simp [insertNonzero, hrs, hlt, ih]
          ring

/-- Zero-aware insertion has the same evaluation law. -/
theorem eval_insertTerm (v : Fin 4 → ℤ) (t : ℝ) (r : Relation) (c : ℤ)
    (p : SparseLaurent) :
    evalSparse v t (insertTerm r c p) =
      (c : ℂ) * relationMode r v t + evalSparse v t p := by
  by_cases hc : c = 0
  · subst c
    simp [insertTerm]
  · simp [insertTerm, hc, eval_insertNonzero]

/-- Normalization preserves the value of the raw term list. -/
theorem eval_normalizeSparse (v : Fin 4 → ℤ) (t : ℝ) (p : SparseLaurent) :
    evalSparse v t (normalizeSparse p) = evalSparse v t p := by
  induction p with
  | nil => simp [normalizeSparse]
  | cons hd xs ih =>
      rcases hd with ⟨r,c⟩
      simp [normalizeSparse, eval_insertTerm, ih]

/-- Evaluation of one row of a raw convolution. -/
theorem eval_mulRow (v : Fin 4 → ℤ) (t : ℝ) (r : Relation) (c : ℤ)
    (q : SparseLaurent) :
    evalSparse v t (q.map fun sd => (r + sd.1, c * sd.2)) =
      ((c : ℂ) * relationMode r v t) * evalSparse v t q := by
  induction q with
  | nil => simp
  | cons hd qs ih =>
      rcases hd with ⟨s,d⟩
      simp [evalSparse, relationMode_add, ih]
      push_cast
      ring

/-- Raw convolution evaluates multiplicatively. -/
theorem eval_rawMul (v : Fin 4 → ℤ) (t : ℝ) (p q : SparseLaurent) :
    evalSparse v t (rawMul p q) = evalSparse v t p * evalSparse v t q := by
  induction p with
  | nil => simp [rawMul]
  | cons hd ps ih =>
      rcases hd with ⟨r,c⟩
      simp only [rawMul, List.flatMap_cons]
      rw [evalSparse_append, eval_mulRow, ih]
      simp [evalSparse]
      ring

/-- Sparse multiplication evaluates multiplicatively. -/
theorem eval_sparseMul (v : Fin 4 → ℤ) (t : ℝ) (p q : SparseLaurent) :
    evalSparse v t (sparseMul p q) = evalSparse v t p * evalSparse v t q := by
  rw [sparseMul, eval_normalizeSparse, eval_rawMul]

/-- Sparse cube evaluates as a cube. -/
theorem eval_sparseCube (v : Fin 4 → ℤ) (t : ℝ) (p : SparseLaurent) :
    evalSparse v t (sparseCube p) = (evalSparse v t p)^3 := by
  unfold sparseCube
  rw [eval_sparseMul, eval_sparseMul]
  ring

/-- Negating coefficients negates evaluation. -/
theorem eval_sparseNeg (v : Fin 4 → ℤ) (t : ℝ) (p : SparseLaurent) :
    evalSparse v t (sparseNeg p) = - evalSparse v t p := by
  induction p with
  | nil => simp [sparseNeg]
  | cons hd ps ih =>
      rcases hd with ⟨r,c⟩
      simp [sparseNeg, evalSparse, ih]
      push_cast
      ring

/-- Dot product with a basis exponent. -/
theorem relationDot_basis (v : Fin 4 → ℤ) (i : Fin 4) :
    relationDot (basisRelation i) v = v i := by
  classical
  simp [relationDot, basisRelation]

/-- Dot product with a negative basis exponent. -/
theorem relationDot_neg_basis (v : Fin 4 → ℤ) (i : Fin 4) :
    relationDot (-basisRelation i) v = -v i := by
  simp [relationDot, basisRelation]

/-- Real phase angle. -/
noncomputable def phaseAngleInt (v : Fin 4 → ℤ) (i : Fin 4) (t : ℝ) : ℝ :=
  2 * Real.pi * ((v i : ℝ) * t)

theorem relationMode_basis (v : Fin 4 → ℤ) (i : Fin 4) (t : ℝ) :
    relationMode (basisRelation i) v t =
      Complex.exp ((phaseAngleInt v i t : ℂ) * Complex.I) := by
  unfold relationMode fourierMode phaseAngleInt
  rw [relationDot_basis]
  congr 1
  push_cast
  ring

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
      Complex.exp ((-x : ℂ) * Complex.I) = ((2 * Real.cos x : ℝ) : ℂ) := by
  rw [Complex.exp_mul_I, Complex.exp_mul_I]
  simp [Real.cos_neg, Real.sin_neg]
  push_cast
  ring

/-- Evaluation of `2-zᵢ-zᵢ⁻¹`. -/
theorem eval_qBase (v : Fin 4 → ℤ) (i : Fin 4) (t : ℝ) :
    evalSparse v t (qBase i) = ((2 - 2 * Real.cos (phaseAngleInt v i t) : ℝ) : ℂ) := by
  rw [show qBase i = [(zeroRelation, 2), (basisRelation i, -1), (-basisRelation i, -1)] by rfl]
  simp only [evalSparse_cons, evalSparse_nil]
  rw [relationMode_zero, relationMode_basis, relationMode_neg_basis]
  have h := exp_I_add_exp_neg_I (phaseAngleInt v i t)
  calc
    (2 : ℂ) * 1 + (-1 : ℂ) * Complex.exp ((phaseAngleInt v i t : ℂ) * Complex.I) +
        ((-1 : ℂ) * Complex.exp ((-phaseAngleInt v i t : ℂ) * Complex.I) + 0) =
        (2 : ℂ) -
          (Complex.exp ((phaseAngleInt v i t : ℂ) * Complex.I) +
           Complex.exp ((-phaseAngleInt v i t : ℂ) * Complex.I)) := by ring
    _ = (2 : ℂ) - ((2 * Real.cos (phaseAngleInt v i t) : ℝ) : ℂ) := by rw [h]
    _ = ((2 - 2 * Real.cos (phaseAngleInt v i t) : ℝ) : ℂ) := by push_cast; ring

/-- Evaluation of the linear factor. -/
theorem eval_firstLinear (v : Fin 4 → ℤ) (t : ℝ) :
    evalSparse v t firstLinear =
      ((2 * (3 + Real.cos (phaseAngleInt v 0 t) + Real.cos (phaseAngleInt v 1 t) +
        Real.cos (phaseAngleInt v 2 t) + Real.cos (phaseAngleInt v 3 t)) : ℝ) : ℂ) := by
  simp only [firstLinear, evalSparse_cons, evalSparse_nil]
  rw [relationMode_zero,
      relationMode_basis, relationMode_neg_basis,
      relationMode_basis, relationMode_neg_basis,
      relationMode_basis, relationMode_neg_basis,
      relationMode_basis, relationMode_neg_basis]
  have h0 := exp_I_add_exp_neg_I (phaseAngleInt v 0 t)
  have h1 := exp_I_add_exp_neg_I (phaseAngleInt v 1 t)
  have h2 := exp_I_add_exp_neg_I (phaseAngleInt v 2 t)
  have h3 := exp_I_add_exp_neg_I (phaseAngleInt v 3 t)
  calc
    _ = (6 : ℂ) +
        (Complex.exp ((phaseAngleInt v 0 t : ℂ) * Complex.I) + Complex.exp ((-phaseAngleInt v 0 t : ℂ) * Complex.I)) +
        (Complex.exp ((phaseAngleInt v 1 t : ℂ) * Complex.I) + Complex.exp ((-phaseAngleInt v 1 t : ℂ) * Complex.I)) +
        (Complex.exp ((phaseAngleInt v 2 t : ℂ) * Complex.I) + Complex.exp ((-phaseAngleInt v 2 t : ℂ) * Complex.I)) +
        (Complex.exp ((phaseAngleInt v 3 t : ℂ) * Complex.I) + Complex.exp ((-phaseAngleInt v 3 t : ℂ) * Complex.I)) := by ring
    _ = (6 : ℂ) + ((2 * Real.cos (phaseAngleInt v 0 t) : ℝ) : ℂ) +
        ((2 * Real.cos (phaseAngleInt v 1 t) : ℝ) : ℂ) +
        ((2 * Real.cos (phaseAngleInt v 2 t) : ℝ) : ℂ) +
        ((2 * Real.cos (phaseAngleInt v 3 t) : ℝ) : ℂ) := by rw [h0, h1, h2, h3]
    _ = ((2 * (3 + Real.cos (phaseAngleInt v 0 t) + Real.cos (phaseAngleInt v 1 t) +
        Real.cos (phaseAngleInt v 2 t) + Real.cos (phaseAngleInt v 3 t)) : ℝ) : ℂ) := by
          push_cast
          ring

/-- Signed-integer real certificate. -/
noncomputable def firstCertificateAtInt (v : Fin 4 → ℤ) (t : ℝ) : ℝ :=
  firstCertificateValue
    (Real.cos (phaseAngleInt v 0 t))
    (Real.cos (phaseAngleInt v 1 t))
    (Real.cos (phaseAngleInt v 2 t))
    (Real.cos (phaseAngleInt v 3 t))

/-- The compact sparse certificate evaluates to the real certificate. -/
theorem eval_firstLaurentPolynomial (v : Fin 4 → ℤ) (t : ℝ) :
    evalSparse v t firstLaurentPolynomial = (firstCertificateAtInt v t : ℂ) := by
  unfold firstLaurentPolynomial
  rw [eval_sparseNeg,
      eval_sparseMul, eval_sparseMul, eval_sparseMul, eval_sparseMul,
      eval_firstLinear,
      eval_sparseCube, eval_qBase,
      eval_sparseCube, eval_qBase,
      eval_sparseCube, eval_qBase,
      eval_sparseCube, eval_qBase]
  unfold firstCertificateAtInt firstCertificateValue
  push_cast
  ring

/-- Explicit finite Fourier sum. -/
noncomputable def firstFourierSum (v : Fin 4 → ℤ) (t : ℝ) : ℂ :=
  (supportBox.map fun r => (firstCoeff r : ℂ) * relationMode r v t).sum

/-- The coefficient reconstruction evaluates to the explicit Fourier sum. -/
theorem eval_firstCoeffPolynomial (v : Fin 4 → ℤ) (t : ℝ) :
    evalSparse v t firstCoeffPolynomial = firstFourierSum v t := by
  unfold firstCoeffPolynomial firstFourierSum
  rw [eval_normalizeSparse]
  induction supportBox with
  | nil => simp [evalSparse]
  | cons r rs ih => simp [evalSparse, ih]

/-- Pointwise Fourier expansion of the first certificate. -/
theorem firstFourierSum_eq_certificate (v : Fin 4 → ℤ) (t : ℝ) :
    firstFourierSum v t = (firstCertificateAtInt v t : ℂ) := by
  calc
    firstFourierSum v t = evalSparse v t firstCoeffPolynomial :=
      (eval_firstCoeffPolynomial v t).symm
    _ = evalSparse v t firstLaurentPolynomial := by rw [firstLaurentPolynomial_eq_firstCoeffPolynomial]
    _ = (firstCertificateAtInt v t : ℂ) := eval_firstLaurentPolynomial v t

#print axioms firstLaurentPolynomial_eq_firstCoeffPolynomial
#print axioms eval_sparseMul
#print axioms firstFourierSum_eq_certificate

end LonelyRunner
''')

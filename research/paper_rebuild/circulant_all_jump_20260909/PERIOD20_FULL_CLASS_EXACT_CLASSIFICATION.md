# Exact full-class classification at period 20

Date: 2026-09-15

Status: **Verified by exact finite computation**.

This note records the stronger conclusion already certified by `verify_period20_full_class_jump10.py`.  It is deliberately labeled `Verified`, not `Proved`, under the project evidence convention because the final exclusion step consists of finitely many exact endpoint certificates.

---

## 1. Complete variational class

Take

\[
p=20,\qquad s=10.
\]

There are

\[
2^{19}=524288
\]

legal flux words and exactly

\[
\boxed{13648}
\]

dihedral orbits.

Let

\[
R(Q)=\max_{|z|=1}\rho(H_Q(z))^2.
\]

Define the four-defect word

\[
\boxed{
Q_j=+1\iff j\in\{0,2,4,6\},
}
\]

with every other flux negative.

---

## 2. Exact finite classification

The exact verifier proves all of the following.

1. Endpoint even-moment inequalities through order `14` reduce the `13648` dihedral orbits to exactly
   \[
   \boxed{160}
   \]
   candidates compatible with an edge at most `8`.

2. For the four-defect target, the all-phase determinant at
   \[
   y_0=31/4
   \]
   factors into the two palindromic factors recorded in `PERIOD20_FOUR_DEFECT_BEATS_TWO_DEFECT_THEOREM.md`; the resulting Sturm polynomial has no zero on `[-2,2]`, and a reference-fiber Sylvester certificate gives
   \[
   \boxed{R(Q^{(4)})<31/4.}
   \]

3. Every one of the other `159` moment-surviving dihedral orbits has an endpoint `z=1` or `z=-1` for which
   \[
   31I-4H(z)^2
   \]
   has a nonpositive leading principal minor.  Hence each competitor satisfies
   \[
   R(Q)\ge31/4.
   \]

The first failing minor occurs at order at most `19` in every case.

Therefore the exact finite computation establishes

\[
\boxed{
Q^{(4)}\text{ is the unique period-20 full-class optimizer, modulo dihedral symmetry.}
}
\tag{2.1}
\]

In particular period `20` is the first audited layer where the complete periodic optimizer is no longer a two-defect word.

---

## 3. Evidence status

The statement (2.1) is stronger than the analytic theorem

\[
R(Q^{(4)})<31/4<R_{2\rm def},
\]

but its proof currently uses exact enumeration of a finite orbit set.  Hence:

- `PERIOD20_FOUR_DEFECT_BEATS_TWO_DEFECT_THEOREM.md`: **Proved** analytic separation from the complete two-defect family;
- the present full-class uniqueness statement: **Verified** exact finite classification.

A conceptual proof should replace the `159` endpoint minor certificates by a period-independent local/moment obstruction before this result is promoted to a structural theorem.

---

## 4. Variational transition ladder

The strongest audited full-class data are now:

\[
\begin{array}{c|c|c}
p&\text{full-class optimizer}&\text{status}\\ \hline
8&2\text{ defects, distance }2&\text{Proved}\\
12&2\text{ defects, distance }2&\text{Verified}\\
16&2\text{ defects, balanced distance }4&\text{Verified}\\
20&4\text{ defects }\{0,2,4,6\}&\text{Verified}.
\end{array}
\]

Thus the defect-number transition in the complete periodic class occurs no later than period `20`, and at period `20` it is exact.

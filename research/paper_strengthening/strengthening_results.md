# Period-eight strengthening results

## Current decision table

| Task | Verdict | Result | Proof status | Article value |
|---|---|---|---|---|
| 1A exact finite positive sector | PASS | `rho(A_(8L,+))^2=eta` for every `L>=1` | analytic + independent symbolic audit | Tier A; replaces the rational bound as the natural main theorem |
| 1B negative sector | PASS | exact formula `4+sqrt(8+2cos(pi/L)+sqrt(26-6cos(pi/L)))` | analytic + independent symbolic audit | Tier B; concise corollary of the closed dispersion law |
| 2A minimal period | PASS | no legal displayed period below 8 has squared edge below 8 | moment reduction + nine finite exact certificates + independent audit | Tier A; explains why period eight is genuinely first |
| proof hygiene | PASS | lift, cyclic, reflection, and cell-repetition invariance; primitive-period formulation | analytic + independent exact matrix audit | closes the orbit reductions used by existing theorems |
| full period-eight dispersion | PASS | all four squared branches, exact endpoints, simple fibers, and exact gaps | analytic + independent symbolic audit | completes rather than enlarges the period-eight calculation |
| 2B quantitative period-eight gap | NOT EXPLORED — procedural stop only | no investigation performed | no mathematical verdict | outside the final closure round |
| 3A M4 | NOT EXPLORED — procedural stop only | no investigation performed | no mathematical verdict | backup test not triggered because the chiral theorem succeeded |
| 3B M5 | NOT EXPLORED — procedural stop only | no investigation performed | no mathematical verdict | outside scope |
| 3C general defect rigidity | NOT EXPLORED — procedural stop only | no investigation performed | no mathematical verdict | retain the proved M1--M3 necessary obstruction only |
| 4A/4B natural monomial half-cell chiral criterion/reduction | PASS | iff criterion `tau_(i+m)=-tau_i`, equivalent to half-periodic `Q` with negative half-cell flux; general `2m -> m` squared reduction | analytic + independent exact matrix audit | Tier A; supplies the general mechanism behind period eight |
| 5 new periodic families | NOT EXPLORED — procedural stop only | no investigation performed | no mathematical verdict | expressly excluded from the final closure round |

## Procedural-stop correction and final closure decision

The user-defined strong-stop condition requires two of three outcomes:

1. exact finite witness theorem;
2. period-eight rigidity/minimal-period theorem;
3. general chiral or defect structural theorem.

The earlier table used `STOPPED` and `KILLED` as if they were mathematical
verdicts.  For directions never investigated, that wording was inaccurate;
they are now marked `NOT EXPLORED — procedural stop only`.

The final authorized round pursued only the natural monomial half-cell chiral
class and proved the strong iff criterion.  Together with items 1 and 2, all
three structural targets are now present.  The repository is therefore marked

```text
MATHEMATICAL_STRENGTHENING_CLOSED
```

No M4 feasibility test was needed, and no further theorem-search route is
authorized in this project stage.

## Strongest theorem package after final strengthening

### Theorem I: general half-cell chiral mechanism

For a `2m`-periodic Hamilton-gauge word, the natural monomial operator
`D T_m`, after the Bloch normalization

```text
gamma_m(z)^2=(-1)^m z^(-1),
```

induces a chiral involution if and only if

```text
tau_(i+m)=-tau_i.
```

Equivalently, `Q_i=tau_i tau_(i+1)` is `m`-periodic and has negative
half-cell flux.  The fiber spectrum is symmetric and its squared problem
reduces from dimension `2m` to dimension `m`.

### Theorem II: exact period-eight solvability

For every `L>=1`, the positive-holonomy period-eight signing satisfies

```text
rho(A_(8L,+))^2=eta=4+sqrt(10+2sqrt(5)).
```

For every `L>=4`, this is strictly smaller than the twisted benchmark.

The complete four squared branches are

```text
y_(sigma,tau)(c)=4+sigma sqrt(8+c+tau sqrt(26-3c)).
```

In particular, for `-2<=c<=2`, the upper squared-fiber branch is

```text
r(c)=4+sqrt(8+c+sqrt(26-3c)).
```

The negative-holonomy ring has the exact squared edge

```text
4+sqrt(8+2cos(pi/L)+sqrt(26-6cos(pi/L))),
```

which is strictly below eta and converges to eta.

### Theorem III: first occurrence

Eight is the smallest primitive period of a legal Hamilton-gauge signing with
squared Bloch edge below eight.  The alternating period-two phase and its cell
repetitions attain eight.

### Theorem IV: rigidity at first occurrence

At primitive period eight, the antipodal two-defect phase is the unique
sub-eight class modulo cyclic translation, reflection, and the precisely
stated lift/cell conventions.

### Structural support

The period-eight trichotomy and the general M1--M3 defect obstruction remain
part of the package.  Lift and dihedral invariance now justify the orbit
reductions analytically, and zone folding justifies the primitive-period
formulation.

## Formal-verification boundary

The frozen Lean project remains unchanged. It proves the alpha = +1 strict
comparison through the rational separator in Hermitian eigenvalue form. The
exact edge, negative sector, minimal-period result, invariance lemmas, full
dispersion, and general chiral criterion are analytic/finite-exact results
with independent symbolic verifiers, not Lean claims.

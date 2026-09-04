# Period-eight strengthening results

## Current decision table

| Task | Verdict | Result | Proof status | Article value |
|---|---|---|---|---|
| 1A exact finite positive sector | PASS | `rho(A_(8L,+))^2=eta` for every `L>=1` | analytic + independent symbolic audit | Tier A; replaces the rational bound as the natural main theorem |
| 1B negative sector | PASS | exact formula `4+sqrt(8+2cos(pi/L)+sqrt(26-6cos(pi/L)))` | analytic + independent symbolic audit | Tier B; concise corollary of the closed dispersion law |
| 2A minimal period | PASS | no legal displayed period below 8 has squared edge below 8 | moment reduction + nine finite exact certificates + independent audit | Tier A; explains why period eight is genuinely first |
| 2B quantitative period-eight gap | STOPPED | not run | strong-stop criterion reached | do not spend proof budget unless later reviewers demand it |
| 3A M4 | STOPPED | not run | strong-stop criterion reached | existing M1--M3 already powers the minimal-period reduction |
| 3B M5 | KILLED | prerequisite M4 not run | stop rule | excluded |
| 3C general defect rigidity | STOPPED | not run | strong-stop criterion reached | retain frozen necessary obstruction only |
| 4A/4B general chiral criterion/reduction | STOPPED | not run | strong-stop criterion reached | current package does not justify a SIGMA narrative |
| 5 new periodic families | KILLED | prerequisite Tasks 3/4 not pursued | stop rule | no brute-force search |

## Strong-stop decision

The user-defined strong-stop condition requires two of three outcomes:

1. exact finite witness theorem;
2. period-eight rigidity/minimal-period theorem;
3. general chiral or defect structural theorem.

Items 1 and 2 are now proved. Mathematical exploration stops here. The next
work is literature reconstruction, venue calibration, narrative selection,
and manuscript architecture.

## Strongest theorem package after strengthening

### Theorem A: exact finite period-eight edge

For every `L>=1`, the positive-holonomy period-eight signing satisfies

```text
rho(A_(8L,+))^2=eta=4+sqrt(10+2sqrt(5)).
```

For every `L>=4`, this is strictly smaller than the twisted benchmark.

### Theorem B: closed finite-sector dispersion

For `-2<=c<=2`, the upper squared-fiber branch is

```text
r(c)=4+sqrt(8+c+sqrt(26-3c)).
```

The negative-holonomy ring has the exact squared edge

```text
4+sqrt(8+2cos(pi/L)+sqrt(26-6cos(pi/L))),
```

which is strictly below eta and converges to eta.

### Theorem C: minimal period below eight

No legal periodic phase of displayed period `p<8` has squared Bloch edge
below eight. The alternating period-two phase and its even repetitions attain
eight. Period eight admits the unique antipodal two-defect class below eight,
modulo the stated symmetries.

### Structural support

The period-eight trichotomy and the general M1--M3 defect obstruction remain
part of the package. The minimal-period proof shows that the moment theorem
has a concrete role rather than being an unrelated final section.

## Formal-verification boundary

The frozen Lean project remains unchanged. It proves the alpha = +1 strict
comparison through the rational separator in Hermitian eigenvalue form. The
new exact-edge, negative-sector, and minimal-period results are analytic and
finite-exact results with independent symbolic verifiers, not Lean claims.

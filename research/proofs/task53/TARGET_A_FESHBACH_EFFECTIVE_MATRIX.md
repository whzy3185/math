# Feshbach Effective Matrix: Task 53 Boundary

> **Superseded and corrected by Task 55.** The conditional `r`-dimensional
> problem below is itself dimensionally wrong: one G6 interface contributes
> two squared modes at `c6`. It must not be used as an open dependency.

The old Task 53 proposal used `r` truncated positive-branch G6 modes and
formally wrote

```text
H_eff=c6 I_r+T+R.
```

The identity omitted the negative unsquared partner at every interface. Task
55 proves `rank P_(H6,{c6})=2`, constructs `2r` Gram-orthonormalized columns,
proves the codimension-`2r` complement gap, and obtains the valid equation

```text
det(H_eff(z)-z I_(2r))=0.
```

No leading coupling coefficient, holonomy sign law, or finite-ring
simplicity formula follows from that corrected norm-level theorem.

Historical Task 53 status: `CONDITIONAL_ON_D1_COMPLEMENT_RESOLVENT`.
Final status of the displayed `r`-dimensional proposal:
`FALSIFIED_AS_STATED`; corrected exact-`2r` Feshbach theorem:
`COMPUTER_ASSISTED_PROVED`.

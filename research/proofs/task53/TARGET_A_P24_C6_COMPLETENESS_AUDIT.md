# p<=24 Completeness Audit

For periods at most 16, all 2626 inherited dihedral orbit records are checked.
Each non-target is covered by an exact `F_k>0 => R>8` exclusion, an inherited
Rayleigh quotient above `c6_upper`, or one of the sixteen Task 53 witnesses.

For each period 17 through 24, the exact closure file satisfies

```text
moment_excluded_through_F16 + survivors = legal_dihedral_orbits.
```

All moment exclusions imply `R>8`. Every non-target survivor certificate has
an exact integer Rayleigh quotient above `c6_upper`; target repetitions are
identified explicitly. Source hashes bind the audit to the Task 51 CSV and
the low-period frontier. Removing an orbit or changing a witness makes the
checker fail.

The audit is finite and proves nothing about primitive period 25 or larger.

Status: COMPLETE for `p<=24`.

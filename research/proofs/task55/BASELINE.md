# Target A Task 55 Baseline

## Repository State

Reference checkpoint and actual starting `HEAD`:

```text
bd1934da29a2eb56cf2045554c00c104d79a7959
```

Branch:

```text
agent/target-a-discovery-snapshot
```

At reconciliation, local and remote had ahead/behind count `0/0` and merge
base `bd1934d`. The working tree contained preserved Task 55 work in progress,
so its classification was `LOCAL_WIP`. No branch switch, worktree, reset, or
pull was used.

## Frozen Manuscripts

The formal manuscript directories were not modified. Their Git tree hashes
at the integration base are

```text
English  59e3a8f73a152ef06f994e979b7219a3365efeae
Chinese  57ae03fb5b90866f84d0d72b414008678e8f5004
```

Task 55 changes are confined to research proofs, certificates, review
records, and scripts.

## Inherited Theorems

The following inherited conclusions remain valid after the Task 55 audit:

1. The original conjecture holds for every even `8<=n<=30` and first fails at
   `n=32`.
2. The period-eight edge is
   `eta=4+sqrt(10+2sqrt(5))`.
3. The single-G6 squared spectral top is `c6`, isolated from the remaining
   single-interface spectrum by `delta6=1/100`.
4. The global tent IMS error is
   `(240R-342)/(R(2R^2+1))<=120/R^2`.
5. Exact rational LDL certificates cover every even `48<=n<240`, while the
   global IMS argument covers every even `n>=240`. Thus every even `n>=48`
   has an explicit certified counterexample.
6. Pointed compactness and the tight/dichotomy/normalized-vanishing
   trichotomy survive. The unrestricted common liminf remains open.

## Mandatory Rank Correction

The Task 55 hostile audit falsified one inherited auxiliary chain. For the
single G6 interface,

```text
(Ku)_i=(-1)^i u_(9-i),
K^2=-I,
KA=-AK,
KH=HK.
```

The simple positive and negative `A` roots therefore square to the same
`H=A^2` level, and

```text
rank P_(H6,{c6})=2.
```

Consequently the old exact-`r` count, codimension-`r` complement, and
problem-specific `r x r` Feshbach application are false as stated. Any
accepted replacement must use `2r` localized columns. This correction does
not affect the independently proved `n>=48` theorem.

## Evidence Policy

No read-only discovery is promoted solely from a subagent report. A theorem
is integrated only after a producer artifact and an implementation-independent
checker agree. Bounded negative searches remain bounded evidence, and
high-precision values remain high-precision evidence unless converted to
exact or interval-certified statements.

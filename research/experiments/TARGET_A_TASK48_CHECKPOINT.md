# Target A Task 48 Safe-Stop Checkpoint

The broad Task 48 was superseded by the focused Task 48A after completion of
its first atomic certificate batch.  This checkpoint preserves only work that
has a clear evidence status.

## Classification

### VALID_COMPLETE_RESULT

- `research/experiments/exact_frontier/`
- `research/scripts/target_a_task48_frontier.py`

The generator rebuilt all 184 Task 47 `F16` survivors, identified the 125
states already selected in Task 47, and certified the remaining 59 states.
The exact partition contains 183 strict `R>eta` certificates, one repeated
period-8 equality at displayed period 24, and zero unresolved states.  Thus
the experimental frontier through displayed period 24 is closed.

### VALID_PARTIAL_RESULT

- `research/experiments/TARGET_A_TASK48_BASELINE.md`

This records the verified entry state and manuscript freeze.  It remains a
valid provenance record although the broad Task 48 did not continue.

### TEMPORARY / INCOMPLETE

None.  No incomplete generated artifact was written to the repository.

### FAILED / OBSOLETE

None.

## Checkpoint validation

- Frontier accounting: `TASK48_FRONTIER_CHECKPOINT_PASS`
- Full tests: `275 passed, 3 skipped, 20 subtests passed`
- Task 47 regression: pass
- Minimality certificate: pass
- Computational evidence: pass
- Submission artifact manifest: pass
- Formal English and Chinese manuscript trees changed: no

The exact frontier is retained as input evidence for Task 48A.  No formal
theorem or manuscript claim is changed by this checkpoint.

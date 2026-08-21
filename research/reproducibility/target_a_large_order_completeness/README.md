# Large-Order Record-Set Audit

Run the complete audit from the repository root with Python 3.12:

```text
python research/scripts/target_a_record_set_audit.py --n 24 26 28 30
```

The Python route emits fixed-weight FKM bracelet representatives into a
temporary disk-mapped table. The separately compiled C route scans all binary
words, builds each dihedral orbit directly, and consumes the matching table
entry. Temporary tables are deleted after each order.

The per-order JSON files contain defect-count and orbit-size histograms,
represented-space totals, exact mismatch counters, traversal closure, and the
status of ordering-independent record-level set equality. `summary.json`
collects the four production orders and identifies the exact C source hash and
compiler used for the recorded run.

Approximate temporary disk requirements are `2^n` bytes for order `n`; the
largest run therefore needs 1 GiB. The independent scanner additionally uses
a `2^n`-bit visited map in memory. Hashes are provenance metadata only and do
not replace exact set consumption.

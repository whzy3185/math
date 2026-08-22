# Target A Task 51 Baseline

- Repository HEAD: `82895863a59f8014d547544a7b3bb18aaa0cc8e5`
- Branch: `agent/target-a-discovery-snapshot`
- Entry working tree: clean
- Entry ahead/behind: `0/0`
- Remote HEAD: `82895863a59f8014d547544a7b3bb18aaa0cc8e5`
- Architecture: `arm64`
- Python: `3.12.13`
- NumPy: `2.3.5`
- SciPy: not installed in the clean Task 50/51 runtime
- SymPy: `1.14.0`
- mpmath: `1.3.0`
- English manuscript tree: `59e3a8f73a152ef06f994e979b7219a3365efeae`
- Chinese manuscript tree: `57ae03fb5b90866f84d0d72b414008678e8f5004`

## Entry Regression

The literal full-suite entry run reported `345 passed, 3 skipped, 20
subtests passed` and one infrastructure failure.  The failure was the stale
Task 49 proof-freeze test: it treated the additive, already verified Task 50
proof directory as a forbidden Task 49-era modification.  No mathematical
test failed.  Task 51 repairs the guard so that it rejects modifications,
deletions, or renames of old proof artifacts while permitting later tasks to
add isolated proof directories.  The post-repair baseline is recorded by the
Task 51 verifier.

The formal English and Chinese manuscript trees remain frozen at the hashes
above.  Task 51 writes only to its experiment, discovery, proof, review, and
reproducibility directories plus shared scripts and tests.

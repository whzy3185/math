# Mycielski M6 Hall-ratio certificate

**Exact verified finite result:** `rho(M6)=10/3`, with `M2=K2` and ordinary Mycielski iteration. M6 has 47 vertices.

Start with `PROOF.md` for the graph convention, structural recurrence, compressed enumeration theorem, certificate explanation, and explicit 20-vertex extremal witness. No claim of publication novelty or complete extremal classification is made.

## Verify independently of numerical optimization

Run with Python 3, standard library only:

```
python check_exact_certificate.py
```

The checker reconstructs the graph, regenerates all 857 maximal independent sets using Bron–Kerbosch, verifies the witness, and checks every rational dual inequality and binary split. It imports no LP/MILP solver. Its output is `exact_certificate_check.json` and the console report.

Required input data:

- `m6_candidates.json`: graph and sorted maximal-independent-set masks
- `upper_certificates.json`: 273-node exact rational certificate, about 42 KB

## Reproduce certificate discovery

SciPy and NumPy are needed only for generating candidate numerical LP solutions:

```
python explore_counts.py
python certify_upper.py
python check_exact_certificate.py
```

`certify_upper.py` uses numerical LP solutions to propose rational weights, corrects them conservatively, and outputs exact fractions. The independent checker verifies the result using integers and fractions only. Discovery has explicit node/time bounds.

## Other artifacts

- `verify_structure.py`: exhaustive recurrence checks on all simple graphs through four vertices and independent MIS cross-check
- `structural_verification.json`: 33,864 induced-subset recurrence comparisons
- `extremal_witness_structure.json`: original/clone/apex split and witness graph statistics
- `bounded_milp.py` and its output: exploratory finite profile; numerical results outside independently matched bounds remain observational
- `certificate_build_output.txt`: discovery statistics
- `exact_certificate_check_output.txt`: exact checker output

The calculation avoids enumerating all `2^47` induced subsets. It enumerates only 7,407 independent sets of the preceding 23-vertex graph and compresses them to 857 maximal independent sets of M6.

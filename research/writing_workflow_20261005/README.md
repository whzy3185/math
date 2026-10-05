# Mathematics paper workflow toolkit

A generic, executable procedure from a mathematical question to a human submission decision. It includes sixteen stage contracts, eight role prompts, eight JSON Schemas, conservative validators, and entirely synthetic demonstrations/tests.

This distribution contains no real manuscript, private project identity, source inventory, research receipt, or real review record. It does not submit, publish or assign authors.

## Start here

- `WORKFLOW.md`: the complete S00–S15 process, with inputs, outputs, roles, acceptance criteria, recovery and stopping rules
- `PRIMARY_SOURCES.md`: official publisher/technical guidance and author advice, with dates and bounded relevance
- `SYNTHETIC_DEMO.md`: an elementary mathematical example and invented administrative fixtures
- `prompts/`: initial reviewer, re-reviewer, editor, mathematical auditor, literature auditor, formal auditor, coordinator and release custodian
- `schemas/` and `templates/`: claims, proof obligations, required inventories, issue responses, versions, receipts and packets
- `scripts/`: generic packet construction, schema/evidence/context checks, synthetic fixture generation and validation
- `tests/`: synthetic positive and negative controls
- `MINIMIZATION.md`: what may enter this public package

## Run locally

Python 3.10+ is sufficient for the validators. Packet PDF inspection also requires Poppler's `pdftotext` and `pdfinfo`; missing tools block that check. The optional `jsonschema` package independently checks schema structure. The built-in schema guard remains available without it.

```sh
python3 scripts/validate_bundle.py
python3 examples/odd_sum_check.py
python3 scripts/make_synthetic_example.py /tmp/generic_math_example
python3 scripts/workflow_check.py readiness /tmp/generic_math_example/record.json
```

The example is fictional administrative test data, not a real proof review, author consent or venue approval. A validator cannot authenticate an invented attestation.

## Use on an authorized project

1. Copy the templates into a separate local work directory
2. Record exact claims, hypotheses, proof obligations, source/packet identities and genuine evidence
3. Freeze a required claim/obligation/issue inventory and preserve prior versions
4. Use an explicit allowlist to create a new neutral packet:

```sh
python3 scripts/make_packet.py PLAN.json --source-root INPUT_DIRECTORY --output NEW_PACKET_DIRECTORY
python3 scripts/workflow_check.py packet NEW_PACKET_DIRECTORY --output OUTSIDE_PACKET_REPORT.json
```

5. Manually inspect the packet and linked-source exposure, then use a genuinely new review context
6. Have a different editor revise, obtain issue closure, and retire each context after two rounds
7. Complete the applicable formalization, PDF, reproducibility, policy and human decision gates

Optional user inputs can be checked explicitly:

```sh
python3 scripts/validate_bundle.py --readiness-record /path/to/record.json --packet /path/to/packet --output-dir /tmp/local_checks
```

Keep resulting private records and reports outside this public distribution. With no explicit inputs, the wrapper runs only generic software checks and synthetic fixtures. Missing user inputs fail rather than being silently treated as checked.

## Interpret results carefully

Observed, finiteVerified, analyticProved, computerAssistedProved and PublishedEstablished are separate evidence categories. Finite experiments do not automatically prove universal claims. A negative source search is not a novelty proof. A Lean build does not establish correspondence to informal prose. A public archive link is not a successful replay.

The readiness checker verifies structure, file identity and cross-record consistency. Mathematical judgments, actual isolation, policy interpretation, authorship and consent still require authentic evidence. A structurally complete record grants no publication or submission authority.

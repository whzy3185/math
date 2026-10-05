# Reproducing the fixed 424-declaration source checkpoint

This snapshot contains all 37 verified TargetA modules, the exact 424-name audit source and the three pinned project configuration files. No state 11 or later source is included. The original AllTheorems module is unchanged. The extra audit imports AllTheorems, Period8ConjectureConstant and R2TenthStepCertificate.

Use official Lean 4.33.1 (leanprover/lean4:v4.33.1), commit 819816b2e0a3bf405af45ae5c7af2491d8f5bee6. The official Linux archive hash is 890afd185370f85666025b883914ab4f4b339136f8c96167b69cfb62aecaf235. Preserve lake-manifest.json; Mathlib is pinned to 0df444a360eaa60ab8c11dca51a86af692955474, with all other revisions retained. Run official Lake from formal/. The lakefile requires the official Mathlib repository and contains no custom build hooks. Fetch dependencies and the official cache using `lake exe cache get`.

The measured successful route first builds TargetA.AllTheorems, TargetA.Period8ConjectureConstant and TargetA.R2FourthStepCertificate through Lake. It then compiles Fifth, Sixth, Seventh, Eighth, Ninth and Tenth sequentially with official Lean's full-artifact argument shape:

```
lean SOURCE -o FRESH_OLEAN -i FRESH_ILEAN -c FRESH_C --setup CHECKED_COMPILER_INPUT --json -j 1
```

Do not assume a default Lake build of all later modules has passed: the earlier default step 5 normalization timed out. The successful route preserves a complete isolated TargetA namespace directory, because Lean resolves a namespace to the first matching search-path root rather than falling through for each missing module. Copy every already verified TargetA compiled artifact and required sidecar into that directory, then add the newly checked module outputs. Put this complete directory first in LEAN_PATH and retain the official dependency paths from `lake env printenv LEAN_PATH`.

Each compiler-input JSON keeps the canonical package/options/module mode/plugins/dynlibs and all nonproject import mappings. Starting from the preceding canonical or verified setup, change only the module name, redirect project object mappings to byte-identical copied artifacts and add the immediately preceding verified module. The successful Sixth setup had 8,701 import mappings; Tenth had 8,705. For the initial Fifth run the actual canonical Lake setup was retained. An input JSON is not a successful-build trace. Never fabricate Lake traces or overwrite a verified cache with unchecked outputs.

At every step, hash the exact source, setup and project imports before and after compilation; require a clean exit, three fresh full artifacts and exactly the 12 expected new theorem axiom reports. The run used a 180-second hard wall limit, a 150-second review threshold in stages 7–10 and a 300,000-heartbeat cap per statement. A compile exceeding the review threshold stops subsequent numerical stages. The state 7 run passed in 149.806 seconds; the remaining stages were below 130 seconds.

Finally, using the complete verified namespace and official dependencies, run:

```
lean -j 1 R2TenthStepAxiomAudit.lean
```

The fresh aggregate run passed in 78.659 seconds under a 120-second hard wall limit. Match all 424 unique expected #print names from that source. Accept both Lean's no-axioms form and wrapped axiom lists. Every axiom must belong to propext, Classical.choice, Quot.sound; reject sorryAx, missing/extra/duplicate names or errors. The exact successful normalized output is logs/audit424.log. Hashes of the unchanged original log and compiler records are in logs/audit_provenance.json and logs/serial_compile_evidence.json. Workspace-specific compiler input/output metadata stays in the separately frozen local archive rather than this minimal public source set. These instructions describe the verified run; no second clean-room rebuild of the newly packaged source snapshot is claimed.

The closed result reaches rational and real recurrence state 10. It does not identify the recorded S26 seed: 30 finite assertions remain, namely 15 inverse identities, 14 six-field transitions and one terminal match (1,228 scalar equalities). Positive eliminated pivots, the raw graph/block correspondence, contraction, response decay, infinite tails and the full R2 theorem remain separate. The paper's 237-declaration formalization paragraph is unchanged.

# Dependencies

## Mathematical dependency graph

The graph uses mathematical statements rather than historical task labels.

    signed adjacency and switching invariance
        |
        +-- exact finite minimality through order 30 -----+
        +-- exact order-32 upper certificate -------------+
        +-- local compression                              |
        |      -> parity-lifted cyclic closure             +--> complete
        |      -> exact terminal discharge ---------------+    truth
        +-- exact order-40 upper certificate -------------+    classification
        +-- 96-row exact finite LDL bridge ---------------+
        +-- global G6 edge -> tent IMS                     |
               -> residue endpoints and monotonicity -----+

The exact-$2r$ cluster theorem, the bound $3505r(9/25)^\ell$, and
$N_{\mathrm{exp}}=3120$ are valid corrected results but are not dependencies
of this theorem.  The analytic tail uses the one-interface spectral edge, not
its rank.

## Logical inputs

| input | role | evidence |
|---|---|---|
| finite minimality for even $8\le n\le30$ | no smaller failure | exact finite exhaustion |
| order-32 certificate | explicit strict failure | exact positive definiteness and algebraic comparison |
| local finite-state theorem | no failure at $34,36,38,42,44,46$ | independent exact finite reconstruction |
| order-40 certificate | explicit strict failure | exact rational LDL and rational threshold lower bound |
| finite structured tail | all 96 even orders $48\le n<240$ | independent exact sparse rational LDL |
| global G6 edge and tent IMS | all even $n\ge240$ | analytic inequalities plus four exact endpoints |

## Provenance appendix

Historical task labels appear only in this source map.

| content | certificate | independent checker |
|---|---|---|
| $8\le n\le30$ | research/counterexamples/target_a_minimality_certificate.json | research/scripts/verify_target_a_minimality_certificate.py |
| $n=32$ | research/counterexamples/target_a_n32_period8_certificate.json | research/scripts/verify_target_a_n32_certificate.py |
| six no-counterexample orders | research/proofs/task55/certificates/small_order_exact_classification.json | research/scripts/verify_target_a_task55_small_order_exact.py |
| $n=40$ | research/proofs/task55/TARGET_A_ORDERS_34_46_CERTIFICATES.json | research/scripts/verify_target_a_task55_orders_34_46.py |
| $48\le n<240$ and $n\ge240$ | research/proofs/task54/TARGET_A_TASK54_EVENTUAL_THRESHOLD_CERTIFICATE.json | research/scripts/verify_target_a_task54_threshold.py |

Reference checkpoint:
e6a01d8bf30088dae1042a237398bee2df138280.

## Artifact hashes

    a4b5248fee46b56ac763773c90b8087d454b6928a6bcd66622b4fdecac3e8ded  target_a_minimality_certificate.json
    db1378c6a7e5ab8526890be41c929a60ee17675d920a5ca0c501f49d888e46b4  target_a_n32_period8_certificate.json
    cb12d8502c6fcf31c5e8f1d23f3b9f1bb44b28b05a58f2e02067df08c04132b4  small_order_exact_classification.json
    6385a7e35b69ff32cba41b719faa554eef3060d020d0c54e0fd702d100cb6669  TARGET_A_ORDERS_34_46_CERTIFICATES.json
    18e4a9e8e6d21ba19aa95eb0c117c0b5f8e9bb59ddcfbf881d1c2d110744ea47  TARGET_A_TASK54_EVENTUAL_THRESHOLD_CERTIFICATE.json

No unrestricted common-liminf theorem, universal multi-gap optimality result,
arbitrary-period classification, or minimiser classification is used.

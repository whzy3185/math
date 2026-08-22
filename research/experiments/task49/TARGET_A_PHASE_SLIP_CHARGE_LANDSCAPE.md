# Target A Phase-Slip Charge Landscape

This bounded insurance experiment compares ways to distribute circumference
excess over well-separated local gaps.  Both holonomies are evaluated, and the
lower finite-ring squared spectral radius is recorded.

| Total excess | Tested configurations | Lowest observed configuration | Squared level |
|---:|---|---|---:|
| 2 | `[2]` | single gap-6 | 7.905369311620334 |
| 4 | `[4]`, `[2,2]`, `[6,-2]`, `[3,1]` | two separated gap-6 slips | 7.905369311620326 |
| 6 | `[6]`, `[4,2]`, `[2,2,2]` | three separated gap-6 slips | 7.905369311653343 |

The data support the physical choice of splitting positive excess into +2
phase slips when sufficiently separated.  Single gap-8, mixed gap-10/gap-2,
and odd local alternatives are higher in the tested large rings.

Status: `USEFUL` numerical large-separation evidence.

This is not a charge-selection theorem and does not exclude untested local
configurations.  Raw data are in `insurance/charge_landscape.json`.

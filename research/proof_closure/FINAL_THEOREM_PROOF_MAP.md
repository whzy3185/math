# Final Theorem Proof Map

| Theorem | Pure analytic core | Exact algebra needed | Finite cases needed | Computer-generated data | Lean target |
|---|---|---|---|---|---|
| switching invariance | yes | no | no | no | matrix diagonal conjugacy |
| twisted spectrum | yes | elementary trigonometry | no | no | Fourier/block statement after a suitable finite-cyclic API |
| period-eight bulk | nearly | polynomial expansion and endpoint ordering | no | coefficient identity currently CAS-audited | fiber determinant and positivity identity |
| phase-slip charge | yes | no | no | no | word endpoint arithmetic |
| G6 local root | transfer reduction | degree-ten Sturm interval | no | exact transfer coefficients | scalar polynomial and root isolation checker |
| G6 global edge | partial | physical branch exclusion | no | Grassmann/cofactor atlas | FORMALIZATION_OPEN |
| residue-zero failure tail | yes | elementary radical/rational comparison | no beyond `n>=48` inequality | no LDL rows | `8 | n` family theorem |
| nonzero-residue IMS tail | analytic mechanism | exact endpoint arithmetic | threshold endpoints | stored G6 cap constants | localization/IMS formalization deferred |
| equality 8..30 | no | threshold algebra | full finite coverage | exhaustive certificates | FINITE_FORMAL_PROVED target only |
| equality 34/36 | partial local rigidity | local Rayleigh table | finite local table | 13/14-bit windows | finite-language theorem after reduction |
| equality 38..46 | no unified proof yet | terminal lower certificates | finite closure | local language and terminal witnesses | FINITE_FORMAL_PROVED target only |
| failures 32/40 | period-eight family theorem | elementary cosine/rational comparison | no | old LDL pivots retained only as backup | residue-zero family theorem |
| complete classification | derived | as above | remaining finite rows | exact certificates | FORMALIZATION_OPEN |

No theorem in this map is upgraded merely because a future Lean finite
decision succeeds. The proof type must remain visible in both the human and
formal records.

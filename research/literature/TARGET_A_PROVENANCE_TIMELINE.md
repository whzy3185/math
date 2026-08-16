# Target A Provenance Timeline

Cutoff: **2026-08-16**  
Baseline: `c5cadf3ec7e160fc994453907fe83c579dc89646`

This timeline separates independent public sources from the Target A project's own repository record. Git author/committer timestamps are provenance evidence, but they do not by themselves establish the first time a commit became public.

## Independent Public Record

| Timestamp | Event | Evidence and relevance |
|---|---|---|
| 2013-07-07; revised 2013-12-23 | arXiv:1307.1841 public. | [`Schrodinger operators on periodic discrete graphs`](https://arxiv.org/abs/1307.1841) provides general Floquet fiber-operator methodology relevant to N10/N11, not either target result. |
| 2021-09 | DOI 10.1016/j.laa.2021.04.023 published. | [`Measure-theoretic bounds on the spectral radius of graphs from walks`](https://doi.org/10.1016/j.laa.2021.04.023) supplies general spectral-moment support inequalities relevant to N10. |
| 2023-01-01 | DOI 10.1515/spma-2023-0104 published. | [`Walks and eigenvalues of signed graphs`](https://doi.org/10.1515/spma-2023-0104) supplies walk/closed-walk spectral-radius bounds relevant to N10. |
| 2023-02-21 | arXiv:2302.10496 submitted. | [`Spectra of power hypergraphs and signed graphs via parity-closed walks`](https://arxiv.org/abs/2302.10496) supplies related closed-walk/spectral-moment methodology for N8, not a Target A result. |
| 2023-02-25 | arXiv:2302.13103 submitted. | [`Floquet isospectrality for periodic graph operators`](https://arxiv.org/abs/2302.13103) is general periodic-operator methodology, not N10 or N11. |
| 2026-07-19T16:05:20Z | Author repository created. | [`Vaibhavs25/bilu-linial-parity`](https://github.com/Vaibhavs25/bilu-linial-parity) public metadata. |
| 2026-07-19T17:07:14Z | arXiv:2607.17343 v1 submitted. | General parity-family and trace/cycle framework; no target counterexample or period-8 classification found. |
| 2026-07-19T17:25:09Z | Latest author-repository commit. | Commit `312f0e2f0b4cdc588b3c06c4754f1df231d4da6a`; all eight repository commits are on 19 July. |
| 2026-07-19T17:33:48Z | arXiv:2607.18334 v1 submitted. | States Conjecture 3 and verified range `n=8,10,12,14,16,18`; gives the all-unbalanced phase value used as close prior for part of N6. |
| 2026-07-21T03:17:07Z | DataCite metadata update for arXiv:2607.17343. | Version remains 1 in accessed record. |
| 2026-07-22T01:50:43Z | DataCite metadata update for arXiv:2607.18334. | Version remains 1 in accessed record. |
| 2026-07-25 | Author's unrelated GitHub repository update. | `cactus2distance` activity was reviewed; no Target A update was found. |
| 2026-07-31 | Author GitHub profile metadata updated. | Four public repositories were listed; no additional signed-circulant result was found. |
| 2026-08-16 audit | arXiv versions rechecked. | Both primary papers remained v1; no author correction or new verified range was found. |
| 2026-08-16 audit | Citation/follow-up indices rechecked. | OpenAlex/DataCite showed zero citations; Semantic Scholar exposed only reciprocal companion-paper citations in the retrieved endpoints. |

## Target A Project Record

All timestamps below are Git author and committer timestamps in Asia/Shanghai (`+08:00`). They document the local/project sequence. The audit does not infer a matching public-availability time from them.

| Timestamp | Commit | Project milestone | Claims materially present |
|---|---|---|---|
| 2026-08-15T17:11:25+08:00 | `21d5b848ec6222e9cca8b263dcc9cd397b86b236` | Freeze Target A counterexample discovery. | Initial counterexample/disproof record (N1). |
| 2026-08-15T22:13:17+08:00 | `cd14e6ab001a5321e95e2e4412e55c33cbbea5c6` | Certify `n=32` as smallest. | N1, N2. |
| 2026-08-15T23:11:14+08:00 | `344f445178cd65501604a8bb7ed523de8c0c4dd8` | Independent period-8 Floquet audit. | Floquet basis supporting N3/N4. |
| 2026-08-16T11:11:25+08:00 | `239ff8d206e88bbc7463863ad635bbf73e350791` | Independent infinite-family audit. | N3. |
| 2026-08-16T11:53:27+08:00 | `c7bfed6dcf881e00cc1d900c2d514d1de4298ab1` | Sharp period-8 spectral constant. | N4. |
| 2026-08-16T12:21:06+08:00 | `b2c58f26e9753831ca5db8d8615ba16a0670e3df` | Complete period-8 flux classification. | N5, N6. |
| 2026-08-16T12:59:14+08:00 | `c5cadf3ec7e160fc994453907fe83c579dc89646` | Period-8 structural mechanism. | N7, N8, N9; exact audit baseline. |
| 2026-08-16T13:26:10+08:00 | `637de46394592f918f8e719c88648a46077f1214` | General-period moment obstruction follow-up. | N10; descendant of baseline and not part of the exact baseline. |
| 2026-08-16T13:44:48+08:00 | `d43046f86d6b9f9ddf9a38b9d63dae0d11a7178d` | Low-period spectral-frontier classification. | N11; descendant of N10 and not part of the exact baseline. |

## Public Visibility Observation

At `2026-08-16T05:33:13Z` (`13:33:13+08:00`), an anonymous request to the raw GitHub URL for `TARGET_A_PERIOD8_STRUCTURAL_MECHANISM.md` at commit `637de46394592f918f8e719c88648a46077f1214` returned HTTP 200. GitHub HTML independently labeled [`whzy3185/math`](https://github.com/whzy3185/math) **Public** and exposed the baseline commit and its descendant.

At `2026-08-16T05:45:32Z` (`13:45:32+08:00`), anonymous raw requests returned HTTP 200 for `TARGET_A_GENERAL_PERIOD_MOMENT_OBSTRUCTIONS.md` at commit `637de46394592f918f8e719c88648a46077f1214` and `TARGET_A_LOW_PERIOD_SPECTRAL_FRONTIER.md` at commit `d43046f86d6b9f9ddf9a38b9d63dae0d11a7178d`.

Accordingly, the claims were publicly readable from the project repository by that observation time. The precise branch-push/publication instant was not recovered, so this audit does not assign an earlier public timestamp. This project-origin disclosure is recorded for provenance and is excluded from the independent-prior classifications.

## Baseline Source Fingerprints

| Baseline file | SHA-256 |
|---|---|
| `research/proofs/TARGET_A_SMALLEST_COUNTEREXAMPLE.md` | `668a3742e4c565ab6dc24d19565befd8531b26cd1ef56fc91528b81ef32062ed` |
| `research/proofs/TARGET_A_PERIOD8_FAMILY.md` | `602eb8e9bc775830628314b2395c81bf9c83a4eea0fde7d6c248e94e570e303a` |
| `research/proofs/TARGET_A_PERIOD8_SHARP_CONSTANT.md` | `e912a020ae2dc0931903b07172ec44f8823902c49a09f08356795c4ffa3e1c72` |
| `research/proofs/TARGET_A_PERIOD8_PATTERN_CLASSIFICATION.md` | `653f4b67401f8bb83aa043070260c3b5949a1fb833a72db0fc8b7a1b807ac05a` |
| `research/proofs/TARGET_A_PERIOD8_STRUCTURAL_MECHANISM.md` | `ca89c37eeabe100d3f2fe62695cf99b2cba6eaf116966862eb0e45352e7277d4` |

## Synchronization Source Fingerprints

| Commit and file | SHA-256 |
|---|---|
| `637de463:research/proofs/TARGET_A_GENERAL_PERIOD_MOMENT_OBSTRUCTIONS.md` | `14bb089d2d3dbb375ca0e409557fc1fd8121ad5106f2e08cb5d7005aef8d7a33` |
| `637de463:research/proofs/target_a_general_period_moment_obstructions.json` | `566928bc0fc06bc984a102d29f84a8694d9c9cb17b254e8940d3c53bdaac2401` |
| `d43046f8:research/proofs/TARGET_A_LOW_PERIOD_SPECTRAL_FRONTIER.md` | `a3e155b00744cd33e40d525494a11cc54bbb7fe1a310148f5db4af7eea83159c` |
| `d43046f8:research/proofs/target_a_low_period_spectral_frontier.json` | `82e69ab7df7d81d6c2c46364a6e07aba7578fbc3ad21a69dcc17ffd08333928d` |

## Caution

This chronology is a source-provenance record. It does not adjudicate authorship, legal priority, mathematical validity, or whether unindexed or non-public work existed earlier.

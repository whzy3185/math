# Target A Structural Discovery Matrix

Abbreviations: `P` proved, `EF` exact finite, `DN` deterministic numerical,
`O` open, `NA` stopped with reason.  Proof cost is relative (`L/M/H/VH`).

| QUESTION | OLD ASSUMPTION | NEW EVIDENCE | BEST CURRENT METHOD | FALSIFIED? | EXACT STATUS | POTENTIAL THEOREM | DEPENDENCIES | PROOF COST | JCTB VALUE | FINAL STORY RELEVANCE |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 order-nine factorization | irreducible 9D | exact `1+4+4` | exterior algebra | no | P | recurrence decomposition | T50 | L | 4 | high |
| 2 `9->4+4` | hoped | Bezout projectors | `Q(y)[E]` | no | P | split closure lemma | 1 | L | 4 | high |
| 3 `4->2` | hoped | reciprocal quadratics | `t+t^-1` | no | P | modal formula | 1 | L | 4 | high |
| 4 Chebyshev | equal pair weights | weights unequal | modal solve | yes, pure cosh | DN | cosh+sinh form | 3 | M | 2 | low |
| 5 shifted positivity | only beta=8 | beta=7.98 through k32 | exact coefficients | no | EF | finite prefix exclusion | 1 | L | 4 | high |
| 6 modal decomposition | unavailable | separated dominant root | algebraic modes | no | DN | exact modal closure | 2 | H | 4 | high |
| 7 dominant mode | plausible | ratio `<0.26` near 8 | interval modes | no | O/PROMISING | analytic tail | 6 | H | 5 | very high |
| 8 tail+prefix | absent | prefix k32 exact | hybrid proof | no | EF+O | all-k finite cap | 5,7 | H | 5 | very high |
| 9 polyhedral cone | likely | mixed projected signs | rational cone | partly | O/WEAK | invariant cone | 2 | VH | 2 | low |
| 10 positive generating function | plausible | unequal/signed modes | partial fractions | yes | DN | none current | 6 | M | 1 | low |
| 11 closure Hankel | plausible | 24/24 failures | Hankel minors | yes | DN | none current | T50 | L | 1 | low |
| 12 symplectic trace | unexplored | exterior factor exact | wedge traces | no | P_REDUCTION | low trace recurrence | 1 | M | 3 | medium |
| 13 finite Evans | empirical | k32 real exclusion | exact determinant | no | EF | uniform root exclusion | 5 | H | 5 | very high |
| 14 Rouche | possible | exact real sign stronger prefix | modal split | no | O/WEAK | complex exclusion | 7 | H | 2 | low |
| 15 argument principle | possible | not needed prefix | interval winding | no | NA: weaker prefix | root count | 13 | H | 2 | low |
| 16 Schur/Riccati | possible | no rational order interval | block square | no | O/WEAK | SPD recursion | local A2 | VH | 2 | low |
| 17 Birman-Schwinger | charged finite rank | naive global model invalid | piecewise bulk | yes, naive | O/PROMISING | interface counting | 18,19 | H | 4 | medium |
| 18 rank/inertia | unknown | neutral ranks 8-16 exact | integer Sturm | no | P | compact core lemma | charge | L | 3 | medium |
| 19 infinite Green | expected | no closed restriction | stable transfer | no | O/WEAK | Green formula | bulk | H | 3 | medium |
| 20 finite Green | images expected | one determinant-lemma check | resolvent identity | no | DN | exponential comparison | 19 | H | 4 | medium |
| 21 matrix SOS | expected | symbolic growth poor | Fejer-Riesz | no | O/WEAK | local positivity | bulk | VH | 2 | low |
| 22 charge conservation | informal | `sum q=n-4d` | gap partition | no | P | charge lemma | legality | L | 5 | very high |
| 23 single-charge spectrum | G6/G10 only | 11 species mapped | transfer/open interface | no | DN | charge spectrum | 22 | H | 5 | very high |
| 24 q=-2 | possible competitor | level `8.0809858` | interface scan | yes, as competitor | DN | gap2 exclusion | 23 | M | 5 | very high |
| 25 charge recurrence | hoped | period-8 insertion signal | transfer products | no | O/PROMISING | recurrence in g | 23 | H | 4 | high |
| 26 charge algebra | unrelated constants | common symmetric Evans variables | elimination | no | P for G6 | algebraic family | 51 | VH | 4 | high |
| 27 two-slip | scalar tails | two-level cluster | effective subspace | no | DN | fixed-two theorem | T49 | H | 5 | very high |
| 28 three-slip | G10 core | three G6 near c6 | effective subspace | yes, G10 core | DN | fixed-three theorem | 23 | H | 5 | very high |
| 29 four-slip | pairwise | four-level cluster | effective subspace | no | DN | fixed-four theorem | 27 | H | 3 | medium |
| 30 three G6 vs G10 | uncertain | margin `0.07173` | finite rings | no | DN_STRONG | residue-six upper bound | 28 | M | 5 | very high |
| 31 effective matrix | scalar fit | cluster reconstructed | projected seeds | no | DN | tunnelling matrix | 27-29 | H | 5 | high |
| 32 many-body | pairwise assumed | below double resolution | high-precision Evans | unresolved | O | remainder theorem | 31 | VH | 4 | high |
| 33 two-path mod16 | multiplier sign | geometry+holonomy needed | two-path matrix | no | O/PROMISING | mod16 law | 27 | H | 4 | high |
| 34 mixed charge | few cases | gap2 combinations costly | minimax | no | DN | decomposition theorem | 22-24 | H | 5 | high |
| 35 sub-eight atlas | few phases | 13 primitive p<=24 | reused frontier | no | P eta/DN `<8` | phase classification | T48 | M | 5 | high |
| 36 family mining | `[4,g]` only | mixed phases found | Bloch atlas | yes, only branch | DN | defect-crystal families | 35 | H | 5 | high |
| 37 density diagram | one envelope | multiple commensurate branches | density atlas | no | DN | phase envelope | 35 | VH | 4 | high |
| 38 M4 | unknown | 10-class exact formula | closed walks | no | P | M4 motif lemma | T42 | L | 5 | high |
| 39 M5/M6 | maybe useful | 27/76 exact classes | closed walks | no | P_DATA | higher motif lemma | 38 | M | 3 | medium |
| 40 Hankel-local | hoped | no positive local split | motif expansion | no | O/WEAK | local certificate | 38 | VH | 5 | high |
| 41 window Rayleigh | hoped unique | 108 windows survive | integer vectors | yes, current depth | EF | stronger window theorem | 38 | H | 5 | high |
| 42 de Bruijn | target only | 30 cycles through p16 | overlap cycles | yes, current relaxation | EF_BOUNDED | survivor classification | 41 | H | 4 | high |
| 43 cycle polytope | promising | survivor set too broad | marginal LP | no | O | finite relaxation | 42 | H | 4 | medium |
| 44 SDP/SOS | possible | no clean rational certificate | bounded SDP | no | O/WEAK | SOS exclusion | 41 | VH | 3 | medium |
| 45 transfer multicone | possible | not rationalized | cocycle cone | no | O/PROMISING | hyperbolicity theorem | bulk | VH | 5 | very high |
| 46 subadditive optimization | possible | conceptual fit only | extremal norm | no | O | unique minimizing measure | 45 | VH | 5 | very high |
| 47 Peierls gap | assumed positive | 11 bounded motifs positive | finite defects | no | DN | uniform defect gap | 41 | VH | 5 | very high |
| 48 transparent defect | none | none in bounded scope | adversarial motifs | no | DN_BOUNDED | absence theorem | 47 | VH | 5 | high |
| 49 asymptotic constants | G6/G10 split | all nonzero residues approach c6 | charge minimax | yes, G10 limit | DN_STRONG | residue phase diagram | 28,35 | VH | 5 | very high |
| 50 finite-size correction | scalar Floquet | matrix/holonomy needed | high-precision Evans | partly | O | asymptotic expansion | 31 | VH | 5 | high |
| 51 c6 polynomial | PSLQ candidate | exact resultant factor | symmetric Evans | no | P | degree-10 theorem | T50 | M | 5 | very high |
| 52 c10 polynomial | unknown | growth stop | symmetric Evans | no | O | algebraic theorem | 26 | VH | 2 | low |
| 53 general Evans algebra | separate | `(S,P)` template | elimination | no | P_TEMPLATE | charge algebra family | 26 | VH | 4 | high |
| 54 trace map | possible | exterior coordinates | trace invariants | no | O/PROMISING | word dynamics | 12 | H | 3 | medium |
| 55 topology | possible protection | same translated sectors | chiral audit | yes, protection story | P chiral/O invariant | none needed | T40 | M | 1 | low |
| 56 odd n | ignored | d odd, odd charges elementary | legality | no | P bookkeeping/DN | odd phase diagram | 22,23 | H | 3 | future |
| 57 nearby circulant | portable | order rises to six | recurrence audit | no | NA: weak signal | portability | none | VH | 1 | future |
| 58 continuous phases | signed robust | formulation broad | magnetic Hessian | no | NA: scope | stability theorem | none | VH | 1 | future |

Central conclusion: the strongest new exact result is the degree-ten theorem
for `c6`; the strongest structural reframe is the elementary `+2` multi-slip
picture; the strongest still-open theorem is the common nonzero-residue limit.

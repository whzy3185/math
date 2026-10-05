# Stability literature scope

Targeted primary-source check, 5 October 2026, approximately 09:49 UTC. The search used the exact unique-minimum-domination terminology together with extremal edges, stability and edge edits. This is a bounded check, not exhaustive citation coverage.

The present proposed stability parameter is the number of edge additions/deletions required to reach an extremal graph, minimized over all vertex relabellings. It is a different question from whether the domination number, or the number of minimum dominating sets, survives a prescribed edge or vertex deletion.

## Direct baseline

Koch and Narayan, [Maximal bipartite graphs with a unique minimum dominating set](https://arxiv.org/abs/2511.01719), arXiv:2511.01719v1, studies extremal edge counts. The retrieved record still has only v1. The current boundary maxima used in this pilot are the separately proved and audited results in the project papers, not results attributed to this conjecture source.

Erlbacher's [pinned public Koch–Narayan artifact package](https://github.com/demonstrandum-research/artifacts/blob/94db9ed50d48a57aae5ccb72e6a95a2b8f8f39d3/problems/p2-factory/kills/koch-narayan/WRITEUP.md) supplies the earlier finite counterexamples and unbalanced constructions. The inspected write-up does not state an edge-edit stability theorem or this row-modification obstruction. Existing attribution of those earlier examples and construction mechanisms remains unchanged.

## Nearby terminology, different statements

- Goddard and Henning, *Graphs with Unique Minimum Specified Domination Sets*, Graphs and Combinatorics 39 (2023), article103, [institutional primary record](https://pure.uj.ac.za/en/publications/graphs-with-unique-minimum-specified-domination-sets/), [author-hosted manuscript](https://people.computing.clemson.edu/~goddard/papers/uniqueDom.pdf), DOI10.1007/s00373-023-02704-1. This studies uniqueness and the maximum possible domination parameters, including the n/3 threshold; it is relevant background for private-neighbour forcing, not a sharp-edge edit-distance result.
- Allagan, Pereyra, Gray, Sawyer and Morgan, *Dominion in trees: Structural forcing, Fibonacci growth, and periodic rigidity*, Open Journal of Discrete Applied Mathematics 9(2) (2026),77–86, [publisher's full article](https://pisrt.org/psr-press/journals/odam/04-vol-9-2026-issue-2/dominion-in-trees-structural-forcing-fibonacci-growth-and-periodic-rigidity/), DOI10.30538/psrp-odam2026.0135, published12August2026. Its stability statement bounds changes in the number of minimum dominating sets under leaf deletion in tree families. It does not concern edit distance from dense extremal bipartite graphs. The journal title/author list differs from the earlier arXiv2601.03485 record, so the final publisher source is used here.
- Hedetniemi, *On graphs having a unique minimum independent dominating set*, Australasian Journal of Combinatorics68(3)(2017),357–370, [journal PDF](https://ajc.maths.uq.edu.au/pdf/68/ajc_v68_p357.pdf). The independence constraint changes the optimization domain. The obstruction constructed here deliberately adds edges inside the unique dominating set, so a potential theorem under independence would require a separate analysis.

No directly matching primary theorem was located in this targeted pass. That finding does not prove novelty or exclude unindexed or unpublished work. The pilot's all-graph upper estimate and obstruction require their own mathematical audit regardless of literature status.

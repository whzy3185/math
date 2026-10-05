"""Exact structural tools for any nonempty finite simple base graph.

Adjacency lists are tuples of integer bitmasks. See GENERAL_THEOREM.md.
No optimization library is required, and no polynomial-time Hall solver is
claimed. Enumeration cost is parameterized by the base independent-set count.
"""
from math import comb


def validate_graph(adjacency):
    n = len(adjacency)
    if n == 0:
        raise ValueError('The base graph must have at least one vertex')
    full = (1 << n) - 1
    if any(not isinstance(a, int) or a < 0 or a & ~full for a in adjacency):
        raise ValueError('Invalid adjacency mask')
    if any(adjacency[v] & (1 << v) for v in range(n)):
        raise ValueError('Loops are not permitted')
    if any(bool(adjacency[u] & (1 << v)) != bool(adjacency[v] & (1 << u))
           for u in range(n) for v in range(n)):
        raise ValueError('The graph must be undirected')


def mycielski(adjacency):
    validate_graph(adjacency)
    n = len(adjacency)
    result = [0] * (2*n + 1)
    for v, neighbors in enumerate(adjacency):
        result[v] = neighbors | (neighbors << n)
        result[n+v] = neighbors | (1 << (2*n))
    result[2*n] = ((1 << n) - 1) << n
    return tuple(result)


def independent_sets_with_neighborhood(adjacency, allowed=None):
    """Yield each pair (I, N(I)) once, including the empty independent set."""
    validate_graph(adjacency)
    full = (1 << len(adjacency)) - 1
    if allowed is None:
        allowed = full
    if allowed < 0 or allowed & ~full:
        raise ValueError('Invalid allowed vertex mask')

    def generate(available, chosen, neighborhood):
        yield chosen, neighborhood
        while available:
            bit = available & -available
            available ^= bit
            v = bit.bit_length() - 1
            yield from generate(available & ~adjacency[v], chosen | bit,
                                neighborhood | adjacency[v])
    yield from generate(allowed, 0, 0)


def maximal_independent_sets_mycielski(adjacency):
    """Return all maximal independent sets of μ(G), using the base only."""
    validate_graph(adjacency)
    n = len(adjacency)
    full = (1 << n) - 1
    unions = set()
    output = set()
    for independent, neighborhood in independent_sets_with_neighborhood(adjacency):
        unions.add(neighborhood)
        if independent | neighborhood == full:
            output.add(independent | (1 << (2*n)))
    for neighborhood in unions:
        closed = sum(1 << v for v in range(n)
                     if adjacency[v] & ~neighborhood == 0)
        clones = (full ^ neighborhood) << n
        output.add(closed | clones)
    return tuple(sorted(output))


def induced_independence(adjacency, originals, clones, apex=False):
    """Exact α for an arbitrary induced subset of μ(G)."""
    validate_graph(adjacency)
    full = (1 << len(adjacency)) - 1
    if originals < 0 or clones < 0 or (originals | clones) & ~full:
        raise ValueError('Invalid original/clone mask')
    base_alpha = clone_branch = 0
    for independent, neighborhood in independent_sets_with_neighborhood(adjacency, originals):
        size = independent.bit_count()
        base_alpha = max(base_alpha, size)
        clone_branch = max(clone_branch, size + (clones & ~neighborhood).bit_count())
    return max(clone_branch, int(bool(apex)) + base_alpha)


def independence_polynomial_mycielski(adjacency):
    """Return exact coefficients c_j counting j-vertex independent sets."""
    validate_graph(adjacency)
    n = len(adjacency)
    coefficients = [0] * (2*n + 2)
    for independent, neighborhood in independent_sets_with_neighborhood(adjacency):
        size = independent.bit_count()
        available_clones = n - neighborhood.bit_count()
        coefficients[size+1] += 1  # The apex branch.
        for j in range(available_clones+1):
            coefficients[size+j] += comb(available_clones, j)
    return tuple(coefficients)


def hall_profile_model(adjacency, k):
    """Describe the exact binary model; does not invoke or trust a solver.

    Maximize sum(x_v), for binary x_v, subject to sum_{v in mask} x_v <= k
    for each returned row. The certificate workflow can verify upper bounds.
    """
    if not isinstance(k, int) or k < 0:
        raise ValueError('k must be a nonnegative integer')
    masks = maximal_independent_sets_mycielski(adjacency)
    return {'vertices': 2*len(adjacency)+1, 'row_masks': masks,
            'row_upper_bounds': (k,)*len(masks)}

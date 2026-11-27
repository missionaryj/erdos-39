"""Check overlaps, cross-pair loads and slope-separated quadratic rulers."""
from collections import Counter
from itertools import product

from interlaced import marked
from paired_gaps import gap_map


def ruler(prime, curvature, offset, indices):
    return [2 * prime * x + (curvature * x * x + offset) % prime for x in indices]


def cross_loads(first, second):
    first_gaps, second_gaps = gap_map(first), gap_map(second)
    shared = sorted(first_gaps.keys() & second_gaps.keys())
    loads = {}
    for gap in shared:
        for pair in product(first_gaps[gap], second_gaps[gap]):
            loads.setdefault(pair, []).append(gap)
    return shared, loads


def matching_size(component, neighbors):
    """Enumerate matchings in one component of the small marked-ruler example."""
    if not component:
        return 0
    vertex = min(component)
    rest = component - {vertex}
    best = matching_size(rest, neighbors)
    for other in neighbors[vertex] & rest:
        best = max(best, 1 + matching_size(rest - {other}, neighbors))
    return best


def marked_example():
    blocks = [
        [marked(level, 2 * prime * i + i * i % prime) for i in range(1, prime)]
        for level, prime in [(3, 67), (4, 257)]
    ]
    shared, loads = cross_loads(*blocks)
    assert max(map(len, loads.values())) == 2
    neighbors = {gap: set() for gap in shared}
    for occurrences in loads.values():
        if len(occurrences) == 2:
            first, second = occurrences
            neighbors[first].add(second)
            neighbors[second].add(first)
    unseen = set(shared)
    sizes = Counter()
    matching = 0
    while unseen:
        component = {unseen.pop()}
        pending = list(component)
        while pending:
            for gap in neighbors[pending.pop()] & unseen:
                unseen.remove(gap)
                component.add(gap)
                pending.append(gap)
        sizes[len(component)] += 1
        matching += matching_size(component, neighbors)
    assert sizes == {1: 288, 2: 11, 3: 7, 4: 2}
    assert (len(shared), matching) == (339, 22)
    print("Marked rulers, minimum cross-pair cover:", len(shared) - matching)


def quadratic_example(prime):
    first = ruler(prime, 1, 0, range(prime))
    second = ruler(prime, 2, 0, range(prime))
    shared, loads = cross_loads(first, second)
    assert max(map(len, loads.values())) <= 2
    # Check that these particular zero offsets already meet the averaging bound.
    assert 4 * len(shared) >= (prime // 4) * prime
    left = ruler(prime, 1, 0, (x for x in range(prime) if 4*x < prime))
    right = ruler(prime, 2, 0, (x for x in range(prime)
                                if prime <= 4*((2*x) % prime) < 2*prime))
    assert gap_map(left).keys().isdisjoint(gap_map(right))
    assert len({a + b for a in left for b in right}) == len(left) * len(right)
    print(prime, len(shared), max(map(len, loads.values())), len(left), len(right))


if __name__ == "__main__":
    marked_example()
    print("Prime, shared differences, max load, retained left, retained right")
    for prime in [31, 67, 127, 257]:
        quadratic_example(prime)

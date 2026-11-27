"""Find which mark labels coincide in every solution of the gap equations."""
from collections import Counter

from interlaced import marked
from paired_gaps import gap_map


def endpoint_equations(first, second, prime):
    left, right = gap_map(first), gap_map(second)
    pivots = {}
    for gap in sorted(left.keys() & right.keys()):
        row = {v: 1 for v in left[gap]}
        row.update({len(first) + v: prime - 1 for v in right[gap]})
        while row:
            lead = min(row)
            factor = row[lead]
            if lead not in pivots:
                inverse = pow(factor, -1, prime)
                pivots[lead] = {v: a * inverse % prime for v, a in row.items()}
                break
            for v, a in pivots[lead].items():
                value = (row.get(v, 0) - factor * a) % prime
                if value:
                    row[v] = value
                else:
                    row.pop(v, None)
    return pivots


def coordinate_functionals(size, pivots, prime):
    free = [i for i in range(size) if i not in pivots]
    labels = [None] * size
    for column, variable in enumerate(free):
        labels[variable] = tuple(int(i == column) for i in range(len(free)))
    for pivot in sorted(pivots, reverse=True):
        terms = [(a, labels[v]) for v, a in pivots[pivot].items() if v != pivot]
        labels[pivot] = tuple(-sum(a * vec[i] for a, vec in terms) % prime
                              for i in range(len(free)))
    return labels


def verify(first, second, prime):
    pivots = endpoint_equations(first, second, prime)
    labels = coordinate_functionals(len(first) + len(second), pivots, prime)
    left, right = gap_map(first), gap_map(second)
    for gap in left.keys() & right.keys():
        i, j = left[gap]
        u, v = right[gap]
        vectors = (labels[i], labels[j], labels[len(first)+u], labels[len(first)+v])
        assert all((a+b-c-d) % prime == 0 for a, b, c, d in zip(*vectors))
    fibers = [max(Counter(group).values())
              for group in (labels[:len(first)], labels[len(first):])]
    return len(pivots), len(labels) - len(pivots), fibers


if __name__ == "__main__":
    blocks = [
        [marked(level, 2 * prime * i + i * i % prime) for i in range(1, prime)]
        for level, prime in [(3, 67), (4, 257)]
    ]
    for prime in [3, 5, 7, 11, 13, 17, 31, 67, 127, 257, 1009, 65521]:
        rank, dimension, fibers = verify(*blocks, prime)
        assert (rank, dimension, fibers) == (297, 25, [66, 230])
        print(prime, "rank", rank, "nullity", dimension, "largest forced fibers", fibers)

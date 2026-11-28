"""Check the ordinary lift and its overlap with the full first-row difference set."""
from collections import Counter, defaultdict
from itertools import combinations_with_replacement

from coupled_rows import graph


def encoded(point, prime):
    return sum(digit * (2*prime)**i for i, digit in enumerate(point[:6]))


def canonical_gap(a, b, prime, modular):
    if not modular:
        return abs(encoded(a, prime)-encoded(b, prime))
    forward = tuple((i-j) % prime for i, j in zip(a[:6], b[:6]))
    backward = tuple((-k) % prime for k in forward)
    return min(forward, backward)


def exact_extension(points, prime, modular):
    old = [i for i, x in enumerate(points) if x[-1] == 0]
    other = [i for i, x in enumerate(points) if x[-1] != 0]
    gaps = {}
    for i, a in enumerate(points):
        for j, b in enumerate(points[:i]):
            gaps[i, j] = canonical_gap(a, b, prime, modular)
    used = {gaps[max(i,j), min(i,j)] for i in old for j in old if j < i}
    assert len(used) == len(old)*(len(old)-1)//2
    best = 0

    def search(index, kept, occupied):
        nonlocal best
        best = max(best, len(kept)-len(old))
        if len(kept)-len(old)+len(other)-index <= best:
            return
        i = other[index]
        new = {gaps[max(i,j), min(i,j)] for j in kept}
        if len(new) == len(kept) and new.isdisjoint(occupied):
            search(index+1, kept+[i], occupied | new)
        search(index+1, kept, occupied)

    search(0, old, used)
    return best


def fiber_check(prime, nonsquare):
    points, _ = graph(prime, nonsquare)
    old = [x for x in points if x[-1] == 0]
    old_gaps = {}
    for i, a in enumerate(old):
        for b in old[:i]:
            key = canonical_gap(a, b, prime, True)
            assert key not in old_gaps
            old_gaps[key] = canonical_gap(a, b, prime, False)
    fibers = defaultdict(list)
    for a in points:
        if a[4:6] != (0, 0):
            fibers[a[4:6]].append(a)
    assert len(fibers) == prime**2-1
    matched = total = 0
    for fiber in fibers.values():
        assert len(fiber) == prime-1
        for i, a in enumerate(fiber):
            for b in fiber[:i]:
                key = canonical_gap(a, b, prime, True)
                matched += old_gaps[key] == canonical_gap(a, b, prime, False)
                total += 1
    positive = [a for a in points if 1 <= a[0] <= (prime-1)//2]
    sums = Counter(tuple((i+j) % prime for i, j in zip(a[:6], b[:6]))
                   for a, b in combinations_with_replacement(positive, 2))
    assert max(sums.values()) <= 6
    print(prime, len(positive), max(sums.values()), matched, total)
    if prime == 3:
        print("Exact additions with the whole first row (modular, integer):",
              exact_extension(points, prime, True), exact_extension(points, prime, False))


if __name__ == "__main__":
    print("Prime, retained positive-slab marks, max sum count, ordinary matches, modular matches")
    for parameters in [(3, 2), (5, 2), (7, 3), (11, 2)]:
        fiber_check(*parameters)

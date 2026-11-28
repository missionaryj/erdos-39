"""Count all sums and gaps in the two-level elliptic-quadric construction."""
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, product

from field_bridge import square


def blocks(p):
    d = next(a for a in range(2, p) if pow(a, (p-1)//2, p) == p-1)
    elements = list(product(range(p), repeat=2))
    squares = {x: square(x, (-d, 0), p) for x in elements}
    residues = set(squares.values())
    alpha = next(a for a in elements if a not in residues)

    def mul(x, y):
        a, b = x
        u, v = y
        return ((a*u+d*b*v) % p, (a*v+b*u) % p)

    def det(gamma):
        a, b = mul(alpha, squares[gamma])
        return ((a-1) % p, b)

    gamma = next(g for g in elements if det(g) not in residues)
    old = [x+squares[x]+(0, 0) for x in elements if 4*x[0] < p]
    new = []
    cone_size = 0
    for z in elements:
        u, v = mul(alpha, squares[z])
        for x in elements:
            y = ((squares[x][0]+u) % p, (squares[x][1]+v) % p)
            if (mul(gamma, y)[0] + 2*mul(x, z)[0]) % p:
                continue
            cone_size += 1
            if z != (0, 0) and p <= 4*x[0] < 2*p:
                new.append(x+y+z)
    assert cone_size == p**3-p*(p-1)
    return old, new


def signature(a, b, p, sign):
    return tuple((x + sign*y) % p for x, y in zip(a, b))


def repair(marks):
    # A conflict records the four indices of two unequal pairs with equal sums.
    buckets = defaultdict(list)
    conflicts = []
    for i, j in combinations_with_replacement(range(len(marks)), 2):
        value = marks[i] + marks[j]
        for k, l in buckets[value]:
            conflicts.append(frozenset((i, j, k, l)))
        buckets[value].append((i, j))
    incident = [set() for _ in marks]
    for n, edge in enumerate(conflicts):
        assert len(edge) == 4
        for i in edge:
            incident[i].add(n)
    removed = []
    while True:
        i = max(range(len(marks)), key=lambda k: len(incident[k]))
        if not incident[i]:
            break
        removed.append(i)
        for n in tuple(incident[i]):
            for j in conflicts[n]:
                incident[j].remove(n)
    keep = set(range(len(marks))) - set(removed)
    for i in reversed(removed):
        keep.add(i)
        if any(edge <= keep for edge in conflicts):
            keep.remove(i)
    return [marks[i] for i in sorted(keep)]


def check(p):
    old, new = blocks(p)
    for sign in (-1, 1):
        pairings = combinations if sign == -1 else combinations_with_replacement
        groups = []
        for points in (old, new):
            counts = Counter()
            for a, b in pairings(points, 2):
                counts[signature(a, b, p, sign)] += 1
                if sign == -1:
                    counts[signature(b, a, p, sign)] += 1
            groups.append(counts)
        assert max(groups[0].values()) == 1
        if sign == -1:
            assert groups[0].keys().isdisjoint(groups[1])
        mixed = Counter(signature(a, b, p, sign) for a in new for b in old)
        assert max(mixed.values()) == 1
        new_max = max(groups[1].values())
        if sign == -1:
            gap_max = new_max
            assert new_max <= 2
        else:
            sum_max = new_max
            assert new_max <= 4

    def lift(v):
        return sum(value*(2*p)**i for i, value in enumerate(v))

    marks = [4*lift(v)+1 for v in old]+[4*lift(v)+2 for v in new]
    assert sum(v < 4*(2*p)**4 for v in marks) == len(old)
    ordinary_gaps = Counter(abs(a-b) for a, b in combinations(marks, 2))
    ordinary_sums = Counter(a+b for a, b in combinations_with_replacement(marks, 2))
    assert max(ordinary_gaps.values()) <= 2 and max(ordinary_sums.values()) <= 4
    retained = repair([4*lift(v)+2 for v in new])
    witness = [4*lift(v)+1 for v in old] + retained
    sums = {a+b for a, b in combinations_with_replacement(witness, 2)}
    assert len(sums) == len(witness)*(len(witness)+1)//2
    print(p, len(old), len(new), len(retained), len(sums), gap_max, sum_max,
          max(ordinary_gaps.values()), max(ordinary_sums.values()))


if __name__ == "__main__":
    print("p, early, later, later after repair, distinct repaired sums, modular later gap/sum maxima, integer union gap/sum maxima")
    for prime in (7, 11, 13, 17):
        check(prime)

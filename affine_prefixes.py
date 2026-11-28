"""Count intersections of finite-field parabolas with affine subspaces."""
from collections import Counter
from itertools import combinations, combinations_with_replacement, product

from field_bridge import graph_points


def row_spaces(p, dimension, rank):
    """Enumerate constraint spaces by their unique reduced row echelon bases."""
    for pivots in combinations(range(dimension), rank):
        free = [(i, j) for i, pivot in enumerate(pivots)
                for j in range(pivot + 1, dimension) if j not in pivots]
        for coefficients in product(range(p), repeat=len(free)):
            rows = [[int(j == pivot) for j in range(dimension)] for pivot in pivots]
            for (i, j), value in zip(free, coefficients):
                rows[i][j] = value
            yield rows


def check_all_flats(p, nonsquare):
    points = [x+y for x, y in graph_points(p, (-nonsquare, 0))]
    maxima = []
    for rank in range(2, -1, -1):
        best = 0
        for rows in row_spaces(p, 4, rank):
            counts = Counter(tuple(sum(a*b for a, b in zip(row, v)) % p for row in rows)
                             for v in points)
            best = max(best, max(counts.values()))
        maxima.append(best)
    assert maxima == [p, 2*p-1, p*p]
    print(f"All affine flats, p={p}, degree 2: {maxima}")


def check_flag(p, modulus):
    degree = len(modulus)
    d = degree // 2
    # For the quartic examples theta^2 has minimal polynomial Y^2+Y+2,
    # whose constant term is a nonsquare. The quadratic extensions are fields.
    if d == 2:
        assert all((y*y+y+2) % p for y in range(p))
        assert pow(2, (p-1)//2, p) == p-1
    else:
        assert all((y*y+modulus[0]) % p for y in range(p))
    radix = 2*p
    marks = []
    for x, y in graph_points(p, modulus):
        digits = x[::2] + y[::2] + x[1::2] + y[1::2]
        marks.append(1 + sum(v*radix**i for i, v in enumerate(digits)))
    counts = [sum(v <= radix**(2*d+t) for v in marks) for t in range(2*d+1)]
    expected = [p**d + p**t - p**max(0, t-d) for t in range(2*d+1)]
    assert counts == expected
    pair_sums = {x+y for x, y in combinations_with_replacement(marks, 2)}
    assert len(pair_sums) == len(marks)*(len(marks)+1)//2
    print(f"One flag, p={p}, degree {degree}: {counts}; {len(pair_sums)} distinct sums")


def check_tagged_rows(p):
    old = [(x, x*x % p, 0) for x in range(p)]
    later = []
    for z in range(1, p):
        later.append((z*z % p, 0, z))
        if z <= (p-1)//2:
            later.append((z*z % p, z, z))
    assert len(old) + len(later) == (5*p-3)//2

    def gaps(points):
        return [tuple((b-a) % p for a, b in zip(u, v))
                for u in points for v in points if u != v]

    ordered = gaps(old) + gaps(later)
    assert len(ordered) == len(set(ordered))
    radix = 2*p
    marks = [4*(x+radix*y+radix**2*z)+tag
             for points, tag in ((old, 1), (later, 2)) for x, y, z in points]
    assert len({a+b for a, b in combinations_with_replacement(marks, 2)}) == len(marks)*(len(marks)+1)//2
    print(f"Tagged rows, p={p}: {len(old)} early, {len(later)} later")


if __name__ == "__main__":
    for p, nonsquare in ((3, 2), (5, 2), (7, 3)):
        check_all_flats(p, nonsquare)
        check_flag(p, (-nonsquare, 0))
    for p in (3, 5):
        check_flag(p, (2, 0, 1, 0))
    for p in (3, 5, 7, 17, 43):
        check_tagged_rows(p)

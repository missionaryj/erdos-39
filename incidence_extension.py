"""Check a product construction while preserving a prescribed first row."""
from functools import cache
from itertools import combinations, combinations_with_replacement

def ruler(prime):
    return [2*prime*i + i*i % prime for i in range(prime)]


def verify(p, q, initial, rows):
    low, high = ruler(p), ruler(q)
    base = 4*p*p
    assert len(rows) < len(high)
    all_rows = [set(initial)] + [set(row) for row in rows]
    assert all(len(left & right) <= 1 for left, right in combinations(all_rows, 2))
    marks = [base*high[j] + low[i] + 1
             for j, row in enumerate(all_rows) for i in sorted(row)]
    assert len([x for x in marks if x <= base]) == len(initial)
    sums = {x+y for x, y in combinations_with_replacement(marks, 2)}
    assert len(sums) == len(marks)*(len(marks)+1)//2
    return len(marks), max(marks), len(sums)


def tiny_maximum(p, initial, columns):
    """Enumerate all row neighborhoods, remembering the pairs already used."""
    pairs = list(combinations(range(p), 2))

    def pair_mask(subset):
        return sum(1 << k for k, (a, b) in enumerate(pairs)
                   if a in subset and b in subset)

    choices = [(pair_mask(row), size) for size in range(p+1)
               for row in combinations(range(p), size) if len(set(row) & initial) <= 1]

    @cache
    def best(remaining, used):
        if not remaining:
            return 0
        return max(size + best(remaining-1, used | mask)
                   for mask, size in choices if not mask & used)

    return best(columns, pair_mask(initial))


if __name__ == "__main__":
    initial = set(range(4))
    outside = [{4, 5}, {4, 6}, {5, 6}, {4}]
    rows = [points | {i} for i, points in enumerate(outside)]
    tiny = verify(7, 5, initial, rows)
    assert tiny_maximum(7, initial, 4) == tiny[0] - len(initial) == 11
    assert tiny_maximum(3, set(), 4) == 7
    print("Exact 7 by 5 example (marks, maximum, distinct sums):", tiny)

    # Forty-two affine lines on 49 points, plus one private old label per row.
    initial = set(range(52))
    rows = []
    for slope in range(6):
        for intercept in range(7):
            line = {52 + 7*x + (slope*x+intercept) % 7 for x in range(7)}
            rows.append(line | {len(rows)})
    medium = verify(101, 43, initial, rows)
    assert medium[0] == 388
    print("Affine-plane example (marks, maximum, distinct sums):", medium)

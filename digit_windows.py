"""Check the finite shifted-window bound on extensions of a digit-box prefix."""
from collections import Counter
from itertools import combinations, product
from math import isqrt, prod


def window_bound(p, dim, old_count, length, h):
    radix = 2*p
    top = (length + radix**(dim-1) - 1) // radix**(dim-1)
    old_support = (p+h-1)**dim
    new_support = (radix+h-1)**(dim-1) * (top+h-1)
    shifts = h**dim
    # The exact overlap inequality is A*T^2 <= B*T+C.
    a = shifts**2 * old_support
    b = new_support * old_support * shifts
    c = new_support * (old_support*(shifts**2+(old_count-1)*shifts)
                       - shifts**2*old_count**2)
    assert c >= 0
    return (b + isqrt(b*b+4*a*c)) // (2*a)


def check_weights():
    for p in (3, 5, 7):
        old = [(x*x % p, x) for x in range(p)]
        gaps = {(b[0]-a[0], b[1]-a[1]) for a in old for b in old if a != b}
        assert len(gaps) == p*(p-1)
        for h in range(1, p+1):
            multiplicity = Counter((x+i, y+j) for x, y in old for i, j in product(range(h), repeat=2))
            energy = sum(n*n for n in multiplicity.values())
            weighted = sum(prod(max(0, h-abs(v)) for v in g) for g in gaps)
            assert energy == p*h*h + weighted
            assert energy*(p+h-1)**2 >= (p*h*h)**2

        # Construct a later block by directly testing ordinary positive gaps.
        old_marks = [a+2*p*b for a, b in old]
        used = {abs(y-x) for x, y in combinations(old_marks, 2)}
        later = []
        for y in range(p**3):
            new_gaps = {y-x for x in later}
            if new_gaps.isdisjoint(used):
                later.append(y)
                used.update(new_gaps)
        assert len(later) <= min(window_bound(p, 2, p, p**3, h) for h in range(1, p+1))


def all_sidon_gap_sets(marks):
    result = []
    for count in range(len(marks)+1):
        for subset in combinations(marks, count):
            gaps = {b-a for a, b in combinations(subset, 2)}
            if len(gaps) == count*(count-1)//2:
                result.append((count, gaps))
    return result


def check_small_bounds():
    for p, dim, length in ((5, 1, 10), (2, 2, 11), (2, 3, 12)):
        old_marks = sorted(sum(v*(2*p)**i for i, v in enumerate(x))
                           for x in product(range(p), repeat=dim))
        old_blocks = all_sidon_gap_sets(old_marks)
        later_blocks = all_sidon_gap_sets(range(length))
        best = {}
        for t, old in old_blocks:
            attainable = max(u for u, later in later_blocks if old.isdisjoint(later))
            best[t] = max(best.get(t, 0), attainable)
        for t, u in best.items():
            for h in range(1, 2*p+1):
                assert u <= window_bound(p, dim, t, length, h)


if __name__ == "__main__":
    check_weights()
    check_small_bounds()
    for p in (101, 1009, 10007, 100003):
        limit, h = min((window_bound(p, 2, p, p**3, h), h) for h in range(1, p+1))
        print(f"p={p}, interval length {p**3}: at most {limit} later marks (h={h})")

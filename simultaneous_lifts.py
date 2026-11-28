"""Check one residue lift at every shallow cutoff and at its final horizon."""
from bisect import bisect_right
from itertools import combinations_with_replacement
from math import isqrt

from incidence_extension import ruler


def prime_at_most(bound):
    for candidate in range(bound, 2, -1):
        if all(candidate % d for d in range(2, isqrt(candidate)+1)):
            return candidate
    raise ValueError("the demonstration needs a larger final horizon")


def build_heights(classes, horizon):
    shallow = classes // 2
    deep = classes - shallow
    prime = prime_at_most(isqrt(deep*horizon//2))
    fibers = [[] for _ in range(deep)]
    for value in ruler(prime):
        quotient, residue = divmod(value, deep)
        assert quotient <= horizon
        fibers[residue].append(quotient)

    rows = [[0, i+1] for i in range(shallow)]
    removed = 0
    for fiber in fibers:
        keep = []
        for height in sorted(fiber):
            if not keep or height - keep[-1] > shallow:
                keep.append(height)
        removed += len(fiber) - len(keep)
        rows.append([height-keep[0] for height in keep] if keep else [0])
    assert removed <= shallow
    return rows, prime, removed


def verify_lift():
    classes, horizon = 101, 10000
    rows, source_size, removed = build_heights(classes, horizon)
    modulus = 4*classes**2
    marks = [1+residue+modulus*height
             for residue, row in zip(ruler(classes), rows) for height in row]
    for cap in range(classes//2+1):
        assert sum(x <= modulus*(cap+1) for x in marks) == classes+cap
    assert max(marks) <= modulus*(horizon+1)
    sums = {a+b for a, b in combinations_with_replacement(marks, 2)}
    assert len(sums) == len(marks)*(len(marks)+1)//2
    print("Source size, removed for spacing, final marks, distinct sums:",
          source_size, removed, len(marks), len(sums))


def verify_tagged_rows():
    p, q, width = 17, 11, 7
    low, high = ruler(p), ruler(q)
    modulus = 4*p*p
    marks = [1+x for x in low]
    for j in range(1, q):
        for tag in range(width):
            index = (j*tag) % p
            marks.append(1+low[index]+modulus*(tag+2*width*high[j]))
    assert len(marks) == p+(q-1)*width
    sums = {a+b for a, b in combinations_with_replacement(marks, 2)}
    assert len(sums) == len(marks)*(len(marks)+1)//2
    print("Tagged extension, final marks and distinct sums:", len(marks), len(sums))


def prime_stride_profile(classes):
    """Use distinct primes for the columns assigned to different height cutoffs."""
    multipliers = [n for n in range(classes+1, 2*classes)
                   if all(n % d for d in range(2, isqrt(n)+1))]
    shallow = classes // 2
    rows = [[0, i+1] for i in range(shallow)]
    levels = [2**k for k in range(classes.bit_length()) if 2**k >= 64]
    for i, multiplier in enumerate(multipliers[:classes-shallow]):
        ratio = levels[i % len(levels)]
        prime = prime_at_most(isqrt(ratio//4))
        unscaled = ruler(prime)
        assert max(unscaled) < classes and multiplier*max(unscaled) <= classes*ratio
        rows.append([multiplier*x for x in unscaled])
    rows.extend([[0] for _ in range(classes-len(rows))])
    gaps = set()
    for row in rows:
        for i, upper in enumerate(row):
            for lower in row[:i]:
                difference = upper-lower
                assert difference > 0 and difference not in gaps
                gaps.add(difference)
    heights = sorted(h for row in rows for h in row)
    for cap in range(shallow+1):
        assert bisect_right(heights, cap) == classes+cap
    return [(cap, bisect_right(heights, cap)-classes)
            for cap in [classes, 8*classes, 64*classes, classes**2]]


if __name__ == "__main__":
    verify_tagged_rows()
    verify_lift()
    print("Uniform lift (height, additions):", prime_stride_profile(1009))

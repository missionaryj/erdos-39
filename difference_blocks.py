"""Check the block encoding and its difference criterion on small finite examples."""
from itertools import combinations, combinations_with_replacement, product


def encode(level, x):
    if level < 1 or not 0 <= x < 1 << (level * level):
        raise ValueError("payload does not fit at this level")
    encoded = 0
    for j in range(1, level + 1):
        width = 2*j - 1
        offset = (j-1)**2
        chunk = (x >> offset) & ((1 << width)-1)
        position = offset + 3*(j-1)
        encoded |= chunk << position
        if j == level:
            encoded |= 1 << (position + width + 1)
    return encoded


def differences_unique(blocks):
    differences = [b-a for block in blocks for a,b in combinations(sorted(block),2)]
    return len(set(differences)) == len(differences)


def sums_unique(values):
    sums = [a+b for a,b in combinations_with_replacement(values,2)]
    return len(set(sums)) == len(sums)


if __name__ == "__main__":
    # Singleton overlaps and identical payloads in different blocks are allowed.
    choices = [[subset for k in range(1, min(4, size)+1)
                for subset in combinations(range(size), k)] for size in (2,5,5)]
    tested = 0
    for blocks in product(*choices):
        if differences_unique(blocks):
            words = [encode(j,x) for j,block in enumerate(blocks,1) for x in block]
            assert len(words) == len(set(words)) and sums_unique(words)
            tested += 1
    # No block construction can hide a repeated within-block difference in
    # this one-chunk example: distinct labels alone do not suffice.
    assert not sums_unique([encode(j,x) for j in (1,2) for x in (0,1)])
    print(f"Verified all {tested} compatible triples in the test family.")

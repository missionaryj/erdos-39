"""Check a finite prefix of the two-colour ruler construction."""
from itertools import combinations_with_replacement
from math import isqrt
from difference_blocks import sums_unique


def marked(level, x):
    """Insert the level marker even when the payload extends past it."""
    fields = max(level, isqrt(max(0, x.bit_length()-1))+1)
    word = 0
    for j in range(1, fields+1):
        width = 2*j-1
        offset = (j-1)**2
        position = offset + 3*(j-1)
        chunk = (x >> offset) & ((1 << width)-1)
        word |= chunk << position
        if j == level:
            word |= 1 << (position+width+1)
    return word


if __name__ == "__main__":
    # The third and fourth primes exceed twice the square of the previous
    # prime of the same colour. Use the full blocks for this finite test.
    primes = [3, 11, 67, 257]
    parts = [[], []]
    labels = {}
    for j,p in enumerate(primes):
        assert all(p % d for d in range(2, isqrt(p)+1))
        if j >= 2:
            assert p > 2*primes[j-2]**2
        for i in range(1,p):
            w = marked(j+1,2*p*i + i*i%p)
            assert w not in labels
            labels[w] = (p,i)
            parts[j%2].append(w)
    for part in parts:
        assert sums_unique(part)
    print("Two Sidon colour sizes:", *(len(part) for part in parts))
    seen = {}
    for a,b in combinations_with_replacement(labels,2):
        s = a+b
        if s in seen:
            c,d = seen[s]
            print("Repeated sum in union:", s, (labels[a],labels[b]), (labels[c],labels[d]))
            assert (a,b) != (c,d) and a+b == c+d
            break
        seen[s] = (a,b)
    else:
        raise AssertionError("expected a mixed-colour collision in this example")

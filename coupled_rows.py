"""Enumerate gaps of a quadratic extension of a prescribed first row."""
from collections import Counter
from itertools import product

from field_bridge import square


def check(prime, nonsquare):
    modulus = (-nonsquare, 0)
    elements = list(product(range(prime), repeat=2))
    squares = {x: square(x, modulus, prime) for x in elements}
    assert len(set(squares.values())) == (prime**2+1)//2
    alpha = next(x for x in elements if x[1] and x not in squares.values())

    points = []
    for b in range(prime):
        for x in elements:
            x2 = squares[x]
            v = ((x2[0] + b + alpha[0]*b*b) % prime, (x2[1] + alpha[1]*b*b) % prime)
            w = tuple(b*a % prime for a in x)
            points.append(x+v+w+(b,))
    projected = Counter()
    full = set()
    for a in points:
        for b in points:
            if a == b:
                continue
            diff = tuple((i-j) % prime for i, j in zip(a, b))
            assert diff not in full
            full.add(diff)
            projected[diff[:-1]] += 1
    assert max(projected.values()) <= 4
    # The zero-height slice in the tagged model is exactly the old parabola.
    assert sum(all(v == 0 for v in x[4:]) for x in points) == prime**2
    print(prime, alpha, len(points), max(projected.values()), len(full))


if __name__ == "__main__":
    print("Prime, alpha, marks, largest projected gap multiplicity, distinct tagged gaps")
    for example in [(3, 2), (5, 2), (7, 3)]:
        check(*example)

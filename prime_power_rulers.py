"""Verify the explicit cubic-precision construction using modular differences."""
from itertools import combinations
from math import isqrt


def prime_below_half(length):
    for q in range((length - 1) // 2, 2, -1):
        if all(q % d for d in range(2, isqrt(q) + 1)):
            return q
    raise ValueError("this example requires an odd prime below half the digit base")


def check(prime, m):
    length = prime**m
    modulus = length**3
    q = prime_below_half(length)
    quotients = [i + length * (i*i % q) for i in range(q)]
    parameters = [a + length * s for a in range(length) for s in quotients]
    seen = set()
    for x, y in combinations(parameters, 2):
        horizontal = (x-y) % modulus
        vertical = (x*x-y*y) % modulus
        # Both orientations must be unique, even if a repeated difference
        # would use one pair in the reverse of the enumerated order.
        for difference in [(horizontal, vertical), (-horizontal % modulus, -vertical % modulus)]:
            assert difference not in seen
            seen.add(difference)
    assert len(seen) == len(parameters) * (len(parameters) - 1)
    return modulus, q, len(parameters), len(seen)


if __name__ == "__main__":
    print("Modulus, auxiliary prime, parameters, distinct ordered differences")
    for prime, m in [(3, 2), (11, 1), (5, 2), (3, 3)]:
        print(*check(prime, m))

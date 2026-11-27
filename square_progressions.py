"""Exact first repeated sum among squares of roots in one residue class."""
from math import gcd


def first_collision(m, r):
    """Scan by largest root. An explicit Gaussian-product witness bounds the scan."""
    assert m >= 3 and m % 2 and 0 < r < m and gcd(m, r) == 1
    k, w = 2*m + 1, m + r
    v = w + m
    limit = max(k*v + m*w, k*w + m*v)
    seen = {}
    for x in range(r, limit + 1, m):
        for y in range(r, x + 1, m):
            value = x*x + y*y
            if value in seen:
                a, b = seen[value]
                assert a*a + b*b == value and (a,b) != (y,x)
                # Exact test for x >= 2(1+sqrt(2))m^2.
                assert x > 2*m*m and (x - 2*m*m)**2 >= 8*m**4
                return (a,b), (y,x)
            seen[value] = (y,x)
    raise AssertionError("explicit witness missing")


if __name__ == "__main__":
    for m in range(3, 36, 2):
        for r in range(1, m):
            if gcd(m, r) == 1:
                first_collision(m, r)
    for m in [3, 5, 11, 31, 101, 251]:
        before, after = first_collision(m, 1)
        print(m, before, after, f"{after[1]/m**2:.5f}")

"""Check reconstructed chords and solve small two-level thinning instances."""
from collections import Counter, defaultdict
from functools import cache
from itertools import combinations, combinations_with_replacement
from random import Random

from field_bridge import graph_points, lift


def fiber_edges(prime, nonsquare, cubic):
    assert all(x*x % prime != nonsquare for x in range(prime))
    assert all((x**3 + cubic[2]*x*x + cubic[1]*x + cubic[0]) % prime
               for x in range(prime))
    small = graph_points(prime, (-nonsquare, 0))
    large = graph_points(prime, cubic)
    gaps = {}
    for i, (x, y) in enumerate(small):
        for j, (u, v) in enumerate(small):
            if i != j:
                key = tuple((b-a) % prime for a, b in zip(x+y, u+v))
                assert key not in gaps
                gaps[key] = (i, j)
    fibers = defaultdict(list)
    for i, (x, y) in enumerate(large):
        fibers[x[2], y[2]].append(i)
    constant, linear, quadratic = cubic
    k = -quadratic % prime
    ell = (k*k-linear) % prime
    groups = []
    max_degree = 0
    for (e, f), indices in fibers.items():
        edges = []
        degree = Counter()
        for a, b in combinations(range(len(indices)), 2):
            x, y = large[indices[a]]
            u, v = large[indices[b]]
            key = tuple((j-i) % prime for i, j in zip(x[:2]+y[:2], u[:2]+v[:2]))
            i, j = gaps[key]
            edges.append((a, b, (1 << i) | (1 << j)))
            if e:
                degree.update((i, j))
                inv2 = pow(2, -1, prime)
                t = (u[1]+x[1])*inv2 % prime
                h = (u[1]-x[1])*inv2 % prime
                rho = (-t*pow(e, -1, prime)-k) % prime
                value = ((-rho)**3 + quadratic*rho**2-linear*rho+constant) % prime
                a1 = e*value*pow((rho*rho-nonsquare) % prime, -1, prime) % prime
                z1 = (a1-h) % prime
                ubar = (f-t*t-h*h-2*k*e*t-ell*e*e)*pow(2*e, -1, prime)
                z0 = (ubar-rho*a1-e*(linear-quadratic*rho+rho*rho)-rho*h) % prime
                assert small[i][0] == (z0, z1)
        if degree:
            max_degree = max(max_degree, max(degree.values()))
        groups.append((indices, edges))
    assert max_degree <= 6
    return small, large, groups, max_degree


def survivors(groups, old_mask):
    selected = []
    for indices, edges in groups:
        adj = [0] * len(indices)
        for i, j, old_pair in edges:
            if old_mask & old_pair == old_pair:
                adj[i] |= 1 << j
                adj[j] |= 1 << i

        @cache
        def largest(mask):
            if not mask:
                return 0
            bit = mask & -mask
            rest = mask ^ bit
            with_first = bit | largest(rest & ~adj[bit.bit_length()-1])
            if not rest & adj[bit.bit_length()-1]:
                return with_first
            without_first = largest(rest)
            return max((with_first, without_first), key=int.bit_count)

        mask = largest((1 << len(indices))-1)
        selected.extend(v for i, v in enumerate(indices) if (mask >> i) & 1)
    return selected


def run(prime, nonsquare, cubic):
    small, large, groups, degree = fiber_edges(prime, nonsquare, cubic)
    if prime == 3:
        maxima = [0] * (len(small)+1)
        for old_mask in range(1 << len(small)):
            k = old_mask.bit_count()
            maxima[k] = max(maxima[k], len(survivors(groups, old_mask)))
        print("p=3, optimal later counts by earlier count:", maxima)
    old = Random(39).sample(range(len(small)), len(small)//2)
    new = survivors(groups, sum(1 << i for i in old))
    marks = [4*lift(small[i], prime)+1 for i in old]
    marks.extend(4*lift(large[i], prime)+2 for i in new)
    sums = {a+b for a, b in combinations_with_replacement(marks, 2)}
    assert len(sums) == len(marks)*(len(marks)+1)//2
    print(prime, degree, len(old), len(new), len(sums))


if __name__ == "__main__":
    print("Prime, maximum chord degree in regular fibers, old marks, new marks, distinct sums")
    for example in [(3, 2, (1, 2, 0)), (5, 3, (1, 1, 0)), (7, 6, (2, 0, 0)),
                    (11, 2, (4, 1, 0))]:
        run(*example)

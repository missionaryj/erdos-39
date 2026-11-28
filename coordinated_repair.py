"""Verify exact two-block repair costs for early parameters on two parallel lines."""
from itertools import combinations
from random import Random

from fiber_thinning import fiber_edges, survivors
from field_bridge import lift, square


def ordinary_groups(groups, earlier, later):
    result = []
    for indices, edges in groups:
        matched = []
        for a, b, pair in edges:
            i = (pair & -pair).bit_length() - 1
            j = (pair ^ (1 << i)).bit_length() - 1
            if abs(earlier[i] - earlier[j]) == abs(later[indices[a]] - later[indices[b]]):
                matched.append((a, b, pair))
        result.append((indices, matched))
    return result


def run(p, nonsquare, cubic):
    small, large, groups, _ = fiber_edges(p, nonsquare, cubic)
    earlier = [lift(point, p) for point in small]
    later = [lift(point, p) for point in large]
    ordinary = ordinary_groups(groups, earlier, later)
    common = sum(len(edges) for _, edges in ordinary)
    assert sum(len(edges) for _, edges in groups) == len(small) * (len(small) - 1) // 2
    if p <= 7:
        early_gaps = {abs(x - y) for x, y in combinations(earlier, 2)}
        direct = sum(abs(x - y) in early_gaps for x, y in combinations(later, 2))
        assert direct == common
    lookup = {x: i for i, (x, _) in enumerate(large)}
    rng = Random(39)
    lines = [i for i, ((_, s), _) in enumerate(small) if s in (1, p - 1)]
    rng.shuffle(lines)
    for k in range(1, len(lines) + 1):
        chosen = lines[:k]
        mask = sum(1 << i for i in chosen)
        offsets = {later[lookup[small[i][0] + (0,)]] - earlier[i] for i in chosen}
        assert 1 <= len(offsets) <= 2
        modular_loss = len(large) - len(survivors(groups, mask))
        kept = survivors(ordinary, mask)
        ordinary_loss = len(large) - len(kept)
        assert (modular_loss, ordinary_loss) == (k - 1, k - len(offsets))

    # Directly test all actual earlier gaps against the optimal final extension.
    forbidden = {abs(earlier[i] - earlier[j]) for i, j in combinations(lines, 2)}
    kept_marks = {later[i] for i in kept}
    assert all(x + gap not in kept_marks for x in kept_marks for gap in forbidden)

    sample = rng.sample(range(len(small)), len(lines))
    mask = sum(1 << i for i in sample)
    sampled_losses = [len(large) - len(survivors(graph, mask)) for graph in (groups, ordinary)]
    print(p, common, len(lines), modular_loss, ordinary_loss, *sampled_losses)


def verify_opposite_digits(p, d):
    # Fix B=-D and C=1. Among the p possible quadratic coefficients at least
    # one gives no root: each of the p-1 nonzero roots rules out one choice.
    excluded = {-(x**3 - d*x + 1) * pow(x*x, -1, p) % p for x in range(1, p)}
    quadratic = next(a for a in range(p) if a not in excluded)
    small, large, groups, _ = fiber_edges(p, d, (1, -d, quadratic))
    earlier = [lift(point, p) for point in small]
    later = [lift(point, p) for point in large]
    ordinary = ordinary_groups(groups, earlier, later)
    rows = [[i for i, ((_, s), _) in enumerate(small) if s == t] for t in (0, p-1)]
    left, right = (sum(1 << i for i in row) for row in rows)
    modular_cross = sum(1 for _, edges in groups for _, _, pair in edges
                        if pair & left and pair & right)
    ordinary_cross = sum(1 for _, edges in ordinary for _, _, pair in edges
                         if pair & left and pair & right)
    assert modular_cross == p*p and ordinary_cross == 0
    mask = left | right
    modular_loss = len(large) - len(survivors(groups, mask))
    ordinary_loss = len(large) - len(survivors(ordinary, mask))
    wraps = {((r*r % p) + d >= p) for r in range(p)}
    assert modular_loss >= (p*p+1)//2 + 2*(p-1)
    assert ordinary_loss == 2*p - 1 - len(wraps)
    print(p, modular_cross, ordinary_cross, modular_loss, ordinary_loss)


def sampled_density(p, trials):
    # Use theta^3 = c, with c a noncube, so K has degree three.
    assert p % 3 == 1
    c = next(i for i in range(2, p) if pow(i, (p - 1) // 3, p) != 1)
    d = next(i for i in range(2, p) if pow(i, (p - 1) // 2, p) != 1)
    rng = Random(39)
    matches = 0
    for _ in range(trials):
        r, s, rho = (rng.randrange(p) for _ in range(3))
        h = rng.randrange(1, p)
        # (theta^2 - D)(theta^2 - rho*theta + rho^2) / P(-rho).
        inv = pow(-rho**3 - c, -1, p)
        j0 = (-rho*c - d*rho*rho) * inv
        j1 = (rho*d + c) * inv
        j2 = (rho*rho - d) * inv
        a = (r, s)
        b = ((r + 2*h*rho) % p, (s + 2*h) % p)
        x = ((r + (s+h)*j0) % p, (s + (s+h)*j1) % p, ((s+h)*j2) % p)
        y = ((x[0] + 2*h*rho) % p, (x[1] + 2*h) % p, x[2])
        a2, b2 = (square(v, (-d, 0), p) for v in (a, b))
        x2, y2 = (square(v, (-c, 0, 0), p) for v in (x, y))
        assert all((v-u-t+w) % p == 0 for u, v, w, t in zip(a2+(0,), b2+(0,), x2, y2))
        matches += lift((b, b2), p) - lift((a, a2), p) == lift((y, y2), p) - lift((x, x2), p)
    return matches


if __name__ == "__main__":
    print("p, full ordinary conflicts, early count, aligned modular/integer losses, sampled losses")
    for example in [(3, 2, (1, 2, 0)), (5, 3, (1, 1, 0)), (7, 6, (2, 0, 0)),
                    (11, 2, (4, 1, 0)), (17, 3, (3, 1, 0))]:
        run(*example)
    print("p, opposite-digit cross conflicts modular/integer, total losses modular/integer")
    for p, d in ((3, 2), (5, 3), (7, 6), (11, 2), (17, 3)):
        verify_opposite_digits(p, d)
    print("p, sampled ordinary matches out of 30000 nonhorizontal earlier chords")
    for p in (1009, 100003):
        print(p, sampled_density(p, 30000))

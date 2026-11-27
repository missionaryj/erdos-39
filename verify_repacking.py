"""Verify the repacked witness and an exact bound for its frozen prefix."""
import json
from itertools import combinations, combinations_with_replacement
from pathlib import Path

data = Path(__file__).resolve().parent / "data"
original = json.loads((data / "witness.json").read_text())
points = json.loads((data / "repacked-witness.json").read_text())
limit = 2**20
boundary = limit // 4
prefix = [a for a in original if a <= boundary]
assert points == sorted(set(points)) and 1 <= points[0] <= points[-1] <= limit
assert [a for a in points if a <= boundary] == prefix
assert len(prefix) == 208 and len(points) == 357
sums = {a + b for a, b in combinations_with_replacement(points, 2)}
assert len(sums) == len(points) * (len(points) + 1) // 2
print(f"{len(points) - len(prefix)} additions, {len(sums)} distinct sums")

h = 4657
span = limit - boundary + h - 1
gaps = [b - a for a, b in combinations(prefix, 2)]
assert len(gaps) == len(set(gaps))
budget = h * (h - 1) - 2 * sum(h - d for d in gaps if d < h)
for t in (747, 748):
    q, r = divmod(t * h, span)
    minimum = span * q * (q - 1) + 2 * q * r
    print(f"{t} additions require at least {minimum} ordered overlaps, budget {budget}")
    assert (minimum <= budget) == (t == 747)

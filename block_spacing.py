"""Check spacing extraction against exact interval optima for a finite Sidon witness."""
from bisect import bisect_right
from itertools import combinations
from math import isqrt
from pathlib import Path
import json


def extract(points, gap):
    result = []
    for x in points:
        if not result or x - result[-1] >= gap:
            result.append(x)
    return result


def optimum_size(points, gap):
    # For each prefix, compare keeping or skipping its last point.
    best = [0]
    for i, x in enumerate(points):
        compatible = bisect_right(points, x - gap, 0, i)
        best.append(max(best[-1], 1 + best[compatible]))
    return best[-1]


if __name__ == "__main__":
    data = Path(__file__).resolve().parent / "data" / "repacked-witness.json"
    witness = json.loads(data.read_text())
    for X in (4096, 16384, 65536, 262144, 1048576):
        points = [x for x in witness if x < X]
        gap = isqrt(X)
        selected = extract(points, gap)
        edges = sum(b-a < gap for a,b in combinations(points, 2))
        assert edges <= gap-1
        assert all(b-a >= gap for a,b in zip(selected, selected[1:]))
        assert len(selected) == optimum_size(points, gap)
        assert len(selected)*(len(points)+2*edges) >= len(points)**2
        print(X, len(points), gap, edges, len(selected))

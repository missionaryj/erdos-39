"""Thin four marked rulers and verify all sums after joining the survivors."""
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from random import Random

from interlaced import marked


def gap_map(block):
    gaps = {abs(x-y): (i,j) for (i,x),(j,y) in combinations(enumerate(block), 2)}
    assert len(gaps) == len(block)*(len(block)-1)//2
    return gaps


def independent_indices(size, edges):
    """Choose a minimum-degree remaining vertex; mark all its neighbours unavailable."""
    neighbours = [0]*size
    for i,j in edges:
        neighbours[i] |= 1 << j
        neighbours[j] |= 1 << i
    remaining = (1 << size)-1
    selected = []
    while remaining:
        candidates = (i for i in range(size) if remaining & (1 << i))
        vertex = min(candidates, key=lambda i: (neighbours[i] & remaining).bit_count())
        selected.append(vertex)
        remaining &= ~(neighbours[vertex] | (1 << vertex))
    return selected


if __name__ == "__main__":
    blocks = [[marked(j,2*p*i+i*i%p) for i in range(1,p)]
              for j,p in enumerate([3,11,67,257],1)]
    maps = [gap_map(block) for block in blocks]
    fixed = blocks[0]+blocks[1]
    old = set(maps[0]) | set(maps[1])
    assert not (set(maps[0]) & set(maps[1]))
    third = independent_indices(len(blocks[2]), [maps[2][d] for d in old if d in maps[2]])
    fixed_edges = [maps[3][d] for d in old if d in maps[3]]
    matches = [(maps[2][d],maps[3][d]) for d in sorted(set(maps[2]) & set(maps[3]))]
    rng = Random(39)
    best_key = (Fraction(0),0)
    for count in range(42,57):
        for _ in range(12):
            keep = set(rng.sample(third,count))
            edges = fixed_edges + [pair for (i,j),pair in matches if i in keep and j in keep]
            last = independent_indices(len(blocks[3]),edges)
            key = (min(Fraction(count,len(blocks[2])),Fraction(len(last),len(blocks[3]))),
                   count+len(last))
            if key > best_key:
                best_key = key
                best = [fixed, [blocks[2][i] for i in sorted(keep)],
                        [blocks[3][i] for i in last]]
    joined = sum(best, [])
    sums = {a+b for a,b in combinations_with_replacement(joined,2)}
    assert len(sums) == len(joined)*(len(joined)+1)//2
    print("Retained by block:", len(blocks[0]),len(blocks[1]),len(best[1]),len(best[2]))
    print("Smallest retained fraction:",best_key[0])
    print("Joined size:",len(joined),"Distinct sums:",len(sums))

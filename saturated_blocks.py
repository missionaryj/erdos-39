"""Exact two-block bounds; verify an example from the cyclic Sidon construction."""
from itertools import combinations
from math import gcd
from random import Random


def cyclic_block(p):
    # For these prime inputs an element of order p-1 is a primitive root.
    g = next(g for g in range(2,p) if len({pow(g,i,p) for i in range(p-1)}) == p-1)
    return [i+(p-1)*((i-pow(g,i,p)) % p) for i in range(p-1)]


def gaps(points):
    result = {b-a for a,b in combinations(sorted(points),2)}
    assert len(result) == len(points)*(len(points)-1)//2
    return result


def excess(m,n,t,u,h):
    # Returns numerator and denominator of a lower bound on twice the
    # weighted overlap, counting weight h-d at common differences d<h.
    a,b = m+h-1,n+h-1
    denominator = a*b
    numerator = (h*t)**2*b + (h*u)**2*a - h*(t+u+h-1)*denominator
    return numerator,denominator


def rounded_up(a,b):
    return -(-a//b)


if __name__ == '__main__':
    p,q = 127,631
    m,n = p*(p-1),q*(q-1)
    old,large = cyclic_block(p),cyclic_block(q)
    old_gaps = gaps(old)
    t,u = len(old),len(large)
    overlap_floor,width = 0,0
    ceiling = u
    for h in range(2,m+1):
        num,den = excess(m,n,t,u,h)
        count = rounded_up(num,2*(h-1)*den)
        if count > overlap_floor:
            overlap_floor,width = count,h
        while excess(m,n,t,ceiling,h)[0] > 0:
            ceiling -= 1
    print(f"At sizes {t}, {u}, at least {overlap_floor} shared gaps (h={width}).")
    print(f"With {t} old marks and disjoint gaps, at most {ceiling} new marks.")
    rng = Random(39)
    for trial in range(6):
        a,b = 1,0
        if trial:
            b = rng.randrange(n)
            while True:
                a = rng.randrange(1,n)
                if gcd(a,n) == 1:
                    break
        overlap = len(old_gaps & gaps([(a*x+b) % n for x in large]))
        assert overlap >= overlap_floor
        print(f"a={a}, b={b}, common positive differences={overlap}")

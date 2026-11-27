"""Compare exact mixed digit-sum collisions with CRT candidates in two finite layers."""
from collections import Counter
from itertools import combinations
from math import gcd, isqrt, prod


def primes(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[:2] = bytes(2)
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p*p::p] = bytes((limit-p*p)//p+1)
    return [i for i, v in enumerate(sieve) if v]


def digit_table(q):
    factors = [p for p in primes(q-1) if (q-1) % p == 0]
    g = next(i for i in range(2,q) if all(pow(i,(q-1)//p,q)!=1 for p in factors))
    return {pow(g,i,q): i for i in range(q+1,2*q)}


def reconstruct(t, modulus, bound):
    """Find a reduced positive numerator/denominator at most bound; 2*bound² < modulus."""
    assert 2*bound*bound < modulus
    a,b = t, modulus
    prev, curr = 1, 0  # denominators of successive continued-fraction convergents
    while b:
        digit, remainder = divmod(a,b)
        denominator = digit*curr + prev
        if denominator > bound:
            break
        numerator = t*denominator % modulus
        if 0 < numerator <= bound and gcd(numerator,denominator)==1:
            return numerator, denominator
        prev,curr = curr, denominator
        a,b = b,remainder
    return None


def experiment(shared, exclusive):
    moduli = shared + exclusive
    u,v = prod(shared),prod(exclusive)
    modulus = u*v
    x,y = isqrt((modulus-1)//2),isqrt((u-1)//2)
    labels = [p for p in primes(x) if p not in moduli]
    low = [p for p in labels if p<=y]
    high = {p for p in labels if p>y}
    tables = [digit_table(q) for q in moduli]

    def encode(p, depth):
        value = 0
        for i in reversed(range(depth)):
            value = value*4*moduli[i]+tables[i][p % moduli[i]]
        return value

    candidates = set()
    for s,z in combinations(low,2):
        ratio = z*pow(s,-1,u) % u
        t = 1+v*((ratio-1)*pow(v,-1,u) % u)
        pair = reconstruct(t,modulus,x)
        if pair and all(p in high for p in pair):
            p,h = pair
            candidates.add((s,z,p,h))

    brute = {(s,z,p,h) for s,z in combinations(low,2) for p in high
             for h in high if p!=h and (p-h)%v==0 and (p*s-h*z)%u==0}
    assert candidates == brute
    lo = {p:encode(p,len(shared)) for p in low}
    hi = {p:encode(p,len(moduli)) for p in high}
    exact = {row for row in candidates if lo[row[0]]+hi[row[2]]==lo[row[1]]+hi[row[3]]}
    sums = [a+b for a in lo.values() for b in hi.values()]
    assert len(exact) == sum(n*(n-1)//2 for n in Counter(sums).values())
    print(shared,exclusive,len(low),len(high),len(candidates),len(exact))


if __name__ == '__main__':
    for common,tail in [([101,103],[7]),([307],[7]),([61,73],[11])]:
        experiment(common,tail)

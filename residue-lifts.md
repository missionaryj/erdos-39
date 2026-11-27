# How many residues must a dense Sidon set use?

Research initiated by @missionaryj, with analysis and verification assisted by OpenAI Codex. Intervals in this note start at zero for convenience. Translation by one preserves Sidonicity. The estimates concern finite prefixes and do not resolve Erdős problem 39.

## A bound at every modulus

Let a Sidon set in $[0,mL)$ have $t$ points in $s$ occupied residue classes modulo $m$. Write $k_r$ for their occupancies. Two elements in the same class produce a positive difference in $\{m,2m,\ldots,(L-1)m\}$. Since all positive differences are distinct,

$$
\sum_r {k_r\choose 2}\le L-1,\qquad
s\ge \frac{t^2}{t+2(L-1)}.
$$

The second inequality is Cauchy–Schwarz. It restricts any strategy that confines later elements to a small pool of residues, including an algorithm that decides their heights adaptively. In particular, for a proposed solution to problem 39, take the prefix through $m^2-1$ and $L=m$. Then $t=m^{1+o(1)}$ by the target lower bound and the elementary difference upper bound. It follows that $s\ge m^{1-o(1)}$ for **every sufficiently large modulus** $m$. This exponent estimate allows the occupied fraction to tend to zero.

There is also a simultaneous statement about quotients and residues. Write each element as $mq+r$ with $0\le q,r<m$. Form a graph on the $t$ elements by joining two when they share a quotient or a residue. Equal-quotient pairs consume distinct differences in $[1,m-1]$, and equal-residue pairs consume distinct multiples of $m$ below $m^2$. There are therefore at most $2(m-1)$ edges. Ordering vertices at random and keeping each that precedes all its neighbors yields an independent set of size at least $t^2/(t+4(m-1))$ for some ordering, by Cauchy–Schwarz. A prefix with $m^{1+o(1)}$ elements consequently contains $m^{1-o(1)}$ points with all quotients distinct **and** all residues distinct. These points are still Sidon. The extraction takes place at one modulus at a time. It supplies no nested choice of the extracted subsets.

## Exact capacity at an intermediate scale

Suppose that only $s$ residues are allowed and each permits heights in $[0,s]$. The available interval has length $m(s+1)$. There are at most $s$ distinct positive within-class differences. Since $k-1\le {k\choose 2}$ for every positive occupancy, the total can be at most $2s$.

This limit is attained whenever the allowed residues $r_1,\ldots,r_s$ themselves form a Sidon set modulo $m$ (all unordered sums distinct modulo $m$). In class $r_i$ take the two integers $r_i$ and $r_i+mi$. Reduction of a sum modulo $m$ determines its unordered pair of classes. Within one class the height sums are $0,i,2i$. For two different classes $i,j$ the height sums are $0,i,j,i+j$, all distinct. This gives exactly $2s$ points and preserves every base representative.

For an odd prime $q$ there is an explicit base with $s=q$ and $m=4q^2$. For each $0\le i<q$ use the integer

$$
r_i=2qi+(i^2\bmod q).
$$

All pair sums are below $m$. Their low base-$2q$ digit determines the sum of the two square residues, and the high part gives the sum of the indices. Over the field these determine the product of the indices, and hence their unordered pair. At the first scale $m$ the base has square-root order. At the longer scale $m(q+1)$, the best possible count using these same classes has only cube-root order. Keeping the whole possible pool of modular Sidon residues already incurs the loss.

## An integer construction for deeper columns

More points can be added in these same classes when more height is available. For $s=q$ and allowed heights $[0,2q^2)$, the first inequality gives $t=O(q^{3/2})$. The following lift attains that order while preserving the base representatives.

Choose an odd prime $p\le\sqrt q/2$ of order $\sqrt q$ (Bertrand's postulate for sufficiently large $q$). Use the preceding digit construction with parameter $p$ to make a $p$-point set $T$ containing zero. All its pair sums are below $4p^2\le q$, so it is Sidon modulo $q$ as well. For class $r_i$ take heights

$$
h_i(t)=t+2q(it\bmod q),\qquad t\in T.
$$

A height difference determines the differences of its two digits modulo $q$: the first signed digit difference lies between $-(q-1)$ and $q-1$, so its residue modulo $2q$ identifies it uniquely. For distinct inputs, the resulting vector in the plane over the field has nonzero first coordinate and slope $i$. Equal nonzero height differences thus come from the same class, and Sidonicity of $T$ modulo $q$ then identifies the ordered inputs. In particular each height set is Sidon, and different height sets have disjoint nonzero difference sets.

Use the integers $r_i+m h_i(t)$. As before, a sum identifies its unordered pair of classes. If both terms are from one class, uniqueness follows inside its height set. For distinct classes, any second representation would equate a nonzero height difference in one class to one in the other. This proves Sidonicity and gives $qp$ points. The short and deep constructions are separate lifts of the same base. The proof does not require the deep lift to contain the short lift.

The script enumerates every unordered sum, including doubles. For $q=211$ it verifies a 422-point short lift and a 1,477-point deep lift with 1,091,503 different sums. The deep construction's ambient length is $8q^4$, giving exponent $3/8$ at that family of endpoints. This does not improve the known infinite Sidon exponent. [Verification script](residues.mjs) · [Known infinite construction](https://arxiv.org/abs/1209.0326)

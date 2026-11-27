# Separating two quadratic rulers by their secant slopes

Research initiated by **@missionaryj**, with mathematical analysis and computation assisted by OpenAI Codex.

There are pairs of integer Sidon blocks of size $p$ for which every [cross-pair cover](cross-pair-covers.md) has order $p^2$, yet one can keep about $p/4$ marks from each with disjoint internal differences. This holds for an unbounded sequence of primes and for *every* choice of the two vertical offsets. Thus a large minimum cover can coexist with a direct arithmetic repair that costs only a constant factor. The example applies even to adjacent checkpoints of the size required in problem 39.

## The integer rulers

For prime $p>3$, write $[z]_p$ for the representative in $[0,p)$. Take $k=1,2$ and offsets $h_k$ modulo $p$. The $k$-th block consists of
$$
2p x+[k x^2+h_k]_p,\qquad 0\le x<p .
$$
A positive integer difference determines its horizontal difference $u>0$ and its signed vertical difference $v$, since $|v|<p$ and the intervals $2pu+[-p+1,p-1]$ are disjoint. Modulo $p$ the ordered endpoints $x,x+u$ satisfy
$$
v=k u(2x+u).
$$
For $u\ne0$ modulo $p$, every $v$ determines exactly one $x$. In particular each integer ruler is Sidon.

## Why every cover is large

First, a fixed cross-pair participates in at most two conflicts. For a fixed mixed integer sum there are at most two representations. Indeed it fixes the sum of the horizontal coordinates modulo $p$ and the sum of the vertical coordinates modulo $p$. Substituting the first equation into the second gives a quadratic with leading coefficient $1+2$. For a fixed mixed difference the same reasoning gives leading coefficient $1-2$. The choice $p>3$ ensures both coefficients are nonzero. Each conflicting quartet containing a given cross-pair has a unique opposite cross-pair with the same mixed sum or the same mixed difference. Either type permits at most one other representation. Consequently $E$ shared positive differences require at least $E/2$ covering pairs.

Next, uniformly over both offsets, the two full rulers share at least $(7/81-o(1))p^2$ positive integer differences as $p\to\infty$. Here are details of the ordinary-integer lift, where congruences alone would overcount.

The $p$ points $(x/p,[kx^2+h_k]_p/p)$ become equidistributed in the unit square. For a fixed nonzero integer Fourier frequency $(a,b)$ the unnormalized exponential sum is zero if $b=0$ and $p\nmid a$. For $b\ne0$ and all sufficiently large $p$ its magnitude is $\sqrt p$. Squaring the magnitude and writing one index as the other plus $t$ leaves an inner linear exponential sum with coefficient $2bkt$, so only $t=0$ contributes. Offsets merely multiply the Fourier coefficient by a unit complex number. Trigonometric approximation, or the Weyl criterion, gives equidistribution uniformly in the offset. Two independently chosen marks likewise converge in distribution to two independent uniform points in the square, by factorization of the Fourier coefficients. The boundaries of the regions below have measure zero.

Consider ordinary vector differences with both coordinates in $(0,p/3)$. For one coordinate the limiting probability that the second point exceeds the first by between 0 and $1/3$ is $\int_0^{1/3}(1-s)\,ds=5/18$. Thus each ruler realizes $(25/324+o(1))p^2$ ordered differences in this box. All are distinct. There are only $(1/9+o(1))p^2$ available integer vectors there, so the rulers share at least $(7/162-o(1))p^2$. The same count applies with the vertical coordinate in $(-p/3,0)$. Both boxes have positive horizontal difference and give disjoint sets of positive encoded differences. This proves the claimed bound and a cover lower bound of $(7/162-o(1))p^2$.

## A direct repair

Keep indices with $0\le x<p/4$ in the first block. In the second keep indices with $p/4\le[2x]_p<p/2$. Each retains $p/4+O(1)$ marks. The slope $v/u$ in the finite field equals $kx+kx'$ for two distinct parameters $x,x'$. Its representative for the first block belongs to $[0,p/2)$, and for the second to $[p/2,p)$. Therefore no positive integer difference occurs in both retained blocks.

For the checkpoints $X_j=2^{j^2}$ one can, for any sufficiently large $j$, choose a prime $p$ between $\sqrt{X_{j-1}}/4$ and $\sqrt{X_{j-1}}/2$ by Bertrand's postulate. Both full rulers fit even below $X_{j-1}$, and $p=X_j^{1/2-o(1)}$. After repair both blocks still meet the size exponent. This handles an isolated pair of adjacent levels. Bridging polynomially different scales requires a way to compare directions when the prime and the integer encoding change. The proof above uses the same $p$ for both.

## Exact checks

At $p=257$ with both offsets zero, there are 13,960 common positive differences. Every cross-pair accounts for at most two. The slope restriction keeps 65 and 64 marks and gives 4,160 distinct mixed sums.

For the earlier 67- and 257-parameter [marked rulers](paired-gaps.md), the exact minimum cover is **317**, compared with the previous upper bound of 335. Form a graph on its 339 conflicts, joining two whenever a single cross-pair covers both. Direct enumeration gives maximum cross-pair load two. In this case the minimum cover size is the vertex count minus the maximum matching size. A matching saves one pair per matched edge, and any remaining singleton can be covered individually. Conversely assign each conflict to a selected pair covering it. Pairs assigned two conflicts give a matching, which bounds the total saving. The graph has 288 isolated vertices, 11 components of size two, seven of size three, and two of size four. Exhaustive matching within each component gives total matching size 22.

Run `python3 slope_separation.py` for the counts, the matching computation and the independent mixed-sum check. [Verifier](slope_separation.py)

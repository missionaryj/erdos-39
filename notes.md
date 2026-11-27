# Mathematical notes

## Finite reformulation

Write A(N) for the count through N. It suffices to find a single sequence δⱼ→0 such that, for each k, some Sidon subset of [1,2ᵏ] has at least 2^((1/2−δⱼ)j) points through 2ʲ for every 1≤j≤k. Repeatedly take infinite subsequences with the same prefix through 2ʲ, possible by finiteness. The stabilized prefixes agree and their union is Sidon since any collision has finite support. The dyadic bounds extend to intermediate N by monotonicity. Conversely, translate any solution to start at 1 and truncate it. Its dyadic log-count divided by j (log base 2) has liminf at least 1/2. Taking the positive part of the deficit from 1/2 gives the required δⱼ. A large count at the last checkpoint alone gives no such conclusion.

## Appending an interval

Let B in [1,M] and T in [3M,4M] be Sidon with sizes b,t and t>0. The three sum ranges for old-old, old-new and new-new pairs are disjoint. On T join each pair whose positive difference occurs in B. Sidonicity of T gives at most b(b−1)/2 edges. In a random ordering, keep vertices preceding all their neighbors. The expected number is the sum of 1/(1+degree), at least t²/(t+b(b−1)) by Cauchy–Schwarz. Some independent set of this size can therefore be appended to B. When t is of order √M, this estimate permits a constant fraction of T for b≤M^(1/4). It is too weak near the desired exponent.

## Algebraic constructions

Over an odd-characteristic field or polynomial ring the graph (x,x²) is Sidon. The two coordinate sums determine the product of the inputs and hence their unordered pair, by factoring the monic quadratic over the fraction field. Degree less than d gives d input coefficients and up to 2d−1 square coefficients. Any single linear summary L of the squares that works on the entire polynomial ring must be injective. If L(h)=0 for nonzero h, the distinct pairs {0,h+1} and {1,h} have equal first sums and their square sums differ by 2h. This argument leaves open restricted input families and summaries that vary with the stage.

For x=a+bu over F₃ retain input and square coordinates using u²=0 or u²=2. Among subsets containing all three constants, exhaustive checking gives maximum sizes 6 and 9 respectively. The second quotient is a field. In the first quotient a maximizing family consists of all inputs with b=0 or b=1.

### Intermediate scales in a field tower

Let K have odd order q and take its quadratic extension with u² a nonsquare of K. A block fixes the new coordinates of input and output, leaving q² ambient positions. For the square graph the label is (b,2ab). The zero label contains q points. A label with b≠0 determines a unique input, and other labels are empty. The q most populated whole blocks contain exactly 2q−1 points among q³ positions. Repeating such whole-block orderings gives exponent at most 1/3 on these scales. This calculation concerns the finite array before any integer encoding. The script verifies counts 5, 9, 13, 17 and 21 for q=3,5,7,9 and 11.

More generally, assume a Sidon graph over the larger field contains the complete graph of a function K→K over the old field. For each nonzero old shift h, all q output differences f(a+h)−f(a) are distinct and therefore exhaust K. Two distinct points in one other block would supply an old-coordinate difference with nonzero input shift, already realized in the old block. Thus every other block contains at most one point. Thinning to r old points uses precisely r(r−1) of the q(q−1) directed old differences with nonzero input shift. Taking r about q/2 frees roughly three quarters of the differences while preserving the old exponent. Making collisions between the new blocks simultaneously avoidable remains unresolved.

## Integer search

A finite integer set is Sidon exactly when all its positive differences are distinct, by rearranging a repeated sum or difference. When adjoining x, check the absolute distances to existing elements against old distances and against one another. The second check handles a midpoint between two old elements. In the prefix search we shuffle each interval, set a random occupancy target at the first four checkpoints, and maximize the smallest observed ratio A(N)/√N over five checkpoints. Ties keep the earlier trial. Subsequent stages use one seeded shuffle per interval and accept every compatible addition. This produces a maximal extension within each scanned interval for that ordering. Optimality does not follow.

## Difference bounds for a fixed prefix

Let D be the positive differences of the retained prefix. Suppose t new points lie in an interval of length L (number of integer positions). Split into m=ceil(L/H) consecutive bins of width at most H. If their occupancies are tᵢ then

    ∑ binom(tᵢ,2) ≤ H−1−|D ∩ [1,H−1]|.

Every within-bin pair consumes a distinct available short difference. Balanced occupancies minimize the left side for fixed t. For the last extension L=786432 and the 208 old points are fixed. Width 3347 gives 235 bins and a budget of 1893 differences, bounding t by 1060.

### Counting shifted intervals

For a positive integer h let R(y) count representations y=x+i with x a new point and 1≤i≤h. There are th representations across at most L+h−1 positions. Every positive new-to-new difference is distinct and avoids D. Expanding the sum of squares gives

    (th)²/(L+h−1) ≤ ∑ R(y)²
                   ≤ th + h(h−1) − 2∑_{d∈D, d<h}(h−d).

The lower bound is Cauchy–Schwarz. On the right, a difference d<h contributes twice its overlap h−d. Summing over all possible d and subtracting the old differences gives the stated upper bound. This uses only internal differences of each set, so additional constraints may improve the bound.

With h=4722 the verified witness prefix gives (4722t)² ≤ 791153(4722t+12424446). The largest admissible integer is 752. Direct evaluation at 752 and 753 verifies the cutoff. This leaves the optimum between 138 and 752 inclusive. A stronger bound or a denser extension for this one prefix would still leave the infinite problem open.

### Repacking the last interval

Fix exactly the same 208 old points. Starting from the 346-point greedy set, remove one point above the cutoff and try replacing it by several compatible points. To limit the search, for each possible new point intersect the sets of old endpoints involved in its collisions. A removal can make that point admissible only if it hits every collision. The C++ search also checks for repeated distances to the new point itself and rechecks compatibility between replacements. Seven improving rounds give 357 points in total. All 63,903 unordered sums, including doubles, were independently verified.

The upper bound also improves by preserving the integer values of the shifted-interval counts. Write $S=L+h-1$ and $th=qS+r$ with $0\le r<S$. Among $S$ nonnegative integer occupancies with sum $th$, the smallest possible ordered-overlap count is

$$
\sum_y R(y)(R(y)-1)\ \ge\ S q(q-1)+2qr .
$$

Moving one unit from a larger occupancy to a smaller one reduces the sum whenever they differ by at least two. At the minimum there are $r$ occupancies of size $q+1$ and the rest have size $q$. The earlier difference argument gives the upper bound $h(h-1)-2\sum_{d\in D,d<h}(h-d)$ on the same ordered-overlap count.

For $h=4657$, an extension of size 748 requires at least 12,045,728 ordered overlaps, exceeding the available 12,045,692. Any larger extension would contain one of size 748. This gives the updated bounds of **149 to 747 additions**, inclusive, for this prefix and interval. Run `python3 verify_repacking.py` to check both certificates. To reproduce the construction with GNU C++20, compile `g++ -O3 -std=c++20 repack.cpp -o /tmp/repack39` and run `/tmp/repack39 < data/witness.json`.

### What a fixed prefix can decide

If a solution to problem 39 exists, then every specified finite Sidon prefix can begin a solution. Let the desired prefix be $B\subseteq[1,M]$ and let $A$ be a hypothetical solution on positive integers. Pick an integer $d>2M$ and take $C=B\cup dA$. Its prefix through $M$ is exactly $B$. Sums of two old elements are at most $2M$, and every sum involving a new element is larger. Two new elements sum to zero modulo $d$, while a mixed sum has residue $b\in B$, which identifies its old summand. Uniqueness within $A$ handles sums of two new elements. Finally $C(N)\ge A(\lfloor N/d\rfloor)$, preserving every required exponent because $d$ is fixed. Consequently, failure to extend a particular finite prefix at the *next* checkpoint cannot alone disprove the conjecture. A negative argument must force failures arbitrarily far out in a way incompatible with the asymptotic bounds.

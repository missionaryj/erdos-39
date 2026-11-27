# Cover shared differences by pairs of marks

In the [neighboring-block formulation](neighboring-blocks.md), a single pair of marks from different levels can participate in many conflicts. The following sufficient condition counts the pairs that need to be separated. It can be strictly cheaper than counting all shared differences. The existence of the required infinite system of covers is unproved.

Let $X_j=2^{j^2}$, and let $B_j\subset[0,X_j)$ be Sidon, of size $t_j=X_j^{1/2+o(1)}$ and minimum spacing at least $\lceil\sqrt{X_j}\rceil$. Regard marks from different blocks as distinct vertices, even when their numerical values agree. For each $j$ choose a set $F_j$ of pairs joining a mark of $B_j$ to a mark of an earlier $B_i$ with $j/\sqrt 2<i<j$. Require that for every shared difference between these two levels, at least one of the four cross-pairs between the endpoints of its two occurrences belongs to $F_j$. Suppose
$$
|F_j|\le t_j X_j^{o(1)}.
$$
Then there exist subsets $C_j\subseteq B_j$ of sizes $X_j^{1/2+o(1)}$ for all sufficiently large $j$ with globally distinct positive internal differences. The [block encoding](difference-blocks.md) would give a solution to problem 39.

**Proof.** Put $D_j=\max(1,|F_j|/t_j)$. Independently propose each vertex of level $i$ with probability
$$
p_i=\min\left(1,\min_{i<j<\sqrt 2 i}\frac{1}{j^4 D_j}\right),
$$
using 1 if the index set is empty. The range of later indices is finite, and $\log X_j\le 2\log X_i$ there. Thus $\log(1/p_i)=o(\log X_i)$, uniformly as $i$ grows.

Call a vertex of $B_j$ blocked if it has a proposed earlier neighbour in $F_j$. Each covering edge has its earlier endpoint proposed with probability at most $1/(j^4 D_j)$. By linearity of expectation the expected number of blocked vertices is at most $t_j/j^4$. By Markov's inequality the probability that more than half the block is blocked is at most $2/j^4$. Conditional on all earlier proposals, selection within the unblocked part of $B_j$ remains independent with probability $p_j$. When at least half the block is unblocked, a Chernoff bound shows that the probability of retaining fewer than $p_jt_j/4$ vertices is at most $\exp(-p_jt_j/16)$. These errors are summable. With probability one every sufficiently large level retains at least $p_jt_j/4=X_j^{1/2+o(1)}$ unblocked, proposed vertices.

Keep only those vertices. No covering edge survives at both ends. A repeated difference would have to come from two nearby levels by spacing, and its four endpoints would contain a covering edge, which is impossible. This proves the criterion.

**Why the count can change.** For two labelled copies of the same $t$-mark ruler, all $\binom t2$ differences coincide. Just $t$ cross-pairs cover them: match each mark to its own copy. This example illustrates the distinction between the two counts, without providing the infinite family. More generally, if several repeated differences come from correspondences $c=b+s$ or $c=s-b$, a cross-pair on such a correspondence can cover many of them.

**A finite diagnostic.** In the previous marked rulers with parameters 67 and 257 there are 16,896 mixed pairs and 16,561 distinct mixed sums. Keeping one pair per sum and marking all other pairs gives a cover of size 335. The number of shared positive differences is 339. In this example grouping by equal sum alone yields little saving. The open construction question is whether covers can be chosen with the displayed subpower overhead at every level.

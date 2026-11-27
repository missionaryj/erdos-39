# Repairing cross-block collisions

Research initiated by @missionaryj, with analysis and code assisted by OpenAI Codex. The [interleaved example](interlaced.md) had collisions across colours. Here we remove vertices from individual blocks and check the resulting union as one set.

## A finite witness

Using the same four marked rulers, we retain **2 of 2**, **10 of 10**, **48 of 66**, and **181 of 256** marks. One Sidon set contains all 241 survivors. The check enumerates its 29,161 unordered sums including doubles. The smallest retained fraction is $181/256$, about 70.7%. This is a lower bound from a search: no optimum is asserted.

For two different levels, equal marked sums identify their unordered level pair. After orienting the terms by level, a collision is equivalent to two pairs in the respective levels having the same positive **encoded** difference. For the first two levels choose all marks. On the third level join pairs whose difference occurs in either previous level, then select an independent set. Try seeded samples from this independent set; for each sample, construct the forbidden-edge graph on the fourth level and take a minimum-degree greedy independent set. Score by the smallest retained proportion across the levels. The final pair-sum verification does not use the search's difference test. [Reproducible search and independent check](paired_gaps.py)

## What a count of shared differences can guarantee

Let two individually Sidon blocks have $m,n$ marks with $2\le m\le n$. Suppose $E$ positive differences occur in both. Each common difference pairs one edge (unordered pair of vertices) in the first block with one edge in the second. Distinct common differences use distinct edges on both sides, although the edges can share vertices. We seek subsets retaining no paired edges on both sides.

Choose exactly $r$ of the $m$ vertices uniformly, for $1\le r\le m$. An expected $E r(r-1)/(m(m-1))$ paired edges remain active, so some choice has at most that many. On the other block these active edges form a graph. A random ordering and selection of every vertex preceding all its neighbours gives an independent set of size at least
$$
\frac{n^2}{n+2E r(r-1)/(m(m-1))}
$$
for some ordering, by Cauchy–Schwarz. This preserves the chosen $r$ vertices on the first side and eliminates all cross-difference conflicts. Applied to level-marked blocks it gives a Sidon union of the survivors. For arbitrary unmarked input blocks it guarantees disjoint internal differences; distinct level markers may still be needed to distinguish different types of sums.

In particular one can retain on **both** sides a fraction of order $\min(1,(n/E)^{1/3})$ when $E>0$. To see this take $r=\max(1,\lfloor m\theta\rfloor)$ with $\theta=\min(1,(n/(2E))^{1/3})$. The first fraction is at least $\theta/2$, and the second at least $1/(1+2E\theta^2/n)\ge\theta/2$. For $E=0$ all vertices may be kept. Counting every cross-pair separately and deleting one point per collision can give a much weaker estimate.

## Where a proof from edge pairing alone stops

Consider the abstract model in which every first-block edge is matched injectively to a second-block edge, with no requirement that the edge labels arise from actual integer distances. Suppose $m^2/(n\log n)\to\infty$. There are matchings for which no compatible subsets retain a common fraction greater than a constant times $(n\log n/m^2)^{1/3}$. Combined with the previous estimate at $E=\binom m2$, this fixes the worst-case power for this abstract model.

Indeed, match the $\binom m2$ edges uniformly without replacement into the $\binom n2$ edges. For fixed vertex subsets of sizes $r,s$, the probability they are compatible is at most
$$
\exp\left(-\binom r2\binom s2/\binom n2\right).
$$
This follows by exposing the distinct partners of the first subset's edges one at a time. Put $r=\lceil\alpha m\rceil$, $s=\lceil\alpha n\rceil$, and $\alpha=(C n\log n/m^2)^{1/3}$ with a sufficiently large absolute constant $C$. The log of the number of choices of subsets is $O(\alpha n\log n)$, whereas the negative exponent has magnitude at least a constant times $\alpha^4m^2=C\alpha n\log n$. A union bound gives a matching with no compatible pair of subsets of those sizes. Larger subsets would contain a pair of those sizes.

This obstruction concerns arbitrary edge matchings. Integer differences satisfy additional identities, including $(z-x)=(z-y)+(y-x)$ for ordered triples of marks. A random matching need not preserve any such identity. The open step for #39 is to exploit realizable arithmetic structure or design special blocks, with enough retention simultaneously throughout an unbounded sequence of scales. The four-block computation proves neither outcome.

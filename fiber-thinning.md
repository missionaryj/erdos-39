# A sharp two-scale exponent for random thinning of two quadratic blocks

Research initiated by **@missionaryj**, with mathematical analysis and computation assisted by OpenAI Codex.

For the [degree-two and degree-three blocks](field-bridge.md), keep each earlier mark independently with probability $\delta=p^{-\lambda}$ and then choose the later subset optimally. In this model the best common exponent at the two integer horizons is **$3/7$** with probability tending to one for each fixed choice of $\lambda\ge0$. The later subset may depend on the entire earlier sample. The upper bound allows ordinary integer differences to differ even where their modular images agree. Exceptionally coordinated choices of both subsets remain outside this result.

Let $p$ range over odd primes. Take $L=\mathbb F_p(\xi)$, $\xi^2=D$ a nonsquare in the base field, and $K=\mathbb F_p(\theta)$ of degree three with monic irreducible polynomial $P(X)=X^3+AX^2+BX+C$. The small and large graphs are $(x,x^2)$ over the respective fields. Embed each small coordinate via $U(r+s\xi)=r+s\theta$. Use their common four components as the lowest integer digits and the two remaining large components as the highest digits, all in radix $2p$. Multiply the encodings by four and add one on the small block or two on the large one. Equal sums then identify their level pair. Internally both blocks are Sidon. A choice of subsets is therefore Sidon exactly when their positive internal integer differences are disjoint.

The horizons may be taken as $4(2p)^4$ and $4(2p)^6$. At most $p$ large-block points enter the early horizon, since vanishing high digits force $x=u+t\theta$ and then $t^2=0$.

## The tradeoff

Let $N$ be the maximum number of later marks compatible with the earlier sample. If $p^2\delta\to\infty$, with probability tending to one,
$$
 N\gg\min(p^3,p^2\delta^{-2}).
$$
For every $\delta>0$, with probability tending to one,
$$
 N\ll\min\{p^3,\ p^2(\sqrt p(\log p)^2+\delta^{-2}\log p)\}.
$$
If disjointness is required already for modular differences, the $\sqrt p(\log p)^2$ term can be dropped.

For the lower bound, fix $k$ earlier marks. Each of their unordered pairs forbids at most one unordered pair on the later block, even when ruling out modular conflicts: every nonzero oriented difference of the large parabola occurs at most once. A graph on $p^3$ vertices with at most $\binom k2$ edges has an independent set of size at least $p^6/(p^3+k^2)$, by the random-order independent-set bound. A binomial sample has $k\asymp p^2\delta$ with high probability under the stated assumption.

In particular for $1/4\le\lambda\le1/2$ the upper and lower powers agree, giving $N=p^{2+2\lambda+o(1)}$. The early exponent is $(2-\lambda)/4$, and the later exponent is $(2+2\lambda)/6$ in this range. They agree at $\lambda=2/7$ and give $3/7$. For $\lambda<1/4$ the later exponent is at most $5/12+o(1)$; for $\lambda>1/2$ the early exponent is at most $3/8+o(1)$ with high probability (by binomial concentration or Markov's inequality). In particular the construction at $\lambda=2/7$ gives actual integer Sidon witnesses with that common exponent. This is a statement about two specified horizons.

## How often one early endpoint can appear in a later fiber

A later fiber fixes the high components $e=[x]_2$ and $f=[x^2]_2$, where the subscript denotes the coefficient of $\theta^2$. For $e=0$ there are just $p^2$ marks in total. For $e\ne0$ the fiber is parametrized by $t\in\mathbb F_p$:
$$
 x=u(t)+t\theta+e\theta^2,\qquad
 u(t)=(f-t^2-2ket-le^2)/(2e),\quad k=[\theta^3]_2,\quad l=[\theta^4]_2 .
$$
Each pair $t\ne t'$ has a modular difference in the small coordinate space, with nonzero horizontal part. It therefore matches exactly one oriented early chord. **In a fixed such fiber, a given early point starts at most six of these oriented chords.**

Here are the formulas. Set $h=(t'-t)/2$, $y=(t+t')/2$, $\rho=-y/e-k$. The horizontal gap is $2h(\theta+\rho)$. Write the early midpoint as $a_0+a_1\xi$. Using $U(\xi)^2-U(\xi^2)=\theta^2-D$ to compare the two secant equations gives the later midpoint as
$$
 a_0+a_1 F(\rho),\qquad F(\rho)=\frac{\rho\theta+D}{\theta+\rho}.
$$
Indeed multiplying this expression by $2h(\theta+\rho)$ gives $U(2h(a_0+a_1\xi)(\xi+\rho))$. Polynomial division in $P$ gives $[F]_2=(\rho^2-D)/P(-\rho)$ and $[F]_0=\rho+[F]_2(B-A\rho+\rho^2)$. Thus the start $Z=z_0+z_1\xi$ of the early chord satisfies
$$
 a_1=\frac{eP(-\rho)}{\rho^2-D},\qquad z_1=a_1-h,\qquad
 z_0=\bar u-e(B-A\rho+\rho^2)-\rho(a_1+h),
$$
where $\bar u=(f-y^2-h^2-2key-le^2)/(2e)$.

Fix $z_0,z_1$. Substitute $h=a_1-z_1$ and $y=-e(\rho+k)$ into the last equation. Multiplication by $(\rho^2-D)^2$ gives a polynomial of degree at most six. It is nonzero: $a_1$ has a simple pole at $\rho=\xi$ because $P(-\xi)\ne0$, and the term $-h^2/(2e)$ has a double pole there while every other term has at most a simple pole. Each possible $\rho$ gives at most one ordered $(t,t')$. This proves the assertion.

## Modular and ordinary conflicts

In any $t_0$-element subset of a regular fiber, the $\binom{t_0}{2}$ pairs correspond to edges on early endpoints. Their multigraph has maximum degree six by the chord bound, so greedy selection gives a matching of size $\gg t_0^2$ for $t_0\ge2$. Matched edges have independent survival events, each of probability $\delta^2$. The chance that none survives is at most $\exp(-c\delta^2t_0^2)$.

For the ordinary lift the same matching bound holds for $t_0\ge C\sqrt p(\log p)^2$, counting only pairs that match as ordinary gaps. We give the carry argument because it is essential for the integer upper bound. For $T\subset\mathbb F_p$ of size $s$, the formula for $Z(t,t')$ above, extended also to the diagonal, satisfies the following estimate for any nonzero base-field linear frequency of $(Z,Z^2)$. Its normalized character sum over $T^2$ is bounded in magnitude by
$$
 O\left(\frac{\sqrt p}{s}+\frac{p^{1/4}}{\sqrt s}\right).
$$
Indeed for fixed $t$ and variable $t'$ the two conjugate expressions for $Z$ are
$$
 \bar u-e(B-A\rho+\rho^2)-h(\rho\mathbin{\pm}\xi)
       +a_1(\mathbin{\pm}\xi-\rho).
$$
The last term has a single nonzero simple pole at $\rho=\mp\xi$. These conjugate pole locations, viewed in the $t'$ variable, are disjoint from those for any different fixed $t$: their base-field translates can coincide only for identical translates, since their difference is a nonzero multiple of $e\xi$ outside the base field. Every frequency is $\operatorname{Tr}_{L/\mathbb F_p}(aZ+bZ^2)$, $(a,b)\ne(0,0)$. Its pole orders are two if $b\ne0$ and one otherwise. Subtracting the phases for two distinct fixed parameters leaves these poles uncancelled. The degrees are absolutely bounded, and the simple or double poles preclude an Artin–Schreier difference for odd $p$. The standard Weil bound for complete rational additive character sums therefore gives $O(\sqrt p)$ for this phase difference. There are no poles at base-field inputs. Cauchy–Schwarz over $t'$ and completion to $\mathbb F_p$ give the stated estimate (the $s$ diagonal terms cost $p$ each).

Partition the four low digits of the later points into a fixed grid of boxes of side at most $p/64$. A largest box from the chosen $t_0$ marks contains $s\gg t_0$ of them. For each of the four old starting digits, the fraction within $p/32$ of either end of its digit range is at most $1/16+O(1/p)$ plus $O(\log p)$ times the character estimate, by interval Fourier expansion. With the constant $C$ sufficiently large the union of these four boundary events covers less than half of $T^2$. Excluding the diagonal still leaves $\gg t_0^2$ pairs. For those pairs, the small signed differences of the four later low digits can be added to the old starting digits without wrap. The two modularly matched chords then have identical ordinary digit differences and hence equal integer gaps. The same degree-six matching extraction applies.

Finally union-bound over at most $p^2\binom{p}{t_0}$ candidate subsets of that size. Taking $t_0\ge C'\delta^{-2}\log p$ makes the failure probability tend to zero, additionally imposing the carry threshold for integers. Larger compatible subsets would contain one of size $t_0$. Summing over fibers and including the exceptional $p^2$ vertices proves the upper bounds. If the threshold exceeds $p$ the trivial ceiling suffices.

## Exact checks

The verifier compares the reconstructed start with direct field subtraction for every regular-fiber pair in four small cases. It also computes exact independent sets one fiber at a time. At $p=3$, optimizing both the earlier subset and the modularly compatible later subset gives later maxima $27,27,26,25,24,23,22,17,15,8$ for earlier counts zero through nine. With a seeded sample of 60 earlier marks at $p=11$, the conditional modular optimum is 712 later marks. Their integer union has 298,378 distinct unordered sums. The exhaustive claims concern the stated finite models. [Verifier](fiber_thinning.py)

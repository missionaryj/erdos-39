# Covering the gaps with several Sidon sets

Research initiated by @missionaryj, with analysis and code assisted by OpenAI Codex. We ask what happens to the finite-block construction if different colours need only satisfy the Sidon condition separately. No optimality across all such constructions is claimed.

**Claim.** For each fixed integer $k\ge1$ there exist $k$ pairwise disjoint infinite Sidon sets whose union $U$ satisfies
$$
\liminf_{N\to\infty}\frac{\log U(N)}{\log N}
=\frac1{1+2^{1/k}}.
$$
In this construction each individual colour has lower counting exponent exactly $1/3$. The union can approach exponent $1/2$ by choosing a large fixed $k$. This is a relaxation of #39, which requires a single Sidon set.

## The rulers and their scales

Set $\rho=2^{1/k}$ and $Z_j=\exp(\rho^j)$ for positive indices $j$. For all sufficiently large $j$ take a prime $p_j$ between $Z_j/16$ and $Z_j/8$ (Bertrand's postulate, or take the first prime above the lower endpoint and allow integer rounding). Then $\log p_{j+1}/\log p_j\to\rho$, the primes are eventually strictly increasing, and $p_{j+k}>2p_j^2$ for all sufficiently large $j$ since $Z_{j+k}=Z_j^2$. Discard an initial segment so these facts always hold.

At index $j$ use the positive payloads
$$
T_j=\{2p_j i+(i^2\bmod p_j):1\le i<p_j\}.
$$
These form a Sidon ruler. Indeed a pair sum gives the index sum and, modulo $p_j$, the sum of the two squared indices. Those determine the index product modulo the odd prime and hence the unordered pair of indices. All positive differences of $T_j$ are larger than $p_j$ and smaller than $2p_j^2$. Assign colour $j\bmod k$ to this ruler. The difference ranges of rulers of one colour are disjoint by construction.

## Keeping the early marks visible

For a payload $x$ from level $j$, split its binary digits from the least significant end into chunks of widths $1,3,5,\ldots$. After each chunk insert one zero guard bit followed by a two-bit field. Put a single $1$ in that field at chunk $j$ and leave all other fields zero. Continue until both the payload and its marker have been encoded. In particular the payload may extend beyond its marker. Write $F(j,x)$ for the resulting integer.

A sum of two encodings decodes the unordered pair of levels and the original sum of payloads. For two distinct levels of the same colour, a second representation would give a common positive difference in their rulers. For a single level, uniqueness holds within the ruler itself. Each colour is therefore Sidon, and the marker also makes the colours disjoint. [Detailed decoding argument](difference-blocks.md#sufficiency)

Along the payloads $x\in T_j$ we have $x>p_j$ and $j=O_k(\log\log x)$. For large $j$ the marker therefore lies within the original payload's chunk count. With $b$ payload bits there are at most $\lceil\sqrt b\rceil$ chunks, and padding the last chunk to its full width costs at most $2\lceil\sqrt b\rceil$ further bits. Thus $x\le F(j,x)\le x^{1+o(1)}$ uniformly on all large payloads. Counting labelled payloads before encoding preserves the lower counting exponent: for every $\delta>0$ and all large $N$, all sufficiently large payloads through $N^{1/(1+\delta)}$ are encoded by $N$, while any encoding through $N$ has payload at most $N$.

## Counts in the gaps

Let $P(x)$ count labelled payloads through $x$, and take $p_j^2\le x<p_{j+1}^2$. The $j$-th ruler contributes at least a constant times $p_j$ marks because its $i$-th mark lies between $2p_ji$ and $2p_ji+p_j$. The next ruler similarly contributes at least a constant times $x/p_{j+1}$ when this quotient is at least 4. Smaller quotients are covered by the first lower bound. Hence
$$
P(x)\gg\max(p_j,x/p_{j+1}).
$$
The log-count divided by $\log x$ for this lower envelope is smallest at $x=p_jp_{j+1}$: the first term gives a decreasing ratio up to the crossing and the second an increasing ratio afterwards. Its value there tends to $1/(1+\rho)$.

At the crossing the total count from rulers through $j$ is at most $jp_j$. Every later active ruler contributes at most $x/(2p_{j+1})$, and there are only $O_k(\log\log x)$ active levels since the first mark exceeds $p_i$ at each level $i$. This gives the matching upper exponent. For an individual colour the same argument uses consecutive primes $p_j,p_{j+k}$ within that colour. The log ratio tends to 2, giving exponent $1/3$. Thus choosing a colour by the pigeonhole principle at each $N$ would switch colours as $N$ changes.

## Exact collision check

A two-colour finite example uses prime parameters $3,11,67,257$ in order. They obey the necessary same-colour separation. The script checks **every** unordered pair sum within each colour. It finds colour sizes 68 and 266, and two distinct representations of 606577 across colours. The conflicting pairs, in (prime,index) notation, are $((11,7),(67,8))$ and $((11,3),(67,9))$. The early marker resolves level identity, but both representations have exactly the same two levels. An additional rule preventing such coincidences while retaining density would be needed to obtain one Sidon set. [Verifier](interlaced.py)

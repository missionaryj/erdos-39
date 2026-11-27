# Combining finite Sidon blocks with separate differences

Research initiated by @missionaryj, with mathematical exploration and verification assisted by OpenAI Codex. The following criterion removes any need to nest the individual finite sets or to check sums involving four different blocks. Existence of blocks of the required sizes is open.

## Criterion

Put $X_j=2^{j^2}$ for integers $j\ge1$. Erdős #39 has an affirmative answer if and only if there exist finite sets $B_j\subseteq[0,X_j)$ with both properties:

1. $|B_j|\ge 2^{j^2/2-o(j^2)}$ as $j\to\infty$.
2. Each positive integer occurs at most once in the list of differences $b-a$ formed **within** a block, over all $j$ and all $a<b$ in $B_j$.

The blocks may be translated within their size limit and may contain common elements. Differences between a point of one block and a point of another are unrestricted.

### Necessity

Suppose $A=\{a_1<a_2<\cdots\}$ is a solution. Take the elements below $X_j$ whose index is $2^{j-1}$ times an odd number as $B_j$. Different blocks then receive disjoint sets of indices. Any repeated within-block difference, even between two different blocks, would repeat a difference of $A$. Among the first $t$ indices the specified class occurs $t/2^j+O(1)$ times. Here $t=A(X_j-1)\ge 2^{j^2/2-o(j^2)}$, so the cost of the partition preserves the required exponent.

### Sufficiency

Write a payload $x\in B_j$ in binary, least significant end first, in chunks of lengths $1,3,5,\ldots,2j-1$. These lengths sum to $j^2$. Encode each chunk in a field containing its payload, a zero guard bit, and a two-bit marker. In the marker write $1$ in chunk $j$ and zero in all other chunks. Missing high fields are zero. The encoded positive integer is less than $Y_j=2^{j^2+3j}$.

Adding two encoded integers produces no carry from any payload into a marker or from any marker into the next field. A sum therefore records the unordered pair of block indices, allowing a repeated index. It also records the sums of the two payloads in each chunk. Recombining these chunk sums with their original binary weights recovers the ordinary sum of the two original payloads.

For equal encoded sums from a single block, condition 2 gives the usual Sidon property of that block. For equal sums from two different blocks $i,j$, order the terms by their markers and write the resulting equality as $x+y=x'+y'$. If $x\ne x'$, the same positive difference $|x-x'|=|y-y'|$ occurs within both blocks, contradicting condition 2. Otherwise both pairs agree. Thus the entire encoded set is Sidon. Its count through $Y_j$ is at least $|B_j|$. Since $\log Y_{j+1}/\log Y_j\to1$, monotonicity supplies the desired exponent between these checkpoints as well.

An equivalent finite task is to find one sequence of size requirements $m_j\ge2^{j^2/2-o(j^2)}$ such that for each $k$ there exists a compatible family of blocks $1$ through $k$ meeting those requirements. Each position has only finitely many possible blocks. Successively stabilizing the first, second, and subsequent blocks on infinite subsequences gives a compatible infinite family. A fixed repeated difference would already appear in a finite subfamily.

## A construction at separated scales

A dense finite block can avoid *every* difference of all earlier blocks when its prime parameter exceeds their maximum diameter. For an odd prime $p$ take

$$
T_p=\{2pi+(i^2\bmod p):0\le i<p\}.
$$

The digit argument in [the residue construction](residue-lifts.md) proves it is Sidon. Its diameter is below $2p^2$ and consecutive elements are separated by at least $p+1$. Hence adjoining $T_p$ to a difference family of maximum diameter at most $p$ preserves condition 2. This attains square-root order at the new endpoint. Repeating this rule is possible at scales roughly the square of the preceding scale; it does not supply the required sizes at the intervening checkpoints. Treating all smaller differences as forbidden discards information about which ones have actually been used.

## An obstruction to allocating differences by their powers of two

Suppose that for each block we reserve a set $S_j$ of values of the exponent of two dividing a nonzero difference, and that the $S_j$ are pairwise disjoint. In the binary expansions of $x,y$, the least position where the two differ gives precisely this exponent. Thus projection onto the bit positions in $S_j\cap[0,j^2)$ is injective on $B_j$, and $\log_2 |B_j|\le |S_j\cap[0,j^2)|$. For $J/2\le j\le J$, the sum of these upper bounds is at most $J^2$ by disjointness. The required sizes would instead give a sum of order $J^3$. Allocating only this exponent cannot produce the desired blocks. The odd parts of differences are left unrestricted by this obstruction.

The verifier enumerates all compatible triples of small blocks in its stated test family and checks all encoded unordered sums, including doubles. [Run the verifier](difference_blocks.py)

### Even two polynomially related scales cannot reserve separate powers of two

Let $B,C$ be Sidon blocks of sizes $b,c$ in intervals of lengths $M,N$, respectively, where $M\le N$. Suppose no positive difference within $B$ has the same 2-adic valuation (exponent of two in its factorization) as a positive difference within $C$. For a power of two $q$, let $r_B,r_C$ count the occupied residue classes modulo $q$. Then $r_B r_C\le q$. Indeed, two different representations of a residue as a sum of one occupied residue from each block would give differences from the two blocks equal modulo $q$ up to sign and nonzero modulo $q$. They would have the same valuation below $\log_2 q$.

Counting pairs within a residue class of $B$ gives $r_B\ge b^2/(b+2\lfloor(M-1)/q\rfloor)$: each pair consumes a distinct positive multiple of $q$, and Cauchy–Schwarz bounds the sum of squared class sizes from below. The analogous bound holds for $C$. Take $q$ between $\sqrt M$ and $2\sqrt M$. If $b=M^{1/2+o(1)}$, then $r_B\ge M^{1/2-o(1)}$, whence $r_C\le M^{o(1)}$. Substitution into the bound for $C$ yields $c=O(r_C+\sqrt{r_C N/q})$. In particular, if $M=N^{r+o(1)}$ for fixed $0<r\le1$, then $c\le N^{1/2-r/4+o(1)}$. Thus a power loss already occurs with two blocks under this particular reservation rule. The actual difference-block criterion permits equal valuations whenever the integer differences themselves differ.

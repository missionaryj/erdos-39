# Extending a Sidon prefix with two finite rulers

Research initiated by **@missionaryj**, with mathematical analysis and computation assisted by OpenAI Codex.

A product of two finite Sidon rulers admits an exact extension calculation when the first row has already been partly filled. A point-line incidence construction attains the resulting bound up to absolute constants and preserves the specified prefix. This gives explicit Sidon sets at two different horizons. The count at the later horizon also measures the loss from encoding the two coordinates separately.

Let $U$ be a nonempty finite Sidon set of nonnegative integers with $p$ elements. Take a second Sidon set $V=\{0=v_0<v_1<\cdots<v_h\}$ and an integer $K>2\max U$. Use candidate marks
$$
1+u+K v_j,\qquad u\in U,\quad 0\le j\le h.
$$
The given prefix consists of $m$ specified marks in row zero. No more marks may be added to that row. Write $s=p-m$. For $m\ge h\ge1$ the **exact maximum number of additions** to the later rows is
$$
h+z(s,h),
$$
where $z(s,h)$ is the largest number of edges in a bipartite graph on $s$ and $h$ vertices with no four-cycle. Put $z(0,h)=0$.

## Proof

Associate each chosen mark with the edge $(u,j)$. Reducing a sum (after subtracting the two constant shifts) modulo $K$ recovers the low sum. Sidonicity of $U$ recovers its unordered pair of low labels, and Sidonicity of $V$ then recovers its unordered pair of row labels. If a label is repeated in either coordinate there is only one matching. Otherwise the only two possible matchings between the coordinate pairs would form the four edges of a rectangle. Conversely such a rectangle gives equal integer sums. Hence the integer set is Sidon exactly when the graph has no four-cycle.

Each later row can contain at most one of the $m$ old labels, since two would make a rectangle with row zero. The later edges on the remaining $s$ labels contribute at most $z(s,h)$. To attain the bound, take a maximizing graph on those $s$ labels and give each later row its own distinct old label. No two later rows acquire a shared old label. Each meets row zero in exactly one label. The resulting integer set retains the original prefix and attains the formula.

For $s,h\ge1$, write $a=\min(s,h)$ and $b=\max(s,h)$. The classical elementary estimates give $z(s,h)=\Theta(b+a\sqrt b)$. Indeed a pair of vertices on the smaller side has at most one common neighbor. Cauchy–Schwarz on the degrees of the larger side gives $z^2/b-z\le a(a-1)$. A star gives $b$ edges. For the other lower bound take a prime $l$ of order $\sqrt b$ with $l^2\le b$, and use points and nonvertical affine lines over $\mathbb F_l$. There are $l^2$ vertices on each side, all of degree $l$. Use the whole available larger side of the plane and keep $\min(a,l^2)$ vertices on its other side. Distinct lines meet in at most one point. This yields order $a\sqrt b$ edges, and isolated vertices fill out the requested part sizes. Small bounded values of $b$ are absorbed in the constants.

## What this gives at polynomially separated horizons

For odd primes $p,q$ take $U=\{2pi+[i^2]_p:0\le i<p\}$, use the corresponding $q$-ruler for $V$, and put $K=4p^2$. Each ruler is Sidon since the digit sums recover the sum of the indices and the sum of their squares modulo the prime, and these determine the unordered pair. The first horizon is $K$ and the whole set lies below a constant times $p^2q^2$.

Suppose $q=p^{\theta+o(1)}$ for fixed $0<\theta<1$, and keep $m=\lfloor p/2\rfloor$ first-row marks. Here $h=q-1\le m$ eventually. The best possible final count in this host has order $p+q\sqrt p$. In terms of the later horizon its exponent is
$$
\frac{\max(1,\theta+1/2)}{2+2\theta}.
$$
The small prefix has square-root order. The later exponent falls strictly below $1/2$ for every fixed $\theta$ in this range. Filling more of row zero consumes available low labels. In particular, a full first row permits just $h$ additions. These ceilings concern this product host and leave open constructions whose high and low coordinates interact.

## Checks

With $p=7$, $q=5$, and four specified first-row marks, exhaustive enumeration shows that at most 11 marks can be added simultaneously. An explicit choice has 15 marks with all 120 unordered sums distinct. With $p=101$ and $q=43$, use 42 affine lines on 49 points over $\mathbb F_7$ and a private old label for each line. This retains all 52 prescribed first-row marks and adds eight in each successive row, giving simultaneous counts $52+8j$ after rows $1$ through $j$ for every $0\le j\le42$. All 75,466 unordered sums in this 388-mark construction are distinct. [Exact verifier](incidence_extension.py)

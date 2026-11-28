# How many later marks does an earlier parabola cost?

Research initiated by **@missionaryj**, with mathematical analysis and computation assisted by OpenAI Codex.

In the degree-two and degree-three parabola construction, a coordinated choice of $k\le 2p$ earlier parameters costs at most $k-1$ of the $p^3$ later marks. A uniform random choice of the same size costs asymptotically $(16/81)\binom{k}{2}$ later marks in the integer lift when $k\to\infty$. In fact the random formula holds throughout $1\ll k\ll p^{3/2}$, where both inequalities mean that the corresponding ratios tend to zero. The coefficient comes from the exact limiting probability that four modular digit differences agree as ordinary signed differences.

We use the [two parabola blocks and lift](fiber-thinning.md). Let $p$ be an odd prime, $L=\mathbb F_p(\xi)$ with $\xi^2=D$ a nonsquare, $K=\mathbb F_p(\theta)$ of degree three, and $U(r+s\xi)=r+s\theta$. Each parameter gives the point $(a,a^2)$ in its field. The integer encoding uses radix $2p$, placing the two low horizontal digits and the two low vertical digits first, then the two remaining digits for the larger field. A factor of four and level markers $1,2$ separate the sum types. Within each block the marks are Sidon. Between blocks, one must eliminate all common positive ordinary differences. One can also impose the stronger modular difference condition in $K^2$ using $U$ on both early coordinates.

## Exact repair on two parallel lines

Fix $z\in\mathbb F_p^\times$ and take any nonempty set $A$ of $k$ earlier parameters $r+s\xi$ with $s\in\{z,-z\}$. Put $g=\theta^2-D$. The identity
$$
 U(a)^2-U(a^2)=g s^2
$$
makes the $k$ later graph points with parameters $U(A)$ a single translate of the embedded earlier points. A nonzero horizontal gap $d$ and its vertical gap $v$ identify the unique start of a parabola chord as $(v/d-d)/2$. Hence all modular conflicts form exactly a clique on $U(A)$. Precisely $k-1$ deletions are necessary and sufficient.

In the integer lift, write $w_a$ for the later encoding at $U(a)$ minus the earlier encoding at $a$, before marking the levels. The two horizontal low digits agree. The vertical linear digit is $2rs$ in both graphs, and the later high vertical digit is always the representative of $z^2$. Only the constant vertical digit can wrap in the translation from $r^2+Dz^2$ to $r^2$ modulo $p$. Thus the number $H$ of distinct values of $w_a$ is one or two. A modularly matched pair agrees as an ordinary difference exactly when its two offsets are equal. Reversing only the later pair cannot give equality either, since its nonzero modular horizontal gap would then equal its own negative. The conflict graph is the disjoint union of the cliques indexed by the offsets. The exact minimum deletion count is **$k-H$**.

## Counting ordinary conflicts in the full graphs

For all choices of the two defining fields and bases as above, the fraction of the $\binom{p^2}{2}$ earlier pairs whose unique matched later pair has the same ordinary gap tends to **$16/81$** as $p\to\infty$.

To see this, parameterize an ordered earlier pair by its start $a=r+s\xi$ and its increment $2h(\rho+\xi)$, with $r,s,\rho\in\mathbb F_p$ and $h\ne0$. The omitted horizontal increments in $\mathbb F_p^\times$ are a fraction $1/(p+1)$ of all nonzero increments. Put $m=s+h$ and $J=-g/(\theta+\rho)$. The unique matched later chord starts at
$$
 X=U(a)+mJ
$$
and has increment $2h(\rho+\theta)$. Indeed the discrepancy between squaring in the two fields is $g s^2$ at the start and $g(s+2h)^2$ at the end, and the correction $2mJ\cdot2h(\rho+\theta)$ cancels their difference.

Let $O$ be the four low digits of the earlier start, $V$ the four low digits of its increment **on the graph**, and $W$ the low digits of the later graph start minus $O$, all taken in $\mathbb F_p$. For a uniform ordered pair, the twelve coordinates of $(O,V,W)$, represented in $[0,p)$ and divided by $p$, become equidistributed in the twelve-dimensional unit cube. Here are details giving uniformity in the defining polynomials.

For a frequency of the twelve coordinates, write $a',b',c'$ for the three horizontal coefficient pairs and $A,B,C$ for their three vertical counterparts, indexed by $0,1$. With $\rho$ fixed the phase is a polynomial of degree at most two in $r,s,h$. Write $j=([J]_0,[J]_1)$ for the low coefficients of $J$. The coefficient of $r^2$ is $A_0$. The terms bilinear in $r$ and $(s,h)$ are
$$
 2r\{A_1s+2h(B_0\rho+B_1)+(s+h)C\cdot j\}.
$$
Indeed the old square has low coordinates $(r^2+Ds^2,2rs)$, the change in the square contains the term $4rh(\rho+\xi)$, and the difference between squares at the two starts contains the term $2r(s+h)J$.

The functions $1,j_0,j_1$ are linearly independent over $\mathbb F_p$. Both $j_i$ vanish at infinity. Any linear form on the low coordinates vanishing on $J$ must, by expansion in $1/\rho$, vanish on $g,g\theta,g\theta^2$. These form a basis of $K$. Consequently, identically zero coefficients of $r^2,rs,rh$ force $A=B=C=0$. With the vertical frequencies zero, the remaining linear coefficients in $r,s,h$ are
$$
 a'_0,\qquad a'_1+c'\cdot j,\qquad 2(b'_0\rho+b'_1)+c'\cdot j.
$$
Their identical vanishing forces $a'=b'=c'=0$ by the same independence.

For any nonzero frequency, at least one of the displayed coefficients is a nonzero rational function of $\rho$ of absolutely bounded degree. This degree bound follows by writing $(\theta+\rho)^{-1}$ with denominator its cubic norm and numerator of degree at most two. Only $O(1)$ values of $\rho$ can therefore give a constant phase. For the others a normalized complete additive character sum over $r,s,h$ has magnitude at most $p^{-1/2}$, by diagonalizing the quadratic part and applying the one-variable Gauss sum bound, or by linear orthogonality if the quadratic part vanishes. Removing $h=0$ and restoring the omitted pairs costs $O(1/p)$. This proves a uniform $O(p^{-1/2})$ bound on the nonzero Fourier coefficients of the distribution. In particular every fixed nonzero integral frequency tends to zero, giving the claimed equidistribution by the Weyl criterion.

In each digit the two starting residues are $o$ and $o+w$ modulo $p$, and the common increment is $v$. All three are asymptotically independent and uniform after this invertible change of torus coordinates. Conditional on limiting increment $t\in[0,1)$, the two ordinary signed differences agree exactly when both increments wrap or neither wraps, of limiting probability $t^2+(1-t)^2$. The boundary of this test has measure zero. All four digit tests must pass, because equal integer differences force equal signed differences in every digit: the difference of two signed digits has magnitude at most $2p-2$, strictly less than the radix. The two high digits are fixed along each matched chord. Integrating across all four digits gives $(\int_0^1(t^2+(1-t)^2)\,dt)^4=(2/3)^4$. Passing to unordered positive differences preserves the fraction.

## The same earlier set can cost linearly as integers and quadratically modulo the field

There is a choice of cubic for which **all $p^2$ cross-line modular conflicts disappear in the integer lift**. Take the earlier parameters on $s=0,-1$. Fix any $C\ne0$ and choose the cubic $P(T)=T^3+AT^2-DT+C$ irreducible. Such an $A$ exists for every odd $p$: each nonzero candidate root excludes just one $A$, and zero is never a root.

For the general cubic $T^3+AT^2+BT+C$, write $J=j_0+j_1\theta+j_2\theta^2$ as in the chord calculation. Multiplication by $\theta+\rho$ gives
$$
 j_1=\frac{(B+D)\rho-C-DA}{P(-\rho)},\qquad
 j_2=\frac{\rho^2-D}{P(-\rho)}.
$$
With $B=-D$, $j_1$ never vanishes. Indeed $C=-DA$ would factor $P(T)=(T+A)(T^2-D)$. Orient a cross-line old chord from $s=0$ to $s=-1$. Its ordinary horizontal linear digit increases by $p-1$. For its later chord to match this signed difference, the later starting digit must be zero. That digit is $s+mj_1=-j_1/2\ne0$. This excludes every cross-line ordinary conflict. Within each line the offset-clique calculation above applies; the two projected vertex sets are disjoint. The total optimum ordinary deletion count is exactly $2p-1-H_{-1}$, where $H_{-1}\in\{1,2\}$ counts offsets on the second line.

For comparison, the optimum modular deletion count is $p^2+O(p)$. To prove this, project each later vertex to its linear and quadratic horizontal digits $(t,e)$. For every slope $\rho$, the $p$ choices of the old real starting digit give a perfect matching from the class $(t,e)=m(j_1,j_2)$ to $(t-1,e)$, where $m=-1/2$. All start classes are distinct. In fact, if $J(\rho)-J(\rho')$ were a base-field scalar for distinct slopes, then $(\theta+\rho)(\theta+\rho')$ would be proportional to $g$. Comparing the three coefficients forces $\rho'=-\rho$ and $\rho^2=D$, impossible. All end classes are likewise distinct. Thus every vertex has cross-line degree at most two, giving the elementary lower bound $p^2/2$ even without any curve estimate.

For the sharper count assume $p>3$. Over the algebraic closure, the start classes belong to the irreducible plane curve parametrized by $m(j_1,j_2)$. Its degree is at most three: a generic line cuts its parametrization in the roots of a polynomial of degree at most three after clearing $P(-\rho)$. Its $e$ coordinate is nonconstant. The horizontal translate by $(-1,0)$ is a distinct curve, since translation invariance would put $p$ distinct points on a horizontal line through any affine point, exceeding its degree. By Bézout the two curves share at most nine points. Hence only $9p$ later vertices can cover two cross-line edges in a single deletion. At least $p^2-9p$ deletions are required for those edges alone. One deletion per cross-line edge and at most $2p-2$ for the within-line edges always suffice. In fact the cross-line edges all have $e=mj_2\ne0$, disjoint from the two within-line cliques at $e=0$.

## Sparse random repair

Choose $A$ uniformly among all $k$-subsets of the $p^2$ earlier parameters, with $k\to\infty$ and $k=o(p^{3/2})$. With probability tending to one, the minimum modular deletion count is $(1+o(1))\binom{k}{2}$ and the minimum ordinary deletion count is $(16/81+o(1))\binom{k}{2}$.

Label every later conflict edge by its unique unordered pair of early parameters. All labels are distinct and each possible early pair occurs. Exactly $\binom{k}{2}$ modular edges survive selection. The ordinary edge count has expectation $(16/81+o(1))\binom{k}{2}$ by the preceding result. Its variance is $O(k^2+k^3)$: disjoint labels are negatively correlated under uniform sampling, and the $O(p^6)$ pairs of labels sharing one parameter survive jointly with probability at most $(k/p^2)^3$. This gives concentration on the $k^2$ scale.

It remains to show that almost all the selected edges require separate deletions. Put $q=k/p^2$. Group later points by their two high digits $(e,f)$. There are $p^2$ vertices with $e=0$, each in a fiber of size at most $2p$, since $f$ is then the square of the horizontal linear digit. Only $O(p^3 q^2)$ edges survive there in expectation. Each remaining vertex is incident to at most $p-1$ modular edges, all within a single regular fiber. Among any of these edges, each old parameter occurs in at most six labels by the [regular-fiber chord bound](fiber-thinning.md#how-often-one-early-endpoint-can-appear-in-a-later-fiber). Thus at a given later vertex there are $O(p)$ pairs of incident edges with overlapping labels and $O(p^2)$ with disjoint labels. The expected total number of selected incident edge pairs over all regular vertices is at most
$$
 O(p^4 q^3+p^5 q^4)=O(k^3/p^2+k^4/p^3).
$$
These contributions, together with the exceptional edges, are $o(k^2)$. By Markov's inequality, with high probability the number of surviving edges that are exceptional or touch another surviving edge is $o(k^2)$. Each isolated edge requires a separate deletion. Deleting one endpoint per edge always suffices. The same argument applies to the ordinary conflict subgraph.

## Finite checks and scope

At $p=17$, all 34 earlier parameters on $s=\pm1$ cost exactly 33 later marks modulo the field and 32 in the integer lift. A fixed random sample of 34 costs 431 and 103 respectively. For the opposite-digit example at the same prime, the identical 34 earlier marks cost 321 modular deletions and 31 ordinary deletions; none of their 289 cross-line pairs match as integers. At $p=100003$, direct reconstruction and squaring of 30,000 seeded nonhorizontal chords found 5,929 ordinary matches (19.76%, versus a limiting 19.75%). The verifier computes both optima by independent-set search for every prefix of a shuffled pair of lines at five primes and directly checks integer gap disjointness for the final coordinated choice. [Verifier](coordinated_repair.py)

The early horizon is of order $p^4$. The coordinated examples here retain at most $2p$ prescribed early parameters, while H1 calls for counts of order $p^{2-o(1)}$ at such a horizon and compatible counts across successive horizons. The sparse random formula also leaves open what coordinated choices can do in that denser range.

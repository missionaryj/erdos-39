# Comparing quadratic blocks at polynomially different scales

Research initiated by **@missionaryj**, with mathematical analysis and computation assisted by OpenAI Codex.

At one prime, the secant slope of a parabola gives [endpoint labels](endpoint-labels.md) that agree on every shared difference. What happens if the small and large rulers use fields of different degrees over the same base? In the range where their scales interact, polynomial labels of bounded degree can certify only a vanishing fraction of the modular conflicts in the model below. There are corresponding integer lifts with the same obstruction. This narrows the search for labels and leaves open the possibility of choosing subsets by other means.

## Setup and bound

Fix integers $m<n<2m$ and an odd prime $q$. Write $E=\mathbb F_q^m$ and $H=\mathbb F_q^n$. Give each space a symmetric bilinear multiplication for which multiplication by every nonzero element is an invertible linear map. Ordinary multiplication in the fields of orders $q^m,q^n$ supplies examples. Write $M_d$ and $N_w$ for the two multiplication maps. In each space take the graph of $Q(x)=x x/2$. Fix arbitrary injective linear maps $U,V:E\longrightarrow H$ to embed the two small coordinates into the large ones.

Every ordered small difference $(d,v)$ with $d\ne0$ occurs exactly once. Its endpoint parameters are $M_d^{-1}v\pm d/2$, since subtracting the quadratic values gives the product of the horizontal difference and the midpoint. The embedded gap has unique large endpoints $N_{U(d)}^{-1}V(v)\pm U(d)/2$.

Suppose the small and large parameters receive scalar labels $f:E\to\mathbb F_q$ and $g:H\to\mathbb F_q$ given by polynomials of total degree at most $D<q$, at least one nonconstant. Then their sums of endpoint labels agree for at most
$$
 D(m+n+1) q^{2m-1}
$$
of the $q^m(q^m-1)$ ordered small differences. The upper bound can be trivial for small $q$. For fixed dimensions and bounded $D$ the fraction tends to zero, uniformly over the embeddings and labels.

## Proof

Use the $m$ coordinates of $d$ as indeterminates. Let $A(d)=\det M_d$ and $B(d)=\det N_{U(d)}$. These homogeneous polynomials of degrees $m,n$ are nonzero on every nonzero base-field vector. The polynomial $A$ is irreducible over $\mathbb F_q$. Otherwise a homogeneous factor of positive degree less than $m$ would have a nonzero zero by Chevalley–Warning. For this use of the theorem, sum $1-P(d)^{q-1}$ over the space for a homogeneous polynomial $P$ of degree less than $m$. Every monomial in the power has some variable with exponent less than $q-1$, so its sum vanishes in the field. The number of zeros is divisible by $q$, and the origin is one. By the same argument $A$ cannot divide $B$, since the quotient would have degree $n-m$ strictly between 0 and $m$ and would supply a nonzero zero of $B$.

Consider the difference of the two sums of endpoint labels as a rational function of $(d,v)$. If $f$ has positive degree $r$, let $f_r$ be its leading homogeneous part. Choose $v_0$ so that $f_r(M_{d_0}^{-1}v_0)\ne0$ for some fixed $d_0\ne0$. This is possible by invertibility and $r<q$. Substitute $v=t v_0$. The coefficient of $t^r$ on the small side is the nonzero rational function $2 f_r(M_d^{-1}v_0)$. It is homogeneous of degree $-r$ in $d$. By the adjugate formula its denominator divides $A^r$, and its reduced denominator must contain $A$ because a nonzero polynomial cannot have negative degree. Every coefficient on the large side has denominator dividing $B^D$. Since $A$ is irreducible and does not divide $B$, the coefficients cannot agree identically.

If $f$ is constant and $g$ has positive degree $s$, choose $z\in H$ with $g_s(z)\ne0$. The linear map $d\mapsto N_{U(d)}z\bmod V(E)$ has a nonzero kernel because its source has dimension $m$ and its target dimension $n-m<m$. Take $d_0\ne0$ in the kernel and $v_0$ with $V(v_0)=N_{U(d_0)}z$. At $d=d_0$ and $v=t v_0$ the coefficient of $t^s$ on the large side is $2g_s(z)\ne0$, again proving nonidentity.

Multiply the label difference by $A^D B^D$. The result is a nonzero polynomial of total degree at most $D(m+n+1)$. For example, each small endpoint component has denominator $A$ and numerator of degree at most $m+1$ in $(d,v)$. The same bound uses $n+1$ on the large side. The polynomial zero bound in $2m$ variables now gives the assertion, as both denominators are nonzero at every difference under consideration.

## Integer lifts and scope

Choose coordinate bases on the large horizontal and vertical spaces extending the respective images of the small bases. Put the $2m$ common coordinates first, followed by the remaining coordinates, and encode their representatives as base-$2q$ digits. Each graph gives an integer Sidon set because an ordinary difference recovers the full signed digit vector, and the modular graph has unique ordered nonzero differences. The integer horizons are $(2q)^{2m}$ and $(2q)^{2n}$, with respectively $q^m$ and $q^n$ marks.

There exist coordinate offsets for which at least $q^m(q^m-1)/2^{2m+1}$ positive integer differences coincide. Translate each graph independently in its own vector space before taking representatives. For a shared modular difference, a component with residue $r$ lifts to $r$ or $r-q$ with probabilities $1-r/q$ and $r/q$. The two lifts agree with probability at least $1/2$. The low-coordinate translations are independent across components, and all remaining difference coordinates are zero in both graphs. Take expectations and divide by two for opposite orientations. The label bound applies uniformly to any labels chosen even after the offsets are fixed, since every ordinary match is a modular match on the original parameter pairs. Thus for fixed $m,n$, certifying a fixed positive fraction of the conflicts on these lifts with one such polynomial-label pair requires degree of order at least $q$.

The denominator argument uses full quadratic graphs, linear embeddings of the two coordinates, and polynomial labels over the common base field. It does not estimate how many conflicts survive after deleting marks. In particular it gives no upper bound for general Sidon sets in problem 39.

## Exact finite tests

For degrees two and three we also tested arbitrary scalar labels on the full modular graphs. Using $x^2$ in place of $x^2/2$ scales both ordinate coordinates by the same factor. In the examples at $q=5,7$ the entire linear system has nullity one, both in characteristic $q$ and in characteristic 101. Thus even unrestricted labels satisfying every equation must be the same constant on both blocks in those examples. At $q=3$ the nullity is nine.

| Base prime | Modular conflicts, unoriented | Integer conflicts, zero offsets | Number of label variables |
|---:|---:|---:|---:|
| 3 | 36 | 13 | 36 |
| 5 | 300 | 87 | 150 |
| 7 | 1,176 | 335 | 392 |

The code enumerates all ordered modular gaps, checks uniqueness in each graph, constructs one equation per shared unoriented gap, and computes rank by modular elimination. It checks the integer gaps independently. [Verifier](field_bridge.py)

# A near-full prefix constrains later growth

Research initiated by @missionaryj, with analysis and verification assisted by OpenAI Codex. We apply the elementary shifted-interval counting method to **both** Sidon blocks. This gives a necessary condition for a solution to Erdős #39. It also explains a limitation of choosing optimal finite blocks independently. No novelty claim is made for the estimates.

## The overlap inequality

Let $B,C$ be Sidon sets in integer intervals of $M,L$ positions, with sizes $t,u$. Let $D(B)$ denote the set of positive differences. For every positive integer $h$ put
$$
W_h=\sum_{d\in D(B)\cap D(C),\ d<h}(h-d).
$$
Then
$$
2W_h\ \ge\ \frac{(ht)^2}{M+h-1}+\frac{(hu)^2}{L+h-1}-h(t+u)-h(h-1).
$$
Indeed, let $R_B(y)$ count the ways to write $y=b+i$ for $b\in B$ and $1\le i\le h$. There are $ht$ representations in at most $M+h-1$ positions. By Cauchy–Schwarz their sum of squared multiplicities is at least $(ht)^2/(M+h-1)$. Its exact value is $ht+2\sum_{d\in D(B),d<h}(h-d)$ because $B$ is Sidon. Add the corresponding bound for $C$. The union of the two difference sets contributes at most $\sum_{d=1}^{h-1}(h-d)=h(h-1)/2$; their intersection contributes $W_h$ once more. This proves the inequality with no assumptions on the locations of the intervals or how the sets were selected.

## How far a dense prefix constrains the count

Let $A$ be any Sidon set of positive integers and let $t=A(M)$, $M\ge2$. Define
$$
\eta=\max(0,1-t/\sqrt M)+M^{-1/4},\qquad L=\lfloor M/\eta\rfloor.
$$
Then **$A(M+L)=O(\sqrt M)$**, with an absolute implied constant.

To see this, apply the inequality to $B=A\cap[1,M]$ and $C=A\cap[M+1,M+L]$. Sidonicity of $A$ gives $W_h=0$ since the two blocks cannot realize the same difference. Writing $u=|C|$ gives
$$
\frac{u^2}{L+h-1}
\le 1-\frac{t^2}{M+h-1}+\frac{t+u}{h}.
$$
Take $h=\lceil M^{3/4}\rceil$. From the definition of $\eta$, the first two terms on the right combined are at most $2\max(0,1-t/\sqrt M)+(h-1)/M=O(\eta)$. The elementary distinct-differences bound $\binom t2\le M-1$ gives $t/h=O(M^{-1/4})$. Also $L+h=O(M/\eta)$ and $(L+h)/h=O(\sqrt M)$ because $M^{-1/4}\le\eta\le2$. Multiplying through gives $u^2\le O(M)+O(\sqrt M)u$, hence $u=O(\sqrt M)$.

In particular, if $A(M)\ge\sqrt M-O(M^{1/4})$ along an unbounded sequence of $M$, then $L\gg M^{5/4}$ there. At the endpoints $N=M+L$ the count is $O(N^{2/5})$. A fixed multiplicative constant in the horizon can also be accommodated: using $L=\lfloor M^{5/4}\rfloor$ directly in the proof gives $u=O(\sqrt M)$ under the same deficit assumption. More generally, an additive deficit $O(M^{1/2-\delta})$ infinitely often for fixed $\delta>0$ forces an upper counting exponent at those endpoints of at most $1/(2(1+\min(\delta,1/4)))$, strictly below $1/2$.

The hypothesis is much stronger than the lower bound in #39. For example, counts of order $\sqrt M/\log M$ eventually exceed $M^{1/2-\epsilon}$ for each fixed $\epsilon>0$, while leaving a deficit of order $\sqrt M$. This argument gives no contradiction for a set with that growth. It rules out an approach that insists on keeping prefixes polynomially close to the leading constant one infinitely often.

## Testing independent placements

For a prime modulus $P$, let $T$ be Sidon modulo $P$ with $k$ points. Apply a uniformly random affine map $x\mapsto ax+b$ with $a\ne0$ and lift to representatives in $[0,P)$. Each ordered pair of distinct points has a uniform image among all $P(P-1)$ ordered distinct pairs. Precisely $P-d$ of those pairs have ordinary oriented difference $d>0$ for $d<P$. Modular Sidonicity implies there is at most one such representation per realization. Consequently for any fixed old difference set $D\subset[1,P-1]$ the **exact mean** overlap is
$$
\frac{k(k-1)}{P-1}\sum_{d\in D}(1-d/P).
$$
For $k\asymp\sqrt P$ and old differences below $o(P)$ the mean is of order $|D|$. An old Sidon block with $M^{1/2-o(1)}$ marks has $M^{1-o(1)}$ differences. When $M=P^r$ for fixed $1/2<r<1$, the mean is polynomially larger than the $P^{1/2+o(1)}$ overlap sufficient in the [neighboring-block criterion](neighboring-blocks.md). A mean bound alone leaves exceptional placements open. The deterministic inequality above applies to every placement.

For a separate exact illustration use $M=16002$, $L=397530$, $t=126$, and $u=630$. The overlap inequality with $h=16002$ forces at least 3271 common positive differences for **any** Sidon blocks of these sizes and lengths, since each shared difference contributes at most $h-1$ to $W_h$. Scanning $h$ also rules out 361 new marks when disjoint differences are required, giving a ceiling of 360. This ceiling is for this example's parameters only.

The script constructs near-full blocks modulo $p(p-1)$ for $p=127,631$. For $0\le i<p-1$ the mark has residues $i\bmod(p-1)$ and $g^i\bmod p$, with $g$ primitive modulo $p$. A nonzero index difference $k\bmod(p-1)$ makes the other coordinate difference $g^i(g^k-1)$ determine $i$, so ordered differences are unique. Six affine placements for the larger block give between 7710 and 7821 common integer differences. These composite-modulus examples illustrate the deterministic bound; the prime-modulus mean formula is a separate calculation. [Exact verification](saturated_blocks.py)

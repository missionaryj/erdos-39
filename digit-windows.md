# A dense digit-box prefix restricts every integer extension

Research initiated by **@missionaryj**, with mathematical analysis and computation assisted by OpenAI Codex.

Consider the integer ruler $R_p=\{2px+[x^2]_p:0\le x<p\}$ for an odd prime $p$. **Any integer Sidon set containing this ruler, or a translate of it, has at most $O(p^{7/5})$ points in every interval of $p^3$ positions.** This holds with arbitrary later marks and ordinary integer differences. Square-root order at that horizon would be $p^{3/2}$. The loss persists if up to $p^{1-\epsilon}$ marks of the ruler are discarded for fixed $\epsilon>0$.

The input to the proof is the size of the prefix in its *digit box*. The ruler has $p$ points in a box of $p^2$ digit vectors. Its integer diameter is about $2p^2$, so a near-equality hypothesis in the usual integer interval Sidon bound would miss this example.

## Finite inequality

Fix integers $p\ge2$, $d\ge1$, put $b=2p$, and let $E(x)=\sum_{i=0}^{d-1}b^i x_i$. Take $t$ vectors $R\subset\{0,\ldots,p-1\}^d$ whose encoded integers are Sidon. Suppose $B$ is a Sidon set of $u$ integers in an interval of $N$ positions whose positive differences avoid those of $E(R)$. This includes the remaining points in any interval of a Sidon extension of a translate of $E(R)$.

For any positive integer $h$ write
$$
 w=h^d,\quad D_R=(p+h-1)^d,\quad
 D_B=(b+h-1)^{d-1}\big(\lceil N/b^{d-1}\rceil+h-1\big).
$$
Then
$$
 \frac{(wt)^2}{D_R}+\frac{(wu)^2}{D_B}
 \ \le\ w(t+u)+w^2-w. \tag{1}
$$

Translate $B$ into $[0,N)$ and write each integer using $d-1$ low digits in radix $b$ and one unrestricted high quotient. This gives vectors $T$ decoding to the translated marks, including when $d=1$. All nonzero ordered vector differences from $R$ and $T$ taken together are distinct. Indeed two equal vectors decode to equal signed integer differences, ruled out by the hypotheses. Translation of either block preserves its internal differences.

Let $J=\{0,\ldots,h-1\}^d$, and write $r_J(v)$ for the number of ordered pairs from $J$ with difference $v$. For $S=R$ or $T$, Cauchy–Schwarz bounds the sum of squares of multiplicities of $S+J$ below by $(w|S|)^2/|S+J|$. The same sum of squares equals $w|S|$ plus $\sum_{v\in (S-S)\setminus\{0\}}r_J(v)$. On adding the two estimates, each nonzero difference of $J$ is counted at most with its own multiplicity, whose total is $w^2-w$. The displayed support bounds $D_R,D_B$ follow coordinate by coordinate. This proves (1).

## All polynomially intermediate horizons

Put $M=p^d$ and $\delta=\max(0,1-t/\sqrt M)$. For $M\le N\le M^2$ and fixed $d$, (1) yields
$$
 t+u\ll_d \sqrt M+
       \left(\frac{N^{d+1}}{M}\right)^{1/(2d+1)}
       +\sqrt{N\delta}. \tag{2}
$$
In particular, if $N=M^{r+o(1)}$ with $1<r<2$ fixed and $\delta\le M^{-\eta}$ for fixed $\eta>0$, the bound saves a fixed power over $\sqrt N$ throughout this range.

Here are the estimates. The ordinary vector difference count gives $t(t-1)<(2p)^d$, so $t\ll_d\sqrt M$. For $1\le h\le p$, one has $D_B\ll_d N$ since $N\ge p^d$, and
$$
 1-t^2/D_R\le 2\delta+O_d(h/p).
$$
After division by $w^2$, solving (1) as a quadratic inequality in $u$ gives
$$
 u\ll_d N/h^d+\sqrt{N\delta}+\sqrt{Nh/p}+\sqrt{Nt/h^d}.
$$
The last term is at most $(t+N/h^d)/2$. Take $h=\lceil(Np)^{1/(2d+1)}\rceil$, which is at most $p$ since $N\le p^{2d}$. The first and third terms have order $(N^{d+1}/M)^{1/(2d+1)}$.

For $d=2$, the quadratic ruler has distinct ordered differences because its two signed digits are recoverable and $2xu+u^2\bmod p$ determines $x$ for nonzero horizontal increment $u\bmod p$. More generally, **any** Sidon ruler on $p-a$ digit vectors in the same square gives
$$
 t+u\ll p^{7/5}+p\sqrt a \qquad(N=p^3,\ 0\le a\le p).
$$
For example, $a\le p^{1-\epsilon}$ gives a saving of $\min(1/10,\epsilon/2)$ from the exponent $3/2$. The argument permits arbitrary distributions of the missing points. In dimension one, (2) bounds extensions of a near-full ordinary prefix by $O(\sqrt M+(N^2/M)^{1/3}+\sqrt{N\delta})$. This optimizes the earlier [shifted-interval inequality](two-block-overlap.md) over the entire subquadratic range. Equidistribution of extremal one-dimensional Sidon sets in short intervals has also been studied by Cilleruelo and by Ortega and Prendiville. [Ortega and Prendiville](https://www.numdam.org/articles/10.5802/jtnb.1239/)

## Checks and scope

The verifier counts the shifted multiplicities directly for three finite rulers, checks ordinary difference-disjoint extensions, and evaluates the exact quadratic bound (1) with integer arithmetic. At $p=100003$, scanning $1\le h\le p$ gives at most 18,677,074 additional marks in any interval of $p^3$ positions from $h=13515$. The square root of this interval length exceeds 31.6 million. [Verifier](digit_windows.py)

H1 allows a prefix of size $M^{1/2-o(1)}$. Such a prefix can have $\delta$ arbitrarily close to one. Inequality (2) then leaves the square-root exponent possible. Its obstruction applies when a proposed construction retains a sufficiently full fixed-dimensional digit box at a relevant earlier scale.

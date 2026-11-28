# A sharp bound for a quadratic ruler at prime-power precision

Research initiated by **@missionaryj**, with mathematical analysis and computation assisted by OpenAI Codex.

Let $p$ be a fixed odd prime and $P=p^k$. Among the integer marks $2Px+[x^2]_P$ for $0\le x<P$, the largest Sidon subset has size $\Theta_p(P^{2/3})$. Here $[z]_P$ is the representative in $[0,P)$. The ambient length is of order $P^2$, so this construction has counting exponent $1/3$. The bound applies specifically to this host.

The motivation is that congruent vector differences $(u,v)$ at two nested precisions imply $v\equiv u(x+x')\pmod{p^k}$ at the lower precision, where $u=x'-x$. For $0<|u|<p^k$, dividing out the power of $p$ in $u$ recovers the sum of the endpoint parameters modulo $p^{k-v_p(u)}$. This allows [slope comparisons](slope-separation.md) across precisions provided the encoding preserves coordinate differences. The following calculation establishes the cost already within a single level.

## Upper bound

More generally consider a Sidon subset of $t$ marks $2Px+f(x)$ with $0\le x,f(x)<P$. Suppose congruence of the inputs modulo $R=p^s$ implies congruence of the outputs modulo $R$. By Cauchy–Schwarz at least $(t^2/R-t)/2$ unordered pairs have both inputs in the same class modulo $R$. Orient these by increasing $x$. Their positive horizontal differences and signed vertical differences are multiples of $R$ with absolute value less than $P$. There are at most $2(P/R)^2$ such vectors, and reusing one repeats an integer difference. Hence
$$
 t^2\le Rt+4P^2/R.
$$
Squaring respects every congruence. Using $s=\lfloor 2k/3\rfloor$ gives $t=O_p(P^{2/3})$. Even preserving just one intermediate precision $R=P^{\lambda+o(1)}$, $0<\lambda<1$, gives $t\le P^{\max(\lambda,1-\lambda/2)+o(1)}$.

## Matching construction

First take $P=L^3$ with $L=p^m$. By Bertrand's postulate choose an odd prime $q$ between $L/4$ and $L/2$ for sufficiently large $L$. Use
$$
 S=\{i+L[i^2]_q:0\le i<q\}, \qquad
 T=\{a+Ls:0\le a<L,\ s\in S\}.
$$
The residues of $S$ modulo $L$ are distinct, and $S$ is Sidon modulo $L^2$. In fact both digit sums are less than $L$. Equal modular sums first give the same sum of indices and then the same sum of their squared residues. Modulo $q$ this determines the product as well, so the two indices are the roots of the same monic quadratic. The indices lie in $[0,q)$.

The $Lq$ parameters of $T$ are distinct modulo $L^2$ by their first two digits $a,i$. Suppose two different ordered pairs of graph points $(x,x^2)$ had the same nonzero vector difference modulo $P$. Write the starting parameters as $x,x+h$ and the ending parameters as $x+d,x+h+d$. Then $d,h$ are nonzero modulo $P$ and $2dh=0$ modulo $P$. Both are differences of distinct elements of $T$, so neither is divisible by $p^{2m}$. Since $p$ is odd, $p^{3m}\mid dh$ implies both are divisible by $p^m$. All four parameters therefore have the same first digit $a$. Subtracting $a$ and dividing by $L$ gives two distinct ordered pairs in $S$ with the same nonzero difference modulo $L^2$, which is impossible.

The integer ruler inherits the modular difference property because its radix $2P$ makes the signed vertical difference recoverable from the integer difference. This supplies at least $L^2/4$ marks for sufficiently large $L$. For general $k$, use the same parameters as at $P_0=p^{3\lfloor k/3\rfloor}$. Any repeated modular difference at $P$ would reduce to one at $P_0$, where the parameters are still distinct. As $P/P_0\le p^2$, the lower bound is $\Omega_p(P^{2/3})$.

At $P=3^9$ this gives 351 marks and 122,850 distinct ordered differences in the two coordinates modulo $P$. [Exact verifier](prime_power_rulers.py)

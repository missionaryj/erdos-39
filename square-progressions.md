# First repeated sum of squares in a residue class

Research initiated by @missionaryj, with mathematical exploration and drafting assisted by OpenAI Codex. A natural host for Erdős problem 39 is the sequence of squares, which already has counting exponent 1/2. Selecting a dense Sidon subset of the squares is a separate extremal problem. A recent finite upper bound is $R\exp(-c\log R/\log\log R)$ roots through $R$. This bound is compatible with the exponent $R^{1-o(1)}$ required by the square approach. [Erdős problem 773](https://www.erdosproblems.com/773) · [Combinatorial large sieve preprint](https://arxiv.org/abs/2606.17487)

## A sharp threshold for a complete progression

For odd $m\ge3$ and a unit $r$ modulo $m$, let $H(m,r)$ be the least possible largest root in a nontrivial equality $a^2+b^2=c^2+d^2$ with all four roots positive and congruent to $r$ modulo $m$. Pairs are unordered, and equal entries within a pair are allowed. For every fixed $0<\epsilon<1/4$, uniformly in the unit $r$,

$$
2(1+\sqrt2)m^2\ \le\ H(m,r)\ \le\
2(1+\sqrt2)m^2+O_\epsilon(m^{7/4+\epsilon}).
$$

### Lower bound

Set $D=a+b-c-d$. If $D=0$, the common sum and sum of squares determine the product, so the two pairs agree. For a nontrivial collision write each root as $r+mj$. Expanding the squares gives $2r(D/m)\equiv0\pmod m$. Thus $m^2$ divides $D$, since $2r$ is a unit. Squares agree with their roots modulo two, so $D$ is also even. Hence $|D|\ge2m^2$.

Take $(x,y)$ to be the pair with smaller coordinate sum, ordered with $x\ge y$. The larger sum is at most $\sqrt{2(x^2+y^2)}$. For $0\le t\le1$ the convex function $\sqrt{2(1+t^2)}-1-t$ has maximum $\sqrt2-1$ at zero (its other endpoint value is zero). Taking $t=y/x$ gives $|D|\le(\sqrt2-1)x$. This proves the lower bound.

### Upper bound

Choose positive integers $k,w$ with $kw\equiv r\pmod m$ and set $v=w+m$. The two pairs

$$
(kv-mw,\;kw+mv),\qquad(kv+mw,\;kw-mv)
$$

have the same squared norm $(k^2+m^2)(v^2+w^2)$. All four coordinates are $r$ modulo $m$. The first coordinate sum exceeds the second by exactly $2m(v-w)=2m^2$, so the pairs are distinct.

Write $\alpha=1+\sqrt2$, $\beta=1/\sqrt2$, and $U=m^{3/4+\epsilon}$. Select $k\in[\alpha m+U,\alpha m+2U]$ and $w\in[\beta m+U,\beta m+2U]$ satisfying the product congruence. Such integers exist for every sufficiently large odd $m$, uniformly in $r$. Indeed the modular-hyperbola rectangle estimate gives a count $\varphi(m) (U+O(1))^2/m^2+O(m^{1/2+o(1)})$. Use the actual integer lengths of the two intervals in the main term. Since $\varphi(m)=m^{1-o(1)}$, the main term dominates. The interval for $k$ can be translated by $-2m$ before applying the estimate. [Shparlinski, *Modular hyperbolas*, Theorem 13 and formula (10)](https://arxiv.org/pdf/1103.2879)

At the limiting values $k=\alpha m$, $w=\beta m$ the coordinate $kw-mv$ vanishes because $(\alpha-1)\beta=1$. Our shifts make it strictly positive. The other coordinates are strictly positive for all large $m$. The largest limiting coordinate is $kv+mw=2(1+\sqrt2)m^2$; the shifts change each coordinate by $O(mU)$. This proves the upper estimate. For a finite explicit witness at any modulus one can use $k=2m+1$, $w=m+r$ with $1\le r<m$. These choices also make all coordinates positive.

## Consequence for the infinite construction

At the first collision the complete progression has supplied only $\Theta(m)$ roots and its largest squared value is $\Theta(m^4)$. The resulting count at this scale has exponent 1/4. A construction that aims for exponent 1/2 using squares would need to choose roots more selectively across classes. The calculation imposes no fixed power loss on arbitrary subsets of squares. No novelty claim is made for the threshold.

The verifier scans roots in increasing order, enumerates all unordered pairs up to the first collision, and tests the irrational lower bound with integer arithmetic. It covers every unit class for odd moduli from 3 through 35 and selected larger examples. For $m=251$, $r=1$, the first equal sums are $210841^2+221383^2=503^2+305719^2$. The ratio $305719/251^2$ is about 4.85261, compared with the limiting value 4.82843. [Exact verifier](square_progressions.py)

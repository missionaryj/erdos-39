# Two square-root horizons with every mixed collision removed

Research initiated by **@missionaryj**, with mathematical analysis and computation assisted by OpenAI Codex.

For every sufficiently large prime $p$, the construction below gives $\gg p^2$ early integers through $4(2p)^4$ and $\gg p^3$ later integers through $4(2p)^6$. The early block is Sidon. Every sum with one summand in each block has a unique representation in the union. No internal early difference occurs in the later block. In the union each nonzero ordered difference occurs at most **twice**, and every sum has at most **four** unordered representations, including doubles. Thus the remaining collisions occur entirely among later marks. At $p=17$, deleting 390 later marks gives a genuine 779-mark Sidon set retaining all 85 early marks. The proof of the multiplicity bounds is uniform; the size of that particular repair is a finite computation.

## A finite target for the two horizons

Let $L=\mathbb F_{p^2}$ and choose a nonsquare $\alpha\in L$. Identify $K=L(\theta)$ with $L^2$ by $P=x+z\theta$, where $\theta^2=\alpha$. Write $\pi:K\to L$ for the constant coefficient. The later marks are selected from the graph
$$
 (x,\pi(P^2),z)=(x,x^2+\alpha z^2,z).
$$
A repeated sum on this graph is exactly a rectangle in the parameter plane with respect to the quadratic form $x^2+\alpha z^2$. Indeed, the horizontal sum fixes a parallelogram. If $D=(u,v)$ and $H=(u',v')$ are its adjacent sides, the second-coordinate discrepancy between its diagonal sums is $2(uu'+\alpha vv')=2\pi(DH)$. The form is anisotropic because $-1$ is a square in $L$ and $\alpha$ is a nonsquare. There are no midpoint collisions or collinear nontrivial rectangles. For the general relation between rectangle counts and additive energy of a paraboloid see [Lewko, *Counting rectangles and an improved restriction estimate for the paraboloid*](https://arxiv.org/abs/1901.10085).

Consequently, a rectangle-free parameter set of size $p^{3-o(1)}$ in this plane would give two genuine Sidon blocks at the stated exponents. Here is how to make them compatible. Fix a nonzero base-field coordinate $\ell:L\to\mathbb F_p$, using representatives in $[0,p)$. In the early block take $(a,a^2,0)$ with $0\le\ell(a)<p/4$. In the later block take $z\ne0$ and $p/4\le\ell(x)<p/2$. A translate of any proposed parameter set retains a constant fraction under these two later restrictions, by averaging over translations in $L^2$. Translations preserve rectangles.

For a later gap to match an early one, the later endpoints must have equal $z$. The ratio of the second-coordinate difference to the nonzero first-coordinate difference then equals $x+x'$ in the later block and $a+a'$ in the early one. Their $\ell$ values lie in disjoint intervals modulo $p$. A mixed sum fixes $z$, $x+a$ and $x^2+a^2$ after subtracting $\alpha z^2$. It therefore determines the unordered pair $\{x,a\}$, and the intervals distinguish its roles. A mixed difference from early to later likewise fixes $z$, $x-a\ne0$ and $x^2-a^2$, hence both endpoints.

## An explicit cone with at most two representations per difference

Choose a base-field linear functional $\lambda:K\to\mathbb F_p$ such that $Q(P)=\lambda(P^2)$ is a nondegenerate quadratic form of nonsquare determinant and $\lambda$ is nonzero on $\theta L$. Use the cone $Q(P)=0$ as the later parameter set before the two restrictions.

Here is an explicit choice matching the verifier. Take
$$
 \lambda(x+z\theta)=\operatorname{Tr}_{L/\mathbb F_p}(\gamma x+z),\qquad
 \chi_L(\alpha\gamma^2-1)=-1,
$$
where $\chi_L$ is the quadratic character. Such a $\gamma$ exists. In fact $\sum_\gamma\chi_L(\alpha\gamma^2-1)=-\chi_L(\alpha)=1$ and none of the terms vanish. The character sum follows by counting the factorizations $(u-v)(u+v)=1/\alpha$. The binary form inside the trace has determinant $\alpha\gamma^2-1$. After diagonalizing it over $L$, its determinant over $\mathbb F_p$ has the square class of the norm of this element: the determinant of the trace pairing appears twice, and multiplication by a scalar contributes its norm. The norm of a nonsquare in $L$ is a nonsquare in $\mathbb F_p$.

No two-dimensional subspace is totally isotropic for $Q$. Otherwise the Gram matrix in a basis starting with that subspace would have block form $\left(\begin{smallmatrix}0&B\\B^t&A\end{smallmatrix}\right)$ with square determinant $(\det B)^2$. In particular, every affine line contained in the cone passes through the origin: for $P+tv$ on the cone identically, $P,v$ are isotropic and orthogonal for its polar form.

The cone contains $p^3-p(p-1)$ points. For example, diagonalize $Q$ and expand the zero indicator in additive characters. The zero frequency gives $p^3$; each nonzero frequency contributes $-p$ after normalization because the determinant is a nonsquare and the fourth power of the quadratic Gauss sum is $p^2$. At most $2p^2$ cone points satisfy $\ell(x)=0$, by the polynomial zero bound on that hyperplane; the restricted form is nonzero since a three-dimensional totally isotropic space is impossible. Scaling by $\mathbb F_p^\times$ equalizes the counts at all nonzero values of $\ell(x)$. Discarding $z=0$ costs at most $p^2$ further points. The fixed later interval therefore retains $\gg p^3$ marks.

For a prescribed nonzero horizontal difference $D\in K$, write the earlier endpoint of the later-block chord as $P$. Specifying its vertical difference fixes $\pi(DP)$ by expansion of $(P+D)^2$. The two cone equations also fix $\lambda(DP)=-\lambda(D^2)/2$. These are three independent base-field linear conditions, since $\lambda$ is nonzero on $\ker\pi=\theta L$ and multiplication by $D$ is invertible. The potential starts lie on one affine line. If at least three starts work, $Q(P)$ and $Q(P+D)$ vanish identically on that line by degree two. Both the line and its translate by $D$ must then pass through zero. They coincide, so their direction is $D$, which would give $\pi(D^2)=0$ from the fixed value of $\pi(DP)$. Anisotropy rules this out. Thus there are at most two starts.

## Four unordered representations per sum

A later sum fixes $C=P+P'$ and $\pi(P^2+P'^2)$. The interval restriction makes $C\ne0$. Write $D=P-P'$. The cone equations and the given sum fix both $\lambda(D^2)$ and $\pi(D^2)$, and give $\lambda(CD)=0$. Hence $D^2=v+th$ for some fixed $v\in K$, $t\in\mathbb F_p$, where $h$ spans $\ker\pi\cap\ker\lambda$. The element $h$ is a nonsquare in $K$: it belongs to $\theta L^\times$, all of $L^\times$ consists of squares in $K$, and $N_{K/L}(\theta)=-\alpha$ is a nonsquare in $L$.

If $v/h\in L$, the only possible square in $h(v/h+\mathbb F_p)$ is zero, yielding at most the double pair. Otherwise $v/h$ has four distinct conjugates $r_i$ over $\mathbb F_p$. After extension to an algebraic closure, split $K$ into its four embedding coordinates. The equations read
$$
 D_i^2=h_i(t+r_i)\quad(1\le i\le4),\qquad \sum_{i=1}^4 c_iD_i=0 ,
$$
with all $h_i,c_i\ne0$. For the last assertion write $\lambda(CD)$ as a trace pairing with a nonzero coefficient. Over the rational function field in $t$, the four factors $t+r_i$ have independent square classes, since each has a different simple zero. Thus the four square roots allow independent sign changes, and no signed sum with all coefficients nonzero vanishes identically. Multiplying the linear expression over all sign choices gives a nonzero polynomial in $t$. The solution set is finite. Eliminating $t$ gives three quadrics and the linear equation in the four coordinates of $D$. The affine Bézout bound gives at most eight isolated solutions over the algebraic closure. They come in pairs $D,-D$, and $D=0$ is impossible in this case. This proves the claimed four.

## Integer checks and the remaining step

Use the six base-field components in the order $x,\pi(P^2),z$ as radix-$2p$ digits, multiply the encoding by four, and add one on the early block or two on the later block. Every sum identifies its level pair modulo four. Every difference identifies its ordered mixed type or is internal to a level. Ordinary equalities imply equality of the corresponding modular vectors because digit sums never carry. The slope separation handles the shared internal difference type.

The verifier enumerates every unordered sum and every nonzero difference at four primes, then removes later vertices to break the actual repeated integer sums. At $p=17$ the unrestricted union in these intervals has maximum integer difference multiplicity two and sum multiplicity three. The modular later block attains both bounds, two and four. The repaired set keeps 694 later marks, with all 303,810 unordered sums in the union distinct. [Verifier](cone_blocks.py)

To retain the exponent at the later horizon through this construction, a sufficient next result would be a rectangle-free subset of size $p^{3-o(1)}$ in the parameter plane. The cone supplies a bound of two on each difference and leaves actual rectangles. Even the two-horizon Sidon result would still need a construction across all the horizons in H1.

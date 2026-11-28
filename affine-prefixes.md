# Exact prefix counts for one affine encoding of a parabola

Research initiated by **@missionaryj**, with mathematical analysis and computation assisted by OpenAI Codex.

Let $q$ be an odd prime power, $d\ge1$, $s=q^d$, $K=\mathbb F_{s^2}$ and $L=\mathbb F_s$. The graph $S=\{(x,x^2):x\in K\}$ is Sidon in the additive group $K^2$. Among *all affine subspaces* of dimension $2d+t$ over $\mathbb F_q$, the largest intersection with $S$ has exactly
$$
 s+q^t-q^{\max(0,t-d)}\qquad(0\le t\le 2d)
$$
points. **One nested sequence of subspaces attains every maximum simultaneously.** At dimension $3d$ the exact count is $2s-1$.

## Upper bound

For every nontrivial additive character $\chi$ on $K^2$, $|\sum_{v\in S}\chi(v)|\le s$. To see this, write $\chi(x,y)=\alpha(x)\beta(y)$ with additive characters on $K$. If $\beta$ is trivial, summation in $x$ gives zero. Otherwise the squared magnitude can be evaluated by writing the two horizontal parameters as $x+h,x$. For $h\ne0$ the inner sum contains the character $\beta(2hx)$ and vanishes. The diagonal contributes $s^2$.

An affine subspace of codimension $r=2d-t$ has indicator equal to an average over $q^r$ characters of the quotient by its direction space, each multiplied by a phase for the translate. The trivial character contributes $s^2/q^r=q^t$ points. The others add at most $(1-q^{-r})s$. Rounding down gives the stated integer upper bound, including at $r=0$.

## Simultaneous equality

Write $K=L+L\theta$ with $\theta^2$ a nonsquare in $L$. For $x=a+b\theta$ the two high components of $(x,x^2)$ over $L$ are $(b,w)=(b,2ab)$. Each specified high pair with $b\ne0$ has one preimage. The pair $(0,0)$ has $s$ preimages, and $(0,w)$ for $w\ne0$ has none.

Use the $2d$ low coordinates in $L^2$ first, then the $d$ base-field digits of $b$, then those of $w$. Allowing the first $2d+t$ coordinates to vary and setting the rest to zero admits $q^t$ high pairs. Exactly $q^{\max(0,t-d)}$ of these have $b=0$. The number of points is therefore $q^t-q^{\max(0,t-d)}+s$, as required.

For prime $q$, the coordinates are integer digits in radix $2q$. A level of $m$ free digits gives the integer cutoff $(2q)^m$ after shifting every mark by one. An arbitrary invertible affine coordinate change on $K^2$ gives precisely an affine-flat preimage at this cutoff. Equal integer sums imply equal modular vector sums, so the lifts are Sidon. For fixed $d$ and $q\to\infty$ the $3d$-digit horizon has at most $(2q)^{3d(1/3+o(1))}$ points under **every** such encoding. The same bound applies after thinning. Even covering an early set by pieces with different affine encodings of this host needs $q^{d/2-o(1)}$ pieces to reach $q^{3d/2-o(1)}$ points there, by the union bound.

## Exact extension with a level marker and one extra field coordinate

There is a related optimization in $L^3$. Prescribe the $s$ old points $(x,x^2,0)$, and choose later points $(u,v,z)$ with $z\ne0$. Require each block to be modular Sidon and their internal nonzero differences to be disjoint. A level marker distinguishes the two blocks in an integer encoding. In this model the exact maximum combined count is $(5s-3)/2$.

Indeed, the early block uses every difference $(u,v,0)$ with $u\ne0$. All later points at a given $z$ must therefore have the same first coordinate. If row $z$ has $k_z$ marks, its internal differences consume $k_z(k_z-1)$ distinct nonzero vertical values over the entire family. There are only $s-1$ available. Since $2(k_z-1)\le k_z(k_z-1)$ for a nonempty row, the number of later marks is at most $(s-1)+(s-1)/2$.

Put the point $(z^2,0,z)$ in every nonzero row, and add $(z^2,c_z,z)$ in $(s-1)/2$ distinct rows, using one representative $c_z$ from each pair $\{c,-c\}\subset L^\times$. Within rows every ordered vertical difference is unique. Between rows a nonzero difference in $z$ and the corresponding difference in $z^2$ determine the ordered pair of rows. Two different representations using the same two rows would give equal nonzero internal vertical differences in these rows. This proves Sidonicity and attains the upper bound. For a prime base field, multiplying the radix encodings by four and adding one in the old block or two in the later block makes the integer union Sidon. At $q=43,d=1$, it keeps 43 old marks and adds exactly 63.

## Verification and relevance to H1

The verifier exhausts all affine subspaces and their translates in the indicated dimensions for $q=3,5,7$ and $d=1$. In the quartic field at $q=5$, the same digit order attains counts $25,29,49,145,625$ and all 195,625 integer sums of unordered pairs are distinct. [Verifier](affine_prefixes.py)

The exact counts above describe one host and a specific modular extension model. The [digit-box bound](digit-windows.md) treats arbitrary integer extensions of a full earlier quadratic ruler and allows ordinary carries. H1 still requires a uniform family that retains the square-root exponent through the intermediate horizons.

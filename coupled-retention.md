# How thinning the coupled rows interacts with integer carries

Research initiated by **@missionaryj**, with mathematical analysis and verification assisted by OpenAI Codex.

For the [six-coordinate construction](coupled-rows.md), ordinary integer gaps can be different even when they agree modulo the base prime in every digit. The following bound takes that freedom into account. It applies even when almost all of the early row has been discarded, provided that one sufficiently wide coordinate box of the row is kept intact.

Let $p$ tend to infinity through odd primes, $K=\mathbb F_{p^2}$, and $\alpha$ a nonsquare in $K$. Lift
$$
 (x,\ x^2+b+\alpha b^2,\ bx),\qquad x\in K,\ b\in\mathbb F_p,
$$
to integers using the six base-field components as digits in radix $2p$, in the order shown. A coordinate box in the first four digits means a product of ordinary intervals of representatives in $[0,p)$.

**Retention bound.** Suppose a Sidon subset of the lifted integers retains every row-zero mark $(x,x^2,0)$ whose first four digits lie in one box, each of whose four side lengths is at least $\rho p$, with $0<\rho\le1$ and $\rho=p^{-o(1)}$. Then the subset contains at most $p^{5/2+o(1)}$ marks altogether. The original set has $p^3$ marks at a horizon of order $p^6$. Thus keeping a whole box of the stated size forces a power loss at that horizon. The assertion allows the location of the box to depend on $p$.

### Reconstructing the old chord

Fix a nonzero high coordinate $w=bx$. Its possible points are indexed by the nonzero rows $b$, with $x=w/b$. Given two different rows $b,c$ in this fiber, the gap from $w/b$ to $w/c$ has the same modular low-coordinate difference as the chord of the old parabola starting at
$$
 Z(b,c)=\frac wb-\frac{bc(1+\alpha(b+c))}{2w}
$$
and ending at $Z(b,c)+w/c-w/b$. Indeed the common translation of the two horizontal parameters changes the squared difference by $c+\alpha c^2-b-\alpha b^2$. Since the horizontal gap is nonzero, this old chord is unique.

### Distribution of its starting point

For any subset $T\subset\mathbb F_p^\times$ of size $t>0$, take the $t^2$ ordered pairs in $T^2$, including the diagonal for this estimate. For any nonzero additive frequency of the four coordinates of $(Z,Z^2)$, the magnitude of its average character over these pairs is at most
$$
 C\left(\frac{\sqrt p}{t}+\frac{p^{1/4}}{\sqrt t}\right)
$$
with an absolute constant. To prove this write its phase as $P_b(c)=\ell_1(Z)+\ell_2(Z^2)$ with base-field linear forms $\ell_i:K\to\mathbb F_p$. Put $A=1/(2w)$ and $B=\alpha/(2w)$, so $Z=w/b-(A b+B b^2)c-Bbc^2$.

If $\ell_2\ne0$, the coefficient of $c^4$ is $\ell_2(B^2)b^2$. If it vanishes identically, the coefficient of $c^3$ is $2\ell_2(AB)b^2$ and is nonzero for $b\ne0$, because $B^2,AB$ are independent over the base field. If $\ell_2=0$, use the coefficient $-\ell_1(B)b$ of $c^2$, or, when that vanishes, the coefficient $-\ell_1(A)b$ of $c$. In each case there is a nonconstant coefficient at positive $c$-degree taking the same value for at most two possible $b$ per value.

Apply Cauchy–Schwarz over the $c$ variable, then extend the resulting sum of squared magnitudes to all $c\in\mathbb F_p$. The square of the unnormalized character sum is bounded by $t$ times the sum over $b,b'\in T$ of the magnitudes of complete character sums for $P_b-P_{b'}$. At most $2t$ pairs can have the selected coefficient equal and cost at most $p$ apiece. For the others the phase is a nonconstant polynomial of degree at most four, giving a bound $3\sqrt p$ by the standard Weil bound for additive character sums when $p>4$. Dividing by $t^4$ and taking a square root gives the estimate.

### Forcing an ordinary repeated difference

Inside the retained box take its middle half in each coordinate. Its normalized volume is $\gg\rho^4$. The normalized Fourier coefficients of an interval of residues have sum of absolute values $O(\log p)$, by the geometric-sum formula. Fourier expansion in four coordinates therefore bounds the discrepancy of the proportion of old chord starts in the smaller box from its volume by
$$
 O\left((\log p)^4\left(\sqrt p/t+p^{1/4}/\sqrt t\right)\right).
$$
This estimate is uniform in the box and the fiber.

Partition the four low coordinates of the retained points at $w$ into $O(\rho^{-4})$ cells of side at most $\rho p/8$. If a cell contains $t>C'\sqrt p(\log p)^8\rho^{-8}$ points, for a sufficiently large absolute $C'$, the preceding estimate puts $\gg\rho^4 t^2$ old chord starts in the smaller box. For all sufficiently large $p$ this exceeds the $t$ diagonal pairs. Take an off-diagonal pair giving such a start. Each signed digit difference between its two new points has absolute value at most $\rho p/8$. Adding those signed differences to the four digits of the old chord start stays inside the retained box without any modular wrap. The modular reconstruction now implies equality of the **ordinary** digit differences. The new and old pairs are distinct, since $w\ne0$, and their integer gaps agree. This contradicts Sidonicity.

Consequently each nonzero high fiber has $O(\sqrt p(\log p)^8\rho^{-12})$ retained points. There are $p^2-1$ such fibers. The fiber at zero consists of row zero and at most $p-1$ other points. This proves the bound. For example, even retaining the full row restricted to an ordinary interval of length $\asymp p$ in one input coordinate is subject to it. Arbitrary sparse thinnings of row zero need not contain such a box.

## A simultaneous bound on unordered sums

There is also a constant-density thinning of the whole untagged construction with at most six unordered representations per modular sum, including doubles, while the earlier bound of four on ordered nonzero differences still holds. Keep those $x$ whose first base-field component has representative between $1$ and $(p-1)/2$. In every sum the horizontal coordinate $S=x+x'$ is nonzero. The thinning retains $p(p-1)/2$ early points and $p^2(p-1)/2$ in total.

Write $V,W$ for the second and third sum coordinates. When the two row labels agree, $W=bS$ determines the row and the sum of squares recovers its unordered parameter pair. Otherwise write the rows as $j+c,j-c$, set $z=c^2\ne0$, and put $D=V-S^2/2$. Eliminating the horizontal parameters gives
$$
 (W-jS)^2-2zD+4jz+4\alpha j^2 z+4\alpha z^2=0 .
$$
Use the basis $1,\alpha$. Write $(W-jS)^2=A_0(j)+\alpha A_1(j)$, $D=D_0+\alpha D_1$ and $L=4j-2D_0$. The first coordinate equation is $A_0+Lz=0$. Eliminating $z$ in the second gives
$$
 A_1 L^2+(2D_1-4j^2)A_0 L+4 A_0^2=0.
$$
This polynomial in $j$ has degree five. Indeed $S^2$ has nonzero first component, since every nonzero element of $\alpha\mathbb F_p$ is a nonsquare in $K$. The coefficient of degree five is $-16$ times this component. Each root with $L\ne0$ gives at most one $z$. At the possible root with $L=0$ a solution requires $A_0=0$, making it at least a double root of the displayed polynomial. There the second coordinate equation is quadratic in $z$ and permits at most two values. Thus there are at most five pairs $(j,z)$. Each square $z\ne0$ determines one unordered row pair, and $S,W$ then recover the horizontal parameters. Including the same-row possibility gives at most six. The bound passes to the integer lift because equal integer sums determine equal modular sums.

## Finite checks

At $p=7$, 720 unordered pairs of nonzero-high points lie in a common high fiber. Every such pair has a matching modular chord in row zero, and 161 also match as ordinary integer gaps in the chosen bases. At $p=3$, exhaustive search with all nine row-zero marks fixed permits exactly seven modular additions or fifteen integer additions. These differing optima are why the ordinary carry calculation matters. In the half-coordinate thinning at $p=11$, enumeration of every unordered sum of the 605 retained points gives maximum multiplicity four. [Exact verifier](coupled_retention.py)

# A quadratic construction with at most four representations of each difference

Research initiated by **@missionaryj**, with mathematical analysis and verification assisted by OpenAI Codex.

This construction permits new low-coordinate residues after the initial Sidon prefix. Over an odd prime $p$ it has $p^2$ initial-row points and $p^3$ points altogether. Six base-field coordinates suffice to bound every nonzero ordered difference multiplicity by four. Adding the row index as a seventh coordinate makes all such differences unique. The distinction matters for H1, which requires uniqueness.

Let $K=\mathbb F_{p^2}$ and choose a nonsquare $\alpha\in K$. Every nonzero base-field element is a square in $K$, so $1,\alpha$ are linearly independent over $\mathbb F_p$. For $x\in K$ and $b\in\mathbb F_p$ take
$$
 (x,\;x^2+b+\alpha b^2,\; b x)\in K^3.
$$
The layer $b=0$ is an ordinary Sidon parabola in its first two coordinates.

## Recovering the row difference

For an ordered pair let $d=x'-x$, $c=b'-b$, and $j=(b+b')/2$. Write $v$ and $w$ for the differences in the second and third coordinates. When $d\ne0$ the equations are
$$
 x+x'=(v-c-2\alpha jc)/d,\qquad
 2dw=c(v-c)+2j(d^2-\alpha c^2).
$$
Once $c$ is specified these equations determine $j$ and both endpoints. The factor $d^2-\alpha c^2$ never vanishes for $d\ne0$, by the nonsquare choice. Furthermore $c$ must satisfy
$$
 \frac{2dw-cv+c^2}{d^2-\alpha c^2}\in\mathbb F_p .
$$
Equate the ratio with its conjugate under $z\mapsto z^p$ and clear denominators, treating $c$ as a base-field variable. The resulting polynomial has degree four, with leading coefficient $\alpha-\alpha^p\ne0$ up to sign. There are at most four possible $c$.

For $d=0$ a nonzero difference must have $c\ne0$. Now $v=c+2\alpha jc$ determines $c,j$ in the basis $1,\alpha$, and $w=cx$ recovers $x=x'$. This proves the four-representation bound in all cases. It concerns ordered differences. Bounded multiplicity of pair sums would require its own argument.

## The exact cost of a correction depending only on the row

Appending $b$ makes $c$ available, so the seven-coordinate set is Sidon. Conversely, for a correction $h(b)$ in any abelian group, if the full corrected set is Sidon in the product group then $h$ is injective.

To see this, suppose two distinct rows have the same correction. Take the two ordered row transitions from row zero to these two rows. Their correction differences agree, and their row differences $c_1,c_2$ are distinct. Fix any $d\ne0$. For a transition with row midpoint $j_i$, the right side of the equation for $2dw$ is affine in $v$ with slope $c_i$. Since the slopes differ, there is a $v\in K$ where the two right sides agree. For each transition the first equation then supplies actual $x,x'$ with horizontal difference $d$. These different pairs give the same corrected difference. Thus every row-only correction distinguishing all modular gaps needs at least $p$ values, and $b$ attains that minimum.

## Integer interpretation

Expand each $K$ coordinate into two base-field components, take representatives in $[0,p)$, and use them as digits in radix $2p$, with $x$ and the second coordinate lowest. In the corrected construction put $b$ above all six digits. A signed integer difference uniquely recovers its digit differences because each has absolute value less than $p$. After shifting the encoded integers by one, the initial $p^2$ row-zero marks lie through $(2p)^4$. There are $p^3$ marks through $(2p)^6$ with the fourfold difference allowance, or through $(2p)^7$ with full Sidon uniqueness. The row-only lower bound is proved for modular differences. It does not exclude an integer construction exploiting carries or a correction also depending on $x$.

At $p=5$ and $7$, exhaustive tests attain modular multiplicity four before adding the row index. At $p=7$, all 117,306 nonzero ordered differences of the 343 corrected points are distinct. The uncorrected size at the two displayed horizons has the desired square-root order, but multiplicity four and two horizons do not give the simultaneous Sidon construction required by H1. [Verifier](coupled_rows.py)

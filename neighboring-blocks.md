# Which earlier blocks can collide?

Research initiated by @missionaryj, with mathematical exploration and software assisted by OpenAI Codex. Use the [difference-block criterion](difference-blocks.md) with $X_j=2^{j^2}$. The argument below identifies the range of interactions one needs to control in that criterion and gives an unconditional construction for a single window of nearby scales. The simultaneous infinite construction remains open.

## Spacing costs no exponent

Let $B$ be a finite Sidon set of $t>0$ integers. For a positive integer $h$, join two vertices when their distance is less than $h$. Each distance is used at most once, so there are at most $h-1$ edges. There exists an $h$-separated subset of size at least
$$
\frac{t^2}{t+2(h-1)}.
$$
Indeed, retain vertices preceding all their neighbors in a random ordering. This gives an independent set whose expected size is the sum of $1/(1+\deg v)$, at least the displayed bound by Cauchy–Schwarz. In this particular graph an optimal subset is also found by taking the least available integer and skipping all points less than $h$ above it. In an optimum one may replace its first point by the least available integer without decreasing any subsequent gap; iterate.

Take $t\ge X_j^{1/2-o(1)}$ and $h_j=\lceil\sqrt{X_j}\rceil$. The retained size still has exponent $1/2$, and all retained differences lie in $[h_j,X_j)$. Thus blocks at indices $i<j$ with $2i^2\le j^2$ automatically have disjoint difference sets after this extraction. The remaining indices lie in the window $j/\sqrt2<i<j$. Spacing alone cannot replace $1/2$ by a larger fixed power: a subset of $[0,X)$ separated by $X^{1/2+\eta}$ has size at most $1+X^{1/2-\eta}$.

## A sufficient overlap estimate

Write $D(B)$ for the positive internal differences. It suffices to construct one sequence of finite Sidon blocks $B_j\subset[0,X_j)$ of sizes $t_j\ge X_j^{1/2-o(1)}$ satisfying
$$
E_j=\left|D(B_j)\ \cap\!
  \bigcup_{j/\sqrt2<i<j}D(B_i)\right|
  \le X_j^{1/2+o(1)}.
$$
No spacing assumption is needed on these input blocks. On each $B_j$, join a pair if its difference is below $h_j$ or occurs in a block of the indicated window. There are at most $h_j-1+E_j$ edges by Sidonicity. The same independent-set estimate gives a subset of size at least $t_j^2/(t_j+2(h_j-1+E_j))$, which has exponent $1/2$. Earlier blocks outside the window have diameter below $h_j$. For pairs inside the window we excluded collisions even with the original, unthinned earlier block. Hence the extracted blocks have globally distinct internal differences, as required. This is a sufficient estimate on proposed blocks, not an estimate established for any infinite candidate of the required sizes.

## Many adjacent levels in a single finite construction

Fix a large top index $J$ and any integer width $w=w(J)=o(J)$, $0\le w<J$. All levels $J-w,\ldots,J$ can meet the target exponent simultaneously while avoiding any previously allocated differences at most $\sqrt{X_J}$. For this finite window choose a prime $p$ between $\lceil\sqrt{X_J}\rceil$ and twice that number, and use the Sidon ruler
$$
T(i)=2pi+(i^2\bmod p),\qquad 0\le i<p.
$$
The [digit proof](residue-lifts.md) gives Sidonicity; gaps between consecutive marks are at least $p+1$. For each window index $j$ allocate a separate consecutive slice of
$$
k_j=\left\lfloor\frac{X_j}{4p(w+1)}\right\rfloor
$$
indices. The total number allocated is at most $X_J/(4p)\le p/4$. Translate each corresponding set of marks so its minimum is zero. A slice of $k_j\ge1$ marks has diameter below $2pk_j\le X_j/2$. Internal differences are unchanged by translation, and no difference can occur in two slices of the same Sidon ruler. Their minimum positive difference exceeds $\sqrt{X_J}$.

Uniformly throughout this window, $\log_2 p=J^2/2+O(1)$ and $j^2=J^2-o(J^2)$. Therefore $\log_2 k_j=j^2/2-o(j^2)$ in the sense of a uniform lower bound. This permits growing windows, for example $w=\lfloor\sqrt J\rfloor$. Two independently built windows may still collide where their difference ranges overlap. In particular, this construction does not bridge from indices near $J/\sqrt2$ through the entire intervening range to $J-w$.

## Finite verification

In the repository's 357-point witness below $2^{20}$ there are exactly 600 pairs at distance below 1024. Greedy extraction leaves 231 marks separated by at least 1024. A prefix dynamic program independently verifies this is the maximum possible within that witness. This checks the extraction procedure, not the missing overlap estimate. [Verifier](block_spacing.py) · [Input witness](data/repacked-witness.json)

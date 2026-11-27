# A linear test for separating shared differences

Research initiated by **@missionaryj**, with mathematical analysis and software assisted by OpenAI Codex.

The secant slope in the [quadratic example](slope-separation.md) is a sum of endpoint labels. The same idea gives a sufficient condition for Erdős 39 in which the labels can change for each pair of levels. They solve a homogeneous linear system specified entirely by the lists of repeated differences.

## Repair after arbitrary previous deletions

Let $B,C$ be finite Sidon rulers. For a chosen collection of their shared differences, seek labels $f(b),g(c)$ in a common odd prime field such that
$$
 f(b)+f(b')=g(c)+g(c')
 \quad\text{whenever}\quad b'-b=c'-c>0
$$
for the chosen differences. Suppose no value of $f$ occurs more than $|B|/16$ times. There are subsets of $B,C$ of sizes at least $|B|/8,|C|/8$ such that none of these differences survives in both. No assumption on the multiplicities of $g$ is needed.

Represent the labels on a circle of circumference $p$, with residues at integer positions. Write $m=|B|$ and let $F$ be the largest fiber of $f$. Rotate an open semicircle whose boundary avoids the labels, measuring the number of first-block marks inside. A half turn interchanges the inside and outside counts. At each change only one residue crosses a boundary because $p$ is odd, so the count changes by at most $F$. We can therefore choose complementary semicircles both containing at least $m/2-F$ first-block marks. Use the one containing at least half the second-block marks. Lift all labels there to a common real interval of length $p/2$.

Take a median of the first labels in this interval, counted with multiplicity. Each strictly smaller or strictly larger side contains at least $(m/2-F)/2-F$ first marks. At least half the second marks in the interval lie weakly on one side of the median. Keep those, and keep first marks strictly on the opposite side. The lower bounds are $m/4-3F/2\ge m/8$ and $|C|/4$. The two types of pair sums lie strictly apart and all sums lie in one open interval of length $p$. They cannot agree modulo $p$.

## Simultaneous criterion

Use the spaced blocks in the [neighboring-scale formulation](neighboring-blocks.md), with $X_i=2^{i^2}$ and sizes $t_i=X_i^{1/2+o(1)}$. For every interacting pair $i<j$ suppose the label equations for **all** its shared differences admit a solution in an odd prime field. Fields and labels can be chosen independently for each pair. Suppose on at least one of its levels $k\in\{i,j\}$ every label has multiplicity at most $t_k/(16\cdot 8^{2k})$. Then Erdős 39 has an affirmative answer.

Process interacting pairs by increasing larger index, breaking ties arbitrarily. Each level $k$ occurs in fewer than $2k$ pairs, since its partners have indices strictly between $k/\sqrt 2$ and $\sqrt 2 k$. Repeated application of the preceding lemma preserves at least $8^{-2k}t_k$ marks on that level. Indeed, whenever it is the side with the multiplicity bound, the original bound is at most one sixteenth of the current size by induction. Deletions preserve all earlier repairs. Each block stabilizes after finitely many operations, and the loss has logarithm $O(k)=o(\log X_k)$. The final blocks have disjoint internal differences and give the desired integer sequence by the [block encoding](difference-blocks.md).

The argument also permits exceptions. If the omitted conflicts admit the [cross-pair covers](cross-pair-covers.md) of size $t_j X_j^{o(1)}$ at level $j$, restrict those covers to the survivors and apply that criterion. Their sizes still meet its bound because the first round of deletions lost only $X_j^{o(1)}$ as a factor.

## What the linear system detects

For any two full quadratic blocks at the same prime, $f(x)=k_1x$, $g(y)=k_2y$ satisfy the equations, including after arbitrary vertical offsets. Each label map is injective. Thus this test covers the example whose minimum cross-pair cover grows quadratically.

For the previous 66- and 256-mark rulers the system from all 339 shared differences has 322 columns. At each of the twelve primes tested, its rank is 297. Although its solution space has dimension 25, **all 66 labels on the small side are forced equal, and 230 labels on the large side are forced equal**. To verify the assertion for every solution in a tested characteristic, express each coordinate as a linear functional of the 25 free coordinates by exact elimination. Equal coefficient vectors force equal labels. The verifier also substitutes a basis of the full solution space back into the 339 equations. The tested primes range from 3 to 65,521. No conclusion in other characteristics follows from these computations.

The outstanding construction is to obtain sufficiently spread labels or sufficiently few uncovered exceptions on every interacting pair at once. [Exact verifier](endpoint_labels.py)

# Dense random candidates and the cost of repairing them

Research initiated by @missionaryj, with analysis assisted by OpenAI Codex. These deductions address one approach to Erdős problem 39. The independent selection model below already has the required counting exponent at every large scale. Its residual collisions are a structural obstacle, even when we permit bounded changes to the retained integers.

## A relaxation with arbitrarily slowly increasing representation counts

Fix any nondecreasing positive integer function $g(s)$ tending to infinity. There exists a set $A$ with $A(N)=N^{1/2+o(1)}$ and at most $g(s)$ unordered representations of every integer $s$ as a sum of two elements of $A$, including doubles. The construction depends on the prescribed function. Related fixed-multiplicity results include Cilleruelo's probabilistic constructions. [Fixed-multiplicity paper](https://matematicas.uam.es/~franciscojavier.cilleruelo/Preprints/probabilistic%20constructions%20of%20B2g.pdf)

Independently include $n$ with probability $p_n=n^{-1/2-1/\sqrt{g(n)}}$. The expected count through $N$ is at most $2\sqrt N$. Summing over the last half of the interval gives a lower bound of order $N^{1/2-1/\sqrt{g(\lfloor N/2\rfloor)}}$. Chernoff bounds on dyadic checkpoints, followed by Borel–Cantelli and monotonicity, give the asserted exponent almost surely.

For a fixed sum $s$, the off-diagonal unordered pairs use disjoint inputs. Their occurrence indicators are independent. Their mean total $\mu_s$ is at most $C s^{-1/\sqrt{g(s)}}$ for an absolute constant $C$. Indeed, the larger summand is at least $s/2$ and at most $s$, and the sum of $[i(s-i)]^{-1/2}$ over $1\le i<s/2$ is bounded uniformly by comparison with $\sqrt{2/s}\sum_{i\le s/2} i^{-1/2}$. With $k=g(s)$, the expected number of collections of $k$ distinct occurring pairs is at most $\mu_s^k/k!$. Even allowing a diagonal pair, more than $g(s)$ representations requires at least $k$ off-diagonal pairs. The violation probability is therefore at most $s^{-\sqrt{k}} C^k/k!$, summable since $k\to\infty$. Almost surely only finitely many sums violate the cap. Removing the finitely many inputs involved in those violations preserves the exponent.

## Deletions and local changes

Consider any independent host with inclusion probabilities $p_n\le C n^{-1/2}$, including the one above. Allow an algorithm to see the entire host, discard any elements, and move each retained integer $n$ by at most $n^\gamma$, for a fixed $0\le\gamma<1/2$. Almost surely **every** Sidon set $S$ obtained in this way satisfies

$$
S(N)\le N^{\beta+o(1)},\qquad
\beta=\max\{1/3,\;1/4+\gamma/2\}.
$$

In particular, displacements of size $n^{1/6}$ still give exponent at most $1/3$. Even displacements of size $n^{1/2-\delta}$ for a fixed $0<\delta<1/2$ leave a fixed exponent gap. This is an upper bound. It makes no assertion about attainability.

### Proof

Work in the output block $[M,2M)$ for dyadic $M$. All preimages of outputs in this block lie in $[M/2,3M]$ for sufficiently large $M$, since displacements are sublinear. Each output has at most $O(M^\gamma)$ possible preimages. For a particular set of $t$ outputs to occur, they need distinct selected preimages. Sum over only injective assignments. Independence gives probability at most $(C' M^{\gamma-1/2})^t$ by the union bound. This step permits arbitrary dependence among the algorithm's choices.

Theorem 2.1 of Kohayakawa, Lee, Rödl and Samotij, applied after translation with their parameter $\sigma=1/2$, bounds the number of $t$-point Sidon subsets of this output block by

$$
M^{3s_0}\left(\frac{64e M}{t^2}\right)^t,\qquad
s_0=(4M\log M)^{1/3},\quad t\ge 2s_0.
$$

[Counting theorem, authors' manuscript](https://www.math.tau.ac.il/~samotij/papers/Sidon.pdf)

Multiplying these bounds gives an upper bound on the probability that even one such repair is possible. Set $t=\lceil M^{\beta+\epsilon}\rceil$ for any fixed small $\epsilon>0$. The factor inside the resulting $t$-th power is at most $C''M^{-2\epsilon}$, and $3s_0\log M=o(t\log M)$. Thus the probability is at most $\exp(-\epsilon t\log M)$ for all sufficiently large $M$ (absorbing the constant and the prefactor). Larger repaired sets would contain a $t$-point subset. The probabilities are summable on dyadic blocks. Borel–Cantelli, a geometric sum over blocks, and then a countable sequence $\epsilon\downarrow0$ prove the bound simultaneously for every repaired set.

### Implication for problem 39

A representation cap tending to infinity arbitrarily slowly is compatible with the target density, yet the random host produced by this proof almost surely cannot supply a Sidon subset of that density even after the specified repairs. Substituting a constant cap of one into the first proof loses the density estimate. The obstruction in the second proof uses independence of host membership for distinct preimages. It leaves open constructions in which membership decisions are coordinated across scales. No novelty claim is made for these deductions.

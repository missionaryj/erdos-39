# Erdős problem 39

Research initiated by **@missionaryj**. Mathematical exploration, software and drafting assisted by OpenAI Codex. This repository records partial results on the dense infinite Sidon set problem. The question remains open in the cited literature.

A Sidon set has distinct sums for all unordered pairs, including pairs with equal entries. Does there exist one infinite Sidon set of positive integers whose count through N is at least a constant (depending on ε) times N^(1/2−ε) for every ε>0 at every sufficiently large N? Cilleruelo constructed a sequence with counting exponent √2−1+o(1), following Ruzsa’s earlier existence result. [Problem and bibliography](https://www.erdosproblems.com/39) · [Cilleruelo’s paper](https://arxiv.org/abs/1209.0326)

## Reproduce the experiments

Use Node.js 18 or later. No packages are required.

```sh
node fields.mjs
node experiments.mjs
node experiments.mjs --generate
node experiments.mjs --search-prefix
```

The default integer run independently checks every unordered pair sum in the stored witness and computes two upper bounds for extending its 208-point prefix. The generate option reconstructs and writes the witness from the frozen 46-point prefix. The search-prefix option reruns the 3,000 seeded trials that selected that prefix. The field script exhausts the nine-input test and enumerates the quadratic-extension blocks.

| N | Points ≤ N | Individually admissible candidates above previous checkpoint before greedy extension |
|---:|---:|---:|
| 16 | 3 | — |
| 64 | 6 | — |
| 256 | 12 | — |
| 1,024 | 25 | — |
| 4,096 | 46 | — |
| 16,384 | 74 | 9,200 |
| 65,536 | 123 | 37,759 |
| 262,144 | 208 | 149,510 |
| 1,048,576 | 346 | 585,157 |

The 346 integers have 59,685 distinct positive differences and 60,031 distinct unordered sums. In the final interval the algorithm retained 138 mutually compatible additions. For this exact prefix the translated-interval inequality gives an upper bound of 752 additions. The maximum is unknown. These finite measurements do not determine the asymptotic exponent.

[Full witness](data/witness.json) · [Proofs, assumptions and limitations](notes.md)

A separate note constructs near-square-root-density random sets with any prescribed diverging cap on sum representations. It derives a bound on how many points can survive if collisions are repaired by deletions and local moves. [Random constructions and repair bounds](random-repair.md)

For a construction that coordinates points by residue class, a difference count gives an exact intermediate-scale limit and a necessary condition for every candidate infinite solution. Two explicit integer lifts test the sharpness of the bound. Run `node residues.mjs` to verify their sums. [Residue-class bounds and constructions](residue-lifts.md)

For square roots in a single invertible class modulo an odd integer, the first repeated sum of squares has a sharp asymptotic threshold. Run `python3 square_progressions.py` to reproduce the finite checks. [Threshold and proof](square-progressions.md)

The analysis of Cilleruelo’s prime encoding isolates a limitation of changing digit positions and gives a continued-fraction test for mixed-level collisions. Run `python3 prime_layers.py` to reproduce the finite checks. [Prime-layer analysis](prime-layers.md)

The [Left to Solve reduction](lean/Erdos39.erdos_39.R1.lean) passed the Lean kernel and axiom audit and was merged with credit to **@missionaryj**. It proves the implication from two hypotheses to #39. H1 asks for a uniform finite construction and H2 transfers it to an infinite set by compactness. The upstream proof of H2 by @ivillar was merged in PR #9874. H1 remains open. Our [local H2 draft](lean/Erdos39.erdos_39.R1.H2.lean) is separate. [Accepted reduction PR #8688](https://github.com/GuillaumeBAUD-coder/open-math-agents/pull/8688) · [Accepted H2 proof PR #9874](https://github.com/GuillaumeBAUD-coder/open-math-agents/pull/9874)

Repacking the last interval increases the verified count from 346 to 357 with the same 208-point prefix. The revised bounds are **149–747 additions** in that interval. Run `python3 verify_repacking.py` for the independent checks. [Witness](data/repacked-witness.json) · [Bounds and finite-prefix extension lemma](notes.md#repacking-the-last-interval)

An equivalent formulation asks for finite blocks at successive scales whose internal positive differences are all distinct across the family. A binary encoding combines such blocks into one infinite Sidon set at the required exponent. Run `python3 difference_blocks.py` for the finite checks. [Criterion, construction at separated scales, and unresolved step](difference-blocks.md)

The difference-block criterion can be localized to earlier indices between $j/\sqrt2$ and $j$. A single finite ruler also supplies compatible blocks for growing windows of nearby indices. Run `python3 block_spacing.py` to verify the spacing experiment. [Neighboring scales and the outstanding overlap estimate](neighboring-blocks.md)

A prefix with at least $\sqrt M-O(M^{1/4})$ points constrains the count through $M^{5/4}$ to $O(\sqrt M)$. A weighted difference count quantifies the overlap required of neighboring blocks and explains why independent affine placement has too much overlap on average in the dense regime. [Proof, assumptions, and exact finite example](two-block-overlap.md)

Interleaving $k$ Sidon sets yields an explicit union with lower counting exponent $1/(1+2^{1/k})$. Each colour has exponent $1/3$ in this construction. Run `python3 interlaced.py` to check a mixed-colour collision in the finite example. [Construction and proof](interlaced.md)

The four interleaved blocks can be thinned to a single 241-element Sidon set, keeping at least 70.7% of each block. A two-block bound and an abstract matching example identify the limits of a repair argument based solely on pairing equal differences. Run `python3 paired_gaps.py` to reproduce the witness. [Proof and finite repair](paired-gaps.md)

Two quadratic integer rulers can require quadratically many cross-pairs to cover their conflicts, even though a secant-slope restriction keeps a quarter of each with disjoint differences. The earlier marked-ruler example has exact minimum cross-pair cover 317. Run `python3 slope_separation.py` for the finite checks. [Slope separation and proof](slope-separation.md) · [Cross-pair cover criterion](cross-pair-covers.md)

A linear system on the endpoints of shared differences gives a sufficient criterion that can compare each pair of levels in its own prime field. The proof allows repeated thinning after earlier repairs. Run `python3 endpoint_labels.py` to check all solutions of the system for the earlier marked rulers in twelve characteristics. [Endpoint labels and simultaneous criterion](endpoint-labels.md)

For the quadratic ruler modulo a fixed odd prime power $P$, the largest Sidon subset has order $P^{2/3}$. An explicit three-digit construction attains that order. Run `python3 prime_power_rulers.py` for the modular checks. [Construction and upper bound](prime-power-rulers.md)

For full quadratic graphs over different field degrees, bounded-degree endpoint labels capture only a vanishing fraction of shared modular differences when the larger degree lies strictly between the smaller degree and its double. The proof also gives integer lifts at polynomially different horizons. Run `python3 field_bridge.py` for the exact small-field systems. [Bound and proof](field-bridge.md)

For a product of two finite rulers with a prescribed first-row prefix, an exact extension formula follows from four-cycle-free bipartite graphs. A point-line construction gives a 388-mark example with 52 prescribed early marks. Run `python3 incidence_extension.py` for the exhaustive small optimum and the independent sum checks. [Extension formula and two-horizon bound](incidence-extension.md)

A single residue lift preserves a prescribed modular Sidon prefix, attains the exact maximum number of additions at every shallow cutoff, and approaches the height-packing bound within a logarithmic factor at all heights from $s$ through $s^2$, where $s$ is the number of base marks. A separate terminal construction attains the optimal order at any specified deeper horizon. Run `python3 simultaneous_lifts.py` for the checks. [Simultaneous bounds and constructions](simultaneous-lifts.md)

A quadratic construction that opens additional residues has square-root counts at two polynomially different horizons with nonzero difference multiplicity at most four. A row coordinate restores Sidon uniqueness, and its alphabet size is optimal among corrections depending only on the row in this modular model. [Proof and exact tests](coupled-rows.md)

For the six-coordinate construction, retaining an intact box of the early parabola forces a power loss even for ordinary integer Sidon sets. A separate thinning bounds both sum and difference multiplicities by absolute constants at two horizons. Run `python3 coupled_retention.py` for exact small-field checks. [Carry analysis and bounds](coupled-retention.md)

For independent thinning of the earlier degree-two parabola followed by optimal selection from the degree-three parabola, the sharp common exponent at the two prescribed horizons is $3/7$ with high probability. The upper bound also applies to ordinary integer gaps in the specified digit lift. Run `python3 fiber_thinning.py` for four finite checks. [Tradeoff, chord calculation and exact small optima](fiber-thinning.md)

For the same two parabolas, a coordinated choice on two parallel lines has an exact linear repair cost. A uniformly sampled earlier subset of size $1\ll k\ll p^{3/2}$ requires $(16/81+o(1))\binom{k}{2}$ later deletions in the integer lift with high probability. For another explicit pair of lines the same earlier marks cost $p^2+O(p)$ later deletions modulo the field and at most $2p-2$ as integers. [Proof and exact checks](coordinated-repair.md)

Any integer Sidon extension of the $p$-mark ruler $2px+[x^2]_p$ has only $O(p^{7/5})$ marks in every interval of $p^3$ positions. A shifted-box inequality gives estimates for arbitrary near-full digit boxes throughout the subquadratic range. [Proof and exact finite bounds](digit-windows.md)

For a single parabola over $\mathbb F_{q^{2d}}$, one affine digit order simultaneously attains the exact maximal prefix counts in dimensions $2d$ through $4d$. The maximum at dimension $3d$ is $2q^d-1$. [Extremal counts, construction and verification](affine-prefixes.md)

An elliptic quadric gives square-root counts at the $p^4$ and $p^6$ horizons with all mixed sums unique, no shared early and later internal differences, at most two representations per nonzero difference, and at most four per unordered sum. At $p=17$ a finite repair retains all 85 early marks and 694 later ones with exact Sidon uniqueness. [Construction, rectangle criterion and verifier](cone-blocks.md)

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

The [Left to Solve reduction draft](lean/Erdos39.erdos_39.R1.lean) separates constructing finite Sidon sets with one shared growth envelope from passing to an infinite set by compactness. The file proves only the conditional implication from its two stated hypotheses and awaits verification against the pinned Lean environment. The first hypothesis contains the outstanding finite construction.

The submitted version of the reduction is tracked in [upstream PR 8688](https://github.com/GuillaumeBAUD-coder/open-math-agents/pull/8688). A [draft proof of the compactness hypothesis](lean/Erdos39.erdos_39.R1.H2.lean) adapts the finite-coordinate subsequence argument used for Erdős 28. It awaits kernel verification. The uniform finite construction remains open.

Repacking the last interval increases the verified count from 346 to 357 with the same 208-point prefix. The revised bounds are **149–747 additions** in that interval. Run `python3 verify_repacking.py` for the independent checks. [Witness](data/repacked-witness.json) · [Bounds and finite-prefix extension lemma](notes.md#repacking-the-last-interval)

An equivalent formulation asks for finite blocks at successive scales whose internal positive differences are all distinct across the family. A binary encoding combines such blocks into one infinite Sidon set at the required exponent. Run `python3 difference_blocks.py` for the finite checks. [Criterion, construction at separated scales, and unresolved step](difference-blocks.md)

The difference-block criterion can be localized to earlier indices between $j/\sqrt2$ and $j$. A single finite ruler also supplies compatible blocks for growing windows of nearby indices. Run `python3 block_spacing.py` to verify the spacing experiment. [Neighboring scales and the outstanding overlap estimate](neighboring-blocks.md)

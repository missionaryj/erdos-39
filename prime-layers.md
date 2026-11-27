# Mixed-level collisions in the discrete-logarithm construction

Research initiated by @missionaryj, with analysis and code assisted by OpenAI Codex. Cilleruelo constructs an infinite Sidon sequence of counting exponent $\sqrt2-1$. This note examines two modifications of the argument. The first changes the active digits at a given level. The second recovers the actual prime pairs behind a possible collision. [Cilleruelo, *Infinite Sidon sequences*, Section 2](https://arxiv.org/pdf/1209.0326)

## Which step changes the exponent?

In Cilleruelo's construction each prime label is encoded by discrete logarithms modulo several different primes. Digits have enough space for addition without carries, and their ranges distinguish one active digit from the sum of two. For two fixed levels write $p,h$ for labels from the larger level and $s,z$ for labels from the smaller one. Equal encoded sums require $ps\equiv hz\pmod U$ in the common digits and $p\equiv h\pmod V$ in the large-only digits. Here $U,V$ are the corresponding products of moduli. If masks also allow small-only digits with product $W$, then $s\equiv z\pmod W$ as well. These are necessary conditions for the fixed pairing of levels.

In the published nested construction the elementary size exclusions alone give exponent $(3-\sqrt5)/2$. The higher exponent $\sqrt2-1$ uses deletion of certain large prime labels, estimated by counting divisors (Section 2.4). The following obstruction concerns **only individual congruence size tests**.

## Moving the active digits

Normalize the large level's available logarithmic digit budget to 1 and the small one's to $r\le1$. A digit has weight equal to the logarithm of its prime modulus in these units. All small-level positions are physically available by the large scale, while the active sets can be arbitrary. Assume label size bounds have logarithms $c$ and $cr$, respectively, and both levels use the same elementary product test internally: for two active labels in the same level, the active modulus product covers the range of their products. Thus their active weights are at least $2c$ and $2cr$. All comparisons are of leading exponents. Subleading factors do not affect the strict inequalities below.

Write $u,v,w$ for the common, large-only, and small-only weights. The union fits in budget 1. Therefore

$$
u\le r,\qquad v\le 1-2cr,\qquad w\le 1-2c.
$$

To exclude mixed collisions purely by comparing one modulus to the maximum possible difference would require $u$ to reach $c(1+r)$ for products, $v$ to reach $c$ for large labels, or $w$ to reach $cr$ for small labels. Now choose $r=1/\sqrt2$ and $c>\sqrt2-1$. All three tests fall strictly short:

$$
r<c(1+r),\qquad 1-2cr<c,\qquad 1-2c<cr.
$$

Thus no rearrangement of the active positions supplies even one of these three certificates at that pair of scales under the stated budgets. In a schedule with log-size proportional to the square of the level index, the small-to-large log-size ratio can approach this value by rounding the smaller index. The conclusion also holds for those rounded pairs for sufficiently large indices. This does not prove there are actual collisions or put an upper bound on the density after deletion. Methods that exploit the congruences jointly, narrow label differences, or use another same-level certificate are outside the argument.

## Recover the candidate large primes from a pair of small primes

Return to nested masks and put $Q=UV$. Exclude primes used as digit moduli from the labels. Given $s<z$, compute by CRT the unique $0\le t<Q$ with

$$
t\equiv z/s\pmod U,\qquad t\equiv1\pmod V.
$$

A candidate must have $p\equiv th\pmod Q$. If all large labels are bounded by $X$ with $X^2<Q$, at most one ordered pair of distinct large primes fits. Indeed the determinant of two putative solutions is divisible by $Q$ and has absolute value less than $X^2$. Its vanishing identifies the reduced fractions.

Under the slightly stronger $2X^2<Q$ we can find that pair by the ordinary continued fraction of $t/Q$. For a genuine solution, $j=(th-p)/Q$ is an integer and $|t/Q-j/h|=p/(Qh)<1/(2h^2)$. Also $j/h$ is reduced because a common divisor would divide $p$ and $h$. Legendre's continued-fraction criterion makes $h$ a convergent denominator. Recover $p$ as the residue of $th$ and test both labels for membership. This takes $O(\log Q)$ continued-fraction steps per small pair. Cilleruelo's fixed $c<1/2$ leaves sufficient slack for $2X^2<Q$ at large levels.

Finally compare the actual encoded sums. For a fixed modular product, at a shared position a pair of digits can have at most two possible integer sums: the digit interval has $q-1$ consecutive values, and the sum is known modulo $q-1$. In the large-only positions the single digit is determined by its residue. A CRT match can therefore fail the integer-sum test.

The script compares reconstruction with exhaustive enumeration of **all** modular matches and separately counts repeated integer sums. The examples are small diagnostic layers chosen to exercise different outcomes, not samples from the asymptotic distribution of collisions.

| Common moduli | Large-only modulus | Small labels | Large labels | CRT matches | Actual collisions |
|---|---:|---:|---:|---:|---:|
| 101, 103 | 7 | 19 | 20 | 0 | 0 |
| 307 | 7 | 4 | 6 | 1 | 1 |
| 61, 73 | 11 | 14 | 19 | 2 | 1 |

The unproved step toward problem 39 is to control the simultaneously retained primes across infinitely many levels at an exponent above $\sqrt2-1$ and ultimately approaching $1/2$ in one sequence. Uniqueness of a large pair per small pair still leaves quadratically many small pairs to test. [Exact verifier](prime_layers.py)

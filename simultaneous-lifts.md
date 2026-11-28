# Simultaneous height bounds above a prescribed Sidon prefix

Research initiated by **@missionaryj**, with mathematical analysis and verification assisted by OpenAI Codex.

Let $r_1,\ldots,r_s$ in $[0,m)$ be Sidon modulo $m$, including double sums. Fix all $s$ initial marks $1+r_i$. Add marks of the form $1+r_i+mx$ with positive integer heights $x$. Write $E(h)$ for the number of additions through height $h$. This counts the new marks through the integer horizon $m(h+1)$.

**A single lift works at every height through $s^2$.** For all sufficiently large $s$ there is one finite Sidon extension satisfying
$$
 E(h)=h \quad(0\le h\le\lfloor s/2\rfloor),\qquad
 E(h)\gg \frac{\sqrt{s h}}{(\log s)^2}\quad(s\le h\le s^2)
$$
at every integer height in the indicated ranges. The constants are absolute. Between the two ranges monotonicity gives $E(h)\ge\lfloor s/2\rfloor$. Separately, for any prescribed final height $H\ge s$ one can preserve the exact shallow counts and obtain $E(H)\gg\sqrt{sH}$, with a lift depending on $H$.

## How height differences control the construction

Give residue $r_i$ a set of heights $T_i$ containing zero. It suffices that all positive differences within the $T_i$ be distinct across the entire family. Indeed reduction modulo $m$ identifies the unordered pair of residue labels in any sum. Within one label the heights are Sidon. For distinct labels, two different matchings of the height sums would repeat a positive height difference across their two sets.

Conversely, reusing such a difference would violate the integer Sidon condition. If there are $e_i$ additions in column $i$ through height $h$, the $\sum_i\binom{1+e_i}{2}$ within-column differences are distinct integers in $[1,h]$. Hence $E(h)\le h$ and $E(h)^2/s+E(h)\le2h$. This proves exact optimality in the shallow range and bounds the loss in the growing range by a logarithmic factor.

## Construction at every intermediate cutoff

In $b=\lfloor s/2\rfloor$ columns use height pairs $\{0,i\}$, $1\le i\le b$. Assign distinct primes $P\in(s,2s)$ to other columns, leaving any unused columns at height zero. There are $\gg s/\log s$ available primes by the prime number theorem. Use at most $s-b$ of them and distribute them as evenly as possible among the dyadic numbers $d=2^k$ with $64\le d\le s$. Each dyadic level receives $\gg s/(\log s)^2$ columns.

For level $d$ choose a Sidon ruler $R_d$ containing zero, with diameter at most $d/2$ and $|R_d|-1\gg\sqrt d$. For example use the marks $2\ell i+[i^2]_\ell$, $0\le i<\ell$, with an odd prime $\ell$ of order $\sqrt d$ and $2\ell^2\le d/2$. Bertrand's postulate suffices for large $d$, and the bounded small levels can use $\{0,1\}$. In a column with prime $P$ use $T_i=P R_d$. All marks of that column have height at most $s d$.

Two columns with primes $P\ne P'$ cannot repeat a difference. An equality $Pa=P'a'$ would imply $P\mid a'$, but every nonzero rank difference $a'$ is positive and less than $s<P$. Differences in prime columns exceed $b$ and therefore cannot clash with the shallow pairs. These statements hold simultaneously for the entire construction.

For $64s\le h\le s^2$, the largest dyadic $d\le h/s$ satisfies $d>h/(2s)$. The columns at that level alone supply $\gg s\sqrt d/(\log s)^2$ additions. For $s\le h<64s$ the shallow pairs give the stated lower bound. This argument uses the same height sets for every cutoff.

## Reaching any single final height

Again use the $b$ shallow columns and put $k=s-b$. Take a finite Sidon ruler $S\subset[0,kH]$ of size at least $c\sqrt{kH}$ for an absolute $c>0$. Partition it by residue modulo $k$. In each residue class replace a mark by its integer quotient upon division by $k$. Every positive difference within these quotient sets is unique across the family, since multiplying a repeated quotient difference by $k$ would repeat a difference of $S$.

Delete a point from each still-present pair at distance at most $b$. There are at most $b$ such pairs in total. Translate each remaining nonempty set to have minimum zero, and use $\{0\}$ for any empty set. Translations preserve the differences and the largest height stays at most $H$. The deep columns contribute at least $c\sqrt{kH}-b-k$ additions; the shallow ones contribute $b$. When $H/s$ exceeds a sufficiently large absolute constant this gives $E(H)\gg\sqrt{sH}$. For bounded $H/s\ge1$ the shallow additions alone suffice. The same lift attains $E(h)=h$ at every shallow height.

At $s=101$, $H=10{,}000$, the verifier splits a 503-point source ruler and removes 20 points for spacing. The single resulting integer set attains the exact shallow counts at all heights zero through 50 and has 583 marks at the final cutoff. All 170,236 unordered sums, including doubles, are distinct.

## A correction depending on both coordinates

In the [product-ruler extension](incidence-extension.md), keep a whole row of $p$ low marks $u_i$, indexed by $i$ modulo an odd prime $p$. Use high Sidon row labels $v_0=0<v_1<\cdots<v_h$, $h<p$. Allow the mark in cell $(i,j)$ to be
$$
 1+u_i+K(c_{ij}+2t v_j),\qquad 0\le c_{ij}<t,\quad K>2\max_i u_i .
$$
The first row has correction zero. Every later row can add at most $\min(t,p)$ marks, since two equal corrections in a row would form a repeated sum with the two corresponding cells of row zero. This bound is simultaneously attainable in every row.

In row $j>0$, put a mark at $i=j z\bmod p$ with correction $z$ for each $0\le z<\min(t,p)$. An integer sum determines its low-label pair, correction sum, and row-label pair by successive digit decoding. Ambiguity requires a rectangle with equal correction sums along its diagonals. For nonzero rows $j,k$, equality would imply $(j^{-1}-k^{-1})(i-i')=0$ modulo $p$ for its distinct columns $i,i'$, which is impossible. In row zero the distinct corrections in the other row rule it out. For $p=17$, ten later rows and $t=7$, the exact 70 additions give 87 marks with 3,828 distinct unordered sums.

## What remains for H1

These results retain only the original $s$ residue classes modulo $m$. For a base of square-root size $s\asymp\sqrt m$, at height $h=s$ the total count is at most $2s$ while the integer horizon has order $s^3$. Thus even optimal height packing in these fixed classes leaves a power gap in H1. A construction through that transition must populate additional residues or change the encoding. [Exact verifier](simultaneous_lifts.py) · [Original residue bounds](residue-lifts.md)

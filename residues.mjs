// Finite lifts of a modular Sidon set. Run with Node.js 18 or later.
import assert from 'node:assert/strict';

function isPrime(n) {
  if (n < 2) return false;
  for (let k = 2; k*k <= n; ++k) if (n%k === 0) return false;
  return true;
}

function parabolaDigit(i, p) {
  return 2*p*i + (i*i)%p;
}

function verifySums(points, modulus = Infinity) {
  const sums = new Set();
  for (let j=0; j<points.length; ++j) {
    for (let i=0; i<=j; ++i) {
      const sum = (points[i]+points[j])%modulus;
      assert(!sums.has(sum), 'repeated pair sum');
      sums.add(sum);
    }
  }
  return sums.size;
}

for (const q of [43, 101, 211]) {
  const m = 4*q*q;
  const residues = Array.from({length:q}, (_, i) => parabolaDigit(i,q));
  verifySums(residues,m);
  const shortLift = residues.flatMap((r,i) => [r,r+m*(i+1)]);
  verifySums(shortLift);
  assert(Math.max(...shortLift) < m*(q+1));
  assert.equal(shortLift.length,2*q);

  let p = Math.floor(Math.sqrt(q/4));
  while (!isPrime(p)) --p;
  const scalars = Array.from({length:p}, (_, i) => parabolaDigit(i,p));
  verifySums(scalars,q);
  const longLift = residues.flatMap((r,i) => scalars.map(t => {
    const height = t + 2*q*((i*t)%q);
    return r + m*height;
  }));
  assert(Math.max(...longLift) < m*2*q*q);
  const sums = verifySums(longLift);
  console.log({q,p,shortPoints:shortLift.length,longPoints:longLift.length,distinctLongSums:sums});
}

import assert from 'node:assert/strict';

// f=a+bu, with u²=d and coefficients in F_3.
function graph(x, d) {
  const a = x%3, b = Math.floor(x/3);
  return [a,b,(a*a+d*b*b)%3,(2*a*b)%3];
}
for (const d of [0,2]) {
  let best = [];
  for (let mask = 7; mask < 512; mask++) {
    if ((mask & 7) !== 7) continue;
    const inputs = Array.from({length:9},(_,i)=>i).filter(i => mask & (1<<i));
    const points = inputs.map(x => graph(x,d)), sums = new Set();
    for (let i=0; i<points.length; i++)
      for (let j=0; j<=i; j++)
        sums.add(points[i].map((x,k)=>(x+points[j][k])%3).join(','));
    if (sums.size === inputs.length*(inputs.length+1)/2 && inputs.length > best.length)
      best = inputs;
  }
  assert.equal(best.length, d === 0 ? 6 : 9);
  console.log({d, best});
}

// Encode a+b*u as a+3*b in F_9. For the other q the field is prime.
function multiply(x,y,q) {
  if (q!==9) return x*y%q;
  const a=x%3, b=Math.floor(x/3), c=y%3, d=Math.floor(y/3);
  return (a*c+2*b*d)%3 + 3*((a*d+b*c)%3);
}
for (const q of [3,5,7,9,11]) {
  const sizes = Array(q*q).fill(0);
  for (let a=0; a<q; a++)
    for (let b=0; b<q; b++)
      sizes[b*q+multiply(2,multiply(a,b,q),q)]++;
  sizes.sort((a,b)=>b-a);
  const top = sizes.slice(0,q).reduce((x,y)=>x+y,0);
  assert.equal(top,2*q-1);
  console.log({q, top});
}

import assert from 'node:assert/strict';
import {readFileSync, writeFileSync} from 'node:fs';

const witnessFile = new URL('./data/witness.json', import.meta.url);
const checkpoints = [16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576];
const prefix = [5,6,13,17,38,56,73,128,142,162,227,254,280,327,401,515,612,635,657,765,767,844,863,994,1003,1415,1635,1881,1935,1976,2042,2188,2431,2847,2860,2875,2988,3172,3307,3338,3533,3676,3880,4019,4077,4082];

function randomIndex(seed) {
  return limit => {
    seed = (Math.imul(1664525, seed) + 1013904223) >>> 0;
    return Math.floor(seed / 2**32 * limit);
  };
}

function shuffledInterval(lower, upper, random) {
  const values = Array.from({length: upper - lower}, (_, i) => lower + i + 1);
  for (let i = values.length - 1; i > 0; i--) {
    const j = random(i + 1);
    [values[i], values[j]] = [values[j], values[i]];
  }
  return values;
}

function add(value, points, differences) {
  const fresh = new Set();
  for (const point of points) {
    const gap = Math.abs(point - value);
    if (!gap || differences.has(gap) || fresh.has(gap)) return false;
    fresh.add(gap);
  }
  points.push(value);
  for (const gap of fresh) differences.add(gap);
  return true;
}

function searchPrefix() {
  const random = randomIndex(739);
  let bestScore = 0, best;
  for (let run = 0; run < 3000; run++) {
    const points = [], differences = new Set();
    let previous = 0, score = Infinity;
    for (const n of checkpoints.slice(0, 5)) {
      const candidates = shuffledInterval(previous, n, random);
      const target = Math.ceil((0.55 + random(30)/100) * Math.sqrt(n));
      for (const x of candidates) {
        if (n < 4096 && points.length >= target) break;
        add(x, points, differences);
      }
      score = Math.min(score, points.length / Math.sqrt(n));
      previous = n;
    }
    if (score > bestScore) {
      bestScore = score;
      best = points.sort((a,b) => a-b);
    }
  }
  assert.deepEqual(best, prefix);
}

function generate() {
  const points = [], differences = new Set();
  for (const x of prefix) assert(add(x, points, differences));
  for (const n of checkpoints.slice(5)) {
    // Every candidate is above all old points, so new-to-old gaps are distinct.
    const candidates = shuffledInterval(n/4, n, randomIndex(39));
    const available = candidates.filter(x => points.every(a => !differences.has(x-a))).length;
    for (const x of candidates) add(x, points, differences);
    console.log({n, available, retained: points.length});
  }
  writeFileSync(witnessFile, JSON.stringify(points.sort((a,b) => a-b)) + '\n');
}

if (process.argv.includes('--search-prefix')) searchPrefix();
if (process.argv.includes('--generate')) generate();
const points = JSON.parse(readFileSync(witnessFile, 'utf8'));
assert(points.every((a,i) => Number.isSafeInteger(a) && a > 0 && (!i || a > points[i-1])));
assert(points.at(-1) <= checkpoints.at(-1));
const sums = new Set();
for (let i = 0; i < points.length; i++)
  for (let j = 0; j <= i; j++) sums.add(points[i] + points[j]);
assert.equal(sums.size, points.length * (points.length+1)/2);
assert.deepEqual(checkpoints.map(n => points.filter(x => x<=n).length), [3,6,12,25,46,74,123,208,346]);
console.log('Distinct unordered sums including doubles:', sums.size);

// Balanced occupancy minimizes the number of within-bin pairs at fixed total.
function minimumPairs(total, bins) {
  const base = Math.floor(total / bins);
  return bins * base * (base-1)/2 + (total % bins) * base;
}

const last = checkpoints.at(-1), start = last/4;
const old = points.filter(x => x<=start), gaps = [];
for (let i = 0; i < old.length; i++)
  for (let j = 0; j < i; j++) gaps.push(old[i]-old[j]);
gaps.sort((a,b) => a-b);
let consumed = 0, best = {bound: Infinity};
for (let width = 1; width <= last-start; width++) {
  while (consumed < gaps.length && gaps[consumed] < width) consumed++;
  const budget = width-1-consumed, bins = Math.ceil((last-start)/width);
  let low = 0, high = last-start+1;
  while (high-low > 1) {
    const mid = Math.floor((low+high)/2);
    if (minimumPairs(mid,bins) <= budget) low = mid;
    else high = mid;
  }
  if (low < best.bound) best = {bound: low, width, bins, consumed, budget};
}
assert(best.bound >= points.length-old.length);
console.log('Best single-width cap on last-stage additions:', best);

// Count ordered collisions among x+i, x new, 1 <= i <= h.
let seen = 0, gapSum = 0, translated = {bound: Infinity};
for (let h = 1; h <= last-start; h++) {
  while (seen < gaps.length && gaps[seen] < h) gapSum += gaps[seen++];
  const span = last-start+h-1;
  const slack = h*(h-1)-2*(seen*h-gapSum);
  // All products below are evaluated as integers at the boundary using BigInt.
  const root = (span/h + Math.sqrt((span/h)**2+4*span*slack/h**2))/2;
  const cap = Math.floor(root);
  if (cap < translated.bound) translated = {bound:cap, h, slack, span};
}
const {bound,h,slack,span} = translated;
function feasible(t) {
  return (BigInt(h)*BigInt(t))**2n <= BigInt(span)*(BigInt(t)*BigInt(h)+BigInt(slack));
}
assert(feasible(bound) && !feasible(bound+1));
assert(bound >= points.length-old.length);
console.log('Translated-interval cap on last-stage additions:', translated);

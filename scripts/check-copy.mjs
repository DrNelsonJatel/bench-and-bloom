// Build-time product-claim guard for benchandbloom.com.
//
// The bottled syrup is an ACIDIFIED (~pH 2.3), high-Brix, SHELF-STABLE product:
// it pours deep ruby and blooms lavender violet in milk. It is NOT the blue,
// refrigerated, four-ingredient 1:5 syrup the site originally described.
// Any build that reintroduces a retired claim fails here rather than shipping.
//
// The anchor how-to is exempt from the colour rules on purpose: it teaches a
// home 1:1 recipe with no acid, which genuinely does set blue and bloom pink.
import { readFileSync, readdirSync, statSync, existsSync } from 'node:fs';
import { join, sep } from 'node:path';

const DIST = 'dist';
const ANCHOR = ['recipes', 'how-to-make-lavender-simple-syrup'].join(sep);

const walk = (d) => readdirSync(d).flatMap((f) => {
  const p = join(d, f);
  return statSync(p).isDirectory() ? walk(p) : p.endsWith('.html') ? [p] : [];
});

// [id, regex, appliesToAnchorPage]
const FORBIDDEN = [
  ['bottle-described-as-blue',
   /pours? (a )?(clean |vivid |deep )?blue|it is a deep blue|stays? (a )?(vivid |striking )?blue|natural (deep )?blue/i, false],
  ['citrus-colour-change',
   /bloom\w*\s+(it\s+)?(to|from blue to)\s+pink|turns? it pink|blue to (sunset )?pink/i, false],
  ['retired-sunset-pink', /sunset[- ]pink/i, true],
  ['wrong-ingredient-count', /four[- ]ingredient|Four ingredients/i, false],
  ['refrigeration-claim', /keep refrigerated|garder au froid/i, true],
  ['stale-launch-date', /mid-July|available mid/i, true],
  // regulated / disallowed claims carried from the label spec
  ['disallowed-origin-claim', /\bProvence\b|French lavender/i, true],
  ['disallowed-regulated-claim', /\borganic\b|100% natural/i, true],
  // CFIA origin rules: cane sugar is ~65% of this product by mass and is not grown
  // in Canada, so "Product of Canada" fails the 2% non-Canadian test. The correct
  // claim is "Made in Canada from domestic and imported ingredients".
  ['disallowed-origin-product-of-canada', /Product of Canada|Produit du Canada/i, true],
  // Brix and pH are calculated, not measured (product spec open items 4 and 5).
  // No public preservation claim until a refractometer and pH meter confirm them.
  ['unverified-preservation-claim', /shelf[- ]stable|ambient[- ]stable|does not need refrigerat/i, true],
  // The proprietor's home address must never be published. The dealer address on
  // label and site is the FARM: 3820 Partridge Rd, Naramata BC V0H 1N1.
  ['home-address-must-not-ship', /Bernard\s*Ave|V1Y\s*6P7/i, true],
];

const REQUIRED = [
  ['lavender-milk page built', () => existsSync(join(DIST, 'recipes', 'lavender-milk', 'index.html'))],
  ['five ingredients disclosed on /syrup', () =>
    /five ingredients/i.test(readFileSync(join(DIST, 'syrup', 'index.html'), 'utf8'))],
  ['citric acid disclosed on /syrup', () =>
    /citric acid/i.test(readFileSync(join(DIST, 'syrup', 'index.html'), 'utf8'))],
  ['anchor discloses how the bottle differs', () =>
    /How our bottle differs/.test(readFileSync(join(DIST, ANCHOR, 'index.html'), 'utf8'))],
  // Grosso is positioned on TASTING NOTES (earthy and warm, less floral), not on
  // essential-oil content: the oil framing risked reading against the standing
  // "no essential oils" line on the same page. Keep that clean-label claim pinned.
  ['no-essential-oils claim still on /syrup', () =>
    /never add extracted essential oil|no essential oils/i.test(readFileSync(join(DIST, 'syrup', 'index.html'), 'utf8'))],
];

let fails = 0;
const pages = walk(DIST);
console.log(`copy-guard: scanning ${pages.length} pages`);

// The anchor's own card text is rendered on the recipes hub too, so exempting
// the anchor PAGE is not enough. A match is also allowed when its immediate
// context carries one of these home-recipe markers.
const HOME_RECIPE_MARKERS = [/to make at home/i, /made differently/i, /How our bottle differs/i];
const isHomeRecipeContext = (text, index) => {
  const ctx = text.slice(Math.max(0, index - 160), index + 160);
  return HOME_RECIPE_MARKERS.some((m) => m.test(ctx));
};

for (const [id, re, anchorToo] of FORBIDDEN) {
  const hits = [];
  const rx = new RegExp(re.source, re.flags.includes('g') ? re.flags : re.flags + 'g');
  for (const p of pages) {
    if (!anchorToo && p.includes(ANCHOR)) continue;
    const t = readFileSync(p, 'utf8');
    for (const m of t.matchAll(rx)) {
      if (!anchorToo && isHomeRecipeContext(t, m.index)) continue;
      hits.push(`${p}: "${m[0]}"`);
    }
  }
  if (hits.length) { fails++; console.error(`  FAIL ${id}`); hits.slice(0, 5).forEach((h) => console.error(`       ${h}`)); }
  else console.log(`  ok   ${id}`);
}

for (const [id, fn] of REQUIRED) {
  let ok = false;
  try { ok = fn(); } catch { ok = false; }
  if (ok) console.log(`  ok   ${id}`); else { fails++; console.error(`  FAIL ${id}`); }
}

// internal /recipes/* links must resolve
const missing = new Set();
for (const p of pages) {
  for (const m of readFileSync(p, 'utf8').matchAll(/href="(\/recipes\/[a-z0-9-]+)"/g)) {
    if (!existsSync(join(DIST, m[1].slice(1), 'index.html'))) missing.add(m[1]);
  }
}
if (missing.size) { fails++; console.error(`  FAIL broken-recipe-links: ${[...missing].join(', ')}`); }
else console.log('  ok   broken-recipe-links');

if (fails) { console.error(`\ncopy-guard: ${fails} failure(s). Build blocked.`); process.exit(1); }
console.log('\ncopy-guard: all checks passed.');

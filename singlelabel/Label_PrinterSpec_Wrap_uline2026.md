# Bench & Bloom — Single Wrap Label Printer Spec (uline2026)

Hand this file **plus `Label_benchandbloom_Final_uline2026_Wrap.svg`** to the label printer
(StickerYou / Jukebox / Avery WePrint / a local trade printer). The `.png` / `.jpg` in this folder
are **previews only** — print from the **SVG** (vector, infinite resolution).

This replaces the old two-label set. **Why one wrap:** without a benchtop labeller, getting two
separate labels square and aligned on opposite faces by hand is fiddly. A single wrap is applied in
one motion — line up the top edge, roll the bottle once — so it's the right call for a hand-applied
pilot run.

---

## The bottle
- **Uline S-23397** — 8 oz Clear Boston Round glass, neck finish **28-400**.
- Height 5.437″ · body diameter **2.375″** · **circumference 7.46″** · straight **label panel 3.125″ tall**.
- Tamper band: **Uline S-17668** black shrink band (55 × 28 mm) over the cap/neck, **above** the label.

## Label size & geometry
- **Trim: 7.25″ W × 2.75″ H** (single piece, wraps the bottle).
- **Bleed: 0.125″** all sides → **artwork / cut sheet 7.5″ × 3.0″**.
- **Safe margin: 0.125″** inside trim — all text/logo/barcode are kept inside it.
- **Wrap math:** 7.25″ label on a **7.46″** circumference leaves a **~0.21″ vertical window of bare
  glass** where the two ends approach each other. This is **intentional and good**:
  1. the violet syrup still peeks through (the colour-change is the product's hook), and
  2. the ends **never need to butt or overlap precisely** — so hand application is forgiving (no
     labeller, no registration headache, no wrinkled seam).
- **Height:** 2.75″ centres in the 3.125″ straight panel with ≈ 0.19″ clearance top and bottom.
- The file is built at final size. **Magenta dashed = trim, cyan dashed = safe.** Two faint green
  dashed verticals mark where the wrap curves front↔back (front panel framed by the gold rules).
  **Delete the `#guides` layer before printing** (or tell the printer they're non-printing).

## Dating, logo & extras (2026 pilot)
- **Front logo** = the official outlined **Bench & Bloom** lockup (sprig + wordmark + descriptor),
  embedded as vector — fully font-independent. The descriptor reads the brand-canonical
  **"NARAMATA BENCH BOTANICALS"** (regenerated as outlined Inter; the old logo art said
  "Lavender · Naramata Bench" — now corrected here and in `public/brand/logo-*.svg`).
- **Best-before convention = 12 months.** Pilot batch: **Packaged 2026 07 01 → Best before 2027 07 01**
  (`YYYY MM DD`, bilingual) + **LOT 2026-001**. Driven by **butterfly-pea colour fade**, not safety
  (high-sugar + hot-fill is shelf-stable far longer); 12 months protects the blue→pink feature. Stamp
  the real packaged/best-before dates + lot per batch.
- **Ingredients (4, current product):** sugar, water, lavender (*Lavandula* ×*intermedia* 'Grosso'),
  butterfly pea flower (*Clitoria ternatea*) — bilingual, descending by weight, binomials italicised.
  Clean-label trio stated: **no essential oils, no artificial colour, no synthetic flavour.**
- **QR code** (left wing, beside the UPC) → `benchandbloom.com/recipes/naramata-sunset` (the
  colour-change signature serve). 33-module symbol with a 4-module quiet zone; keep it ≥ 11 mm square
  in print and do **not** recolour or crop the quiet zone, or it may not scan.

## Layout (how it reads on the bottle)
- **Centre = FRONT / Principal Display Panel:** sprig mark, "Bench & Bloom", descriptor, common name
  (EN + FR), tasting line, net quantity. Framed by two thin gold rules.
- **Right wing → curves to the back:** Nutrition Facts, ingredients (EN/FR), how to use.
- **Left wing → curves to the back:** provenance story, best-before/lot, "Prepared for" address,
  website, Product of Canada, **UPC barcode**.
- The two wings meet at the **rear seam/window**. Orient the bottle PDP-forward when applying.

---

## Material, stock & colour  (what to actually order)

**Face stock — order this:**
- **Soft-matte / cream BOPP film** (bi-axially-oriented polypropylene). **Waterproof and oil/
  moisture-resistant** — this bottle lives in a fridge, sweats with condensation, and gets handled
  with wet hands. Paper stock will cockle, wick, and tear; **do not use paper.**
- **Slight cream/natural tint preferred** over bright optic-white — it flatters the `#F7F3EE` chalk
  ground and reads premium/editorial, not crafty. If the printer only offers white BOPP, that's
  fine because the artwork carries its own chalk ground edge-to-edge (full-bleed `#F7F3EE`).
- **Avoid glossy white film** — it cheapens the wine-country positioning and fights the matte brand.

**Adhesive:**
- **Permanent, clear, glass-rated, cold/wet-resistant** (a "fridge/freezer-grade" or BS5609-style
  permanent acrylic adhesive). Tell the printer it's **for glass, refrigerated, with condensation.**

**Finish / lamination:**
- **Matte laminate or matte varnish over-coat** — adds scuff/water durability and the tactile
  premium feel. Avoid gloss laminate.
- Optional upgrade if budget allows: **spot-gloss or soft-touch** on the wordmark/sprig only — nice,
  not necessary for the pilot.

**Colour / printing:**
- **Print CMYK** using the brand values in the palette table below. For the lavender, a **spot
  Pantone** (≈ **PANTONE 5275 C / 668 C** family — ask the printer to match `#5A4A78`) gives a more
  consistent, richer violet across runs if they offer spot; CMYK is acceptable for a short pilot run.
- **Resolution:** vector (infinite); any embedded raster ≥ **300 dpi**.
- **Black:** legal/body text prints as the brand **Onyx `#2D2933`** (a rich near-black), not 100% K
  flat black — keeps the warm, editorial tone. Barcode bars must be **true black on white** (below).

**Barcode:**
- Keep the barcode panel **solid black bars on a plain white block** (already built that way). Do
  **not** tint it, reverse it, or shrink it below ~80% — scanners need the quiet zones and contrast.
- The art carries a placeholder rendering of **GTIN 627146286305 (GS1 Canada)**. **[VERIFY]** swap in
  the final scannable barcode from your GS1 GTIN before the run (your printer or a free GS1 generator
  can output a print-ready EPS/SVG at the correct magnification).

**Fonts:**
- **Fraunces** (wordmark + "Lavender Simple Syrup") and **Inter** (everything else). Both free
  (Google Fonts / SIL OFL). **Outline / vectorise all fonts before sending to print**, or supply the
  font files. The mark, rules, and colour fields are already vector.

---

## Full brand palette (CMYK for print)

| Role | Name | HEX | CMYK | Pantone (approx.) |
|---|---|---|---|---|
| **Ground** (label paper) | Chalk White | `#F7F3EE` | 0 / 2 / 4 / 3 | Warm Gray 1 C |
| **Wordmark / headings** | Lavender Deep ("Dark Denim") | `#5A4A78` | 25 / 38 / 0 / 53 | 5275 C |
| Primary accent (sprig buds) | Lavender | `#7C6A9C` | 21 / 32 / 0 / 39 | 666 C |
| Sprig bud highlight | Sprig Violet | `#7E6FA0` | 21 / 30 / 0 / 37 | 666 C |
| **Legal / body text** | Onyx | `#2D2933` | 12 / 20 / 0 / 80 | Black 7 C |
| Secondary text | Ink Soft | `#5A5266` | 12 / 19 / 0 / 60 | Cool Gray 11 C |
| **Rules / eyebrow / accents** | Bench Gold | `#C2A05E` | 22 / 31 / 70 / 4 | 4515 C |
| Gold text (contrast) | Gold Deep | `#7A5E28` | 22 / 41 / 90 / 36 | 4505 C |
| Foliage (sprig stem) | Sage | `#8A9A78` | 26 / 9 / 40 / 16 | 5783 C |
| Cool accent (sparingly) | Lake | `#4F7286` | 65 / 32 / 22 / 8 | 5415 C |

Usage rules carried from the brand guide: **lavender is an accent, never body text**; body text =
Onyx on Chalk; **gold is for thin rules and small accents only** (it cheapens in large fills); lake +
sage are quiet supporting tints.

---

## Regulatory — Canada ✓ built in,  US ⚠ one divergence

The label is built to **Canadian** prepackaged-food rules (SFCR / FDR / CFIA) and is **bilingual
(EN/FR)** throughout. Items below marked **[VERIFY]** must be confirmed before printing via CFIA's
free **Industry Labelling Tool** (inspection.canada.ca) or a food-labelling consultant. **The French
copy is a solid draft — have it professionally verified.**

**Canada — present on the label:**
- ✓ Common name, **bilingual**, on the PDP — "Lavender Simple Syrup / Sirop simple à la lavande"
- ✓ **Net quantity** on the PDP in metric — **250 mL** — **[VERIFY type height** for the PDP area]
- ✓ Ingredient list, **bilingual, descending by weight** — **[VERIFY order against your recipe]**
- ✓ Nutrition Facts table, **bilingual** — **[VERIFY — currently an ESTIMATE]** (see below)
- ✓ Dealer name + principal place of business — "Prepared for … Naramata, BC, Canada V0H 1N0"
      **[VERIFY the civic address is correct]**
- ✓ Best-before + lot code fields (`YYYY MM DD` / `LOT 2026-001`) — **fill in real values per batch**
- ✓ Allergens: sugar/water/lavender/butterfly-pea carry **no priority allergens** → no "Contains"
      line. **[VERIFY]** add "may contain" **only if** shared-equipment cross-contact is real.
- **[VERIFY] Front-of-pack "High in sugars / Élevé en sucres" symbol** — mandatory since Jan 1 2026
      over the sugar threshold; sugars/syrups *may* be exempt, but a flavoured lavender syrup is a
      grey area. **Confirm with CFIA before printing** — if it applies, the symbol goes top-right of
      the PDP and the layout will need a small adjustment.

**United States (FDA) — if you also sell on Amazon.com:**
- ✓ **Net quantity is dual-declared** on the PDP — **"250 mL (8.45 fl oz)"** — satisfies FDA's
      requirement for both metric and US customary, and Canada's metric requirement. (8.45 fl oz is
      the accurate US conversion of a 250 mL fill — not "8 fl oz".)
- ✓ Statement of identity in **English**, ingredient list in English, and name/place of business —
      all present and FDA-acceptable (foreign address with city + country is allowed).
- ⚠ **Nutrition panel is the one genuine conflict.** A **US FDA Nutrition Facts panel** has a
      **different format** from the Canadian one (different reference values, mandatory nutrients,
      "Amount Per Serving", larger "Calories", US daily-value footnote). **One panel cannot be
      simultaneously compliant in both countries.** Two clean options:
  1. **Print the Canadian bilingual table** (as built) and sell on **Amazon.ca**. For **Amazon.com**,
     run a **separate US label variant** with an FDA-format panel. *(I can generate that US variant
     SVG from this file in ~one pass — just say the word.)*
  2. **Carry both panels** (Canadian *Valeur nutritive* + US *Nutrition Facts*) side-by-side on the
     back — fully dual-compliant, but it's tight on a 7.25″ wrap and would mean trimming other back
     copy. Feasible if cross-border from day one matters more than breathing room.
- For the pilot (Amazon.ca first), **option 1 is recommended**: ship the Canadian label now, add the
  US variant when/if you list on Amazon.com.

**Nutrition Facts values are a GENERIC ESTIMATE** (modeled on comparable market syrups: ~50 cal,
~12–13 g sugar per 15 mL). **[VERIFY] — replace with a calculated table** from your actual recipe
quantities + serving size (a recognized nutrition database or a lab CoA). I can draft the real table
once you give me the recipe.

---

## Pre-print checklist
- [ ] **[VERIFY]** all items above in the CFIA Industry Labelling Tool (worth the hour for a real run)
- [ ] Replace estimated Nutrition Facts with a **calculated** table (give me the recipe)
- [ ] Confirm civic address + postal code in "Prepared for / Préparé pour"
- [ ] Drop in the **real scannable barcode** for GTIN 627146286305 (GS1 magnification)
- [ ] Have the **French** professionally verified
- [ ] Decide CMYK vs. spot Pantone for the lavender (ask printer)
- [ ] **Outline the fonts** (Fraunces + Inter) or supply font files
- [ ] **Delete the `#guides` layer** (trim/safe/fold lines) before output
- [ ] Order **soft-matte cream BOPP, permanent glass/fridge adhesive, matte laminate**
- [ ] Print one, **wrap a real bottle**, check the 0.21″ window sits where you want it and the panel
      clears the shrink band

## Files in this folder
- `Label_benchandbloom_Final_uline2026_Wrap.svg` — **the print master** (vector)
- `Label_benchandbloom_Final_uline2026_Wrap.png` / `.jpg` — previews only
- `Label_PrinterSpec_Wrap_uline2026.md` — this spec
